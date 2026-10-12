# Tokens — single source

> One page per slide. Paste this base once per deck, then paste any pattern from `references/layouts.md` or `references/layout-templates/`. Canonical: 8pt spacing, 16px radius, dark-first.

```css
:root {
  --space-1: 8px; --space-2: 16px; --space-3: 24px;
  --space-4: 32px; --space-5: 48px; --space-6: 64px;
  --radius-card: 16px; --radius-pill: 999px;
  --bg: #0B1020; --surface: #131A2E; --card: #131A2E;
  --border: rgba(148, 163, 184, .22); --muted: #94A3B8;
  --primary: #4F7DF3; --success: #16A34A;
}
.slide-inner { max-width: 1120px; margin: 0 auto; padding: 48px; }
h1 { font-size: clamp(2rem, 5vw, 3.5rem); letter-spacing: -0.02em; line-height: 1.05; }
h2 { font-size: clamp(1.5rem, 3vw, 2.25rem); letter-spacing: -0.015em; line-height: 1.15; }
.lead { font-size: 1.2rem; opacity: .8; max-width: 60ch; }
img.fit { width: 100%; aspect-ratio: 16/9; object-fit: cover; border-radius: 16px; border: 1px solid var(--border); }
.eyebrow { font-size: .8rem; letter-spacing: .12em; text-transform: uppercase; opacity: .65; }
.tnum { font-variant-numeric: tabular-nums; }
```

Spacing `8 / 16 / 24 / 32 / 48 / 64`. Type `h1 clamp(2rem,5vw,3.5rem)`, `h2 clamp(1.5rem,3vw,2.25rem)`, body `17-19px`, captions `14px`. Skill path: `skills/slideshow/references/tokens.md`.
