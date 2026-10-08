# Glassmorphism — Frosted Cards Done Right

> Vibe: keynote vision film, depth, calm over color. Frosted cards floating above a deep, quiet gradient.

**When to use:** product visions, keynote closers, year-in-review montages where atmosphere carries the ending.
**Avoid when:** text-heavy explainers, printed handouts, projector rooms. Frost reads as gray smudge on bad bulbs and vanishes on paper.

## Tokens (deep base + frost)

```css
:root, .dark {
  --bg: #0B1020; --surface: rgba(255,255,255,.08); --card: rgba(255,255,255,.1);
  --fg: #F4F7FF; --muted: #A9B4C7; --border: rgba(255,255,255,.22);
  --primary: #7DD3FC; --accent: #C4B5FD;
  --success: #4ADE80; --warning: #FBBF24;
  --code-bg: rgba(13,17,23,.85); --code-fg: #E6EDF3;
}
```

Text `#F4F7FF` on the deep base clears 13:1. Muted `#A9B4C7` is captions only. Card borders stay 1px `rgba(255,255,255,.22)` so edges survive.

## Typography

Headings `Sora` or `Space Grotesk` 600, body `Inter`. Frost blurs thin type, so minimum weights are 600 for headings, 500 for labels.

```html
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet" />
```

```css
--font-display: "Sora", system-ui, sans-serif;
--font-body: "Inter", system-ui, sans-serif;
.glass h2 { font-weight: 600; letter-spacing: -0.015em; }
```

Body never drops below 17px on frost; blur plus small type destroys legibility.

## Code theme

Shiki `vitesse-dark` / `github-dark` inside a solid `#0D1117E6` block. Code never sits directly on frosted blur; it gets its own near-solid panel.

```js
const html = await codeToHtml(source, {
  lang: 'ts', theme: 'vitesse-dark'
});
```

## Gradient rule

The base may hold the deck's single gradient: one deep indigo-to-teal wash behind everything. Cards themselves stay flat frost, never gradients.

```css
.base-vision {
  background:
    radial-gradient(1100px 520px at 15% 0%, #1E2A5A 0%, transparent 60%),
    radial-gradient(900px 500px at 90% 20%, #0E4A4A 0%, transparent 55%),
    #0B1020;
}
.glass {
  background: rgba(255,255,255,.1);
  backdrop-filter: blur(18px) saturate(1.3);
  border: 1px solid rgba(255,255,255,.22);
  border-radius: 20px;
}
@media (prefers-reduced-transparency: reduce) {
  .glass { background: #1A2238; backdrop-filter: none; }
}
```

Max two glass cards per slide. The third element is flat text.

## Signature layout — vision base + two frost cards

```html
<div class="slide-inner base-vision" style="border-radius:24px;display:grid;grid-template-columns:1fr 1fr;gap:20px;padding:40px">
  <div class="glass" style="padding:28px">
    <div class="eyebrow">2027 vision</div>
    <h2>Calm software.</h2>
    <p style="color:#A9B4C7">Deploys fade into the background. Teams notice Fridays again.</p>
  </div>
  <div class="glass" style="padding:28px">
    <div style="font-size:2.4rem;font-weight:800">99.99%</div>
    <p style="color:#A9B4C7">Calm measured monthly. Status pages stay green through launches.</p>
    <img src="assets/calm.png" alt="Uptime chart holding steady at four nines across twelve months" class="fit" />
  </div>
</div>
```

## Per-engine notes

- **reveal.js:** `backdrop-filter` needs a positioned parent; set the base gradient on `<section>` and `.glass` on inner divs. Test in Chrome and Safari; Firefox needs `layout.css.backdrop-filter.enabled` history noted in speaker notes.
- **Slidev (UnoCSS):** `backdrop-blur-xl bg-white/10 border border-white/20 rounded-[20px]` reproduces `.glass`; base wash as arbitrary radial backgrounds.
- **Marp (`@theme`):** Marp export flattens `backdrop-filter` in PDF — ship a solid-fill fallback (`#1A2238`) as the export theme so print stays legible.

## Anti-slop don'ts

1. Max two glass cards per slide. Three frosted panels stack blur on blur and the text underneath turns to soup.
2. No frost without fallback. Every `.glass` ships the `prefers-reduced-transparency` solid fill; transparency-off users get `#1A2238`.
3. No small gray text on frost. Labels stay 14px+ at 500 weight in `#F4F7FF` or `#A9B4C7`; thin 12px captions dissolve in blur.
