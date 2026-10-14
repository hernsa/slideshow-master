# Bento Minimal — Data Story

> Vibe: quiet grid, loud numbers. The most restrained palette here: blue bars, green deltas, nothing else.

**When to use:** metrics reviews, board updates, growth stories, experiment readouts where numbers carry the talk.
**Avoid when:** emotional narratives or customer stories. This palette has no warmth by design; move story slides to Botanical Warm.

## Palette (explicit RGB — paste into build.py)

- BG `#0A0F1E`
- INK `#E8EEF9`
- ACCENT `#60A5FA`
- ACCENT2 `#4ADE80`
- MUTED `#8A93A6`
- CARD `#151D33`

## Type

Everything `Inter` with tabular numbers. Display numbers tighten tracking.

Map Display → hero/title tiers, Body → body tier, Mono → code/mono
lines only (`references/tokens.md`).

## PPTX notes

- Station this palette's ramp: BG → 2 mid stops → saturated break.
- Glow/decor use ACCENT at low alpha (`deco_blob`, `glow()`); never
  OuterGlow, never gradient fills on shapes.
- Plates darken the BG further in PIL; scrims use BG at 60–70% alpha.

## Anti-slop don'ts

1. No second accent color. Blue carries bars, green carries deltas, slate carries everything else.
2. No color-only deltas. Every `▲/▼` needs an explicit `+`/`−` sign and a unit.
3. No two-sentence bento cells. One line plus one metric per cell; overflow becomes a new slide.
