# GitHub Tech — Corporate Neutral

> Vibe: calm, trustworthy, docs-led. Light-first; dark reserved for code slides. Prints perfectly.

**When to use:** corporate keynotes, API platform stories, decks that become PDF handouts or compliance-reviewed artifacts.
**Avoid when:** you need emotional punch. This palette is deliberately calm. Never add glow or neon; it breaks the contract.

## Palette (explicit RGB — paste into build.py)

- BG `#0D1117`
- INK `#E6EDF3`
- ACCENT `#4493F8`
- ACCENT2 `#A371F7`
- MUTED `#8B949E`
- CARD `#161B22`

## Type

Single family `Inter` for headings and body; `JetBrains Mono` for code only.

Map Display → hero/title tiers, Body → body tier, Mono → code/mono
lines only (`references/tokens.md`).

## PPTX notes

- Station this palette's ramp: BG → 2 mid stops → saturated break.
- Glow/decor use ACCENT at low alpha (`deco_blob`, `glow()`); never
  OuterGlow, never gradient fills on shapes.
- Plates darken the BG further in PIL; scrims use BG at 60–70% alpha.

## Anti-slop don'ts

1. No glow, shadows, or neon on cards. A 1px `#D0D7DE` border is the entire elevation system.
2. No second font for headings. `Inter` 700 carries the hierarchy; a serif display face would break trust.
3. No icon wall of twelve features. Three bullets plus one snippet is the maximum density.
