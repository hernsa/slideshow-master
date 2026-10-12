# Framing — open / divide / close

> Tokens in [tokens.md](../tokens.md). One page per slide. This file owns framing; body patterns live in `references/layouts.md`, diagrams in `references/data-graphics/diagrams.md`. Shared boilerplate: see `_index.md` footer.

## Open (title hero)

```html
<div class="slide-inner" style="min-height:60vh;display:flex;flex-direction:column;justify-content:center">
  <div class="eyebrow">Acme Corp · Q3 engineering review · Oct 2026</div>
  <h1 style="margin:12px 0 0">Ship calmly.</h1>
  <p class="lead" style="margin-top:16px">How preview deploys took p95 from 412ms to 243ms in six weeks — and ended Friday fear.</p>
  <div style="display:flex;gap:12px;align-items:center;margin-top:24px">
    <img src="assets/ada.jpg" alt="Portrait of Ada Okafor" style="width:48px;height:48px;border-radius:50%;object-fit:cover" />
    <div><strong>Ada Okafor</strong><div style="opacity:.65;font-size:14px">Platform Lead, Acme</div></div>
  </div>
</div>
```

## Divide (numbered + number-free variant)

```html
<div class="slide-inner" style="min-height:60vh;display:flex;flex-direction:column;justify-content:center;gap:16px">
  <div style="font-size:5rem;font-weight:800;opacity:.14;line-height:1">02</div>
  <div class="eyebrow">Part two — evidence</div>
  <h1 style="margin:0">The pipeline recovered</h1>
  <p class="lead">Three changes, six weeks, p95 down 41%.</p>
</div>
```

```html
<div class="slide-inner" style="min-height:60vh;display:flex;flex-direction:column;justify-content:center">
  <div class="eyebrow">Acme Corp — Q3 review</div>
  <h1>Ship calmly.</h1>
  <p class="lead">Ada Okafor · Platform Lead · October 2026</p>
</div>
```

## Close (ask + QR variant)

```html
<div class="slide-inner" style="min-height:60vh;display:flex;flex-direction:column;justify-content:center;align-items:flex-start;gap:16px">
  <div class="eyebrow">Try it tonight</div>
  <h1 style="margin:0">Ship your next deploy<br />in one command.</h1>
  <code style="background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:12px 20px;font-size:1.05rem">npx acme-deploy --preview</code>
  <p style="opacity:.7;font-size:16px;margin:0">Slides plus demo: <strong>acme.dev/talks/q3</strong> · ada@acme.dev</p>
</div>
```

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

## Don't

- Don't headline the close "Thank you" and don't ship a divider without a number — headline the ask, number the chapters.
