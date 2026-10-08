# Color Usage — Deploying Color Across a Deck

> Companion to `colors.md`. Tokens live there; this file tells you where each
> token goes slide by slide so the deck never reads as a white wall.
> Components reference variables, never raw hex. If a hex appears outside
> `:root` / `@theme`, it is a bug.

Demo universe for every example below: Acme Shield Q3 readout. Speaker Ada,
data owner Jonas, lab photo by Maria Santos. Headline stat: p95 latency fell
41% (412ms to 243ms over six weeks, edge logs Jun 14 to Sep 2, confirmed
against billing export). Second stat: NRR 128%. All slides below use these
real beats — never placeholder text.

Related: palettes + tokens + contrast pairs in `colors.md`; ship gates in
`verify-checklist.md` (Gates 5, 9, 17); layout sketches in `layouts.md`;
slide-type sketches in `layout-templates/`.

---

## 1. The anti-white-wall rule

**Max 2 consecutive slides on the base `bg`. Every 3rd slide must change
surface.** A "surface change" is one of: tinted section divider, image bleed,
accent band, dark quote slide, dark code slide, stat-bento band, CTA wash.

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

Track the rotation in the outline itself with a `bg:` tag per slide:

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
deck, then repeat. The table lists the assignment; the sketches show the CSS.

| Slide type | Light decks (base `bg`) | Dark decks (base `bg`) | Notes |
|---|---|---|---|
| Hero / title | Brand surface + glow ≤ 8% | Brand surface + glow ≤ 8% | The one allowed gradient lives here, or nowhere |
| Section divider | Solid `primary` or dark wash, inverted text | Solid `primary` or deeper `bg`, inverted text | Always tinted — never base `bg` with a bigger heading |
| Quote | Dark surface (`code-bg` or palette dark `bg`) | Deeper card + accent rule | Dark quote slides are the easiest rotation lever |
| Code | Always dark block (`code-bg #0D1117`) even in light decks | Dark block, same value | Screenshots match; Shiki theme follows the block, not the page |
| Stat / bento | `surface` band behind white cards | `surface` band behind dark cards | Cards carry 1px `var(--border)` so they survive projectors |
| Image bleed | Full-bleed photo + scrim, caption overlaid | Same, heavier scrim | Caption + credit always; scrim guarantees 4.5:1 |
| Comparison | `surface` panel vs `card` panel | Same split | Loser side muted, winner side `primary` border |
| CTA / closing | Accent-tinted wash (`surface` + `primary` band) | Gradient CTA or solid `primary` | Buttons `primary`, one highlight number in `accent` |

Hero sketch (light deck, Teal Serenity tokens via variables):

```html
<section class="hero-teal">
  <p class="kicker">Acme Shield · Q3 readout</p>
  <h1>p95 fell 41% in six weeks</h1>
  <p>412ms to 243ms across three regions. Ada presents, Jonas on data.</p>
</section>
```

```css
.hero-teal {
  background: linear-gradient(135deg, var(--primary) 0%, #0F766E 55%, #115E59 100%);
  color: #FFFFFF;
}
.hero-teal .kicker { color: #CCFBF1; letter-spacing: .12em; text-transform: uppercase; }
```

Divider sketch (solid primary, inverted text — works in every palette):

```html
<section class="divider">
  <span class="rule" aria-hidden="true"></span>
  <p class="kicker">Part 2</p>
  <h2>The fix</h2>
  <p>Shield rollout: three regions, one flag, zero downtime deploys.</p>
</section>
```

```css
.divider { background: var(--primary); color: #FFFFFF; }
.divider .kicker { color: #FFFFFF; opacity: .8; }
.divider .rule { display: block; width: 48px; height: 4px; background: #FFFFFF; opacity: .9; }
```

Quote sketch (always dark, even in light decks):

```html
<section class="quote-dark">
  <span class="rule" aria-hidden="true"></span>
  <blockquote>"Deploys stopped being scary. Our p95 graph looks like a ski slope now."</blockquote>
  <p class="attr">Lena Moreau, CTO of Northwind — Acme Shield customer since June</p>
</section>
```

```css
.quote-dark { background: #0D1117; color: #E6EDF3; }
.quote-dark .attr { color: #8B949E; }
.quote-dark .rule { display: block; width: 48px; height: 4px; background: var(--accent); }
```

