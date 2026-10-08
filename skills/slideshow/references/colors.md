# Colors — Tokens + 6 Palettes + Rules + Code Themes

> Components reference variables, never raw hex. If a hex appears outside `:root` / `@theme`, it is a bug.

## Base tokens (ship this first)

```css
:root {
  --bg: #FFFFFF;
  --surface: #F1F5F9;
  --card: #FFFFFF;
  --fg: #0F172A;
  --muted: #64748B;
  --border: #E2E8F0;
  --primary: #2563EB;
  --accent: #7C3AED;
  --success: #16A34A;
  --warning: #F59E0B;
  --danger: #DC2626;
  --code-bg: #0D1117;
  --code-fg: #E6EDF3;
}
.dark {
  --bg: #0B1020;
  --surface: #1A2238;
  --card: #141B30;
  --fg: #E8EEF9;
  --muted: #8A93A6;
  --border: #2A3348;
  --primary: #4F7DF3;
  --accent: #9B6BFF;
  --success: #22C55E;
  --warning: #FBBF24;
  --danger: #F87171;
  --code-bg: #0D1117;
  --code-fg: #E6EDF3;
}
```

Toggle `.dark` on `<html>`. All cards use `var(--card)`, all page fills use `var(--bg)`, all inset panels use `var(--surface)`.

```js
// theme toggle (copy-paste)
const root = document.documentElement;
document.getElementById('theme-toggle').addEventListener('click', () => {
  root.classList.toggle('dark');
  document.querySelectorAll('pre code').forEach(el => {
    el.dataset.theme = root.classList.contains('dark') ? 'dark' : 'light';
  });
});
```

## Global rules

- **WCAG:** normal text >= 4.5:1, large text (>= 18pt / 14pt bold) >= 3:1. Check `fg` on `bg` and `muted` on `bg` *and* `muted` on `surface` before shipping. Muted-on-surface fails most often.
- **60-30-10:** 60% neutral bg, 30% surface, 10% accent maximum. One accent per slide. Amber/green/red are data signals, not decoration.
- **Max 1 gradient per deck.** Never gradient body text (`background-clip: text` kills contrast and exports badly). Allowed: single hero background *or* one chart series, never both.
- **Banned default:** full-bleed purple-blue linear gradient (`#7C3AED` to `#2563EB` cover slide). Pick a palette below instead.
- **Max 2 font families + mono for code only.** Example: `Inter` + `Fraunces`, code `JetBrains Mono`.
- **Shiki dual themes:** `vitesse-light` / `vitesse-dark` or `github-light` / `github-dark`. Match Shiki theme to `.dark` toggle. Never ship an unstyled gray code block.
- **Borders do work:** 1px `var(--border)` on every card and image. On projectors, borderless white cards on white backgrounds vanish.
- **Success/warning discipline:** green means up-good or pass. Amber means caution or one highlight number. Red means down-bad or danger. Never use green for decoration.

---

## Palette 1. Midnight SaaS — devtools dark

Devtools-dark, dashboards, CLI product tours. Mono code blocks, glowing borders on dark, terminal green for pass states.

### Full token table

| Token | Light (docs companion) | Dark (primary) | Usage |
|---|---|---|---|
| `bg` | `#F8FAFC` | `#0B1020` | Page fill |
| `surface` | `#E2E8F0` | `#1A2238` | Inset panels, table headers |
| `card` | `#FFFFFF` | `#141B30` | Cards, modals |
| `fg` | `#0F172A` | `#E8EEF9` | Headings, body |
| `muted` | `#64748B` | `#8A93A6` | Captions, axes, footers |
| `border` | `#E2E8F0` | `#2A3348` | Card + image borders |
| `primary` | `#2563EB` | `#4F7DF3` | Links, primary buttons, bars |
| `accent` | `#7C3AED` | `#9B6BFF` | One highlight per slide |
| `success` | `#16A34A` | `#22C55E` | Pass, up-good deltas |
| `warning` | `#D97706` | `#FBBF24` | Caution, one highlight number |

