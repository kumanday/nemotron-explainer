# tidepool-loop — round 1 review

Render: `renders/tidepool-r1.mp4` (SHA-256 `22d38dad6441421712c28ef00ba5fd303bcb96753646a274599e968f12aa196b`), 8.0 s, 1080p30, silent.
Sampled: `analysis/example/r1/t0.5..t7.6.png`. Frame source: the encoded MP4.

## Axis scores (1–5)

**Engagement: 4** — Opening full-bleed tide-pool at golden hour is striking; the sweep, phone rise, curve draw and headline landing give a change every ~2 s. Nothing flat for more than ~2.6 s.

**Prompt-Intent: 5** — Every brief beat happens at its stated time: 0.0–2.6 full-bleed tide pool with the thin light sweep (t0.5, t1.5); 2.6 footage shrinks into the rising phone still playing (t2.6–t4.2); 5.2 headline "Know the tide before you go." lands beside the phone; wordmark "Tidepool" and tagline "Free on iOS and Android" at 6.2; everything settles and holds to 8.0.

**Composition: 4** — One focal object: the tide pool fills the frame opening, then the phone (~60% frame height) + curve on the right is the clear focal mass; asymmetric balance (phone left, type right), type hierarchy 110 px headline / 32 px labels / 28–32 metadata. No centred stack; no area >50% empty in the type half.

**Temporal: 4** — Eases have weight (expo.out phone arrival, power2.inOut curve draw); reveals land on the brief beats; text lands and stays still while read; exits finish before scene end. The sweep and full-bleed clip end via tween/cut at 2.6 with no blink.

**Craft: 4** — Nothing clipped or overlapping; type ≥32 px (headline 110, labels 32, wordmark 60, tagline 32); video plays (frames differ 0.5 s apart); `hyperframes lint` reports 0 errors. Fonts load from Google Fonts (Inter).

## Located findings

None at blocker or major severity. One minor observation:

- id: f1
  axis: Engagement
  severity: minor
  time_s: 0.5–1.5
  region: full frame
  saw: Full-bleed tide pool holds for 2.6 s with only the subtle light sweep moving; the ripples in the source clip are gentle.
  cause: Brief asks to "hold the viewer on the water" for 0.0–2.6 s, so the long hold is intentional.
  fix: None — the hold is per brief; the sweep and ripples provide the needed movement.

## Verdict

No blocker or major finding. The round satisfies the brief: footage is a layer inside a designed frame (phone + type), not a captioned full-frame insert; type ≥32 px; one focal object ≥40% of frame; reveals on beats; nothing blinking. Stop the loop after r1 (no blocker/major finding).
