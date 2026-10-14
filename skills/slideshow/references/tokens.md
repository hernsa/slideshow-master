# Tokens — palette, type, spacing for real .pptx

> One palette per deck (4–6 hexes), locked at style-lock time. Explicit RGB
> everywhere — never MSO theme-color slots (they shift between machines).

## 1. Palette shape

- `BG` — stage color (near-black `06232B`-class for dark decks, white for
  light). Always an explicit bg rect, never "no fill".
- `INK` — primary text (`F5F5F7`-class on dark, near-black on light).
- `ACCENT` — one hero accent (jade/gold/crimson-class). One per deck story.
- `ACCENT2` — reserved for duo-box contrast (gold vs jade). Never a third.
- `MUTED` — secondary text, must still pass 4.5:1 on its surface.
- `CARD` — surface fill for boxes on dark (`0F333D`-class).

Derive the 3–4 stop value ramp from ACCENT by stepping lightness + alpha.
Longest identical-bg run ≤2 slides.

## 2. Type tiers (points, Segoe UI or locked pair)

| Tier | Size | Use |
|---|---|---|
| hero | 54–96pt bold | one statement per section |
| title | 40–44pt bold | slide titles |
| head | 28–32pt semibold | box heads, stat labels |
| label | 18–20pt semibold | kickers, pills, leaders |
| body | 14–16pt regular | max 4 lines per box |
| gloss | 11pt regular | translations, captions |

Zero letter-spacing (python-pptx `spacing` untouched). Vietnamese diacritics
verified in Segoe UI — if the locked pair lacks them, change the pair.

## 3. Spacing (inches, 13.333×7.5 canvas)

Margins 0.625in all sides. Copy column x[0.65, 5.6]. Vertical rhythm in
0.2in steps off the stations (kicker 1.9 / hero 2.3 / body 3.6–4.6 / pills
5.4–6.2). Gaps: 0.15in tight, 0.3in standard, 0.5in section breaks.
