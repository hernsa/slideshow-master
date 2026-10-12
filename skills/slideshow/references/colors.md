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
- **Max 2 font families + mono for code only.** Single-sourced per-style in `references/visual-styles/*.md` — never duplicated here.
- **Shiki dual themes:** `vitesse-light` / `vitesse-dark` or `github-light` / `github-dark`. Match Shiki theme to `.dark` toggle. Never ship an unstyled gray code block.
- **Borders do work:** 1px `var(--border)` on every card and image. On projectors, borderless white cards on white backgrounds vanish.
- **Success/warning discipline:** green means up-good or pass. Amber means caution or one highlight number. Red means down-bad or danger. Never use green for decoration.
- **Canonical build tokens:** 8pt spacing scale `8/16/24/32/48/64`, radius `16px`, dark-first `#0B1020` + accent `#4F7DF3`. Spacing, type-clamp, and radius base CSS lives in `references/layouts.md` — use that file, do not duplicate its token block here.
- **One page per slide. Always.**

## 6-palette token summary

Per-palette fonts, pairing URLs, usage guidance, Shiki picks, and Tailwind `@theme` snippets live single-sourced in `references/visual-styles/*.md`. The picker lives in `references/visual-styles/_index.md`. This table is the summary only.

| # | Palette | Dark tokens | Light tokens | Best for |
|---|---|---|---|---|
| 1 | Midnight SaaS | `bg #0B1020` `surface #1A2238` `card #141B30` `fg #E8EEF9` `muted #8A93A6` `border #2A3348` `primary #4F7DF3` `accent #9B6BFF` | `bg #F8FAFC` `fg #0F172A` (handout only) | Devtools dark, dashboards, CLI tours |
| 2 | GitHub Tech | `bg #0D1117` `surface #161B22` `fg #E6EDF3` `muted #8B949E` `border #30363D` `primary #4493F8` `accent #A371F7` | `bg #FFFFFF` `surface #F1F5F9` `fg #0D1117` `muted #57606A` `border #D0D7DE` `primary #2563EB` `accent #7C3AED` | Corporate keynotes, docs-led talks |
| 3 | Paper Editorial | `bg #1A1A18` `fg #F2EFE6` (evening variant) | `bg #FAF9F6` `surface #EFEDE6` `card #FFFFFF` `fg #1A1A18` `muted #6B6660` `border #DDD8CC` `primary #B45309` `accent #0F766E` | Essay keynotes, founder stories |
| 4 | Teal Serenity | `bg #0B1F1E` `surface #123836` `card #0F2E2C` `fg #ECFDF5` | `bg #FFFFFF` `surface #F0FDFA` `fg #0F172A` `muted #5F6B7A` `border #CCFBF1` `primary #0D9488` `accent #F59E0B` | Pitches, investor updates |
| 5 | Bento Minimal | `bg #0A0F1E` `surface #151D33` `fg #E8EEF9` `primary #60A5FA` `accent #4ADE80` | `bg #FFFFFF` `surface #F1F5F9` `card #F8FAFC` `fg #0F172A` `muted #64748B` `border #E2E8F0` `primary #2563EB` `accent #16A34A` | Metrics reviews, QBRs |
| 6 | Botanical Warm | `bg #1C1917` `surface #292524` `fg #FAF7F0` `accent #FB923C` | `bg #FEFCF8` `surface #F5F0E6` `card #FFFDF7` `fg #1C1917` `muted #78716C` `border #E7DFCF` `primary #15803D` `accent #C2410C` | Workshops, education, community |

## Contrast fail-points (only list that matters)

- Teal `#0D9488` on `#FFFFFF` is **3.9:1** — FAIL for body, PASS for large text + UI only. Never set paragraphs in teal.
- Green `#16A34A` on `#FFFFFF` is **3.3:1** — large numbers only, labels stay muted.
- `primary` / `accent` body text is banned deck-wide; headings at 18pt+ may use them at 3:1.
- Muted-on-surface fails most often — measure `fg/bg`, `muted/bg`, `muted/surface` on every deck.

## Gradient discipline (global — the only two examples)

```css
.hero-midnight {
  background:
    radial-gradient(1200px 500px at 20% -10%, rgba(79,125,243,.35), transparent 60%),
    radial-gradient(900px 420px at 90% 10%, rgba(155,107,255,.28), transparent 60%),
    #0B1020;
}
```

```css
.bar-primary {
  background: linear-gradient(180deg, #3B82F6 0%, #1D4ED8 100%);
}
```

Per-palette gradient variants are deleted — one hero *or* one bar series per deck, never both. Projector fallback class and rotation usage live in `references/color-usage.md`.

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

## Pastel rotation tokens (light-section cycle)

Five soft fills for light-deck rotation. Ink is specified per fill — never reuse body `muted` on pastels without re-measuring.

```css
:root {
  --pastel-1: #FDE8EF; --ink-on-p1: #581C2C;
  --pastel-2: #FEF3D8; --ink-on-p2: #573B0A;
  --pastel-3: #DFF7EC; --ink-on-p3: #0B3B2C;
  --pastel-4: #E2EFFD; --ink-on-p4: #16294D;
  --pastel-5: #EDE7FB; --ink-on-p5: #2A1E5E;
}
```

Cycle in order 1→5 across consecutive light sections; never repeat adjacent fills. Ink-on-pastel pairs clear 7:1+.

## Dark showcase mode tokens

Near-black stage for product reveals. Gold + white type only — no muted text on stage.

```css
.showcase {
  --stage: #000000;
  --show-gold: #E8C477;
  --show-white: #FFFFFF;
  background: #000000; color: #FFFFFF;
  box-shadow: inset 0 0 220px rgba(232,196,119,.16);
}
.showcase .gold { color: var(--show-gold); }
```

Spotlight glow counts as the deck's one gradient. One gold number per stage slide.

## Oversized display type tier

`h1` clamp caps near 64pt per `references/layouts.md`. Display tier sits above it — single line, tight tracking, one accent word max.

```css
.display { font-weight: 800; letter-spacing: -0.04em; line-height: .95; text-wrap: balance; }
.display-96 { font-size: 96pt; }
.display-120 { font-size: 120pt; }
.display-138 { font-size: 138pt; }
```

96pt section openers, 120pt stat reveals, 138pt single-word closers. Never two display lines stacked.

## Blob / arch / circle photo crops

One mask per deck. Masks replace raw rectangles on designed slides.

```css
.mask-blob { border-radius: 38% 62% 55% 45% / 48% 42% 58% 52%; overflow: hidden; }
.mask-arch { border-radius: 50% 50% 0 0 / 38% 38% 0 0; overflow: hidden; }
.mask-circle { border-radius: 50%; aspect-ratio: 1/1; overflow: hidden; }
.mask-blob img, .mask-arch img, .mask-circle img { width: 100%; height: 100%; object-fit: cover; }
```

Named-shape persistence across adjacent slides is the morph anchor — see `references/color-usage.md` rebuild + anchor spec and `references/pptx-motion-language.md`.

## Full-bleed photo + minimal text

Scrim stops only — deep crop/credit rules live in `references/media/images.md`.

```css
.bleed-scrim { background: linear-gradient(180deg, rgba(0,0,0,.55) 0%, rgba(0,0,0,.35) 55%, rgba(0,0,0,.25) 100%); }
.bleed-scrim--heavy { background: linear-gradient(180deg, rgba(0,0,0,.68) 0%, rgba(0,0,0,.45) 60%, rgba(0,0,0,.30) 100%); }
```

Caption + scrim must clear 4.5:1; usage rule (word cap, image-id spec) lives in `references/color-usage.md`.
