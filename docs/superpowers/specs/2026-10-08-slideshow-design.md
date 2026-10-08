# slideshow-master — Design Doc
Date: 2026-10-08 | Status: approved (Approach A — Hybrid Engine Router) | Author: ENI + LO

## 1. Goal
A universal agent skill repo (`slideshow-master`) that lets any coding harness
(Claude Code / Codex / opencode) produce modern, non-slop HTML slideshows via an
organized, detailed workflow: ask user → clarify colors → research → find images → verify.

Success = agent opens SKILL.md, follows 7 phases, routes to the right engine,
applies anti-slop design tokens, and ships a verified deck (HTML + PDF/PPTX export).

## 2. Key decisions (locked)
- **Approach A — Hybrid Engine Router.** One skill, three engine backends, explicit routing rules. No single-engine lock-in.
- **Format:** universal. SKILL.md + `references/` + `scripts/` + `examples/` readable by all harnesses (Claude `.claude/skills/`, opencode `.opencode/skills/` + `.agents/skills/` compat paths documented in README).
- **Images:** hybrid + verify. AI-gen OR stock OR local, but every image passes existence/dimensions/license check in Verify phase.
- **Code examples mandatory.** Every deck type includes at least one code-slide pattern (Shiki preferred, highlight.js fallback).
- **Anti-slop lock:** design-taste-frontend rules embedded — Design Read line, dials, no purple-blue default gradients, 60-30-10, 2-font max.

## 3. Repo layout
```
slideshow-master/
├── README.md                        # install for Claude Code / Codex / opencode, router table
├── skills/slideshow/SKILL.md        # THE skill (frontmatter name+description, 7-phase workflow)
├── skills/slideshow/references/
│   ├── animations.md                # §5 condensed
│   ├── colors.md                    # §6 condensed (6 palettes + tokens)
│   ├── layouts.md                   # §7 condensed (6 box patterns)
│   ├── engines.md                   # reveal vs Slidev vs Marp matrix + routing
│   └── verify-checklist.md          # export + a11y + perf gates
├── skills/slideshow/scripts/
│   ├── verify-images.(py|ts)        # existence, size, license log
│   ├── export-deck.(sh|py)          # PDF/PPTX/SPA per engine
│   └── new-deck-scaffold.(sh|py)    # scaffold router
├── skills/slideshow/examples/
│   ├── reveal-demo/ (code + fragments + auto-animate)
│   ├── slidev-demo/ (Markdown + v-click + Shiki)
│   └── marp-demo/ (Markdown + directives + transition)
└── docs/superpowers/specs/2026-10-08-slideshow-design.md (this file)
```

## 4. The 7-phase workflow (SKILL.md backbone)
1. **Intake** — topic, audience, length, code-heavy? presenter notes? export target?
2. **Design Read** (mandatory 1 line) — "Reading this as: <kind> for <audience>, <vibe>, leaning toward <engine+palette>." + dials VARIANCE/MOTION/DENSITY.
3. **Research** — topic facts, 2+ sources per claim, code API versions verified.
4. **Images** — hybrid source, log license, local `assets/` copy, verify dimensions.
5. **Route engine** — code-heavy/interactive → reveal.js (or Slidev if Markdown-first team); fast text/export-clean → Marp; Vue/React team → Slidev/Spectacle note.
6. **Build** — Markdown source first, theme tokens, fragments, notes, code blocks ≤12 lines.
7. **Verify + Export** — checklist gate (contrast ≥4.5:1, reduced-motion fallback, mobile swipe, PDF/PPTX renders, no broken assets).

## 5. Animations / transitions (deep-research synthesis)
- **Morph = continuity primitive.** Same element across states: reveal `data-id="hero"`, View Transitions `view-transition-name: hero`, GSAP `data-flip-id="hero"`. Unique names only.
- **reveal.js Auto-Animate** — adjacent `<section data-auto-animate>`; engine FLIP-diffs matched nodes (transform-only = 60fps; avoid animating font-size).
- **FLIP (all morph under the hood)** — First(rect) → Last(rect) → Invert(transform) → Play(animate to none). Raw fallback: `el.animate([{transform:'translate(dx,dy)'},{transform:'none'}],{duration:400})`.
- **GSAP Flip plugin** — `Flip.getState('.card')` → mutate → `Flip.from(state,{duration:.6,ease:'power2.inOut',absolute:true})`. Stagger ≤0.05–0.1s.
- **View Transitions API (Baseline 2025)** — `document.startViewTransition(()=>showSlide(next))`; root crossfade default; named elements get custom paths; always instant-switch fallback + `prefers-reduced-motion` gate.
- **Marp** — 33 built-ins, Bespoke template only: frontmatter `transition: fade 0.5s`, per-slide `<!-- _transition: cover-left -->`. CSS-only, zero JS, best static export.
- **Slidev** — frontmatter `transition: slide-left|fade|view-transition`; steps `<div v-click>`; motion `<div v-motion :initial="{x:-80,opacity:0}" :enter="{x:0,opacity:1}">`; draggable `v-drag`.
- **reveal slide/bg transitions** — global `Reveal.initialize({transition:'convex',backgroundTransition:'slide'})`, per-slide `<section data-transition="zoom">`. Cheapest = `fade`.
- **Fragments (reveal canonical)** — `.fragment` + variants (`fade-up/highlight-red/grow/...`), `data-fragment-index` ordering, `fragmentshown/hidden` events. Slidev equiv = `v-click`; Marp = none.
- **Parallax** — reveal legacy bg-translate for click decks; CSS `animation-timeline: scroll()/view()` transformed layers for scrollytelling. Never full-bg `background-attachment:fixed` on mobile.

