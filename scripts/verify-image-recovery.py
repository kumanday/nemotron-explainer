#!/usr/bin/env python3
"""Make one inference request from a private copy of a session; never run production."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import uuid

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--session", type=Path, required=True)
    args = parser.parse_args()
    if not os.environ.get("NEBIUS_API_KEY"):
        raise SystemExit("NEBIUS_API_KEY is missing from the calling environment")
    source = args.session.resolve()
    data = source.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    run_id = "image-recovery-" + uuid.uuid4().hex[:12]
    folder = ROOT / ".pi/smoke" / run_id
    folder.mkdir(parents=True, mode=0o700)
    copy = folder / "private-session.jsonl"
    copy.write_bytes(data)
    copy.chmod(0o600)
    command = ["pi", "--approve", "--offline", "--no-context-files", "--no-skills",
               "--no-prompt-templates", "--no-mcp", "--no-extensions", "-e", str(ROOT / ".pi/extensions/nebius.ts"),
               "--provider", "nebius-hackathon", "--model", "nvidia/Nemotron-3.5-Super-VL",
               "--tools", "read", "--session", str(copy), "--mode", "json", "-p",
               "Reply only IMAGE_LIMIT_RECOVERY_OK. Do not continue production, run tools or inspect new files."]
    output = folder / "private-response.jsonl"
    with output.open("w") as stdout, (folder / "private-stderr.txt").open("w") as stderr:
        output.chmod(0o600)
        try:
            result = subprocess.run(command, cwd=ROOT, env={**os.environ, "NEMOTRON_RUN_ID": run_id},
                                    stdout=stdout, stderr=stderr, timeout=180)
            code = result.returncode
        except subprocess.TimeoutExpired:
            code = 124
    events = [json.loads(line) for line in (ROOT / ".pi/evidence/runtime.jsonl").read_text().splitlines() if line.strip()]
    events = [event for event in events if event.get("run_id") == run_id]
    requests = [event for event in events if event["event"] == "provider_request"]
    assistants = [event for event in events if event["event"] == "assistant_end"]
    final = None
    for line in output.read_text().splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if event.get("type") == "message_end" and event.get("message", {}).get("role") == "assistant":
            final = event["message"]
    text = "".join(block.get("text", "") for block in (final or {}).get("content", []) if block.get("type") == "text")
    checks = {
        "pi_exit_zero": code == 0,
        "original_session_unchanged": hashlib.sha256(source.read_bytes()).hexdigest() == digest,
        "over_limit_history_exercised": any(event.get("image_inputs_before_limit", 0) > 8 for event in requests),
        "sent_at_most_eight": bool(requests) and all(event.get("image_inputs", 99) <= 8 for event in requests),
        "omission_recorded": any(event.get("omitted_image_inputs", 0) > 0 for event in requests),
        "expected_route": bool(requests) and all(event.get("provider") == "nebius-hackathon"
            and event.get("model") == "nvidia/Nemotron-3.5-Super-VL"
            and event.get("base_url") == "https://api.tokenfactory.us-north1.nebius.com/v1/" for event in requests),
        "clean_final_stop": bool(assistants) and all(event.get("stop_reason") == "stop" for event in assistants),
        "expected_response": text.strip() == "IMAGE_LIMIT_RECOVERY_OK",
        "production_tools_not_executed": not any(event["event"] == "tool_end" for event in events),
    }
    report = {"run_id": run_id, "passed": all(checks.values()), "checks": checks,
              "request_images": [{"before": event.get("image_inputs_before_limit"), "sent": event.get("image_inputs"),
                                  "omitted": event.get("omitted_image_inputs")} for event in requests],
              "estimated_inference_cost_usd": sum((event.get("usage") or {}).get("estimated_cost_usd") or 0 for event in assistants),
              "private_diagnostics": str(folder.relative_to(ROOT))}
    (ROOT / "analysis/image-limit-recovery.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
