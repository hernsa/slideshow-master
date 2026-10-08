# Tutorial Mode — Goal → Steps → Pitfalls → Exercise

> 8 slides. Goal: the audience can repeat the skill tomorrow without you.
> Use when success means typed-along steps and a finished exercise.

## Arc description

Promise one reproducible outcome on slide 1, then walk numbered steps the
audience types along with — each step shows command, expected output, and
the check that proves it worked. Pitfalls get their own slide so mistakes
feel normal, then a 5-minute exercise locks the skill. Ships with a print
handout (Marp PDF) because nobody remembers flags from stage. When not to
use: persuading skeptics with a hero demo (use `tech-talk.md`), winning
budget (use `pitch.md`).

Reference thread: "Why HTML beats PPTX for tech talks" as a lab — "Ship
your first HTML talk in 40 minutes: scaffold, theme, code, export."

## Per-slide outline

### 1. Goal — "Leave With a Talk That Builds to URL + PDF"
- Layout: title + outcome checklist (3 checks) + time box "40 min".
- Beats: "You will run `npx slidev slides.md`, theme it, and export PDF."
- Notes hint: `<!-- presenter: read the three checks aloud; audience nods = contract. -->`

### 2. Setup check — "Node 20, One Scaffold, Zero Surprises"
- Layout: code slide, 6-line terminal block (`node --version`, scaffold script).
- Beats: `scripts/new-deck-scaffold.sh slidev my-talk`, `npx slidev --version` → 52.x, open `localhost:3030`.
- Notes hint: 3-minute fix window; helpers walk the room while slide stays up.

### 3. Step 1 — "Scaffold: Slides.md in 60 Seconds"
- Layout: code+preview, left scaffold output tree, right first rendered slide.
- Beats: where `slides.md`, `assets/`, and `examples/slidev-demo/` live; what never to rename.
- Notes hint: call out the Markdown-first rule (`SKILL.md` Phase 6 step 2).

### 4. Step 2 — "Theme It: One Palette, Two Fonts, Mono for Code"
- Layout: split 40/60, left token block (bg/surface/accent), right before/after thumbs.
- Beats: pick ONE palette from `references/colors.md` (Botanical Warm), declare dark/light tokens, max 2 fonts.
- Notes hint: warn — never auto-invert; author both token sets explicitly.

### 5. Step 3 — "Code Slides That Survive the Back Row"
- Layout: code slide, 10-line ` ```ts {1,3|5} ` fence with Shiki dual theme.
- Beats: ≤12 lines, line numbers on, block bg = surface token, JetBrains Mono 18px.
- Notes hint: live-highlight lines 1 and 3, then 5 — the `{1,3|5}` click dance.

### 6. Pitfalls — "The 3 Errors Everyone Hits at 4pm"
- Layout: bento 3-cell — Chromium missing, images 404 in PDF, `v-click` lost in export.
- Beats: `npx playwright install chromium`; `--allow-local-files` for Marp; each `v-click` = extra PDF page.
- Notes hint: map each pitfall to `references/engines.md` § Troubleshooting with the exact fix command.

### 7. Exercise — "5 Minutes: Theme + Export Your Deck"
- Layout: exercise card — task, done-when checklist, stretch goal.
- Beats: swap accent token, rebuild (`npx slidev build --out dist/`), export PDF, open it.
- Notes hint: timer visible; play music; collect URLs in chat for show-and-tell.

### 8. Recap + handout — "Your Next Talk Ships as URL, PDF, Source"
- Layout: three takeaway lines + QR to handout PDF + QR to `examples/marp-demo/`.
- Beats: handout has all commands; source ships alongside the deck per `SKILL.md` Phase 7.
- Notes hint: leave exercise checklist up during Q&A; late finishers keep working.

## Timing (40-minute lab)

Minutes 0–5: slides 1–2 (goal + setup check, fix stragglers). Minutes 5–25:
slides 3–5 (one step per 6 minutes: demo 2, type-along 3, check 1). Minutes
25–30: slide 6 pitfalls — invite the room to hit errors early. Minutes 30–35:
slide 7 exercise with a visible timer. Minutes 35–40: slide 8 recap, handout
QR, hallway URLs. Never steal exercise minutes for extra lecturing.

## Handout spec (Marp PDF, 2 pages)

Page 1: all commands in order with expected outputs (`node --version` →
v20.x, `npx slidev --version` → 52.x, build + export lines). Page 2: the
three pitfalls with exact fixes from `references/engines.md` § Troubleshooting
plus the accent-token swap recipe. Build with
`npx marp slides.md -o handout.pdf --allow-local-files`; confirm code wraps
at 14px+ and paginates without orphans before printing.

## Visual system

- Palette: Botanical Warm (cream `#F7F3EA`, leaf `#2F6B4F`, clay `#C4622D`), from `references/colors.md`.
- Fonts: Outfit headings / DM Sans body / JetBrains Mono code at 16–20px.
- Images: before/after theme thumbs (local `assets/theme-before.png`), no stock needed; diagrams over photos.
- Motion: `v-click` stepwise reveals only (`MOTION_INTENSITY 4`); every animated deck carries a `prefers-reduced-motion` fallback per `references/animations.md`.

## Mode-specific don'ts

1. Don't put two new commands on one slide — one slide, one command, one check.
2. Don't skip expected output — every command shows what success looks like.
3. Don't exceed 12 code lines — overflow goes to the handout, not smaller font.
4. Don't hide pitfalls in an appendix — normalize them on slide 6 with fixes.
5. Don't end without a handout QR — memory fades, the PDF doesn't.
6. Don't use cloth-eared jargon — audience is students/mixed, so gloss every flag on first use.
