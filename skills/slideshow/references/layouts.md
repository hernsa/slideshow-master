# Layouts — inches grid for 13.333 × 7.5in slides

> Canvas lock: 13.333 × 7.5in (1280 × 720 @96dpi). Content margins 0.625in;
> live zone x ∈ [0.625, 12.7], y ∈ [0.625, 6.875]. Copy-paste recipes live in
> `layout-templates/` — this file is the grid + the section patterns.

## The grid

- 12 columns of ~0.95in with 0.15in gutters inside the live zone. Eyeball it:
  left copy column x ∈ [0.65, 5.6], right visual column x ∈ [6.4, 12.7].
- Mirror free: copy-right/visual-left is the same layout flipped (S4 proved it).
- Kicker at y ≈ 1.9 (with 0.5in accent bar left of it), hero y ≈ 2.3,
  body y ≈ 3.6–4.6, gloss/pills y ≈ 5.4–6.2. Bottom 0.6in stays empty.
- Text ceilings: hero ≤ 2 lines @54–60pt, title ≤ 2 lines @40–44pt, body ≤
  4 lines @16pt, gloss 1 line @11pt. Overflow = cut words, never shrink type.

## Section patterns (pick one per section, reuse every slide in it)

1. **Copy-left + tile cluster.** Copy x ∈ [0.65, 5.2]; 2 circle tiles
   (2.0–2.6in ⌀) + diamond disc right half; plate full-bleed behind at the
   section brightness. Recipe: `photo-collage.md`.
2. **Mirrored.** Same shapes, copy x ∈ [7.8, 12.7], visuals left. The mirror
   IS the variety — geometry identical, positions flipped. Scrim follows the
   copy side (`scrim-right`).
3. **Duo boxes + feature photo.** Two accent boxes side by side (each ~2.6in
   wide) + one feature photo right; fork/flow pills under the copy. Recipe:
   phases of `photo-collage.md` + pills.
4. **Black stage.** Pure `#000000` bg, centred hero 54–96pt, one accent word,
   product raster with baked glow, leader-line callout, size row at y ≈ 6.3.
   Recipe: `annotation-stage.md`. Max one section per deck.
5. **Pastel community.** Pastel bg from the ramp, rotated rect plate
   (±3–6°, tilt baked in PIL), freeform blob + ring behind, white card for
   text, pill label. Recipe: `pastel-collage.md`.
6. **Display statement.** One line, 60–96pt, centred, plate or black behind.
   Recipe: `display-type.md`.

## Z-order (bottom → top, every slide)

`background rect → plate → tiles/discs → deco (blobs/rings) → scrims →
diagram boxes → pills → copy (kicker/hero/body) → logo`. Scrims sit ABOVE
plates but BELOW all text. The logo rides top, never inside the copy column
flow.

## Continuity rules (morph needs them)

- Same shape names + same template = same positions ± the ONE moving anchor.
- `scrim-left`/`scrim-right` keep their names across slides even when the
  side flips (the name is the identity; geometry may differ).
- Parked shapes wait at `left=14.5in` (off-canvas) with final names already set.
- Copy column never rotates, never moves inside a section — its immobility is
  what makes the flying anchor read as motion.
