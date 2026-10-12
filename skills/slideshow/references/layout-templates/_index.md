# Layout templates — index

> Tokens are canonical in [tokens.md](../tokens.md) — 8pt spacing, 16px radius, dark-first. One page per slide.

## All 8 types

| Type | Use when | File |
|---|---|---|
| framing | open, divide, or close the talk (hero, numbered divider, CTA + QR) | [framing.md](./framing.md) |
| photo-hero | true full-bleed photo beat, inset 0, scrim 60%+, 25 words max | [photo-hero.md](./photo-hero.md) |
| photo-collage | photographic narrative section — darkened full-bleed plate + 4 circular tiles + rotating disc anchor | [photo-collage.md](./photo-collage.md) |
| pastel-collage | warm explainer/community section — freeform blobs behind rotated photo plates, text on white cards | [pastel-collage.md](./pastel-collage.md) |
| display-type | giant one-line statement at clamp(4rem,10vw,9rem) | [display-type.md](./display-type.md) |
| annotation-stage | showcase mode — pure `#000`, baked spotlight raster, leader-line callouts, parked off-canvas artboards | [annotation-stage.md](./annotation-stage.md) |
| showcase | dark near-black product moment, photo is decoration | [showcase.md](./showcase.md) |
| motion | static-position anchors across slides, no fragments | [motion.md](./motion.md) |

Diagrams moved: architecture, flow, timeline live in `references/data-graphics/diagrams.md` §§1-3 — single ownership, picker points there.

Each of `photo-collage`, `pastel-collage`, and `annotation-stage` is transcribed from a
reference deck and ships its own slide spec block (`Text runs:` / `Z-order:` /
`Entrances:` / `Anchors:` / `Images:` / `Done when:`). Copy that block into
`visual-plan.md` verbatim.

## Picker rule

1. Ask: is the point sequential or parallel?
2. Sequential (steps, history, process) goes to `references/data-graphics/diagrams.md` §2 (flow) or §3 (timeline).
3. Parallel (options, metrics, features) goes to `references/layouts.md` §2C (header + 2-col) or §4 (stat cards).
4. Proof (voice, code) goes to `references/layouts.md` §5 (quote) or §6 (code + preview); architecture goes to diagrams §1.
5. Ask next: is this section about **seeing something** or **reading something**?
   - Seeing, photographic, mood/history/archive → `photo-collage.md` (dark photographic) or `pastel-collage.md` (warm community).
   - Seeing, one subject on a stage → `annotation-stage.md` (showcase mode only).
   - Reading → the diagram/parallel routes in steps 2-4.
6. Framing (open, divide, close) goes to `framing.md`, `photo-hero.md`, `display-type.md`, or `showcase.md`.
7. Motion feel without export breakage goes to `motion.md` (static anchors, no v-click/fragment).
8. Pick **one organic device per deck** — circular tile cluster OR blob-behind-plate OR arch crop. Never mix.
9. If two slides in a row use the same template, merge them or change the visual on the second one.

## How to use a template file

- Each file holds a copy-paste sketch plus one don't; shared rules live in the footer below.
- Copy the HTML into your slide, swap Acme content for real content, keep gaps, radii, type sizes.
- Every template collapses to one column under `800px`. Test at `390px` before shipping.

## Shared footer (applies to every template above)
1. One page per slide — one template, one point; never paste two templates on one slide.
2. Spacing 8pt (`8/16/24/32/48/64`), radius 16px, dark-first; type from `../tokens.md`.
3. reveal.js: plain HTML in `<section>`; Slidev: matching `layout:` or raw HTML; Marp: raw HTML, screenshot fallback for iframes.
4. Collapse grids to 1 col under 800px (2-col under 520px to 1 col); code `13.5px` scroll-x on small screens.
5. Alt text conclusion-first; deltas pair arrow plus sign with color; captions 14px muted with source.
6. DOM order matches narration; decorative arrows `aria-hidden`; page `title` matches `h1`.
7. Contrast 4.5:1 minimum; `prefers-reduced-motion` cuts fragments and animation to final state.
8. QR never stands alone (short URL beside it); code is real text, never an image.
9. One accent per slide; caps: dividers 3 per deck, heroes 2 per deck, showcase 1 section per deck.
10. Every slide carries at least one photographic or hand-drawn image; a deck with zero rasters fails Gate 3.
11. Test at 390px plus projector grayscale before shipping; keep gaps, radii, alt text as written.
