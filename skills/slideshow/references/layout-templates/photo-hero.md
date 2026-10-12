# Photo hero — true full-bleed

> Tokens in [tokens.md](../tokens.md). One page per slide. Edge-to-edge photo, `inset:0`, scrim `≥60%`, `≤25` words. Variants: dark (default) + pastel.

```html
<div style="position:absolute;inset:0;overflow:hidden">
  <img src="assets/lab-night.jpg" alt="Acme lab at night with deploy dashboard glowing green" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover" />
  <div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(11,16,32,.82) 0%,rgba(11,16,32,.45) 55%,transparent 85%)"></div>
  <div style="position:absolute;left:48px;bottom:48px;max-width:560px">
    <div class="eyebrow" style="color:#fff">On site — August</div>
    <h1 style="color:#fff;margin:8px 0">Deploy day, minus the fear</h1>
    <p style="color:#E8EEF9;margin:0">Shield on. p95 243ms. Home by six.</p>
  </div>
</div>
```

Pastel variant: swap scrim for `BBE6F7` ground, near-black `#1F2328` type, single accent. Dark variant: `#0B1020` scrim, white type.

```html
<div style="position:absolute;inset:0;background:#BBE6F7;padding:48px;display:flex;align-items:flex-end">
  <h1 style="color:#1F2328;margin:0;max-width:12ch">Calm is a feature.</h1>
</div>
```

## Don't

- Don't place white type below `60%` scrim or run past `25` words — cut words before lowering the scrim.
