# Upload and publication checklist (draft — awaits user authorization)

Production is incomplete. Before publication, produce the required TTV footage
and explanatory motion graphics, pass `scripts/check-delivery.py` on the new
candidate, and inspect its actual encoded video. Use the accepted artifact path
and verified facts for every item below.

## Pre-publication (owner review)
- [ ] Owner approves the proposed license (`submission/LICENSE.md`, MIT)
- [ ] Owner reviews `submission/provenance.json`, `submission/verification.md`
- [ ] Owner reviews `submission/attribution.md` and `submission/devpost-description.md`
- [ ] Owner confirms no credentials, signed URLs, private transcripts, or hidden
      reasoning are in any public file

## Repository (do not push without authorization)
- [ ] Create public repository
- [ ] Add `LICENSE` (owner-approved), `README.md`, example brief
- [ ] Include source (`edit/hyperframes/self-demo/`), permitted assets, and
      retrieval instructions for media (narration/generated footage via their
      providers)
- [ ] Add `submission/` package (provenance, verification, attribution,
      Devpost description, upload checklist)
- [ ] Pin dependency versions (Pi 1.1.0, HyperFrames 0.8.142, Media Tooling
      source revision)

## YouTube demonstration (under 3 minutes)
- [ ] Upload the accepted versioned MP4 (under 180 s, 1080p30, H.264/AAC)
- [ ] Title and description referencing the workflow and component roles
- [ ] Link to the public repository
- [ ] Set as the hackathon demo video

## Devpost entry
- [ ] Fill in project name: Nemotron Explainer
- [ ] Use `submission/devpost-description.md`
- [ ] Category: Best Apps and Agents
- [ ] Add repository URL and YouTube video URL
- [ ] Submit before the deadline: 2026-10-30 12:00 America/Bogota

## Notes
- Target final video by 10:30, submission preparation by 11:00, leaving an hour
  for the user's publication decisions and uploads.
- No public upload, repository push, or submission occurs without the user's
  explicit authorization.
