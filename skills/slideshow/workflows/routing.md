# Routing Workflow — Request Features → Mode + Engine + Style + Workflow

> Deterministic router. Answer from the tables, not from follow-up questions.
> Only ask the user when two rows tie after applying tie-breakers.

## Step 1 — Detect mode (first match wins, top to bottom)

| # | If the request contains | Mode | Example trigger |
|---|---|---|---|
| 1 | Live demo, runnable code, iframe, benchmark, API walkthrough | tech-talk (`references/modes/tech-talk.md`) | "live-code the export drill" |
| 2 | Ask with amount/date/approval, investor or exec audience | pitch (`references/modes/pitch.md`) | "seed pitch, $18k ask" |
| 3 | Numbered steps the audience types, install/configure/ship, exercise | tutorial (`references/modes/tutorial.md`) | "40-min lab, they build along" |
| 4 | Gallery, portfolio, redesigns, past talks, theme range | showcase (`references/modes/showcase.md`) | "show six shipped themes" |
| 5 | Keynote, opener/closer, vision, mixed non-technical crowd | narrative (`references/modes/narrative.md`) | "open the conference" |
| 6 | None of the above / "just make a deck" | tech-talk for engineers, narrative for mixed (see tie-breakers) | "defaults" → SKILL.md Phase 1 defaults |

Tie-breakers (apply in order): code + story → closing slide decides (diff =
tech-talk, quotable line = narrative). Ask + gallery → ask number present =
pitch. Steps + demo → audience types = tutorial, audience watches = tech-talk.

## Step 2 — Detect engine (first match wins)

| # | If the deck needs | Engine | Export path |
|---|---|---|---|
| 1 | Iframes, Auto-Animate morphs, per-fragment control, custom JS, parallax | reveal.js 6 | `index.html` serve + decktape PDF (`scripts/export-deck.sh reveal`) |
| 2 | Live code highlighting, Monaco runner, `v-click` pedagogy, Markdown + Vue | Slidev 52 | `npx slidev build --out dist/` + `slidev export --format pdf` |
| 3 | Fast text-heavy, clean static export, non-dev author, email-able single file | Marp CLI 4 | `npx marp slides.md -o deck.html --allow-local-files` + PDF/PPTX |
| 4 | Code walkthrough IS the talk | Slidev first; reveal.js if custom runner needed | Shiki `vitesse-light + vitesse-dark` |
| 5 | Must survive email / no-JS / offline projector | Marp + print-PDF fallback | Screenshots replace iframes |
| 6 | Mixed or unsure | reveal.js | Widest envelope; degrades gracefully |

Full matrix, pins, and migration notes: `references/engines.md`.
Starters: `examples/reveal-demo/`, `examples/slidev-demo/`, `examples/marp-demo/`.

## Step 3 — Detect visual style (authority: `references/modes/_index.md`)

Pick exactly one row from the dials-per-mode table there (palette default + font pair per routed mode); declare it in the Design Read. Mode default wins when no brand is given; max 2 families + mono for code.

Anti-slop lock (all rows): no `linear-gradient(135deg, #8B5CF6, #3B82F6)`;
max 1 gradient per deck as 4px bar or ≤8% glow; captions ≥14px;
body contrast ≥4.5:1 (≥7:1 projectors).

## Step 4 — Detect workflow file

| Condition | Workflow file |
|---|---|
| Full quality bar, client-facing, >15 min available | `workflows/generate-deck.md` (Default) |
| Lightning talk, internal sync, fix-forward, ≤15 min | `workflows/quick-generate.md` (fast path, Marp-first, bento-minimal) |
| Unsure | Default (`generate-deck.md`) |

## Step 5 — Emit the routing slip (paste this, filled)

```markdown
Mode: tech-talk (`references/modes/tech-talk.md`) — live export-drill demo
Engine: Slidev 52 (Monaco runner + v-click) — fallback reveal.js if custom runner needed
Style: Midnight SaaS dark + Space Grotesk/Inter/JetBrains Mono
Workflow: `workflows/generate-deck.md`
Outline gate: 10 one-liners before build (SKILL.md Phase 6.1)
Verify: `references/verify-checklist.md` + `scripts/verify-images.py` + `scripts/export-deck.sh slidev`
```
