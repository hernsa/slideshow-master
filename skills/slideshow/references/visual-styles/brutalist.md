# Brutalist — Raw Borders, Flat Color

> Vibe: photocopied zine, exposed structure, loud on purpose. Monospace, thick borders, zero radius.

**When to use:** art-code talks, protest tech, zine launches, workshops that reject corporate polish.
**Avoid when:** enterprise buyers, board updates, funerals and weddings of software. Raw reads as unfinished to risk-averse rooms.

## Tokens (paper + ink + two flats)

```css
:root {
  --bg: #FFFDF0; --surface: #F2EDDC; --card: #FFFFFF;
  --fg: #111111; --muted: #555555; --border: #111111;
  --primary: #2B4EFF; --accent: #FF4D00;
  --success: #0E7A3D; --warning: #B45309;
  --code-bg: #111111; --code-fg: #FFFDF0;
}
```

Borders are 3px solid `#111111` everywhere. Radius is `0` everywhere. Two flats only: cobalt `#2B4EFF` and safety orange `#FF4D00`.

## Typography

Everything monospace: `Space Mono` or `IBM Plex Mono`. Headings uppercase, tight leading.

```html
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=IBM+Plex+Mono:wght@400;600&display=swap" rel="stylesheet" />
```

```css
--font-display: "Space Mono", ui-monospace, monospace;
--font-body: "Space Mono", ui-monospace, monospace;
h1 { font-size: clamp(2.4rem, 6vw, 4.2rem); text-transform: uppercase; line-height: .95; }
.sticker { background: var(--accent); color: #fff; padding: 4px 12px; display: inline-block; }
```

Uppercase headings plus one sticker label per slide is the hierarchy. No font-size ladder beyond h1 and body.

## Code theme

Shiki `github-dark` on `#111111` blocks with a 3px ink border and square corners. Light code does not exist here.

```js
const html = await codeToHtml(source, {
  lang: 'js', theme: 'github-dark'
});
```

## Gradient rule

None. No gradients, no shadows, no blur. Separation comes from 3px ink borders and flat color blocks.

```css
.card-brutal {
  background: #FFFFFF; border: 3px solid #111111;
  border-radius: 0; padding: 24px;
  box-shadow: 6px 6px 0 #111111;
}
```

The 6px hard offset shadow is the only depth allowed, and it is flat ink, never blur.

## Signature layout — manifesto + sticker + hard card

```html
<div class="slide-inner">
  <span class="sticker" style="background:#FF4D00;color:#fff;padding:4px 12px;font-weight:700">№ 03 — DEMO OR IT DIDN'T HAPPEN</span>
  <h1 style="font-family:'Space Mono',monospace">DELETE THE<br/>DASHBOARD.</h1>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:24px">
    <div style="background:#fff;border:3px solid #111;box-shadow:6px 6px 0 #111;padding:24px">
      <strong>RULE 01.</strong> One claim per slide.<br/><strong>RULE 02.</strong> Prove it live.
    </div>
    <pre style="background:#111;color:#FFFDF0;border:3px solid #111;padding:20px;font-size:15px;margin:0"><code>$ ./prove-it --live
PASS 31/31 · 41s</code></pre>
  </div>
</div>
```

## Per-engine notes

- **reveal.js:** kill default radius with `* { border-radius: 0 !important; }`; hard shadows as `box-shadow: 6px 6px 0 #111`.
- **Slidev (UnoCSS):** `border-3 border-black rounded-none shadow-[6px_6px_0_#111]` utilities; uppercase via `uppercase tracking-tight`.
- **Marp (`@theme`):** `section { background: #FFFDF0; font-family: 'Space Mono', monospace; }` with `h1 { text-transform: uppercase; }`.

## Anti-slop don'ts

1. No radius, no blur, no gradient — ever. A single `border-radius: 8px` collapses the entire stance.
2. No third flat color. Cobalt plus safety-orange plus ink is the complete set; teal, violet, and pastels are banned.
3. No lorem-length paragraphs. Forty words per slide maximum; overflow is a second slide with a new sticker number.
