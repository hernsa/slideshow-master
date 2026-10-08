# Swiss Minimal — Ultra-Clean Black on White

> Vibe: gallery wall, grid, enormous type. No decoration; spacing and scale do all the work.

**When to use:** manifesto talks, typographic keynotes, design portfolios where one sentence must fill the room.
**Avoid when:** data-dense reviews, live code demos, or any slide needing more than two proof points. Restraint fails when evidence matters.

## Tokens (pure mono, single mode)

```css
:root {
  --bg: #FFFFFF; --surface: #F5F5F5; --card: #FFFFFF;
  --fg: #0A0A0A; --muted: #525252; --border: #0A0A0A;
  --primary: #0A0A0A; --accent: #DC2626;
  --success: #0A0A0A; --warning: #0A0A0A;
  --code-bg: #0A0A0A; --code-fg: #FAFAFA;
}
```

Single accent: signal red `#DC2626`, used at most once per deck for one word or one rule. Borders are black 2px, never gray hairlines.

## Typography

One family: `Inter` tight, or `Archivo` for a grotesque edge. No serif, no mono except code.

```html
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;700;800&family=Inter:wght@400;500&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet" />
```

```css
--font-display: "Archivo", "Inter", system-ui, sans-serif;
--font-body: "Inter", system-ui, sans-serif;
h1 { font-size: clamp(3rem, 8vw, 6rem); font-weight: 800; letter-spacing: -0.04em; line-height: .95; }
.rule { height: 4px; background: var(--fg); width: 96px; }
```

Grid: 12 columns, 24px gutters, 64px margins. Left-align everything; centering is banned except the closing word.

## Code theme

Shiki `github-light` on white, `github-dark` only when the code block is inverted to `#0A0A0A`. Code is rare here; prefer a giant command line over a file dump.

```js
const html = await codeToHtml(source, {
  lang: 'bash', themes: { light: 'github-light', dark: 'github-dark' }
});
```

## Gradient rule

None. Zero gradients in Swiss Minimal. Depth comes from scale contrast (96px title against 14px caption), never from fills.

```css
.hero-swiss { background: #FFFFFF; border-bottom: 2px solid #0A0A0A; }
```

## Signature layout — giant claim + rule + caption

```html
<div class="slide-inner" style="min-height:60vh;display:flex;flex-direction:column;justify-content:center">
  <div class="rule"></div>
  <h1 style="margin:24px 0">Ship<br/>calmly.</h1>
  <p style="font-size:19px;max-width:44ch">Preview deploys cut p95 from 412ms to 243ms. Ada Okafor, Acme Corp, October 2026.</p>
  <p style="font-size:14px;color:#525252;margin-top:32px">01 — Thesis · 20 minutes · three proofs</p>
</div>
```

## Per-engine notes

- **reveal.js:** disable default themes; set `section { background: #fff; color: #0A0A0A; text-align: left; }` and hard-code the 96px rule div.
- **Slidev (UnoCSS):** `text-left max-w-[1120px] mx-auto` wrapper; title as `text-[clamp(3rem,8vw,6rem)] font-extrabold tracking-tight leading-none`.
- **Marp (`@theme`):** `section { background: #fff; padding: 64px; } h1 { font-size: 84px; letter-spacing: -0.04em; }`.

## Anti-slop don'ts

1. No icons, illustrations, or rounded cards. If the slide feels empty, enlarge the type instead of adding decoration.
2. No centered paragraphs or gradient headlines. Left edge alignment is the entire layout system.
3. No muted-gray body at 15px. Body stays 18–19px `#0A0A0A`; muted `#525252` is captions only.
