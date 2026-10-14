# Charts — big numbers first, tables second (PPTX-native)

> Prefer a giant stat over a chart. Prefer a chart over a table. Prefer a
> 3-row table over a 6-row table. Density kills persuasion.

## 1. Giant stats (the default)

One 54–72pt number + 3–6 word label, left of copy or centered on a break
slide. Proven: `1994` / UNESCO listed · `1,600` / islands & islets. Gold on
dark, ink on light. The number is a morph anchor — count it up across slides
by duplicating the digit shape with a new value (Morph tweens it).

## 2. Native charts (when trends demand it)

python-pptx `add_chart` with `XL_CHART_TYPE.COLUMN_CLUSTERED` or `.LINE`
only. Then strip: no gridlines, no legend (label series directly in 14pt),
axis labels 12pt muted, data labels on the points, accent fills flat. Max 5
categories, max 2 series. Chart frame inside the live zone, never full-bleed.

## 3. Tables (last resort)

python-pptx `add_table`, ≤4 rows × ≤3 cols. Header row solid accent + white
14pt semibold; body 13–14pt; row banding with 8% tint, no vertical rules.
Cell margins 0.05–0.08in. A table that needs scrolling or 10pt type is a
handout, not a slide — cut it.

## 4. Don'ts

- No pie charts (angles lie), no 3D anything, no MSO theme-color fills
  (explicit RGB — theme slots shift between machines).
- Chart/table data MUST match research-notes numbers verbatim (Gate 2).
