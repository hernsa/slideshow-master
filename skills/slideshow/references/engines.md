# Engines — reveal.js / Slidev / Marp Full Guide

> Pick exactly one engine per deck. Do not mix runtimes. The table below routes you in 30 seconds; the rest of this file keeps you shipping.

## Full comparison matrix

| Dimension | reveal.js 6 | Slidev 52 | Marp CLI |
|---|---|---|---|
| Authoring | HTML sections (+ Markdown plugin) | Markdown `slides.md` + Vue components | Markdown with directives |
| Runtime | Browser SPA, `Reveal.initialize()` | Vite + Vue 3 SPA | Static HTML (bespoke template) or static export |
| Motion | Auto-Animate, fragments, slide/bg transitions, parallax | Slide transitions, `v-click`, `v-motion`, `v-drag`, view-transition | 33 `transition` keywords, per-slide `_transition` |
| Code blocks | highlight.js / Shiki plugin, `data-line-numbers` | Shiki + Monaco runnable, `{1,3\|5}` highlights | Fenced code, theme CSS only |
| Live demo embeds | First-class iframes | First-class iframes + components | Screenshots preferred, iframes export-poorly |
| Export HTML | Serve `index.html` directly | `slidev build` → `dist/` SPA | `marp -o deck.html` single file |
| Export PDF | decktape via `?print-pdf` | `slidev export --format pdf` (Playwright) | `marp -o deck.pdf` (Chromium) |
| Export PPTX | Via decktape/PDF chain only | `slidev export` experimental (code as images) | `marp -o deck.pptx` native (static cuts) |
| Export PNG | decktape per-slide | `slidev export --format png` | `marp --images png` |
| Offline | Fully offline after `npm i` | Offline after build; dev needs node | Fully offline single file |
| Learning curve | Low (HTML) → medium (plugins) | Medium (Markdown + Vue when customizing) | Lowest (Markdown only) |
| Best for | Product tours, morph/chart stories, iframes | Dev talks, live code, click-step pedagogy | Conference submissions, fast text, clean handouts |
| Weak at | Long Markdown authorship | Print-perfect handouts, PPTX fidelity | True morph, interactivity |
| Example dir | `examples/reveal-demo/` | `examples/slidev-demo/` | `examples/marp-demo/` |

Routing rule restated: interactive / morph / iframes → reveal.js. Markdown-first / live code → Slidev. Fast text / clean export → Marp.

---

## Version pins + install commands

Pin in `package.json`, verify with `--version` before building. Never float `latest` in CI.

```json
{
  "devDependencies": {
    "reveal.js": "^6.0.0",
    "@slidev/cli": "^52.0.0",
    "@marp-team/marp-cli": "^4.1.0",
    "decktape": "^3.0.0"
  },
  "engines": { "node": ">=20" }
}
```

Install per engine (copy-paste):

```bash
# reveal.js
npm i reveal.js@^6.0.0
npx reveal --version 2>/dev/null || node -e "console.log(require('reveal.js/package.json').version)"

# Slidev
npm i -D @slidev/cli@^52.0.0
npx slidev --version

# Marp CLI (+ Chromium for PDF/PPTX)
npm i -D @marp-team/marp-cli@latest
npx marp --version
npx marp --bespoke.transition --version
```

Chromium note: Marp PDF and Slidev PDF export both drive headless Chromium. On CI install it explicitly:

```bash
npx playwright install chromium
# Marp fallback if Chrome missing:
# npx marp --pdf --allow-local-files slides.md
```

Verify checklist before building:

```bash
node --version        # want v20+
npx slidev --version  # want 52.x
npx marp --version    # want 4.x
```

---

## Minimal hello-world per engine (copy-paste)

### reveal.js hello-world

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="stylesheet" href="node_modules/reveal.js/dist/reset.css" />
  <link rel="stylesheet" href="node_modules/reveal.js/dist/reveal.css" />
  <link rel="stylesheet" href="node_modules/reveal.js/dist/theme/white.css" />
  <title>Acme — reveal hello</title>
</head>
<body>
  <div class="reveal">
    <div class="slides">
      <section>
        <h1>Ship calmly.</h1>
        <p>Preview deploys, p95 down 41%.</p>
        <aside class="notes">Open with the number. Pause. Then the story.</aside>
      </section>
      <section data-auto-animate>
        <h2 data-id="t">Pipeline</h2>
        <div data-id="bar" style="width:120px;height:24px;background:#2563EB;border-radius:6px"></div>
      </section>
      <section data-auto-animate>
        <h2 data-id="t">Pipeline: deployed</h2>
        <div data-id="bar" style="width:320px;height:24px;background:#16A34A;border-radius:6px"></div>
      </section>
    </div>
  </div>
  <script src="node_modules/reveal.js/dist/reveal.js"></script>
  <script>
    Reveal.initialize({ hash: true, transition: 'fade', autoAnimate: true });
  </script>
