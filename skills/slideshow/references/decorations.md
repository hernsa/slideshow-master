# Decorations & Asymmetry — Rules of Engagement

> Decoration is not noise. It is the visual grammar that makes a deck feel designed rather than generated. The rule: **decks must not be symmetrical-everywhere** — no three equal cards, no centered hero on every slide, no same five-layout loop. Vary composition; decorate deliberately; ship with restraint.

## 1. The anti-symmetry rule

Three equal cards in a row, centered hero, same 50/50 split repeated five times, every slide a card grid — this is the default AI look. Break it:

- **Vary layouts:** one bento, one split, one rail, one oversized-number slide, one full-bleed image, one centered CTA close.
- **Offset the grid:** push the main column left, float the visual right; the hero line does not have to sit dead center.
- **Mix aspect ratios** when using bento cells: one 2×2 hero cell, one tall cell, two small squares.
- **Use asymmetric margins:** a left rail with content indented right, or a right rail with content pulled left.
- **Intentional tension** beats accidental symmetry. If a slide would render three identical boxes, change two of them.

## 2. Decoration primitives (pick 1–2 per slide max)

| Primitive | What it is | Rule |
|---|---|---|
| **Kicker/eyebrow** | Small uppercase label above the heading | One per slide, `12–14px`, `letter-spacing .08em`, color `--accent` |
| **Rule bar** | 4px × 48px accent line under/near the heading | One per slide, `--primary`, never gradient |
| **Left rail** | Accent border on the slide's left edge | One per deck; signals a section change |
| **Oversized number** | Giant stat (`font-size 4–6rem`, weight 800) | One per slide, tabular figures, muted-label beside it |
| **Background shape** | Subtle SVG/CSS shape layer behind content | Opacity ≤ 8%; never a busy mesh; never behind text without a scrim |
| **Chip row** | Small pills summarizing categories | 2–4 chips per slide max, `border-radius 999px`, `--border` + `--card` |

## 3. Background shape layers (tasteful)

Shapes exist to add depth, not noise. Every shape layer must be at `opacity ≤ 0.08` behind content, or ≥ 0.9 as a deliberate flat-color band (never in-between where it fights the text).

```html
<!-- diagonal band, flat, behind nothing critical -->
<div style="position:absolute;top:-20%;right:-10%;width:60%;height:140%;background:var(--primary);opacity:.08;transform:rotate(12deg);border-radius:24px;z-index:0"></div>
<!-- soft radial glow, hero only -->
<div style="position:absolute;top:-30%;left:-20%;width:120%;height:120%;background:radial-gradient(circle at 30% 30%,var(--accent),transparent 60%);opacity:.07;z-index:0"></div>
<div style="position:relative;z-index:1">…slide content…</div>
```

Rules: shapes sit behind content (`z-index:0` with content `z-index:1`), never behind text without the 8% cap, rotate in multiples of 12°, and never animate. One shape layer per slide.

## 4. Oversized numbers (the "proof slide" move)

A single giant number carries more weight than a row of four. Use it for the slide's one takeaway.

```html
<div style="display:flex;align-items:baseline;gap:16px">
  <div style="font-size:6rem;font-weight:800;line-height:1;color:var(--primary);font-variant-numeric:tabular-nums">412ms</div>
  <div style="color:var(--muted);font-size:1rem">→ 243ms p95 · Q3</div>
</div>
```

## 5. Non-centered heroes

Center the hero once, then break it. A left-aligned headline with the visual right, an eyebrow that anchors top-left, a number that bleeds off the right edge — these read as designed, not templated.

```html
<div class="slide-inner" style="display:grid;grid-template-columns:1.2fr .8fr;gap:48px;align-items:center;min-height:100%">
  <div>
    <div class="eyebrow">ACME FIELD OS · Q3</div>
    <h1 style="text-align:left;margin:0 0 16px">Three revolutions, one idea.</h1>
    <p style="max-width:520px;color:var(--muted);font-size:1.15rem">One deck, three histories — how England, America, and France each reordered power.</p>
  </div>
  <div style="text-align:right">
    <div style="font-size:9rem;font-weight:800;color:var(--primary);opacity:.9;line-height:1">3</div>
    <div style="color:var(--muted)">revolutions · one idea</div>
  </div>
</div>
```

## 6. The decor budget

- 1–2 decoration primitives per slide. If a slide already has a background shape, skip the rule bar.
- Max 1 oversized number per slide; never two numbers fighting for the eye.
- Shape layers at ≤ 8% opacity; flat color bands at ≥ 0.9. No mid-opacity ghost text.
- Decoration must never be the reason a slide fails contrast (Gate 5) or reads cluttered.

## 7. Per-engine notes

- **reveal.js:** shapes are absolute-positioned `<div>`s inside the `<section>`; give them `z-index:0` and content `z-index:1`. Oversized numbers pair with `r-fit-text`.
- **Slidev:** use UnoCSS `absolute` positioning (`absolute right-0 top-0`), `opacity-8` utilities, and `layout: fact` for oversized numbers.
- **Marp:** shapes via `<div>` + inline style in Markdown; oversized numbers via `<!-- _class: fact -->` or a `.stat` class in the theme CSS.

## Anti-slop don'ts

1. No decorative SVG blobs behind every slide — one background shape per slide, most slides have none.
2. No emoji as decoration. Icons are inline SVG (`media/icons.md`), numbers are type, shapes are CSS/SVG geometry.
3. Symmetry is not a requirement, but chaos is not either. Every decorative element earns its place: it reinforces the takeaway or it leaves.
