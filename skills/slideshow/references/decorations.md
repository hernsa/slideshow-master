# Decorations — freeform blobs, rings, confetti (PPTX-native)

> Organic feel comes from decorative freeforms layered BEHIND clean photos —
> never from masking the photos. Pick ONE organic device per deck
> (blob-behind / tile-cluster / arch) and never mix.

## 1. The three devices

- **Blob-behind** (pastel/community decks): 2–3 large freeform blobs at
  10–20% tint of the accent, tucked behind plates and cards. Draw with
  `build_freeform` (cloud-ish 8–12 point closed paths) or reuse one cached
  blob shape copied across slides. Fill only, no line.
- **Tile-cluster** (dark photographic decks): the circular tiles ARE the
  decor — 3–4 circles right-half stacked. No extra blobs.
- **Arch** (editorial decks): one tall `roundRect`-with-big-`adj` or
  freeform arch outline (2.25pt accent line, no fill) standing behind a
  feature photo. One per section max.

## 2. Rings and confetti (accents, not devices)

- **Ring**: ellipse outline, 2.25–3pt, accent at 60–80% alpha. Tuck into a
  corner or behind a tile — never centered on text. Proven spots: top-right
  of mirrored slides, bottom-left of heritage slides. Check renders for
  collisions with kickers and glyphs (the ring-vs-`music` collision is real).
- **Confetti**: 6–12 tiny rects/dots (0.06–0.12in) scattered at low alpha
  near section breaks only. Never on body slides.
- **Glow**: radial-feel via 2–3 concentric translucent ellipses behind a
  black-stage subject, OR bake it into the PNG. Never `OuterGlow` effects —
  they rasterize unpredictably in renders.

## 3. Rules

- 1–2 decorative primitives per slide, all behind content in z-order
  (bg → plate → tiles → DECO → scrims → copy).
- Decor shapes get stable names (`deco-blob-a`, `deco-ring`) and near-stable
  positions — drifting one per section is a valid morph anchor.
- No shadows on decor (`ShadowFormat` off). Depth comes from layering, not
  drop shadows.
- Reduced-motion/narrative rule: decor never animates with entrances; it is
  either static or a morph anchor.
