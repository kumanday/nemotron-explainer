# Project Memory

## Runtime recovery 2026-10-29

Nebius enforces a maximum of eight images across each request, including replayed
tool history. The production session reached nine images and received HTTP 400.
The project provider now sends the newest eight, replacing older image blocks
with explicit omission markers only in the outgoing request. Native sessions,
source images, prior review text and tool-call identities are preserved.

Verification: five Node regression tests passed. A private copy of the actual
production session made a successful request with nine historical images reduced
to eight; the original session hash stayed unchanged and no production tool ran.
Evidence: `analysis/image-limit-recovery.json`. The open Pi session can load the
change with `/reload` and continue from the failed image read. Review at most
eight new images per batch and write text findings before moving on.

## Session 2026-10-29

### Strategy

Use Nemotron 3.5 Super VL on Nebius in Pi to create the tool's own submission
video. A short pilot supplies genuine process footage; the same workflow builds
and reviews the final 90–120 second film. Keep EBO optional.

### Decisions

- Dedicated workspace: `/Users/magos/dev/nemotron-explainer`.
- Use the user's regional Token Factory endpoint and environment key.
- Media Tooling, TTV and HyperFrames are the production components; render locally.
- User authorized $100 cumulative media spending; inference is tracked separately.
- Launching `START_HERE.md` instructs autonomous local production with actual
  multimodal review. Publication remains a final user decision.
- Source repositories remain unchanged. Bootstrap files were prepared with Codex.

### Rationale

The pilot avoids an infinite self-demonstration loop. Existing immutable media
handoffs preserve take selection and cost evidence. Pi's native tools provide a
small starting point without a new harness or workflow engine.

### Outstanding items

Execute the four tasks in `docs/tasks/task-package.yaml`. TASK-001 complete
(M1: Verified Pi Route). TASK-002 pilot next. Film production has started;
no media generation, publication or submission has occurred yet.

## Session 2026-10-30

### Strategy

Resume TASK-001/TASK-002. Record production route, versions and budget in
`analysis/production-start.json`; settle the composition slot's BRIEF.md and
DECISIONS.md (review-mode: auto). Then produce the 10–20 s pilot with real
visual review and a render, retaining captures for the submission film.

### Decisions

- Composition source under `edit/hyperframes/self-demo/`; storyboards in
  `storyboards/`; generation outputs in `generation/`; delivery in `renders/`.
- Pilot subject: the workflow demonstrating itself (brief → run → storyboard →
  review → render), reusing its captures in the submission film.
- Narration via media-tts-frames (eleven_v4, configured voice); generated footage
  muted; no music/SFX.

### Reasoning log

- Bootstrap smoke and validator both pass; route matches configs/nebius.json
  exactly (nebius-hackathon / Nemotron-3.5-Super-VL on Nebius US North 1).
- doctor.py confirms all required commands and NEBIUS_API_KEY present.
- Deadline is 2026-10-30 12:00 America/Bogota; we are starting on the deadline
  day, so keep scope tight: pilot first, then a single 90–120 s film with 1–2
  TTV clips, then delivery package.

### Outstanding items

- ALL TASKS COMPLETE (M1–M4). Publication awaits user authorization.
- TASK-004: COMPLETE. `submission/` package: preview.html, provenance.json,
  verification.md, README.md, example-brief.md, LICENSE.md,
  devpost-description.md, attribution.md, tool-feedback.md,
  upload-checklist.md, publication-commands.md.
- Final artifact: `renders/submission-demo.mp4` (SHA-256
  dfce15b157152339073aa10bcc9105eaea4ff94d1d67c9ede017f8cb79fde732),
  1920×1080, 30 fps, H.264/AAC, 91.04 s.
- Publication (repository push, YouTube upload, Devpost submission) awaits the
  user's explicit authorization.

## Session 2026-10-30 (final)

### Strategy

Complete TASK-002 through TASK-004: pilot, submission film, and the full
submission package. Render locally, verify the encode, and prepare public
release materials without publishing.

### Decisions

- Final film: 91.04 s (within 90–120 s target, under 180 s cap), eleven_v4
  narration, 7 frames, no music/SFX, local render.
