# Film v3 — director's treatment

Human direction for the submission film, written to be built, reviewed and revised
by Nemotron 3.5 Super VL in this workflow. Nemotron writes STORYBOARD.md, SPEC.md,
SCRIPT.md, every composition and every review from this treatment. Where a line says
**[fill from run]**, use what the worked example actually produced. Never invent it.

## The film in one sentence

Code2Video ranked Nemotron 3 last when every model got one shot with no tools and
no sight of its own render; this film shows Nemotron 3.5 Super VL getting the loop
a human designer uses, render, look, fix, on a real brief, and lets the viewer
judge the before and after.

## What changed from v2, and why

| v2 problem (seen in the encode) | v3 rule |
|---|---|
| Story was "the tool made this video", with nothing at stake | Story is a claim with a test: one-shot vs. loop on the same brief |
| Reveals hand-timed; credits appeared up to 4.5 s before they were spoken | Every reveal sits on a `{@cue}`; `scripts/cues.py --check` gates it |
| Input brief overflowed the frame top and bottom | `hyperframes check` overflow issues block delivery |
| Text at 26–34 px in a mostly empty dark frame | Minimum 32 px; one focal object fills 40%+ of the frame |
| Credits list reflowed and two items overlapped | No `.clip` children in flow layouts; every element exits by tween |
| Terminal screenshots shown at 1:1 (unreadable) | Real artifacts are cropped and pushed in to 3–6 readable lines |
| Generated clip played full frame under a caption, then cut away | Generated footage is a layer inside a designed composition |
| "91 s" bar explained nothing | Every graphic carries information the narration needs |

## Visual system (one look across every scene)

- **Ground** `#0a0e14`, **panel** `#131a24`, **rule** `#243142`, **ink** `#f2f5f8`,
  **muted** `#8d9bb0`. **Agent** `#c8f560` (lime): the loop, the agent's actions.
  **Flag** `#ffb020` (amber): defects the agent found. **Last** `#ff5a5f`: only the
  Nemotron 3 Ultra row in scene 1. The Tidepool example keeps its own navy/teal/sand
  palette, so the viewer can always tell the film from the work it is examining.
- **Type**: Inter 800 for display, Inter 500 for body, JetBrains Mono (or Space Mono)
  for code and file names. Hero 140–180 px, headline 96–120, body 48–56,
  label 32–36, code 34–40. Nothing under 32 px except metadata chips (28 px).
- **Grid**: 120 px outer margin, 12 columns. Layouts are asymmetric: the focal object
  on 7–8 columns, text on 4–5. Never everything centred.
- **The spine**: the loop diagram **Write → Render → Look → Fix ↺** is the film's
  recurring object. Built large in scene 2; docked as a slim stage bar across the
  top (y 60–140 px) in scenes 4–6, with the active stage lit in agent lime and the
  others muted; expanded again in scene 8 with tool names attached.
