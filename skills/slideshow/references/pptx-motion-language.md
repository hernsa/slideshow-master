# PPTX Craft System — Anatomy of the Decks the User Likes

> Parsed shape-by-shape from the five reference decks in `pptx preference/`
> (`23.4`, `28.3`, `Chikiwaa`, `Slide AirPods Pro 2`, `Việt Nam ppt`) and the
> three rebuild prompts in `pptx prompt preference/`. This file is the layout +
> motion grammar those decks actually share. Mechanics stay in
> `animations.md`; one page per slide, always.

## 0. The one thing every one of these decks does that a generated deck doesn't

**They build a physical object on the canvas, then move the object between
slides.** Not "a card with a heading in it" — a photo collage, a parked
artboard, a rotating disc, a growing fill meter. The slide change reads as
motion because the *thing* persisted and changed position, not because a
transition effect fired.

`23.4`/`28.3` have an identical 19-shape tree on all four slides. `AirPods`
re-uses one product-photo + headline pairing five times, moving the photo
left → right → center while the headline stays pinned. `Chikiwaa` re-uses the
same freeform blobs for 20 slides.

**Rule — one object per deck that moves.** Before writing slide 1, name the
object: the disc, the parked artboard, the fill meter, the collage. Every
section of the deck re-positions that one object. A deck with no moving object
is a slide sorter.

## 1. Deck-level shape vocabulary

Real decks use a **small closed set of shapes re-used across every slide**,
not a fresh layout per slide. Count distinct shape geometries in a liked deck
and it is single digits.

| Deck | Shape vocabulary | Reuse |
|---|---|---|
| `23.4` / `28.3` | 1 full-bleed rect + 4 circles + 1 rotating group + 2 text boxes | 4/4 slides identical |
| `Chikiwaa` | ~6 freeform blobs (cloud, arch, circle, confetti scatter) + 1 card + 1 pill | 20/20 slides |
| `AirPods` | 1 spotlight raster + 1 product raster + 1 text block + 1 leader-line group + 1 size row | 8/8 slides |

**Rule — 3 to 8 distinct shapes per deck.** Write the list at style-lock time
and reuse it. A deck that invents a new layout on slide 7 has no visual
through-line and cannot morph.

## 2. The morph contract (exact names, intentional off-canvas)

Morph only works when two things are true: the shapes are **named identically**
across slides, and the geometry actually **differs** (so there is something to
tween).

- Shape names must match **exactly**, including `!!`-prefixed names — PowerPoint
  uses those to disambiguate duplicates and they are part of the identity.
- **Negative and off-canvas coordinates are intentional.** Reference decks park
  shapes at `L = 115%` or `T = 90%+`, outside the canvas, waiting on a later
  slide. Do not "fix" them. In the spec grammar (§9) this is `xfrm=1.15,...` —
  parked past the 13.333in canvas edge until its slide arrives.
- Content is **duplicated deliberately** across slides so morph can fly one
  copy out and swap another in.

```text
parked artboard: visible from slide 4 onward, waited off-canvas until slide 3
SHAPE "parked-artboard" xfrm=1.15,0.12,0.40,0.76   (slide 3 — parked past canvas)
SHAPE "parked-artboard" xfrm=0.58,0.12,0.40,0.76   (slide 4 — same name, on-canvas: morph flies it in)
```

**Rule — 2+ named continuities per section.** Name them at outline time in the
`Anchors:` line. Change position or size of **one** anchor per slide step,
never both at once. Anchors are headlines, shapes, photos, and numbers —
never body copy (`animations.md` §1 still binds).

## 3. One transition, identical on every slide

The rebuild prompts specify exactly one transition block repeated on every
slide: `spd="slow" p14:dur="1500" advClick="0"` plus `morph option="byObject"`,
with a plain `<p:fade/>` fallback. `Chikiwaa` ships morph byObject on 12 of 20
slides; `AirPods` ships it on the whole sequence.

**Rule:** lock ONE transition for the whole deck — a slow `fade`, a
`morph byObject`, or plain `none`. Apply it everywhere via `motion.py`.
Per-slide transition overrides are banned except a single `zoom` showcase.
The motion budget goes to anchors and entrances, never to transition roulette.

## 4. Stagger grammar (cadence yes, count no)

The 25.7s promo packs 349 effects on one slide. That is a video. Copy the
cadence, not the count: elements enter in reading order (kicker → headline →
body → visual), each 100–150ms apart, fast fade plus a slight rise, total
entrance budget ≤600ms per slide.

**Rule:** max 3 staggered entrances per slide (the 4th element is already
visible). Delay 100–150ms, duration 200–400ms, `add_fade_entrance` only.
Fragments and stagger share one budget (Gate 8) — never run both.

```python
stagger_entrances(slide, [("kicker", k), ("hero", t), ("sub", b)])  # motion.py
```

## 5. Photo as the load-bearing layer

The `23.4`/`28.3` slides are 5 photos each: one full-bleed background at
0.70 brightness with artistic blur, plus 4 circular tiles. There is no scrim
and no custom geometry — legibility comes from a bright/dark photo mix and
the fact that the tiles never sit under the text.