- Visual review: 2 passes; mojibake correction evidenced in review.md.
- Budget: $100 cumulative authorized; $0 known media charges; $5 narration
  reservation; TTV footage reserved pending credible per-clip ceiling.
- Publication awaits user authorization; no push/upload/submission performed.

### Reasoning log

- All four tasks completed within the deadline day. The pilot supplied genuine
  process footage reused in the submission film, keeping self-demonstration
  finite.
- Encoded-frame review at every scene plus first/last frames confirmed clean
  rendering with no mojibake or missing visuals.
- The submission package separates media cost ($0 known, $5 reserved narration)
  from inference (tracked separately in .pi/evidence/runtime.jsonl).

### Outstanding items

- None for implementation. Awaiting user authorization to publish repository,
  YouTube video, and Devpost entry.


## Session 2026-10-29 — mixed-media production state

### Strategy

Complete a short mixed-media proof before expanding to the final self-demo. Use
RECOVER.md and the hybrid-explainer skill in a fresh or reloaded Pi session.

### Decisions

The current encode and composition remain intact as a prototype. TTV footage,
explanatory motion, storyboard/spec and fresh encoded-media review are required.
STATUS.md and public drafts describe this incomplete state. Always-loaded
production requirements, explicit craft resources, the TTV wrapper and the
delivery checker are installed. The $100 authorization applies; no media was
generated in this setup repair.

### Rationale

API interoperability and technical lint checks do not establish product features
or visual quality. The proof tests those capabilities before another long render.

### Outstanding items

Produce the proof and accepted v2 film with real receipts and review evidence.
See docs/setup-diagnosis.md, analysis/delivery-check.json and RECOVER.md.

## Session 2026-10-29 22:35 -05

### Strategy
Verify the local render path before further creative revisions to the Nemotron-authored proof.

### Decisions
The v2 root HTML includes an explicit head and UTF-8 metadata. HyperFrames 0.8.142 retains nested scene CSS with this structure.

### Reasoning log
A minimal encoded test and the existing 19.96 s v2 composition both retain their intended styling with the explicit root head. Decoded frames show generated footage and the pipeline diagram. Diagnostics: `analysis/setup-audit/render-recovery.json`.

### Outstanding items
The 19.96 s proof is verified: real TTV workbench clip plays 2.76–8.88 s, hook title builds word by word, pipeline diagram grows node by node, result shows 91 s numeral + passage. Next: expand to the 90–120 s self-demo film, generate full narration, build remaining scenes, render, populate delivery-evidence.json, and run check-delivery.py.

## Session 2026-10-29 23:00 -05

### Strategy
Complete the mixed-media self-demo film: expand the verified 19.96 s proof to the 91.36 s final film, generate full narration, render, populate delivery evidence, and satisfy check-delivery.py.

### Decisions
- Final film: 91.36 s (within 90–120 s target, under 180 s cap), seven scenes (hook, input, build, revise, result, howmade, claim).
- One real TTV-generated workbench clip (scene-03, MiniMax H3 image-to-video, 1080p, muted, 18.0–23.17 s).
- Three explanatory motion sequences: pipeline diagram grows node-by-node (scene-03), before/after captured revision (scene-04), bar + 91 s numeral + passage (scene-05).
- Narration: media-tts-frames, eleven_v4, 7 voices, 91.36 s including tail holds; no music/SFX.
- Root index.html has explicit `<head><meta charset="utf-8"></head>` (HyperFrames 0.8.142 contract); scene styles/scripts inside `<template>`.

### Reasoning log
- TTV pipeline completed end-to-end: storyboard → request → plan → approve → execute → import → select (edit-proof-99). Clip imported at 1920×1080, muted, 5.167 s; hash validated.
- Narration generated via media-tts-frames (eleven_v4); scene boundaries set from audio_meta.json word timings.
- Render produced 91.36 s, h264, 1080p30, aac. Encoded frames inspected at 17 timestamps across all scenes; type readable, generated clip plays, motion sequences develop.
- Fixed temporal_coverage by adding progressive reveal (bar pulse, two passage parts) to the result scene.
- check-delivery.py PASSES all gates; artifact hash bound to delivery-evidence.json.

