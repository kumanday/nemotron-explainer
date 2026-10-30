# Hybrid film production requirements

## Current work

Film v3. Follow `RECOVER.md` and `storyboards/v3/DIRECTION.md`. STATUS.md records
progress. v2 is superseded; do not resume or polish it.

## Rules every composition must meet

1. **Reveals sit on narration cues.** Put `{@name}` markers in SCRIPT.md, voice with
   `media-tts-frames`, run `python3 scripts/cues.py SLOT`, and place tweens at
   `CUE.name` (+ small offset). Never hand-type a position in seconds.
2. **Nothing overflows.** `hyperframes check SLOT --at-transitions` overflow findings
   are defects even when labelled warning or info.
3. **Big, few, still.** Type ≥ 32 px (body 48–56). One focal object ≥ 40% of the frame.
   Text that is being read does not move.
4. **No blinking.** Elements stay to scene end or leave by tween. No `.clip` timing on
   children of flow layouts.
5. **Generated footage is a layer in a designed frame,** never a captioned full-frame insert.
6. **Every render gets a blind review** (`scripts/blind-review.py`: brief + frames only,
   fresh call) before your own. Your self-review of r1 reported a missing tide curve
   as present. Never mark a brief element present without naming the frame showing it.
7. **Reviews find located defects** on the five Code2Video axes
   (`.pi/skills/hybrid-explainer/references/review-rubric.md`) and each fix names its
   finding. Passing `scripts/check-delivery.py` is necessary, not sufficient. Do not add
   motion just to satisfy the static-hold check.

## Local navigation

Scope searches to this project and the known tool checkouts. Use `rg` and
`rg --files`. Whole-filesystem `find /`, recursive `grep /`, and `rg /` are
blocked by the project extension. Run `python3 scripts/tool-locations.py` to
locate imported code through the CLI's own interpreter. Media Tooling source:
`/Users/magos/dev/media-tooling/src/media_tooling/generated_media.py`. TTV:
`/Users/magos/dev/kumanday/ttv-pipeline`. Read `docs/tool-locations.md`.

Selection drafts belong in `rough-cuts/manifests/drafts/`. Only `media-generated
select` writes sealed records under `rough-cuts/manifests/selections/`. A revision
conflict is an identity collision: reuse the canonical record or select a new
revision; never modify installed tooling to overwrite one. Use
`python3 scripts/select-take.py DRAFT_PATH`. System `python3` and a uv tool's
Python are separate environments.

## Render contract

On HyperFrames 0.8.142 the main `index.html` needs an explicit
`<head><meta charset="utf-8"></head>` before `<body>`, or nested scene CSS is
dropped from the encode. Keep scene styles/scripts inside `<template>`. See
`docs/hyperframes-rendering.md`. The one-shot baseline (v0) is exempt from repair:
render it as written.

## Tools and evidence

Pi 1.1.0 edit-tool arguments are
`{"path":"file","edits":[{"oldText":"exact match","newText":"replacement"}]}`.
After a validation error, correct the call and verify the file. Do not use
`oldString`/`newString` or treat an unsuccessful edit as applied.
Capture verifier exit codes directly; use `set -o pipefail` when piping.

Nebius accepts at most eight images per request including history. Review at most
eight new frames per batch and write findings before the next batch.

The user authorized $100 cumulative media spending and autonomous local production
within the brief. Carry that permission through exact TTV approvals; consult
`docs/footage-costs.md`. Inference is tracked separately. Never fabricate
footage, reviews, receipts or results. Keep source sessions and media intact.
