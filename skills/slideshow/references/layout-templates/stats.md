# Stats layout

> KPI comparison: label plus big number plus one honest delta.
> Reuses `layouts.md` stat-card tokens: gap `16px`, padding `24px`,
> label `12-13px` uppercase muted, number `2.2rem/800` tabular,
> delta `15px/600`, radius `16px`.

## When to use

- Traction slides, QBR snapshots, experiment readouts.
- Exactly 3-4 metrics that share one time window.
- Each card answers: what, how much, and which direction.
- Use bento when one hero metric dominates; use timeline when order matters.

## Copy-paste HTML sketch

```html
<div class="slide-inner">
  <div class="eyebrow">Evidence — June 14 to September 2</div>
  <h2>Latency fell, volume held</h2>
  <div class="tpl-grid" style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:24px">
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px">
      <small style="opacity:.65;letter-spacing:.08em">P95 LATENCY</small>
      <div style="font-size:2.2rem;font-weight:800;font-variant-numeric:tabular-nums">243ms</div>
      <span style="color:#16A34A;font-weight:600;font-size:15px">▼ −41% vs 412ms</span>
    </div>
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px">
      <small style="opacity:.65;letter-spacing:.08em">DEPLOYS / WEEK</small>
      <div style="font-size:2.2rem;font-weight:800;font-variant-numeric:tabular-nums">31</div>
      <span style="color:#16A34A;font-weight:600;font-size:15px">▲ 8× vs 4</span>
    </div>
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px">
      <small style="opacity:.65;letter-spacing:.08em">FAILED DEPLOYS</small>
      <div style="font-size:2.2rem;font-weight:800;font-variant-numeric:tabular-nums">2</div>
      <span style="opacity:.65;font-weight:600;font-size:15px">both auto-rolled back</span>
    </div>
  </div>
  <p style="font-size:14px;opacity:.65;margin-top:16px">Edge logs plus deploy ledger. Sampling error ±2 points.</p>
</div>
```

## Spacing and type tokens

- Numbers use `font-variant-numeric: tabular-nums` so digits align.
- Units live inside the number (`243ms`, `$2.4M`), never in the label alone.
- Deltas pair arrow plus sign plus color for projector safety.
- Caption line cites window plus method under the grid.

## Per-engine notes

- **reveal.js:** plain HTML grid in one `<section>`. Reveal each card with
  `class="fragment"` in DOM order. Record the three contrast pairs.
- **Slidev:** `flex gap-4` plus `p-6 rounded-2xl` works, or paste the HTML.
  Each `v-click` adds an export page, so expect 3 steps to mean 3 PDF pages.
- **Marp:** paste HTML verbatim. Marp centers content, so the outer
  `.slide-inner` keeps left alignment consistent with the rest of the deck.

## Responsive

```css
@media (max-width: 800px) {
  .tpl-grid { grid-template-columns: 1fr 1fr !important; }
}
@media (max-width: 520px) {
  .tpl-grid { grid-template-columns: 1fr !important; }
}
```

## Accessibility

- Never color alone: green still carries `▼ −41%` text.
- Print check: cards stay readable in grayscale because arrows persist.

## Anti-slop don't

- Don't ship four cards with mixed windows like "ARR, NPS, churn, uptime".
  One window, one story, comparable deltas.
