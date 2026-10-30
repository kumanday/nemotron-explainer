# Local HyperFrames rendering

HyperFrames 0.8.142 needs an explicit head in the main `index.html` to retain
styles extracted from nested scenes during local rendering:

```html
<html data-composition-variables='[]'>
  <head>
    <meta charset="utf-8">
  </head>
  <body>
    <!-- Composition root, scene hosts, audio and root timeline. -->
  </body>
</html>
```

Keep each scene's styles, markup and scripts inside its `<template>`. The root
head is the destination for the extracted styles. A normal browser can infer a
head; this version's render assembler only appends those styles when its root
parser finds an authored head. Browser previews and local encodes can therefore
differ even when the source CSS is correct.

If an encoded scene has tiny text at the top left, check this structure before
changing font sizes, rewriting scene documents, or changing capture settings.
The root head fix works with templated scenes. Inspect frames decoded from an
actual MP4 at several times, including scene midpoints and cut boundaries.

The local reproduction is under `analysis/setup-audit/hf-explicit-head/`: a
1920×1080 composition with a nested scene declaring 120 px cyan centered text.
The encoded test retains that style with the explicit root head. The fixture
without it renders small, unstyled text. `scripts/check-delivery.py` checks for
the explicit root head; that structural check does not replace visual review.

Keep diagnostics under this project's `analysis/setup-audit/`. Resolve installed
tool locations with `scripts/tool-locations.py`; scope source searches to the
reported checkout or package. Whole-filesystem searches are unnecessary.
