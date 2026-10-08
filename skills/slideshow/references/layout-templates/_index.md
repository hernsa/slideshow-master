# Layout templates — index

> All sketches reuse `skills/slideshow/references/layouts.md` tokens:
> spacing `8 / 16 / 24 / 32 / 48 / 64`, `h1: clamp(2rem,5vw,3.5rem)`,
> `h2: clamp(1.5rem,3vw,2.25rem)`, body `17-19px`, captions `14px`,
> `--radius-card: 16px`, `--radius-pill: 999px`,
> `.slide-inner { max-width: 1120px; margin: 0 auto; padding: 48px; }`,
> `.eyebrow`, `.lead`, `img.fit` (`16/9`, `cover`, `1px solid var(--border)`).
> Base deck CSS lives in `layouts.md` — paste it once, then paste any template below.

## All 12 types

| Type | Use when | File |
|---|---|---|
| comparison | before/after, A vs B, us vs them with a verdict header | [comparison.md](./comparison.md) |
| timeline | 3-6 sequential milestones with dates and one-line outcomes | [timeline.md](./timeline.md) |
| stats | 3-4 KPIs with deltas for traction or experiment results | [stats.md](./stats.md) |
| quote | one voice, one sentence, with face and role | [quote.md](./quote.md) |
| code-demo | 12 lines max beside live preview or screenshot | [code-demo.md](./code-demo.md) |
| diagram | CSS/SVG architecture boxes, no external libs | [diagram.md](./diagram.md) |
| flowchart | pure CSS steps with arrows, left-to-right or top-down | [flowchart.md](./flowchart.md) |
| title-hero | conference opener: claim plus credential, zero clutter | [title-hero.md](./title-hero.md) |
| section-divider | new chapter marker, max 3 per deck, numbered | [section-divider.md](./section-divider.md) |
| cta-closing | final Q&A backdrop: one ask plus one contact path | [cta-closing.md](./cta-closing.md) |
| image-fullbleed | one emotional beat with scrimmed text overlay | [image-fullbleed.md](./image-fullbleed.md) |
| two-column | claim left plus visual right, the default persuasive slide | [two-column.md](./two-column.md) |

## Picker rule

1. Ask: is the point sequential or parallel?
2. Sequential (steps, history, process) goes to `timeline.md` or `flowchart.md`.
3. Parallel (options, metrics, features) goes to `comparison.md` or `stats.md`.
4. Proof (voice, code, architecture) goes to `quote.md`, `code-demo.md`, or `diagram.md`.
5. Framing (open, divide, close, feel) goes to `title-hero.md`,
   `section-divider.md`, `cta-closing.md`, or `image-fullbleed.md`.
6. Default persuasive beat goes to `two-column.md`.
7. If two slides in a row use the same template, merge them or change
   the visual on the second one.

## How to use a template file

- Each file holds: when-to-use, copy-paste HTML sketch, spacing tokens,
  per-engine notes for reveal.js / Slidev / Marp, and one anti-slop rule.
- Copy the HTML into your slide, swap the Acme example content for real
  content, keep the gaps, radii, and type sizes as written.
- Keep `alt` text conclusion-first, for example
  `alt="Weekly p95 latency falling from 412 to 243 milliseconds"`.
- Every template collapses to one column under `800px`.
  Test at `390px` before shipping.
- One accent color per slide. Deltas always pair arrow plus sign
  with color, never color alone.
- Captions are `14px` with `opacity: .65` and a real source.

## Responsive collapse snippet

```css
@media (max-width: 800px) {
  .tpl-grid { grid-template-columns: 1fr !important; }
}
@media (max-width: 520px) {
  .tpl-grid { grid-template-columns: 1fr !important; }
  pre { font-size: 13.5px; overflow-x: auto; }
}
```

## Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  .fragment { opacity: 1 !important; transform: none !important; }
}
```

Anti-slop rule for this index: never paste two templates onto one slide.
One slide, one template, one point.