Code sketch (dark block pasted on light slide — the block is dark, the page stays light):

```html
<section class="code-slide">
  <h2>One flag, ninety seconds</h2>
  <pre><code class="language-ts">shield.enable({ staleWhileRevalidate: 90 });
// rollout: iad → fra → hnd — Jonas, edge logs Jun 14 → Sep 2</code></pre>
  <p class="cap">Full module: github.com/acme/shield — link in notes.</p>
</section>
```

```css
.code-slide { background: var(--bg); color: var(--fg); }
.code-slide pre { background: #0D1117; color: #E6EDF3; border-radius: 16px; }
.code-slide .cap { color: var(--muted); }
```

CTA sketch (accent-tinted wash, single highlight number):

```html
<section class="cta">
  <p class="kicker">The ask</p>
  <h2>Roll Shield to all regions by Oct 31</h2>
  <p>Costs one sprint. Saves <strong>169ms</strong> on every checkout.</p>
  <a class="btn" href="#">Approve the rollout</a>
</section>
```

```css
.cta { background: var(--surface); color: var(--fg); border-top: 4px solid var(--primary); }
.cta strong { color: var(--accent); }
.cta .btn { background: var(--primary); color: #FFFFFF; }
```

---

## 3. Worked full-deck color scripts (4 palettes)

Each script is a 10-slide Acme Shield Q3 readout: stall (2), fix (4),
proof (3), ask (1). `bg:` names the page fill; components inside still use
`card` / `surface` / `code-bg` per section 2. Token values are copied exactly
from `colors.md` — variables in code, hex here as spec.

### 3A. Midnight SaaS (dark-first devtools)

Palette tokens: dark primary `bg #0B1020`, `surface #1A2238`,
`card #141B30`, `fg #E8EEF9`, `muted #8A93A6`, `border #2A3348`,
`primary #4F7DF3`, `accent #9B6BFF`. Light handout: `bg #F8FAFC`,
`fg #0F172A`. Code stays `#0D1117` / `#E6EDF3` in both modes.

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

### 3B. Paper Editorial (serif keynote, light-first)

Palette tokens: light `bg #FAF9F6`, `surface #EFEDE6`, `card #FFFFFF`,
`fg #1A1A18`, `muted #6B6660`, `border #DDD8CC`, `primary #B45309`,
`accent #0F766E`. Dark evening: `bg #1A1A18`, `fg #F2EFE6`. Code blocks
stay neutral `#FFFFFF` cards (light) — never paper-tinted code backgrounds.

| # | Beat | `bg:` surface | What the audience sees |
|---|---|---|---|
| 1 | Hero | `bg #FAF9F6`, generous 64px margins | Fraunces headline "The summer deploys stopped hurting", chapter numeral in `#B45309` |
| 2 | Stall | base `bg #FAF9F6` | Essay slide: three paragraphs on the June outage, drop cap, folio "1" |
| 3 | Stall | `surface #EFEDE6` pull-quote panel | Support ticket verbatim on tinted panel — SURFACE CHANGE |
| 4 | Divider | solid `primary #B45309`, cream text `#FAF9F6` | "Chapter II — The fix" — SURFACE CHANGE |
| 5 | Fix | base `bg #FAF9F6` | Shield rollout diary: three dated entries, hairline `#DDD8CC` rules |
| 6 | Fix | white `#FFFFFF` code card on paper | 9-line snippet, `github-light` Shiki, caption in `muted #6B6660` |
| 7 | Proof | base `bg #FAF9F6` | Single-column p95 chart, axes in muted, one teal `#0F766E` highlight dot |
| 8 | Proof | `surface #EFEDE6` stat band | NRR 128% set in Fraunces 72pt, method note underneath |
| 9 | Quote | dark `#1A1A18` evening slide | Lena Moreau quote in cream `#F2EFE6`, teal rule — SURFACE CHANGE |
| 10 | Ask | warm vignette (allowed gradient) | Closing: "Ship the calm" + rollout date, vignette `#EFEDE6 → #FAF9F6` |

Rotation check: paper decks feel wall-like fastest, so the tinted panel (3),
ochre divider (4), and dark quote (9) do the heavy lifting. Code stays white
so syntax hues do not shift on cream.

### 3C. Teal Serenity (startup pitch, light-first)

