# Data Graphics — Picker Index

> HTML equivalent of ppt-master tables/charts vocabularies. Pure HTML/CSS/SVG only — no external chart libs. All sketches reuse 8pt spacing (`8 / 16 / 24 / 32 / 48 / 64`) and CSS variables (`--bg, --surface, --card, --fg, --muted, --border, --primary, --accent, --success, --warning, --danger` + `.dark` overrides from `colors.md`).

Base tokens (paste once per deck):

```css
:root {
  --space-1: 8px; --space-2: 16px; --space-3: 24px;
  --space-4: 32px; --space-5: 48px; --space-6: 64px;
  --radius-card: 16px; --radius-pill: 999px;
}
.tnum { font-variant-numeric: tabular-nums; }
.dark {
  --bg: #0B1020; --surface: #1A2238; --card: #141B30;
  --fg: #E8EEF9; --muted: #8A93A6; --border: #2A3348;
  --primary: #4F7DF3; --accent: #9B6BFF;
  --success: #22C55E; --warning: #FBBF24; --danger: #F87171;
}
```

## Picker — which graphic for which story

| Story you tell | Graphic to use | File | Max per deck |
|---|---|---|---|
| Trend over time (deploys/wk, p95) | Line / sparkline (inline SVG polyline) | `charts.md §2` | 3 |
| Part-to-whole share (traffic split, failures) | Donut (SVG `stroke-dasharray`) | `charts.md §3` | 2 |
| Ranked comparison (regions, services) | Bar chart (flex bars, `%` widths) | `charts.md §1` | 3 |
| Single KPI + delta (p95, NRR, churn) | Progress ring + stat delta | `charts.md §4` | 2 slides |
| Exact values / plans (tiers, releases) | Comparison / metric table | `tables.md §1+§3` | 3 |
| Verdict across options (cache A vs B) | Feature checklist matrix | `tables.md §2` | 2 |
| Fuzzy judgment (risk, readiness) | Rating dots + note | `tables.md §4` | 2 |
| How it fits together (edge → origin) | Architecture boxes-and-arrows | `diagrams.md §1` | 2 |
| Who does what, in what order | Swimlane / flow | `diagrams.md §2` | 2 |
| When it happened (6-week recovery) | Vertical-rail timeline | `diagrams.md §3` | 2 |
| Who owns what (platform team) | Org / tree | `diagrams.md §4` | 1 |

## File pointers

- `charts.md` — bar, line/sparkline, donut, rings + deltas. Each: when-to-use, HTML sketch, per-engine notes, 1 don't.
- `tables.md` — comparison matrix, checklist, metric table, rating matrix. Zebra tokens + overflow rule.
- `diagrams.md` — architecture, swimlane, timeline, org/tree. Label rule: never under `14px`.

## Global rules (all data-graphics)

- Dark/light safe: fills use `var(--surface)` / `var(--card)`, text uses `var(--fg)` / `var(--muted)`, never raw hex outside `:root` / `@theme`.
- Numbers are `tabular-nums`; units live inside the number (`243ms`, `47.2%`).
- Deltas pair arrow + sign + color (`▲ +18%`, `▼ −41%`) so grayscale still reads.
- Type floor: chart labels `14px` minimum, diagram boxes `14–16px`, table body never below `15px` to fit.
- Responsive: every chart/table/diagram wraps or scrolls under `800px` — see per-file overflow rules.
- Captions mandatory: every graphic ends with a `14px muted` source line (dataset + window + owner).
- Per-engine: **reveal.js** = raw HTML in `<section>`; **Slidev** = same HTML or UnoCSS (`flex`, `grid`, `gap-4`); **Marp** = HTML `<div>` + `<style>`, screenshots for export.

## Anti-slop rule (the one rule)

- No 3D pies, no gradient rainbow series, no fake `99.99%` precision — use messy organic numbers (`47.2%`, `243ms`, `31 deploys/wk`) with a dated source line (`Edge logs, Jun 14 → Sep 2`).
