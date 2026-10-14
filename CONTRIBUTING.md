# Contributing

> Add palettes, layout recipes, and modes with small, reviewable files.
> Every addition must pass the ship gates in
> `skills/slideshow/references/verify-checklist.md`.

## Ground rules

- One contribution per pull request. Small diffs review fast.
- Python-first: every recipe is a `build.py` helper call, never prose.
- No filler lines, no missing rasters, no hotlinked art.
- Read every render by eye before asking for review.

## How to add a palette

File: edit `skills/slideshow/references/visual-styles/`.

1. Append one palette section: name, vibe, BG/INK/ACCENT/ACCENT2/MUTED/
   CARD hexes, font pair plus mono.
2. Contrast: body text readable on renders at 960px wide; record the
   plate/scrim treatment that achieves it.
3. Verify: build a 3-slide sample (title + collage + close), export
   renders, attach them to the PR.

## How to add a layout recipe

Path: `skills/slideshow/references/layout-templates/<name>.md`.

1. File naming: lowercase hyphenated, for example `agenda.md`.
   Register the row in `layout-templates/_index.md` table and bump
   `templates_index.json` (count + version).
2. Required sections in order: title, when-to-use, python-pptx recipe
   calling ONLY the scaffold Helper API contract (`_index.md`), slide
   spec block (`Template:` / `Text runs:` / `Z-order:` / `Images:` /
   `Entrances:` / `Anchors:` / `Done when:`), one anti-slop rule.
3. Recipes stay copy-paste ready with concrete content, never empty
   boxes. Rotation always baked in PIL, inches units, `name=` set.
4. Verify: build a 2-slide sample reusing the recipe, confirm Morph
   carries the anchors across both renders.

## How to add a mode

Modes are narrative arcs (`references/modes/`), not settings.

1. Name: lowercase, one arc per file, under 60 lines: slide count,
   section flow, section→template mapping, PPTX notes (moving object,
   raster needs, entrance exceptions).
2. Verify: the arc's slide count matches a mode in the SKILL.md route
   table, or update the table in the same PR.

## Verify steps for every PR

```powershell
python scripts/check-repo.py
python -m py_compile skills/slideshow/scripts/scaffold.py skills/slideshow/scripts/verify-pptx.py skills/slideshow/scripts/render.py skills/slideshow/scripts/verify-images.py
```

Gates: rasters on every slide, zero filler hits, notes 1:1, motion
budget (≤3 fade/slide), morph-name discipline, renders read by eye.

## PR shape

Title: `Add <name> <kind>: one-line effect`.
Body: palette used, raster count, continuity anchors, render proof
(PNGs attached), decision log when routing changed.
Keep the diff under `300` lines when possible; split style plus docs
into two PRs when it grows past that.
