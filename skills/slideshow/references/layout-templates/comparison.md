# Comparison layout

> Decide first, prove second. Header states the verdict in plain words.
> Columns show the evidence. Reuses `layouts.md` split tokens:
> gap `24px`, cards `16px` radius, `1px solid var(--border)`,
> padding `24px`, `h2: clamp(1.5rem,3vw,2.25rem)`.

## When to use

- Before/after a migration, refactor, or pricing change.
- Option A vs option B when you recommend one of them.
- Us vs them for competitive positioning with numbers.
- Keep to two columns. Three-way splits cramp text and shrink type.

## Copy-paste HTML sketch

```html
<div class="slide-inner">
  <div class="eyebrow">Migration result — six weeks</div>
  <h2>Before the shield, after the shield</h2>
  <div class="tpl-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:24px">
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px">
      <div class="eyebrow">Before</div>
      <p style="font-size:18px;line-height:1.6;margin:12px 0 0">Origin hit on every request. p95 at 412ms. Deploys froze traffic for 40 seconds.</p>
      <p style="font-size:14px;opacity:.65;margin:12px 0 0">June edge logs, 4,120 requests sampled.</p>
    </div>
    <div style="background:#F0FDF4;border:1px solid #BBF7D0;border-radius:16px;padding:24px">
      <div class="eyebrow">After</div>
      <p style="font-size:18px;line-height:1.6;margin:12px 0 0">Shield absorbs 83% of repeats. p95 at 243ms. Deploys ship without traffic dips.</p>
      <p style="font-size:14px;opacity:.65;margin:12px 0 0">September edge logs, 6,840 requests sampled.</p>
    </div>
  </div>
</div>
```

## Spacing and type tokens

- Header `h2` at `clamp(1.5rem,3vw,2.25rem)`, `letter-spacing: -0.015em`.
- Eyebrow `13px`, uppercase, `letter-spacing: .12em`, `opacity: .65`.
- Body `18px/1.6`, caption `14px` muted under each column.
- Winner column gets the green wash `#F0FDF4` plus `#BBF7D0` border.
- Loser column stays on `var(--surface)` with `var(--border)`.

## Per-engine notes

- **reveal.js:** plain HTML inside one `<section>`. Add `class="fragment"` to
  the After card so it appears on second click. Speaker note in
  `<aside class="notes">` states the verdict sentence.
- **Slidev:** use `layout: two-cols` with `::right::` for the After column,
  or paste the HTML as-is. Add `v-click` on the winner card for staging.
- **Marp:** paste the HTML block verbatim. Markdown tables stretch badly
  in Marp themes, so keep the HTML grid. Center themes need a full-width
  wrapper around the grid.

## Responsive

```css
@media (max-width: 800px) {
  .tpl-grid { grid-template-columns: 1fr !important; }
}
```

## Accessibility

- Verdict is text, not color alone. The green wash never carries meaning solo.
- Keep reading order Before then After in DOM order for screen readers.

## Anti-slop don't

- Don't write a neutral header like "Comparison". Write the verdict:
  "Shield cut p95 by 41%".
