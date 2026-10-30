#!/usr/bin/env python3
"""Check required hybrid-film evidence. This does not grade artistic quality."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

class Tags(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.tags = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def render_head_present(composition):
    root = composition / "index.html"
    if not root.is_file():
        return False
    tags = [tag for tag, _ in Tags(root.read_text()).tags]
    return "head" in tags and "body" in tags and tags.index("head") < tags.index("body")

def motion_intervals(raw, width=160, height=90, fps=2, threshold=0.2):
    size = width * height
    frames = [raw[i:i + size] for i in range(0, len(raw), size) if len(raw[i:i + size]) == size]
    differences = [sum(abs(a - b) for a, b in zip(left, right)) / size for left, right in zip(frames, frames[1:])]
    intervals, start = [], None
    for i, difference in enumerate(differences + [float("inf")]):
        if difference < threshold:
            if start is None:
                start = i / fps
        elif start is not None:
            end = i / fps
            if end - start >= 3:
                intervals.append({"start_s": start, "end_s": end, "duration_s": end - start})
            start = None
    return intervals

def mounted_sources(composition):
    seen, videos = set(), set()
    def visit(path):
        if path in seen or not path.is_file():
            return
        seen.add(path)
        for tag, attrs in Tags(path.read_text()).tags:
            src = attrs.get("src", "")
            if tag == "video" and src and "://" not in src:
                videos.add((composition / src).resolve())
            child = attrs.get("data-composition-src")
            if child and "://" not in child:
                visit((composition / child).resolve())
    visit(composition / "index.html")
    return videos

AXES = ["Engagement", "Prompt-Intent", "Composition", "Temporal", "Craft"]

def layout_issues(composition):
    """Text overflow and overlap found by `hyperframes check`; these were ignored as warnings in v2."""
    if not (composition / "index.html").is_file():
        return None, "no index.html"
    run = subprocess.run(["hyperframes", "check", str(composition), "--json", "--at-transitions", "--samples", "40"],
                         capture_output=True, text=True, timeout=1800)
    try:
        report = json.loads(run.stdout[run.stdout.index("{"):])
    except ValueError:
        return None, run.stderr[-400:]
    findings = [dict(item, section=section) for section in ["lint", "runtime", "layout", "motion"]
                for item in (report.get(section) or {}).get("findings", [])]
    issues = [i for i in findings if i.get("severity") == "error"
              or "overflow" in i.get("code", "") or "overlap" in i.get("code", "")]
    return issues, report

def check(artifact, composition, evidence_path, min_duration=90, max_duration=150, max_hold=5):
    checks = []
    def add(name, passed, detail):
        checks.append({"name": name, "passed": bool(passed), "detail": detail})
    add("artifact", artifact.is_file(), str(artifact))
    add("render_document_head", render_head_present(composition), "The root index.html needs an explicit head before body so HyperFrames 0.8.142 retains nested scene styles")
    for name in ["STORYBOARD.md", "SPEC.md", "REVIEW.md"]:
        add(name, (composition / name).is_file(), str(composition / name))
    add("design_spec", any((composition / name).is_file() for name in ["frame.md", "design.md", "DESIGN.md"]), "A numerical visual design spec is required")
    digest, duration = None, 0
    if artifact.is_file():
        digest = sha(artifact)
        probe = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type,codec_name,width,height,r_frame_rate", "-of", "json", str(artifact)], capture_output=True, text=True)
        data = json.loads(probe.stdout) if probe.returncode == 0 else {}
        duration = float(data.get("format", {}).get("duration", 0))
        video = next((s for s in data.get("streams", []) if s.get("codec_type") == "video"), {})
        add("delivery_format", video.get("codec_name") == "h264" and video.get("width") == 1920 and video.get("height") == 1080 and video.get("r_frame_rate") in ["30/1", "30000/1000"] and 0 < duration < 180, "H.264, 1080p30, nonempty and under 180 seconds")
        add("duration_target", min_duration <= duration <= max_duration, {"duration_s": duration, "target_s": [min_duration, max_duration]})
        add("narration_stream", any(s.get("codec_type") == "audio" and s.get("codec_name") == "aac" for s in data.get("streams", [])), "An AAC audio stream is required; intelligibility needs review")
        decoded = subprocess.run(["ffmpeg", "-v", "error", "-i", str(artifact), "-vf", "fps=2,scale=160:90,format=gray", "-f", "rawvideo", "pipe:1"], capture_output=True)
        intervals = motion_intervals(decoded.stdout) if decoded.returncode == 0 else []
        longest = max((i["duration_s"] for i in intervals), default=0)
        add("temporal_coverage", decoded.returncode == 0 and bool(decoded.stdout) and longest <= max_hold, {"max_near_static_hold_s": longest, "limit_s": max_hold, "intervals": intervals, "note": "Pixel change detects long holds, not explanatory quality"})
    cues = subprocess.run([sys.executable, str(ROOT / "scripts/cues.py"), str(composition), "--check"], capture_output=True, text=True)
    add("cue_sync", cues.returncode == 0, {"note": "Reveals must use narration cues; run scripts/cues.py SLOT --check",
                                          "errors": [line for line in cues.stdout.splitlines() if line.startswith("error:")][:20]})
    issues, layout = layout_issues(composition)
    add("layout_clean", issues == [], {"note": "No text overflow/overlap or errors in hyperframes check --at-transitions",
                                       "issues": (issues or [])[:20] if issues is not None else layout})
    review_notes = composition / "REVIEW.md"
    text = review_notes.read_text() if review_notes.is_file() else ""
    add("review_axes", all(axis in text for axis in AXES) and "region:" in text,
        "REVIEW.md scores all five axes and records located findings (references/review-rubric.md)")
    evidence = json.loads(evidence_path.read_text()) if evidence_path.is_file() else {}
    add("artifact_bound_evidence", digest is not None and evidence.get("artifact_sha256") == digest, "Evidence must name the actual encoded artifact SHA-256")
    videos = mounted_sources(composition)
    add("video_layer", bool(videos), "Generated footage must be mounted as an actual video content layer")
    footage = evidence.get("generated_footage", [])
    add("generated_footage_evidence", bool(footage), "At least one executed TTV video clip must be included")
    for index, item in enumerate(footage):
        result_path = ROOT / item.get("result", "MISSING")
        source = (composition / item.get("composition_src", "MISSING")).resolve()
        valid = result_path.is_file() and source.is_file() and source in videos
        detail = "Missing TTV result, local source, or mounted video layer"
        if valid:
            validation = subprocess.run(["media-generated", "validate", "result", str(result_path)], capture_output=True, text=True)
            result = json.loads(result_path.read_text())
            clips = [(scene, clip) for scene in result.get("scenes", []) for clip in scene.get("clips", []) if clip.get("clip_id") == item.get("clip_id")]
            valid = validation.returncode == 0 and result.get("result_kind") == "video" and len(clips) == 1
            if valid:
                scene, clip = clips[0]
                attempt = next((a for a in scene.get("attempts", []) if a.get("attempt_id") == clip.get("attempt_id")), {})
                valid = clip.get("asset", {}).get("sha256") == "sha256:" + sha(source) and attempt.get("status") == "succeeded" and bool(attempt.get("provider_request_id"))
                detail = "Validated TTV result, successful provider receipt and source hash must agree"
            start, end = item.get("visible_start_s", -1), item.get("visible_end_s", -1)
            valid = valid and 0 <= start < end <= duration
        add(f"generated_clip_{index + 1}", valid, detail)
    review = evidence.get("motion_review", {})
    sequences = review.get("sequences", [])
    valid_review = review.get("status") == "passed" and digest is not None and review.get("artifact_sha256") == digest and len(sequences) >= 2 and (ROOT / review.get("notes", "MISSING")).is_file()
    for sequence in sequences:
        images = sequence.get("images", [])
        valid_review = valid_review and 0 <= sequence.get("start_s", -1) < sequence.get("end_s", -1) <= duration and len(set(images)) >= 3 and all((ROOT / path).is_file() for path in images) and bool(sequence.get("explanation"))
    add("explanatory_motion_review", valid_review, "Two actual timecoded motion sequences, sampled images, concrete observations and hash-bound review are required")
    return {"passed": all(item["passed"] for item in checks), "artifact_sha256": digest, "checks": checks,
            "limits": "This checks required evidence and obvious omissions. A critical visual and listening review is still required."}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact", type=Path, default=Path("renders/submission-demo-v3.mp4"))
    parser.add_argument("--composition", type=Path, default=Path("edit/hyperframes/film-v3"))
    parser.add_argument("--evidence", type=Path, default=Path("analysis/delivery-evidence.json"))
    parser.add_argument("--output", type=Path, default=Path("analysis/delivery-check.json"))
    parser.add_argument("--min-duration", type=float, default=90)
    parser.add_argument("--max-duration", type=float, default=150)
    parser.add_argument("--max-hold", type=float, default=5, help="longest allowed near-static stretch in seconds")
    args = parser.parse_args()
    report = check((ROOT / args.artifact).resolve(), (ROOT / args.composition).resolve(), ROOT / args.evidence,
                   args.min_duration, args.max_duration, args.max_hold)
    output = ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"passed": report["passed"], "failed_checks": [item for item in report["checks"] if not item["passed"]]}, indent=2))
    raise SystemExit(0 if report["passed"] else 1)
