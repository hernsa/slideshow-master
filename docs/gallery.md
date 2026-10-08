# Gallery — the three starter decks

All three starters tell the same 10-slide story ("Why HTML beats PPTX for
tech talks", Ada Demo, DevConf 2026) so you can compare engines directly.
Shared system: dark `#0B1020` + accent `#4F7DF3`, two font families + mono,
line-numbered 8-line `fetch` POST block, bento problem slide, 4-metric stat
row with deltas, inline-SVG split graphic, callout tip, CTA closer. Speaker
notes on every substantive slide, `prefers-reduced-motion` fallback in each.

> No screenshots are checked in — render locally (one command each, below)
> so what you see always matches the current source.

## reveal-demo — interactive / morph

`skills/slideshow/examples/reveal-demo/index.html` — standalone HTML,
reveal.js `5.1.0` CDN. `data-auto-animate` morph pair (hero metric 72 gray
→ 97 accent, shared `data-id`), fragment steps, `<aside class="notes">`
per slide.

```bash
cd skills/slideshow/examples/reveal-demo && python3 -m http.server 8000
# open http://localhost:8000 — S for speaker view, E for overview
```

## slidev-demo — Markdown-first / code-heavy

`skills/slideshow/examples/slidev-demo/slides.md` — frontmatter
(theme/transition/highlighter/fonts), `transition: slide-left`, `v-click`
steps, `v-motion` on both morph continuations, presenter-note comments.

```bash
cd skills/slideshow/examples/slidev-demo && npx --yes @slidev/cli@latest --open
```

## marp-demo — fast / clean export

`skills/slideshow/examples/marp-demo/deck.md` — `marp: true` frontmatter,
`/* @theme demo-dark */` block, global `_transition` plus per-slide
overrides (`fade`, `slide`, `none`, `zoom`, `cover-left`).

```bash
npx --yes @marp-team/marp-cli@latest skills/slideshow/examples/marp-demo/deck.md \
  -o /tmp/marp-demo.html --allow-local-files --preview
```
