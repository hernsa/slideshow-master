# slideshow-master

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skill](https://img.shields.io/badge/skill-universal-blue.svg)](skills/slideshow/SKILL.md)
[![Engines](https://img.shields.io/badge/engines-reveal.js_%7C_Slidev_%7C_Marp-green.svg)](skills/slideshow/references/engines.md)

Universal agent skill for building modern HTML slideshows — conference-grade
decks with **bold themes, rotation, decorations, research-backed content**, and
full verification, not AI-slop defaults.

**How it works:** a Hybrid Engine Router. The agent runs a 7-phase workflow
(Intake → Design Read → **Research (artifact)** → Images → **Outline + Visual Plan** → Build → Verify+Export)
and picks the right engine per deck: **reveal.js** for interactive/morph
decks, **Slidev** for Markdown-first/code-heavy decks, **Marp** for fast
text decks with clean export.

## Contents

```
skills/slideshow/
├── SKILL.md                    # lean router: route table, vocabulary, discipline
├── workflows/
│   ├── routing.md              # deterministic router: mode + engine + style
│   ├── generate-deck.md        # full Default procedure (Plan → Do·Check·Act)
│   └── quick-generate.md       # 15-minute fast path (fixed style, Marp-first)
├── references/
│   ├── modes/                  # 5 narrative arcs: tech-talk, pitch, tutorial, showcase, narrative
│   ├── visual-styles/          # 13 styles (STRONG default + SOFT explicit) + picker + styles_index.json
│   ├── layout-templates/       # 12 slide types (comparison … two-column) + picker + templates_index.json
│   ├── data-graphics/          # charts, tables, diagrams (pure HTML/CSS/SVG) + picker + graphics_index.json
│   ├── media/                  # images + icons guides + picker + media_index.json
│   ├── decorations.md          # asymmetry primitives: kicker, rule-bar, left-rail, oversized number, bg shape, chip row
│   ├── color-usage.md          # deploy color per slide: rotation scripts, dividers, bands
│   ├── engines.md              # reveal.js vs Slidev vs Marp matrix + version pins
│   ├── animations.md           # Auto-Animate, morph, FLIP, View Transitions, fragments
│   ├── colors.md               # 6 palettes, dark/light tokens, fonts, code themes
│   ├── layouts.md              # bento, split, callout, stat, quote, code+preview, images
│   └── verify-checklist.md     # 23 gates: images, contrast, placeholders, motion, fragment budget, notes, export, theme, density, decorations
├── scripts/
│   ├── new-deck-scaffold.sh    # scaffold a new deck from a starter
│   ├── verify-images.py        # check assets are local, sized, credited
│   ├── verify-deck.py          # check slide structure: V/T density, no TTT, fragment budget, content density, theme rotation
│   └── export-deck.sh          # build HTML / PDF / PPTX per engine
└── examples/
    ├── reveal-demo/            # full reveal.js starter deck (11 slides) — rotation demo
    ├── slidev-demo/            # full Slidev starter deck (11 slides) — rotation demo
    └── marp-demo/              # full Marp starter deck (11 slides) — rotation demo
```

Repo-level: `docs/` (getting-started, gallery, faq, why-html-slides,
roadmap), `CONTRIBUTING.md` (add a style / palette / template / mode).

## Gallery — the three starter decks

All three tell the same 11-slide story ("Why HTML beats PPTX for tech
talks") so engines compare directly: **dark `#0B1020` + accent `#4F7DF3`**,
**morph pair + rotation** (tinted quote slide), fragments, notes, reduced-motion fallback.
Starters ship passing all 23 verify gates.

| Starter | Best for | Preview |
|---|---|---|
| `examples/reveal-demo/` | Interactive / morph / live demos | `python3 -m http.server` + open `index.html` (`S` speaker view) |
| `examples/slidev-demo/` | Markdown-first / live code | `npx @slidev/cli --open` on `slides.md` |
| `examples/marp-demo/` | Fast text / clean export | `marp-cli deck.md --preview` |

Render commands + per-deck details: [`docs/gallery.md`](docs/gallery.md).

## Install (one skill, every harness)

- **Claude Code:** copy `skills/slideshow/` → `.claude/skills/slideshow/`
  (project) or `~/.claude/skills/slideshow/` (global)
- **opencode:** copy `skills/slideshow/` → `.opencode/skills/slideshow/`
  (or `.agents/skills/slideshow/` — both are discovered)
- **Codex:** copy `skills/slideshow/` → `.codex/skills/slideshow/`

No dependencies to install for the skill itself. Each *engine* needs its
own toolchain only when you build with it (Node for reveal.js/Slidev/Marp;
`marp-cli` for Marp export; `decktape` for reveal.js PDF).

## Router (which engine when)

| Need | Engine | Starter |
|---|---|---|
| Interactive / morph / iframes / live demos | reveal.js | `examples/reveal-demo/` |
| Markdown-first / live code / Vue team | Slidev | `examples/slidev-demo/` |
| Fast text / clean export / non-dev author | Marp | `examples/marp-demo/` |

Unsure or mixed? Default to reveal.js — widest capability envelope.
Full trade-off matrix in `skills/slideshow/references/engines.md`.

## Workflow (what the agent does)

1. **Route** — request → ONE workflow (`generate-deck` or `quick-generate`)
   + ONE mode + engine + visual style (`workflows/routing.md`)
2. **Intake & Design Read** — questions, one-line Design Read, dials
3. **Research (artifact)** — run `topic-research.md`, produce `research-notes.md`
   (4-8 bullets/slide, 2-source log, ship-blocking)
4. **Outline + Visual Plan** — one line/slide with `bg:` tag, `visual-plan.md`
   (SVGs to draw + images to source), depth rule (≥1.5x topics), nod
5. **Images + Decorations** — execute `visual-plan.md`, `assets/CREDITS.md`,
   decorations.md primitives, asymmetry enforced
6. **Build** — Markdown source → theme → layouts → morph → code → notes
7. **Verify + Export** — 23 gates (`verify-checklist.md`), repair at owning
   layer, export HTML / PDF / PPTX, ship source + decision log

Details: `skills/slideshow/SKILL.md` + `skills/slideshow/workflows/`.

## Anti-slop contract

Every deck the skill produces must pass: **explicit STRONG palette (no cream defaults)**, body contrast ≥4.5:1 / 7:1 projector, **color rotation** (max 2 consecutive same-bg), **content density** (≥2x via research-notes.md), **decorations & asymmetry** (1-2 primitives/slide, no three-equal-cards), max 1 gradient (accent bar or ≤8% glow — never purple-blue), 2 font families max + mono, code ≤12 lines with Shiki dual theme, `prefers-reduced-motion` fallback, speaker notes on every substantive slide, zero placeholders. Enforced by `references/verify-checklist.md` (23 gates).

## New deck in 30 seconds

```bash
bash skills/slideshow/scripts/new-deck-scaffold.sh reveal my-talk
cd my-talk
python3 ../skills/slideshow/scripts/verify-images.py
python3 ../skills/slideshow/scripts/verify-deck.py slides.md
bash ../skills/slideshow/scripts/export-deck.sh reveal
```