Palette tokens: light `bg #FFFFFF`, `surface #F0FDFA`, `card #FFFFFF`,
`fg #0F172A`, `muted #5F6B7A`, `border #CCFBF1`, `primary #0D9488`,
`accent #F59E0B`. Dark demo: `bg #0B1F1E`, `surface #123836`,
`card #0F2E2C`, `fg #ECFDF5`. Amber reserved for exactly one highlight
number per deck.

| # | Beat | `bg:` surface | What the audience sees |
|---|---|---|---|
| 1 | Hero | white `bg #FFFFFF` + teal kicker | "Checkout in 243ms" — Sora headline, teal `#0D9488` CTA button |
| 2 | Problem | base `bg #FFFFFF` | Cart abandonment 23% at 412ms, one angry quote from checkout logs |
| 3 | Problem | `surface #F0FDFA` tinted panel | Three tickets, mint band, teal left borders — SURFACE CHANGE |
| 4 | Divider | photo bleed, checkout session | Full-bleed photo of checkout terminal, dark scrim, caption — SURFACE CHANGE |
| 5 | Solution | base `bg #FFFFFF` | Shield diagram: edge → cache → origin, 3 boxes, 1px `#CCFBF1` borders |
| 6 | Demo | dark `#0B1F1E` code slide | Live terminal on dark, `vitesse-dark`, mint `fg #ECFDF5` — SURFACE CHANGE |
| 7 | Traction | base `bg #FFFFFF` | p95 412 → 243ms bars, single-series teal wash (allowed gradient) |
| 8 | Traction | `surface #F0FDFA` bento | NRR **128%** in amber `#F59E0B` — the deck's one amber number |
| 9 | Team | base `bg #FFFFFF` | Ada, Jonas, Maria Santos: three portraits, names + roles, muted captions |
| 10 | Ask | CTA gradient (allowed gradient) | Teal gradient wash, white headline "Raise the seed round", scrim under body |

Rotation check: mint band (3), photo (4), dark demo (6), CTA wash (10) break
every run. Amber appears once (slide 8) — anywhere else it gets cut. White
on `#0D9488` is 3.9:1, so CTA body copy sits under a dark scrim, headings
only in white.

### 3D. Botanical Warm (workshop / edu, light-first)

Palette tokens: light `bg #FEFCF8`, `surface #F5F0E6`, `card #FFFDF7`,
`fg #1C1917`, `muted #78716C`, `border #E7DFCF`, `primary #15803D`,
`accent #C2410C`. Dark evening: `bg #1C1917`, `surface #292524`,
`fg #FAF7F0`, `accent #FB923C`. One `Caveat` annotation per deck maximum.

| # | Beat | `bg:` surface | What the audience sees |
|---|---|---|---|
| 1 | Welcome | sunrise wash (allowed gradient) | "Welcome to Ship Calm" — Fraunces headline, gradient `#FEFCF8 → #F5F0E6 → #EDE5D3` |
| 2 | Why slow hurts | base `bg #FEFCF8` | Checkout story: Amara's bakery, 412ms cart, warm illustration |
| 3 | Why slow hurts | `surface #F5F0E6` panel | Three learner sticky notes on kraft panel — SURFACE CHANGE |
| 4 | Divider | solid `primary #15803D`, cream text | "Part 2 — Try it yourself" with leaf rule — SURFACE CHANGE |
| 5 | Try it | base `bg #FEFCF8` | Exercise: enable Shield on a staging checkout, 4 steps, checkboxes |
| 6 | Try it | white `#FFFDF7` code card | 8-line snippet, `github-light`, one `Caveat` arrow "start here!" |
| 7 | What changed | base `bg #FEFCF8` | Before/after: 412ms vs 243ms, terracotta `#C2410C` callout border on winner |
| 8 | What changed | `surface #F5F0E6` stat band | NRR 128% + two learner quotes, kraft band — SURFACE CHANGE |
| 9 | Story | dark `#1C1917` evening slide | Amara's quote in cream `#FAF7F0`, terracotta `#FB923C` rule — SURFACE CHANGE |
| 10 | Thank you | base `bg #FEFCF8` + leaf footer | "Take the checklist home" + QR to repo, leaf-green button `#15803D` |

Rotation check: kraft panels (3, 8), green divider (4), dark story (9) keep
cream from walling. Muted `#78716C` on `#FEFCF8` is 4.6:1 — keep captions at
14px or larger, never 12px. Code stays neutral white so token hues survive.

