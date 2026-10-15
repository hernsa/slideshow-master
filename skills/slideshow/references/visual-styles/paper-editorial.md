# Paper Editorial — Serif Keynote

> Vibe: essay, ink on paper, generous margins. Serif headings, hairline rules, zero glow.

**When to use:** 20-minute narrative arcs, memoirs, craft talks, founder stories where whitespace does the persuading.
**Avoid when:** dashboards, API references, or slides with more than four numbers. Serif numerals in tables look wrong; move those slides to GitHub Tech.

## Palette (explicit RGB — paste into build.py)

- BG `#1A1A18`
- INK `#F2EFE6`
- ACCENT `#F59E0B`
- ACCENT2 `#2DD4BF`
- MUTED `#A8A29E`
- CARD `#2A2925`

## Type

Headings `Fraunces` optical serif, body `Inter`, code `IBM Plex Mono`.

Map Display → hero/title tiers, Body → body tier, Mono → code/mono
lines only (`references/tokens.md`).

## PPTX notes

- Station this palette's ramp: BG → 2 mid stops → saturated break.
- No glow/decor shapes — hairlines, rules, and whitespace carry the style;
  never OuterGlow, never gradient fills on shapes.
- Plates darken the BG further in PIL; scrims use BG at 60–70% alpha.

## Anti-slop don'ts

1. No rounded neon cards or pill badges. A `#DDD8CC` hairline (0.75pt line) and a left rule are the decoration.
2. No tabular data in serif. Numbers, tables, and axes switch to `Inter` with tabular figures.
3. No three-column feature grids. One idea per slide; margins stay at 0.625in minimum.
