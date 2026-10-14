# Photo hero — true full-bleed

> Tokens in [tokens.md](../tokens.md). Edge-to-edge plate, scrim `≥60%` on the copy side, `≤25` words. Variants: dark (default) + pastel.

```python
slide = new_slide()
plate(slide, "assets/01_lab_night.jpg", 0.70)          # full-bleed, darkened + blurred in PIL
scrim_left(slide, 0.62)                                # a:alpha 38000 ≈ 62%, named "scrim-left"
kicker(slide, "ON SITE — AUGUST", x=0.65, y=4.3, color="#FFFFFF")
title(slide, "Deploy day, minus the fear", x=0.65, y=4.7, w=7.3, size=44, color="#FFFFFF")
body(slide, "Shield on. p95 243ms. Home by six.", x=0.65, y=5.8, w=7.0, size=16, color="#E8EEF9")
set_notes(slide, "Pause on the photo; read the three短句 slowly.")
```

Pastel variant: swap plate+scrim for a pastel ground and near-black type:

```python
slide = new_slide()
solid_bg(slide, "#BBE6F7")
title(slide, "Calm is a feature.", x=0.65, y=4.6, w=8.0, size=54, color="#1F2328")
```

## Slide spec

```
Slide N — <Title>                      bg: photo
  Text runs:  kicker {11pt} ; title {44pt ≤2 lines} ; body {≤25 words total}
  Z-order:    plate → scrim-left → copy
  Entrances:  none
  Anchors:    scrim-left shared with neighbors for the morph glide
  Images:     assets/<NN>_<name>.jpg (the plate)
  Done when:  copy sits fully inside the scrim on the render; ≤25 words.
```

## Don't

- Don't place white type below `60%` scrim or run past `25` words — cut words before lowering the scrim.
