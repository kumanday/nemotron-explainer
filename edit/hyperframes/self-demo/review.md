# Pilot visual review (TASK-002)

## Review mode
auto — Nemotron inspected actual storyboard cells and sampled frames from the
seekable composition; real motion/audio checked via the draft encode.

## Inspected frames
- frame-00-at-2.5s.png — hook: "Pilot - 10-20 s - 1080p30" / "Made by this tool" / subtitle. Clean dark card, readable type, accent kicker.
- frame-01-at-7.8s.png — input: briefs/pilot.md panel beside a genuine terminal capture of the media-tts-frames run. Legible at delivery size.
- frame-02-at-12.7s.png — build: three storyboard cells (hook/input/build) plus a composition source snippet. Readable.
- frame-03-at-17s.png — claim: "This video was created using this tool." with component credits. Readable.

## Disposition
passed — no blocking issue. One correction applied before this pass: mojibake
(`·`, `–`, `—`) in hook kicker, input label and claim credits replaced with
plain ASCII hyphens; re-snapshots confirmed clean rendering.

## Evidence
- renders/pilot-draft.mp4: 1920×1080, 30 fps, 19.24 s, H.264/AAC (ffprobe).
- audio_meta.json: 4 voices, eleven_v4, 19.24 s total.
- assets/captures/tts-run.png: genuine terminal capture of the narrated run.
- snapshots/ and contact-sheet.jpg: sampled frames.

## Review test (labeled)
This first render needed no defect; the mojibake correction was caught during
the snapshot review and fixed before delivery. No defect was staged.
