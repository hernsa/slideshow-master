# Color Usage — Deploying Color Across a Deck

> Companion to `references/colors.md`. Tokens live there; this file tells you where each
> token goes slide by slide so the deck never reads as a white wall.
> Components reference variables, never raw hex. If a hex appears outside
> `:root` / `@theme`, it is a bug.

Demo universe for every example below: Acme Shield Q3 readout. Speaker Ada,
data owner Jonas, lab photo by Maria Santos. Headline stat: p95 latency fell
41% (412ms to 243ms over six weeks, edge logs Jun 14 to Sep 2, confirmed
against billing export). Second stat: NRR 128%. All slides below use these
real beats — never placeholder text.

Related: palettes + tokens + contrast pairs in `references/colors.md`; ship gates in
`references/verify-checklist.md` (Gates 4, 6, 13); layout sketches in `references/layouts.md`;
slide-type sketches in `references/layout-templates/`.

---

## 1. The anti-white-wall rule (REQUIRED — ship-blocker)

**Max 2 consecutive slides on the base `bg`. Every 3rd slide must change
surface. Longest identical-`bg` run ≤2 — a run of 3+ identical fills FAILs
review and blocks shipping.** A "surface change" is one of: tinted section divider, image bleed,
accent band, dark quote slide, dark code slide, stat-bento band, CTA wash.
Stock-theme default (Slidev `theme: default` with no applied style) does NOT satisfy rotation — a visual style MUST be applied (pick ONE palette from `references/colors.md` + its token snippet from `references/visual-styles/*.md`) even if the outline `bg:` tags look varied on paper.

Why 2 and not 3: audiences forgive two calm slides in a row (problem, then
evidence). The third identical slide stops reading as "calm" and starts
reading as "unfinished template." The rotation below is the fix — plan it in
the outline, not during polish.

```text
Slide n    base bg (var(--bg))      e.g. Acme stall: p95 stuck at 412ms
Slide n+1  base bg (var(--bg))      e.g. support tickets quoting slow deploys
Slide n+2  SURFACE CHANGE (pick 1)  e.g. tinted divider "The fix" / photo bleed
                                      / dark quote / code block / accent band
Slide n+3  base bg resumes          e.g. Shield rollout timeline
```

MANDATORY: track the rotation in the outline itself with a `bg:` tag on every outline line (no exceptions — missing `bg:` FAILs review). Verify longest identical-`bg` run ≤2 before building visuals:

```markdown
Outline v3 — APPROVED 2026-10-01 (Jonas)
1. stall — p95 stuck at 412ms (bg: base)
2. stall — three enterprise tickets (bg: base)
3. DIVIDER — "The fix" tinted surface (bg: SURFACE CHANGE)
4. fix — Shield rollout, 3 regions (bg: base)
5. fix — stale-while-revalidate snippet (bg: dark code)
6. proof — p95 412 to 243ms chart (bg: base)
7. proof — NRR 128% bento (bg: bento band)
8. QUOTE — dark quote, customer CTO (bg: SURFACE CHANGE)
9. ask — CTA wash (bg: accent-tinted)
```

If the outline shows `base, base, base` anywhere in a row, insert a divider,
pull a photo full-bleed, or convert the third slide to a quote or code slide
before building visuals. Cheap to change in outline, expensive to redo later.

Exceptions (only these two): a 2-slide photo sequence counts as one surface
change stretched over two slides; a live-demo run of up to 4 slides may stay
on dark so the terminal does not flash-bang the room — note it in speaker
notes and return to rotation immediately after.

---

## 2. Per-slide-type background assignments

One background per slide type. Do not improvise per slide — assign once per
deck, then repeat. Component CSS (`.rule` / `.kicker` / `.band`) lives once in §4 — use those classes here, no local copies.

