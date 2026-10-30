#!/usr/bin/env python3
"""Compile a draft from the drafts directory; preserve native immutable outputs."""
import argparse
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]

def prepare(project, draft_path):
    project, draft_path = project.resolve(), draft_path.resolve()
    drafts = project / "rough-cuts/manifests/drafts"
    if not draft_path.is_relative_to(drafts):
        raise ValueError("Save input under rough-cuts/manifests/drafts/. selections/ is CLI output, not an input workspace.")
    draft = json.loads(draft_path.read_text())
    if any(key in draft for key in ["document_sha256", "selection_version", "edl"]):
        raise ValueError("Input is a sealed selection. Reuse it for render; create a plain draft with a new ID for an edit.")
    identifier = draft.get("edit_revision_id", "")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,255}", identifier):
        raise ValueError("Draft requires a valid edit_revision_id")
    output = project / "rough-cuts/manifests/selections" / (identifier + ".json")
    if output.exists():
        canonical = json.loads(output.read_text())
        if not canonical.get("document_sha256"):
            raise ValueError("Output path contains an unsealed draft. Preserve it under drafts/ before running select.")
        if any(canonical.get(key) != value for key, value in draft.items()):
            raise ValueError("This ID already has a different immutable selection. Preserve it and choose a new edit_revision_id.")
        return output, True
    return output, False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("draft", type=Path)
    args = parser.parse_args()
    draft = args.draft if args.draft.is_absolute() else ROOT / args.draft
    try:
        output, existing = prepare(ROOT, draft)
    except (OSError, ValueError) as error:
        raise SystemExit(str(error))
    if existing:
        result = subprocess.run(["media-generated", "validate", "selection", str(output)], capture_output=True, text=True)
        if result.returncode:
            raise SystemExit("Existing selection did not validate; preserve it and inspect the native validator output.")
        print(json.dumps({"selection": str(output.relative_to(ROOT)), "status": "existing_matching_selection_reused"}))
    else:
        result = subprocess.run(["media-generated", "--project", str(ROOT), "select", str(draft)])
        raise SystemExit(result.returncode)