### Dark + light pairs
Ship dark-first. Light is for handout PDF only. Dark `bg #0B1020` with `fg #E8EEF9` measures ~13.8:1. Light `bg #F8FAFC` with `fg #0F172A` measures ~15.2:1. Muted on dark surface (`#8A93A6` on `#1A2238`) measures ~5.1:1 — passes.

### Contrast ratios (measured, sRGB)
- `fg / bg` dark: 13.8:1 — PASS AAA
- `muted / bg` dark: 7.2:1 — PASS AA
- `primary / bg` dark (`#4F7DF3` on `#0B1020`): 5.4:1 — PASS for large text + UI, fail for small body (do not set body in primary)
- `accent / bg` dark: 4.9:1 — PASS AA for large text, use for headings only

### When to use vs avoid
Use for evening meetups, devtools launches, live CLI demos where the terminal is the hero. Avoid for printed handouts, morning corporate keynotes, or education decks for non-technical audiences (dark tires unfamiliar readers).

### Font pairing + Google Fonts URL
Headings `Space Grotesk` 600, body `Inter` 400/500, code `JetBrains Mono` 400.

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
```

```css
--font-display: "Space Grotesk", system-ui, sans-serif;
--font-body: "Inter", system-ui, sans-serif;
--font-mono: "JetBrains Mono", ui-monospace, monospace;
```

### Code theme
Shiki `vitesse-dark` (primary) / `vitesse-light` (handout). Background stays `#0D1117` in both modes so screenshots match.

### Gradient-allowed example (one per deck)
Hero background only, never text:

```css
.hero-midnight {
  background:
    radial-gradient(1200px 500px at 20% -10%, rgba(79,125,243,.35), transparent 60%),
    radial-gradient(900px 420px at 90% 10%, rgba(155,107,255,.28), transparent 60%),
    #0B1020;
}
```

### Tailwind v4 @theme snippet
```css
@theme {
  --color-bg: #0B1020;
  --color-surface: #1A2238;
  --color-card: #141B30;
  --color-fg: #E8EEF9;
  --color-muted: #8A93A6;
  --color-border: #2A3348;
  --color-primary: #4F7DF3;
  --color-accent: #9B6BFF;
  --color-success: #22C55E;
  --color-warning: #FBBF24;
  --font-display: "Space Grotesk", system-ui, sans-serif;
  --font-sans: "Inter", system-ui, sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, monospace;
}
```

---

## Palette 2. GitHub Tech — corporate neutral

Corporate keynotes, docs-led talks, API platform stories. Neutral, trustworthy, prints perfectly.

### Full token table

| Token | Light (primary) | Dark (code slides) | Usage |
|---|---|---|---|
| `bg` | `#FFFFFF` | `#0D1117` | Page fill |
| `surface` | `#F1F5F9` | `#161B22` | Panels, table stripes |
| `card` | `#FFFFFF` | `#161B22` | Cards |
| `fg` | `#0D1117` | `#E6EDF3` | Headings, body |
| `muted` | `#57606A` | `#8B949E` | Captions, secondary |
| `border` | `#D0D7DE` | `#30363D` | Borders, dividers |
| `primary` | `#2563EB` | `#4493F8` | Links, buttons |
| `accent` | `#7C3AED` | `#A371F7` | Single highlight |
| `success` | `#1A7F37` | `#3FB950` | Pass deltas |
| `warning` | `#9A6700` | `#D29922` | Caution |

### Contrast ratios
- Light `fg / bg` (`#0D1117` on `#FFFFFF`): 18.1:1 — PASS AAA
- Light `muted / bg` (`#57606A` on `#FFFFFF`): 6.9:1 — PASS AA
- Light `muted / surface` (`#57606A` on `#F1F5F9`): 6.1:1 — PASS AA
- Dark code `fg / bg` (`#E6EDF3` on `#0D1117`): 15.9:1 — PASS AAA

