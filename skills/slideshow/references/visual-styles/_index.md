# Visual Styles — Index (HTML Slideshows)

> One style per deck. Pick at title-slide time, then lock tokens, fonts, and code theme for all slides.

## All 10 styles

| # | Name | Vibe | Best for | File |
|---|---|---|---|---|
| 1 | Midnight SaaS | Devtools dark, violet glow | CLI launches, evening meetups | [midnight-saas.md](midnight-saas.md) |
| 2 | GitHub Tech | Corporate neutral, flat | API talks, handout PDFs | [github-tech.md](github-tech.md) |
| 3 | Paper Editorial | Serif keynote, warm paper | Founder stories, design talks | [paper-editorial.md](paper-editorial.md) |
| 4 | Teal Serenity | Clean SaaS pitch, teal CTA | Pitches, investor updates | [teal-serenity.md](teal-serenity.md) |
| 5 | Bento Minimal | Data story, stat cards | QBRs, experiment readouts | [bento-minimal.md](bento-minimal.md) |
| 6 | Botanical Warm | Friendly workshop, cream + leaf | Teaching, nonprofits, onboarding | [botanical-warm.md](botanical-warm.md) |
| 7 | Swiss Minimal | Ultra-clean black on white | Manifesto talks, typographic keynotes | [swiss-minimal.md](swiss-minimal.md) |
| 8 | Dark Tech | Neon on near-black, mono display | Hackathons, infra deep-dives | [dark-tech.md](dark-tech.md) |
| 9 | Brutalist | Raw borders, flat color, mono | Zines, protest tech, art-code | [brutalist.md](brutalist.md) |
| 10 | Glassmorphism | Frosted cards on deep gradient | Product visions, keynote closers | [glassmorphism.md](glassmorphism.md) |

## How to pick one (60 seconds)

1. **Audience first:** engineers at night → Midnight SaaS or Dark Tech. Mixed stakeholders → GitHub Tech. Investors → Teal Serenity. Students → Botanical Warm.
2. **Artifact second:** if the deck becomes a printed PDF, eliminate dark-first styles. Keep GitHub Tech, Bento Minimal, Paper Editorial, Swiss Minimal.
3. **Content third:** numbers-heavy → Bento Minimal. Code-heavy → Midnight SaaS, GitHub Tech, Dark Tech. Story-heavy → Paper Editorial, Botanical Warm.
4. **Tie-break:** unsure → GitHub Tech light. It never offends and always prints.

## The 1-style-per-deck rule

- Tokens, fonts, and Shiki theme are set once in the title slide and never change mid-deck.
- The single allowed gradient (if the style permits one) appears on exactly one slide type: hero background *or* one chart series, never both.
- Accent color appears once per slide maximum. Amber, green, and red are data signals, never decoration.
- Switching styles mid-deck (e.g. bento numbers in Botanical, then neon code in Dark Tech) reads as two decks stapled together. If a slide truly needs another palette, convert its content to fit the locked style instead.
- Dark-first styles ship a light handout variant only via the token pairs in their file. Do not invent a third variant.

## Lock checklist (run once per deck)

- Copy the style's `:root` / `.dark` tokens into the deck shell before writing slide one.
- Load the style's Google Fonts URL verbatim; cap at two families plus mono for code.
- Set the Shiki dual theme from the style file and keep code background fixed across modes.
- Record the style name in the deck frontmatter so exports reuse the matching Marp theme.

## Token contract (all styles)

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
}
.slide-inner { max-width: 1120px; margin: 0 auto; padding: 48px; }
img.fit {
  width: 100%; aspect-ratio: 16/9; object-fit: cover;
  border-radius: 16px; border: 1px solid var(--border);
}
```

Each style file overrides this contract with its own values, then adds typography, code theme, one HTML sketch, per-engine notes, and three anti-slop rules.
