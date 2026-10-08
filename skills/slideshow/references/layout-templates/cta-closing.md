# CTA closing layout

> Final slide that stays up during Q&A. One ask plus one contact path.
> Reuses `layouts.md` closing tokens: command `17px` mono,
> padding `12-20px`, radius `12px`, headline left-aligned.

## When to use

- Last slide of any talk, sized for photos from row ten.
- One command, one URL, one email max. Pick the path you will answer.
- Restates the thesis, introduces nothing new.
- Appendix follows only after this slide, never before it.

## Copy-paste HTML sketch

```html
<div class="slide-inner" style="min-height:60vh;display:flex;flex-direction:column;justify-content:center;align-items:flex-start;gap:16px">
  <div class="eyebrow">Try it tonight</div>
  <h1 style="margin:0">Ship your next deploy<br />in one command.</h1>
  <code style="background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:12px 20px;font-size:1.05rem">npx acme-deploy --preview</code>
  <p style="opacity:.7;font-size:16px;margin:0">Slides plus demo: <strong>acme.dev/talks/q3</strong> · ada@acme.dev</p>
  <p style="font-size:14px;opacity:.55;margin:0">Stays up during Q&A. No new charts after this point.</p>
</div>
```

## QR variant for in-person rooms

```html
<div class="slide-inner" style="display:grid;grid-template-columns:1fr auto;gap:32px;align-items:center;min-height:60vh">
  <div>
    <div class="eyebrow">Take the demo home</div>
    <h1>Scan for slides and repo.</h1>
    <p class="lead">Four-minute video plus the shield config.</p>
    <p><strong>acme.dev/talks/q3</strong></p>
  </div>
  <img src="assets/qr.png" alt="QR code linking to slides and demo at acme dot dev slash talks slash q3" style="width:180px;height:180px;border:1px solid var(--border);border-radius:16px" />
</div>
```

## Spacing and type tokens

- Command block is copyable at `17px`; never rasterize it as an image.
- Contact line `16px`, hint line `14px` muted.
- QR is `180px` square with border and radius, caption names the target.

## Per-engine notes

- **reveal.js:** final `<section>` with a subtle tint via
  `data-background-color`. Keep fragments off so the full ask photographs.
- **Slidev:** `layout: end` reuses intro styling. Check the built `dist/`
  version, since `end` themes shift alignment.
- **Marp:** final `#` slide with centered or left text. QR plus short URL
  both appear because venue Wi-Fi often blocks camera lookup pages.

## Responsive

- QR grid collapses to one column under `800px`; QR follows the text.
- Command block scrolls horizontally instead of shrinking.

## Accessibility

- QR never stands alone; the short URL sits beside it as text.
- Command is real `<code>` text for copy-paste and screen readers.

## Anti-slop don't

- Don't headline the slide "Thank you". Headline the ask, then say
  thanks with your voice while the URL stays on screen.
