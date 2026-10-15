# Crimson Bold — Deep Maroon & Red

> Vibe: a raised fist in a dark hall. Deep maroon, signal red, gold as the only flame. The default for history, revolution, and any content that should feel urgent and alive.

**When to use:** history lessons, revolutions, social movements, protest/activism talks, anything with stakes and momentum. The default recommendation for classroom and narrative content.
**Avoid when:** the user explicitly asks for light/paper/minimal, or when the deck is a compliance/legal readout where red reads as danger. On bad projectors the dark maroon holds up better than any cream background.

## Palette (explicit RGB — paste into build.py)

- BG `#160D0D`
- INK `#FFF5F2`
- ACCENT `#E5484D`
- ACCENT2 `#F4C95D`
- MUTED `#B8A5A5`
- CARD `#241515`

## Type

Headings `Syne` 700 (bold, angular, protest-poster energy), body `Inter` 400/500, code `JetBrains Mono` 400.

Map Display → hero/title tiers, Body → body tier, Mono → code/mono
lines only (`references/tokens.md`).

## PPTX notes

- Station this palette's ramp: BG → 2 mid stops → saturated break.
- Glow/decor use ACCENT at low alpha (`deco_blob`, `glow()`); never
  OuterGlow, never gradient fills on shapes.
- Plates darken the BG further in PIL; scrims use BG at 60–70% alpha.

## Anti-slop don'ts

1. No full-bleed red-to-black linear gradient cover — that is a generic movie-poster cliché. Use the radial bonfire wash only.
2. No more than one gold accent per slide. `#F4C95D` marks numbers and data signals, never headers and never buttons in bulk.
3. No thin-weight serif body on the dark maroon. Keep body at Inter 400/500 minimum (≥14pt) or it crushes on a projector.
