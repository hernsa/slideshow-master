# Export Verify — Per-Engine Export Procedure

> The export is the artifact that outlives the talk. "Works on my laptop" means
> nothing until the PDF paginates, the PPTX opens elsewhere, and the HTML runs
> with zero console errors.

## 1. When this stage runs

- Full path: `generate-deck.md` step 11, only after `stages/visual-review.md` signs off.
- Fast path: sprint 0:12–0:15 — HTML + PDF opened once, pagination confirmed, then ship.
- Never export to rescue a red gate; export verifies green work.

## 2. Pre-export freeze

Confirm the outline version, the visual-review handoff, and a clean placeholder
scan are all in the delivery note. Export from the final commit — screenshots of
auth-gated demos already in `assets/`, no `localhost` demo URLs left live.

## 3. Per-engine export commands

Run from the skill root. `scripts/export-deck.sh <reveal|slidev|marp> <deck-path> [out-dir]`
writes into `dist/` by default.

reveal.js — serve first, decktape needs a URL:

```bash
npx serve . -l 8000 &
scripts/export-deck.sh reveal "http://localhost:8000/?print-pdf" dist
# raw fallback with a longer load pause for heavy decks:
npx decktape reveal --load-pause 2000 "http://localhost:8000/?print-pdf" deck.pdf
```

Fragments print as final state by default. PPTX has no native path — export PDF,
then convert, or rebuild in Marp when PPTX is the deliverable.

Slidev — PDF plus the static SPA in one script:

```bash
scripts/export-deck.sh slidev slides.md dist
# raw equivalents:
npx slidev export --format pdf slides.md --output deck.pdf
npx slidev export --format pptx slides.md --output deck.pptx
npx slidev build slides.md --out dist/
npx serve dist/
```

`v-click` steps export as extra PDF pages — three clicks means three pages, which
is expected. Remove `v-drag` before export. PPTX is experimental and rasterizes
code blocks: verify monospace fallback at 14px+. REQUIRED for every Slidev deck: ship an HTTP launcher (e.g. `START-DECK.cmd` with `python -m http.server 8000 --directory dist` + open `http://localhost:8000/`) with a no-double-click-`dist/index.html` warning (`file://` renders blank), plus a PDF fallback artifact (`deck.pdf`) verified page-by-page. Build notes (required): Google Fonts offline risk — self-host via `public/fonts/` + `@font-face` or ship a system-font fallback stack for projector machines with no network; Slidev 52.x `cssMinify:false` workaround — if `slidev build` crashes in CSS minify (seen on 52.20), set `cssMinify: false` in config, rebuild, and re-verify over HTTP before shipping.

Marp — HTML, PDF, and native PPTX from one source:

```bash
scripts/export-deck.sh marp slides.md dist
# raw equivalents (note --allow-local-files for assets/):
npx marp slides.md -o deck.html --allow-local-files
npx marp slides.md -o deck.html --bespoke.transition --allow-local-files
npx marp slides.md -o deck.pdf --allow-local-files
npx marp slides.md -o deck.pptx --allow-local-files
```

The script's Marp path omits `--allow-local-files`: if exported output drops
local images, re-run the raw commands with the flag. PPTX degrades transitions
to static cuts — expected, not a defect.

## 4. Post-export checks

1. Open every artifact: HTML in Chromium and Firefox, PDF at 100% zoom, PPTX in PowerPoint and Google Slides.
2. Page count equals slide count — plus Slidev `v-click` step pages where applicable.
3. Zero clipped lines in the PDF; fonts embedded and readable in the PPTX (system fonts if PPTX is the deliverable).
4. Notes present: reveal.js speaker view via `?notes`, Slidev `<!-- -->` comments intact, Marp presenter notes in the HTML.
5. Console shows zero errors and zero 404s across a full walk in both browsers (Gate 16).
6. Ship the Markdown source alongside the built deck, plus the engine decision log from `references/engines.md`.

## 5. What ships per target

| Target | Artifacts | Notes |
|---|---|---|
| Live URL | `dist/` SPA (Slidev/reveal) or `deck.html` (Marp) + HTTP launcher (`START-DECK.cmd`) for every Slidev deck | serve to confirm, never `file://` for SPAs — launcher runs `python -m http.server` + warns no-double-click-`dist` |
| Handout | `deck.pdf` (REQUIRED fallback for every Slidev deck) | page count checked, notes version when the venue prints them |
| Send-ahead | `deck.pptx` (Marp native) or PDF chain (reveal/Slidev) | system fonts, cuts only |
| Always | Markdown source + engine decision log + ship record | source is diffable; the log explains the engine |

Engine decision log (paste from `references/engines.md`, filled):

```markdown
Engine: Slidev 52 (live code + v-click pedagogy)
Why not reveal.js: no custom runner needed; Markdown authorship is faster
Why not Marp: live code highlighting is essential, Marp renders code static
Export path: export-deck.sh slidev → PDF 15pp + dist/ SPA verified
Fallback: static PDF reads standalone; reduced-motion cuts verified
```

## 6. Worked ship record (Acme Q3 — 12 slides — Slidev 52)

```markdown
Deck: Acme Q3 — 12 slides — Slidev 52
Date: 2026-10-08 · Checker: Ada
- Outline approved: yes (v3, 2026-10-01, Jonas)
- 2-source rule: 6/6 stats sourced
- Images: 5 local, all ≤400KB, credited + licensed
- Contrast: fg/bg 15.8:1, muted/bg 6.1:1, muted/surface 4.9:1
- Placeholders: 0 hits on greps
- Fonts: 2 + mono · Code lines: max 9 · Gradients: 1
- Reduced motion: cuts verified in emulation
- Notes: 12/12 · Keyboard: pass · Mobile 390px: pass
- Export: PDF 15pp (12 + 3 v-click steps) clean, PPTX spot-check pass, console 0 errors
```

## 7. Handoff

Paste one line: `Export done: HTML + PDF + source shipped, ship record signed — deck is out.` If any check fails, stop shipping and open `governance/failure-recovery.md`.
