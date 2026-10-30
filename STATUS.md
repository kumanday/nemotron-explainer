# Project status

Stage: **production incomplete — film v3 in progress.** Follow `RECOVER.md`.

- v2 (`renders/submission-demo-v2.mp4`, 91.36 s) passed the earlier delivery gate
  but is not accepted: hand-timed reveals out of sync with the narration, text
  overflowing the frame, type too small, overlapping credits, and generated footage
  that was not integrated into the composition. The gate has been tightened
  (`cue_sync`, `layout_clean`, `review_axes`, `duration_target`, 5 s hold limit);
  v2 now fails it. v2 sources stay intact. Its record: `docs/archive/STATUS-v2.md`.
- v3 plan: `storyboards/v3/DIRECTION.md`. The Tidepool example (one-shot v0, then
  loop rounds) feeds film v3 at `edit/hyperframes/film-v3/` →
  `renders/submission-demo-v3.mp4`.
- Tidepool worked example: loop COMPLETE. Final render `renders/tidepool-r7.mp4`
  blind-reviewed clean (all five axes 5/5, zero findings). v0 attempt 1 failed
  (token limit, no HTML); v0b attempt 2 succeeded (medium effort, HTML extracted)
  and is the recorded one-shot baseline. r1 self-review was wrong (missed missing
  tide curve, missing label, overlap, cropped phone); blind review caught it.
  Loop lineage: `edit/hyperframes/tidepool-loop/`, rounds r1→r7. Real diffs and
  source copies in `analysis/example/r7/`. `analysis/example/summary.json`
  updated.
- Film v3 slot `edit/hyperframes/film-v3/` exists with STORYBOARD.md, SPEC.md,
  SCRIPT.md, CUES.md, audio_meta.json (9 voices) and all 9 scene compositions
  built. SCRIPT.md currently states the OLD false r1 review result (lines 4–8)
  and must be rewritten from the real record (DIRECTION.md scene 5 beat),
  re-voiced with `media-tts-frames`, then `scripts/cues.py edit/hyperframes/film-v3`.
- Media budget: $100 cumulative. `analysis/media-budget.json` records the v2
  MiniMax clip (op-2) and the v3 tidepool clip (op-3); actual USD unknown until
  provider billing is reported. Narration executed, actual USD unknown ($5
  reservation). Inference tracked separately in `.pi/evidence/runtime.jsonl`.
- Publication awaits user authorization.

Record the actual time at each RECOVER.md checkpoint in `edit/project.md`.
