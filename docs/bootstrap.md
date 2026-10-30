# Bootstrap evidence

Bootstrap performed on October 29, 2026, America/Bogota. Film production remains
the next task for Pi; this document describes only the prepared environment.

## Installed route

- Pi CLI: 1.1.0.
- HyperFrames CLI: 0.8.142.
- Media Tooling source: `daa6482597ba418fd0aeee504cf78f2ecba5cdde`.
- TTV Pipeline source: `078107e401c2602ec77e9a15ef095ada9b8257cd`.
- Exact endpoint/model: `configs/nebius.json`.
- Environment availability was checked without reading key values into context.
  Nebius, Fal, ElevenLabs, configured English voice and image-provider credentials
  were present. Presence does not verify those media providers' current billing
  access. No paid media generation was attempted.

## Verified behavior

1. Authenticated `GET /models` on the supplied regional endpoint listed the exact
   model ID.
2. A direct Chat Completions probe returned HTTP 200, the expected model, `stop`,
   the requested short answer and token usage including reasoning tokens. It
   accepted `reasoning_effort: high`; effort semantics remain provider-defined.
3. The real Pi CLI loaded the project provider and completed the visual/tool
   smoke. Pi read a synthetic image, sent it as image input to the model, wrote
   correct color observations and stopped cleanly. The metadata retained usage
   across three provider requests. See `analysis/bootstrap-smoke.json`.
4. A separate fresh session using project defaults, with no explicit provider or
   model flag, selected `nebius-hackathon/nvidia/Nemotron-3.5-Super-VL` and returned
   `BOOTSTRAP_READY` with a clean stop.

The project omits `enabledModels`: this Pi release resolves that scope before
legacy extension models are registered, producing a startup warning. Project
defaults and the explicit launcher select the verified route. `/demo-route`
reports the current selection. Changing models intentionally changes authorship;
the metadata ledger records any such selection.

## Remaining production checks

Run-time media generation, TTV import, narration, HyperFrames composition and
rendering, video review and public packaging still need to be demonstrated on
the new project. Native video transport, long contexts and maximum response
length have not been tested. No EBO integration is required.

Source documentation consulted: the installed Pi 1.1.0 model, custom-provider,
configuration, settings, extension docs and exported event declarations; Media
Tooling's generated-media documentation and motion-graphics/TTS skills; TTV's
integration README and validation record; the current HyperFrames router.
