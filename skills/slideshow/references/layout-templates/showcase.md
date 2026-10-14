# Showcase — dark system

> Tokens in [tokens.md](../tokens.md). Near-black ground, white type, photo is decoration. No cards, no borders. One section per deck.

```python
slide = new_slide()
solid_bg(slide, "#06080F")
kicker(slide, "SHIELD · LIVE", x=0.65, y=1.9, color=ACCENT)
title(slide, "83% never hits origin.", x=0.65, y=2.3, w=5.0, size=44, color="#FFFFFF",
      accent="83%", accent_color=ACCENT)
body(slide, "September edge logs. 4.7M requests.", x=0.65, y=4.3, w=5.0, size=16, color="#C7D0E0")
body(slide, "npx acme-deploy --preview", x=0.65, y=5.0, w=5.0, size=16, mono=True, color="#F5F5F7")
rect_pic(slide, "feature", "assets/02_shield_dark.png", x=6.9, y=1.6, w=5.2, h=3.9)
```

Rules: bg `#000`–`#0A0A0A`, body `#F5F5F7`, one accent only. Photos uncropped or arch-masked, never carded. Code/mono lines stay light on dark.

## Slide spec

```
Slide N — <Title>                      bg: dark-solid
  Text runs:  kicker {11pt ACCENT} ; title {44pt} ; body {16pt} ; mono {16pt}
  Z-order:    bg → feature → copy
  Entrances:  feature .22s (optional; ≤3 total)
  Anchors:    feature frame reused across the section
  Images:     assets/<NN>_<name>.png (the feature photo)
  Done when:  no card fills, no border boxes; photo carries the texture.
```

## Don't

- Don't add card fills or border boxes here — the photo carries the texture.
