# Flowchart layout

> Pure CSS steps with arrows. Order plus decisions, no libraries.
> Reuses deck tokens: gap `16px`, radius `16px`, padding `20px`,
> eyebrow `13px`, body `16-18px`, captions `14px`.

## When to use

- Deploy pipelines, auth flows, incident runbooks with 3-5 steps.
- Any path with one branch: happy path plus one escape hatch.
- Onboarding checklists where step 2 gates step 3.
- Use diagram when placement matters more than sequence.

## Copy-paste HTML sketch

```html
<div class="slide-inner">
  <div class="eyebrow">Deploy pipeline — four gates</div>
  <h2>Push to calm in four steps</h2>
  <div style="display:grid;grid-template-columns:1fr auto 1fr auto 1fr auto 1fr;gap:12px;align-items:stretch;margin-top:24px" class="tpl-grid">
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:20px">
      <div style="font-weight:800">1. Push</div>
      <p style="font-size:15px;opacity:.7;margin:8px 0 0">Preview URL spins up.</p>
    </div>
    <div style="align-self:center;font-size:22px;opacity:.5" aria-hidden="true">→</div>
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:20px">
      <div style="font-weight:800">2. Check</div>
      <p style="font-size:15px;opacity:.7;margin:8px 0 0">Tests plus shield replay.</p>
    </div>
    <div style="align-self:center;font-size:22px;opacity:.5" aria-hidden="true">→</div>
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:20px">
      <div style="font-weight:800">3. Promote</div>
      <p style="font-size:15px;opacity:.7;margin:8px 0 0">One command, staged.</p>
    </div>
    <div style="align-self:center;font-size:22px;opacity:.5" aria-hidden="true">→</div>
    <div style="background:#F0FDF4;border:1px solid #BBF7D0;border-radius:16px;padding:20px">
      <div style="font-weight:800">4. Verify</div>
      <p style="font-size:15px;opacity:.7;margin:8px 0 0">p95 watched 30 min.</p>
    </div>
  </div>
  <div style="border-left:4px solid #F59E0B;background:#FFFBEB;padding:12px 20px;border-radius:12px;margin-top:16px;font-size:15px">
    <strong>Branch:</strong> check fails go back to push with the log link. No silent skips.
  </div>
</div>
```

## Spacing and type tokens

- Step number plus name `17px/800`, detail `15px` muted.
- Arrows `22px` with `opacity: .5`, hidden from assistive tech.
- Branch callout holds the one decision; main rail stays linear.
- Top-down variant: change grid to one column with `↓` arrows.

## Per-engine notes

- **reveal.js:** reveal steps with `class="fragment"` per box, arrows
  always visible so the rail reads before the steps land.
- **Slidev:** `v-click` per step box. Keep arrows static outside clicks
  so layout never shifts mid-talk.
- **Marp:** static four-up reads cleanly in PDF. Marp has no staged
  fragments worth relying on, so the branch callout must make sense
  without animation.

## Responsive

```css
@media (max-width: 800px) {
  .tpl-grid { grid-template-columns: 1fr !important; }
}
```

## Accessibility

- DOM order matches step order. Arrows are decorative only.
- Branch logic is text, never an arrow color change.

## Anti-slop don't

- Don't draw six diamonds with yes/no spaghetti. One rail, one branch,
  each box under ten words.
