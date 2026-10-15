# Images — sourcing, PIL prep, and placement (PPTX-native)

> Every slide carries ≥1 photographic or hand-drawn raster. SVG diagrams ride
> ON TOP of photographs, never instead of them. A `CREDITS.md` line reading
> "no external raster images" is a failure line, never a credit line.

## 1. Sourcing ladder (top rung first)

1. **Real photography of the actual subject** — shoot it, or pull licensed
   archive/CC photos of the real place/thing/person. The iSpeak deck used
   Wikimedia Commons Halong Bay photos, each credited with author + license.
2. **Stock with a paper trail** — Unsplash/Pexels, still logged per file.
3. **Generated/AI imagery** — only when 1–2 are impossible; log the tool.
4. **Placeholder grey boxes** — never ship. A missing file STOPS the build
   (workflow phase 7), it never becomes a grey rect.

**Log every file** in `assets/CREDITS.md`: filename, source URL, author,
license. No hotlinking — everything vendored under `assets/`.

## 2. Naming

`<NN>_<name>.jpg` — slide number + stem: `01_bay.jpg`, `04_tile-boat.jpg`.
Names must match the visual-plan `Images:` lines exactly. Same stem across
slides = same photo reused (morph continuity loves this).

## 3. PIL prep — do this BEFORE python-pptx (never fix in PowerPoint)

All prep happens in phase 7 with Pillow. Proven patterns from the iSpeak build:

- **Plates** (full-bleed backgrounds): darken to a target brightness
  (`.70` moody / `.85` light / `.45–.50` under white text on daylight photos)
  + slight Gaussian blur. Cache by `(src, brightness)` — the same plate at
  two brightness levels is two files, e.g. `02_karst.jpg` + `07_karst-dark.jpg`.
- **Square pre-crops**: `add_picture` stretches to the frame, so center-crop
  tiles/discs to squares in PIL first. Circles and diamonds MUST be square.
- **Baked rotation**: never `shape.rotation` on a custom-geometry picture —
  PowerPoint renders a white wedge. `img.rotate(angle, resample=BICUBIC,
  expand=True)` in PIL, shape rotation stays 0.
- **Keyed logos**: white→transparent via PIL alpha keying (`logo-ngoquyen.png`
  pattern), then place top-right at ~1.1in wide.

## 4. Placement grammar (python-pptx)

- **Plate**: `add_picture` deliberately OVERSIZED for full bleed — placed at
  `-0.8,-0.45in` and sized `13.333×7.5in × 1.12` so no edge gap appears,
  no border. Name it `plate`.
- **Circle tile**: square pre-crop → `add_picture`, then swap geometry
  rect→ellipse via the `a:prstGeom prst="ellipse"` edit. Right half only,
  stacked with 19%-style offsets. Name `tile-N`.
- **Diamond disc**: square pre-crop (rotation baked) → `add_picture`, swap
  geometry to `diamond`. The rotating anchor — same name every slide.
- **Feature rect**: plain rect photo, rotate the CONTENT in PIL ±3–6°,
  shape stays axis-aligned. Blob/ring decor goes behind it.
- **Scrim**: when text sits on a plate, a black rect from the text edge at
  60–65% alpha (`a:alpha val="62000"` = 62%). Both sides reuse the SAME
  name `scrim-left` (the scaffold's `scrim_right` keeps it) so a mirrored
  slide morphs the identical rect — morph continuity over side-specific
  naming.
- **Black-stage subjects**: RGBA PNGs with baked glow/alpha, placed on a
  pure `#000` bg rect. Never `drop-shadow` — bake it.

## 5. Budgets

- Raster floor: ≥1 raster per slide AND deck total (unique images) ≥ slides,
  rasters on ≥60% of slides.
- Narrative/photo sections: 3–6 rasters per slide (plate + tiles + disc).
- File weight: photos ≤400KB, backgrounds ≤200KB, ≤1920px on the long edge.
  The iSpeak final was 2.5MB for 8 slides / 15 rasters — that is the shape.
- Alt text: `set_alt(picture, "…")`, conclusion-first, ≤140 chars.
