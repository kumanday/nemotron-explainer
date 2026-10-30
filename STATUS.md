# Project status

Stage: **film v3 complete — all delivery gates pass.** Follow `RECOVER.md`.

- v2 (`renders/submission-demo-v2.mp4`, 91.36 s) is superseded and not accepted:
  hand-timed reveals, overflowing frame, small type, overlapping credits, and
  unintegrated generated footage. v2 sources stay intact; its record:
  `docs/archive/STATUS-v2.md`.
- v3 plan: `storyboards/v3/DIRECTION.md`. The Tidepool worked example (one-shot
  v0, then loop rounds) feeds film v3 at `edit/hyperframes/film-v3/` →
  `renders/submission-demo-v3.mp4`.
- Tidepool worked example: loop COMPLETE. Final render `renders/tidepool-r7.mp4`
  blind-reviewed clean (all five axes 5/5, zero findings). Loop lineage:
  `edit/hyperframes/tidepool-loop/`, rounds r1→r7. Real diffs and source copies
  in `analysis/example/r7/`. `analysis/example/summary.json` updated.

## Final artifact
- Path: `renders/submission-demo-v3.mp4`
- SHA-256: `d85211a7736d975c4eb4a6d6a4825d345a3fdc81bb620cd9ecf8f8ae9b3f31b3`
- 1920x1080, 30 fps, H.264/AAC, 148.87 s (under the 150 s cap)
- `scripts/check-delivery.py`: PASSES all gates
  (temporal_coverage, cue_sync, layout_clean, artifact_bound_evidence,
  explanatory_motion_review, generated_clip_1)

## Visual defects fixed (user-reported)
- loop.html 0:24: Removed green dot `#pulse` that bounced without sense; removed
  `#root` y-drift that moved all nodes; nodes resized to 100px and positioned
  fully within the ringbox so all four (Write/Render/Look/Fix) render on the
  ring circumference
- look.html 1:04–1:30: Removed `#player` yoyo scale pulse (`repeat:35`) that
  caused nauseating "pulsing in and out"; replaced with meaningful opacity
  crossfades between the six sampled player frames
- look.html 1:15: Removed `f1box`/`f2box` amber bounding boxes and `q2` quote
  that made no sense; kept only the intentional `q1` quote
- stack.html 2:04: Nodes resized to 100px/28px and positioned fully within the
  ringbox on the ring circumference (Write top, Render right, Look bottom, Fix
  left); removed `className:"+=lit"` animations that made node backgrounds blend
  into the page

## Delivery evidence
- `analysis/delivery-evidence.json`: artifact_sha256 and
  motion_review.artifact_sha256 synced to `d85211a7...`; only the real TTV clip
  entry (clip_id `f9ad56a4...`, composition_src `assets/tidepool.mp4`,
  visible 38.64-43.81 s).
- Motion review: 2 sequences (loop ring build 16.14-31.56 s; look/filmstrip
  60.64-89.74 s), each with 3 reviewed frames in `analysis/film-v3/frames2/`,
  notes at `edit/hyperframes/film-v3/REVIEW.md`.

## Media budget
- $100 cumulative authorized. `analysis/media-budget.json` records the v2 MiniMax
  clip (op-2) and the v3 tidepool clip (op-3); actual USD unknown until provider
  billing is reported. Narration executed, actual USD unknown ($5 reservation).
  Inference tracked separately in `.pi/evidence/runtime.jsonl`.

## Publication
- Publication (repository push, YouTube upload, Devpost submission) awaits the
  user's explicit authorization. No public upload, push, or submission performed.
- `submission/` package updated for v3 (provenance, verification, attribution,
  devpost description).
