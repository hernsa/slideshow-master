# Pitch Mode — Hook → Problem → Solution → Traction → Ask

> 8 slides. Goal: win a yes — funding, headcount, migration approval.
> Use when the last slide names an amount, a date, and a contact.

## Arc description

Hook in 10 seconds with a vivid loss, widen to a problem the decision-maker
already budgets for, then land the solution as the inevitable fix. Traction
is evidence, not adjectives: numbers, logos, shipped dates. The ask is one
slide with one number and one deadline — never three options. When not to
use: teaching a skill (use `tutorial.md`), proving craft range (use
`showcase.md`), rallying a crowd with story (use `narrative.md`).

Reference thread: "Why HTML beats PPTX for tech talks" reframed as a pitch —
"Fund the HTML talk kit so every team ships talks like software."

## Per-slide outline

### 1. Hook — "Demo Day Froze for 90 Seconds. 400 People Watched."
- Layout: full-bleed photo + 7-word headline + source line (`references/layouts.md` §7).
- Beats: the frozen PPTX dialog, the hallway re-export, the laugh that wasn't kind.
- Notes hint: `<!-- presenter: 10 seconds, no context. Let the photo land. -->`

### 2. Problem — "Every Tech Talk Ships as a Brittle File"
- Layout: split 50/50, left three pain bullets, right stacked screenshots (font swap, gray charts, missing video).
- Beats: version drift across laptops, no review diff, handout rots after the event.
- Notes hint: quantify — "14 re-exports last quarter across 6 teams" style, 2 sources required.

### 3. Solution — "Talks Are Runtimes: URL, PDF, Source"
- Layout: bento 3-cell (live URL / PDF handout / Markdown source), one icon per cell.
- Beats: one `slides.md` builds all three via `scripts/export-deck.sh slidev`.
- Notes hint: name the engine bias here — Slidev for dev teams, Marp for execs who forward PDFs.

### 4. How it works — "Write Markdown, Get a Stage and a Handout"
- Layout: code+preview, left 8-line `slides.md` fence, right rendered slide thumbnail.
- Beats: frontmatter `theme + transition`, `v-click` steps, `npx slidev build --out dist/`.
- Notes hint: keep code to 8 lines; this is a pitch, not a workshop.

### 5. Why now — "HTML Finally Prints Cleanly"
- Layout: stat row — Playwright PDF 11s, handout 41% smaller, zero installs for viewers.
- Beats: Chromium PDF fidelity crossed the bar in 2024; projectors still punish low contrast, so ≥7:1.
- Notes hint: each stat gets `<!-- sources: ... -->`; single-source stats marked `[unverified]`.

### 6. Traction — "6 Teams, 23 Talks, Zero Hallway Re-Exports"
- Layout: logo strip + two bars (before/after re-export count), captions ≥14px.
- Beats: pilot team names, dates, quote from one organizer, link to `examples/slidev-demo/`.
- Notes hint: no logo without written permission; gray-box any pending approvals.

### 7. Ask — "Approve $18k + 2 Weeks: Ship the Team Talk Kit"
- Layout: centered ask, one number, one date, one owner (`references/layouts.md` §1 variant).
- Beats: amount, what it buys (theme + scaffold via `scripts/new-deck-scaffold.sh` + training), decision date.
- Notes hint: say the number out loud; never let the ask live only in small print.

### 8. Contact — "URL, PDF, and My Calendar Link Stay Up"
- Layout: contact strip — name, email, QR to live deck, QR to PDF handout.
- Beats: leave this slide up during Q&A; it is the receipt for the ask.
- Notes hint: test both QR codes from the back row on venue Wi-Fi before doors open.

## Timing (12 minutes + Q&A)

Minutes 0–2: slides 1–2 (hook + problem, no interruptions). Minutes 2–6:
slides 3–5 (solution + why-now, the only numbers in the deck). Minutes 6–9:
slides 6–7 (traction, then the ask with a pause after the number). Minutes
9–12: slide 8 up, Q&A with the calendar QR visible. Rehearse the ask sentence
verbatim — "I am asking for $18k and two weeks to ship the team talk kit by
the 30th" — so it survives nerves.

## Appendix (not presented, shipped in PDF)

A. Cost breakdown: theme tokens, scaffold, two training sessions, Chromium
export lane. B. Risk note: PPTX holdouts get the Marp bridge from
`references/engines.md` § Migration. C. Source links: `slides.md`, live URL,
prior pilot decks with dates. Appendix pages carry `paginate: true` and print
cleanly via `npx marp slides.md -o deck.pdf --allow-local-files`.

## Visual system

- Palette: Paper Editorial light (paper `#FAF7F2`, ink `#1A1A1A`, accent persimmon `#C2410C`), from `references/colors.md`.
- Fonts: Fraunces display / Inter body; mono only on slide 4 (JetBrains Mono 16px).
- Images: one hero projector photo, three small pain screenshots, logo strip on slide 6 — all local in `assets/`, credited.
- Motion: fades only (`MOTION_INTENSITY 3`); investors forward PDFs where motion dies anyway. See `references/animations.md` §5 fallback.

## Mode-specific don'ts

1. Don't put the ask on two slides — one number, one date, one owner.
2. Don't use three equal feature cards — bento with one hero cell beats symmetry.
3. Don't exceed 25 words on slides 1–3 — if it needs a paragraph, it belongs in notes.
4. Don't show a logo wall without permission dates in `assets/CREDITS.md`.
5. Don't end with "Thank You" confetti — end with the contact strip and live QR codes.
6. Don't live-demo in a pitch unless the demo is under 60 seconds — link it, don't drive it.
