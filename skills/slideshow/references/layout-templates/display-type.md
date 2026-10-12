# Display type — giant statement

> Tokens in [tokens.md](../tokens.md). One page per slide. One line, one claim, type does the work. Pastel rotation allowed.

```html
<div class="slide-inner" style="min-height:70vh;display:flex;flex-direction:column;justify-content:center">
  <div class="eyebrow">Acme Corp · thesis</div>
  <h1 style="font-size:clamp(4rem,10vw,9rem);line-height:.95;letter-spacing:-0.03em;margin:16px 0">Ship calmly.</h1>
  <p class="lead">Preview deploys took p95 from 412ms to 243ms.</p>
</div>
```

Scale: `clamp(4rem,10vw,9rem)` up to ~138pt on wide screens. One accent word max in italic or mono: `Ship <em>calmly</em>.` Pastel rotation (`BBE6F7 → FFFDE4 → E2EFFB`) keeps saturation under ~35%, text near-black `#1F2328`.

```html
<div style="background:#FFFDE4;padding:48px;min-height:70vh;display:flex;align-items:center">
  <h1 style="font-size:clamp(4rem,10vw,9rem);color:#1F2328;margin:0">41% faster.</h1>
</div>
```

## Don't

- Don't stack a paragraph under giant type — one lead sentence, then stop.
