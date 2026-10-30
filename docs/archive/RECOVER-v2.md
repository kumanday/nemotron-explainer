# Build the required mixed-media result

## Render the current proof

Read `docs/hyperframes-rendering.md`. The 19.96-second composition in
`edit/hyperframes/self-demo-v2/` has an explicit root `<head>` with UTF-8 metadata,
which preserves nested scene CSS in HyperFrames 0.8.142. Render that source and
inspect decoded frames before changing the typography or layout. Keep the head
when editing the main HTML; scene styles and scripts stay inside `<template>`.
Continue from existing footage and narration. Inspect animation and generated
video playback across multiple times; a styled still alone does not pass review.

## Resume the current generation/selection work

Read `docs/tool-locations.md` before investigating package paths or selection
errors. The first generated clip has succeeded. Drafts are preserved under
`rough-cuts/manifests/drafts/`, and `edit-proof-99` has been compiled with the native
selection command and validated. Inspect those records and continue to actual composition;
avoid repeating paid generation. Scope searches to the known source checkouts.

Read `.pi/skills/hybrid-explainer/SKILL.md` and `.pi/APPEND_SYSTEM.md` first, then
load the craft references listed by that skill. Continue using Nemotron 3.5 Super
VL on the verified Nebius route. Existing $100 media authorization applies.

## Current canonical state

`renders/submission-demo.mp4` is an incomplete prototype. It contains narrated
text/screenshots with basic entrance fades. It has no generated video, and the
encode includes a near-static interval from approximately 37 to 56 seconds. The
prototype source contains no `<video>` layers. The generated clip identified in
the resume section is ready for integration. `STORYBOARD.md`,
`SPEC.md` and a design spec are missing. These requirements remain open.

The edit tool recovered after the validation errors by using `edits[].oldText`
and `edits[].newText`. Those errors do not explain the missing footage and craft.
Narration metadata includes tail holds; account for those explicitly rather than
claiming that a successful encode proves pacing or narration completeness.

## Work in a new version

Preserve the existing prototype, session and media. Use
`edit/hyperframes/self-demo-v2/` and `renders/submission-demo-v2.mp4`. Reuse good
assets and narration only where the revised story supports them. The final film
must still be produced by this Pi/Nemotron workflow.

## Prove the core capability first

1. Write an actual storyboard and numerical design/motion spec. Plan a short
   worked example that transforms across beats, with large objects and legible
   type. Read the creative house-style/video-composition and animation guidance.
2. Make a 15–20 second proof containing one real TTV-generated clip and at least
   two explanatory motion sequences. A brief can become a storyboard/filmstrip;
   an editor can inspect a region and visibly change the composition. Choose the
   treatment yourself; avoid text cards describing unperformed steps.
3. Use `docs/footage-costs.md` to reserve video cost, review exact TTV plans and
   execute/import/select the footage. Pricing uncertainty is not a reason to omit
   a mandatory feature silently. Diagnose an actual failure when one occurs.
4. Render and inspect the proof as multiple timestamped frames at video and
   phone scale. State what visibly changes and how it explains the narration.
   Correct real issues. Preserve a matched before/after pair for any revision.
5. If two passes still cannot deliver the core proof, report that capability gap
   with the artifact and errors. Do not build another long text-card film and
   mark the task complete.

## Expand the successful proof

Use genuine process footage from the proof to build the 90–120 second self-demo.
Favor the result and visible actions over architecture paragraphs. Include the
actual generated footage in the final encode. Apply the same visual/temporal
review to this final film, and tie evidence to its actual SHA-256.

Populate `analysis/delivery-evidence.json` from real receipts and review evidence.
Then run:

```sh
python3 scripts/check-delivery.py \
  --artifact renders/submission-demo-v2.mp4 \
  --composition edit/hyperframes/self-demo-v2
```

Satisfy every gate before declaring completion. Passing this gate does not prove
the film is compelling: inspect it critically. Keep any unresolved feature,
legibility, motion, provenance or cost issue explicit. Public copy must describe
the actual delivered result. EBO is optional; publication remains the user's
decision. Deadline: October 30 at noon America/Bogota.
