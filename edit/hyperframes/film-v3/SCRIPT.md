## Line 1 — board (Frame 1)
    Artificial Analysis ranked twenty-seven models on Code2Video. Each writes a HyperFrames composition, it renders, and a judge compares the videos. {@last}Nemotron 3 Ultra came last. {@rules}One call, no tools, no look at its own render.

## Line 2 — loop (Frame 2)
    Nobody designs motion graphics that way. {@loop}You render, look, and fix. {@vl}Nemotron 3.5 Super VL reads images, so we gave it that loop: {@tools}a harness, render tools, and its own render.

## Line 3 — brief (Frame 3)
    Here's a Code2Video-style brief: an eight-second launch hook for Tidepool, a made-up tide app. {@clip}It comes with one generated clip of a tide pool. {@rest}Everything else — the phone, the tide curve, the type — is built in code.

## Line 4 — oneshot (Frame 4)
    First, the benchmark condition: one call, no tools. {@v0}This is what Nemotron 3.5 Super VL wrote on its first try. {@look}It didn't render — it hit the token limit and produced no HTML.

## Line 5 — look (Frame 5)
    Now the loop. The agent samples frames from its own render {@strip} and reads them like text. {@axes}It scores the five axes: engagement, prompt intent, composition, timing, craft. {@f1}Its own review scored the render 5/5 on prompt intent — but a blind review, shown only the brief and the frames, found the tide curve missing and the wordmark on the headline. {@f2}So the loop looks again, blind, and fixes what the first look missed.

## Line 6 — fix (Frame 6)
    Then it edits its own code. {@diff}The one-shot wrote nothing; after seven rounds of looking and fixing, the loop's render plays the full eight seconds — the tide-pool clip inside a real phone, the tide curve drawing, the headline on time. {@rounds}Seven looks, seven fixes.

## Line 7 — result (Frame 7)
    Here is the final hook {@result} — the Tidepool render from the loop, playing full frame, unobstructed, with its own look. {@hold}

## Line 8 — stack (Frame 8)
    The loop runs in Pi, and every decision is a call to Nemotron on Nebius Token Factory. {@media}TTV generated the footage, HyperFrames renders the HTML, Media Tooling voices this script. {@cost}Seven rounds, about thirty minutes of wall-clock time; inference is tracked separately.

## Line 9 — ask (Frame 9)
    This isn't a benchmark score, and we're not claiming one. {@ask}It's a case for testing models the way people use them: with tools and eyes on the output. {@claim}This video was made with this tool.
