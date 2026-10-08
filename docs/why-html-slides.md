# Why HTML slides

> PPTX shares files. HTML ships talks: live code, version control,
> morph, and a deploy URL. Each claim below names the engine backing
> in this repo: reveal.js 6, Slidev 52, Marp CLI 4.

## 1. Live code beats screenshots

Claim: audiences trust code they watch run.
Backing: Slidev Monaco runnable plus `v-click` line staging, or
reveal.js iframe beside a 12-line block from `layout-templates/code-demo.md`.
Marp falls back to screenshots for export, which proves the rule: live
where the engine allows, frozen where it must print.
PPTX can only show a picture of code.

## 2. Version control beats track changes

Claim: talks are documents and deserve diffs.
Backing: Slidev and Marp author in `slides.md`, reveal.js builds from
Markdown source before HTML. Every edit in this repo diffs line by line:
`skills/slideshow/SKILL.md` phase 6 mandates Markdown-first for that
reason. Try diffing two `.pptx` binaries and the point lands.

## 3. Morph beats slide pushes

Claim: motion should explain, not decorate.
Backing: reveal.js `data-auto-animate` with matching `data-id`,
Slidev `view-transition` plus `v-motion`, Marp `transition` keywords
for simple cuts. `references/animations.md` caps morph at one moment
per section with a `prefers-reduced-motion` cut fallback. PPTX morph
exists but rarely survives venue machines or web sharing.

## 4. A URL beats an attachment

Claim: the best handout is a link that works on phones.
Backing: reveal.js serves `index.html` directly, Slidev builds a `dist/`
SPA with `slidev build`, Marp emits a single self-contained HTML file
via `marp -o deck.html`. All three pass the `390px` gate in
`references/verify-checklist.md`. No attachment size limits, no font
swaps, no macro warnings.

## 5. Export still covers handouts

Claim: HTML-first does not abandon PDF or PPTX.
Backing: Marp exports HTML, PDF, PPTX, PNG natively. Slidev exports PDF
and PNG via Playwright with experimental PPTX. reveal.js exports PDF via
decktape `?print-pdf`. `scripts/export-deck.sh` wraps each path per engine.
Write once, ship the URL plus the PDF plus the PPTX when organizers ask.

## 6. Review beats comment threads

Claim: talks improve when review is structured.
Backing: `references/verify-checklist.md` gives 16 gates with pass
numbers: contrast `4.5:1`, photos `400KB`, code `12` lines, gradients `1`,
notes `1:1`. `scripts/verify-images.py` plus grep checks run in CI.
PPTX review is "slide 12 looks off". HTML review is a checklist with
numbers and a ship record.

## 7. Offline still works

Claim: venues have terrible Wi-Fi and HTML handles it.
Backing: images live in `assets/`, fonts fall back to system stacks,
Marp single-file output runs with zero network. The skill bans hotlinks
for exactly this reason. A self-contained folder plus `npx serve` beats
a cloud deck that spins during your opener.

## When PPTX still wins

Email-only organizers, locked-down corporate laptops, and translation
vendors who live in PowerPoint. For those, author in Marp, export PPTX
natively, swap to system fonts, screenshot the iframes, and set motion
to cuts. The talk stays HTML-first; the deliverable meets the room.

Bottom line: author in Markdown and HTML, present from the browser,
export to whatever the organizers require. This repo exists to make
that loop five minutes long.
