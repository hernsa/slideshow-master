# Tables — construction + the handout rule (PPTX-native)

> A table on a slide is a concession. Earn it: ≤4 rows, ≤3 columns,
> 13pt minimum, or it becomes a handout page.

## 1. Construction (`table()` helper over python-pptx `add_table`)

- Use `table(slide, name, x, y, w, h, rows)` — rows[0] is the header. It
  rejects >4 rows / >3 cols and <13pt body outright.
- Header: solid accent fill + white 14pt semibold, one line per cell.
- Body: 13–14pt regular, ink on white or 8%-tint banding. No vertical
  rules; horizontal rules 0.75pt divider color only.
- Cell margins 0.05–0.08in; column widths set explicitly (never auto-fit
  surprises — set `table.columns[i].width`).
- Table frame inside the live zone with 0.625in margins respected.

## 2. The handout rule

If the table needs 10–12pt type, scrolling, or a 5th row, it is NOT a
slide. Options in order: (a) cut to 3 rows of verdicts, (b) convert to
flow pills or duo boxes, (c) move to an appendix slide marked `none`
transition + `NO-NOTES` exempt, (d) speaker-notes handout.

## 3. Don'ts

- No merged-header mazes, no nested tables, no images inside cells.
- Table numbers match research-notes verbatim (Gate 2) — no rounding
  surprises between the table and the spoken script.
