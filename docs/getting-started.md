# Getting started with slideshow-master

> Build your first conference-grade HTML deck in five minutes.
> One skill, three engines, seven phases. This guide uses the real
> paths in this repo: `skills/slideshow/SKILL.md`,
> `skills/slideshow/references/`, `skills/slideshow/scripts/`,
> `skills/slideshow/examples/`.

## What you get

- Hybrid engine router: reveal.js 6 for interactive decks,
  Slidev 52 for Markdown-first code decks, Marp CLI 4 for fast text decks.
- Six palettes plus fonts plus code themes in `references/colors.md`.
- Box patterns in `references/layouts.md` plus ready sketches in
  `references/layout-templates/`.
- Motion rules in `references/animations.md`.
- Ship gates in `references/verify-checklist.md`.
- Scripts: `scripts/new-deck-scaffold.sh`, `scripts/verify-images.py`,
  `scripts/export-deck.sh`.
- Starters: `examples/reveal-demo/`, `examples/slidev-demo/`,
  `examples/marp-demo/`.

## 1. Install the skill

No dependencies for the skill itself. Copy the folder, nothing to compile.

### Claude Code

```bash
mkdir -p .claude/skills/slideshow
cp -r skills/slideshow/* .claude/skills/slideshow/
ls .claude/skills/slideshow/SKILL.md
```

Global install instead:

```bash
mkdir -p ~/.claude/skills/slideshow
cp -r skills/slideshow/* ~/.claude/skills/slideshow/
```

### Codex

```bash
mkdir -p .codex/skills/slideshow
cp -r skills/slideshow/* .codex/skills/slideshow/
ls .codex/skills/slideshow/SKILL.md
```

### opencode

```bash
mkdir -p .opencode/skills/slideshow
cp -r skills/slideshow/* .opencode/skills/slideshow/
ls .opencode/skills/slideshow/SKILL.md
```

Alternate opencode path, also discovered:

```bash
mkdir -p .agents/skills/slideshow
cp -r skills/slideshow/* .agents/skills/slideshow/
```

## 2. First deck in five minutes

Pick the reveal starter. It has the widest capability envelope.

```bash
bash skills/slideshow/scripts/new-deck-scaffold.sh reveal my-talk
cd my-talk
ls
```

You now hold a working deck folder with `slides/` plus `assets/`.

Edit the outline first, one line per slide:

```markdown
1. Ship calmly — thesis plus face
2. The stall — p95 412ms chart
3. The fix — shield three lines plus demo shot
4. The proof — three stat cards plus latency chart
5. Try it tonight — command plus URL
```

Build the slides from `references/layout-templates/` sketches.
Start with `title-hero.md`, then `two-column.md`, then `stats.md`,
then `cta-closing.md`.

Copy images into `assets/` and log them:

```bash
cp ~/Pictures/lab.jpg assets/lab.jpg
echo "lab.jpg | Maria Santos, Acme lab | internal use" >> assets/CREDITS.md
python3 ../skills/slideshow/scripts/verify-images.py
```

Serve and click through:

```bash
npx serve . -l 8000
```

Open `http://localhost:8000/`. Check keyboard: Right, Space,
Left, Home, End. Check phone width at `390px`.

## 3. Engine choice summary

| Need | Engine | Starter |
|---|---|---|
| Interactive, morph, iframes, live demos | reveal.js 6 | `examples/reveal-demo/` |
| Markdown-first, live code, Vue team | Slidev 52 | `examples/slidev-demo/` |
| Fast text, clean export, non-dev author | Marp CLI 4 | `examples/marp-demo/` |

Unsure or mixed: default to reveal.js. Full matrix plus version pins
live in `skills/slideshow/references/engines.md`.

Slidev quick run:

```bash
npx slidev slides.md
npx slidev build slides.md --out dist/
npx serve dist/
```

Marp quick run:

```bash
npx marp slides.md -o deck.html --allow-local-files
npx marp slides.md -o deck.pdf --allow-local-files
```

## 4. Verify plus export flow

Run the gates in order. Fail any gate means do not ship.

```bash
python3 ../skills/slideshow/scripts/verify-images.py
grep -rni "lorem\|test test\|untitled" --include="*.md" --include="*.html" .
grep -rni "gradient" --include="*.css" --include="*.html" --include="*.md" . | wc -l
bash ../skills/slideshow/scripts/export-deck.sh reveal
```

What each step proves:

- `verify-images.py`: every `src` under `assets/`, photos `<=400KB`,
  full-bleed `>=1600px` wide, every `<img>` with `alt`.
- Greps: zero filler lines, gradient count `<=1`, fonts `2` plus mono.
- `export-deck.sh`: HTML opens with zero console errors, PDF paginates
  fully, PPTX opens in PowerPoint plus Google Slides.

Fill the ship record from `references/verify-checklist.md`:

```markdown
Deck: my-talk — 12 slides — reveal.js 6
Date: 2026-10-08 · Checker: Ada
Images: 5 local, all <=400KB, credited
Contrast: fg/bg 15.8:1, muted/bg 6.1:1
Notes: 12/12 · Keyboard: pass · Mobile 390px: pass
Export: PDF 12pp clean, console 0 errors
```

## 5. Next steps

- Read `skills/slideshow/SKILL.md` phases 1 to 7 before a real talk.
- Pick one palette from `references/colors.md` and declare it.
- Add one morph moment per section from `references/animations.md`.
- Add speaker notes to every substantive slide.
- Test `prefers-reduced-motion` in DevTools Rendering panel.
- Ship Markdown source beside the built deck for the next editor.
