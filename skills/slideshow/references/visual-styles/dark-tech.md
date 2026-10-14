# Dark Tech — Neon on Near-Black

> Vibe: server room at 2am, phosphor mono, one live wire. Dev aesthetic with strict glow discipline.

**When to use:** hackathons, infra deep-dives, security talks, perf clinics where code and terminals dominate.
**Avoid when:** daylight keynotes, investor pitches, printed handouts. Neon dies under fluorescents and on paper.

## Palette (explicit RGB — paste into build.py)

- BG `#05070D`
- INK `#E2F3FF`
- ACCENT `#22D3EE`
- ACCENT2 `#A3E635`
- MUTED `#7D8DA6`
- CARD `#0B1220`

## Type

Display mono `JetBrains Mono` 700 for headings; body `Inter`; code `JetBrains Mono` 400.

Map Display → hero/title tiers, Body → body tier, Mono → code/mono
lines only (`references/tokens.md`).

## PPTX notes

- Station this palette's ramp: BG → 2 mid stops → saturated break.
- Glow/decor use ACCENT at low alpha (`deco_blob`, `glow()`); never
  OuterGlow, never gradient fills on shapes.
- Plates darken the BG further in PIL; scrims use BG at 60–70% alpha.

## Anti-slop don'ts

1. Max one glow per slide. Terminal glows or stat glows, never both, never borders plus text-glow plus shadow.
2. No rainbow syntax or multicolor headings. Cyan structure, lime live-value, slate everything else.
3. No stock circuit-board backgrounds. Near-black flat `#05070D` plus one mono grid overlay at 6% opacity is the texture ceiling.
