# Icons — inline vector glyphs, zero emoji (PPTX-native)

> Icons are drawn as native PowerPoint shapes, not pictures. No emoji
> anywhere — PowerPoint renders color-emoji inconsistently across machines
> and it reads as slop. Grep the OOXML for emoji codepoints in review.

## 1. The icon set (draw, don't import)

Build every icon from 2–4 native shapes: rounded rects, ellipses, triangles
(freeform), and straight connectors. Proven dozen: pin, arrow, check, play,
leaf, wave, book, chip, mic, star, quote-mark, calendar. One weight
(2.25pt lines or solid fills), one accent color per deck.

## 2. Construction rules

- **Connectors** (`MSO_CONNECTOR.STRAIGHT`) for leader lines: hairline
  (1pt) weight, accent color → transparent end. Leader = line + 0.16in dot
  (small ellipse) + 18pt label. The dot is the anchor, name it. Use
  `connect(...)` for the line and `dot(slide, name, cx, cy)` for the dot —
  or the composed `leader(...)` helper.
- **Pills swallow icons**: icon + label inside a rounded rect (`roundRect`,
  `adj` for full stadium). One font size (14–16pt semibold) for all pills
  in a deck.
- **Pairing**: icon first, label second, 0.11–0.17in gap. Never icon-only except
  the leader dot.
- **Reuse**: same icon shapes, same names (`icon-pin`), same positions
  across slides. Icons are morph anchors too.

## 3. Don'ts

- No emoji, no Wingdings/private-use glyphs, no icon fonts (Segoe UI Symbol
  falls back unpredictably).
- No imported PNG icons — they blur on export renders and can't recolor.
- Max 3 distinct icon shapes per deck. A fourth icon means a pill or label
  should have done the job.
