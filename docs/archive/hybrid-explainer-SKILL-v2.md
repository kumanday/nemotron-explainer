---
name: hybrid-explainer
description: Produce or repair this project's mixed-media explainer using Nemotron on Nebius, real TTV footage, narrated HyperFrames motion graphics, and evidence-based delivery checks.
---

# Produce a hybrid explainer

## Load the production and craft guidance

Read these files before creating a storyboard or composition. Record the paths
actually read in the production decision record; an advertised skill name is not
loaded guidance.

1. `/Users/magos/dev/media-tooling/.agents/skills/media-motion-graphics/SKILL.md`
2. Its `references/generated-film-playbook.md`, `scripts/ttv_round.py`, and
   `/Users/magos/dev/media-tooling/docs/generated-media.md`.
3. `/Users/magos/.agents/skills/hyperframes/SKILL.md`, then its
   `references/types/explainer.md`, `references/story.md`, `references/spec.md`,
   `references/motion.md` and `references/review.md`.
4. `/Users/magos/.agents/skills/hyperframes-creative/SKILL.md` and its mandatory
   `references/house-style.md` and `references/video-composition.md`.
5. `/Users/magos/.agents/skills/hyperframes-animation/SKILL.md`,
   `/Users/magos/.agents/skills/hyperframes-core/SKILL.md`,
   `/Users/magos/.agents/skills/hyperframes-registry/SKILL.md`, and
   `/Users/magos/.agents/skills/hyperframes-cli/SKILL.md`.
6. `/Users/magos/dev/media-tooling/.agents/skills/media-tts/SKILL.md`.

Use current CLI help and installed runtime contracts if an older reference
example conflicts. Read only relevant animation rules/blueprints after choosing
the visual mechanism. Keep `.clip` lifecycle under the framework's control;
animate children for entrance/exit polish. Root and scene timelines are seekable.

Read `docs/hyperframes-rendering.md` before rendering. The main `index.html`
needs an explicit `<head><meta charset="utf-8"></head>` before `<body>` on
HyperFrames 0.8.142 so nested scene CSS survives the encode. Keep nested scene
styles and scripts inside `<template>`. Verify decoded frames against the design;
browser previews alone do not establish render parity.

## Make the film, not a report about the film

Create `STORYBOARD.md` and a numerical `SPEC.md` before source. Each shot names
what changes on screen, when it changes, why that movement explains the narration,
the source asset, and the expected final state. A scene saying “build storyboard”
does not replace an actual storyboard. Search the registry before hand-building a
named effect. Keep the direction coherent across generated footage and graphics.

Typography must work at video scale: choose headline/body/label sizes in SPEC,
use a substantial focal object, and inspect a 360 px wide review sheet. Small
paragraphs on a mostly empty canvas fail review. Use a growing diagram, a worked
example, a meaningful transformation, or a guided visual comparison across beats.
Fades and sliding cards alone do not meet the brief. Avoid narration that merely
reads paragraphs displayed on screen.

## Integrate generated footage

Use `scripts/ttv-round plan --request ID` after creating and sending a reviewed
request with `media-generated`. Review exact prompts, variants, references and
costs; use `scripts/ttv-round execute ...` within the cumulative $100 authorization.
The wrapper delegates to the installed helper. Read its help and native contracts.
Use existing image generation or supplied keyframes through the documented TTV
path. Record their costs separately from video. See `docs/footage-costs.md` for a
current conservative video quote.

Retain the request/plan/approval/result chain and selected take. Author selection
input under `rough-cuts/manifests/drafts/` and run `scripts/select-take.py`.
The CLI owns `selections/` and generated EDLs; preserve those immutable outputs.
Verify import and selection. Put the actual generated clip in a timed `<video>` content layer and
show it in the encode. Record its result path, clip ID, source hash and visible
interval in `analysis/delivery-evidence.json`. Planning or a reserved budget is
not executed footage. If a call is blocked, solve or report that exact blocker.

## Keep narration and review honest

Narration comes from Media Tooling. `audio_meta.json` duration_s includes tail
holds (normally 0.6 s, 1.6 s on the last clip); raw MP3 length is shorter. Use the
documented duration sync, or explicitly account for hold adjustments in SPEC.
Do not diagnose trimmed silence as clipped speech without inspecting word timing.

Review the actual encode: sample multiple timestamps inside a motion sequence,
not only each scene's first frame. Include cut boundaries and phone-size views.
State what you observed at each time and what it implies. Keep images, timestamps,
feedback and the artifact hash. A before/after comparison uses the same scene,
time and crop from two versions; a terminal screenshot beside a title card is not
evidence of a visual repair. Record measured sound checks separately from hearing.

## Finish only with evidence

Follow `RECOVER.md` when repairing the current prototype. Preserve its sources
and encode; use a new versioned composition and delivery file.

Fill `analysis/delivery-evidence.json` from real work using the example template.
Run `python3 scripts/check-delivery.py --artifact PATH --composition PATH` and
fix every failed gate. It checks required files, generated-video lineage and
presence, motion review tied to the actual encode, and long static stretches.
It does not establish artistic quality; the visual review still must be critical.

Only then update STATUS, provenance, verification and public copy. Unknown
charges remain unknown; current totals include all executed attempts. Use actual
timestamps, not an inferred deadline date. EBO remains optional.
