# Swiss Minimal — Ultra-Clean Black on White

> Vibe: gallery wall, grid, enormous type. No decoration; spacing and scale do all the work.

**When to use:** manifesto talks, typographic keynotes, design portfolios where one sentence must fill the room.
**Avoid when:** data-dense reviews, live code demos, or any slide needing more than two proof points. Restraint fails when evidence matters.

## Palette (explicit RGB — paste into build.py)

- BG `#FFFFFF`
- INK `#0A0A0A`
- ACCENT `#0A0A0A`
- ACCENT2 `#DC2626`
- MUTED `#525252`
- CARD `#F5F5F5`

## Type

One family: `Inter` tight, or `Archivo` for a grotesque edge. No serif, no mono except code.

Map Display → hero/title tiers, Body → body tier, Mono → code/mono
lines only (`references/tokens.md`).

## PPTX notes

- Station this palette's ramp: BG → 2 mid stops → saturated break.
- No glow/decor shapes — spacing and scale do all the work;
  never OuterGlow, never gradient fills on shapes.
- Plates darken the BG further in PIL; scrims use BG at 60–70% alpha.

## Anti-slop don'ts

1. No icons, illustrations, or rounded cards. If the slide feels empty, enlarge the type instead of adding decoration.
2. No centered paragraphs or gradient headlines. Left edge alignment is the entire layout system.
3. No muted-gray body at small sizes. Body stays 14–15pt `#0A0A0A`; muted `#525252` is captions only.
