# Delivery verification

Status: complete. `renders/submission-demo-v3.mp4` is the accepted mixed-media
submission film. Its SHA-256 is
`d18eb5c715657e02702b1361188a521269a0b66d3a925511cd85a94b666836f5`.

Verified media properties: H.264/AAC MP4, 1920×1080, 30 fps, 148.87 s (under
the 150 s cap). The encode contains the real TTV-generated tidepool clip as a
designed layer (visible 38.64–43.81 s), explanatory motion graphics in two
sequences, cue-timed reveals, and narration produced by media-tts-frames
(eleven_v4).

`scripts/check-delivery.py` passes all gates on the final artifact:
temporal_coverage, cue_sync, layout_clean, artifact_bound_evidence,
explanatory_motion_review and generated_clip_1. The delivery-evidence SHA
matches the rendered artifact.

Before/after evidence compares the same scene, timestamp and crop:
`analysis/film-v3/frames2/` holds the reviewed loop (t20/t25/t30) and look
(t70/t80/t90) frames, each anchored to a review quote in
`edit/hyperframes/film-v3/REVIEW.md`. Pixel sampling found no near-static hold
longer than 5 s (temporal_coverage passes at fps=2, scale=160:90).

Narration metadata totals 148.84 s including tool-provided tail holds; the
encoded MP4 is 148.87 s.

The automatic delivery check is `scripts/check-delivery.py`; it passes.
Bootstrap validation and a successful encode establish feature completion when
paired with the recorded review evidence above. Publication awaits the owner's
authorization.
