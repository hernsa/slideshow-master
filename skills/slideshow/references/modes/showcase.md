# Showcase Mode — Gallery / Portfolio Sweep

> 6 slides. Goal: prove range with visual evidence, fast.
> Use when the work speaks louder than any argument — themes, redesigns, past talks.

## Arc description

A gallery, not an essay. One frame slide sets taste, then four project
spreads show before/after or stage/handout pairs, then a contact strip
closes. No live demo, no typed steps — screenshots carry the proof so the
deck survives email, offline projectors, and silent scrolling. When not to
use: teaching (use `tutorial.md`), asking for money (use `pitch.md`),
proving one thesis live (use `tech-talk.md`).

Reference thread: "Why HTML beats PPTX for tech talks" as a gallery —
six shipped talk themes, each with stage shot + handout + stack note.

## Per-slide outline

### 1. Frame — "Six Talk Themes That Ship as URL + PDF"
- Layout: title + bento preview grid of 4 thumbs (2 large, 2 small), captions ≥14px.
- Beats: taste statement in one line ("dark-tech, amber accent, mono for code"), client mix, year range.
- Notes hint: `<!-- presenter: 20 seconds. Name the through-line, then stop talking over the work. -->`

### 2. Project A — "Midnight SaaS: The PPTX Rescue Talk"
- Layout: split 50/50 — left before (gray PPTX export), right after (amber-on-ink reveal.js stage).
- Beats: stack note — reveal.js 6 + Auto-Animate bars; export via decktape `?print-pdf`.
- Notes hint: credit photographer + talk venue in `assets/CREDITS.md`; no hotlinked stage photos.

### 3. Project B — "Paper Editorial: The Board-Forward Deck"
- Layout: full-bleed handout spread + small stage inset (10% corner).
- Beats: Marp single-file HTML → PDF; system-font freeze for PPTX delivery; paginate styling.
- Notes hint: point out the 4px accent bar — the only gradient-free flourish allowed.

### 4. Project C — "Botanical Warm: The Workshop Handout"
- Layout: split 40/60 — left exercise checklist, right Slidev `v-click` step capture.
- Beats: Slidev 52 + Shiki dual theme; each `v-click` exports as its own PDF page (expected).
- Notes hint: mention `examples/slidev-demo/` as the reusable scaffold for this look.

### 5. Project D — "Ink Keynote: The 400-Seat Opener"
- Layout: full-bleed stage photo with ≥40% scrim + 7-word overlay line.
- Beats: parallax hero, one morph moment (title → pipeline bar), reduced-motion cut verified.
- Notes hint: dimensions ≥1600px wide per `scripts/verify-images.py`; `object-fit: cover`, radius 16–24px.

### 6. Contact — "Steal Any Theme: Source + Live URLs"
- Layout: contact strip + three thumbnail links (live URL, PDF, `slides.md` source).
- Beats: name, email, three QRs max; no ask number — this is proof, not a pitch.
- Notes hint: leave up during hallway chat; thumbnails must open with zero console errors.

## Asset spec (all local, all credited)

Each project ships two files: a stage capture (`assets/showcase-a-stage.png`)
and a handout crop (`assets/showcase-a-handout.png`), both 16/9, full-bleed
≥1600px wide. Log filename + source + license in `assets/CREDITS.md` per
`SKILL.md` Phase 4; run `scripts/verify-images.py` before layout. Captions
name the engine and version (reveal.js 6, Slidev 52, Marp CLI 4) so the next
agent can rebuild the look from `examples/` starters without guessing.

## Timing (10 minutes, silent-scroll safe)

Minutes 0–1: slide 1 frame, one taste sentence. Minutes 1–7: slides 2–5 at
90 seconds each — 30 seconds of talk, 60 seconds of looking. Minutes 7–10:
slide 6 contact strip with live URLs the room can open now. The deck must
also read cleanly with no presenter: captions carry stack + outcome on every
project slide so the forwarded PDF still persuades.

## Visual system

- Palette: Midnight SaaS dark base, one accent per project (amber, persimmon, leaf, sky) — never two accents on one slide.
- Fonts: Space Grotesk display / Inter body; project slides inherit the project's own fonts in screenshots only.
- Images: all local in `assets/showcase-*.png|jpg`, ≥1600px for full-bleed, 16/9, credited per `SKILL.md` Phase 4.
- Motion: single morph between slides 2→3 (Auto-Animate or `view-transition-name`); static cuts elsewhere. See `references/animations.md` §2.

## Mode-specific don'ts

1. Don't write paragraphs about process — let before/after pairs do the arguing.
2. Don't show more than 4 projects — depth beats catalog; extra work goes to an appendix link.
3. Don't mix two accent colors on one slide — one project, one accent.
4. Don't hotlink portfolio images — copy to `assets/`, log license, verify dimensions.
5. Don't use live iframes for portfolio pieces — screenshots only, so Marp PDF/PNG export stays clean.
6. Don't close with pricing or an ask — showcase ends with source links, pitch ends with a number.
