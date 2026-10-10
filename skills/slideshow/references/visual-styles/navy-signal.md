# Navy Signal — Deep Navy & Cyan

> Vibe: a command deck in a dark ops room. Deep navy, electric cyan signal lines, restrained. The default for engineering, network, and control-plane content.

**When to use:** infrastructure, networking, command-and-control, ops postmortems, platform engineering, anything where precision reads as competence. Live terminals look electric on this background.
**Avoid when:** the user explicitly asks for light/paper, or when the deck is a warm human story where cold blue fights the tone.

## Tokens (dark primary + light companion)

```css
:root {
  --bg: #F7FAFC; --surface: #E5EEF7; --card: #FFFFFF;
  --fg: #0E1B33; --muted: #5B6B85; --border: #D3DFEE;
  --primary: #1D5BD6; --accent: #0E7490;
  --success: #16A34A; --warning: #D97706;
  --code-bg: #0A1226; --code-fg: #DCE7F8;
}
.dark {
  --bg: #0A1226; --surface: #13203F; --card: #16264B;
  --fg: #EAF2FF; --muted: #8FA3C4; --border: #243A63;
  --primary: #4D9FFF; --accent: #22D3EE;
  --success: #22C55E; --warning: #FBBF24;
  --code-bg: #0A1226; --code-fg: #DCE7F8;
}
```

Contrast: dark `fg/bg` 14.6:1 AAA. Muted on dark surface 5.9:1 AA. Cyan `#22D3EE` marks signal/active states and lines — never body copy.

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

Shiki `vitesse-dark` primary, `vitesse-light` for handout. Code background stays `#0A1226` in both modes so screenshots match.

```js
const html = await codeToHtml(source, {
  lang: 'ts', themes: { light: 'vitesse-light', dark: 'vitesse-dark' }
});
```

## Gradient rule

One radial hero wash per deck, background only. Never gradient text. The wash reads as a signal sweep.

```css
.hero-navy {
  background:
    radial-gradient(1100px 480px at 80% -10%, rgba(77,159,255,.35), transparent 60%),
    radial-gradient(800px 400px at 10% 110%, rgba(34,211,238,.16), transparent 60%),
    #0A1226;
}
```

## Signature layout — ops hero + route strip

```html
<div class="slide-inner hero-navy" style="border-radius: 24px">
  <div class="eyebrow">Acme Field OS · Q3 postmortem</div>
  <h1>p95 from 412ms to 243ms.</h1>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:center;margin-top:24px">
    <pre style="background:#0A1226;color:#DCE7F8;border:1px solid #243A63;border-radius:16px;padding:20px;font-size:15px;margin:0"><code># before            # after
route /ingest       route /ingest
  4 workers           12 workers
  p95 412ms           p95 243ms</code></pre>
    <div style="border:1px solid #243A63;border-radius:16px;padding:20px;background:#16264B">
      <div style="font-size:.8rem;color:#8FA3C4">TRAFFIC</div>
      <div style="font-size:2.6rem;font-weight:800;color:#4D9FFF">31k</div>
      <div style="font-size:.9rem;color:#22D3EE">deploys / week · zero rollbacks</div>
    </div>
  </div>
</div>
```

## Per-engine notes

- **reveal.js:** set CSS vars on `:root` and `section.dark`; toggle `.dark` on `<html>`. Use `data-background-color="#0A1226"` for the hero slide.
- **Slidev (UnoCSS):** map tokens in `uno.config.ts` via `theme.colors`; apply with `bg-bg text-fg border-border`. Set `theme: default` + `colorSchema: dark`.
- **Marp (`@theme`):** define the dark tokens under `section.dark` in theme CSS; force `class: dark` in frontmatter for the dark look.

## Anti-slop don'ts

1. No purple-blue AI gradient cover. This navy is a flat field of signal, not a mesh gradient.
2. No cyan on everything — `#22D3EE` marks active signal lines, focus states, and data deltas only. One cyan element per slide.
3. No body text below 17px to fit more bullets. Split the slide instead of shrinking type.
