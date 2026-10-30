# Visual review rubric

Use this for every review round: the Tidepool example's loop and the film itself.
The five axes are the ones HeyGen's Code2Video judge scores. A review is a list of
located defects with fixes, not a description of what the frames show.

## Before looking

1. Render the candidate. Note its SHA-256.
2. Run `hyperframes check SLOT --json --at-transitions`. Every `*_overflow` or
   overlap issue on text is a Craft defect to fix before visual review.
3. For narrated work, run `python3 scripts/cues.py SLOT --check` and fix every error.
4. Sample frames from the **encoded MP4**, not the browser:
   - the example (8 s): 0.5, 1.5, 2.6, 3.4, 4.2, 5.2, 6.4, 7.6 s;
   - the film: each cue time + 0.4 s, each scene's midpoint, and 0.1 s either side
     of each scene boundary.
   `ffmpeg -ss T -i FILE -frames:v 1 -vf scale=1280:-1 OUT.png`. Also build a
   360 px-wide contact sheet to check phone-scale legibility.
5. Read at most eight images per batch. Write findings for that batch to the review
   file before reading the next.

## Blind review first

Run `python3 scripts/blind-review.py --brief BRIEF --render MP4 --out DIR` before
writing your own review. It sends only the brief and the frames to a fresh
Nemotron call, which inventories what is visible before judging. Your own review,
written with the source and plan in mind, has already reported a missing tide curve
as present (r1). Read the blind findings, then check each against the frames. Agree
or disagree with frame evidence. Never mark a brief element present unless you can
name the frame and what is drawn there.

## The five axes (score 1–5 each, with one sentence of evidence)

| Axis | 5 means | Check specifically |
|---|---|---|
| **Engagement** | The first second is striking; something worth watching every 2–3 s | Opening frame; longest stretch with no meaningful change |
| **Prompt-Intent** | Every beat in the brief happens, at its stated time, with its stated copy | Walk the brief line by line; list anything missing or late |
| **Composition** | One clear focal object; asymmetric balance; type hierarchy reads at 360 px | Empty area > 50% of frame; focal object < 30% of frame; centred stacks |
| **Temporal** | Eases have weight; reveals land on cues/beats; holds are long enough to read | Elements that pop in or vanish with no tween; text moving while it is read; reveals more than 0.25 s off their cue |
| **Craft** | Nothing clipped, overlapping, misaligned, unstyled or flickering | Text past the frame or its panel; overlaps; tiny text (< 32 px at 1080p); FOUC or fallback fonts; video not playing |

## Findings format

Write each finding as one block. The film shows these, so be exact:

```
- id: f1
  axis: Craft
  severity: blocker | major | minor
  time_s: 3.4
  region: x=820 y=40 w=960 h=180      # pixels on the 1920x1080 frame
  saw: Headline "Know the tide before you go." runs past the right edge.
  cause: .headline has width:auto and font-size:132px; no max-width.
  fix: Set max-width:760px and font-size:110px; break before "before".
```

`saw` is what is in the image. `cause` names the selector or timeline line in the
source. `fix` is the edit you will make. No finding means no edit: do not change
things that are fine.

## After fixing

- Re-render, re-sample the same timestamps, and compare each finding's frame
  before/after at the same time and crop. Mark each finding fixed, partial or not
  fixed, with the new frame path.
- Keep each round's artifacts: `analysis/example/rN/` holds frames, `REVIEW-rN.md`,
  `diff.patch` (`diff -u` of the sources), render path and hash.
- Stop when a round has no blocker or major finding, or after round 3. Record why.