</body>
</html>
```

Serve + present: `npx serve .` then open `http://localhost:3000/`. Speaker view: append `?notes` on a second window.

### Slidev hello-world (`slides.md`)

```markdown
---
theme: default
transition: slide-left
title: Acme Q3
mdc: true
---

# Ship calmly.

Preview deploys · p95 down 41%

<!--
Speaker note: open with the number, then the story.
-->

---
transition: view-transition
---

# Pipeline: deployed

<div v-click>Edge cache hit</div>
<div v-click>Origin shield added</div>
<div v-click>p95 412ms → 243ms</div>

```ts {1,3}
const cache = new EdgeCache();
cache.enableShield();
deploy({ rollback: true });
```
```

Run + build:

```bash
npx slidev slides.md            # dev at localhost:3030
npx slidev build slides.md --out dist/
```

### Marp hello-world (`slides.md`)

```markdown
---
marp: true
theme: default
paginate: true
transition: fade 0.4s
---

# Ship calmly.

Preview deploys · p95 down 41%

---

<!-- _transition: cover-left 0.5s -->

# Pipeline: deployed

- Edge cache hit
- Origin shield added
- p95 412ms → 243ms

---

<!-- _transition: none -->

# Appendix

Raw weekly numbers live here. No motion, prints cleanly.
```

Render + present:

```bash
npx marp slides.md -o deck.html --allow-local-files
npx marp slides.md -o deck.pdf --allow-local-files
```

---

## Export commands per engine (HTML / PDF / PPTX / PNG)

### reveal.js exports

```bash
# 1. serve the deck (decktape needs a URL)
npx serve . -l 8000 &
# 2. PDF via print CSS
npx decktape reveal "http://localhost:8000/?print-pdf" deck.pdf
# 3. PNG per slide (loop pages)
npx decktape reveal --screenshots --screenshots-size 1920x1080 \
  "http://localhost:8000/" img/page.png
```

Notes: `?print-pdf` must load or pages come out blank. Fragments print as final state by default; `--fragments` flags control stepping. PPTX has no native path — export PDF then convert, or rebuild the deck in Marp for PPTX delivery.

### Slidev exports

```bash
# PDF (Playwright/Chromium)
npx slidev export --format pdf slides.md --output deck.pdf
# PNG per slide
npx slidev export --format png slides.md --output img/
# PPTX (experimental — code blocks rasterize)
npx slidev export --format pptx slides.md --output deck.pptx
# SPA static build
npx slidev build slides.md --out dist/
npx serve dist/
```

Notes: PPTX renders code blocks as images — verify monospace fallback and 14px+ size. `v-click` steps export as separate pages in PDF/PNG (expect 3 clicks = 3 pages). Remove `v-drag` before export.

### Marp exports

```bash
# HTML (single file, shareable)
npx marp slides.md -o deck.html --allow-local-files
# HTML with transitions (bespoke template)
npx marp slides.md -o deck.html --bespoke.transition --allow-local-files
# PDF
npx marp slides.md -o deck.pdf --allow-local-files
# PPTX (transitions degrade to static cuts — expected)
npx marp slides.md -o deck.pptx --allow-local-files
# PNGs
npx marp slides.md -o img/page.png --images png --allow-local-files
```

Notes: pass `--allow-local-files` whenever slides reference `assets/`. PPTX drops transitions and web fonts must be embedded — prefer system fonts if PPTX is the deliverable.

---

## Migration notes (moving a deck between engines)

### Marp → Slidev
1. Copy `slides.md` verbatim — frontmatter `theme`/`transition` mostly transfer.
2. Replace `---` + `<!-- _transition: X -->` overrides with Slidev `---\ntransition: X` per-slide frontmatter.
3. Replace one-slide-per-click-step with `v-click` blocks (collapses 5 Marp slides into 1 Slidev slide).
4. Re-test code blocks: Marp plain fences become Slidev `{lines}` highlights.

### Slidev → reveal.js
1. Expand each `v-click` into fragments: `<p class="fragment">`.
2. Expand `v-motion` entrances into `data-auto-animate` pairs or delete (static is fine).
3. Convert `layout: two-cols` into the 50/50 grid HTML from the layouts guide.
4. Rewire `slides.md` headings into `<section>` elements; move Slidev speaker comments (`<!-- -->`) into `<aside class="notes">`.

### reveal.js → Marp
1. Flatten Auto-Animate pairs into discrete slides (Marp has no morph — show start and end states).
2. Flatten fragments into discrete slides or keep only the final state for handouts.
3. Replace iframes with screenshots (`assets/demo-shot.png`) — Marp export cannot rely on live frames.
4. Set `transition: fade 0.4s` deck-wide; keep at most two `_transition` overrides.

