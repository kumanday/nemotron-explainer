# DECISIONS — self-demo composition slot

## Review scope
review-mode: auto (recorded in BRIEF.md). Nemotron inspects actual storyboard cells and
draft/encoded frames with Pi's image-capable read; two visual review passes max; real
motion/audio checked on short boundary clips.

## Creative direction (settled)
- Subject: the nemotron-explainer workflow demonstrating itself (finite self-demo: one
  pilot supplies genuine process footage; the submission film reuses those captures).
- Visual direction: restrained dark theme, readable type, small accent palette; 1920×1080
  30 fps; captions and key text inside title-safe (80%), content inside action-safe (90%).
- Generated footage: 1–2 TTV clips, audio muted; keyframe review before video approval
  where cost permits.
- Narration: media-tts-frames, eleven_v4, configured English voice; re-voice whole script
  on wording changes.
- No music/SFX. Render locally; no cloud profile.

## Spending permission (carried from user)
- $100 cumulative media budget (configs/budget.json); reservations and all attempts tracked
  in analysis/media-budget.json; inference tracked separately.
- Explicit reviewed variant IDs required before any paid generation; credible cost ceiling
  established before each approval; unknown costs recorded as unknown, never inferred from
  raw provider units.
- Existing user permission covers narration and planned generated footage within budget.

## Component credits
- Pi 1.1.0: agent loop, tools, sessions, route/usage evidence; model nvidia/Nemotron-3.5-Super-VL
  on https://api.tokenfactory.us-north1.nebius.com/v1/ (provider nebius-hackathon).
- Media Tooling daa6482…: narration, assembly, delivery checks.
- TTV Pipeline 078107e…: generated footage planning and import.
- HyperFrames 0.8.142: editable motion graphics and local render.
- Bootstrap/task scaffolding: Codex and human direction.
