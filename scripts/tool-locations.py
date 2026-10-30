#!/usr/bin/env python3
"""Locate an installed Python CLI through its interpreter, without filesystem search."""
import json
from pathlib import Path
import shutil
import subprocess

def locations():
    executable = shutil.which("media-generated")
    if not executable:
        raise RuntimeError("media-generated is not on PATH")
    launcher = Path(executable).resolve()
    first = launcher.read_text().splitlines()[0]
    if not first.startswith("#!/") or " " in first[2:]:
        raise RuntimeError("Unexpected interpreter launcher; inspect the located entry point")
    interpreter = first[2:]
    probe = subprocess.run([interpreter, "-c", "import importlib.util,json; print(json.dumps({'generated_media':importlib.util.find_spec('media_tooling.generated_media').origin}))"], capture_output=True, text=True, check=True)
    return {"media_generated_command": executable, "resolved_launcher": str(launcher),
            "python_interpreter": interpreter, "module_sources": json.loads(probe.stdout),
            "media_tooling_checkout": "/Users/magos/dev/media-tooling",
            "ttv_pipeline_checkout": "/Users/magos/dev/kumanday/ttv-pipeline",
            "ttv_helper": "/Users/magos/dev/media-tooling/.agents/skills/media-motion-graphics/scripts/ttv_round.py"}

if __name__ == "__main__":
    print(json.dumps(locations(), indent=2))
