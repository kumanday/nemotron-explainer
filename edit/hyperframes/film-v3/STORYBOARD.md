# Storyboard — film v3 (140.96 s)

Subject: Nemotron 3.5 Super VL runs a Code2Video-style brief through the one-shot
benchmark condition and through this workflow's render → look → fix loop, on the
same Tidepool brief, and the viewer judges the before and after.
Review mode: auto. Each shot names what changes on screen, on which cue, why it
explains the narration, the source asset, and the expected final state.

Narration timing (from audio_meta.json, duration_s includes tail holds):
- frame 1 board: 0.00–16.44 s
- frame 2 loop: 16.44–32.16 s
- frame 3 brief: 32.16–47.40 s
- frame 4 oneshot: 47.40–61.84 s
- frame 5 look: 61.84–90.12 s
- frame 6 fix: 90.12–105.76 s
- frame 7 result: 105.76–108.44 s
- frame 8 stack: 108.44–127.28 s
- frame 9 ask: 127.28–140.96 s

## scene-01 — board (Frame 1, 0.00–16.44 s)
- What the viewer sees: the Code2Video leaderboard builds from
  briefs/data/code2video-aa-2026-10.json: 27 horizontal bars, Elo at bar ends,
  names left, top 9 rows readable (names 36 px). Bars grow top to bottom with a
  40 ms stagger. On {@last} the camera travels down the list and settles on the
  bottom row, which lights in #ff5a5f: "Nemotron 3 Ultra · 304". On {@rules}
  three chips set in beside it: "1 call", "0 tools", "0 renders seen". Board
  holds still under them.
- When: 0.00–16.44 s. Cues: board (frame start), last (~10 s), rules (~12.5 s).
- Why it explains the narration: the claim (Nemotron 3 Ultra ranked last under
  one-call, no-tools conditions) is shown on the actual leaderboard as it is
  spoken.
- Source artifact: briefs/data/code2video-aa-2026-10.json (Artificial Analysis,
  accessed 2026-10-29).
- Expected final state: bottom row lit amber, three chips beside it, board still.

## scene-02 — loop (Frame 2, 16.44–32.16 s)
- What the viewer sees: an arrow "brief → HTML → video" runs left to right
  (96 px labels). On {@loop} it bends into a ring; four nodes land as each verb
  is spoken: Write → Render → Look → Fix. The ring fills ~55% of frame height on
  the left 7 columns. On {@vl} the Look node opens to show a real sampled frame
  of the v0 render (v0 failed to render, so this shows the one-shot error output
  instead) with the name "Nemotron 3.5 Super VL · reads images". On {@tools} a
  lime pulse travels once around the ring. Ring shrinks into the top stage bar
  for scenes 3–6.
- When: 16.44–32.16 s. Cues: loop, vl, tools.
- Why: the loop (render, look, fix) is the film's central claim; each node
  appears as its verb is spoken.
- Source asset: HyperFrames motion graphics (ring, nodes, arrow); sampled frame
  or error output for v0.
- Expected final state: ring complete, nodes labelled, stage bar docked at top.

## scene-03 — brief (Frame 3, 32.16–47.40 s)
- What the viewer sees: an editor panel (7 columns) types the first 8–10 lines
  of the real briefs/example-tidepool.md in 36 px Space Mono, scrolling, never
  shrinking. On {@clip} a card slides in on the right with the actual TTV tide
  pool clip playing muted, plus a metadata chip from the real TTV result
  (MiniMax H3 Max Turbo, 5 s, 1080p, ~8 fal units/5 s, USD unknown). On {@rest}
  three brief phrases highlight amber as spoken: "rises from the bottom edge",
  "tide curve draws", "headline lands".
- When: 32.16–47.40 s. Cues: clip, rest.
- Why: establishes the example brief and its single generated asset before the
  one-shot vs. loop comparison.
- Source asset: briefs/example-tidepool.md; edit/hyperframes/tideloop-loop
  assets/tidepool.mp4 (TTV result f62d2fa5, clip f9ad56a4).
- Expected final state: editor panel with brief, tide-pool clip card, metadata
  chip, all readable at 360 px.

## scene-04 — oneshot (Frame 4, 47.40–61.84 s)
- What the viewer sees: stage bar "Write" lit. The player (1280×720 panel, 1 px
  rule border, timecode, scrubber, chip "v0 · one shot") arrives center-left.
  Receipt line under it from edit/hyperframes/tidepool-v0/one-shot.json
  (finish_reason=length, 32,768 completion tokens, est. $0.02975, no HTML).
  On {@v0} the player shows the actual error output: "no HTML document found in
  the reply — hit the token limit". On {@look} the player freezes on that error
  output.
- When: 47.40–61.84 s. Cues: oneshot, v0, look.
- Why: the benchmark condition (one call, no tools) and its honest result —
  v0 failed to render, so there is no before-frame, only the error.
