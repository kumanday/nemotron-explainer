# Example brief: a second input for the nemotron-explainer workflow

## Subject
Explain what an API is, in 90–120 seconds, using the same nemotron-explainer
workflow: brief → model run → storyboard → motion graphics → visual review → render.

## Format
- English, 1920×1080, 30 fps, 90–120 seconds (strictly under 180 s).
- ElevenLabs eleven_v4 narration (configured voice), no music/SFX.
- Motion graphics with real captures; 1–2 muted generated clips optional.
- Every on-screen element traces to an actual artifact.

## Suggested beats
1. Hook: "An API is a contract between two programs."
2. Input: this brief shown on screen beside a real run capture.
3. Build: storyboard cells (request, endpoint, response) and composition source.
4. Review: an inspected frame with one evidenced revision.
5. Finished result: a coherent passage built from real captures and graphics.
6. How this was made: accurate component roles (Pi, Nemotron, Media Tooling, TTV, HyperFrames, eleven_v4).
7. Claim: "This video was created using this tool."

## Reproducible commands
```sh
media-tts-frames <this-brief-dir>/SCRIPT.md --hyperframes <composition-root> --out <composition-root>/audio_meta.json
cd <composition-root>
npx hyperframes lint && npx hyperframes check --json
npx hyperframes render --quality delivery --output ../../renders/example-demo.mp4
```
