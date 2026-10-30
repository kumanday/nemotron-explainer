#!/usr/bin/env python3
"""Review a render with a fresh Nemotron call that sees only the brief and the frames.

The agent that wrote a composition tends to see its plan in its frames (r1 scored
Prompt-Intent 5 with no tide curve on screen). This reviewer gets no source, no
history and no intent: the brief text and up to eight frames sampled from the
encoded MP4. It must inventory what is literally visible before it compares that
inventory with the brief, scores the five Code2Video axes and writes located
findings. Same model and route as the agent (configs/nebius.json).

    python3 scripts/blind-review.py --brief briefs/example-tidepool.md \
        --render renders/tidepool-r1.mp4 --out analysis/example/r1/blind

Writes OUT/frames/*.jpg, OUT/blind-review.json (parsed), OUT/reply.md (raw) and
OUT/receipt.json (usage). Fix what it finds; do not argue with it in the review file.
"""
import argparse
import base64
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TIMES = "0.5,1.5,2.6,3.4,4.2,5.2,6.4,7.6"

SYSTEM = """You are a strict motion-design reviewer. You receive a design brief and frames
sampled from a rendered 1920x1080 video, each labelled with its timestamp. You did not
make this video and you do not know what its author intended. Judge only the pixels.

Work in this order and return one JSON object in a ```json fenced block, nothing else.

1. "inventory": for every frame, list each visible object with its approximate box in
   1920x1080 pixels and every piece of legible text copied exactly. If two texts overlap,
   say so. If something is cut off by the frame edge, say so. Describe; do not interpret.
2. "brief_check": for every element and timing the brief requires, give
   {"requirement", "status": "present"|"missing"|"wrong", "evidence": "frame t=X: <inventory line>"}.
   A requirement is present only if an inventory line shows it.
3. "scores": integers 1-5 for "Engagement", "Prompt-Intent", "Composition", "Temporal",
   "Craft", each with one sentence of evidence. Any missing brief element caps
   Prompt-Intent at 3. Any overlap, clipping or illegible text caps Craft at 3.
4. "findings": list of {"id", "axis", "severity": "blocker"|"major"|"minor", "time_s",
   "region": {"x","y","w","h"}, "saw", "suggested_fix"}. Missing brief elements are major.
   Overlapping or clipped text is a blocker.
"""


def frames(render, times, out):
    out.mkdir(parents=True, exist_ok=True)
    paths = []
    for t in times:
        path = out / f"t{t}.jpg"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", str(render), "-frames:v", "1",
                        "-vf", "scale=1280:-1", "-q:v", "3", str(path)], check=True)
        paths.append(path)
    return paths


def stream(url, key, payload, timeout):
    request = urllib.request.Request(url, data=json.dumps(payload).encode(), method="POST", headers={
        "Authorization": f"Bearer {key}", "Content-Type": "application/json", "Accept": "text/event-stream"})
    content, usage, finish = [], None, None
    with urllib.request.urlopen(request, timeout=timeout) as response:
        for raw in response:
            line = raw.decode("utf-8", "replace").strip()
            if not line.startswith("data:") or line[5:].strip() == "[DONE]":
                continue
            event = json.loads(line[5:].strip())
            usage = event.get("usage") or usage
            for choice in event.get("choices", []):
                content.append((choice.get("delta") or {}).get("content") or "")
                finish = choice.get("finish_reason") or finish
    return "".join(content), usage, finish


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--brief", type=Path, required=True)
    parser.add_argument("--render", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--times", default=DEFAULT_TIMES, help="comma-separated seconds, at most eight")
    parser.add_argument("--reasoning-effort", default="medium")
    parser.add_argument("--max-tokens", type=int, default=32768)
    parser.add_argument("--retries", type=int, default=4, help="retries on 5xx with 30 s backoff")
    parser.add_argument("--timeout", type=int, default=1200)
    args = parser.parse_args()

    times = [t.strip() for t in args.times.split(",") if t.strip()]
    if len(times) > 8:
        sys.exit("Nebius accepts at most eight images per request")
    config = json.loads((ROOT / "configs/nebius.json").read_text())
    model, url = config["models"][0]["id"], config["baseUrl"].rstrip("/") + "/chat/completions"
    key = os.environ.get("NEBIUS_API_KEY") or sys.exit("NEBIUS_API_KEY is not set in the environment")

    out = (ROOT / args.out).resolve()
    paths = frames((ROOT / args.render).resolve(), times, out / "frames")
    content = [{"type": "text", "text": "Design brief:\n\n" + (ROOT / args.brief).read_text()}]
    for t, path in zip(times, paths):
        content.append({"type": "text", "text": f"Frame at t={t} s:"})
        content.append({"type": "image_url", "image_url": {
            "url": "data:image/jpeg;base64," + base64.b64encode(path.read_bytes()).decode()}})
    payload = {"model": model, "stream": True, "stream_options": {"include_usage": True},
               "max_tokens": args.max_tokens, "reasoning_effort": args.reasoning_effort,
               "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": content}]}

    started = time.monotonic()
    for attempt in range(args.retries + 1):
        try:
            text, usage, finish = stream(url, key, payload, args.timeout)
            break
        except urllib.error.HTTPError as error:
            if error.code < 500 or attempt == args.retries:
                sys.exit(f"provider returned HTTP {error.code}: {error.read().decode('utf-8', 'replace')[:300]}")
            print(f"HTTP {error.code}; retrying in 30 s ({attempt + 1}/{args.retries})", file=sys.stderr)
            time.sleep(30)
    elapsed = round(time.monotonic() - started, 1)

    (out / "reply.md").write_text(text)
    match = re.search(r"```(?:json)?\s*\n(.*?)```", text, re.S) or re.search(r"(\{.*\})", text, re.S)
    review = None
    if match:
        try:
            review = json.loads(match.group(1))
        except json.JSONDecodeError:
            review = None
    if review is not None:
        (out / "blind-review.json").write_text(json.dumps(review, indent=2) + "\n")
    price = config["models"][0].get("cost", {})
    estimate = round((usage.get("prompt_tokens", 0) * price.get("input", 0)
                      + usage.get("completion_tokens", 0) * price.get("output", 0)) / 1e6, 5) if usage else None
    receipt = {"schema": "nemotron-demo/blind-review-v1", "at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
               "model": model, "endpoint": url, "render": str(args.render), "brief": str(args.brief),
               "times_s": times, "reasoning_effort": args.reasoning_effort, "finish_reason": finish,
               "usage": usage, "estimated_cost_usd": estimate, "elapsed_s": elapsed, "parsed": review is not None}
    (out / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    if review is None:
        sys.exit(f"reply had no parseable JSON (finish_reason={finish}); see {out / 'reply.md'}")
    findings = review.get("findings", [])
    print(json.dumps({"scores": {k: (v.get("score") if isinstance(v, dict) else v) for k, v in review.get("scores", {}).items()},
                      "findings": {s: sum(1 for f in findings if f.get("severity") == s) for s in ["blocker", "major", "minor"]},
                      "missing": [c.get("requirement") for c in review.get("brief_check", []) if c.get("status") != "present"],
                      "elapsed_s": elapsed, "estimated_cost_usd": estimate}, indent=2))


if __name__ == "__main__":
    main()
