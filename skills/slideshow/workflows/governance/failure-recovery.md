# Failure Recovery — Failure Catalog

> Fix at the shallowest layer that owns the fault: slide → outline → style →
> tooling (SKILL.md discipline 7). Never silently downgrade a required artifact.
> Every recovery below ends at a named re-verify gate — recovery without
> re-verification is just a second failure with confidence.

## Owning layers

- slide: one file, one image, one snippet — fix and re-run the slide's gates.
- outline: structure, order, count — fix, get a fresh outline nod, rebuild affected slides.
- style: tokens, fonts, palettes, motion — fix, re-measure, rebuild affected slides.
- tooling: installs, versions, export binaries — fix the environment, re-export everything.

How to tell: change one file and the symptom moves → slide. Change one file
and nothing moves → the layer is deeper. Change a token and five slides shift →
style. Reinstall and the export works → tooling. Cut two slides and the talk
lands → outline was the fault all along.

## Triage before the catalog

1. Reproduce from the final commit: re-run the exact failing command or re-open the exact slide — never diagnose from memory of the failure.
2. Isolate to one layer: one broken image is slide; every image broken is tooling; washed text everywhere is style; a sagging middle is outline.
3. Check the delivery note for the routing slip, outline version, and last green gate — recovery starts from the last known good state.
4. Pick the catalog entry below by symptom, not by guess; run its numbered steps in order.
5. Timebox to 20 minutes per failure; at the cap, escalate one layer up instead of repeating step 4.

Log every recovery in the delivery note:

```text
Failure: contrast trio 4.2:1 on muted/surface (visual-review §4)
Layer: style — fix: .fix-muted, re-measured 15.8/6.1/4.9
Re-verify: Gate 5 green, 390px re-walk clean — resume export-verify.
```

If no entry matches, treat it as a style-layer defect first (most visual
surprises live there), then outline, then tooling — and write the new entry
into this catalog when it resolves.

## 1. Empty asset dir

Symptom: `scripts/verify-images.py` reports `missing file` for every image; the
served deck shows broken-image icons; `ls -lh assets/` holds only `README.txt`.
Owning layer: slide.

1. Confirm the deck dir: `scripts/new-deck-scaffold.sh <engine> <deck>` creates `<deck>/assets/` — work inside it, not a sibling folder.
2. Copy each referenced file into `assets/` and rename `src` to the local path (`assets/lab.jpg`, never `../photos/lab.jpg`).
3. Add the per-file license record `assets/<stem>.txt` (Source / License / Date) plus the `assets/CREDITS.md` entry (`stages/image-review.md` §4).
4. Re-run `python scripts/verify-images.py slides.md --assets-dir assets` to exit 0.
5. Re-verify: Gates 3 (local + sized + credited), 4 (alt text), and 16 (no 404s).

## 2. Broken CDN pin

Symptom: fonts swap to fallback serif on venue Wi-Fi; console shows `Reveal is not defined`
or a failed stylesheet fetch; the deck looked right on home broadband. Owning layer: tooling.

1. Pin per `references/engines.md` — never float `latest`: `reveal.js@^6.0.0`, `@slidev/cli@^52.0.0`, `@marp-team/marp-cli@^4.1.0` in `package.json`.
2. Vendor the runtime locally: `npm i reveal.js@^6.0.0` and reference `node_modules/reveal.js/dist/reveal.js` by relative path (see the hello-world in `engines.md`).
3. For fonts, keep the Google Fonts `<link>` but confirm a system fallback stack renders acceptably with Wi-Fi off.
4. Re-serve from the deck root and walk every slide with the network throttled to offline.
5. Re-verify: Gates 7 (font count), 14 (code highlights render), and 16 (zero console errors).

## 3. Contrast failure

Symptom: the trio reads `fg/bg 15.8:1, muted/bg 6.1:1, muted/surface 4.2:1` — the
third pair fails; body copy in teal measures 3.9:1; the projector wash makes it worse.
Owning layer: style.

