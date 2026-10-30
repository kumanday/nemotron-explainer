#!/usr/bin/env python3
"""Small paid inference check: real Pi streaming, tools, and image understanding."""
import json
import os
from pathlib import Path
import struct
import subprocess
import uuid
import zlib

ROOT = Path(__file__).resolve().parents[1]

def png():
    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xffffffff)
    width, height = 240, 120
    row = b"\0" + b"\xff\0\0" * (width // 2) + b"\0\0\xff" * (width // 2)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)) + chunk(b"IDAT", zlib.compress(row * height)) + chunk(b"IEND", b"")

def main():
    if not os.environ.get("NEBIUS_API_KEY"):
        raise SystemExit("NEBIUS_API_KEY is missing; run from a shell that exports it.")
    run_id = "smoke-" + uuid.uuid4().hex[:12]
    folder = ROOT / ".pi/smoke" / run_id
    folder.mkdir(parents=True, mode=0o700)
    fixture, answer = folder / "visual-probe.png", folder / "observed.json"
    fixture.write_bytes(png())
    prompt = (f"Use read to inspect the image at {fixture}. Use write to save a JSON object at {answer} "
              'with keys "left" and "right", each containing the ordinary English name of the color '
              'you visually observe on that half of the image. Then reply DONE. Use only read and write. '
              'Do not inspect any other files. Do not write or explain your private reasoning.')
    command = ["pi", "--approve", "--offline", "--no-context-files", "--no-skills",
               "--no-prompt-templates", "--no-mcp", "--no-extensions", "-e", str(ROOT / ".pi/extensions/nebius.ts"),
               "--provider", "nebius-hackathon", "--model", "nvidia/Nemotron-3.5-Super-VL",
               "--tools", "read,write", "--session-dir", str(ROOT / ".pi/sessions"), "--mode", "json", "-p", prompt]
    log = folder / "private-stream.jsonl"
    with log.open("w") as output, (folder / "private-stderr.txt").open("w") as error:
        log.chmod(0o600)
        try:
            process = subprocess.run(command, cwd=ROOT, env={**os.environ, "NEMOTRON_RUN_ID": run_id},
                                     stdout=output, stderr=error, timeout=240)
            exit_code = process.returncode
        except subprocess.TimeoutExpired:
            exit_code = 124
    ledger = ROOT / ".pi/evidence/runtime.jsonl"
    events = [json.loads(line) for line in ledger.read_text().splitlines() if line.strip()] if ledger.exists() else []
    events = [event for event in events if event.get("run_id") == run_id]
    requests = [event for event in events if event["event"] == "provider_request"]
    assistants = [event for event in events if event["event"] == "assistant_end"]
    tools = [event for event in events if event["event"] == "tool_end"]
    try:
        observed = json.loads(answer.read_text())
    except (OSError, ValueError):
        observed = {}
    checks = {
        "pi_exit_zero": exit_code == 0,
        "expected_route": bool(requests) and all(event.get("provider") == "nebius-hackathon"
            and event.get("model") == "nvidia/Nemotron-3.5-Super-VL"
            and event.get("base_url") == "https://api.tokenfactory.us-north1.nebius.com/v1/" for event in requests),
        "image_sent": any(event.get("image_inputs", 0) > 0 for event in requests),
        "read_tool_completed": any(event["tool"] == "read" and not event["error"] for event in tools),
        "write_tool_completed": any(event["tool"] == "write" and not event["error"] for event in tools),
        "colors_correct": str(observed.get("left", "")).lower() == "red" and str(observed.get("right", "")).lower() == "blue",
        "clean_final_stop": bool(assistants) and assistants[-1].get("stop_reason") == "stop",
        "no_failed_or_truncated_turns": bool(assistants) and all(event.get("stop_reason") in ("stop", "toolUse") for event in assistants),
        "usage_retained": bool(assistants) and all(event.get("usage", {}).get("total_tokens", 0) > 0 for event in assistants),
    }
    report = {"run_id": run_id, "passed": all(checks.values()), "checks": checks,
              "provider_requests": len(requests), "observed": observed,
              "estimated_inference_cost_usd": sum((event.get("usage") or {}).get("estimated_cost_usd") or 0 for event in assistants),
              "private_diagnostics": str(folder.relative_to(ROOT))}
    (ROOT / "analysis").mkdir(exist_ok=True)
    (ROOT / "analysis/bootstrap-smoke.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
