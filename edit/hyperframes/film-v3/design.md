# Film v3 — numerical visual design spec

OUTPUT: HyperFrames, 1920×1080, 30 fps, H.264 MP4, 151.84 s, eleven_v4 narration via media-tts-frames, generated-clip audio muted, no music/SFX.

TOKENS:
- Ground #0a0e14, panel #131a24, rule #243142, ink #f2f5f8, muted #8d9bb0.
- Agent #c8f560 (lime); Flag #ffb020 (amber); Last #ff5a5f (only the Nemotron 3 Ultra row in scene 1).
- Type: Inter 800 display, Inter 500 body, JetBrains Mono / Space Mono for code and file names.
  Hero 140–180 px, headline 96–120, body 48–56, label 32–36, code 34–40, metadata chips 28 px.
  Nothing under 32 px except metadata chips (28 px).
- Grid: 120 px outer margin, 12 columns. Asymmetric: focal object on 7–8 columns, text on 4–5.
  Never everything centred.

OBJECTS:
- Leaderboard: 27 horizontal bars from briefs/data/code2video-aa-2026-10.json, top 9 rows
  readable (names 36 px), Elo at bar ends, 40 ms stagger top to bottom.
- Spine ring: four nodes (Write, Render, Look, Fix), ≥40% of frame height on the left 7 columns.
- Player: 1280×720 panel (16:9), 1 px rule border, timecode, scrubber, mono chip naming the version.
- Tide-pool clip card: the TTV clip (1920×1080, 5.17 s, muted) inside a real phone device (speaker,
  camera, home chrome) and inside the player — never a captioned full-frame insert.
- Filmstrip row: six sampled frames from analysis/example/r7/.
- Five-row score panel: Engagement, Prompt-Intent, Composition, Temporal, Craft, real r1 scores.
- Amber boxes (SVG stroke draw, 0.5 s) with ≤12-word review quotes.
- code-diff: real round-7 edit, 34 px mono.
- Round counter: r7 with measured duration.
- Lower third on the final render: "Final · round 7 · 8.0 s · inference tracked separately."
- Dashed not-scored row in scene 9: "Nemotron 3.5 Super VL + loop — not scored".
- Claim line 110 px, repository URL 40 px mono, held ≥ 2 s.

MOTION (eases by role):
- Arrival: expo.out / power4.out (0.5–0.8 s).
- Object move: power2.inOut.
- Exit: power3.in, 40% shorter than the entrance.
- Text that is read lands and stays still. No breathing/floating loops on titles.
- Cue-timed: every reveal at CUE.name or CUE.name + offset (−0.15 to +0.4 s); no bare timeline
  positions above 0.75 s.

BANNED: hand-timed reveals, text overflowing the frame, type under 32 px (except 28 px chips),
generated footage as a captioned full-frame insert, overlapping credits, .clip children of flow
layouts, anything that blinks, cutting to an empty ground.
