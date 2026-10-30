# Creative brief: the tool makes its own demonstration

## Audience and promise

AI builders and independent creators. Show that a model can plan and build an
explainer, inspect its visual output and make a useful editorial revision using
existing media tools. The submission film is itself an output of the workflow.

## Format

- English, landscape 1920×1080, 30 fps, 90–120 seconds; strictly under 180 seconds.
- Clear narration using Media Tooling's configured English voice and `eleven_v4`.
- Precise motion graphics for structure and explanation; 1–2 generated clips for
  an intentional visual thread. Actual tool captures supply the demonstration.
- A restrained dark visual direction with readable type and a small accent
  palette. Use real evidence at a readable scale. Choose fonts from installed or
  bundled sources. Keep titles/captions inside safe areas.
- No music or SFX is requested. Mute generated-clip audio.

## Suggested story beats

These are narrative goals, not finished narration. Author the final script from
the work that actually succeeds.

| Beat | Approximate share | What the viewer sees |
|---|---|---|
| Hook | 0–10 s | A polished moment from the result and the self-authorship premise |
| Input | 10–25 s | A real short Markdown brief and a real Pi/Nebius run |
| Build | 25–45 s | Storyboard, one TTV asset handoff, editable motion graphics |
| See and revise | 45–75 s | Actual inspected frames, a specific decision, an honest before/after or labeled test |
| Finished result | 75–95 s | A coherent passage from the generated explainer |
| How this film was made | 95–120 s | The same pipeline making this submission film; accurate component roles and measured facts |

Keep every beat tied to an actual artifact. Genuine footage of the workflow
should remain legible; animation alone is not a demonstration of operation.

## Grounded facts

- Harness: Pi, currently installed version 1.1.0.
- Reasoning/vision/composition model: `nvidia/Nemotron-3.5-Super-VL` through
  `https://api.tokenfactory.us-north1.nebius.com/v1/`.
- Media Tooling supplies processing, narration, assembly and delivery checks.
- TTV Pipeline supplies reviewed provider plans, generated assets and attempts.
- HyperFrames supplies editable HTML/GSAP motion graphics and rendering.
- Code and plan scaffolding were prepared with Codex and human direction.
- EBO is optional. No benchmark or quality/cost advantage is established.

The final film may say “This video was created using this tool” when its actual
script, composition, review and render follow this workflow. Credit video and
voice generation separately. Show measured costs only with their coverage and
uncertainty. Keep final narrative copy canonical and remove superseded claims.

## Production records

Use `edit/hyperframes/self-demo/` for composition source, BRIEF, design spec,
storyboard, narration metadata and decisions. Use `storyboards/` for immutable
TTV handoffs, `generation/` for local provider execution, and
`renders/submission-demo.mp4` for delivery. Create `submission/provenance.json`
and `submission/verification.md` from real records.
