# slideshow-master

Universal agent skill for building modern HTML slideshows — conference-grade
decks with real themes, motion, and verification, not AI-slop defaults.

**How it works:** a Hybrid Engine Router. The agent runs a 7-phase workflow
(Intake → Design Read → Research → Images → Route → Build → Verify+Export)
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
│   ├── visual-styles/          # 10 styles (midnight-saas … glassmorphism) + picker
│   ├── layout-templates/       # 12 slide types (comparison … two-column) + picker
│   ├── engines.md              # reveal.js vs Slidev vs Marp matrix + version pins
│   ├── animations.md           # Auto-Animate, morph, FLIP, View Transitions, fragments
│   ├── colors.md               # 6 palettes, dark/light tokens, fonts, code themes
│   ├── layouts.md              # bento, split, callout, stat, quote, code+preview, images
│   └── verify-checklist.md     # 16 gates: images, contrast, placeholders, motion, notes, export
├── scripts/
│   ├── new-deck-scaffold.sh    # scaffold a new deck from a starter
│   ├── verify-images.py        # check assets are local, sized, credited
│   └── export-deck.sh          # build HTML / PDF / PPTX per engine
└── examples/
    ├── reveal-demo/            # full reveal.js starter deck (10 slides)
    ├── slidev-demo/            # full Slidev starter deck (10 slides)
    └── marp-demo/              # full Marp starter deck (10 slides)
```

Repo-level: `docs/` (getting-started, faq, why-html-slides),
`CONTRIBUTING.md` (add a style / palette / template / mode).

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
2. **Plan** — intake, one-line Design Read, outline (nod before slides)
3. **Do** — Markdown source → theme → layout templates → motion → code → notes
4. **Check·Act** — 16 verify gates, repair at the owning layer
5. **Export** — HTML / PDF / PPTX; ship Markdown source alongside

Details: `skills/slideshow/SKILL.md` + `skills/slideshow/workflows/`.

## Anti-slop contract

Every deck the skill produces must pass: explicit dark/light tokens (never
auto-invert), body contrast ≥4.5:1, max 1 gradient per deck (accent bar or
≤8% glow only — never the purple-blue default), 2 font families max + mono,
code ≤12 lines with Shiki dual theme, `prefers-reduced-motion` fallback,
speaker notes on every substantive slide, zero placeholders. Enforced by
`references/verify-checklist.md`.

## New deck in 30 seconds

```bash
bash skills/slideshow/scripts/new-deck-scaffold.sh reveal my-talk
cd my-talk
python3 ../skills/slideshow/scripts/verify-images.py
bash ../skills/slideshow/scripts/export-deck.sh reveal
```
