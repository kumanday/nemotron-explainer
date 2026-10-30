---
name: hybrid-explainer
description: Produce this project's film v3 and its Tidepool worked example with Nemotron on Nebius - cue-timed HyperFrames motion graphics, integrated TTV footage, five-axis visual review loops and evidence-based delivery checks.
---

# Produce a hybrid explainer

## Load this guidance first

Project references (short; read fully):

1. `references/craft-rules.md`: timing, layout, lifecycle and footage rules, each
   from a defect seen in v1/v2.
2. `references/review-rubric.md`: how every review round samples frames, scores the
   five Code2Video axes and writes located findings.

Upstream skills (read the parts you use and record which ones in DECISIONS.md):

3. `/Users/magos/.agents/skills/hyperframes-core/SKILL.md`: composition contract,
   sub-compositions, media.
4. `/Users/magos/.agents/skills/hyperframes-creative/SKILL.md` with
   `references/house-style.md` and `references/video-composition.md`.
5. `/Users/magos/.agents/skills/hyperframes-animation/SKILL.md`: pick 2–4 rules or one
   blueprint per scene once you know the mechanism.
6. `/Users/magos/.agents/skills/hyperframes-registry/SKILL.md`: `hyperframes catalog
   WORDS`, `hyperframes add NAME`. DIRECTION.md lists blocks to start from.
7. `/Users/magos/dev/media-tooling/.agents/skills/media-tts/SKILL.md`: cues,
   pronunciations, re-voicing.
8. `/Users/magos/dev/media-tooling/.agents/skills/media-motion-graphics/references/generated-film-playbook.md`
   and `/Users/magos/dev/media-tooling/docs/generated-media.md` for the TTV chain.

Use current CLI help when an older example conflicts.

## Two products, one method

- **The Tidepool example** (`briefs/example-tidepool.md`): an 8-second, silent,
  Code2Video-style hook. v0 comes from `scripts/one-shot.py` (one call, no tools)
  and is never edited. The loop copy in `edit/hyperframes/tidepool-loop/` is
  improved round by round with the review rubric.
- **Film v3** (`storyboards/v3/DIRECTION.md`): the narrated 100–120 s film that
  shows the board, the loop, v0, the review findings, the fix and the final hook.

Both use the same method: plan → build → render → sample the encode → review on
five axes with located findings → fix only the findings → re-render → compare the
same frames. The film's scenes 4–7 show that method's real artifacts from the
example, so keep them: frames, review files, diffs, renders, timings, costs.

## Build the film from cues

1. SCRIPT.md lines carry `{@name}` markers at each reveal (DIRECTION.md names them).
2. `media-tts-frames` produces `audio_meta.json` with `cues[]`; `duration_s`
   includes tail holds.
3. Host each scene at its voice frame's start for its full `duration_s`, with a
   matching `<audio>` window. `python3 scripts/cues.py SLOT` fills each scene's
   `/* @cues frame=N */ /* @end-cues */` block and writes CUES.md.
4. Place every tween at `CUE.name` or `CUE.name + offset`.
5. Re-run `cues.py` after any re-voice. `cues.py SLOT --check` must pass.

Before the scenes, write STORYBOARD.md (per shot: what changes, on which cue, why it
explains the line, source asset, end state) and SPEC.md (tokens, type scale, grid,
eases) from DIRECTION.md.

## Generated footage

Run the TTV chain: storyboard revision, `media-generated request`,
`scripts/ttv-round plan --request ID`, review prompts/variants/costs, approve exact
variants, `scripts/ttv-round execute ...`, import, `scripts/select-take.py`.
Record request/plan/approval/result and the selected take. In the film, the clip
appears as an asset card (scene 3) and inside the example renders; in the example
it plays full-bleed, then inside the phone. Record result path, clip ID, source
hash and visible interval in `analysis/delivery-evidence.json`.

## Finish only with evidence

`python3 scripts/check-delivery.py` checks files, generated-footage lineage,
cue sync, layout overflow, review axes, duration and static holds. It cannot judge
whether the film is good. Your rubric review must, and must say what is still weak.
Then update STATUS, provenance, verification and public copy from real records.
Unknown charges remain unknown. Measured numbers only.
