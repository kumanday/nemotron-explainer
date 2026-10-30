# Delivery verification

Status: incomplete. `renders/submission-demo.mp4` is a prototype, not the accepted
mixed-media submission film. Its SHA-256 is
`dfce15b157152339073aa10bcc9105eaea4ff94d1d67c9ede017f8cb79fde732`.

Verified media properties: H.264/AAC MP4, 1920×1080, 30 fps, approximately 91.07 s.
The source contains basic entrance tweens, text and screenshots. It has no video
content layer and there are no executed TTV generation/import records.

Required work: actual TTV footage in the encode; explanatory motion graphics;
STORYBOARD and numerical design/motion specs; legible video-scale type; temporal
review tied to the actual encoded artifact. Pixel sampling found a near-static
hold from about 37 to 56 s. Before/after evidence must compare the same scene,
timestamp and crop. Current before/after source images show different subjects.

Narration metadata totals 96.24 s including tool-provided tail holds. Raw MP3s
and the composition total 91.04 s. Account for holds in the revised timing plan;
this difference alone does not establish clipped speech.

The automatic delivery check is `analysis/delivery-check.json`. It currently
fails. Bootstrap validation and a successful encode establish neither feature
completion nor artistic quality. Produce the versioned candidate using
`RECOVER.md`, run the delivery checker and record new evidence before publication.
