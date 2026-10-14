# Layout templates — index

> Tokens are canonical in [tokens.md](../tokens.md). Every template below is a **python-pptx recipe**: copy the code block into the deck's `build.py`, swap the demo content for real content, keep the geometries. One pattern per slide. Canvas is always 13.333×7.5in blank.

## All 8 types

| Type | Use when | File |
|---|---|---|
| framing | open, divide, or close the talk (hero, numbered divider, CTA + QR) | [framing.md](./framing.md) |
| photo-hero | true full-bleed photo beat, scrim 60%+, 25 words max | [photo-hero.md](./photo-hero.md) |
| photo-collage | photographic narrative — darkened plate + circular tiles + rotating disc | [photo-collage.md](./photo-collage.md) |
| pastel-collage | warm community — blobs behind rotated plates, copy on white card | [pastel-collage.md](./pastel-collage.md) |
| display-type | giant one-line statement at 72–96pt | [display-type.md](./display-type.md) |
| annotation-stage | showcase mode — pure `#000`, baked glow raster, leader callouts | [annotation-stage.md](./annotation-stage.md) |
| showcase | dark near-black product moment, photo is decoration | [showcase.md](./showcase.md) |
| motion | anchor-continuation contract across slides (names, slots, parked shapes) | [motion.md](./motion.md) |

Diagrams moved: architecture, flow, timeline live in `references/data-graphics/diagrams.md` §§1-3 — single ownership, picker points there.

Each recipe file ships its own slide-spec block (`Text runs:` / `Z-order:` / `Images:` / `Entrances:` / `Anchors:` / `Done when:`). Copy that block into `visual-plan.md` verbatim.

## Helper API contract

Every recipe calls helpers with these exact signatures. The scaffold's `build.py` provides them — same names, same parameter order, every deck:

- `new_slide()` → blank 13.333×7.5in slide
- `solid_bg(slide, hex)` · `plate(slide, src, brightness)` · `scrim_left(slide, alpha)` / `scrim_right(slide, alpha)`
- `circle_pic(slide, name, src, cx, cy, d)` · `diamond_pic(slide, name, src, cx, cy, d, rot)` · `rect_pic(slide, name_or_None, src, x, y, w, h, rot=0)`
- `kicker(slide, text, x, y, color, name=None)` · `title(slide, text, x, y, w, size, color=INK, accent=None, accent_color=None, align="left", name=None, mono=False)` · `body(...)` same shape, default 16pt · `gloss(...)` same shape, default 11pt
- `pill(slide, text, x, y, w, fill, color, outline=None)` · `round_rect(slide, name, x, y, w, h, fill, line=None)`
- `deco_blob(slide, name, cx, cy, w, h, color)` · `deco_ring(slide, name, cx, cy, d, color)` · `glow(slide, cx, cy, d, color)`
- `leader(slide, name, x1, y1, x2, y2, label)` · `set_notes(slide, text)`

Rotation is always BAKED in PIL inside `diamond_pic`/`rect_pic` — never `shape.rotation` on a custom-geometry picture (white-wedge artifact). All coordinates in inches. `name=` sets `shape.name` = the morph identity.

## Picker rule

1. Ask: is this section about **seeing something** or **reading something**?
   - Seeing, photographic, mood/history/archive → `photo-collage.md` (dark) or `pastel-collage.md` (warm).
   - Seeing, one subject on a stage → `annotation-stage.md` (showcase mode only).
   - Reading → the diagram/parallel routes below.
2. Sequential (steps, history, process) → `references/data-graphics/diagrams.md` flow or timeline.
3. Parallel (options, metrics, features) → `references/layouts.md` duo-boxes or stat rows.
4. Proof (voice, code) → quote or mono block per `references/layouts.md`; architecture → diagrams §1.
5. Framing (open, divide, close) → `framing.md`, `photo-hero.md`, `display-type.md`, or `showcase.md`.
6. Continuity across slides without entrances → `motion.md` (anchors, one moving element).
7. Pick **one organic device per deck** — circular tile cluster OR blob-behind-plate OR arch crop. Never mix.
8. If two slides in a row use the same template, merge them or change the visual on the second one.

## How to use a template file

- Copy the recipe into `build.py`, swap demo content for real content, keep gaps, sizes, rotations.
- Copy the file's slide-spec block into `visual-plan.md` verbatim, filled with the real slide's values.
- Test at projector contrast (dark rooms forgive; bright rooms kill pastels) before shipping.

## Shared footer (applies to every template above)

1. One pattern per slide; never paste two templates on one slide.
2. Canvas 13.333×7.5in, margins 0.625in, dark-first; type from `../tokens.md`.
3. Photos are real rasters under `assets/`, PIL-prepped (darken/blur/crop/rotation baked); never hotlinked, never grey-boxed.
4. Alt text conclusion-first, ≤140 chars; decorative shapes unnamed or plainly named.
5. Notes on every content slide via `set_notes`; match the spoken line, not the slide text.
6. Contrast 4.5:1 minimum; scrims ≥60% under white type.
7. QR is a real raster, never drawn; code is mono text, never an image.
8. One accent per slide; caps: dividers 3 per deck, heroes 2 per deck, showcase 1 section per deck.
9. Every slide carries at least one photographic raster (display-type excepted — record why); a deck with zero rasters fails Gate 3.
10. Morph names match exactly across slides; parked shapes wait at `x=14.5in`, never "fixed" on-canvas.
11. Read every COM render before shipping; fix in `build.py`, rebuild, re-render, re-read.
