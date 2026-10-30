# Numerical design/motion spec — self-demo-v2 (90–120 s self-demo)

GOAL: The viewer understands that a short Markdown brief becomes a narrated
mixed-media film through this same Nemotron + Media Tooling + TTV +
HyperFrames workflow, and sees one real TTV-generated clip plus explanatory
motion sequences that develop across the narrated beats.

OUTPUT: HyperFrames, 1920×1080, 30 fps, H.264 MP4, 91.36 s, narration only
(eleven_v4 via media-tts-frames), generated-clip audio muted, no music/SFX.

TIME: 91.36 s × 30 fps = 2741 frames. No music; cuts land on word boundaries
and scene changes.

LOOK:
- Ground: #0b0f19 (near-black dark), flat solid; no full-screen linear
  gradients (banding under H.264); accent #22d3ee at full saturation on focal
  elements only, 15-25% for atmospheric glows.
- Ink: #f8fafc for all readable text.
- Display face: Inter, 700-900 weight. Chapter lines 86-96 px, held 0.5 s +
  0.3 s per word. Body 34-44 px (3-4% of short side). Labels 22-30 px.
- Monospace "Space Mono" for the input brief at 42 px.
- Medium: dark tech / product UI; real captures where available; one generated
  workbench shot as the invented world.
- Light/depth: radial accent glow 20% opacity, key light upper left, 8%
  vignette, 2% grain.

OBJECTS:
- The brief (a Markdown block, real copy, large, monospace).
- The pipeline diagram: three nodes (Brief, Storyboard, Render) with drawn
  arrows, each node ≥40% of its local cell, labelled in large type.
- The workbench (TTV-generated 5.17 s clip, full frame, muted).
- A grown bar and the "91 s" numeral (bar fills 80% width; numeral 130 px).
- Real captures: tts-run.png and after-revise.png shown scaled to fill ~88%
  width.
- Component credit list (Pi, Nemotron, Media Tooling, TTV, HyperFrames,
  eleven_v4, no music/SFX).

MOTION (eases by role):
- Arrival: expo.out / power4.out (long tail, lands slow).
- Camera/object move: power2.inOut.
- Exit/zoom-through: power3.in (accelerates).
- Exits 40-50% shorter than entrances; overlap: next element starts when
  previous is 30-50% done; stagger words 60-120 ms, list items 40-80 ms.
- One hero move per shot; secondary moves 50-70% as far, start 100-200 ms
  later.
- No fade-and-slide-up for every element; vary entrances. No breathing/floating
  loops on titles. Landed titles stay dead still.

SHOTS:
- scene-01 hook (0–8.28 s): kinetic title "One brief becomes a film" builds
  word by word (blur 6px→0, opacity 0→1, 0.13 s per word, 0.067 s apart),
  sub-line follows. Hero text 60-80% width.
- scene-02 input (8.28–18.0 s): Markdown brief on screen, lines appear one at
  a time, monospace 42 px.
- scene-03 build (18.0–28.36 s): TTV workbench clip (5.17 s, muted, full
  frame) then growing pipeline diagram (three nodes appear one per beat when
  the voice names them; arrows draw between). Explanatory motion sequence 1.
- scene-04 revise (28.36–40.16 s): before/after captures (tts-run.png then
  after-revise.png) scaled to fill, with chapter tags. Explanatory motion
  sequence 2 (the visual revision).
- scene-05 result (40.16–55.48 s): bar grows to 80% width, "91 s" numeral
  lands, passage holds. Explanatory motion sequence 3.
- scene-06 howmade (55.48–86.88 s): component credit list, one item per beat.
- scene-07 claim (86.88–91.36 s): "This video was created using this tool."
  at 96 px, holds to end.
- Something new every 2-4 s; no static stretch ≥3 s inside motion sequences.

BANNED: dark void with small floating elements; glow/bloom/neon as decoration;
purple-blue gradients; glass cards; everything centred; everything fading in at
once; text that moves while read; corner labels; three cards in a row; logo
docked in a corner.

QA:
- t=4.0 s: hook title large, readable at phone width (360 px).
- t=8.0 s: workbench clip playing full frame, muted, label legible.
- t=12.0 s: input brief lines visible, monospace readable.
- t=20.0 s: pipeline diagram nodes appearing with arrows.
- t=30.0 s: after-revise capture visible, readable.
- t=48.0 s: "91 s" numeral large, bar full, passage readable.
- t=70.0 s: howmade component list, one item per beat.
- t=88.0 s: claim line large and still.