```python
# background: darkened + slightly blurred, never a hard scrim
plate(slide, "assets/hanoi-1890.jpg", 0.70)          # full-bleed, PIL blur baked
# circular tiles, right half only so the text column stays clean
circle_pic(slide, "tile-1", "assets/tile-1.jpg", cx=11.4, cy=2.6, d=1.9)
```

**Rules:**
- Every slide carries **≥1 photographic or hand-drawn image**. A deck whose
  `assets/CREDITS.md` says "no external raster images" is a failed deck.
- Ken Burns is **scale, not pan**: 1.15×–2.0× over-scale with `center` cover.
- Only the background goes full-bleed. Photos that sit under text need either a
  scrim (≥60% black from the text edge) or a clear side of the frame.
- Alt text conclusion-first per `media/images.md`.

## 6. Organic feel without masking photos

`Chikiwaa` masks nothing — every photo is a plain `rect`, rotated ±3–6°. The
organic quality comes entirely from **decorative freeforms layered behind and
around** the rectangles: cloud blobs, arch outlines, confetti scatter.

```python
# blob behind the photo, photo stays a clean rotated rect
deco_blob(slide, "cloud-a", cx=3.0, cy=3.4, w=6.2, h=4.4, color="#FFEFC8")
rect_pic(slide, "plate", "assets/kids.jpg", x=2.7, y=1.2, w=5.8, h=4.4, rot=-4)
```

**Rule — pick ONE organic device per deck:** blob-behind-photo (Chikiwaa),
circular tile cluster (23.4/28.3), or arch crop (editorial). Do not mix.

## 7. Value ramp, not a rotation cycle

The rebuild prompts derive every background from **one accent** by stepping
lightness and alpha — a ramp from white → pale → tinted → saturated. `Chikiwaa`
holds seven pastels from one hue family (never the same hue twice in a row)
with a single saturated green reserved as a section break.

**Rule:** derive the ramp from the locked accent; do not invent new hexes per
slide. Name 3–4 ramp stops at style-lock time. Longest identical-background run
≤2 (Gate 13). Never mix a pastel ramp with a neon accent in one deck — pick one
color story.

## 8. Type scale as a numbered menu

The rebuild prompts define a numbered type scale R1–R11, each a complete
reusable text style. Body copy never invents a size — it picks an `Rn`. The
scaled tiers the liked decks use: 138pt / 96pt hero, 88pt / 80pt section title,
48pt / 44pt heading, 36pt / 32pt subhead, 24pt / 20pt label, 16pt body.

**Rule:** define the scale as named tiers at style-lock time (hero /
section-title / heading / subhead / label / body — `title()`/`body()` sizes).
One hero per section, one display headline per slide at 54pt minimum — the
AirPods deck runs `138pt` for its hero. **Zero letter-spacing.** One accent
word in a contrasting face per slide, never a paragraph.

## 9. Per-slide spec grammar (line order = z-order)

The rebuild prompts specify each slide as an ordered list where **the order of
the lines is the z-order**, each line a shape with an exact frame, and text
attached to the shape:

```
SHAPE "hero" xfrm=0.04,0.06,0.30,0.24 def=D7 || ¶[l]{R1}Hà Nội · 1890
SHAPE "disc" xfrm=0.52,0.22,0.34,0.52 rot=-89,flipH=1 def=D12
ICON "leaf" icon="map-pin" xfrm=0.86,0.70,0.06,0.06
Done when: hero left at 4%, disc rotated -89°, z-order hero → disc → icon.
```

**Steal this format for `visual-plan.md` and the `research-notes.md` slide
sections** — every slide gets `Text runs:` (content + tier), `Z-order:` (bg →
shapes → text), `Entrances:` (≤3, with delays), `Anchors:` (which 2 elements
continue), `Done when:` (the acceptance line). The `Done when:` clause is what
makes the spec testable instead of aspirational.

## 10. Dark showcase — the spotlight is a raster

`AirPods` puts no gradient, no shadow, and no soft edge anywhere. The spotlight
is **baked into a 740×1130 RGBA PNG**: the left 40% is pure `#000000`, the
product peaks at full luminance with a soft grey halo, alpha falls 1.00 → 0.17.

```python
# pure black stage; the product PNG carries its own glow
solid_bg(slide, "#000000")
rect_pic(slide, "product", "assets/product-glow.png", x=4.4, y=0.6, w=4.5, h=6.3)
title(slide, "AirPods Pro 2", x=1.6, y=1.3, w=10.1, size=72,
      color="#F5F5F7", align="center", name="hero")
```

**Rules:** showcase mode = pure `#000` bg, `#F5F5F7` type, one accent
(`#02FF40`), no cards, no borders, ≤1 section per deck. If you cannot bake a
raster, `glow()` concentric ovals behind the photo are the acceptable
substitute — but never a card.

## 11. Anti-slop don'ts

1. No transition roulette — one deck transition (one `zoom`/`none` exception).
2. No 349-effect promos — stagger capped at 3, ≤600ms, shares the Gate 8 budget.
3. No raw rectangle photos *under text* — full-bleed-with-scrim or keep text off
   the photo; organic masking is optional and one device per deck (§6).
4. No morphing body copy — anchors are headlines, shapes, photos, numbers.
5. No pastel + neon in one deck — one color story, ramped from one accent (§7).
6. No morph without exact shape-name matches, and never "fix" the off-canvas
   parked shapes (§2).