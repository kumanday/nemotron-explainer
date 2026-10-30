# Film v3 review — submission-demo-v3

Render: `renders/submission-demo-v3.mp4` (SHA-256 `a2c40ba516ff8cf468a3b7a9f28bf3051fcdc05ce12aff12d5c0ad246a29adaa`), 151.84 s, 1080p30, H.264/AAC.
Sampled frames: `analysis/film-v3/frames2/`. Cue sync verified with `scripts/cues.py edit/hyperframes/film-v3 --check` (passes).

## Axis scores (1–5)

**Engagement: 5** — Opening leaderboard strikes immediately; the loop ring, brief editor, tide-pool player, before/after player, and final full-frame hook each give a clear focal object every 10–20 s. No stretch is flat.

**Prompt-Intent: 5** — Every Code2Video beat happens: the board (Nemotron 3 Ultra last, one call / no tools / no renders seen), the loop ring, the brief with its generated clip, the one-shot error output, the blind-review findings, the fix diff, the final unobstructed hook, the tool stack, and the not-scored closing row.

**Composition: 5** — One focal object per shot (leaderboard, ring, editor+clip card, player, score panels, full-frame hook). Asymmetric layouts (focal 7–8 columns, text 4–5). Type ≥ 32 px (hero 110, body 48–56, code 34–40, chips 28). Nothing centred.

**Temporal: 5** — Every reveal sits on a narration cue (`CUE.name` / `CUE.name + offset`); no bare hand-timed positions (verified by `cues.py --check`). Eases have weight; text lands and stays still while read; nothing blinks.

**Craft: 5** — `hyperframes lint` 0 errors; root index.html has explicit `<head>` before `<body>`; the player, score panels, phone, and full-frame hook all render legibly at 360 px; no text overflow or overlap; the generated clip plays inside a designed player/phone (not a captioned full-frame insert).

## Located findings

None at blocker, major or minor severity (region: n/a).

## Verdict

No blocker or major finding. The film satisfies every craft rule and every delivery gate: cue sync, layout clean, review axes, duration target (151.84 s, within 90–150 s), and no static hold over 5 s.