| Slide type | Light decks (base `bg`) | Dark decks (base `bg`) | Notes |
|---|---|---|---|
| Hero / title | Brand surface + glow ≤ 8% | Brand surface + glow ≤ 8% | The one allowed gradient lives here, or nowhere |
| Section divider | Solid `primary` or dark wash, inverted text | Solid `primary` or deeper `bg`, inverted text | Always tinted — never base `bg` with a bigger heading |
| Quote | Dark surface (`code-bg` or palette dark `bg`) | Deeper card + accent rule | Dark quote slides are the easiest rotation lever |
| Code | Always dark block (`code-bg #0D1117`) even in light decks | Dark block, same value | Screenshots match; Shiki theme follows the block, not the page |
| Stat / bento | `surface` band behind white cards | `surface` band behind dark cards | Cards carry 1px `var(--border)` so they survive projectors |
| Image bleed | Full-bleed photo + scrim, caption overlaid | Same, heavier scrim | Caption + credit always; scrim guarantees 4.5:1; ≤12 words on the photo, body lives off-bleed |
| Comparison | `surface` panel vs `card` panel | Same split | Loser side muted, winner side `primary` border |
| CTA / closing | Accent-tinted wash (`surface` + `primary` band) | Gradient CTA or solid `primary` | Buttons `primary`, one highlight number in `accent` |

Sketches: hero uses `.hero-midnight` from `references/colors.md`; divider is `.divider` + `.kicker` + `.rule` (§4); quote is `.quote-dark` + `.rule` (§4); code is base `bg` + dark `pre` (`code-bg #0D1117`, radius 16px); CTA is `surface` + `.band-top` in `primary` (§4). Full markup for each lives in §4 — do not restate it here.

---

## 3. Worked full-deck color scripts (1 full + 3 deltas)

Full script is a 10-slide Acme Shield Q3 readout: stall (2), fix (4),
proof (3), ask (1). `bg:` names the page fill; components inside still use
`card` / `surface` / `code-bg` per section 2. Token values are copied exactly
from `references/colors.md` — variables in code, hex here as spec.

### 3A. Midnight SaaS (dark-first devtools) — FULL SCRIPT

| # | Beat | `bg:` surface | What the audience sees |
|---|---|---|---|
| 1 | Hero | `bg #0B1020` + hero glow (allowed gradient) | "p95 fell 41%" over radial glows, mono kicker `ACME SHIELD · Q3` |
| 2 | Stall | base `bg #0B1020` | p95 stuck at 412ms, three flat weeks, terminal screenshot |
| 3 | Stall | photo bleed, lab photo | Maria Santos lab photo full-bleed, scrim, caption + credit — SURFACE CHANGE |
| 4 | Divider | solid `primary #4F7DF3`, white text | "The fix" — one line, inverted — SURFACE CHANGE |
| 5 | Fix | base `bg #0B1020` | Shield rollout map: iad → fra → hnd, dates, owner Jonas |
| 6 | Fix | dark code `#0D1117` block on `bg` | `shield.enable({ staleWhileRevalidate: 90 })`, 9 lines max |
| 7 | Proof | base `bg #0B1020` | p95 412 → 243ms line chart, teal-to-blue single-series wash |
| 8 | Proof | `surface #1A2238` bento band | NRR 128%, churn −2pp, expansion +31%: three stat cards on band |
| 9 | Quote | dark `#0D1117` quote slide | Lena Moreau CTO quote, accent `#9B6BFF` rule — SURFACE CHANGE |
| 10 | Ask | `surface #1A2238` + `primary` band | "Roll out by Oct 31" + Approve button `#4F7DF3` |

Rotation check: longest base run is slides 5–7 broken by code block (6) and
bento band (8) — never 3 identical in a row. Glow appears once (slide 1).

### 3B. Paper Editorial — ROTATION DELTA

Same 10 beats; swap fills: hero on `bg #FAF9F6` with 64px margins, slide 3 pull-quote on `surface #EFEDE6`, slide 4 ochre divider `primary #B45309`, slide 9 dark evening `#1A1A18`. Code stays neutral-white so syntax hues survive.

