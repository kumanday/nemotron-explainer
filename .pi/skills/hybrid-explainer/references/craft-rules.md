# Craft rules that v1 and v2 broke

Each rule comes from a defect seen in an earlier encode. They are checked in review.

## Timing

- Every reveal is placed with a narration cue: `CUE.name` or `CUE.name + offset`
  (offsets of −0.15 to +0.4 s). Bare numbers above 0.75 s are rejected by
  `scripts/cues.py --check`. Pattern for a scene script:

  ```js
  /* @cues frame=4 */ /* @end-cues */
  const tl = gsap.timeline({ paused: true });
  tl.from("#player", { y: 80, opacity: 0, duration: 0.7, ease: "expo.out" }, CUE.oneshot);
  tl.from("#receipt", { opacity: 0, duration: 0.4 }, CUE.oneshot + 0.3);
  tl.to("#player .scrub", { scaleX: 1, duration: 8, ease: "none" }, CUE.v0);
  window.__timelines["oneshot"] = tl;
  ```

  Run `python3 scripts/cues.py SLOT` after every `media-tts-frames` run; it fills
  the block and writes `CUES.md`, the cue sheet you build from.
- Cue names are lowercase letters, digits and underscores.
- Scene host `data-start`/`data-duration` and voice `<audio>` windows come from
  `audio_meta.json` `duration_s` (tail hold included). The checker compares them.
  v2 cut its last voice clip 80 ms before the final word ended.
- Text that is read stays still. Kinetic word-by-word reveals only for hero lines
  of six words or fewer, and only in sync with the voice.

## Layout

- Minimum type 32 px at 1080p (metadata chips 28 px). Body 48–56 px.
- One focal object per shot covering at least 40% of the frame. No shot is a
  small block of text floating in an empty dark frame.
- Position with absolute coordinates on the 1920×1080 grid, or a flex container
  whose children never mount/unmount. Never give `.clip` timing to children of a
  flow layout: when one unmounts, its siblings jump (v2 credits list).
- Anything that can be long (code, briefs, lists) gets a fixed panel with
  `overflow:hidden` and a measured height. If it does not fit, scroll it with a
  tween or show fewer lines. Never let content set its own height (v2 brief
  overflowed the frame).
- Real screenshots and terminal output are never shown whole. Crop to the 3–6
  lines that matter and scale so the text is at least 32 px, or push in on the
  region with a transform.

## Lifecycle

- Every element either stays until its scene ends or leaves by a tween that
  finishes at least 0.1 s before its clip ends. Nothing blinks off when a clip
  window closes.
- Do not tween `display`, `visibility` or `autoAlpha` on a `.clip` element;
  animate a child.

## Generated footage

- Generated clips are layers in a designed frame: inside the player, inside the
  phone, behind type with a grade, or as an asset card. Not a full-frame plate
  with a caption that then cuts away.
- Mute it (`muted`), set `data-start`/`data-duration` on the video or its
  wrapper, never both, and confirm in the encode that it moves (two frames
  0.5 s apart differ).

## Transitions

- Carry an object across scene boundaries (the spine, the player, a card), or use
  a registry transition. Never cut to an empty ground.
