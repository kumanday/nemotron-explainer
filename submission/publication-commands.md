# Draft publication commands (do not run without user authorization)

```sh
# 1. Verify the final artifact before anything public
ffprobe -v error -select_streams v:0 \
  -show_entries stream=width,height,r_frame_rate,codec_name,duration \
  -of csv=p=0 renders/submission-demo.mp4
# expect: 1920,1080,30/1,h264,~91.04

# 2. Open the local preview to confirm it plays
open submission/preview.html   # or open in any browser

# 3. Create the public repository (owner action)
gh repo create nemotron-explainer --public --source=. --remote origin

# 4. Add license and push (owner action, after license approval)
git add -A   # .gitignore keeps sessions, evidence, renders and media out
git commit -m "Prepare hackathon submission: workflow + explainer film"
git push -u origin main

# 5. Upload the video to YouTube (owner action)
# Upload renders/submission-demo.mp4 (91 s, under 180 s cap)

# 6. Submit to Devpost (owner action, before 2026-10-30 12:00 America/Bogota)
# Use submission/devpost-description.md; add repo URL and YouTube URL
```

## Boundary
Publication (repository push, YouTube upload, Devpost submission) awaits the
user's explicit authorization. None of the above commands should be run until
the owner approves.
