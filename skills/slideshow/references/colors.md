# Colors — Tokens + 6 Palettes + Rules

## Base tokens

```css
:root {
  --bg: #FFFFFF;
  --surface: #F1F5F9;
  --fg: #0F172A;
  --muted: #64748B;
  --border: #E2E8F0;
  --primary: #2563EB;
  --accent: #7C3AED;
}
.dark {
  --bg: #0B1020;
  --surface: #1A2238;
  --fg: #E8EEF9;
  --muted: #8A93A6;
  --border: #2A3348;
  --primary: #4F7DF3;
  --accent: #9B6BFF;
}
```

Toggle `.dark` on `<html>` or `body`. All components reference vars, never raw hex.

## Rules

- WCAG: normal text >= 4.5:1, large text (>= 18pt / 14pt bold) >= 3:1. Check `var(--fg)` on `var(--bg)` and `var(--muted)` on `var(--bg)` before shipping.
- 60-30-10: 60% neutral bg, 30% surface, 10% accent max. One accent per slide.
- Max 1 gradient per deck. Never gradient body text. Gradient use: single hero background or one chart series only.
- Banned default: full-bleed purple-blue linear gradient (`#7C3AED` -> `#2563EB` cover slide). Pick a palette below instead.
- Max 2 font families + mono for code only. Example: `Inter` + `Fraunces`, code `JetBrains Mono`.
- Shiki dual themes: `vitesse-light` / `vitesse-dark` or `github-light` / `github-dark`. Match Shiki theme to `.dark` toggle.

## Palettes

### 1. Midnight SaaS — devtools dark
- `bg: #0B1020` / `surface: #1A2238` / `text: #E8EEF9` / `primary: #4F7DF3` / `accent: #9B6BFF`
- When: devtools-dark, dashboards, CLI product tours. Pair with mono code blocks, glowing borders on dark.

### 2. GitHub Tech — corporate neutral
- `bg: #FFFFFF` / `surface: #F1F5F9` / `text: #0D1117` / `primary: #2563EB` / `accent: #7C3AED`
- Alt dark surface: `#161B22` for code slides. When: corporate, docs-led talks, API keynotes.

### 3. Paper Editorial — serif keynote
- `bg: #FAF9F6` / `surface: #EFEDE6` / `text: #1A1A18` / `primary: #B45309` / `accent: #0F766E`
- When: serif keynote, essays, publishing. Headings in serif (`Fraunces`), generous margins, no glow.

### 4. Teal Serenity — startup pitch
- `bg: #FFFFFF` / `surface: #F0FDFA` / `text: #0F172A` / `primary: #0D9488` / `accent: #F59E0B`
- When: startup pitch, clean SaaS story. Teal CTA buttons, amber reserved for one highlight number.

### 5. Bento Minimal — data story
- `bg: #FFFFFF` / `surface: #F1F5F9` / `text: #0F172A` / `primary: #2563EB` / `accent: #16A34A`
- When: data-story, metrics reviews. Bento stat cards, blue bars, green deltas only.

### 6. Botanical Warm — human / edu
- `bg: #FEFCF8` / `surface: #F5F0E6` / `text: #1C1917` / `primary: #15803D` / `accent: #C2410C`
- When: human/edu, nonprofit, workshops. Warm paper bg, leaf-green headers, terracotta callouts.
