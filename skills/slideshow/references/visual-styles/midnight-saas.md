# Midnight SaaS — Devtools Dark

> Vibe: late-night terminal, violet haze, confident. Dark-first; light exists only for handout PDF.

**When to use:** devtools launches, CLI product tours, evening meetups where the terminal is the hero. Live demos read beautifully on this background.
**Avoid when:** printed handouts, morning corporate keynotes, non-technical education decks. Dark tires unfamiliar readers and crushes on bad projectors.

## Palette (explicit RGB — paste into build.py)

- BG `#0B1020`
- INK `#E8EEF9`
- ACCENT `#4F7DF3`
- ACCENT2 `#9B6BFF`
- MUTED `#8A93A6`
- CARD `#1A2238`

## Type

Headings `Space Grotesk` 600, body `Inter` 400/500, code `JetBrains Mono` 400.

Map Display → hero/title tiers, Body → body tier, Mono → code/mono
lines only (`references/tokens.md`).

## PPTX notes

- Station this palette's ramp: BG → 2 mid stops → saturated break.
- Glow/decor use ACCENT at low alpha (`deco_blob`, `glow()`); never
  OuterGlow, never gradient fills on shapes.
- Plates darken the BG further in PIL; scrims use BG at 60–70% alpha.

## Anti-slop don'ts

1. No purple-to-blue full-bleed linear cover. The radial wash above is the only glow permitted.
2. No green decorative badges. `#22C55E` marks pass states and up-good deltas only.
3. No body text below 13pt to fit more bullets. Split the slide instead of shrinking type.