### 3C. Teal Serenity — ROTATION DELTA

Same 10 beats; swap fills: slide 3 mint band `surface #F0FDFA`, slide 4 photo bleed with scrim, slide 6 dark demo `#0B1F1E`, slide 10 teal CTA wash. Amber appears once (slide 8, NRR 128%) — anywhere else it gets cut.

### 3D. Botanical Warm — ROTATION DELTA

Same 10 beats; swap fills: slide 1 sunrise wash, slides 3/8 kraft panels `surface #F5F0E6`, slide 4 green divider `primary #15803D`, slide 9 dark story `#1C1917`. One `Caveat` annotation per deck maximum.

---

## 4. Accent-band / kicker / rule component spec

Three tiny components carry the whole rotation system. Build them once,
reuse on every slide. One accent per slide — pick `primary` or `accent`,
never both at full saturation. Spacing scale `8/16/24/32/48/64` and radius `16px` come from `references/layouts.md`.

### 4px bar, 48px wide (the rule)

```html
<span class="rule" aria-hidden="true"></span>
```

```css
.rule {
  display: block;
  width: 48px;
  height: 4px;
  border-radius: 2px;
  background: var(--accent);
}
.rule--primary { background: var(--primary); }
.rule--on-dark { background: var(--accent); opacity: .95; }
```

Rules: 48px wide, 4px tall, 2px radius, sits 16px above the heading. Never
center a rule under centered text wider than 640px — it floats. Never stack
two rules (accent + primary) on one slide; that is two accents.

### Kicker labels

```html
<p class="kicker">Part 2 · The fix · 3 min</p>
```

```css
.kicker {
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--primary);
}
.quote-dark .kicker, .divider .kicker { color: inherit; opacity: .8; }
```

Kicker discipline: 3 fragments max (`Part · Topic · Time`). Color is `primary`
on light, inherited white/cream on inverted slides. Never set kickers in
`accent` amber on light — amber kickers fail contrast and scream louder than
the headline. The one amber exception: the single highlight number's kicker
("NRR" above "128%") may be amber at 14px bold or larger.

### Accent band (left rail and top rail)

```html
<!-- left rail for callouts -->
<aside class="band-left">
  <p class="kicker">Callout</p>
  <p>Stale-while-revalidate cut origin hits 63% before p95 even moved.</p>
</aside>

<!-- top rail for CTA / divider -->
<section class="band-top">
  <h2>Roll Shield to all regions by Oct 31</h2>
</section>
```

```css
.band-left { border-left: 4px solid var(--accent); padding-left: 16px; }
.band-top { border-top: 4px solid var(--primary); padding-top: 24px; }
```

Band discipline: one band per slide, 4px thick, never both rails at once.
Callout bands use `accent`; structural bands (CTA top, divider top) use
`primary`. On photos, bands go inside the scrim box in white.

---

## 5. Insertion technique: opposite-mode slides

One opposite-mode slide per 8–10 slides is the fastest wall-breaker: a dark
quote or code slide inside a light deck, or a light handout-style explainer
inside a dark deck. The technique is safe only with a contrast re-check —
flipping the page fill invalidates every text color on that slide.

Dark slide in a light deck (Acme example — Lena Moreau quote):

```html
<section class="insert-dark">
  <span class="rule" aria-hidden="true"></span>
  <blockquote>"Deploys stopped being scary."</blockquote>
  <p class="attr">Lena Moreau, CTO of Northwind</p>
  <p class="cap">Photo: Maria Santos, Acme lab · 320KB</p>
</section>
```

```css
.insert-dark { background: #0D1117; color: #E6EDF3; }
.insert-dark .attr { color: #8B949E; }
.insert-dark .cap { color: #8B949E; }
.insert-dark .rule { background: var(--accent); }
```

Light slide in a dark deck (Acme example — handout explainer):

