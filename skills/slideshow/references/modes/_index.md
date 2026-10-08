# Modes Index — HTML Slideshow Deck Types

> All modes live in `references/modes/`. The router in `workflows/routing.md`
> selects one mode per deck. Never blend two arcs in one deck.

## Mode table

| Mode | File | Goal | Arc | Slides | Engine bias |
|---|---|---|---|---|---|
| Tech Talk | `references/modes/tech-talk.md` | Persuade engineers with a live demo | Problem → Demo → Code → Takeaways | 10 | Slidev first, reveal.js if custom runner or iframes needed |
| Pitch | `references/modes/pitch.md` | Win a yes: funding, approval, headcount | Hook → Problem → Solution → Traction → Ask | 8 | Marp for email-able static, reveal.js for live narrative |
| Tutorial | `references/modes/tutorial.md` | Teach a skill the audience can repeat hands-on | Goal → Steps → Pitfalls → Exercise | 8 | Slidev (Monaco + `v-click`), Marp for print handout |
| Showcase | `references/modes/showcase.md` | Prove range with visual evidence | Gallery / Portfolio sweep | 6 | reveal.js (morph + full-bleed), Marp for static portfolio PDF |
| Narrative | `references/modes/narrative.md` | Move a mixed audience with a story | Hero → Tension → Turn → Resolution | 8 | reveal.js (Auto-Animate + parallax), Marp fallback for offline |

## How to pick (in order)

1. **Is there a live demo or runnable code?** If yes → `tech-talk.md`.
   Example: "Why HTML beats PPTX for tech talks" with an embedded
   `index.html` that rebuilds live on stage is a tech talk, not a narrative.
2. **Is there an ask with a deadline?** Funding, hiring, migration approval,
   conference acceptance. If yes → `pitch.md`, even if the topic is technical.
3. **Must the audience reproduce steps tomorrow?** Install, configure, ship.
   If yes → `tutorial.md`. Tutorial decks ship a companion `handout.pdf`.
4. **Is the proof mostly screenshots and shipped work?** Redesigns, themes,
   past talks, template gallery. If yes → `showcase.md`.
5. **Otherwise → `narrative.md`.** Keynotes, openers, vision talks, anything
   where feeling carries further than a diff.

## Tie-breakers

- Code + story both present: pick by the closing slide. Ends with a diff or
  benchmark table → tech talk. Ends with a line the audience quotes → narrative.
- Pitch vs showcase: pitch ends with an ask slide (amount, date, contact).
  Showcase ends with a contact strip and three thumbnail links, no ask number.
- Tutorial vs tech talk: tutorial has numbered steps the audience types along
  with. Tech talk has one hero demo the speaker drives while the audience watches.
- Time-boxed to 5 minutes / lightning talk: prefer showcase (6 slides) or
  pitch (8 slides, drop slide 6 traction detail to notes).

## Design dials per mode

| Mode | DESIGN_VARIANCE | MOTION_INTENSITY | VISUAL_DENSITY | Palette default |
|---|---|---|---|---|
| tech-talk | 7 | 6 | 5 | Midnight SaaS dark + JetBrains Mono |
| pitch | 5 | 3 | 3 | Paper Editorial light + Fraunces/Inter |
| tutorial | 4 | 4 | 6 | Botanical Warm + Outfit/DM Sans |
| showcase | 8 | 5 | 2 | Midnight SaaS dark, one accent per project |
| narrative | 9 | 6 | 2 | Ink Keynote dark, warm amber accent |

Dials are set in the Phase 2 Design Read (see `SKILL.md` Phase 2) and drive
layout choices from `references/layouts.md` and motion from
`references/animations.md`.

## Engine bias, restated for the router

- Tech talk code walkthrough is the talk → Slidev first (`vitesse-light +
  vitesse-dark`, Monaco runner). Custom JS runner or multi-iframe →
  reveal.js. See `references/engines.md` § Slidev exports.
- Pitch emailed ahead → Marp single-file HTML + PDF. Pitched live on stage
  with morph transitions → reveal.js with `?print-pdf` fallback.
- Tutorial hands-on → Slidev dev (`npx slidev slides.md`) with `v-click`
  steps. Print handout → Marp PDF via `npx marp slides.md -o deck.pdf`.
- Showcase gallery → reveal.js Auto-Animate morphs between project states.
  Static portfolio leave-behind → Marp PNG per slide.
- Narrative keynote → reveal.js parallax + `data-auto-animate`. Offline
  projector with no network → Marp, screenshots instead of iframes.

## File contract (every mode file)

Each file in this directory follows the same contract:

1. Arc description (3–5 sentences, when to use / when not to use).
2. Per-slide outline: slide number + title + layout from
   `references/layouts.md` + 2–3 beat notes + speaker-notes hint.
3. Visual system: palette tokens from `references/colors.md`, font pair,
   image treatment, one morph moment.
4. Mode-specific don'ts (5 minimum, concrete, no generic advice).
5. Demo-universe titles: every outline uses real titles from the
   "Why HTML beats PPTX for tech talks" universe where fitting, so a new
   agent can see tone and specificity without guessing.

## Outline approval gate

Write the per-slide outline (title + point + visual, one line per slide)
before building any slides, per `SKILL.md` Phase 6 step 1. Paste the outline
into chat or the PR body, get a nod, then build. Outlines are cheap;
rebuilt decks are not.

## Verify pointer

All modes converge on `references/verify-checklist.md` gates and
`scripts/verify-images.py` before export via `scripts/export-deck.sh`.
Mode choice never skips verification.