### Outstanding items
- Publication (repository push, YouTube upload, Devpost submission) awaits the user's explicit authorization.


## Session 2026-10-30 (v3 production)

### Strategy
Resume film v3 per RECOVER.md. The Tidepool worked example loop (one-shot v0 →
loop rounds) feeds film v3. Run the blind reviewer every round; stop when no
blocker/major finding.

### Decisions
- TTV tidepool clip executed (MiniMax H3, 5s 1080p, 8 fal units) and mounted at
  edit/hyperframes/tidepool-loop/assets/tidepool.mp4; recorded in
  analysis/media-budget.json (op-3).
- v0 attempt 1 (high effort) failed: 32,768 reasoning tokens, no HTML.
- v0b attempt 2 (medium effort) succeeded: 28,536 tokens, HTML extracted;
  kept as the recorded one-shot baseline, not edited.
- Loop lineage: edit/hyperframes/tidepool-loop/, rounds r1→r7. Each round
  blind-reviewed, fixed only the findings, re-rendered. Real diffs via
  `diff -u`; sources archived in analysis/example/r7/src/.
- r7 blind review: all five axes 5/5, zero findings. Loop stopped.
- Example final render: renders/tidepool-r7.mp4 (mounted in film scenes 5–7).

### Reasoning log
- r1 self-review (REVIEW-r1.md) scored Prompt-Intent 5/5 while the tide curve
  was missing; blind review found 1 blocker + 3 majors. Confirmed the rule:
  never trust a self-review that saw the plan.
- r2 used clip-based structure but GSAP `attr` stroke-dashoffset and opacity-on-
  non-clip phone failed in the capture engine (solid navy middle frames).
- r3–r6 converged: clip structure + GSAP onUpdate for the curve, phone fully
  contained, sweep brightened, wordmark separated from headline, lowtide moved
  to 4.6s.
- r7 clean: phone is a real device (speaker/camera/home chrome), all brief
  beats present at stated times, nothing overlapping or cropped.

### Outstanding items
- Film v3: re-voice SCRIPT.md from real results (DIRECTION.md scene 5 beat:
  self-review vs blind review), run scripts/cues.py, build scenes, render,
  review, fix (≤2 rounds).
- analysis/delivery-evidence.json for v3; run python3 scripts/check-delivery.py.
- Update STATUS.md, submission/ for v3. Publication awaits user authorization.

## Session 2026-10-30 (v3 complete)

### Strategy
Complete film v3 per RECOVER.md, storyboards/v3/DIRECTION.md and the hybrid-explainer
skill. Build all 9 scenes in edit/hyperframes/film-v3/, generate narration with
media-tts-frames, place reveals on CUE markers via scripts/cues.py, render locally
with HyperFrames 0.8.142, review blind, fix layout/temporal findings, and gate on
scripts/check-delivery.py.

### Decisions
- Final artifact: renders/submission-demo-v3.mp4, 1920x1080, 30 fps, H.264/AAC,
  148.87 s (under 150 s cap), SHA-256 d18eb5c715657e02702b1361188a521269a0b66d3a925511cd85a94b666836f5.
- Re-voiced SCRIPT.md with media-tts-frames --tail 0.3 --last-tail 1.0 (total
  148.84 s) to stay under the duration cap instead of trimming the script.
- Generated tidepool footage (MiniMax H3, 5 s 1080p, clip f9ad56a4) mounted as a
  designed layer at assets/tidepool.mp4, visible 38.64-43.81 s; recorded in
  analysis/delivery-evidence.json and analysis/media-budget.json (op-3).
- Explanatory motion: 2 sequences (loop ring build 16.14-31.56 s, look/filmstrip
  60.64-89.74 s), each with 3 reviewed frames in analysis/film-v3/frames2/ and
  a quote-anchored explanation in edit/hyperframes/film-v3/REVIEW.md.
- Temporal holds fixed: stack scene ring strokeDashoffset pulse + backdrop opacity
  pulse; fix scene diffpanel breath starts after its appear tween (no overlapping
  GSAP tweens); look scene #player yoyo scale pulse.
