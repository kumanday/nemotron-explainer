# Make film v3: one shot vs. the loop

## Resume here (00:45 Oct 30) — corrections to the first v3 session

The first v3 session (ended by Nebius 503s at 00:28) finished the TTV clip, ran v0,
rendered r1 and drafted the film. Four things must be redone before the film:

1. **r1's review is wrong.** REVIEW-r1.md scores Prompt-Intent 5 and finds nothing
   major, but `renders/tidepool-r1.mp4` has no tide curve, no "Low tide 4:12 PM"
   label, no phone shape (a bare rectangle that never rises), and "Tidepool" plus the
   tagline print on top of the headline. Keep REVIEW-r1.md unchanged as a record of
   the self-review. From now on every round also runs the blind reviewer, which sees
   only the brief and frames (a test on r1 found all of the above):
   ```sh
   python3 scripts/blind-review.py --brief briefs/example-tidepool.md \
     --render renders/tidepool-rN.mp4 --out analysis/example/rN/blind
   ```
   Fix every blocker and major finding it reports, then re-render as round N+1.
   The loop stops only when the blind review has no blocker or major finding, or
   after r4. Write your own REVIEW-rN.md after reading the blind review, and say
   where you agree or disagree with it, with frame evidence.
2. **v0 attempt 2.** Attempt 1 (`tidepool-v0/`) spent all 32,768 tokens reasoning at
   `high` effort and returned no HTML. Keep it as recorded. Run attempt 2 once at
   `medium` (now the script default) into `edit/hyperframes/tidepool-v0b/`, render it
   as written to `renders/tidepool-v0b.mp4`, and blind-review it into
   `analysis/example/r0/blind`. The film reports both attempts.
   If v0b renders, the loop starts from a copy of v0b's source (round r2 onward
   edits that lineage; r1 stays as a separate, recorded first draft). If it fails,
   continue from r1.
