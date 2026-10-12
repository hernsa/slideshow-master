# Photo Collage — circular tile cluster over a darkened full-bleed plate

> Derived from `23.4.pptx` / `28.3.pptx`: identical 4-slide shape tree,
> 5 photos per slide, one rotating group, `-30%` background brightness,
> circular tiles that never sit under the text column.
> Grammar and rules → `../pptx-motion-language.md` §2, §5, §7.

**Use when:** narrative / history / case-study / "look at the real thing"
decks. Not for data-dense slides — this device buys mood, not density.

**Anatomy (fixed per deck — 5 shapes):**

| # | Shape | Geometry | Notes |
|---|---|---|---|
| 1 | `bg-plate` | full canvas | darkened + blurred photo |
| 2–5 | `tile-1..4` | `border-radius:50%` | right half, stacked |
| 6 | `disc` | rotating group | the anchor that morphs |
| 7 | `hero` / `sub` | text column, left | **never rotates** |

## Slide 3 — circular collage over plate

```html
<section class="collage" data-bg="assets/hanoi-1890.jpg">
  <div class="plate" role="img" aria-label="Hà Nội street photography, 1890s archive scan"></div>

  <div class="tiles">
    <span class="tile" data-id="tile-1" style="--i:0"></span>
    <span class="tile" data-id="tile-2" style="--i:1"></span>
    <span class="tile" data-id="tile-3" style="--i:2"></span>
    <span class="tile" data-id="tile-4" style="--i:3"></span>
  </div>

  <div class="disc" data-id="disc" style="--rot:-89deg"><img src="assets/disc-jpeg.jpg" alt="Collaged photograph disc, rotated between slides"></div>

  <div class="copy">
    <h2 class="t-title enter-1">Hà Nội · 1890</h2>
    <p class="t-body enter-2">Cửa Thành cũ, ba sứ đô thành, buổi sớm mùa thu.</p>
  </div>
</section>
```

```css
.collage { position: relative; height: 100%; overflow: hidden; isolation: isolate; }

/* 1 — plate: darkened + slightly blurred. Scale over-shoot 1.44x, no pan. */
.plate {
  position: absolute; inset: -6%;
  background: var(--slide-img) center/cover no-repeat;
  filter: brightness(.70) saturate(.85) blur(2px);
  transform: scale(1.44);
  z-index: 0;
}

/* 2–5 — circular tile cluster, right half only */
.tiles { position: absolute; right: 5%; top: 14%; width: 34vw; aspect-ratio: 1; z-index: 2; }
.tile {
  position: absolute; inset: calc(var(--i) * 19%);      /* 4 rings, offset 19% */
  border-radius: 50%;
  background: var(--tile-img) center/cover no-repeat;
  box-shadow: 0 0 0 1px rgb(255 255 255 / .12);
}
.tile[data-id="tile-1"] { --tile-img: url(assets/tile-1.jpg); }
.tile[data-id="tile-2"] { --tile-img: url(assets/tile-2.jpg); }
.tile[data-id="tile-3"] { --tile-img: url(assets/tile-3.jpg); }
.tile[data-id="tile-4"] { --tile-img: url(assets/tile-4.jpg); }

/* 6 — the rotating disc: the anchor. Rotate by -89deg per slide step. */
.disc {
  position: absolute; right: 8%; top: 24%; width: 28vw; aspect-ratio: 1;
  transform: rotate(var(--rot, 0deg));
  transition: transform 1.5s var(--ease-morph);
  z-index: 3; clip-path: polygon(50% 0, 100% 50%, 50% 100%, 0 50%); /* diamond */
}
.disc img { width: 100%; height: 100%; object-fit: cover; border-radius: 50%; }

/* 7 — text column: OUTSIDE the rotating group, never moves */
.copy { position: absolute; left: 4.75%; top: 32%; width: 34%; z-index: 4; }
```

## Slide spec (paste into `visual-plan.md`)

```
Slide 3 — Hà Nội · 1890        bg: dark-photo
  Text runs:  hero "Hà Nội · 1890" {--t-title} ; sub 1 line {--t-body}
  Z-order:    plate → tiles → disc → copy        (4 lines, top to bottom)
  Entrances:  hero .10s, sub .22s                 (2 only — tiles need none)
  Anchors:    disc rotates 0° → -89° ; hero copy pinned identical
  Images:     assets/hanoi-1890.jpg (bg) · tile-1..4.jpg · disc-jpeg.jpg  → 6 rasters
  Done when:  6 images present, hero glyph-identical to slide 2, disc rotated -89°.
```

## Do / Don't

- **Do** keep the text column outside every rotating/translating group — that
  immobility is what makes the disc read as motion.
- **Do** reuse the exact same 7 shapes on every slide of the section. The
  morph target needs identical names.
- **Do** alternate plate brightness (`brightness(.70)` / `.85`) per ramp stop.
- **Don't** put body text over the plate — no scrim exists in this device.
- **Don't** rotate the tiles. Only the disc moves.
- **Don't** add a card, border, or shadow behind the copy column.

## Per-slide ramp for the section

| Slide | Plate brightness | `--rot` | Tile inset offset |
|---|---|---|---|
| 1 | `.70` | `0deg` | `0%` |
| 2 | `.85` | `-89deg` | `19%` |
| 3 | `.70` | `-178deg` | `38%` |
| 4 | `.85` | `-267deg` | `57%` |

One value moves per step (plate OR rotation, not both) — `../pptx-motion-language.md` §2.