# Engines — Routing Matrix

| Need | Route | Example |
|---|---|---|
| Interactive / morph / iframes | reveal.js → `examples/reveal-demo/` | Product tour with `data-auto-animate` chart morph + embedded demo iframe |
| Markdown-first / live code | Slidev → `examples/slidev-demo/` | Dev talk from `slides.md` with runnable code blocks and `v-click` steps |
| Fast text / clean export | Marp → `examples/marp-demo/` | Conference submission in Markdown, export to PDF + PPTX from CLI |

Pick exactly one engine per deck. Do not mix runtimes.

## Version pins

- reveal.js `6` (npm `reveal.js@^6.0.0`)
- Slidev `52` (npm `@slidev/cli@^52.0.0`)
- Marp CLI (npm `@marp-team/marp-cli@latest`)

Pin in `package.json`, verify with `npx <cli> --version` before building.

## Export notes

**reveal.js — decktape PDF:**
```bash
npx decktape reveal "http://localhost:8000/?print-pdf" deck.pdf
```
Serve the deck locally first. Print CSS (`?print-pdf`) must load or pages come out blank.

**Slidev — PDF / PNG / PPTX / SPA:**
```bash
npx slidev export --format pdf slides.md
npx slidev export --format png slides.md
npx slidev build slides.md --out dist/
```
PPTX export renders code blocks as images — check monospace fallback. SPA build goes to `dist/`.

**Marp — HTML / PDF / PPTX / images:**
```bash
npx marp slides.md -o deck.html
npx marp slides.md -o deck.pdf --allow-local-files
npx marp slides.md -o deck.pptx --allow-local-files
npx marp slides.md -o img/page.png --images png
```
Pass `--allow-local-files` when slides reference local images. PPTX drops transitions (static cuts) and web fonts must be embedded.
