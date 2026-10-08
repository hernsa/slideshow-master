# Section divider layout

> New chapter marker. Full-bleed number plus claim. Max 3 per deck.
> Reuses `layouts.md` divider tokens: ghost number `5rem/800/14%`,
> eyebrow `13px`, title `clamp(2.5rem,6vw,4rem)`, lead `1.2rem`.

## When to use

- Between major parts: stall, fix, proof.
- After a demo, to reset attention before numbers.
- Before a heavy data run, to state the verdict first.
- Never between every slide; dividers double slide count fast.

## Copy-paste HTML sketch

```html
<div class="slide-inner" style="min-height:60vh;display:flex;flex-direction:column;justify-content:center;gap:16px">
  <div style="font-size:5rem;font-weight:800;opacity:.14;line-height:1">02</div>
  <div class="eyebrow">Part two — evidence</div>
  <h1 style="margin:0">The pipeline recovered</h1>
  <p class="lead">Three changes, six weeks, p95 down 41%.</p>
  <div style="width:64px;height:4px;background:var(--primary);border-radius:999px;margin-top:8px"></div>
</div>
```

## Number-free variant for closings

```html
<div class="slide-inner" style="min-height:60vh;display:flex;flex-direction:column;justify-content:center">
  <div class="eyebrow">Acme Corp — Q3 review</div>
  <h1>Ship calmly.</h1>
  <p class="lead">Ada Okafor · Platform Lead · October 2026</p>
</div>
```

## Spacing and type tokens

- Ghost number is decorative with `aria-hidden` when read aloud;
  keep it out of the tab order narrative.
- Accent bar `64px` wide, `4px` tall, the single allowed gradient-free mark.
- One eyebrow, one title, one lead. No bullets on dividers.

## Per-engine notes

- **reveal.js:** `<section data-background-color="var(--bg)">` plus sketch.
  Pair with Auto-Animate from the prior divider by matching `data-id`.
- **Slidev:** `layout: section` or `layout: intro`. Native section
  layouts already center; keep the ghost number explicit.
- **Marp:** `<!-- _class: lead -->` plus `#` heading. Marp dividers
  print cleanly, so keep them text-only with no webfont dependency.

## Responsive

- Ghost number drops to `3.5rem` under `520px` to save vertical room.
- Title clamps; never force two lines into one with negative margins.

## Accessibility

- Number is context, so notes carry "Section 2 of 3" for navigation.
- Reduced-motion builds cut straight to dividers with no fade delay.

## Anti-slop don't

- Don't ship a divider without a number. Audiences ask questions
  by section, and "the middle part" helps nobody.
