# Timeline layout

> Sequential beats need order cues: dates, dots, and a connecting rail.
> Reuses `layouts.md` tokens: gap `16px`, radius `16px`,
> eyebrow `13px` uppercase, body `17-19px`, captions `14px`.

## When to use

- Project history with 3-6 dated milestones and one-line outcomes.
- Incident postmortems: what broke, what fixed it, what stuck.
- Roadmap quarters when order matters more than equality.
- Pick bento or stats when items are parallel, not sequential.

## Copy-paste HTML sketch

```html
<div class="slide-inner">
  <div class="eyebrow">June to September — six weeks</div>
  <h2>From Friday fear to calm deploys</h2>
  <div class="tpl-grid" style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:24px">
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px">
      <div style="font-size:13px;font-weight:700;opacity:.6">JUN 14</div>
      <div style="width:12px;height:12px;border-radius:50%;background:var(--primary);margin:12px 0"></div>
      <strong>Stall</strong>
      <p style="opacity:.7;margin:8px 0 0;font-size:16px">p95 412ms, 4 deploys a week.</p>
    </div>
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px">
      <div style="font-size:13px;font-weight:700;opacity:.6">JUL 02</div>
      <div style="width:12px;height:12px;border-radius:50%;background:var(--primary);margin:12px 0"></div>
      <strong>Shield staged</strong>
      <p style="opacity:.7;margin:8px 0 0;font-size:16px">Hit rate climbs to 61% in staging.</p>
    </div>
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px">
      <div style="font-size:13px;font-weight:700;opacity:.6">AUG 09</div>
      <div style="width:12px;height:12px;border-radius:50%;background:var(--primary);margin:12px 0"></div>
      <strong>Cutover</strong>
      <p style="opacity:.7;margin:8px 0 0;font-size:16px">p95 268ms, rollbacks automatic.</p>
    </div>
    <div style="background:#F0FDF4;border:1px solid #BBF7D0;border-radius:16px;padding:24px">
      <div style="font-size:13px;font-weight:700;opacity:.6">SEP 02</div>
      <div style="width:12px;height:12px;border-radius:50%;background:#16A34A;margin:12px 0"></div>
      <strong>Steady</strong>
      <p style="opacity:.7;margin:8px 0 0;font-size:16px">p95 243ms, 31 deploys a week.</p>
    </div>
  </div>
  <p style="font-size:14px;opacity:.65;margin-top:16px">Source: Acme edge logs plus deploy ledger.</p>
</div>
```

## Spacing and type tokens

- Date label `13px/700`, dot `12px` circle, title `17px/700`.
- Detail `16px` muted, card padding `24px`, gap `16px`.
- Final milestone carries the green wash to mark arrival.
- Header claims the arc, never just "Timeline".

## Per-engine notes

- **reveal.js:** wrap each cell in `class="fragment"` for staged walkthrough.
  Keep DOM order chronological so keyboard order matches the story.
- **Slidev:** stage with `v-click` per card. One slide holds all four steps;
  never split one timeline across two slides.
- **Marp:** HTML as-is. Marp export flattens staged steps, so the static
  four-up view must read cleanly on its own without clicks.

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

- Dates are real text (`JUN 14`), never color-only dots.
- Reduced-motion builds show all four cards at once.

## Anti-slop don't

- Don't stack six vague phases like "Discover, Define, Design".
  Name dated events with measured outcomes.
