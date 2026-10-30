# Setup diagnosis and recovery

The current prototype is incomplete. Actual encode inspection and the native Pi
session support these findings:

- The needed skills are installed. Pi read the high-level media-motion-graphics,
  media-tts, HyperFrames router, explainer/format and CLI guidance. It did not
  read the detailed creative house-style, video-composition or animation guidance.
- The source has basic entrance tweens and screenshots, with no video layer.
  The encode has a near-static interval from about 37 to 56 seconds and small
  text on a mostly empty canvas. This fails the requested explanatory motion.
- There are no executed TTV request/plan/approval/import/select commands in the
  production trace. The stated pricing blocker had not been resolved.
- STORYBOARD, SPEC and a numerical design spec are absent. The source contains
  text describing storyboard stages rather than the required production records.
- Edit calls with `oldString`/`newString` failed validation. Later calls used the
  correct `edits[].oldText`/`newText` shape and succeeded. This recovered error is
  separate from the missing product features.
- Narration metadata totals 96.24 s because it includes 0.6 s tail holds and a
  1.6 s final hold. The MP3s/root timeline total 91.04 s. Timing should account
  for these holds; the difference does not establish clipped spoken words.
- The prototype's before/after presentation uses a terminal screenshot and a
  different scene snapshot. A visual repair comparison needs matching subjects,
  timestamps and crops.

The bootstrap's smoke established API/tool/image interoperability. It did not
establish that the model follows the craft workflow or meets product acceptance.
The setup now includes always-loaded requirements, a required project skill,
explicit craft resources, a current conservative video quote, a local TTV wrapper,
and a delivery checker that rejects the current prototype. It also provides the
correct edit schema and exit-code guidance.

Run `./scripts/recover-pi` for a fresh session using the recovery brief. It keeps
the existing project files and asks Nemotron to make a 15–20 second mixed-media
proof before expanding to the final film. To test the existing session instead,
run `/reload`, then ask it to read `RECOVER.md` and proceed.

The checker verifies required evidence and catches clear omissions. It does not
prove artistic quality or that the model's own review is accurate. If the short
proof fails after two visual passes, record that capability limit and inspect the
result before attempting another long film. No replacement film or paid media
was generated as part of this setup repair.