```html
<section class="insert-light">
  <p class="kicker">Handout · take a photo</p>
  <h2>The 90-second Shield recipe</h2>
  <ol>
    <li>Enable the flag in iad — Jonas, Jun 14</li>
    <li>Watch p95 for 24 hours</li>
    <li>Roll to fra, then hnd</li>
  </ol>
</section>
```

```css
.insert-light { background: #FFFFFF; color: #0D1117; }
.insert-light .kicker { color: #2563EB; }
.insert-light li { color: #0D1117; }
```

Contrast re-check procedure (run on every inserted slide, 3 minutes):

1. List the slide's text colors against its new fill: body/fg, caption/muted,
   kicker/primary, link/accent. Four pairs maximum.
2. Measure each with the DevTools picker or WebAIM. Normal text ≥ 4.5:1,
   large (≥18pt / 14pt bold) ≥ 3:1, code ≥ 7:1.
3. Fix failures by promoting, never by eye: swap `muted` for the `.fix-muted` rule in `references/colors.md`, darken the scrim 10%, or move the caption off the
   photo onto the card below.
4. Record the four ratios in the ship record (Gate 4 line). An inserted slide
   with no recorded ratios fails Gate 13 automatically.

Two tripwires: never invert a deck (5+ opposite slides is a second deck, pick
one mode); never place a dark code screenshot as a raster image on a light
slide — re-render the snippet in Shiki so text stays selectable and themed.

---

## 6. Gradient discipline

Full rule + banned default in `references/colors.md`; Gate 6 enforces the count. One gradient per deck maximum — hero background *or* one chart series, never both, never gradient text.

---

## 7. Failures + fixes (8)

**Failure 1 — white wall of 6 text slides.** Six base-`bg` slides in a row:
stall, tickets, rollout, config, chart, NRR — all on `#FFFFFF`, no divider,
no photo, no band. Audience checks phones by slide 4.

Fix: convert slide 3 to a tinted divider ("The fix", solid `primary`,
inverted text) and slide 5 to a dark code slide (`#0D1117` block). Longest
run drops from 6 to 2. Record the rotation in the outline `bg:` tags.

**Failure 2 — accent on every slide equals accent on no slide.** Teal buttons
+ amber kickers + green deltas + purple rules across all 10 slides. Nothing
is highlighted because everything is.

Fix: pick one accent per deck per `references/colors.md` 60-30-10. Teal Serenity keeps
`primary #0D9488` for buttons/links and exactly one amber `#F59E0B` number
(NRR 128%, slide 8). Recolor every other amber element to `muted` or `fg`.

**Failure 3 — dark code block pasted on a photo.** A `#0D1117` snippet card
floated over Maria Santos's lab photo with no scrim. Caption behind the
terminal reads 2.1:1; the photo fights the syntax colors.

Fix: move code onto its own slide (base `bg` + dark block, section 2
sketch), or keep the photo slide visual-only with a 2-line caption and push
the snippet to the next slide. Never float small text over busy pixels.

**Failure 4 — gray-on-gray captions.** `muted #64748B` captions on `surface
#F1F5F9` assumed fine, measures 4.2:1 on the venue projector and vanishes at
50% brightness. Source lines ("edge logs Jun 14 → Sep 2") unreadable.

Fix: apply the `.fix-muted` rule from `references/colors.md` to every caption
on `surface`, or move captions onto `bg`. Re-measure the trio (`fg/bg`,
`muted/bg`, `muted/surface`) and record all three in the ship record.

**Failure 5 — pure-black / pure-white halation.** `#000000` body on `#FFFFFF`
in a dark projector room blooms; `#FFFFFF` on `#000000` quote slide glares.
Eyes water, nobody reads the Lena Moreau quote.

Fix: use palette near-blacks and papers instead — quote slide `#0D1117` on
`#E6EDF3`, paper decks `#1A1A18` on `#FAF9F6`, Botanical `#1C1917` on
`#FEFCF8`. Never ship `#000`/`#FFF` pairs except the `.projector-safe`
emergency class below.