1. Promote the failing muted without redesigning: `.fix-muted { color: var(--fg); opacity: .82; }`.
2. Re-measure all three pairs with the DevTools picker — fixing one pair often shifts another.
3. For projector decks hold body to ≥7:1; never ship gradient body text (Gate 9 bans it).
4. Re-check code blocks separately at ≥7:1 — Shiki theme pairs (`vitesse-light/dark`) must track the mode toggle.
5. Re-verify: Gate 5 (contrast trio recorded, all pass) plus a 390px re-walk for the changed slides.

## 4. Placeholder leak

Symptom: a grepped `TODO`, `lorem`, `coming soon`, `slide title here`, or an
`src="http…"` hotlink survives into the built deck. Owning layer: slide.

1. Run all four greps from the deck root and treat every hit as blocking:
```bash
grep -rni "todo\|placeholder\|coming soon\|fix me\|xxx" --include="*.md" --include="*.html" .
grep -rni "lorem" --include="*.md" --include="*.html" .
grep -rni "slide title here\|untitled\|test test" --include="*.md" --include="*.html" .
grep -rho "src=\"http[^\"]*\"" --include="*.html" --include="*.md" . | sort | uniq -c
```
2. Replace each hit with real content (Acme numbers, credited images) or delete the slide — never ship "TBD".
3. Replace hotlinked `src` with a vendored `assets/` file plus its license record.
4. Re-run all four greps to zero (the fourth keeps only intentional demo/iframe URLs documented in notes).
5. Re-verify: Gate 6 (placeholder scan) and Gate 16 (no 404s from the replaced sources).

## 5. Export tool missing

Symptom: Slidev PDF export hangs at Chromium; `slidev: command not found`; decktape
writes a correct page count of white pages; Marp reports no Chrome. Owning layer: tooling.

1. Missing CLI: `npm i -D @slidev/cli@^52.0.0`, then `npx slidev --version` must print 52.x.
2. Missing Chromium (Slidev and Marp PDF/PPTX both drive headless Chrome): `npx playwright install chromium`, then re-run the export with `--timeout 60000` if it still stalls.
3. Blank decktape PDF: the `?print-pdf` CSS never loaded — open `http://localhost:8000/?print-pdf` in a browser first, then `npx decktape reveal --load-pause 2000 "http://localhost:8000/?print-pdf" deck.pdf`.
4. Marp images missing from output: re-run raw with `--allow-local-files` (`stages/export-verify.md` §3).
5. Re-verify: Gate 15 (page count, no clipping, PPTX spot-check) and Gate 16 (clean console).

## 6. Oversized images

Symptom: a `lab-4MB.png` sits in `assets/`; transitions hitch; the PDF balloons;
`ls -lh assets/` shows files far past budget. Owning layer: slide.

1. List offenders: `ls -lh assets/` — anything over 400KB photos / 200KB backgrounds is one.
2. Re-export each at max 1920px wide (parallax 3000px wide allowed, still ≤400KB), lowering quality until it fits; keep labels at 14px+ on charts.
3. Update the `assets/CREDITS.md` entry with the new size (`320KB, 1920px`) so the record matches the file.
4. Re-run `python scripts/verify-images.py slides.md --assets-dir assets` and reload the deck to confirm no blur or layout shift (width/height or `aspect-ratio` still set).
5. Re-verify: Gate 3 (sizes in budget), Gate 4 (alt intact after re-export), and Gate 13 (mobile still clean).

## Escalation

Three failed recoveries on one failure means the layer is wrong: escalate one
layer up (slide → outline → style → tooling) and state the new hypothesis in the
delivery note. A red lite gate on the fast path that survives one recovery is an
upgrade trigger — switch to `workflows/generate-deck.md`, do not sprint around it.

Worked escalation: the muted trio fails twice after `.fix-muted` (style, 20 min
each). The third attempt escalates to outline — the deck carries muted statistics
on six consecutive slides, so the fault is density, not color. Two stat slides
merge into one bento, muted labels drop to captions only, trio re-measures
`15.8/6.1/5.2` green. The layer was wrong; the catalog steps were right.

## After every recovery

- [ ] Named re-verify gates recorded green with evidence in the delivery note.
- [ ] `assets/CREDITS.md` and license records match the files on disk.
- [ ] Outline version bumped when structure changed, with a fresh approval nod.

Handoff line: `Recovery done: <failure> fixed at <layer>, gates <n> green — resume <stage>.`
