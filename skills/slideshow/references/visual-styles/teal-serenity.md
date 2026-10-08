# Teal Serenity — Startup Pitch

> Vibe: calm water, confident ask, warm highlight. Teal CTAs; amber reserved for exactly one number per deck.

**When to use:** 10-slide pitch arcs (problem, solution, traction, team, ask), investor updates, clean SaaS stories.
**Avoid when:** technical deep-dives (teal code comments are low-contrast) or data-heavy reviews needing blue/green separation instead of teal/amber.

## Tokens (light pitch + dark demo companion)

```css
:root {
  --bg: #FFFFFF; --surface: #F0FDFA; --card: #FFFFFF;
  --fg: #0F172A; --muted: #5F6B7A; --border: #CCFBF1;
  --primary: #0D9488; --accent: #F59E0B;
  --success: #15803D; --warning: #B45309;
  --code-bg: #0D1117; --code-fg: #E6EDF3;
}
.dark {
  --bg: #0B1F1E; --surface: #123836; --card: #0F2E2C;
  --fg: #ECFDF5; --muted: #93A8A6; --border: #1F4D4A;
  --primary: #2DD4BF; --accent: #FBBF24;
  --success: #4ADE80; --warning: #FBBF24;
  --code-bg: #0D1117; --code-fg: #E6EDF3;
}
```

Contrast: light `fg/bg` 15.8:1 AAA. Teal `#0D9488` on white is 3.9:1 — buttons and large headings only, never paragraphs.

## Typography

Headings `Sora` 700, body `Inter`, numbers tabular.

```html
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet" />
```

```css
--font-display: "Sora", system-ui, sans-serif;
--font-body: "Inter", system-ui, sans-serif;
.tnum { font-variant-numeric: tabular-nums; letter-spacing: -0.02em; }
```

## Code theme

Shiki `vitesse-light` / `vitesse-dark`. Teal keywords render cleanly on both without extra tuning.

```js
const html = await codeToHtml(source, {
  lang: 'ts', themes: { light: 'vitesse-light', dark: 'vitesse-dark' }
});
```

## Gradient rule

One CTA gradient per deck, on the ask slide background only.

```css
.hero-teal {
  background: linear-gradient(135deg, #0D9488 0%, #0F766E 55%, #115E59 100%);
  color: #FFFFFF;
}
.hero-teal .muted { color: #CCFBF1; }
```

White on `#0D9488` is large-headings-only. Add a dark scrim if body text sits on the gradient.

## Signature layout — traction split with amber highlight

```html
<div class="slide-inner">
  <div class="eyebrow">Traction · last 12 months</div>
  <h2>Revenue compounding quietly.</h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:32px;align-items:center;margin-top:24px">
    <div>
      <div class="tnum" style="font-size:3.2rem;font-weight:800">$1.8M <span style="color:#F59E0B">ARR</span></div>
      <p style="color:#5F6B7A">Net retention 132% · burn multiple 1.4 · 21 months runway.</p>
      <a href="https://acme.dev/pitch" style="background:#0D9488;color:#fff;padding:12px 24px;border-radius:999px;text-decoration:none;font-weight:600">Book a deep dive</a>
    </div>
    <img src="assets/revenue.png" alt="ARR climbing from 0.4 to 1.8 million over twelve months" class="fit" />
  </div>
</div>
```

## Per-engine notes

- **reveal.js:** style CTA links as pills with `border-radius: 999px`; amber span only around the single highlight number.
- **Slidev (UnoCSS):** `bg-[#0D9488] text-white rounded-full px-6 py-3 font-semibold` for the CTA; `text-[#F59E0B]` for the highlight.
- **Marp (`@theme`):** define `a.cta { background: #0D9488; color: #fff; border-radius: 999px; padding: 12px 24px; }`.

## Anti-slop don'ts

1. No second amber highlight. One amber number per deck; everything else stays teal, slate, or muted.
2. No teal paragraph text. `#0D9488` fails body contrast; paragraphs stay `#0F172A`.
3. No dashboard grid of eight charts. One chart plus three proof points is the pitch maximum.