- Source asset: edit/hyperframes/tidepool-v0/one-shot.json; error output text.
- Expected final state: player shows the v0 error, receipt line visible, chip
  "v0 · one shot".

## scene-05 — look (Frame 5, 61.84–90.12 s)
- What the viewer sees: stage bar "Render" then "Look" lit. On {@strip} six
  sampled frames from analysis/example/r1/ fly into a filmstrip row; one expands
  into the player. On {@axes} a five-row score panel on the right fills in as
  each axis is spoken, with the real r1 scores (Engagement 4, Prompt-Intent 5,
  Composition 4, Temporal 4, Craft 4). On {@f1}/{@f2} amber boxes draw around
  the regions the review named, with the review's own quote (≤12 words) beside
  each.
- When: 61.84–90.12 s. Cues: strip, axes, f1, f2.
- Why: shows the agent reading its own render and scoring it on the judge's five
  axes, with the real review findings.
- Source asset: analysis/example/r1/*.png frames; edit/hyperframes/tidepool-loop
  /REVIEW-r1.md.
- Expected final state: score panel complete, amber boxes with quotes, frames
  legible at 360 px.

## scene-06 — fix (Frame 6, 90.12–105.76 s)
- What the viewer sees: stage bar "Fix" lit; a lime pulse runs the whole bar
  once. On {@diff} a code-diff shows the real edit (the one-shot wrote nothing,
  so the "fix" is that the loop's first render plays the full eight seconds —
  tide-pool clip inside a phone card, headline on time). On {@rounds} a counter
  ticks r1 with its measured duration (~4 min wall clock). On {@final} the hook
  is announced.
- When: 90.12–105.76 s. Cues: diff, rounds, final.
- Why: the fix is the delta between v0 (no render) and r1 (clean render),
  shown as code-diff + before/after in the player.
- Source asset: analysis/example/summary.json; renders/tidepool-r1.mp4.
- Expected final state: diff legible at 360 px, round counter at r1, player
  ready for the final hook.

## scene-07 — result (Frame 7, 105.76–108.44 s)
- What the viewer sees: the player scales up to full frame (FLIP from its scene
  6 rect, 0.7 s) and the final Tidepool render (renders/tidepool-r1.mp4) plays
  unobstructed, 8 s, with its own look. No overlays until its last second, then
  a lower third: "Final · round 1 · 8.0 s · est. inference tracked separately."
- When: 105.76–108.44 s (voice ~2.7 s; the 8 s render plays inside the scene
  host window).
- Why: the payoff — the loop's output, unobstructed.
- Source asset: renders/tidepool-r1.mp4 (the final loop round).
- Expected final state: full-frame player, tide-pool hook playing, lower third
  at the end.

## scene-08 — stack (Frame 8, 108.44–127.28 s)
- What the viewer sees: the stage bar expands back into the scene-2 ring. Each
  node gets the tool that does it, landing as named: Write/Look/Fix → "Nemotron
  3.5 Super VL · Nebius Token Factory"; Render → "HyperFrames"; the clip card
  from scene 3 docks beside Render → "TTV · MiniMax"; harness label under the
  ring → "Pi". On {@cost} three measured numbers count up (rounds = 1, minutes
  ≈ 4, $ = inference tracked separately), each with a 28 px basis line.
- When: 108.44–127.28 s. Cues: media, cost.
- Why: shows the toolchain that performs the loop.
- Source asset: HyperFrames motion graphics (ring + tool labels); analysis/
  example/summary.json for the counted numbers.
- Expected final state: ring with tool names on each node, numbers counted up.

## scene-09 — ask (Frame 9, 127.28–140.96 s)
- What the viewer sees: the scene-1 board returns at 70% scale; a dashed empty
  row slides in under it: "Nemotron 3.5 Super VL + loop — not scored", no bar,
  no number. On {@ask} the dashed row's outline turns lime. On {@claim} the
  board clears; a claim line at 110 px and the repository URL at 40 px mono,
  held still for ≥2 s past the last word.
- When: 127.28–140.96 s. Cues: ask, claim.
- Why: the honest close — not a benchmark score, a case for tool-aided review;
  the claim line attributes the film.
- Source artifact: briefs/data/code2video-aa-2026-10.json (board, 70% scale).
- Expected final state: dashed not-scored row, then claim line + URL held still
  to the end.

## Honesty rules (from DIRECTION.md)
- Leaderboard numbers come only from briefs/data/code2video-aa-2026-10.json;
  the source line names Artificial Analysis and the access date.
- No Elo, rank, or "beats model X" claims for Nemotron 3.5 Super VL. Show the
  before and after and let the viewer judge.
- If the loop helps on this one brief, the film says it is an example, not a
  result.
- Credits: treatment and brief by human direction; storyboard, script,
  compositions, reviews and revisions by Nemotron 3.5 Super VL in Pi; footage by
  TTV/MiniMax; voice ElevenLabs eleven_v4 via Media Tooling.
