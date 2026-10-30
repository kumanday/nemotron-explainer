# Tool source and selection lookup

Run `python3 scripts/tool-locations.py` for exact installed paths. The
`media-generated` entry point is in uv's tool environment. Its editable import
points to `/Users/magos/dev/media-tooling/src/media_tooling/generated_media.py`.
`generated_media.py` is a file. Searching for a directory named `generated_media*`
cannot locate it. No machine-wide search is necessary.

```sh
rg -n 'Selection revision already exists' \
  /Users/magos/dev/media-tooling/src/media_tooling/generated_media.py
```

TTV's source checkout is `/Users/magos/dev/kumanday/ttv-pipeline`. The wrapper
`./scripts/ttv-round` is a zsh executable: invoke it directly, not through Python.

## Selection state

User-authored drafts live under `rough-cuts/manifests/drafts/`; native sealed
selections live under `rough-cuts/manifests/selections/`. The CLI creates a
timestamp, hashes and EDL while sealing a draft. Placing a draft at the canonical
output path causes a revision collision when `select` writes different bytes.

The drafts are preserved as:

- `rough-cuts/manifests/drafts/edit-1.source.json`
- `rough-cuts/manifests/drafts/edit-2.source.json`

The generated video result has already succeeded. The current canonical selection
is `rough-cuts/manifests/selections/edit-proof-99.json`, with
`edit/edl-edit-proof-99.json`. Its native selection validation passes. Continue
from these records without regenerating footage.
For an actual edit, use a new `edit_revision_id`; retain older canonical records.

| File | Owner | Purpose |
|---|---|---|
| `rough-cuts/manifests/drafts/NAME.source.json` | Agent | Editable input JSON |
| `rough-cuts/manifests/selections/ID.json` | Native CLI | Immutable compiled output |
| `edit/edl-ID.json` | Native CLI | Generated EDL |

Use this wrapper for selection:

```sh
python3 scripts/select-take.py rough-cuts/manifests/drafts/edit-proof-99.json
```

It rejects drafts in the output directory and reuses an existing matching
selection without recompiling it. Changed editorial decisions require a new ID.
Keep canonical selections intact. When Python import inspection is necessary,
use the interpreter printed by `scripts/tool-locations.py`: system `python3`
does not contain uv's isolated tool installation.

Whole-filesystem searches are blocked for this workflow. The guard recognizes
common literal root searches; it is a convenience guard, not a shell sandbox.
