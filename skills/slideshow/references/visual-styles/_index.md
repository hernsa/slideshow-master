# Visual Styles — Index (HTML Slideshows)

> One style per deck. Pick at title-slide time, then lock tokens, fonts, and code theme for all slides.

## Two tiers — STRONG default, SOFT only on request

Every deck ships in a **STRONG** style unless the user explicitly asks for light, warm, paper, or minimal. A deck that reads milky, cream, or white-on-white is a FAIL (Gate 21 Theme Lock). The SOFT tier exists for people who ask for it by name — never as the default.

| Tier | Rule |
|---|---|
| **STRONG** | Bold, dark, or deeply saturated. Default for every deck. If unsure, pick by content: history/narrative/classroom → Crimson Bold, engineering/ops → Navy Signal, product/strategy → Forest Ink, live-coding → Dark Tech. |
| **SOFT** | Cream, paper, white, or gentle-neutral. Only when the user explicitly requests warm/light/paper/minimal/editorial. Never the tie-break. |

## All 13 styles

| # | Tier | Name | Vibe | Best for | File |
|---|---|---|---|---|---|
| 1 | STRONG | Crimson Bold | Deep maroon + red, manifesto | History, revolutions, protests, passion talks | [crimson-bold.md](crimson-bold.md) |
| 2 | STRONG | Navy Signal | Deep navy + cyan signal | Command-and-control, ops, network, engineering | [navy-signal.md](navy-signal.md) |
| 3 | STRONG | Forest Ink | Deep green + amber, organic dark | Education, climate, sustainability, product strategy | [forest-ink.md](forest-ink.md) |
| 4 | STRONG | Midnight SaaS | Devtools dark, violet glow | CLI launches, evening meetups | [midnight-saas.md](midnight-saas.md) |
| 5 | STRONG | Dark Tech | Neon on near-black, mono display | Hackathons, infra deep-dives | [dark-tech.md](dark-tech.md) |
| 6 | STRONG | Brutalist | Raw borders, flat color, mono | Zines, protest tech, art-code | [brutalist.md](brutalist.md) |
| 7 | STRONG | Teal Serenity | Clean SaaS pitch, teal CTA | Pitches, investor updates | [teal-serenity.md](teal-serenity.md) |
| 8 | STRONG | Bento Minimal | Data story, stat cards | QBRs, experiment readouts | [bento-minimal.md](bento-minimal.md) |
| 9 | STRONG | Glassmorphism | Frosted cards on deep gradient | Product visions, keynote closers | [glassmorphism.md](glassmorphism.md) |
| 10 | SOFT | GitHub Tech | Corporate neutral, flat | API talks, handout PDFs | [github-tech.md](github-tech.md) |
| 11 | SOFT | Paper Editorial | Serif keynote, warm paper | Founder stories, design talks (on request) | [paper-editorial.md](paper-editorial.md) |
| 12 | SOFT | Botanical Warm | Friendly workshop, cream + leaf | Teaching, nonprofits, onboarding (on request) | [botanical-warm.md](botanical-warm.md) |
| 13 | SOFT | Swiss Minimal | Ultra-clean black on white | Manifesto talks, typographic keynotes (on request) | [swiss-minimal.md](swiss-minimal.md) |

## How to pick one (30 seconds)

1. **Default to STRONG.** Never start from cream or white. If you catch yourself typing `#FEFCF8` or `#FAF9F6` as the base, stop — that is the milky default the skill rejects.
2. **Match content to color:** history/revolution/conflict → **Crimson Bold**. Engineering/ops/network → **Navy Signal**. Education/product/strategy → **Forest Ink**. Live demos or code as hero → **Dark Tech**.
3. **Audience second:** evening engineers → Dark Tech or Midnight SaaS. Investors → Teal Serenity. Data-heavy execs → Bento Minimal.
4. **SOFT tier only on explicit request:** if the user names "light", "warm", "paper", "minimal", or "editorial", open that style file. Otherwise stay STRONG.
5. **Artifact check:** if the deck becomes a printed PDF handout and the user still wants a SOFT look, prefer GitHub Tech or Swiss Minimal over the creamy editorial styles.

## The 1-style-per-deck rule

- Tokens, fonts, and Shiki theme are set once in the title slide and never change mid-deck.
- The single allowed gradient (if the style permits one) appears on exactly one slide type: hero background *or* one chart series, never both.
- Accent color appears once per slide maximum. Amber, green, and red are data signals, never decoration.
- Switching styles mid-deck (e.g. bento numbers in Crimson, then neon code in Dark Tech) reads as two decks stapled together. If a slide truly needs another palette, convert its content to fit the locked style instead.
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
