# Navy Signal — Deep Navy & Cyan

> Vibe: a command deck in a dark ops room. Deep navy, electric cyan signal lines, restrained. The default for engineering, network, and control-plane content.

**When to use:** infrastructure, networking, command-and-control, ops postmortems, platform engineering, anything where precision reads as competence. Live terminals look electric on this background.
**Avoid when:** the user explicitly asks for light/paper, or when the deck is a warm human story where cold blue fights the tone.

## Palette (explicit RGB — paste into build.py)

- BG `#0A1226`
- INK `#EAF2FF`
- ACCENT `#4D9FFF`
- ACCENT2 `#22D3EE`
- MUTED `#8FA3C4`
- CARD `#13203F`

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

1. No purple-blue AI gradient cover. This navy is a flat field of signal, not a mesh gradient.
2. No cyan on everything — `#22D3EE` marks active signal lines, focus states, and data deltas only. One cyan element per slide.
3. No body text below 17px to fit more bullets. Split the slide instead of shrinking type.
