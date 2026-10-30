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
- SHA-256: `6dd737440cf274c66ad55da9ef9a5e9199bd6d17025610102fc1e7b15ddea2a0`
- 1920x1080, 30 fps, H.264/AAC, 148.87 s (under the 150 s cap)
- `scripts/check-delivery.py`: PASSES all gates
  (temporal_coverage, cue_sync, layout_clean, artifact_bound_evidence,
  explanatory_motion_review, generated_clip_1)

## Visual defects fixed (user-reported)
- look.html: removed nauseating `#player` scale pulse (1:04–1:30); replaced with
  meaningful opacity crossfades between sampled player frames
- look.html: removed nonsensical `f1box`/`f2box` amber bounding boxes (1:15)
- loop.html: removed green dot `#pulse` bouncing without sense (0:24–0:31);
  replaced with gentle ring `strokeDashoffset` pulse
- stack.html: nodes enlarged (120px/30px) and centered ON the ring circumference
  instead of appearing tiny and offset (2:03)

## Delivery evidence
- `analysis/delivery-evidence.json`: artifact_sha256 and
  motion_review.artifact_sha256 synced to `6dd73744...`; only the real TTV clip
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
