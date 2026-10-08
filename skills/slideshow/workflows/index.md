# Workflow Index — Map of All Workflows

> Router first, stages second. `workflows/routing.md` picks the path;
> the stage packs below add procedural depth inside that path.
> Never mix procedures across modes (SKILL.md hard rule).

## Route table (summary of `workflows/routing.md`)

| Request | Mode | Engine bias | Workflow |
|---|---|---|---|
| Tech talk, demo, API walkthrough | tech-talk | reveal.js 6 / Slidev 52 | generate-deck |
| Fundraising, sales pitch, ask + amount | pitch | Marp 4 / reveal.js 6 | generate-deck |
| Workshop, how-to, handout | tutorial | Slidev 52 / Marp 4 | generate-deck |
| Portfolio, gallery, launch | showcase | reveal.js 6 | generate-deck |
| Story-driven keynote | narrative | reveal.js 6 | generate-deck |
| "Fast", "quick", "15 minutes", "draft" | any (fixed style) | Marp 4 first | quick-generate |

## When each stage runs

| Stage file | Full path (`generate-deck.md`) | Fast path (`quick-generate.md`) |
|---|---|---|
| `stages/topic-research.md` | Step 4, before outline — full 2-source rule | Skipped — stats marked `[unverified]` in notes |
| `stages/image-review.md` | Step 7, after scaffold — full hybrid pipeline | Sprint 0:08–0:12 — screenshots + one hero only |
| `stages/visual-review.md` | Step 10, on the built deck — full walkthrough | Sprint 0:08–0:12 — lite subset (images, contrast, placeholders) |
| `stages/refine-spec.md` | After user feedback on outline or built deck | Only if an upgrade trigger fires — else fix-forward |
| `stages/export-verify.md` | Step 11 — full per-engine export + checks | Sprint 0:12–0:15 — HTML + PDF opened once, then ship |
| `governance/failure-recovery.md` | Any red gate — fix at the owning layer | Any red lite gate — fix or upgrade to the full path |

## One line per file

- `workflows/routing.md` — deterministic router: mode + engine + style + workflow tables and the routing slip.
- `workflows/generate-deck.md` — full 11-step quality-bar path for client-facing decks.
- `workflows/quick-generate.md` — 15-minute Marp-first sprint for disposable decks, with explicit skipped gates.
- `workflows/stages/topic-research.md` — gap-driven research: 2-source rule, version verification, source logs, stop condition.
- `workflows/stages/image-review.md` — hybrid image pipeline: sourcing decision, credits, sizing, scrims, verify script.
- `workflows/stages/visual-review.md` — self-review walkthrough of the built deck before export.
- `workflows/stages/refine-spec.md` — revision rounds: classifying feedback and re-running only affected phases.
- `workflows/stages/export-verify.md` — per-engine export commands and post-export checks before shipping.
- `workflows/governance/failure-recovery.md` — failure catalog: symptom, owning layer, recovery, re-verify gate.
- `references/verify-checklist.md` — the 16 ship gates every stage resolves to; fail one, do not ship.

## Upgrade and downgrade rules

- Fast path upgrades to the full path when investors, execs, or external clients appear mid-request.
- Fast path upgrades when live code, iframes, or a ninth slide become essential (see `quick-generate.md` triggers).
- Full path never downgrades mid-build; finish the gates, then decide if the next deck earns the fast path.
- Any stage may invoke `governance/failure-recovery.md` on a red gate; recovery never skips its re-verify gate.

## First step for every deck

Fill the routing slip from `workflows/routing.md` step 5, then open the routed workflow —
`generate-deck.md` steps 1–11 or the `quick-generate.md` sprint — and pull in stages as the table above dictates.

## Stage handoff convention

- Each stage ends with a one-line handoff stating what is verified and what runs next.
- Example: `Research done: 6/6 stats sourced, 0 [unverified] — outline may proceed.`
- Copy the handoff into the delivery note so the next stage starts from evidence, not memory.
- Keep the routing slip pinned at the top of the delivery note until the deck ships.