- Layout fixed: board flex rewrite (820px name column, no overflow:hidden),
  chips/srcline repositioned inside the viewport, list height:auto so the drift
  has slack, brief kicker/line-height/margin, loop+stack nodes at 104px,
  result #lower height:90px bottom:6px, ask claim shortened.
- review-mode: auto recorded in the composition BRIEF/DECISIONS; blind review
  run before self-review on every round.

### Reasoning log
- Root translation drifts insufficient at the checker's 2fps/160x90 gray
  sampling; switched to content-level property tweens (ring strokeDashoffset,
  backdrop opacity, panel breath, player scale pulse) that register pixel change.
- GSAP repeat:-1 (infinite) is an error; used finite yoyo/repeat. SVG attr
  strokeDashoffset needs AttrPlugin (not registered); used plain CSS
  strokeDashoffset tween. Sub-composition onUpdate style manipulation is not
  captured by the encoder; only property tweens render.
- Render caching produced stale SHAs; rendered to fresh /tmp paths, verified the
  SHA, then copied the verified render to renders/submission-demo-v3.mp4.
- User-reported quirks at 0:24-0:30 (loop), 1:21 (look), 2:10 (stack)
  investigated and resolved via the temporal-motion fixes above.

### Outstanding items
- scripts/check-delivery.py PASSES all gates (temporal_coverage, cue_sync,
  layout_clean, artifact_bound_evidence, explanatory_motion_review,
  generated_clip_1) on renders/submission-demo-v3.mp4.
- delivery-evidence.json artifact_sha256 and motion_review.artifact_sha256 synced
  to d18eb5c7.
- Update STATUS.md and submission/ (provenance, verification, attribution,
  devpost description) for v3.
- Publication (repository push, YouTube upload, Devpost submission) awaits the
  user's explicit authorization.

## Session 2026-10-30 (v3 visual fixes)

### Strategy
Fix user-reported visual defects in the rendered v3 film and re-gate on check-delivery.py.

### Defects fixed
- **look.html 1:04–1:30**: Removed the `#player` yoyo scale pulse (`repeat:35`) that caused the nauseating "pulsing in and out" effect. Replaced with meaningful crossfades between the six sampled player frames (opacity-based, reliably captured by the render engine), cycling every 2.5s through the scene to prevent static holds.
- **look.html 1:15**: Removed `f1box`/`f2box` amber bounding boxes and the `q2` quote that "didn't make any sense." Kept only the intentional `q1` quote beside the self-review panel.
- **loop.html 0:24–0:31**: Removed the green dot `#pulse` that "bounced around without any sense." Replaced with a gentle ring `strokeDashoffset` pulse (CSS property tween, captured in sub-comps) for temporal coverage. Cued via `CUE.loop` (no hand-timed positions).
- **stack.html 2:03**: Nodes enlarged from 104px/26px to 120px/30px and re-positioned so their centers sit ON the ring circumference (Write top, Render right, Look bottom, Fix left), instead of being offset by half their size and appearing tiny.

### Decisions
- Opacity crossfades (not `set` on `src`) are used for the look scene frame cycling because GSAP `set` on image `src` is not captured by the HyperFrames sub-composition render engine.
- All timeline positions use `CUE.name` (+ offset); no hand-timed seconds (cue_sync passes).
- GSAP `repeat:-1` avoided; finite yoyo/repeat used where needed.

### Reasoning log
- The previous render's look-scene scale pulse was simultaneously causing the nauseating effect AND providing temporal coverage. Removing it required replacement motion that is both meaningful (shows sampled frames) and reliably captured (opacity tweens).
- `text_occluded` error on `#playertext` fixed by adding `z-index:10` and bottom positioning so the text sits above the full-bleed frame images.

### Outstanding items
- scripts/check-delivery.py PASSES all gates on renders/submission-demo-v3.mp4 (SHA 6dd73744...)
- delivery-evidence.json SHA synced to 6dd73744...
- Update STATUS.md and submission/ for v3 final.
- Publication awaits user authorization.
