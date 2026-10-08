# GitHub Tech — Corporate Neutral

> Vibe: calm, trustworthy, docs-led. Light-first; dark reserved for code slides. Prints perfectly.

**When to use:** corporate keynotes, API platform stories, decks that become PDF handouts or compliance-reviewed artifacts.
**Avoid when:** you need emotional punch. This palette is deliberately calm. Never add glow or neon; it breaks the contract.

## Tokens (light primary + dark code companion)

```css
:root {
  --bg: #FFFFFF; --surface: #F1F5F9; --card: #FFFFFF;
  --fg: #0D1117; --muted: #57606A; --border: #D0D7DE;
  --primary: #2563EB; --accent: #7C3AED;
  --success: #1A7F37; --warning: #9A6700;
  --code-bg: #0D1117; --code-fg: #E6EDF3;
}
.dark {
  --bg: #0D1117; --surface: #161B22; --card: #161B22;
  --fg: #E6EDF3; --muted: #8B949E; --border: #30363D;
  --primary: #4493F8; --accent: #A371F7;
  --success: #3FB950; --warning: #D29922;
  --code-bg: #0D1117; --code-fg: #E6EDF3;
}
```

Contrast: light `fg/bg` 18.1:1 AAA. Muted on surface 6.1:1 AA. Dark code pair 15.9:1 AAA.

## Typography

Single family `Inter` for headings and body; `JetBrains Mono` for code only.

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
```

```css
--font-display: "Inter", system-ui, sans-serif;
--font-body: "Inter", system-ui, sans-serif;
--font-mono: "JetBrains Mono", ui-monospace, monospace;
h2 { font-size: clamp(1.5rem, 3vw, 2.25rem); letter-spacing: -0.015em; }
```

## Code theme

Shiki `github-light` / `github-dark`. Matches GitHub rendering so pasted snippets look familiar.

```js
import { codeToHtml } from 'shiki';
const html = await codeToHtml(source, {
  lang: 'ts', themes: { light: 'github-light', dark: 'github-dark' }
});
```

## Gradient rule

One subtle surface wash on the title slide only. Nowhere else.

```css
.hero-github { background: linear-gradient(180deg, #F1F5F9 0%, #FFFFFF 70%); }
.dark .hero-github { background: linear-gradient(180deg, #161B22 0%, #0D1117 70%); }
```

## Signature layout — split claim + API snippet

```html
<div class="slide-inner">
  <div class="eyebrow">Platform update · Q3</div>
  <h2>One token, every service.</h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:32px;align-items:center;margin-top:24px">
    <ul style="line-height:1.9;font-size:18px">
      <li>Scoped keys per environment</li>
      <li>Automatic rotation, 30 days</li>
      <li>Audit log on every call</li>
    </ul>
    <pre style="background:#0D1117;color:#E6EDF3;border-radius:16px;padding:20px;font-size:15px;margin:0"><code>curl -H "Authorization: Bearer $ACME_KEY" \
  https://api.acme.dev/v1/deploys</code></pre>
  </div>
</div>
```

## Per-engine notes

- **reveal.js:** default CSS vars already close; override `--border` to `#D0D7DE` and add the hero wash class on the title `<section>`.
- **Slidev (UnoCSS):** use `bg-white text-[#0D1117] border-[#D0D7DE]` utilities or map `bg/surface/fg/muted/border` in `uno.config.ts` for reuse.
- **Marp (`@theme`):** set `section { background: #FFFFFF; color: #0D1117; }` and style `pre` with `#0D1117` background; code slides get `<!-- _class: dark -->`.

## Anti-slop don'ts

1. No glow, shadows, or neon on cards. A 1px `#D0D7DE` border is the entire elevation system.
2. No second font for headings. `Inter` 700 carries the hierarchy; a serif display face would break trust.
3. No icon wall of twelve features. Three bullets plus one snippet is the maximum density.