---

## 4. Accent-band / kicker / rule component spec

Three tiny components carry the whole rotation system. Build them once,
reuse on every slide. One accent per slide — pick `primary` or `accent`,
never both at full saturation.

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
3. Fix failures by promoting, never by eye: swap `muted` for `fg` at 82%
   opacity (`.fix-muted`), darken the scrim 10%, or move the caption off the
   photo onto the card below.
4. Record the four ratios in the ship record (Gate 5 line). An inserted slide
   with no recorded ratios fails Gate 17 automatically.

```css
/* emergency contrast fix — promote muted without redesigning */
.fix-muted { color: var(--fg); opacity: .82; }
```

Two tripwires: never invert a deck (5+ opposite slides is a second deck, pick
one mode); never place a dark code screenshot as a raster image on a light
slide — re-render the snippet in Shiki so text stays selectable and themed.

---

## 6. Gradient discipline recap

One gradient per deck maximum. Allowed: a single hero background *or* one
chart series — never both. Never gradient body text. Full rule + banned
default in `colors.md`; Gate 9 enforces the count.

Allowed example 1 — hero background wash (GitHub Tech tokens via variables):

```css
.hero-allowed {
  background: linear-gradient(180deg, var(--surface) 0%, var(--bg) 70%);
}
```

Allowed example 2 — single chart-series wash (Bento Minimal bar fade):

```css
.bar-allowed {
  background: linear-gradient(180deg, #3B82F6 0%, #1D4ED8 100%);
}
```

Banned example 1 — full-bleed purple-blue cover (the default AI-slop cover):

```css
/* BANNED — delete on sight */
.banned-cover {
  background: linear-gradient(135deg, #7C3AED 0%, #2563EB 100%);
}
```

Banned example 2 — gradient headline text (kills contrast, rasterizes badly):

```css
/* BANNED — background-clip text fails contrast + exports as mush */
.banned-headline {
  background: linear-gradient(90deg, #0D9488, #F59E0B);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
```

Banned example 3 — gradient on every surface (cover + divider + CTA + card):

```css
/* BANNED — four gradients fighting; keep the hero, delete the rest */
.banned-everywhere { background: linear-gradient(135deg, #0D9488, #115E59); }
/* .divider, .cta, .card must return to solid var(--primary) / var(--surface) / var(--card) */
```

Glow corollary: radial glows count as the deck's one gradient. Cap glow
layers at ≤ 8% opacity each, two layers max, hero only. Midnight SaaS hero
uses `rgba(79,125,243,.35)` — that reads strong on stage; halve it for
projector rooms.

Print fallback: every gradient slide ships a flat-color fallback (hero →
solid `bg`; bars → solid `primary`). Verify by printing one hero and one
chart slide in grayscale — borders must survive, deltas must differ by shape
(arrow + sign), not color alone.

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

Fix: pick one accent per deck per `colors.md` 60-30-10. Teal Serenity keeps
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

Fix: apply `.fix-muted { color: var(--fg); opacity: .82; }` to every caption
on `surface`, or move captions onto `bg`. Re-measure the trio (`fg/bg`,
`muted/bg`, `muted/surface`) and record all three in the ship record.

**Failure 5 — pure-black / pure-white halation.** `#000000` body on `#FFFFFF`
in a dark projector room blooms; `#FFFFFF` on `#000000` quote slide glares.
Eyes water, nobody reads the Lena Moreau quote.

Fix: use palette near-blacks and papers instead — quote slide `#0D1117` on
`#E6EDF3`, paper decks `#1A1A18` on `#FAF9F6`, Botanical `#1C1917` on
`#FEFCF8`. Never ship `#000`/`#FFF` pairs except the `.projector-safe`
emergency class.

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
`.fix-muted`, thicken card borders to 1px `var(--border)` minimum (never
borderless white on white), and carry the `.projector-safe` fallback class
that forces `fg #000` on `bg #FFF` with underlined links. Rehearse on the
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

## Ship it

Before building: pick the palette in `colors.md`, copy its `@theme` snippet,
assign one background per slide type (section 2 table), and tag every outline
line with `bg:`. Before shipping: run Gates 5, 9, and 17–19 — contrast trio
recorded, gradient count ≤ 1, no 3 consecutive same-bg text slides, media
density met, zero emoji icons. Print one bento and one code slide in
grayscale. Then present.
