#!/usr/bin/env python3
"""Generate a HyperFrames composition in one model call, with no tools and no render feedback.

This is the Code2Video-style baseline: one request (system prompt + design brief) to the
configured Nebius route, the reply's HTML written to OUT/index.html, and a usage receipt in
OUT/one-shot.json. The reasoning stream is not stored. Our system prompt approximates
benchmark conditions; it is not HeyGen's prompt, and the result is not a benchmark score.

    python3 scripts/one-shot.py --brief briefs/example-tidepool.md \
        --asset edit/hyperframes/tidepool-loop/assets/tidepool.mp4:assets/tidepool.mp4 \
        --out edit/hyperframes/tidepool-v0

Render it afterwards with `hyperframes render OUT --output ...`; do not repair the HTML
first. A render failure is a recorded baseline result.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import time
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def sha(text):
    return "sha256:" + hashlib.sha256(text.encode()).hexdigest()


def extract_html(text):
    fenced = re.findall(r"```(?:html)?\s*\n(.*?)```", text, re.S | re.I)
    for block in fenced:
        if "<html" in block.lower() or "data-composition-id" in block:
            return block.strip() + "\n"
    match = re.search(r"(<!doctype html.*?</html>|<html.*?</html>)", text, re.S | re.I)
    return match.group(1).strip() + "\n" if match else None


def stream(url, key, payload, timeout):
    request = urllib.request.Request(url, data=json.dumps(payload).encode(), method="POST", headers={
        "Authorization": f"Bearer {key}", "Content-Type": "application/json", "Accept": "text/event-stream"})
    content, usage, finish = [], None, None
    with urllib.request.urlopen(request, timeout=timeout) as response:
        for raw in response:
            line = raw.decode("utf-8", "replace").strip()
            if not line.startswith("data:"):
                continue
            data = line[5:].strip()
            if data == "[DONE]":
                break
            event = json.loads(data)
            usage = event.get("usage") or usage
            for choice in event.get("choices", []):
                content.append((choice.get("delta") or {}).get("content") or "")
                finish = choice.get("finish_reason") or finish
    return "".join(content), usage, finish


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--brief", type=Path, required=True)
    parser.add_argument("--system", type=Path, default=Path("prompts/one-shot-system.md"))
    parser.add_argument("--out", type=Path, required=True, help="new composition directory")
    parser.add_argument("--asset", action="append", default=[], metavar="SRC:DEST",
                        help="copy a supplied asset into OUT (DEST is relative to OUT); repeatable")
    parser.add_argument("--max-tokens", type=int, default=32768)
    parser.add_argument("--reasoning-effort", default="medium",
                        help="high spent all 32768 tokens reasoning with no reply on the first Tidepool run")
    parser.add_argument("--timeout", type=int, default=1200)
    parser.add_argument("--smoke", action="store_true", help="send a tiny request to verify the route; writes nothing")
    args = parser.parse_args()

    config = json.loads((ROOT / "configs/nebius.json").read_text())
    model = config["models"][0]["id"]
    url = config["baseUrl"].rstrip("/") + "/chat/completions"
    key = os.environ.get("NEBIUS_API_KEY")
    if not key:
        sys.exit("NEBIUS_API_KEY is not set in the environment")

    if args.smoke:
        payload = {"model": model, "stream": True, "stream_options": {"include_usage": True}, "max_tokens": 600,
                   "messages": [{"role": "user", "content": "Reply with the single word OK."}]}
        text, usage, finish = stream(url, key, payload, args.timeout)
        print(json.dumps({"route": url, "model": model, "reply": text.strip()[:40], "finish_reason": finish, "usage": usage}))
        return

    out = (ROOT / args.out).resolve()
    if out.exists() and any(out.iterdir()):
        sys.exit(f"{out} is not empty; one-shot runs write a new directory each time")
    system = (ROOT / args.system).read_text()
    brief = (ROOT / args.brief).read_text()
    payload = {"model": model, "stream": True, "stream_options": {"include_usage": True},
               "max_tokens": args.max_tokens, "reasoning_effort": args.reasoning_effort,
               "messages": [{"role": "system", "content": system}, {"role": "user", "content": brief}]}

    started = time.monotonic()
    try:
        text, usage, finish = stream(url, key, payload, args.timeout)
    except urllib.error.HTTPError as error:
        sys.exit(f"provider returned HTTP {error.code}: {error.read().decode('utf-8', 'replace')[:400]}")
    elapsed = round(time.monotonic() - started, 1)

    out.mkdir(parents=True, exist_ok=True)
    (out / "reply.md").write_text(text)
    html = extract_html(text)
    if html:
        (out / "index.html").write_text(html)
    for spec in args.asset:
        source, dest = spec.split(":", 1)
        (out / dest).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / source, out / dest)
    price = config["models"][0].get("cost", {})
    estimate = None
    if usage and price:
        estimate = round((usage.get("prompt_tokens", 0) * price.get("input", 0)
                          + usage.get("completion_tokens", 0) * price.get("output", 0)) / 1e6, 5)
    receipt = {
        "schema": "nemotron-demo/one-shot-v1",
        "at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "condition": "one call, no tools, no render feedback",
        "provider": config["provider"], "model": model, "endpoint": url,
        "reasoning_effort": args.reasoning_effort, "max_tokens": args.max_tokens,
        "system_prompt": {"path": str(args.system), "sha256": sha(system)},
        "brief": {"path": str(args.brief), "sha256": sha(brief)},
        "assets": args.asset, "finish_reason": finish, "usage": usage,
        "estimated_cost_usd": estimate, "cost_basis": "token counts x configs/nebius.json list rates; not an invoice",
        "elapsed_s": elapsed, "html_extracted": bool(html),
    }
    (out / "one-shot.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({k: receipt[k] for k in ["finish_reason", "usage", "estimated_cost_usd", "elapsed_s", "html_extracted"]}))
    if not html:
        sys.exit("no HTML document found in the reply; see reply.md (record this as the baseline result)")


if __name__ == "__main__":
    main()
