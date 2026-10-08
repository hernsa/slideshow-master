# Midnight SaaS — Devtools Dark

> Vibe: late-night terminal, violet haze, confident. Dark-first; light exists only for handout PDF.

**When to use:** devtools launches, CLI product tours, evening meetups where the terminal is the hero. Live demos read beautifully on this background.
**Avoid when:** printed handouts, morning corporate keynotes, non-technical education decks. Dark tires unfamiliar readers and crushes on bad projectors.

## Tokens (dark primary + light companion)

```css
:root {
  --bg: #F8FAFC; --surface: #E2E8F0; --card: #FFFFFF;
  --fg: #0F172A; --muted: #64748B; --border: #E2E8F0;
  --primary: #2563EB; --accent: #7C3AED;
  --success: #16A34A; --warning: #D97706;
  --code-bg: #0D1117; --code-fg: #E6EDF3;
}
.dark {
  --bg: #0B1020; --surface: #1A2238; --card: #141B30;
  --fg: #E8EEF9; --muted: #8A93A6; --border: #2A3348;
  --primary: #4F7DF3; --accent: #9B6BFF;
  --success: #22C55E; --warning: #FBBF24;
  --code-bg: #0D1117; --code-fg: #E6EDF3;
}
```

Contrast: dark `fg/bg` 13.8:1 AAA. Muted on dark surface 5.1:1 AA. Never set body copy in primary or accent.

## Typography

Headings `Space Grotesk` 600, body `Inter` 400/500, code `JetBrains Mono` 400.

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
```

```css
--font-display: "Space Grotesk", system-ui, sans-serif;
--font-body: "Inter", system-ui, sans-serif;
--font-mono: "JetBrains Mono", ui-monospace, monospace;
h1 { font-size: clamp(2.2rem, 5vw, 3.6rem); letter-spacing: -0.02em; }
```

## Code theme

Shiki `vitesse-dark` primary, `vitesse-light` for handout. Code background stays `#0D1117` in both modes so screenshots match.

```js
const html = await codeToHtml(source, {
  lang: 'ts', themes: { light: 'vitesse-light', dark: 'vitesse-dark' }
});
```

## Gradient rule

One radial hero wash per deck, background only. Never gradient text.

```css
.hero-midnight {
  background:
    radial-gradient(1200px 500px at 20% -10%, rgba(79,125,243,.35), transparent 60%),
    radial-gradient(900px 420px at 90% 10%, rgba(155,107,255,.28), transparent 60%),
    #0B1020;
}
```

## Signature layout — terminal hero + stat strip

```html
<div class="slide-inner hero-midnight" style="border-radius: 24px">
  <div class="eyebrow">Acme Ship · v2.4 launch</div>
  <h1>Deploys that feel instant.</h1>
  <pre style="background:#0D1117;color:#E6EDF3;border:1px solid #2A3348;border-radius:16px;padding:20px;font-size:15px"><code>npx acme-deploy --preview
✓ preview ready in 41s · rollback armed</code></pre>
  <p style="color:#8A93A6">Preview URL per push · one-click rollback · p95 243ms</p>
</div>
```

## Per-engine notes

- **reveal.js:** set CSS vars on `:root` and `section.dark`; toggle `.dark` on `<html>`. Use `data-background-color="#0B1020"` for the hero slide.
- **Slidev (UnoCSS):** map tokens in `uno.config.ts` via `theme.colors: { bg, surface, card, fg, muted, border, primary, accent }`; apply with `bg-bg text-fg border-border`.
- **Marp (`@theme`):** define the dark tokens under `section.dark` in theme CSS; Marp export defaults to light so force `class: dark` in frontmatter for code slides.

## Anti-slop don'ts

1. No purple-to-blue full-bleed linear cover. The radial wash above is the only glow permitted.
2. No green decorative badges. `#22C55E` marks pass states and up-good deltas only.
3. No body text below 17px to fit more bullets. Split the slide instead of shrinking type.
