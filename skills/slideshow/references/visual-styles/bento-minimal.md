# Bento Minimal — Data Story

> Vibe: quiet grid, loud numbers. The most restrained palette here: blue bars, green deltas, nothing else.

**When to use:** metrics reviews, board updates, growth stories, experiment readouts where numbers carry the talk.
**Avoid when:** emotional narratives or customer stories. This palette has no warmth by design; move story slides to Botanical Warm.

## Tokens (light metrics + optional dark)

```css
:root {
  --bg: #FFFFFF; --surface: #F1F5F9; --card: #F8FAFC;
  --fg: #0F172A; --muted: #64748B; --border: #E2E8F0;
  --primary: #2563EB; --accent: #16A34A;
  --success: #16A34A; --warning: #D97706;
  --code-bg: #0D1117; --code-fg: #E6EDF3;
}
.dark {
  --bg: #0A0F1E; --surface: #151D33; --card: #101830;
  --fg: #E8EEF9; --muted: #8A93A6; --border: #26314D;
  --primary: #60A5FA; --accent: #4ADE80;
  --success: #4ADE80; --warning: #FBBF24;
  --code-bg: #0D1117; --code-fg: #E6EDF3;
}
```

Contrast: `fg/bg` 15.8:1 AAA. Green `#16A34A` on white is 3.3:1 — large numbers only, labels stay muted.

## Typography

Everything `Inter` with tabular numbers. Display numbers tighten tracking.

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
```

```css
--font-body: "Inter", system-ui, sans-serif;
.tnum { font-variant-numeric: tabular-nums; letter-spacing: -0.02em; }
.stat-num { font-size: 2.2rem; font-weight: 800; }
.stat-label { font-size: 12px; text-transform: uppercase; letter-spacing: .08em; }
```

## Code theme

Minimal code in data decks. When needed, `github-light` / `github-dark` on `#0D1117` blocks.

```js
const html = await codeToHtml(source, {
  lang: 'sql', themes: { light: 'github-light', dark: 'github-dark' }
});
```

## Gradient rule

One chart-series gradient allowed: bars fade top to bottom, never rainbow, never on text.

```css
.bar-primary { background: linear-gradient(180deg, #3B82F6 0%, #1D4ED8 100%); }
```

## Signature layout — hero metric bento

```html
<div class="slide-inner">
  <div class="eyebrow">Q3 readout · six weeks</div>
  <h2>Latency fell, volume held</h2>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:24px">
    <div style="grid-column:span 2;grid-row:span 2;background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:32px">
      <div class="stat-label" style="opacity:.65">P95 latency</div>
      <div class="tnum" style="font-size:3rem;font-weight:800">243ms</div>
      <div style="color:#16A34A;font-weight:600">▼ −41% in 6 wks</div>
    </div>
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px">
      <div class="stat-label" style="opacity:.65">Deploys/wk</div>
      <div class="tnum stat-num">31</div>
    </div>
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px">
      <div class="stat-label" style="opacity:.65">NRR</div>
      <div class="tnum stat-num">128%</div>
    </div>
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px">
      <div class="stat-label" style="opacity:.65">Churn</div>
      <div class="tnum stat-num">1.1%</div>
    </div>
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px">
      <div class="stat-label" style="opacity:.65">NPS</div>
      <div class="tnum stat-num">72</div>
    </div>
  </div>
</div>
```

Deltas always pair arrow plus sign with color so grayscale print still reads.

## Per-engine notes

- **reveal.js:** plain HTML grid inside `<section>`; collapse to 2 columns under 800px with the bento media query from layouts.
- **Slidev (UnoCSS):** `grid grid-cols-4 gap-4` with `col-span-2 row-span-2 rounded-2xl bg-slate-100 border p-8` on the hero cell.
- **Marp (`@theme`):** wrap grids in `<div style="width:100%">` since Marp themes center content; keep `aspect-ratio` on chart images.

## Anti-slop don'ts

1. No second accent color. Blue carries bars, green carries deltas, slate carries everything else.
2. No color-only deltas. Every `▲/▼` needs an explicit `+`/`−` sign and a unit.
3. No two-sentence bento cells. One line plus one metric per cell; overflow becomes a new slide.
