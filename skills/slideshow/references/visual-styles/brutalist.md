# Brutalist — Raw Borders, Flat Color

> Vibe: photocopied zine, exposed structure, loud on purpose. Monospace, thick borders, zero radius.

**When to use:** art-code talks, protest tech, zine launches, workshops that reject corporate polish.
**Avoid when:** enterprise buyers, board updates, funerals and weddings of software. Raw reads as unfinished to risk-averse rooms.

## Palette (explicit RGB — paste into build.py)

- BG `#FFFDF0`
- INK `#111111`
- ACCENT `#2B4EFF`
- ACCENT2 `#FF4D00`
- MUTED `#555555`
- CARD `#F2EDDC`

## Type

Everything monospace: `Space Mono` or `IBM Plex Mono`. Headings uppercase, tight leading.

Map Display → hero/title tiers, Body → body tier, Mono → code/mono
lines only (`references/tokens.md`).

## PPTX notes

- Station this palette's ramp: BG → 2 mid stops → saturated break.
- Glow/decor use ACCENT at low alpha (`deco_blob`, `glow()`); never
  OuterGlow, never gradient fills on shapes.
- Plates darken the BG further in PIL; scrims use BG at 60–70% alpha.

## Anti-slop don'ts

1. No radius, no blur, no gradient — ever. A single `border-radius: 8px` collapses the entire stance.
2. No third flat color. Cobalt plus safety-orange plus ink is the complete set; teal, violet, and pastels are banned.
3. No lorem-length paragraphs. Forty words per slide maximum; overflow is a second slide with a new sticker number.
