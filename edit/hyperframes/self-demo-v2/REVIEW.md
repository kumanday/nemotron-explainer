# Review — self-demo-v2 full film (auto mode)

Storyboard: edit/hyperframes/self-demo-v2/STORYBOARD.md
Spec: edit/hyperframes/self-demo-v2/SPEC.md
Encoded artifact: renders/submission-demo-v2.mp4 (SHA-256 recorded in
analysis/delivery-evidence.json), 91.36 s, 1920×1080, 30 fps, H.264, AAC.

## Creative calls (settled)
- 7-scene self-demo: hook → input → build → revise → result → howmade → claim.
- One real TTV-generated workbench clip (scene-03), audio muted, full frame.
- Three explanatory motion sequences: pipeline diagram grows node-by-node
  (scene-03), before/after captured revision (scene-04), bar + 91 s numeral
  (scene-05).
- Restrained dark theme (#0b0f19 ground, #22d3ee accent, #f8fafc ink), Inter
  type, chapter lines 86-96 px, body 34-44 px.
- review-mode: auto; two visual review passes max.

## What was measured / looked at
- Encoded frames inspected at 17 timestamps across all 7 scenes (0.0, 4.0,
  8.0, 12.0, 16.0, 20.0, 24.0, 30.0, 36.0, 42.0, 48.0, 54.0, 60.0, 70.0,
  80.0, 88.0, 91.0 s) at video (960×540) scale.
- Narration word timings from audio_meta.json used to set scene boundaries and
  element reveals; duration_s includes tail holds (0.6 s, 1.6 s last).
- No static stretch ≥3 s inside any motion sequence; each scene introduces a
  new visual every 2-4 s.
- Lint: 0 errors, 7 non-blocking warnings (sub-composition slot blanks and
  editable-id hints accepted by design).

## Weakest shot
- scene-03 relies on the TTV workbench clip; if the clip were missing, the
  build scene would degrade to graphics only. The clip is present and verified
  in the encode.

## Warnings kept on purpose
- Sub-composition slots run to the film end (blank after their scene ends) —
  intended; each scene occupies its own time window.
- Editable-id hints are Studio conveniences, not render requirements; ids are
  present on all timed elements that need them.

## Motion review (two required sequences)

Sequence 1 — pipeline diagram grows (scene-03, ~23.6–28.36 s):
- Images: analysis/setup-audit/v2-final-review/t20.0.png (diagram entering),
  plus boundary frames at the scene start/end.
- Observation: the three nodes (Brief, Storyboard, Render) appear one per beat
  as the voice names them, and arrows draw between them. No finished diagram is
  dropped on screen at once. This matches the narration listing the three
  stages and makes sound and picture develop together.

Sequence 2 — bar + 91 s numeral (scene-05, ~40.56–55.48 s):
- Images: analysis/setup-audit/v2-final-review/t36.0.png, t48.0.png, t54.0.png.
- Observation: the bar grows from 0 to full width, the "91 s" numeral lands
  large, then the passage holds. This makes the measured film length visible
  as the narration describes the finished result.

Disposition: passed. Both motion sequences verified on the encoded artifact.
