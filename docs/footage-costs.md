# Footage quote for the demo

Checked October 29, 2026, America/Bogota. The existing $100 cumulative media
authorization covers footage, keyframes and narration. No new permission is
needed for an operation that fits this scope and remaining budget.

Fal's official MiniMax H3 Max Turbo page states that its promotional discount
ends October 31, followed by these standard video rates:

| Resolution | Standard USD/second | Five-second video |
|---|---:|---:|
| 480p | 0.025 | 0.125 |
| 768p | 0.04 | 0.20 |
| 1080p | 0.08 | 0.40 |

Use the higher standard rate as a conservative planning basis while the stated
discount applies. Two five-second 1080p clips with two attempts each reserve
$1.60 for video generation. This example is a quote calculation, not executed
work or an invoice. Keyframe generation, other endpoints, provider extras and
narration are separate line items. Confirm the exact payload and rate before
execution. Actual USD may remain unknown in TTV; retain raw billable units and
the quote without converting units into invented charges.

Endpoint: `minimax/h3-max-turbo/image-to-video`.
Use the existing TTV adapter and approved variants, not a direct substitute call.

[Official Fal endpoint and rate note](https://fal.ai/models/minimax/h3-max-turbo/image-to-video)

The local TTV file adapter's help command was verified:

```sh
cd /Users/magos/dev/kumanday/ttv-pipeline
uv run --locked python -m api.generation_handoff --help
```

Its plan/approve/run/result commands are available. This check establishes local
adapter readiness, not provider billing or a completed generation. The Fal MCP
connection needs reauthentication; the installed TTV path uses the existing Fal
environment key independently.
