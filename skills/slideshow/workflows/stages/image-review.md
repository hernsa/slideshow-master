# Stage: image-review — source, prep, credit, verify

> Runs inside `generate-pptx.md` phases 5–7. Output is `assets/` +
> `assets/CREDITS.md`. Authority: `references/media/images.md`.

## Procedure

1. Source per the ladder: real photo > licensed stock > generated.
   Never ship a grey box. Name files `<NN>_<name>.jpg`.
2. Prep in PIL before python-pptx ever sees the file: plates
   (darken + desaturate + blur, cached by brightness), square pre-crops
   for circles/diamonds, rotation baked into pixels (never
   `shape.rotation`), logos alpha-keyed to transparent PNG.
3. Credit every source file in `assets/CREDITS.md`: filename + author +
   license. "No external raster images" is a failure line, never a
   credit line.
4. Run `python scripts/verify-images.py <deck-dir>`: every `build.py`
   ref resolves, every file is credited, budgets hold (photos ≤400KB,
   backgrounds ≤200KB, width ≤1920px).

## Handoff

`Images done: N files, N credited, 0 missing — build may proceed.`
