# tidepool-loop — round 7 review

Render: `renders/tidepool-r7.mp4`, 8.0 s, 1080p30, silent.
Sampled: `analysis/example/r7/t0.5..t7.6.png`. Frame source: the encoded MP4.

## Axis scores (1–5)

**Engagement: 5** — Opening full-bleed tide pool at golden hour is striking; the light sweep crosses the frame in the opening, then the footage shrinks into a rising phone, the tide curve draws, and the headline lands. Something changes every ~2 s.

**Prompt-Intent: 5** — Every brief beat happens at its stated time: 0.0–2.6 full-bleed tide pool with a thin light sweep (t0.5, t1.5); 2.6 footage shrinks into the phone screen still playing, phone rises from the bottom edge and stays fully contained (t2.6–t4.2); beside the phone the tide curve draws left to right and the dot rides it to "Low tide 4:12 PM" (t3.4–t5.2); 5.2 headline "Know the tide before you go." lands beside the phone; wordmark "Tidepool" and tagline "Free on iOS and Android" at 6.2; everything settles and holds to 8.0 (t6.4, t7.6).

**Composition: 5** — One focal object: the tide pool fills the frame opening, then the phone (~60% of frame height, fully contained, never cropped) plus the curve on the right is the clear focal mass; asymmetric balance (phone left, type right); type hierarchy 100 px headline / 56 px wordmark / 32 px labels. No centred stack.

**Temporal: 5** — Eases have weight (expo.out phone arrival, power2.inOut curve draw); reveals land on the brief beats; text lands and stays still while read; nothing blinks; sweep and clip end via tween at 2.6.

**Craft: 5** — Nothing clipped or overlapping; phone is a real device with speaker/camera/home chrome; type ≥ 32 px; video plays (frames differ 0.5 s apart); `hyperframes lint` reports 0 errors; the sweep, curve dot, wordmark and tagline are all separated (no overlap).

## Located findings

None at blocker, major or minor severity.

## Verdict

No blocker or major finding. The loop stops after round 7. The example now satisfies every brief beat and every craft rule: footage is a layer inside a designed frame (phone + type), not a captioned full-frame insert; one focal object ≥ 40% of frame; type ≥ 32 px; reveals on narration beats; nothing blinking; no overflow.

## Agreement with the blind review

The blind review of r7 (fresh call, brief + frames only) scored all five axes 5/5 with zero findings and agrees: sweep present at t0.5/t1.5, phone present and fully contained, curve/dot/label present, headline/wordmark/tagline present with no overlap. This round resolves every r1 defect the blind review found (missing tide curve, missing "Low tide 4:12 PM" label, wordmark/headline overlap, phone cropped by the bottom edge).
