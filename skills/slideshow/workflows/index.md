# Workflow Index — Map of All Workflows

> Router first, stages second. `workflows/routing.md` picks the path;
> the stage packs below add procedural depth inside that path.
> Never mix procedures across modes (SKILL.md hard rule).

## Route table — authority is `workflows/routing.md` Steps 1–4 (mode + engine + style + workflow). No summary copy lives here.

## When each stage runs — authority is `workflows/routing.md` Step 5 (routing slip) plus the routed workflow's own steps (`generate-deck.md` steps 4/7/10/11 or the `quick-generate.md` sprint). No matrix copy lives here.

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
- `references/verify-checklist.md` — the 15 ship gates every stage resolves to; fail one, do not ship.

## Upgrade and downgrade rules

- Fast path upgrades to the full path when investors, execs, or external clients appear mid-request.
- Fast path upgrades when live code, iframes, or a ninth slide become essential (see `quick-generate.md` triggers).
- Full path never downgrades mid-build; finish the gates, then decide if the next deck earns the fast path.
- Any stage may invoke `governance/failure-recovery.md` on a red gate; recovery never skips its re-verify gate.

## First step for every deck

Fill the routing slip from `workflows/routing.md` step 5, then open the routed workflow —
`generate-deck.md` steps 1–11 or the `quick-generate.md` sprint — and pull in stages as the routed workflow dictates.

## Stage handoff convention

- Each stage ends with a one-line handoff stating what is verified and what runs next.
- Example: `Research done: 6/6 stats sourced, 0 [unverified] — outline may proceed.`
- Copy the handoff into the delivery note so the next stage starts from evidence, not memory.
- Keep the routing slip pinned at the top of the delivery note until the deck ships.
