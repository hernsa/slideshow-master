# Paper Editorial — Serif Keynote

> Vibe: essay, ink on paper, generous margins. Serif headings, hairline rules, zero glow.

**When to use:** 20-minute narrative arcs, memoirs, craft talks, founder stories where whitespace does the persuading.
**Avoid when:** dashboards, API references, or slides with more than four numbers. Serif numerals in tables look wrong; move those slides to GitHub Tech.

## Tokens (paper light + evening dark)

```css
:root {
  --bg: #FAF9F6; --surface: #EFEDE6; --card: #FFFFFF;
  --fg: #1A1A18; --muted: #6B6660; --border: #DDD8CC;
  --primary: #B45309; --accent: #0F766E;
  --success: #15803D; --warning: #B45309;
  --code-bg: #FFFFFF; --code-fg: #1A1A18;
}
.dark {
  --bg: #1A1A18; --surface: #2A2925; --card: #242320;
  --fg: #F2EFE6; --muted: #A8A29E; --border: #3F3D38;
  --primary: #F59E0B; --accent: #2DD4BF;
  --success: #4ADE80; --warning: #FBBF24;
  --code-bg: #0D1117; --code-fg: #E6EDF3;
}
```

Contrast: light `fg/bg` 14.6:1 AAA. Muted on paper 5.3:1 AA. Burnt-orange `#B45309` passes barely; prefer `fg` for paragraphs.

## Typography

Headings `Fraunces` optical serif, body `Inter`, code `IBM Plex Mono`.

```html
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet" />
```

```css
--font-display: "Fraunces", Georgia, serif;
--font-body: "Inter", system-ui, sans-serif;
--font-mono: "IBM Plex Mono", ui-monospace, monospace;
.slide-inner { max-width: 880px; padding: 64px 48px; }
```

## Code theme

Shiki `github-light` on `#FFFFFF` cards, `github-dark` for the evening variant. Never tint code backgrounds cream; tint shifts syntax hues.

```js
const html = await codeToHtml(source, {
  lang: 'bash', themes: { light: 'github-light', dark: 'github-dark' }
});
```

## Gradient rule

Paper decks usually skip gradients. One warm vignette allowed on the closing slide.

```css
.hero-paper {
  background: radial-gradient(1000px 420px at 50% 110%, #EFEDE6 0%, #FAF9F6 65%);
}
```

## Signature layout — chapter divider with serif pull

```html
<div class="slide-inner">
  <div class="eyebrow">Chapter two · the slow years</div>
  <div style="font-size:4rem;font-weight:600;opacity:.16;font-family:Fraunces,serif">02</div>
  <h1 style="font-family:Fraunces,serif">We almost shut down twice.</h1>
  <div style="border-left:3px solid #B45309;padding-left:24px;margin-top:24px">
    <p style="font-family:Fraunces,serif;font-size:1.5rem;line-height:1.4;margin:0">“The second time, our largest customer wired the renewal early.”</p>
    <p style="opacity:.65;margin-top:12px">Mara Ellison — Founder, Fieldnotes</p>
  </div>
</div>
```

## Per-engine notes

- **reveal.js:** narrow `.slide-inner` to 880px, raise padding to 64px, set `h1/h2` to `Fraunces`. Hairline `hr` uses `var(--border)`.
- **Slidev (UnoCSS):** add `font-display: Fraunces, Georgia, serif` in `uno.config.ts`; use `max-w-[880px] mx-auto px-12 py-16` on the wrapper.
- **Marp (`@theme`):** `section { background: #FAF9F6; padding: 64px; }` with `h1 { font-family: Fraunces, serif; }`.

## Anti-slop don'ts

1. No rounded neon cards or pill badges. A 1px `#DDD8CC` hairline and a left rule are the decoration.
2. No tabular data in serif. Numbers, tables, and axes switch to `Inter` with tabular figures.
3. No three-column feature grids. One idea per slide; margins stay at 64px minimum.
