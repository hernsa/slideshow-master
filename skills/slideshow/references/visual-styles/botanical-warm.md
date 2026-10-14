# Botanical Warm — Human / Edu

> Vibe: sunlit classroom, cream paper, leaf green. The friendliest palette here; trust over precision.

**When to use:** workshops, nonprofits, education, community talks, onboarding where warmth keeps attention.
**Avoid when:** dense dashboards (cream reduces perceived grid alignment) and late-night hacker venues where low light washes out cream backgrounds.

## Palette (explicit RGB — paste into build.py)

- BG `#1C1917`
- INK `#FAF7F0`
- ACCENT `#4ADE80`
- ACCENT2 `#FB923C`
- MUTED `#A8A29E`
- CARD `#292524`

## Type

Headings warm serif `Fraunces`, body `Inter`, one handwritten `Caveat` annotation per deck maximum.

Map Display → hero/title tiers, Body → body tier, Mono → code/mono
lines only (`references/tokens.md`).

## PPTX notes

- Station this palette's ramp: BG → 2 mid stops → saturated break.
- Glow/decor use ACCENT at low alpha (`deco_blob`, `glow()`); never
  OuterGlow, never gradient fills on shapes.
- Plates darken the BG further in PIL; scrims use BG at 60–70% alpha.

## Anti-slop don'ts

1. No second handwritten note. One `Caveat` annotation per deck; two reads as a greeting card.
2. No cream code blocks. Code sits on `#FFFFFF` with a `#E7DFCF` border, never on `#F5F0E6`.
3. No icon confetti or leaf-pattern borders. One terracotta rule plus real photography carries the warmth.
