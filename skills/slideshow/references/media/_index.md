# Media — Picker Index

> Images + icons: the two things that separate a deck from a document. Pure HTML/CSS/inline-SVG only — no icon fonts, no CDN image hotlinks in shipped decks. All sketches reuse 8pt spacing (`8 / 16 / 24 / 32 / 48 / 64`) and CSS variables (`--bg, --surface, --card, --fg, --muted, --border, --primary, --accent, --success, --warning, --danger` + `.dark` overrides from `colors.md`).

Base tokens (paste once per deck):

```css
:root {
  --space-1: 8px; --space-2: 16px; --space-3: 24px;
  --space-4: 32px; --space-5: 48px; --space-6: 64px;
  --radius-card: 16px; --radius-pill: 999px;
}
```

## Picker — which media for which story

| Story you tell | Media to use | File | Max per deck |
|---|---|---|---|
| Proof it exists (screenshot, photo) | Framed image, `radius 16-24`, border + shadow | `images.md §2` | 1 per slide |
| Immersion (place, mood, scale) | Full-bleed + scrim ladder 60/70/78% | `images.md §2` | 1 per section |
| Brand tint on a photo | Duotone overlay, `mix-blend` + 40% black | `images.md §2` | 2 |
| App / site output | Browser-mock chrome (3 dots + img) | `images.md §2` | 3 |
| Person behind a quote | 64px avatar circle, `object-fit: cover` | `images.md §2` | 1 per quote |
| Text vs visual, 50/50 | Split-screen image panel | `images.md §2` | 3 |
| Action, status, direction | Inline SVG stroke icon (`currentColor`) | `icons.md §2+§3` | unlimited, 1 style |
| 3 features at a glance | Icon chips (surface circle + 24px icon) | `icons.md §4` | 1 row per deck |
| Sequence with owners | Timeline nodes with icons | `icons.md §4` | 2 |
| The one takeaway | Callout box with icon | `icons.md §4` | 1 per slide max |

## File pointers

- `images.md` — sourcing ladder (SVG → licensed → picsum wireframe-only), 6 treatments with HTML sketches, sizing/aspect rules, anti-white-wall rule, per-engine notes, 8 failures + fixes. Attribution format matches `scripts/verify-images.py` (`assets/<stem>.txt` + `CREDITS.md`).
- `icons.md` — inline-SVG-only system, 5 copy-paste icons (arrow-right, check, alert-triangle, chart-bar, quote-mark), 16→48px ladder, 4 layout sketches, per-engine notes, 6 failures + fixes.

## Global rules (all media)

- Offline-safe: no icon fonts, no hotlinked images in shipped decks — everything local or inline, so PDF export never breaks.
- Captions mandatory: every image ends with a `14px muted` caption or source line; every graphic cites dataset + window + owner.
- Dark/light safe: fills use `var(--surface)` / `var(--card)`, icons use `currentColor`, never raw hex outside `:root` / `@theme`.
- Type floor: captions `14px` minimum, never below.
- Per-engine: **reveal.js** = raw HTML in `<section>` (`data-background`, `r-frame`); **Slidev** = same HTML or UnoCSS; **Marp** = HTML `<div>` + `<style>`, screenshots for export.

## Anti-slop rules (the two rules)

- No 3 consecutive text-only slides — every 3rd slide changes surface (tinted divider, image bleed, accent band, dark quote). See `color-usage.md`.
- Zero emoji-as-icons. Ever.