### Any → PPTX-first delivery
1. Freeze one font stack (system fonts: Calibri/Segoe UI for corporate, Arial/Helvetica otherwise).
2. Replace all iframes with screenshots + URLs.
3. Set all transitions to `none`/`fade` — PPTX keeps cuts only.
4. Re-check code at 14px+ in screenshots; live syntax highlighting does not survive PPTX.

---

## Troubleshooting (5+ common errors per engine, with fixes)

### reveal.js

1. **Blank PDF from decktape.** Symptom: `deck.pdf` has correct page count but white pages. Cause: `?print-pdf` CSS did not load before capture. Fix: wait for `http://localhost:8000/?print-pdf` to render fully in a browser first, then re-run decktape with `--load-pause 2000`.
```bash
npx decktape reveal --load-pause 2000 "http://localhost:8000/?print-pdf" deck.pdf
```
2. **Auto-Animate does nothing.** Cause: sections not adjacent, or `data-id` mismatch (typo, different casing). Fix: confirm sibling `<section data-auto-animate>` elements and identical `data-id` strings; check console for `Reveal` errors.
3. **`Reveal is not defined`.** Cause: script path wrong after moving dirs. Fix: use `node_modules/reveal.js/dist/reveal.js` relative path or CDN pin `reveal.js@6.0.0`.
4. **Background image 404 in export.** Cause: relative `data-background-image="img/x.png"` resolved against decktape URL, not file path. Fix: serve from deck root and use `assets/`-rooted paths; verify in Network tab.
5. **Fragments skip on fast clicks.** Cause: double-advance from both clicker + keyboard. Fix: set `fragments: true, controls: true` and test with the actual clicker; disable `touch` if spurious.
6. **Fonts swap mid-morph.** Cause: webfont loads after Auto-Animate measures text. Fix: `preload` fonts + `font-display: swap`, or delay `Reveal.initialize` on `document.fonts.ready`.

### Slidev

1. **`slidev: command not found`.** Cause: `@slidev/cli` not installed locally or npx cache stale. Fix: `npm i -D @slidev/cli@^52.0.0` then `npx slidev --version`.
```bash
npm i -D @slidev/cli@^52.0.0
npx slidev --version
```
2. **PDF export hangs at Chromium.** Cause: Playwright Chromium missing. Fix: `npx playwright install chromium`, then re-run export with `--timeout 60000`.
3. **Code block renders gray / unhighlighted.** Cause: unknown `lang` tag or Shiki theme mismatch. Fix: use ` ```ts ` / ` ```js ` / ` ```bash ` explicitly; set `shiki` theme pair in frontmatter.
4. **`v-click` steps missing in PDF.** Cause: export captured only final state (older CLI default). Fix: upgrade to v52 and confirm per-step pages; each `v-click` should add a page.
5. **UnoCSS class silently ignored.** Cause: typo or non-default preset without config. Fix: check `uno.config.ts`, use standard utilities (`grid`, `gap-4`, `p-6`) first.
6. **SPA build blank on file://.** Cause: opening `dist/index.html` directly breaks asset paths. Fix: always `npx serve dist/` — SPA requires HTTP.

### Marp

1. **Local images missing in PDF/HTML.** Symptom: broken image icons. Cause: forgot `--allow-local-files`. Fix: re-run with the flag.
```bash
npx marp slides.md -o deck.pdf --allow-local-files
```
2. **Transitions do nothing.** Cause: default template ignores `transition` directives. Fix: export HTML with `--bespoke.transition`.
```bash
npx marp slides.md -o deck.html --bespoke.transition --allow-local-files
```
3. **PPTX fonts wrong.** Cause: web fonts not embedded in PPTX. Fix: switch to system fonts for PPTX deliverables, or embed via PowerPoint after export.
4. **Per-slide `_transition` ignored.** Cause: comment placed after content instead of at slide top, or misspelled `_transition`. Fix: first line of the slide must be `<!-- _transition: cover-left -->`.
5. **Paginate missing.** Cause: `paginate: true` absent from frontmatter. Fix: add it; style with `section::after` if custom numbering needed.
6. **Theme not found.** Cause: `theme: my-theme` without `--theme-set`. Fix: `npx marp slides.md --theme-set themes/ -o deck.html`.

---

## Engine decision log (paste into PR / notes)

```markdown
Engine: reveal.js 6 (product tour, morph + iframe demo)
Why not Slidev: no live-code editing needed; Auto-Animate carries the story
Why not Marp: morph + iframe are essential, Marp cannot do either live
Export path: serve + decktape PDF verified (12 pages), HTML shipped to /dist
Fallback: ?print-pdf static reads standalone; reduced-motion cuts verified
```
