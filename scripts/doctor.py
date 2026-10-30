#!/usr/bin/env python3
"""Read-only local prerequisite check. Never print credential values."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def revision(path):
    result = subprocess.run(["git", "-C", str(path), "rev-parse", "HEAD"], capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else None

def main():
    commands = ["pi", "uv", "node", "ffmpeg", "ffprobe", "hyperframes", "media-generated",
                "media-tts", "media-tts-frames", "media-contact-sheet", "media-timeline-view", "media-verify"]
    credentials = ["NEBIUS_API_KEY", "FAL_API_KEY", "FAL_KEY", "ELEVENLABS_API_KEY",
                   "ELEVENLABS_VOICE_ID_EN", "GEMINI_API_KEY", "OPENAI_API_KEY"]
    report = {"commands": {name: shutil.which(name) is not None for name in commands},
              "credentials_available": {name: bool(os.environ.get(name)) for name in credentials},
              "source_revisions": {"media_tooling": revision("/Users/magos/dev/media-tooling"),
                                   "ttv_pipeline": revision("/Users/magos/dev/kumanday/ttv-pipeline")},
              "media_budget_usd": json.loads((ROOT / "configs/budget.json").read_text())["media_total_authorized"],
              "cloud_rendering": "local only; no cloud profile selected"}
    probe = subprocess.run([sys.executable, str(ROOT / "scripts/tool-locations.py")], capture_output=True, text=True)
    report["tool_locations"] = json.loads(probe.stdout) if probe.returncode == 0 else {"available": False, "next_step": "Run scripts/tool-locations.py directly"}
    print(json.dumps(report, indent=2))
    return 0 if all(report["commands"].values()) and report["credentials_available"]["NEBIUS_API_KEY"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
