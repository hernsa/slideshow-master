# AGENTS.md

This file governs how AI agents (opencode, Claude Code, Codex, etc.) work in
this repository.

## Scope

This repo contains exactly one skill, `slideshow`, plus its packaging
(README, reference guides, scripts, demos, docs, CI). Do not add second
skills here — that would dilute the repo's single purpose.

## Conventions

- One skill per folder: `skills/<name>/SKILL.md`. The directory name and the
  frontmatter `name` must match, kebab-case, lowercase alphanumeric with
  single hyphen separators.
- `SKILL.md` frontmatter requires `name` and `description`. Keep the
  description front-loaded with trigger keywords and under ~250 characters.
- Keep `SKILL.md` a lean router (< 150 lines): route table, vocabulary,
  execution discipline, reference map. Push depth into `references/`,
  `workflows/`, `visual-styles/`, `layout-templates/`, `data-graphics/`,
  loaded on demand.
- When adding a guide file, update the matching index (`_index.md` table and
  the sibling index JSON) so the router's reference map stays complete.
- No placeholders, filler text, or unfinished markers in content. Every sketch uses
  concrete demo-universe examples. The only allowed `todo`/`lorem` strings
  are inside the Gate 6 verification grep commands themselves.
- Use relative paths from the skill directory when referencing skill files.
- Slideshow tokens are canonical: inches grid (13.333×7.5in stage,
  0.625in margins, copy x[0.65,5.6]), explicit RGB palette (no theme
  slots), type tiers in pt (hero 54–96 … gloss 11). New styles and
  templates reuse them unless the style explicitly overrides.

## Quality bar

- No hypophora, no filler. Instructions must be actionable and specific.
- No purple-blue AI gradients, no three-equal-card rows
  (see `references/decorations.md` and the style files' anti-slop rules).
- Code samples in demos: max 12 lines, line numbers on, Shiki dual theme.
- User instructions (this file, README, direct requests) take precedence over
  the skill's own guidance.

## Commands

```bash
python scripts/check-repo.py  # frontmatter + index JSONs + Gate 6 (exit 1 on failure)
python -m py_compile skills/slideshow/scripts/verify-images.py  # scripts compile
python -m py_compile skills/slideshow/scripts/verify-pptx.py
python -m py_compile skills/slideshow/scripts/scaffold.py
python -m py_compile skills/slideshow/scripts/render.py
```
