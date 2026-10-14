# Visual Styles — Index (PPTX palettes)

> One style per deck. Pick at style-lock time, then paste its palette
> into `build.py` and derive the value ramp from it. Never mix palettes
> mid-deck.

## Two tiers — STRONG default, SOFT only on request

Every deck ships in a **STRONG** style unless the user explicitly asks
for light, warm, paper, or minimal. A deck that reads milky or
white-on-white is a FAIL (Gate 13). The SOFT tier exists for people
who ask for it by name — never as the default.

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
| 8 | STRONG | Bento Minimal | Data story, stat blocks | QBRs, experiment readouts | [bento-minimal.md](bento-minimal.md) |
| 9 | STRONG | Glassmorphism | Frosted shapes on deep stage | Product visions, keynote closers | [glassmorphism.md](glassmorphism.md) |
| 10 | SOFT | GitHub Tech | Corporate neutral, flat | API talks, handout PDFs | [github-tech.md](github-tech.md) |
| 11 | SOFT | Paper Editorial | Serif keynote, warm paper | Founder stories, design talks (on request) | [paper-editorial.md](paper-editorial.md) |
| 12 | SOFT | Botanical Warm | Friendly workshop, cream + leaf | Teaching, nonprofits, onboarding (on request) | [botanical-warm.md](botanical-warm.md) |
| 13 | SOFT | Swiss Minimal | Ultra-clean black on white | Manifesto talks, typographic keynotes (on request) | [swiss-minimal.md](swiss-minimal.md) |

## How to pick one (30 seconds)

1. **Default to STRONG.** Never start from cream or white.
2. **Match content to color:** history/revolution/conflict → **Crimson
   Bold**. Engineering/ops/network → **Navy Signal**.
   Education/product/strategy → **Forest Ink**. Live demos or code as
   hero → **Dark Tech**.
3. **Audience second:** evening engineers → Dark Tech or Midnight SaaS.
   Investors → Teal Serenity. Data-heavy execs → Bento Minimal.
4. **SOFT tier only on explicit request.**

## The 1-style-per-deck rule

- Palette, fonts, and ramp are set once in `build.py` and never change
  mid-deck.
- Accent color appears once per slide maximum. Amber, green, and red
  are data signals, never decoration.
- Switching styles mid-deck reads as two decks stapled together. If a
  slide truly needs another palette, convert its content to fit the
  locked style instead.

## Lock checklist (run once per deck)

- Paste the style's BG/INK/ACCENT/ACCENT2/MUTED/CARD hexes into
  `build.py`; derive missing slots from the BG ramp at style lock.
- Map Display → hero/title tiers, Body → body tier
  (`references/tokens.md`); mono lines only.
- Record the style name in the ship record.
