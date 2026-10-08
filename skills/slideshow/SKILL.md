---
name: slideshow
description: Create modern HTML slideshows via 7-phase workflow (intake, design read, research, images, engine route, build, verify+export). Routes reveal.js / Slidev / Marp. Anti-slop tokens enforced.
---

# Slideshow Skill (Hybrid Engine Router)

## Phase 1 — Intake
Ask: topic, audience, length, code-heavy?, notes?, export target (HTML/PDF/PPTX)?

## Phase 2 — Design Read (mandatory)
Output one line: "Reading this as: <kind> for <audience>, <vibe>, leaning toward <engine+palette>."
Set dials VARIANCE/MOTION/DENSITY per design-taste-frontend.

## Phase 3 — Research
2+ sources per claim. Verify code API versions.

## Phase 4 — Images
Hybrid source (AI/stock/local) → copy to `assets/` → log license → verify dimensions. See `references/verify-checklist.md`.

## Phase 5 — Route engine
- Interactive/morph/iframes → reveal.js
- Markdown-first/live code/Vue team → Slidev
- Fast text/clean export → Marp
Full matrix: `references/engines.md`.

## Phase 6 — Build
Markdown source first. Theme tokens from `references/colors.md`. Layouts from `references/layouts.md`. Animations from `references/animations.md`. Code blocks ≤12 lines, Shiki preferred.

## Phase 7 — Verify + Export
Run all gates in `references/verify-checklist.md`. Export via `scripts/export-deck`.