### When to use vs avoid
Use when stakeholders outnumber engineers, when the deck becomes a PDF handout, when legal/compliance reviews slides. Avoid when you need emotional punch — this palette is deliberately calm. Do not add glow or neon; it breaks the contract.

### Font pairing + Google Fonts URL
Headings + body `Inter`, code `JetBrains Mono`. Single family keeps it corporate-clean.

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
```

### Code theme
Shiki `github-light` / `github-dark`. Match GitHub's own rendering so pasted snippets look familiar.

```js
// Shiki dual-theme setup
import { codeToHtml } from 'shiki';
const html = await codeToHtml(source, {
  lang: 'ts',
  themes: { light: 'github-light', dark: 'github-dark' }
});
```

### Gradient-allowed example
Subtle surface wash for the title slide only:

```css
.hero-github {
  background: linear-gradient(180deg, #F1F5F9 0%, #FFFFFF 70%);
}
.dark .hero-github {
  background: linear-gradient(180deg, #161B22 0%, #0D1117 70%);
}
```

### Tailwind v4 @theme snippet
```css
@theme {
  --color-bg: #FFFFFF;
  --color-surface: #F1F5F9;
  --color-card: #FFFFFF;
  --color-fg: #0D1117;
  --color-muted: #57606A;
  --color-border: #D0D7DE;
  --color-primary: #2563EB;
  --color-accent: #7C3AED;
  --color-success: #1A7F37;
  --color-warning: #9A6700;
  --font-sans: "Inter", system-ui, sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, monospace;
}
```

---

## Palette 3. Paper Editorial — serif keynote

Essay keynotes, publishing, design talks, founder stories. Serif headings, generous margins, no glow, paper texture.

### Full token table

| Token | Light (primary) | Dark (evening variant) | Usage |
|---|---|---|---|
| `bg` | `#FAF9F6` | `#1A1A18` | Paper fill |
| `surface` | `#EFEDE6` | `#2A2925` | Pull-quote panels |
| `card` | `#FFFFFF` | `#242320` | Cards |
| `fg` | `#1A1A18` | `#F2EFE6` | Body + headings |
| `muted` | `#6B6660` | `#A8A29E` | Captions, folios |
| `border` | `#DDD8CC` | `#3F3D38` | Hairlines |
| `primary` | `#B45309` | `#F59E0B` | Links, chapter numbers |
| `accent` | `#0F766E` | `#2DD4BF` | Single highlight |
| `success` | `#15803D` | `#4ADE80` | Positive deltas |
| `warning` | `#B45309` | `#FBBF24` | Caution |

### Contrast ratios
- `fg / bg` light (`#1A1A18` on `#FAF9F6`): 14.6:1 — PASS AAA
- `muted / bg` light (`#6B6660` on `#FAF9F6`): 5.3:1 — PASS AA
- `primary / bg` light (`#B45309` on `#FAF9F6`): 4.6:1 — PASS AA (body-safe, barely — prefer fg for paragraphs)
- Dark `fg / bg` (`#F2EFE6` on `#1A1A18`): 13.1:1 — PASS AAA

### When to use vs avoid
Use for 20-minute narrative arcs, memoirs, craft talks. Generous whitespace is the point — 64px margins minimum. Avoid for dashboards, API references, or any slide with more than 4 numbers. Serif numerals in tables look wrong; switch those slides to GitHub Tech.

### Font pairing + Google Fonts URL
Headings `Fraunces` 560/640 optical, body `Source Serif 4` or `Inter` for readability, code `IBM Plex Mono`.

```html
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet" />
```

```css
--font-display: "Fraunces", Georgia, serif;
--font-body: "Inter", system-ui, sans-serif;
--font-mono: "IBM Plex Mono", ui-monospace, monospace;
```

### Code theme
Shiki `github-light` on `#FFFFFF` cards (never paper-tinted code backgrounds — tint shifts syntax hues). Dark variant `github-dark`.

### Gradient-allowed example
Paper decks usually skip gradients. If one is needed, a warm vignette on the closing slide:

```css
.hero-paper {
  background: radial-gradient(1000px 420px at 50% 110%, #EFEDE6 0%, #FAF9F6 65%);
}
```

### Tailwind v4 @theme snippet
```css
@theme {
  --color-bg: #FAF9F6;
  --color-surface: #EFEDE6;
  --color-card: #FFFFFF;
  --color-fg: #1A1A18;
  --color-muted: #6B6660;
  --color-border: #DDD8CC;
  --color-primary: #B45309;
  --color-accent: #0F766E;
  --color-success: #15803D;
  --color-warning: #B45309;
  --font-display: "Fraunces", Georgia, serif;
  --font-sans: "Inter", system-ui, sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, monospace;
}
```

---

## Palette 4. Teal Serenity — startup pitch

Startup pitches, clean SaaS stories, investor updates. Teal CTAs, amber reserved for exactly one highlight number per deck.

### Full token table

| Token | Light (primary) | Dark (demo slides) | Usage |
|---|---|---|---|
| `bg` | `#FFFFFF` | `#0B1F1E` | Page fill |
| `surface` | `#F0FDFA` | `#123836` | Panels |
| `card` | `#FFFFFF` | `#0F2E2C` | Cards |
| `fg` | `#0F172A` | `#ECFDF5` | Text |
| `muted` | `#5F6B7A` | `#93A8A6` | Captions |
| `border` | `#CCFBF1` | `#1F4D4A` | Borders |
| `primary` | `#0D9488` | `#2DD4BF` | CTA buttons, links |
| `accent` | `#F59E0B` | `#FBBF24` | One highlight number |
| `success` | `#15803D` | `#4ADE80` | Traction up |
| `warning` | `#B45309` | `#FBBF24` | Burn / risk |

### Contrast ratios
- `fg / bg` light: 15.8:1 — PASS AAA
- `primary / bg` light (`#0D9488` on `#FFFFFF`): 3.9:1 — FAIL for body, PASS for large text + UI. Never set paragraphs in teal; use teal for buttons/headings at 18pt+.
- Dark `fg / bg` (`#ECFDF5` on `#0B1F1E`): 14.9:1 — PASS AAA

### When to use vs avoid
Use for 10-slide pitch arcs: problem, solution, traction, team, ask. Teal buttons photograph well. Avoid for technical deep-dives (teal code comments are low-contrast) and for data-heavy reviews (you need blue + green separation, not teal + amber).

### Font pairing + Google Fonts URL
Headings `Sora` or `Manrope` 700, body `Inter`, numbers `tabular-nums` via `font-variant-numeric`.

```html
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet" />
```

### Code theme
Shiki `vitesse-light` / `vitesse-dark`. Teal keywords render cleanly on both.

### Gradient-allowed example
CTA slide background (the single allowed gradient):

```css
.hero-teal {
  background: linear-gradient(135deg, #0D9488 0%, #0F766E 55%, #115E59 100%);
  color: #FFFFFF;
}
.hero-teal .muted { color: #CCFBF1; }
```

Check white on `#0D9488`: 3.9:1 — large headings only, never 14px body. Add a dark scrim if body text sits on the gradient.

### Tailwind v4 @theme snippet
```css
@theme {
  --color-bg: #FFFFFF;
  --color-surface: #F0FDFA;
  --color-card: #FFFFFF;
  --color-fg: #0F172A;
  --color-muted: #5F6B7A;
  --color-border: #CCFBF1;
  --color-primary: #0D9488;
  --color-accent: #F59E0B;
  --color-success: #15803D;
  --color-warning: #B45309;
  --font-display: "Sora", system-ui, sans-serif;
  --font-sans: "Inter", system-ui, sans-serif;
}
```

---

## Palette 5. Bento Minimal — data story

Metrics reviews, board updates, growth stories. Bento stat cards, blue bars, green deltas only. The most restrained palette here.

### Full token table

| Token | Light (primary) | Dark (optional) | Usage |
|---|---|---|---|
| `bg` | `#FFFFFF` | `#0A0F1E` | Page fill |
| `surface` | `#F1F5F9` | `#151D33` | Card fill |
| `card` | `#F8FAFC` | `#101830` | Stat cards |
| `fg` | `#0F172A` | `#E8EEF9` | Numbers + headings |
| `muted` | `#64748B` | `#8A93A6` | Labels, axes |
| `border` | `#E2E8F0` | `#26314D` | Card borders |
| `primary` | `#2563EB` | `#60A5FA` | Bars, links |
| `accent` | `#16A34A` | `#4ADE80` | Deltas only |
| `success` | `#16A34A` | `#4ADE80` | Up-good |
| `warning` | `#D97706` | `#FBBF24` | Down-bad flag |

### Contrast ratios
- `fg / bg`: 15.8:1 — PASS AAA
- `muted / surface` (`#64748B` on `#F1F5F9`): 4.9:1 — PASS AA
- `primary / bg` (`#2563EB` on `#FFFFFF`): 5.2:1 — PASS AA (chart labels safe)
- Never use green-on-white for small text (`#16A34A` on `#FFFFFF` is 3.3:1 — large numbers only, labels stay muted).

### When to use vs avoid
Use when numbers carry the talk: QBRs, experiment readouts, fundraising traction. One number per card, one delta per card. Avoid for emotional narratives — this palette has no warmth by design. If the deck needs a customer story, switch that single slide to Botanical Warm.

### Font pairing + Google Fonts URL
Everything `Inter` with tabular numbers; display numbers `Inter` 700 with `letter-spacing: -0.02em`.

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
```

```css
.tnum { font-variant-numeric: tabular-nums; letter-spacing: -0.02em; }
```

### Code theme
Minimal code in data decks. When needed, `github-light` / `github-dark` on `#0D1117` blocks.

### Gradient-allowed example
Single chart-series gradient (bars fade top-to-bottom, never rainbow):

```css
.bar-primary {
  background: linear-gradient(180deg, #3B82F6 0%, #1D4ED8 100%);
}
```

### Tailwind v4 @theme snippet
```css
@theme {
  --color-bg: #FFFFFF;
  --color-surface: #F1F5F9;
  --color-card: #F8FAFC;
  --color-fg: #0F172A;
  --color-muted: #64748B;
  --color-border: #E2E8F0;
  --color-primary: #2563EB;
  --color-accent: #16A34A;
  --color-success: #16A34A;
  --color-warning: #D97706;
  --font-sans: "Inter", system-ui, sans-serif;
}
```

---

## Palette 6. Botanical Warm — human / edu

Workshops, nonprofits, education, community talks. Warm paper, leaf-green headers, terracotta callouts. The friendliest palette here.

### Full token table

| Token | Light (primary) | Dark (evening) | Usage |
|---|---|---|---|
| `bg` | `#FEFCF8` | `#1C1917` | Warm paper |
| `surface` | `#F5F0E6` | `#292524` | Panels |
| `card` | `#FFFDF7` | `#292524` | Cards |
| `fg` | `#1C1917` | `#FAF7F0` | Text |
| `muted` | `#78716C` | `#A8A29E` | Captions |
| `border` | `#E7DFCF` | `#44403C` | Borders |
| `primary` | `#15803D` | `#4ADE80` | Headers, buttons |
| `accent` | `#C2410C` | `#FB923C` | Callouts, one highlight |
| `success` | `#15803D` | `#4ADE80` | Growth, pass |
| `warning` | `#C2410C` | `#FB923C` | Attention |

### Contrast ratios
- `fg / bg` (`#1C1917` on `#FEFCF8`): 15.1:1 — PASS AAA
- `muted / bg` (`#78716C` on `#FEFCF8`): 4.6:1 — PASS AA (barely — keep muted at 14px+)
- `primary / bg` (`#15803D` on `#FEFCF8`): 4.9:1 — PASS AA
- `accent / bg` (`#C2410C` on `#FEFCF8`): 4.5:1 — PASS AA exactly; use for headings/callout borders, not paragraphs

### When to use vs avoid
Use for teaching, onboarding, community updates — anywhere trust matters more than precision. Avoid for dense dashboards (warm backgrounds reduce perceived grid alignment) and for late-night hacker venues (low ambient light washes out cream).

### Font pairing + Google Fonts URL
Headings `Fraunces` warm serif, body `Inter` or `Nunito Sans`, hand-written accents `Caveat` for one annotation per deck maximum.

```html
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600&family=Caveat:wght@500&display=swap" rel="stylesheet" />
```

### Code theme
Shiki `github-light` on white cards. Warm-tinted code backgrounds shift token hues — keep code blocks neutral white even on cream slides.

### Gradient-allowed example
Sunrise wash for the welcome slide:

```css
.hero-botanical {
  background: linear-gradient(180deg, #FEFCF8 0%, #F5F0E6 60%, #EDE5D3 100%);
}
```

### Tailwind v4 @theme snippet
```css
@theme {
  --color-bg: #FEFCF8;
  --color-surface: #F5F0E6;
  --color-card: #FFFDF7;
  --color-fg: #1C1917;
  --color-muted: #78716C;
  --color-border: #E7DFCF;
  --color-primary: #15803D;
  --color-accent: #C2410C;
  --color-success: #15803D;
  --color-warning: #C2410C;
  --font-display: "Fraunces", Georgia, serif;
  --font-sans: "Inter", system-ui, sans-serif;
}
```

---

## WCAG quick-check procedure (10 minutes, before every ship)

1. **Sample three pairs per deck:** `fg/bg`, `muted/bg`, `muted/surface`. These cover 95% of failures. Primary/accent body text is banned, so skip them unless you broke the rule.
2. **Measure with a tool, not your eyes.** Use Chrome DevTools color picker contrast readout, or WebAIM Contrast Checker, or `npx contrast-checker`. Record the three ratios in the PR / speaker notes.
3. **Check code blocks separately.** `code-fg` on `code-bg` must clear 7:1 (code is small). `#E6EDF3` on `#0D1117` is 15.9:1 — the preset pair passes; custom pairs usually fail.
4. **Check the projector worst case.** Drop display brightness to 50%, open the deck in sunlight-adjacent light. If muted captions vanish, promote them to `fg` at 90% opacity instead of `muted`.
5. **Check print.** Print one bento slide and one code slide in grayscale. Card borders must survive; deltas must differ by shape (arrow + sign), not color alone.

```css
/* emergency contrast fix — promote muted without redesigning */
.fix-muted { color: var(--fg); opacity: .82; }
```

## Projector-room advice

- Projectors crush darks and wash lights. Dark decks (`Midnight SaaS`) need 10–15% larger type in projector rooms; light decks (`GitHub Tech`, `Bento Minimal`) survive best.
- Cream/paper backgrounds (`Paper Editorial`, `Botanical Warm`) photograph warm under tungsten stage lights. White-balance your title screenshot before tweeting it.
- Teal (`Teal Serenity`) shifts blue under old bulbs. Verify CTA buttons still read as teal, not navy, on the venue projector during rehearsal.
- Bring a high-contrast fallback: one CSS class that forces `fg #000` on `bg #FFF` with underlined links. If the projector is dying, toggle it and keep talking.

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

## Palette picker (60 seconds)

- Devtools / CLI / evening meetup → Midnight SaaS
- Corporate / API / handout PDF → GitHub Tech
- Story / memoir / design → Paper Editorial
- Pitch / fundraise / launch → Teal Serenity
- Metrics / QBR / experiments → Bento Minimal
- Teach / nonprofit / workshop → Botanical Warm
- Unsure → GitHub Tech light. It never offends and always prints.