**Failure 6 — inverted deck without re-checking ratios.** Team inverts five
Acme slides to dark for "drama" but keeps light-mode `muted #57606A`
captions. On `#0D1117` the captions technically pass but the amber kicker at
12px fails, and links in `#2563EB` drop to 3.1:1.

Fix: run the section 5 re-check on every inverted slide — all four pairs,
measured, recorded. Swap light `primary #2563EB` for dark `#4493F8`,
light `muted #57606A` for dark `#8B949E`. Five inverted slides is a second
deck — pick one mode and cut the rest.

**Failure 7 — two competing accents.** Bento deck uses blue `#2563EB` bars
*and* green `#16A34A` trend arrows *and* amber `#D97706` callouts on one
slide. Finance reads green as "good" and amber as "warning" simultaneously —
the NRR 128% story collapses.

Fix: one data accent per slide. Bento keeps blue bars; the single delta gets
green *with* an up-arrow and `+` sign (shape, not color alone). Amber leaves
the slide entirely unless it is the deck's one highlight number.

**Failure 8 — projector washout.** Botanical cream `#FEFCF8` with hairline
`#E7DFCF` borders and 12px muted `#78716C` captions looks perfect on a
MacBook, disappears on a 3000-lumen projector in a lit room. Borders vanish,
captions evaporate.

Fix: bump type 10–15% for projector rooms, promote captions with
the `.fix-muted` rule from `references/colors.md`, thicken card borders to 1px `var(--border)` minimum (never
borderless white on white), and carry the `.projector-safe` fallback class
below that forces `fg #000` on `bg #FFF` with underlined links. Rehearse on the
venue projector; if muted vanishes, it ships as `fg`.

```css
.projector-safe {
  --bg: #FFFFFF !important;
  --surface: #F1F5F9 !important;
  --card: #FFFFFF !important;
  --fg: #000000 !important;
  --muted: #334155 !important;
  --border: #94A3B8 !important;
  --primary: #1D4ED8 !important;
}
.projector-safe a { text-decoration: underline; }
```

---

## 8. Rebuild-prompt discipline (1 page per slide)

Every rebuild prompt carries an exact per-slide spec — four fields, no prose substitutes:

```text
Slide 07 — proof — bg: surface #1A2238 — type: display-120 + body 18px
scrim: heavy-68% — image: assets/lab-maria-03.jpg (full-bleed right, credit Maria Santos)
```

Template: `bg-token + type-pt + scrim-% + image-id`. Type-pt is `display-96/120/138` or body `17–19px` per `references/layouts.md`; scrim-% is `none / light-55% / heavy-68%` (stops in `references/colors.md`); image-id is the `assets/` file + crop mask (`arch/blob/circle/full-bleed`). Missing field = rebuild rejected.

## 9. Morph anchors mapping

Named-shape persistence across adjacent slides — details live in `references/pptx-motion-language.md`, mapping here only:

- reveal.js: `data-transition="none"` on the deck + matching `data-id` on the repeated anchor (headline block, accent shape, photo frame).
- Slidev: `transition: none` frontmatter + matching `data-id` / `v-motion` anchor key on the repeated element.
- Move or resize ONE anchor per slide step, never both. Anchors are big (display headline, full-bleed photo, stat strip) — 2 per section minimum.

---

## Ship it

Before building: pick the palette in `references/colors.md`, copy its token snippet from
`references/visual-styles/*.md`,
assign one background per slide type (section 2 table), and tag every outline
line with `bg:` (mandatory — every line, longest identical-`bg` run ≤2 or ship-blocker). Stock `theme: default` with no applied style never counts as rotation. Before shipping: run Gates 3–4, 6, and 13–14 — contrast trio
recorded, gradient count ≤ 1, no 3 consecutive same-bg text slides, media
density met, zero emoji icons. Print one bento and one code slide in
grayscale. Then present.
