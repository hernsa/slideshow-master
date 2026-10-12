# Annotation Stage — pure black, one product, leader-line callouts

> Derived from `Slide AirPods Pro 2.pptx`: 8 slides, all `#000000`, 138pt hero
> in `#F5F5F7`, one `#02FF40` accent, baked spotlight raster, a leader-line +
> dot group as annotation, a size-comparison row, and off-canvas parked artboards
> at `L=115%` waiting for morph.
> Grammar and rules → `../pptx-motion-language.md` §2, §3, §10.

**Use when:** showcase mode, product launches, feature reveals, single-subject
explains. Maximum one section per deck (the deep black stage reads as a
narrative break, not the deck's default).

**Anatomy (fixed per deck — 5 shapes):**

| # | Shape | Geometry | Notes |
|---|---|---|---|
| 1 | `glow` | baked raster or radial gradient | the spotlight |
| 2 | `product` | RGBA PNG | center / left / right — the anchor |
| 3 | `hero` | centred 138pt | `#F5F5F7`, one accent word |
| 4 | `leader` | line + 12px dot | annotation pointing at product |
| 5 | `size-row` | 4 labels 24pt | `#02FF40`, ~17% apart |

## Slide 4 — product + annotation, one accent

```html
<section class="stage">
  <!-- 1 — glow: if you have a baked RGBA, use it; else the radial-gradient below -->
  <img class="glow" src="assets/product-glow.png" alt="Sản phẩm dưới ánh sáng studio, quầng sáng mờ dần">
  <div class="glow-fallback" aria-hidden="true"></div>

  <!-- 2 — the product: the anchor that moves between slides -->
  <img class="product" data-id="product" src="assets/earbuds.png"
       alt="Tai nghe không dây, ảnh chụp cắt nền PNG">

  <!-- 3 — hero, 138pt, centred, one accent word -->
  <h2 class="hero">Sound<br>without <em>edges</em></h2>

  <!-- 4 — leader line + dot: annotation callout -->
  <div class="leader" data-id="leader">
    <span class="dot"></span>
    <span class="leader-text">Adaptive ANC · 2× quieter</span>
  </div>

  <!-- 5 — size row -->
  <ul class="size-row">
    <li>XS</li><li>S</li><li>M</li><li>L</li>
  </ul>
</section>
```

```css
.stage {
  position: relative; height: 100%; overflow: hidden;
  background: #000; color: #F5F5F7;
}

/* 1 — the baked spotlight. 740×1130 RGBA: left 40% pure #000, alpha falls 1.00 → 0.17 */
.glow { position: absolute; left: 50%; bottom: 0; height: 92%;
        transform: translateX(-50%); z-index: 0; }
.glow-fallback {                                   /* only if no baked raster */
  position: absolute; left: 50%; bottom: -10%; width: 60vw; height: 70vh;
  transform: translateX(-50%);
  background: radial-gradient(ellipse at 50% 70%, rgb(245 245 247 / .35), transparent 65%);
  mix-blend-mode: screen; z-index: 0;
}

/* 2 — the product. Alpha already baked; do NOT add drop-shadow. */
.product { position: absolute; left: 50%; bottom: 6%; height: 68%;
           transform: translateX(-50%); z-index: 2; }

/* 3 — 138pt hero */
.hero {
  position: absolute; inset: 18% 0 auto; z-index: 3; text-align: center;
  font-size: clamp(4rem, 10vw, 9rem);   /* the 138pt tier */
  line-height: 0.92; font-weight: 700; letter-spacing: 0;
}
.hero em { font-style: normal; color: #02FF40; }  /* ONE accent word */

/* 4 — leader line: 1px line + 12px dot, pointing inward */
.leader { position: absolute; left: 12%; top: 56%; z-index: 3; display: flex; align-items: center; gap: 10px; }
.leader .dot { width: 12px; height: 12px; border-radius: 50%; background: #02FF40; }
.leader::after { content: ""; width: clamp(60px, 10vw, 180px); height: 1px;
                 background: linear-gradient(90deg, #02FF40, transparent); }
.leader-text { font-size: 18px; color: #F5F5F7; }

/* 5 — size row: 4 labels, ~17% apart, accent green */
.size-row {
  position: absolute; left: 0; right: 0; bottom: 5%; z-index: 3;
  display: flex; justify-content: center; gap: 17%;
  list-style: none; margin: 0; padding: 0;
  font-size: 24px; font-weight: 600; color: #02FF40;
}
```

## The parked artboard (the morph trick)

Artboards waiting to appear are parked **off-canvas**, not `display:none` —
that's what makes them fly in:

```html
<!-- slide 3: parked -->
<div class="artboard" data-id="artboard-specs" style="left:115%">…</div>
<!-- slide 4: same name, on-canvas at 58% — morph flies it in -->
<div class="artboard" data-id="artboard-specs" style="left:58%">…</div>
```

```css
.artboard { position: absolute; top: 20%; width: 34%; transition: left 1.5s var(--ease-morph); }
```

Never "fix" the `left:115%`. See `../pptx-motion-language.md` §2.

## Slide spec

```
Slide 4 — Sound without edges        bg: pure-black
  Text runs:  hero "Sound without {accent}edges" {--t-hero clamp(4rem,10vw,9rem)} ; leader "Adaptive ANC · 2× quieter" {--t-label}
  Z-order:    glow → product → hero → leader → size-row
  Entrances:  hero .10s, product .22s, leader .34s      (3 max)
  Anchors:    product center → left 12% ; leader appears at 56%
  Transition: fade 0.4s  (one deck transition, §3)
  Done when:  bg is #000 not near-black; exactly one #02FF40 accent word; no cards, no borders.
```

## Do / Don't

- **Do** bake the spotlight into the raster. `filter: drop-shadow()` and
  `box-shadow` are absent from the reference deck entirely.
- **Do** use exactly one accent word per slide, in the contrasting face.
- **Do** keep product art as RGBA PNG with `alphaModFix` applied upstream.
- **Don't** add cards, borders, or radius to anything on this stage.
- **Don't** use `#0A0A0A` or `#111` — it's `#000000`. Depth comes from the
  raster, not the background color.
- **Don't** repeat this template. One showcase section per deck, max.