## 6. Color + typography systems
Rules: WCAG normal ≥4.5:1 (aim 7:1 body), large ≥3:1; no pure #000+#FFF; 1 primary + 1 restrained accent; 60-30-10; max 1 gradient/deck (subtle radial ≤8% or 4px accent bar); never gradient body text; Shiki dual themes; 2 fonts max + mono exception.
```css
:root{ --bg:#FFFFFF; --surface:#F1F5F9; --fg:#0F172A; --muted:#64748B;
 --border:#E2E8F0; --primary:#2563EB; --accent:#7C3AED; }
.dark{ --bg:#0B1020; --surface:#1A2238; --fg:#E8EEF9; --muted:#8A93A6;
 --border:#2A3348; --primary:#4F7DF3; --accent:#9B6BFF; }
```
Six palettes: **Midnight SaaS** (#0B1020/#E8EEF9, devtools); **GitHub Tech** (#0D1117/#161B22, corporate trust); **Paper Editorial** (#FAF9F6/#1A1A18 + burnt orange, keynote); **Teal Serenity** (pitch light/dark); **Bento Minimal** (diagram-heavy); **Botanical Warm** (human/edu). Pairs: Space Grotesk+Inter+JetBrains Mono (tech), Sora+Inter, Fraunces/DM Serif+Inter (editorial), Outfit+DM Sans (friendly). Scale H1 clamp(40px,4.5vw,56px), body clamp(18px,2vw,24px), mono 16–20px/1.6.
Engine tokens: reveal `--r-background-color: var(--bg)` etc.; Slidev UnoCSS + Shiki `vitesse-light/dark` (Slidev ≥v0.50 Shiki-only); Marp `/* @theme */` + required `--bg --fg --muted --rule --accent` tokens.

## 7. Layout / box patterns (8pt scale: 8/16/24/32/48/64)
Global: grid/flex only, radius 12–24px, image border+shadow+16/9 cover, code ≤12 lines.
1. **Bento** — overview/architecture, 4–6 cards uneven weight (hero spans 2×2); Marp max 2×2.
2. **Split 50/50·40/60·header+2col** — text vs visual; reveal `r-hstack`, Slidev `two-cols`, Marp `![bg left:40%]`.
3. **Callout** — max 1/slide, one line + action (info #f0f9ff/#0ea5e9, success, warning, danger variants).
4. **Stat cards** — 3–4 KPIs (label caps, 800-weight number, delta); Slidev `layout: fact`.
5. **Quote** — 1 quote + avatar/role; left 4px rule.
6. **Code+preview** — 1.1fr/0.9fr grid, dark `pre` + light preview mock; reveal `data-trim+line-numbers`, Slidev Monaco runner.
When-vs-avoid: bento≠narrative flow; split≠2 dense lists; callout≠body copy; stats≠>4; quote≠evidence; code≠>20-line tutorial.

## 8. Engine matrix + routing
| Need | Route |
|---|---|
| Interactive demos, iframes, per-element morph, custom CSS control | reveal.js |
| Markdown-first, HMR, live code, Vue team | Slidev |
| Fast text-heavy, clean PDF/PPTX export, zero friction | Marp |
| React-native deck inside app | Spectacle note (appendix) |
Default: code/interactive → reveal; Markdown velocity → Slidev; export-clean → Marp. Hybrid allowed (e.g., Marp export + reveal interactive appendix) but one primary per deck.

## 9. Verify gates (must all pass)
Contrast check, `prefers-reduced-motion` fallback, keyboard/space + mobile swipe, ESC overview, speaker notes present, images exist + licensed + `alt`, code runs/highlights, PDF + PPTX/SPA export renders, no console errors.

## 10. Self-review
- [x] No placeholders — all tokens/palettes concrete hex.
- [x] No contradictions — Marp Bespoke-only motion, Slidev Shiki-only noted.
- [x] Scope bounded — skill + 3 engine demos, no app code.
- [x] User review requested before writing-plans.
