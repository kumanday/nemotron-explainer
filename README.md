# Nemotron Explainer

An experiment in agent-made video: can an open, low-cost vision-language model,
**NVIDIA Nemotron 3.5 Super VL (120B-A12B) on Nebius Token Factory**, produce
correct, good-looking motion-graphics video when it is given a real production
pipeline and the guardrails a human designer relies on?

Built for the [Nebius Global AI Hackathon](https://nebiusglobalaihackathon.devpost.com/).
The submission film is produced by this workflow, with Nemotron writing the
storyboard, script, compositions and reviews.

## How it uses NVIDIA Nemotron and Nebius Token Factory

**Model:** `nvidia/Nemotron-3.5-Super-VL` (120B total, 12B active, reasoning,
text and image input, 262K context), served by **Nebius Token Factory** at the
US North 1 endpoint in [`configs/nebius.json`](configs/nebius.json). Every model
call in the project goes to this one model; nothing falls back to another
provider.

Nemotron does four jobs:

1. **Agent.** It runs inside Pi and writes the storyboard, narration script,
   HyperFrames compositions and code fixes, using Pi's read, bash, edit and
   write tools.
2. **Eyes.** It reads frames sampled from its own encoded render (up to eight
   images per request) and reviews them against a five-axis rubric.
3. **Blind reviewer.** [`scripts/blind-review.py`](scripts/blind-review.py)
   makes a fresh call that sees only the brief and the frames, so the review
   isn't biased by the agent's plan.
4. **One-shot baseline.** [`scripts/one-shot.py`](scripts/one-shot.py) makes
   the single no-tools call that the Code2Video benchmark measures.

**Where Token Factory sped up the work**

- **One-file integration.** Token Factory exposes an OpenAI-compatible API, so
  [`.pi/extensions/nebius.ts`](.pi/extensions/nebius.ts) registers it in Pi
  with no GPU hosting or model serving on our side.
- **Many cheap calls.** The loop depends on looking often. The usage ledger
  records 925 model calls across 7 Pi sessions in about eight hours on
  2026-10-30: 7.5M input tokens, 111M cached-prompt tokens and 0.77M output
  tokens, about $36 at list price ($0.30 per million input, $0.90 per million
  output).
- **Fast reviews.** A blind review of one render takes about 18 seconds and
  costs under one cent, so every round gets one.
- **Long sessions.** The 262K context window holds a full production session
  with its tool output and image history.

Token Factory is the only Nebius service used. Rendering runs locally.

## Why

Artificial Analysis'
[Code2Video benchmark](https://artificialanalysis.ai/articles/code2video-aa) asks
models to write a HyperFrames composition from a brief in a single call, with no
tools and no chance to see the result. Nemotron 3 Ultra ranked last of 27 models
([data](briefs/data/code2video-aa-2026-10.json)). Human motion designers render,
look at the result and fix it. This project tests whether a newer Nemotron model,
given that same loop, closes the gap. If it does, it is a
practical low-cost option for motion graphics.

The experiment builds on media tools I had already written and adds a
considerable amount of new code, tooling and quality guardrails so that
different models, such as Nemotron, can use them and produce reliable work.

## What is reused

- **[Media Tooling](https://github.com/kumanday/media-tooling)**: narration
  (ElevenLabs eleven_v4 with per-word timings), generated-media requests,
  approvals and take selection, verification.
- **[TTV Pipeline](https://github.com/kumanday/ttv-pipeline)**: text/image-to-video
  generation behind an immutable request → plan → approve → execute → import handoff.
- **HyperFrames**: HTML + GSAP compositions rendered to video.
- **Pi**: the coding-agent harness (agent loop, tools, sessions).

Their source stays in their own repositories; this project calls the installed
commands.

## What is new here

**Running Nemotron in Pi on Nebius**

- [`.pi/extensions/nebius.ts`](.pi/extensions/nebius.ts): registers the exact
  regional endpoint and model from [`configs/nebius.json`](configs/nebius.json),
  and keeps a metadata-only usage ledger (no prompts or reasoning).
- [`.pi/lib/image-limit.mjs`](.pi/lib/image-limit.mjs): Nebius accepts at most
  eight images per request, counting replayed history. The adapter sends the
  newest eight and marks older ones as omitted, so long visual-review sessions
  don't fail.
- [`.pi/lib/scoped-search.mjs`](.pi/lib/scoped-search.mjs): blocks whole-disk
  `find /` style searches that stall the agent.
- [`scripts/smoke-pi.py`](scripts/smoke-pi.py),
  [`scripts/check-pi-setup.mjs`](scripts/check-pi-setup.mjs),
  [`scripts/doctor.py`](scripts/doctor.py): route, tool and prerequisite checks
  that never print credentials.

**Guardrails that make the output checkable**

- [`scripts/cues.py`](scripts/cues.py): reveals are timed to `{@cue}` markers in
  the narration script, not hand-typed seconds. It generates the cue table each
  scene uses and fails on stale or missing cues.
- [`scripts/blind-review.py`](scripts/blind-review.py): a fresh Nemotron call
  that sees only the brief and frames from the encoded video. The agent's own
  review, written with its plan in context, reported missing elements as present;
  the blind reviewer found them.
- [`scripts/check-delivery.py`](scripts/check-delivery.py): delivery gates for
  duration, cue sync, layout overflow (via `hyperframes check`), static holds,
  generated footage actually in the encode, hashes and review coverage.
  Quality itself is judged by the reviews.
- [`scripts/one-shot.py`](scripts/one-shot.py): the Code2Video-style baseline.
  One call, no tools, with token and cost receipts.
- [`scripts/select-take.py`](scripts/select-take.py),
  [`scripts/ttv-round`](scripts/ttv-round): project glue for the TTV handoff.

**Instructions for the model**

- [`.pi/APPEND_SYSTEM.md`](.pi/APPEND_SYSTEM.md): rules loaded into every turn
  (cue timing, no overflow, large type, no blinking, footage as a layer, blind
  review every render).
- [`.pi/skills/hybrid-explainer/`](.pi/skills/hybrid-explainer/SKILL.md): the
  production skill, with [craft rules](.pi/skills/hybrid-explainer/references/craft-rules.md)
  and a [five-axis review rubric](.pi/skills/hybrid-explainer/references/review-rubric.md)
  matching the Code2Video judge (Engagement, Prompt-Intent, Composition,
  Temporal, Craft).
- [`storyboards/v3/DIRECTION.md`](storyboards/v3/DIRECTION.md): the human
  direction for the film. Nemotron builds everything from it.
- [`briefs/example-tidepool.md`](briefs/example-tidepool.md): the worked
  example, an 8-second Code2Video-style brief.

## The experiment

The same brief runs twice through Nemotron 3.5 Super VL:

1. **One shot** (`scripts/one-shot.py`): the benchmark's condition.
2. **The loop**: Nemotron writes the composition, renders it, reads frames from
   the encode, gets a blind review, fixes the located defects, and repeats.

Each round keeps its frames, review, real `diff -u` of the source, render hash,
tokens and cost under [`analysis/example/`](analysis/example/)
([summary](analysis/example/summary.json)). The film shows both results.

## Status

Work in progress; this repository is updated as production continues.
[STATUS.md](STATUS.md) is the current state, [RECOVER.md](RECOVER.md) is the brief
the agent is following, and [`edit/project.md`](edit/project.md) is its
production log. Earlier attempts (v1, v2) and why they were rejected are kept in
[`docs/archive/`](docs/archive/) and `edit/hyperframes/self-demo*/` as part of the
record.

## Setup

Tested on macOS with Pi 1.1.0, HyperFrames 0.8.142, Node 25 and Python 3.14.

1. Clone this repository:

   ```sh
   git clone https://github.com/kumanday/nemotron-explainer.git
   cd nemotron-explainer
   ```

2. Install the tools:

   ```sh
   brew install uv ffmpeg node
   npm install -g hyperframes@0.8.142
   uv tool install "media-tooling[elevenlabs] @ git+https://github.com/kumanday/media-tooling"
   media-tooling-link-skills
   ```

   Install the Pi coding agent (1.1.0). For generated footage, also clone
   [TTV Pipeline](https://github.com/kumanday/ttv-pipeline) and run
   `uv sync --extra dev` in it.

3. Set credentials in your environment (never on the command line):

   - `NEBIUS_API_KEY`: required, from Nebius Token Factory.
   - `ELEVENLABS_API_KEY` and `ELEVENLABS_VOICE_ID_EN`: narration.
   - `FAL_KEY`: generated footage.

4. Point Pi at the skills on your machine. [`.pi/settings.json`](.pi/settings.json)
   lists the Media Tooling and HyperFrames skill folders by absolute path;
   change them to where `media-tooling-link-skills` put them (usually
   `~/.agents/skills/`).

5. Check the setup. These print which commands and credentials are present,
   never their values:

   ```sh
   python3 scripts/doctor.py
   node scripts/check-pi-setup.mjs
   python3 scripts/smoke-pi.py   # small paid call: Pi tools and image reading
   ```

## Running it

```sh
./scripts/recover-pi            # fresh Pi session on the current brief
./scripts/recover-pi --continue # resume the last session
```

One-shot and blind review on their own:

```sh
python3 scripts/one-shot.py --brief briefs/example-tidepool.md --out edit/hyperframes/my-v0
python3 scripts/blind-review.py --brief briefs/example-tidepool.md \
  --render renders/tidepool-r7.mp4 --out analysis/my-blind
```

Tests and delivery checks:

```sh
node --test tests/image-limit.test.mjs tests/scoped-search.test.mjs
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/check-delivery.py
```

## Not in this repository

Raw Pi sessions, provider logs, renders, narration audio and generated footage
are kept local (see [.gitignore](.gitignore)). Review frames, diffs, receipts and
sanitized evidence are included. Some records contain absolute paths from the
machine the film was made on.

## License

[MIT](LICENSE) for the code and composition source in this repository.
Media Tooling, TTV Pipeline and HyperFrames keep their own licenses, and
generated narration and footage stay under their providers' terms (see
[submission/LICENSE.md](submission/LICENSE.md)).
