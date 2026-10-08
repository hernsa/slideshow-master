# Two-column layout

> The default persuasive slide: claim left, visual right.
> Reuses `layouts.md` split tokens: `50/50` gap `32px`,
> `40/60` gap `32px`, text `18px/1.9`, visual bordered `16px` radius.

## When to use

- Any claim that needs one visual proof: screenshot, chart, quote.
- Feature beats: three bullets plus product shot.
- Problem beats: lead sentence plus failing graph.
- Split into two slides when both columns want paragraphs.

## Copy-paste HTML sketch

```html
<div class="slide-inner">
  <div class="tpl-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:32px;align-items:center">
    <div>
      <div class="eyebrow">Deploy story</div>
      <h2>Ships in minutes</h2>
      <ul style="line-height:1.9;font-size:18px;margin:16px 0 0;padding-left:20px">
        <li>One CLI command</li>
        <li>Preview URL per push</li>
        <li>One-click rollback</li>
      </ul>
      <p style="font-size:14px;opacity:.65;margin-top:16px">Staged one day before production. See notes for flags.</p>
    </div>
    <figure style="margin:0">
      <img src="assets/deploy.png" alt="Deploy dashboard showing green pipeline with preview URL" style="width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:16px;border:1px solid var(--border);box-shadow:0 8px 30px rgba(2,6,23,.08);display:block" />
      <figcaption style="font-size:14px;opacity:.65;margin-top:8px">Preview pipeline, August 9 build. Source: Acme internal.</figcaption>
    </figure>
  </div>
</div>
```

## Wide-visual variant (40/60)

```html
<div class="tpl-grid" style="display:grid;grid-template-columns:2fr 3fr;gap:32px;align-items:center">
  <div>
    <h2>p95 down 41%</h2>
    <p class="lead">Origin shield absorbed 83% of repeat traffic.</p>
    <p style="color:#16A34A;font-weight:700">412ms to 243ms</p>
  </div>
  <img src="assets/latency.png" alt="Latency chart falling from 412 to 243 milliseconds over six weeks" style="width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:16px;border:1px solid var(--border)" />
</div>
```

## Spacing and type tokens

- Text column: `h2` clamp, bullets `18px`, lead `1.2rem` at `60ch`.
- Visual column always bordered, `16px` radius, `16/9`, `cover`.
- Caption `14px` muted with source under every figure.

## Per-engine notes

- **reveal.js:** plain grid in one `<section>`. No built-in split prop;
  the sketch is the implementation. `r-stack` is for overlays only.
- **Slidev:** native `layout: two-cols`, `layout: image-right`, or
  `layout: image-left` with `::right::` slot. HTML also works verbatim.
- **Marp:** prefer the HTML grid. Marp `split` classes exist only in
  custom themes, and Markdown tables wrap badly at `390px`.

## Responsive

```css
@media (max-width: 800px) {
  .tpl-grid { grid-template-columns: 1fr !important; }
}
```

## Accessibility

- DOM order is claim then visual, matching narration order.
- Charts restate the takeaway in `alt`, never "chart image".

## Anti-slop don't

- Don't run two heavy text columns side by side. Cap the text side
  at three bullets plus one lead sentence.
