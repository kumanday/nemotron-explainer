# Storyboard — self-demo-v2 (91.36 s self-demo)

Subject: the nemotron-explainer workflow demonstrating itself. One short
Markdown brief becomes a narrated mixed-media film through this same pipeline.
Review mode: auto. Each shot names what changes on screen, when, why it explains
the narration, the source asset, and the expected final state.

## scene-01 — hook (0–8.28 s)
- What the viewer sees: dark ground. Large kinetic title "One brief becomes a
  film" builds word by word (blur 6px→0, opacity 0→1, 0.13 s per word, 0.067 s
  apart), landing dead still at 60-80% of frame width. A sub-line follows at
  2.8 s.
- When: 0.0–8.28 s. Title fully landed by ~1.6 s, holds to 8.28 s.
- Why it explains the narration: the opening line is the premise; the type is
  the only thing on screen so the premise reads immediately.
- Source asset: HyperFrames generated typography (no external media).
- Expected final state: title centred, still, readable at 360 px.

## scene-02 — input (8.28–18.0 s)
- What the viewer sees: a Markdown brief in monospace (Space Mono, 42 px),
  lines appear one at a time with a chapter tag "Input brief".
- When: 8.28–18.0 s.
- Why it explains the narration: the narration says it starts with a short
  Markdown brief; the brief is shown on screen as the input.
- Source asset: HyperFrames generated typography (no external media).
- Expected final state: brief lines readable at 360 px.

## scene-03 — build (18.0–28.36 s)
- What the viewer sees: one real TTV-generated 5.17 s clip (MiniMax H3
  image-to-video, 1080p, audio muted) of a creative workbench, full frame, with
  a chapter label. Then a growing pipeline diagram: three nodes — Brief,
  Storyboard, Render — each appears when the voice names it, with arrows drawing
  between them.
- When: 18.0–28.36 s. Workbench clip plays 18.0–23.17 s; diagram builds
  23.6–28.36 s.
- Why it explains the narration: the narration lists the three stages; each
  stage appears exactly as it is named, so sound and picture develop together.
- Source asset: TTV-generated clip (mounted as a timed <video> content layer)
  + HyperFrames motion graphics.
- Expected final state: encoded clip plays full frame, muted; diagram nodes
  connected by arrows, all labels readable at 360 px.

## scene-04 — revise (28.36–40.16 s)
- What the viewer sees: before/after real captures — tts-run.png ("Before
  review") then after-revise.png ("After revision"), each scaled to fill ~88%
  width with a chapter tag.
- When: 28.36–40.16 s. Before 28.76–34.36 s; after 34.76–40.16 s.
- Why it explains the narration: the narration describes inspecting real frames
  and revising; the captured before/after is the visible evidence of that
  revision.
- Source asset: real tool captures (tts-run.png, after-revise.png).
- Expected final state: both captures legible at 360 px, each held long enough
  to read.

## scene-05 — result (40.16–55.48 s)
- What the viewer sees: a bar grows to 80% width while a large "91 s" numeral
  lands, then a one-line coherent passage holds.
- When: 40.16–55.48 s. Bar grows 40.56–42.36 s; numeral lands at ~42.16 s;
  passage holds 44.16–55.48 s (≥2 s final line).
- Why it explains the narration: the narration describes the finished result;
  the growing bar and landed numeral make "a film of measured length" visible.
- Source asset: HyperFrames motion graphics (bar, number, type).
- Expected final state: bar full width, numeral landed, passage readable and
  still for its final ≥2 s.

## scene-06 — how this film was made (55.48–86.88 s)
- What the viewer sees: a component credit list — Pi, Nemotron 3.5 Super VL on
  Nebius, Media Tooling, TTV, HyperFrames, eleven_v4, no music/SFX — one item
  per beat, each with a role line.
- When: 55.48–86.88 s. Seven items, ~4 s each.
- Why it explains the narration: the narration names each component; each item
  appears as it is named.
- Source asset: HyperFrames generated typography.
- Expected final state: each item readable at 360 px, one at a time.

## scene-07 — claim (86.88–91.36 s)
- What the viewer sees: "This video was created using this tool." at 96 px,
  centred, holds to the end.
- When: 86.88–91.36 s.
- Why it explains the narration: the final claim line is the only thing on
  screen, held ≥2 s.
- Source asset: HyperFrames generated typography.
- Expected final state: claim line large, still, readable at 360 px.

## Narration timing (from audio_meta.json, duration_s includes tail holds)
- hook: 0–8.28 s
- input: 8.28–18.0 s
- build: 18.0–28.36 s
- revise: 28.36–40.16 s
- result: 40.16–55.48 s
- howmade: 55.48–86.88 s
- claim: 86.88–91.36 s
