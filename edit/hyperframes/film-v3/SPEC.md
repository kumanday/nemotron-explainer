# Numerical design/motion spec — film v3 (140.96 s)

GOAL: The viewer sees Nemotron 3.5 Super VL run a Code2Video-style brief once
(with no tools) and then through the render → look → fix loop, and judges the
before and after. Built with real artifacts: the AA leaderboard, the Tidepool
brief, the TTV tide-pool clip, the one-shot error output, the r1 review frames,
and the r1 render.

OUTPUT: HyperFrames, 1920×1080, 30 fps, H.264 MP4, 140.96 s, eleven_v4
narration via media-tts-frames, generated-clip audio muted, no music/SFX.

TIME: 140.96 s × 30 fps = 4229 frames. Nine scene hosts, one per narration
frame, hosted at its voice frame's start (data-start/data-duration from
audio_meta.json). Cuts land on scene boundaries; each scene carries its own
voice <audio> window.

LOOK:
- Ground: #0a0e14, panel #131a24, rule #243142, ink #f2f5f8, muted #8d9bb0.
- Agent #c8f560 (lime): the loop, the agent's actions. Flag #ffb020 (amber):
  defects the agent found. Last #ff5a5f: only the Nemotron 3 Ultra row in
  scene 1.
- Type: Inter 800 display, Inter 500 body, JetBrains Mono/Space Mono for code
  and file names. Hero 140–180 px, headline 96–120, body 48–56, label 32–36,
  code 34–40, metadata chips 28 px. Nothing under 32 px except metadata chips.
- Grid: 120 px outer margin, 12 columns. Asymmetric: focal object on 7–8
  columns, text on 4–5. Never everything centred.
- The player: 1280×720 panel (16:9), 1 px rule border (#243142), timecode and a
  scrubber that moves with the clip, a mono chip naming the version. Consistent
  across scenes 4–7.
- The spine: Write → Render → Look → Fix ring, large in scene 2, docked as a
  slim stage bar (y 60–140 px) in scenes 3–6 with the active stage lit in agent
  lime, expanded again in scene 8 with tool names.

OBJECTS:
- Leaderboard: 27 horizontal bars from code2video-aa-2026-10.json, top 9 rows
  readable (names 36 px), Elo at bar ends, 40 ms stagger top to bottom.
- Spine ring: four nodes (Write, Render, Look, Fix), ≥40% of frame height on
  the left 7 columns, arrows between.
- Editor panel: 7 columns, Space Mono 36 px, scrolls the tide-pool brief.
- Tide-pool clip card: the TTV clip (1920×1080, 5.17 s, muted) inside a phone
  or player, never full-frame with a caption.
- Player: 1280×720 panel, chip "v0 · one shot" / "r1 · after one look",
  scrubber, timecode.
- Filmstrip row: six sampled frames from analysis/example/r1/.
- Five-row score panel: Engagement, Prompt-Intent, Composition, Temporal, Craft,
  real r1 scores.
- Amber boxes (SVG stroke draw, 0.5 s) with ≤12-word review quotes.
- code-diff: real edit, 36 px mono, 3–8 lines.
- Round counter: r1 with measured duration.
- Lower third on the final render: "Final · round 1 · 8.0 s · inference tracked
  separately."
- Dashed not-scored row in scene 9: "Nemotron 3.5 Super VL + loop — not
  scored".
- Claim line 110 px, repository URL 40 px mono, held ≥2 s.

MOTION (eases by role):
- Arrival: expo.out / power4.out (0.5–0.8 s, lands slow).
- Camera/object move: power2.inOut.
- Exit: power3.in, 40% shorter than the entrance.
- Text that is read lands and stays still. Kinetic reveals only for hero lines
  of six words or fewer, in sync with the voice.
- One hero move per shot; no breathing/floating loops on titles; no
  fade-and-slide-up on every element; nothing blinks off.
- Cue-timed: every reveal at CUE.name or CUE.name + offset (−0.15 to +0.4 s);
  no bare timeline positions above 0.75 s.

SHOTS (one sub-composition per scene, per STORYBOARD.md):
- scene-01 board: leaderboard builds, last row lit, three chips.
- scene-02 loop: arrow bends to ring, four nodes land, lime pulse, name label.
- scene-03 brief: editor types brief, tide-pool clip card + metadata chip,
  three amber highlights.
- scene-04 oneshot: player arrives, chip "v0 · one shot", receipt line, error
  output shown.
- scene-05 look: filmstrip of six r1 frames, five-row score panel fills, amber
  boxes with quotes.
- scene-06 fix: code-diff, round counter r1, stage bar pulse.
- scene-07 result: player scales full frame, tide-pool-r1.mp4 plays, lower
  third at the end.
- scene-08 stack: ring with tool names per node, numbers count up.
- scene-09 ask: board at 70%, dashed not-scored row, lime outline, claim line
  + URL held to end.

QA (sample the encoded MP4):
- t=8 s: leaderboard top rows readable at 360 px, last row not yet lit.
- t=20 s: ring nodes labelled, Look node shows a frame.
- t=40 s: editor panel brief legible, tide-pool card playing muted.
- t=55 s: player shows v0 error output, receipt line visible.
- t=75 s: score panel filled, amber box with quote.
- t=98 s: code-diff legible, round counter at r1.
- t=107 s: full-frame player, tide-pool clip playing.
- t=118 s: ring with tool names, numbers counted up.
- t=135 s: claim line + URL, both still and readable.

BANNED: hand-timed reveals (bare numbers >0.75 s), text overflowing the frame,
type under 32 px (except 28 px metadata chips), generated footage as a
captioned full-frame insert, credits that overlap, .clip timing on children of
flow layouts, anything that blinks, cutting to an empty ground.
