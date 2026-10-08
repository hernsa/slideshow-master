# Diagram layout

> CSS and inline SVG architecture boxes. Zero external libs.
> Reuses deck tokens: gap `16px`, radius `16px`, border
> `1px solid var(--border)`, captions `14px`, body `17-19px`.

## When to use

- System architecture: client, edge, origin, database in one view.
- Request flow where position implies responsibility.
- Build-vs-buy or layer cakes with 3-5 boxes.
- Reach for flowchart when order and decisions matter more than placement.

## Copy-paste HTML sketch

```html
<div class="slide-inner">
  <div class="eyebrow">Architecture — request path</div>
  <h2>Shield sits between edge and origin</h2>
  <div class="tpl-grid" style="display:grid;grid-template-columns:1fr auto 1fr auto 1fr;gap:16px;align-items:center;margin-top:24px">
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:20px;text-align:center">
      <div style="font-size:13px;opacity:.6;font-weight:700">CLIENT</div>
      <div style="font-weight:700;margin-top:8px">Browser</div>
      <div style="font-size:14px;opacity:.65">repeats 62%</div>
    </div>
    <div style="font-size:24px;opacity:.5" aria-hidden="true">→</div>
    <div style="background:#EFF6FF;border:2px solid #2563EB;border-radius:16px;padding:20px;text-align:center">
      <div style="font-size:13px;opacity:.6;font-weight:700">EDGE</div>
      <div style="font-weight:700;margin-top:8px">Shield cache</div>
      <div style="font-size:14px;opacity:.65">83% hit rate</div>
    </div>
    <div style="font-size:24px;opacity:.5" aria-hidden="true">→</div>
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:20px;text-align:center">
      <div style="font-size:13px;opacity:.6;font-weight:700">ORIGIN</div>
      <div style="font-weight:700;margin-top:8px">API fleet</div>
      <div style="font-size:14px;opacity:.65">rests, scales down</div>
    </div>
  </div>
  <p style="font-size:14px;opacity:.65;margin-top:16px">Reads left to right. Shield is the only new box.</p>
</div>
```

## Inline SVG variant for precise lines

```html
<svg viewBox="0 0 560 120" role="img" aria-label="Browser to shield to API flow" style="width:100%;height:auto;margin-top:24px">
  <rect x="8" y="20" width="150" height="80" rx="12" fill="var(--surface)" stroke="var(--border)" />
  <rect x="205" y="20" width="150" height="80" rx="12" fill="#EFF6FF" stroke="#2563EB" stroke-width="2" />
  <rect x="402" y="20" width="150" height="80" rx="12" fill="var(--surface)" stroke="var(--border)" />
</svg>
```

## Spacing and type tokens

- Box label `13px/700` muted, name `17px/700`, detail `14px` muted.
- Active box gets `2px` accent border; the rest stay `1px`.
- Arrows are `24px` text glyphs with `aria-hidden`, explained by caption.

## Per-engine notes

- **reveal.js:** pure HTML and SVG need no plugin. Animate by duplicating
  the slide with `data-auto-animate` and matching `data-id` per box.
- **Slidev:** same HTML works. UnoCSS `grid` plus `gap-4` is equivalent.
  Avoid Mermaid for this; hand boxes print more reliably.
- **Marp:** HTML plus inline SVG export cleanly to PDF and PPTX.
  No script-backed diagram lib survives Marp export, so keep it static.

## Responsive

```css
@media (max-width: 800px) {
  .tpl-grid { grid-template-columns: 1fr !important; }
}
```

## Accessibility

- Flow direction stated in the caption for screen-reader order.
- SVG carries `role="img"` plus `aria-label` with the takeaway.

## Anti-slop don't

- Don't import a diagram framework for three boxes. Hand boxes in CSS
  load instantly and survive offline projectors.
