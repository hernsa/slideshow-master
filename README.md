# slideshow-master

Universal agent skill for modern HTML slideshows. Hybrid Engine Router: reveal.js / Slidev / Marp.

## Install
- Claude Code: copy `skills/slideshow/` → `.claude/skills/slideshow/`
- opencode: copy `skills/slideshow/` → `.opencode/skills/slideshow/` (or `.agents/skills/slideshow/`)
- Codex: copy `skills/slideshow/` → `.codex/skills/slideshow/`

## Router
| Need | Engine |
|---|---|
| Interactive / morph / iframes | reveal.js (`skills/slideshow/examples/reveal-demo/`) |
| Markdown-first / live code | Slidev (`skills/slideshow/examples/slidev-demo/`) |
| Fast text / clean export | Marp (`skills/slideshow/examples/marp-demo/`) |

## Workflow
Intake → Design Read → Research → Images → Route → Build → Verify+Export. See `skills/slideshow/SKILL.md`.
