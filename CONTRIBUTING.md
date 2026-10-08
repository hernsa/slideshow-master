# Contributing

> Add visual styles, palettes, layout templates, and modes with small,
> reviewable files. Every addition must pass the ship gates in
> `skills/slideshow/references/verify-checklist.md`.

## Ground rules

- One contribution per pull request. Small diffs review fast.
- Markdown-first: even reveal.js additions start as Markdown sketches.
- No filler lines, no empty image sources, no hotlinked art.
- Test at `390px`, keyboard-only, and `prefers-reduced-motion` before asking.

## How to add a visual style

Path: new starter under `skills/slideshow/examples/<name>-demo/`.

1. Name: lowercase plus `-demo`, for example `editorial-demo`.
2. Required sections: tokens, title slide, bento, split, stat row, quote,
   code plus preview, divider, closing, image treatment.
3. Required files: `slides.md` or `index.html`, `theme.css`, `assets/`,
   `assets/CREDITS.md`, `README.md` with serve plus export commands.
4. Line limits: `theme.css` under `400` lines, each slide under `60` lines.
5. Verify: `python3 ../../scripts/verify-images.py` from the demo dir,
   contrast trio recorded, `export-deck.sh` smoke test per engine.

## How to add a palette

File: edit `skills/slideshow/references/colors.md`.

1. Append one palette section: name, vibe, dark plus light tokens,
   font pair plus mono, code theme pair, one allowed accent use.
2. Tokens required: `--bg`, `--fg`, `--surface`, `--border`,
   `--primary`, `--muted`, code `light` plus `dark` theme names.
3. Contrast: body `>=4.5:1`, projector-safe note when `>=7:1`.
4. Fonts: max `2` text families plus `1` mono, weights `<=4` total.
5. Verify: paste the palette on title plus stats plus code slides,
   screenshot both modes, record the three contrast numbers in the PR.

## How to add a layout template

Path: `skills/slideshow/references/layout-templates/<name>.md`.

1. File naming: lowercase hyphenated, for example `comparison.md`.
   Register the row in `layout-templates/_index.md` table.
2. Required sections in order: title, when-to-use, HTML sketch,
   spacing tokens, per-engine notes for reveal.js plus Slidev plus Marp,
   responsive snippet, accessibility note, one anti-slop rule.
3. Line limits: `50` to `100` lines per file. Sketches stay copy-paste
   ready with Acme example content, never empty boxes.
4. Tokens: reuse `layouts.md` scale `8/16/24/32/48/64`, `16px` radius,
   `clamp()` type, `.eyebrow`, `.lead`, `img.fit` treatment.
5. Verify: paste into all three starters, check `800px` plus `390px`
   collapse, confirm `alt` text and caption, run the filler greps.

## How to add a mode

Modes are deck-wide settings like `reduced-motion`, `print`, or `kiosk`.

1. Name: lowercase, documented in `references/animations.md` or a new
   `references/<mode>.md` under `60` lines with purpose plus snippet.
2. Required: CSS or config snippet, per-engine wiring for all three
   engines, fallback when the mode is unsupported, test steps.
3. Example: kiosk mode needs autoplay timing, loop flag, keyboard lock
   note, and Marp static fallback since Marp ignores autoplay.
4. Verify: test in Chromium plus Firefox, record console output,
   attach before and after screenshots in the PR.

## Verify steps for every PR

```bash
python3 skills/slideshow/scripts/verify-images.py
grep -rni "test test\|untitled" --include="*.md" --include="*.html" .
grep -rni "gradient" --include="*.css" --include="*.html" . | wc -l
bash skills/slideshow/scripts/export-deck.sh reveal
```

Gates: images local plus `<=400KB` plus credited, zero filler hits,
gradients `<=1`, fonts `2` plus mono, code `<=12` lines, notes `1:1`,
contrast numbers pasted, mobile plus keyboard plus motion checked.

## PR shape

Title: `Add <name> <kind>: one-line effect`.
Body: engine coverage, palette used, contrast trio, export proof,
screenshots at desktop plus `390px`, decision log when routing changed.
Keep the diff under `300` lines when possible; split style plus docs
into two PRs when it grows past that.