- **The player**: every render of the example plays inside one consistent player:
  a 1280×720 panel (16:9), 1 px rule border, timecode and a scrubber that moves
  with the clip, a mono chip naming the version ("v0 · one shot", "r2 · after
  two looks"). The player is how the viewer knows they are looking at output.
- **Motion**: arrivals `expo.out`/`power4.out` 0.5–0.8 s; moves `power2.inOut`;
  exits `power3.in`, 40% shorter than the entrance. Text lands and stays still
  while it is read. Scene changes carry an object across the cut (the spine,
  the player) or use one registry transition; no cut to an empty ground.

## Registry blocks to start from

Install with `hyperframes add NAME` inside the slot, then restyle to the tokens
above. Search with `hyperframes catalog WORDS` before hand-building anything else.

- `data-chart` or `bar-chart-race`: the leaderboard (scene 1, scene 9).
- `code-typing`: the brief typing into the editor (scene 3).
- `browser-device-stage`: chrome for the player, if it saves work.
- `mk-placeholder-grid`: the filmstrip of sampled frames (scene 5).
- `code-diff`: the agent's real edit (scene 6).
- `before-after-wipe`: same frame, v0 vs. final (scene 6).
- `cinematic-zoom` or `light-leak`: at most two scene transitions in the film.

## Shots

Target 100–120 s. Each scene is one narration frame in SCRIPT.md, one
sub-composition, starting where its voice starts. The narration below is a draft:
keep the cue names, tighten the words, and replace every **[fill from run]**
with what really happened. Read it aloud; cut anything that only describes the
screen.

### 1 · The board (≈12 s) — `board`

> {@board}Artificial Analysis just ranked twenty-seven models on Code2Video. Each
> one writes a HyperFrames composition, it gets rendered, and a judge compares the
> videos. {@last}Nemotron 3 Ultra came last. {@rules}Every model had one call: no
> tools, and no look at its own render.

- `board`: the leaderboard builds from `briefs/data/code2video-aa-2026-10.json`:
  27 horizontal bars, Elo values at the bar ends, names left. Bars grow top to
  bottom with a 40 ms stagger; the frame shows the top 9 rows at readable size
  (names 36 px).
- `last`: the camera (a transform on the board group) travels down the list,
  power2.inOut over 1.6 s, and settles on the bottom rows. The last row lights
  in `#ff5a5f`: "Nemotron 3 Ultra · 304".
- `rules`: three chips set in beside the last row, one per spoken phrase:
  "1 call", "0 tools", "0 renders seen". Board holds still under them.
- Out: the last row's bar shrinks into a single straight arrow that scene 2 uses.
- Source: AA article accessed 2026-10-29 (cite it in a 28 px source line).

### 2 · The loop (≈12 s) — `loop`

> {@line}Nobody designs motion graphics that way. {@loop}You render, you look at the
> frames, and you fix what's wrong. {@vl}Nemotron 3.5 Super VL can read images, so
> we gave it that loop: {@tools}a harness, render tools, and its own render to look at.

- `line`: the arrow from scene 1 runs left to right: "brief → HTML → video", 96 px
  labels, a single pass.
- `loop`: the arrow bends into a ring; four nodes land as each verb is spoken
  ("render", "look", "fix", with "Write" already there): Write → Render → Look → Fix.
  The ring fills 55% of frame height on the left 7 columns.
- `vl`: the Look node opens to show a real sampled frame of the v0 render inside it
  (a frame Nemotron actually read). Name on the right: "Nemotron 3.5 Super VL",
  label "120B total · 12B active · reads images" (verify these figures on Nebius'
  model page before using them; drop the line if unverified).
- `tools`: one lime pulse travels once around the ring. Ring shrinks into the
  top stage bar for scenes 3–6.

### 3 · The brief (≈11 s) — `brief`

> {@brief}So here's a brief in the Code2Video style: an eight-second launch hook for
> Tidepool, a made-up tide app. {@clip}It comes with one generated clip of a tide pool.
> {@rest}Everything else, the phone, the tide curve, the type, has to be built in code.

- `brief`: an editor panel (7 columns) types the real `briefs/example-tidepool.md`
  with `code-typing`, at 36 px mono. Show only the first 8–10 lines that fit;
  scroll, never shrink.
- `clip`: a card slides in on the right with the actual TTV clip playing muted,
  plus a metadata chip from the real TTV result: provider/model, 5 s, 1080p,
  quoted cost. This is the generated footage's first appearance, as an asset.
- `rest`: three phrases in the brief highlight amber as they are spoken
  ("rises from the bottom edge", "tide curve draws", "headline … lands").

### 4 · One shot (≈12 s) — `oneshot`

> {@oneshot}First, the benchmark condition: one call, no tools. {@v0}This is what
> Nemotron 3.5 Super VL wrote on its first try. {@look}[fill from run: "It renders,
> but look at the headline." / "It didn't render at all." Say what is true.]

- Stage bar: "Write" lit.
- `oneshot`: the player arrives center-left; chip "v0 · one shot"; receipt line
  under it from `one-shot.json` (tokens, seconds, est. cost).
- `v0`: the real v0 render plays in the player, all 8 s, scrubber moving.
  If v0 failed to render, show the actual error output in the player instead.
- `look`: the player freezes on the frame the review found worst.

### 5 · Look (≈18 s) — `look`

> {@strip}Now the loop. The agent samples frames from its own render and reads them
> like it reads text. {@axes}It scores them on the judge's five axes: engagement,
> prompt intent, composition, timing, and craft. {@f1}[fill from run: finding one,
> in plain words.] {@f2}[fill from run: finding two.]

- Stage bar: "Render" then "Look" lit.
- `strip`: six frames the agent actually read (`analysis/example/r0/` frames) fly
  into a filmstrip row; one expands into the player.
- `axes`: a five-row score panel on the right fills in as each axis is spoken,
  with the agent's real 1–5 scores from `REVIEW-r1.md` (its review of v0).
- `f1`, `f2`: amber boxes draw (SVG stroke draw, 0.5 s) around the regions the
  review named, using its pixel coordinates scaled into the player; a quote of the
  agent's own finding (≤ 12 words) sets beside each box.
- **The honest twist (use it; it happened):** the agent's first self-review of r1,
  written with its own plan in context, scored Prompt-Intent 5/5 while the tide
  curve was missing and the wordmark sat on the headline. A blind review (same
  model, fresh call, only the brief and the frames) found both. Show the two score
  panels side by side: "self-review" vs. "blind review", same frames. Narration
  draft: "{@self}Its first look went wrong: it saw the plan, not the pixels.
  {@blind}So the loop asks again with only the brief and the frames, and that look
  caught the missing tide curve and the collision." This is the film's best
  evidence that the model's eyes work; do not hide it.

### 6 · Fix (≈14 s) — `fix`

> {@diff}Then it edits its own code. {@wipe}Same moment, before and after.
> {@rounds}[fill from run: "After N rounds of looking and fixing,"] {@final}here's the hook.

- Stage bar: "Fix" lit; then a lime pulse runs the whole bar once per round.
- `diff`: `code-diff` shows the real edit from the first round (3–8 lines from
  `analysis/example/r1/diff.patch`), 36 px mono.
- `wipe`: `before-after-wipe` in the player at the same timestamp as the scene 5
  freeze frame: v0 left, final right.
- `rounds`: a round counter ticks r1 … rN with each round's measured duration.

### 7 · The hook (≈9 s) — `result`

> {@result}(no narration: let it play, or one short line before it starts)

- The player scales up to full frame (FLIP from its scene 6 rect, 0.7 s) and the
  final Tidepool render plays unobstructed, 8 s, with its own look. No overlays
  until its last second, then a lower third: "Final · round N · [fill: time] ·
  [fill: est. inference cost]".

### 8 · How it runs (≈14 s) — `stack`

> {@stack}The loop runs in Pi, and every decision, line of code and frame review is a
> call to Nemotron on Nebius Token Factory. {@media}TTV generated the footage,
> HyperFrames renders the HTML, and Media Tooling voices this script. {@cost}[fill from
> run: "The hook took N rounds, M minutes and about $X of inference."]

- The stage bar expands back into the ring from scene 2. Each node gets the tool
  that does it, landing as named: Write/Look/Fix → "Nemotron 3.5 Super VL ·
  Nebius Token Factory"; Render → "HyperFrames"; the clip card from scene 3 docks
  beside Render → "TTV · MiniMax"; harness label under the ring → "Pi".
- `cost`: three measured numbers count up (rounds, minutes, $), from the real
  ledger, each with a 28 px basis line ("token estimate at list rates").

### 9 · The ask (≈10 s) — `ask`

> {@notscore}This isn't a benchmark score, and we're not claiming one. {@ask}It's a case
> for testing models the way people use them: with tools, and eyes on the output.
> {@claim}This video was made with this tool.

- `notscore`: the scene 1 board returns at 70% scale; a dashed, empty row slides in
  under it: "Nemotron 3.5 Super VL + loop — not scored". No bar, no number.
- `ask`: the dashed row's outline turns lime.
- `claim`: board clears; claim line at 110 px, repository URL at 40 px mono, held
  still for at least 2 s past the last word.

## Honesty rules for this film

- Leaderboard numbers come only from `briefs/data/code2video-aa-2026-10.json`;
  the source line names Artificial Analysis and the access date.
- Our system prompt approximates benchmark conditions. Do not say "same prompt as
  the benchmark". Say "the benchmark condition: one call, no tools".
- No Elo, rank or "beats model X" claims for Nemotron 3.5 Super VL. Show the
  before and after and let the viewer judge.
- If v0 is better than expected or the loop makes something worse, the film says so.
  A loop that helps on one brief is an example, not a result.
- Credits: treatment and brief by human direction (written with Claude Code);
  storyboard, script, compositions, reviews and revisions by Nemotron 3.5 Super VL
  in Pi; footage by TTV/MiniMax; voice ElevenLabs eleven_v4 via Media Tooling.
