# Glassmorphism — Frosted Cards Done Right

> Vibe: keynote vision film, depth, calm over color. Frosted cards floating above a deep, quiet two-stop ramp.

**When to use:** product visions, keynote closers, year-in-review montages where atmosphere carries the ending.
**Avoid when:** text-heavy explainers, printed handouts, projector rooms. Frost reads as gray smudge on bad bulbs and vanishes on paper.

## Palette (explicit RGB — paste into build.py)

- BG `#0B1020`
- INK `#F4F7FF`
- ACCENT `#7DD3FC`
- ACCENT2 `#C4B5FD`
- MUTED `#A9B4C7`
- CARD `#1A2238`

## Type

Headings `Sora` or `Space Grotesk` 600, body `Inter`. Frost blurs thin type, so minimum weights are 600 for headings, 500 for labels.

Map Display → hero/title tiers, Body → body tier, Mono → code/mono
lines only (`references/tokens.md`).

## PPTX notes

- Station this palette's ramp: BG → 2 mid stops → saturated break.
- Glow/decor use ACCENT at low alpha (`deco_blob`, `glow()`); never
  OuterGlow, never gradient fills on shapes.
- Plates darken the BG further in PIL; scrims use BG at 60–70% alpha.

## Anti-slop don'ts

1. Max two glass cards per slide. Three frosted panels stack blur on blur and the text underneath turns to soup.
2. No frost without fallback. Every frosted card ships a solid-fill variant; transparency-off users get `#1A2238`.
3. No small gray text on frost. Labels stay ≥11pt at 500 weight in `#F4F7FF` or `#A9B4C7`; thin small captions dissolve in frost.
