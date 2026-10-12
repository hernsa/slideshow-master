# Showcase — dark system

> Tokens in [tokens.md](../tokens.md). One page per slide. Near-black ground, white type, photo is decoration. No cards, no borders. One section per deck.

```html
<div style="position:absolute;inset:0;background:#06080F;color:#F5F5F7;display:grid;grid-template-columns:1fr 1fr;gap:32px;align-items:center;padding:48px">
  <div>
    <div class="eyebrow" style="color:#8EA2FF">Shield · live</div>
    <h1 style="color:#fff;margin:12px 0">83% never hits origin.</h1>
    <p style="color:#C7D0E0;font-size:1.1rem">September edge logs. 4.7M requests.</p>
    <code style="border:1px solid rgba(255,255,255,.2);border-radius:12px;padding:12px 20px">npx acme-deploy --preview</code>
  </div>
  <img src="assets/shield-dark.png" alt="Shield cache dashboard with 83 percent hit rate on black" style="width:100%;aspect-ratio:4/3;object-fit:cover;display:block" />
</div>
```

Rules: bg `#000`–`#0A0A0A`, body `#F5F5F7`, one accent only. Photos uncropped or arch-masked, never carded. Code stays `#0D1117` on dark.

## Don't

- Don't add card fills or `var(--border)` boxes here — the photo carries the texture.
