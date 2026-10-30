```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Tidepool — Product Launch Hook</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;800&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body { width: 100%; height: 100%; margin: 0; background: #06202b; overflow: hidden; }
  #root {
    position: relative;
    width: 1920px;
    height: 1080px;
    margin: 0 auto;
    background: #06202b;
    overflow: hidden;
  }
  .clip { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }
  .clip video {
    position: absolute; top: 0; left: 0;
    width: 100%; height: 100%;
    object-fit: cover;
    display: block;
    background: #06202b;
  }
  #sweep {
    position: absolute;
    left: -700px; top: 440px;
    width: 700px; height: 3px;
    background: linear-gradient(to right, transparent, #5fd4c4, rgba(255,255,255,0.8), #5fd4c4, transparent);
    filter: drop-shadow(0 0 12px rgba(95,212,196,0.5));
  }
  #phone {
    position: absolute;
    left: 140px; top: 1080px;
    width: 300px; height: 648px;
    background: #0c242f;
    border: 8px solid #06202b;
    border-radius: 60px;
    box-shadow: 0 30px 80px rgba(0,0,0,0.7);
  }
  #screen {
    position: absolute; top: 28px; left: 28px; right: 28px; bottom: 28px;
    border-radius: 44px; overflow: hidden; background: #06202b;
  }
  #phone .speaker {
    position: absolute; top: 22px; left: 50%; transform: translateX(-50%);
    width: 130px; height: 22px; border-radius: 11px; background: #06202b;
  }
  #phone .cam {
    position: absolute; top: 58px; left: 50%; transform: translateX(-50%);
    width: 18px; height: 18px; border-radius: 50%; background: #06202b;
  }
  #phone .bar {
    position: absolute; left: 50%; transform: translateX(-50%); bottom: 16px;
    width: 100px; height: 9px; border-radius: 6px; background: rgba(255,255,255,0.15);
  }
  #curveLayer {
    position: absolute; top: 0; left: 0; width: 100%; height: 100%;
  }
  #tidePathGhost { fill: none; stroke: #5fd4c4; stroke-width: 7; stroke-linecap: round; opacity: 0.18; }
  #tidePath { fill: none; stroke: #5fd4c4; stroke-width: 7; stroke-linecap: round; }
  #tideDot {
    position: absolute;
    left: 570px; top: 706px;
    width: 22px; height: 22px;
    border-radius: 50%; background: #f2c48d;
    box-shadow: 0 0 16px rgba(242,196,141,0.7);
  }
  #lowLabel {
    position: absolute; left: 1220px; top: 935px; width: 640px;
    font-family: "Montserrat", sans-serif; font-size: 34px; font-weight: 600;
    color: #f2c48d; text-align: right; opacity: 0;
  }
  #headline {
    position: absolute; left: 560px; top: 240px; width: 1300px;
    font-family: "Montserrat", sans-serif; font-size: 110px; font-weight: 800;
    color: #ffffff; line-height: 1.22; opacity: 0;
  }
  #wordmark {
    position: absolute; left: 560px; top: 575px;
    font-family: "Montserrat", sans-serif; font-size: 66px; font-weight: 800;
    letter-spacing: -3px; color: #5fd4c4; opacity: 0;
  }
  #subline {
    position: absolute; left: 560px; top: 662px;
    font-family: "Montserrat", sans-serif; font-size: 30px; font-weight: 400;
    color: #9fc7c0; opacity: 0;
  }
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="8" data-width="1920" data-height="1080">
  <div class="clip" data-start="0" data-duration="2.6" data-track-index="0">
    <video src="assets/tidepool.mp4" data-start="0" data-duration="2.6" data-track-index="0" muted playsinline></video>
    <div id="sweep"></div>
  </div>
  <div class="clip" data-start="2.6" data-duration="5.4" data-track-index="1">
    <div id="phone">
      <div class="speaker"></div>
      <div class="cam"></div>
      <div id="screen">
        <video src="assets/tidepool.mp4" data-start="2.6" data-duration="2.6" data-track-index="1" muted playsinline></video>
      </div>
      <div class="bar"></div>
    </div>
    <svg id="curveLayer">
      <path id="tidePathGhost" d="M 580,720 C 800,300 1400,300 1860,900"></path>
      <path id="tidePath" d="M 580,720 C 800,300 1400,300 1860,900"></path>
    </svg>
    <div id="tideDot"></div>
    <div id="lowLabel">Low tide 4:12 PM</div>
    <div id="headline">Know the <span style="color:#5fd4c4">tide</span> before you go.</div>
    <div id="wordmark">Tidepool</div>
    <div id="subline">Free on iOS and Android</div>
  </div>
</div>
<script>
  (function () {
    const tl = gsap.timeline({ paused: true });
    const path = document.getElementById("tidePath");
    const len = path.getTotalLength();
    path.style.strokeDasharray = len;
    path.style.strokeDashoffset = len;
    const dot = document.getElementById("tideDot");
    const surf = { p: 0 };

    function updateDot() {
      const pt = path.getPointAtLength(surf.p * len);
      dot.style.left = (pt.x - 11) + "px";
      dot.style.top = (pt.y - 11) + "px";
    }

    tl.fromTo("#sweep", { x: 0 }, { x: 2620, duration: 2.6, ease: "power2.inOut" }, 0);
    tl.fromTo("#phone", { y: 0 }, { y: -900, duration: 1.7, ease: "power4.out" }, 2.6);
    tl.fromTo("#phone", { scale: 0.88 }, { scale: 1, duration: 1.7, ease: "power4.out" }, 2.6);
    tl.fromTo("#tidePath", { strokeDashoffset: len }, { strokeDashoffset: 0, duration: 2.6, ease: "power1.inOut" }, 2.6);
    tl.to(surf, { p: 1, duration: 2.6, ease: "power1.inOut", onUpdate: updateDot }, 2.6);
    tl.fromTo("#tideDot", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 2.6);
    tl.to("#lowLabel", { opacity: 1, duration: 0.5 }, 4.9);
    tl.fromTo("#headline", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.75, ease: "power3.out" }, 5.2);
    tl.fromTo("#wordmark", { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, 6.1);
    tl.fromTo("#subline", { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }, 6.75);
    tl.to({}, { duration: 0.75 }, 7.25);

    window.__timelines = window.__timelines || {};
    window.__timelines["main"] = tl;
  })();
</script>
</body>
</html>
```