# Forest Ink — Deep Green & Amber

> Vibe: a night walk through a pine forest with a single lantern. Deep green, growing-teal, amber as the light source. The default for education, climate, sustainability, and grounded product strategy.

**When to use:** classrooms, environmental and climate content, sustainability strategy, health, education, anything that should feel alive and grounded without being cute. The default for teaching decks that still need to read bold on a projector.
**Avoid when:** the user explicitly asks for light/paper, or the content is pure cold engineering where green reads as "go" noise.

## Palette (explicit RGB — paste into build.py)

- BG `#0B1712`
- INK `#EEF7EF`
- ACCENT `#34D399`
- ACCENT2 `#FBBF24`
- MUTED `#93A89A`
- CARD `#13241C`

## Type

Headings `Sora` 700 (open, friendly, still bold), body `Inter` 400/500, code `JetBrains Mono` 400.

Map Display → hero/title tiers, Body → body tier, Mono → code/mono
lines only (`references/tokens.md`).

## PPTX notes

- Station this palette's ramp: BG → 2 mid stops → saturated break.
- Glow/decor use ACCENT at low alpha (`deco_blob`, `glow()`); never
  OuterGlow, never gradient fills on shapes.
- Plates darken the BG further in PIL; scrims use BG at 60–70% alpha.

## Anti-slop don'ts

1. No "eco-friendly" pastel leaf green on cream — that is the milky default in disguise. This style is dark-first and bold.
2. No amber on every heading. `#FBBF24` is the single lantern per slide; headers stay `#EEF7EF` or `#34D399`.
3. No three-equal-card rows everywhere. The strip above is one composition — vary split, bento, and rail layouts across the deck.
