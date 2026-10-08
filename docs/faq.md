# FAQ

> Real answers for the decks in this repo: reveal.js 6, Slidev 52,
> Marp CLI 4, starters in `skills/slideshow/examples/`, scripts in
> `skills/slideshow/scripts/`, gates in `references/verify-checklist.md`.

## 1. Which engine should I pick?

Use the router: interactive or morph or iframes goes to reveal.js,
Markdown-first or live code goes to Slidev, fast text or clean export
goes to Marp. Mixed or unsure defaults to reveal.js. The full matrix
is `skills/slideshow/references/engines.md`.

## 2. Can I mix engines in one deck?

No. Pick exactly one engine per deck. Mixing runtimes breaks export,
breaks themes, and doubles test time. Migrate with the notes in
`engines.md` instead of mixing.

## 3. Where do images live?

Every image is copied into the deck `assets/` dir and logged in
`assets/CREDITS.md` with filename plus source plus credit. Never hotlink.
Run `python3 ../skills/slideshow/scripts/verify-images.py` to check.

## 4. What size should photos be?

Photos `<=400KB`, backgrounds `<=200KB`, max width `1920px`.
Full-bleed needs `>=1600px` wide. Parallax allows `3000px` wide but
still `<=400KB`. Compress before committing.

## 5. How do I credit images?

One line per image in `assets/CREDITS.md`, plus a `14px` caption under
the figure. Example: `lab.jpg | Maria Santos, Acme lab | internal use`.
Stock needs photographer plus service. AI output is labeled as such.

## 6. Do all images need alt text?

Yes. Every `<img>` carries `alt`. Informative alts state the takeaway:
`alt="Weekly p95 falling from 412 to 243 milliseconds"`. Decorative
images use empty `alt=""` so readers skip them.

## 7. Which fonts can I use offline?

Ship system stacks for offline rooms: `Segoe UI`, `Calibri`, `Arial`,
plus one mono like `JetBrains Mono`. Webfonts need preloading and a
local fallback. PPTX deliverables must use system fonts or the export
swaps them silently.

## 8. How do I export PDF from each engine?

Marp: `npx marp slides.md -o deck.pdf --allow-local-files`. Slidev:
`npx slidev export --format pdf slides.md`. reveal.js: serve first,
then `npx decktape reveal "http://localhost:8000/?print-pdf" deck.pdf`.
All three need headless Chromium for PDF.

## 9. Why is my reveal.js PDF blank?

The `?print-pdf` CSS did not load before capture. Open the URL in a
browser first, wait for render, then rerun with `--load-pause 2000`.
Serve from the deck root so asset paths resolve.

## 10. Why do Slidev clicks add PDF pages?

Each `v-click` is a step, and steps export as pages. Three clicks mean
three pages. That is expected. Remove `v-drag` before export and confirm
the page count matches steps plus base slides.

## 11. The projector washes out my text. What now?

Measure three pairs: `fg/bg`, `muted/bg`, `muted/surface`. Body needs
`>=4.5:1`, projector decks aim `>=7:1`. Promote failing muted text with
`.fix-muted { color: var(--fg); opacity: .82; }`. Test on the brightest
room setting, not your laptop.

## 12. How do I handle reduced motion?

Add the fallback CSS from `references/animations.md`, disable
Auto-Animate under the media query, and emulate `prefers-reduced-motion`
in DevTools. All fragments must be visible without clicks in that mode.
No flashing over `3Hz` anywhere.

## 13. How many code lines per slide?

Twelve max, `15px` mono minimum, Shiki dual theme. Cut the rest and link
the repo in notes. Slidev highlights with `{1,3}` ranges. Marp needs
plain fences. PPTX rasterizes code, so verify at `14px` plus.

## 14. Can I use iframes for live demos?

Yes in reveal.js and Slidev with a `title` attribute. No for Marp
export and PPTX delivery: screenshot the demo to `assets/demo-shot.png`
at `16/9` and link the URL. Venue Wi-Fi fails exactly when demos matter.

## 15. How many gradients are allowed?

One per deck, as a `4px` accent bar or `<=8%` radial glow. Never on text.
Count with `grep -rni "gradient" --include="*.css" .`. Delete the rest.

## 16. Speaker notes: what goes in them?

One sentence to say, the transition line to the next slide, plus stat
provenance and demo URLs. reveal.js uses `<aside class="notes">`.
Slidev and Marp use `<!-- -->` comments. Appendix slides may skip notes
only when marked `NO-NOTES`.

## 17. Mobile layout breaks at 390px. Fix?

Collapse every grid to one column under `800px` and single column under
`520px`. Code scrolls internally. Tap targets stay `>=44px`. Zero
horizontal scroll. The snippet lives in each `layout-templates/` file.

## 18. Where do I log engine choice?

Paste the decision log from `engines.md` into the PR: engine, why not
the other two, export path, fallback. Example: `Engine: reveal.js 6,
morph plus iframe essential, Marp cannot do either live`.
