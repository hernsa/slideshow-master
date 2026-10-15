# Teal Serenity — Startup Pitch

> Vibe: calm water, confident ask, warm highlight. Teal CTAs; amber reserved for exactly one number per deck.

**When to use:** 10-slide pitch arcs (problem, solution, traction, team, ask), investor updates, clean SaaS stories.
**Avoid when:** technical deep-dives (teal code comments are low-contrast) or data-heavy reviews needing blue/green separation instead of teal/amber.

## Palette (explicit RGB — paste into build.py)

- BG `#0B1F1E`
- INK `#ECFDF5`
- ACCENT `#2DD4BF`
- ACCENT2 `#FBBF24`
- MUTED `#93A8A6`
- CARD `#123836`

## Type

Headings `Sora` 700, body `Inter`, numbers tabular.

Map Display → hero/title tiers, Body → body tier, Mono → code/mono
lines only (`references/tokens.md`).

## PPTX notes

- Station this palette's ramp: BG → 2 mid stops → saturated break.
- Glow/decor use ACCENT at low alpha (`deco_blob`, `glow()`); never
  OuterGlow, never gradient fills on shapes.
- Plates darken the BG further in PIL; scrims use BG at 60–70% alpha.

## Anti-slop don'ts

1. No second amber highlight. One amber number per deck; everything else stays teal, slate, or muted.
2. No teal paragraph text. `#0D9488` fails body contrast; paragraphs stay INK `#ECFDF5`.
3. No dashboard grid of eight charts. One chart plus three proof points is the pitch maximum.