3. **Evidence must be real.** `analysis/example/r1/diff.patch` contains `...`
   placeholders; regenerate every diff with `diff -u OLD NEW > diff.patch` from
   actual files (keep a copy of each round's source in `analysis/example/rN/src/`).
   `summary.json` must not say a composition was "not a model call": everything
   Pi writes is Nemotron's output. Fill tokens and cost per round from
   `.pi/evidence/runtime.jsonl` timestamps and the blind-review receipts.
4. **The film script states the old, false review result.** After the loop ends,
   rewrite SCRIPT.md lines 4–8 from the real record (see DIRECTION.md scene 5's
   self-review vs. blind-review beat), re-voice with `media-tts-frames`, run
   `python3 scripts/cues.py edit/hyperframes/film-v3`, and update the scenes.

Revised cut lines: loop done by **04:30**, film voiced by **05:30**, film rendered
and reviewed by **08:30**, delivery check passing by **10:00**, package by **10:30**.

v2 (`renders/submission-demo-v2.mp4`) passed the old gate but is not accepted. Its
reveals were hand-timed and missed the narration by up to 4.5 s, the brief overflowed
the frame, the type was too small for the empty frames, credits overlapped, and the
generated clip was a full-frame insert with a caption. Keep v2 and its sources as
they are. Build v3 in new directories.

v3 has a new subject. Artificial Analysis' Code2Video benchmark scores HyperFrames
compositions written in one call with no tools, and Nemotron 3 Ultra ranked last
(see `briefs/data/code2video-aa-2026-10.json`). v3 runs a Code2Video-style brief
through Nemotron 3.5 Super VL twice: once under that condition, once with this
workflow's render → look → fix loop. The film shows both results.

## Read first

1. `storyboards/v3/DIRECTION.md`: the treatment. It is the brief for the film.
2. `.pi/skills/hybrid-explainer/SKILL.md`, then its `references/craft-rules.md`
   and `references/review-rubric.md`.
3. `briefs/example-tidepool.md`: the worked example's brief.

## Deadline and cut lines (America/Bogota, Oct 30)

| By | Done | If late |
|---|---|---|
| 01:30 | Tidepool clip generated, imported, selected | Use a 480p or 768p variant; never skip it |
| 02:00 | v0 one-shot rendered (or its failure recorded) | Nothing to cut: it is one call |
| 04:30 | Loop rounds r1–r3 finished, each with review, diff, render | Stop after the last completed round |
| 05:30 | Film SCRIPT.md with cues written from real results; narration voiced | Merge scenes 7–8 |
| 08:30 | Film v3 rendered and reviewed once | Drop the scene 8 count-ups; keep the ring |
| 10:00 | Second film review round fixed; delivery check passes | Ship the best passing render |
| 10:30 | Package in `submission/` updated for v3 | Publication waits for the user |

Record the actual time at each row in `edit/project.md`.

## Steps

### 1 · The generated clip

Make one TTV image-to-video shot for the example through the existing chain
(storyboard revision `storyboard-2` in `storyboards/`, `media-generated request`,
`scripts/ttv-round plan`, approve exact variants, execute, import,
`scripts/select-take.py`). Intent: looking straight down into a clear rocky tide
pool at golden hour, gentle ripples over anemones and pebbles, slow upward
pull-back, photographic, no people, no text, no logos; 5 s, 16:9, 1080p, muted.
Budget: `docs/footage-costs.md`; update `analysis/media-budget.json` (it does
not yet record the MiniMax workbench clip executed for v2; add it).

Copy the selected clip to `edit/hyperframes/tidepool-loop/assets/tidepool.mp4`.

### 2 · The one-shot baseline (v0)

```sh
python3 scripts/one-shot.py --brief briefs/example-tidepool.md \
  --asset edit/hyperframes/tidepool-loop/assets/tidepool.mp4:assets/tidepool.mp4 \
  --out edit/hyperframes/tidepool-v0
hyperframes render edit/hyperframes/tidepool-v0 \
  --output "$PWD/renders/tidepool-v0.mp4"
```

Do not edit v0, and run it once. If the render fails, keep the error output: that
is the baseline result. Sample its frames per the rubric into
`analysis/example/r0/`.

### 3 · The loop (r1–r3)

Copy v0 into `edit/hyperframes/tidepool-loop/` (keep the clip already there).
For each round N:

1. Review round N−1's encode with `references/review-rubric.md`. Write
   `edit/hyperframes/tidepool-loop/REVIEW-rN.md` (five axes, located findings).
2. Fix only what the findings name. Save `diff -u` of the round's source change
   as `analysis/example/rN/diff.patch`.
3. Render to `renders/tidepool-rN.mp4`; sample the same timestamps into
   `analysis/example/rN/`; mark each finding fixed, partial or not fixed.

Stop when a round has no blocker or major finding, or after r3. You may read the
skills and registry; the point is that the model uses its tools and eyes.
Write `analysis/example/summary.json`: rounds, wall-clock minutes per round,
inference tokens and estimated cost per round from `.pi/evidence/runtime.jsonl`,
and one line per round saying what changed.

### 4 · The film

Slot: `edit/hyperframes/film-v3/`, delivered to `renders/submission-demo-v3.mp4`.

1. Write STORYBOARD.md and SPEC.md from DIRECTION.md and the real example results.
2. Write SCRIPT.md: one `## Line N` per DIRECTION scene with its `{@cue}` markers,
   every **[fill from run]** replaced with the truth. Voice it with
   `media-tts-frames` (eleven_v4). Then run `python3 scripts/cues.py
   edit/hyperframes/film-v3` and build from the generated `CUES.md`.
3. One sub-composition per scene, hosted at its voice frame's start, each with a
   `/* @cues frame=N */ /* @end-cues */` block. Mount the example's renders
   (`tidepool-v0.mp4`, the final round) and the TTV clip as `<video>` layers.
4. `hyperframes lint`, `python3 scripts/cues.py edit/hyperframes/film-v3 --check`,
   `hyperframes check edit/hyperframes/film-v3 --at-transitions`, then render.
5. Review the encode with the rubric (REVIEW.md in the slot), fix, re-render.
   Two rounds at most.

### 5 · Delivery

Fill `analysis/delivery-evidence.json` for v3 (generated footage entries for the
tidepool clip as mounted in the film), then:

```sh
python3 scripts/check-delivery.py
```

Defaults are the v3 artifact and slot. Every gate must pass, including the new
`cue_sync`, `layout_clean`, `review_axes`, `duration_target` (90–150 s) and a
5-second static-hold limit. Update `STATUS.md`, `edit/project.md`,
`submission/` (description, provenance, verification, attribution with the
credits line in DIRECTION.md) for v3. Publication waits for the user.
