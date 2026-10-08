# Tech Talk Mode — Problem → Demo → Code → Takeaways

> 10 slides. Goal: persuade engineers with a live demo backed by code.
> Use when the audience can read a diff and will heckle a fake benchmark.

## Arc description

Open on a pain every engineer in the room has felt (a PPTX that broke on
stage Wi-Fi), name the thesis in one sentence, then prove it live. The demo
is the middle of the talk, not the appendix: one hero iframe or Monaco
runner around slide 4–6, flanked by a problem setup and a code teardown.
Close with numbers and three takeaways the audience can steal on Monday.
When not to use: investor pitches (use `pitch.md`), step-by-step labs
(use `tutorial.md`), pure story keynotes (use `narrative.md`).

Reference arc: "Why HTML beats PPTX for tech talks" — thesis: "A talk is a
runtime, not a file, so ship the runtime."

## Per-slide outline

### 1. Title — "Why HTML Beats PPTX for Tech Talks"
- Layout: title + subtitle + speaker strip (`references/layouts.md` §1).
- Beats: conference name, date, one-line thesis under the title. No agenda slide.
- Notes hint: `<!-- presenter: open with the number — 41% smaller handout, zero installs. Pause. -->`

### 2. Problem — "Last Month, My PPTX Died on Stage Wi-Fi"
- Layout: split 40/60, left text, right photo of a frozen projector dialog.
- Beats: embedded video that would not play, fonts swapped to Calibri, 3 linked charts went gray.
- Notes hint: ask for a show of hands — who has re-exported a deck in the hallway.

### 3. Stakes — "A Talk Is a Runtime, Not a File"
- Layout: stat row, three cards max (re-exports per quarter, minutes lost, handout bounce rate).
- Beats: static files rot; runtimes degrade gracefully. Set up the live demo promise.
- Notes hint: land the thesis sentence verbatim; it repeats on slide 10.

### 4. Demo setup — "Tonight: One URL, Zero Installs, Live Code"
- Layout: code+preview (`references/layouts.md` §6), left 12-line snippet, right live iframe.
- Beats: `npx serve dist/` URL on screen, QR code to the same URL, reduced-motion fallback noted.
- Notes hint: `<!-- sources: revealjs.com/auto-animate, marp CLI docs -->` per SKILL.md Phase 3.

### 5. Hero demo — "Watch Me Rebuild This Slide in the Browser"
- Layout: full-bleed iframe (reveal.js) or Slidev Monaco runner with `v-click` steps.
- Beats: change a token (accent `#F59E0B` → `#16A34A`), hot-reload, audience gasps. Keep to 3 clicks.
- Notes hint: pre-record a 20-second fallback video in `assets/demo-fallback.mp4` if Wi-Fi drops.

### 6. Code teardown — "12 Lines: Shiki, Fragments, Notes"
- Layout: code slide, JetBrains Mono 18px, `vitesse-light + vitesse-dark`, line numbers on.
- Beats: show the fence ` ```ts {1,3|5} ` highlight, fragment reveal order, `<aside class="notes">` wiring.
- Notes hint: never more than 12 lines; extra lines go to the handout appendix.

### 7. Benchmarks — "Export Drill: HTML vs PPTX, Timed"
- Layout: stat row + bar visual (Auto-Animate grow from 120px to 320px width bars).
- Beats: HTML→PDF 11s via Playwright, PPTX re-export 4 min + font repair, handout 41% smaller.
- Notes hint: every number needs 2 sources in notes; mark `[unverified]` if single-sourced.

### 8. Migration — "PPTX-First Teams: The 4-Step Bridge"
- Layout: numbered steps horizontal (Marp → Slidev → reveal.js path from `references/engines.md` § Migration).
- Beats: flatten morphs, screenshot iframes, freeze system fonts for PPTX, re-check code at 14px+.
- Notes hint: point to `examples/marp-demo/` as the starting scaffold for PPTX holdouts.

### 9. Pitfalls — "Three Ways This Breaks on Projectors"
- Layout: bento 3-cell (contrast, offline fonts, clicker double-advance).
- Beats: body contrast ≥7:1 for projectors, self-host fonts, disable touch advance.
- Notes hint: cite `references/verify-checklist.md` gates 2 and 4 explicitly.

### 10. Takeaways — "Ship the Runtime: URL, PDF, Source"
- Layout: section divider + three takeaway lines + contact strip.
- Beats: repeat thesis, ship live URL + PDF handout + Markdown source, invite questions with QR.
- Notes hint: end on the live URL slide; leave it up during Q&A, never a "Thanks!" wall.

## Visual system

- Palette: Midnight SaaS dark (bg `#0B1220`, surface `#111C33`, accent amber `#F59E0B`), from `references/colors.md` palette 1.
- Fonts: Space Grotesk headings / Inter body / JetBrains Mono code.
- Images: one frozen-projector photo (`assets/projector-fail.jpg`, credited in `assets/CREDITS.md`), one architecture diagram; rest is live DOM.
- Morph moment: exactly one — slide 7 bars grow via `data-auto-animate` (reveal.js) or `view-transition` (Slidev). See `references/animations.md` §2.

## Mode-specific don'ts

1. Don't open with an agenda slide — open with the projector-failure story.
2. Don't exceed 12 code lines on slide 6 — the overflow goes to handout notes.
3. Don't live-type more than 3 edits — every extra keystroke is dead air.
4. Don't show benchmark numbers without 2 sources in speaker notes.
5. Don't embed more than one iframe — two live frames fight for focus and break offline export.
6. Don't close with "Thank you / Questions?" as the only text — close with the URL + three takeaways.
