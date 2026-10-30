# Project status

Stage: production complete. M1–M4 verified; delivery gate passes.

- Final artifact: `renders/submission-demo-v2.mp4` (SHA-256
  16e09f137290f55fcf310c8f72f4b8bde04b88943b2cf265a376cd72df82d162),
  1920×1080, 30 fps, H.264/AAC, 91.36 s.
- Contains one real TTV-generated workbench clip (MiniMax H3 image-to-video,
  1080p, audio muted, scene-03 at 18.0–23.17 s) and three explanatory motion
  sequences (pipeline diagram grows node-by-node, before/after captured
  revision, bar + 91 s numeral).
- Narration: media-tts-frames, eleven_v4, 7 voices, 91.36 s; no music/SFX.
- Composition source: `edit/hyperframes/self-demo-v2/` (root has explicit
  `<head><meta charset="utf-8"></head>` per HyperFrames 0.8.142 contract;
  scene styles/scripts inside `<template>`).
- `scripts/check-delivery.py --artifact renders/submission-demo-v2.mp4
  --composition edit/hyperframes/self-demo-v2` PASSES all gates.
- Evidence: `analysis/delivery-evidence.json` (real receipts, hash-bound
  review, two timecoded motion sequences).
- Publication awaits user authorization. EBO optional.
