# Workflow Index — Map of All Workflows

> One workflow, five stages. `workflows/generate-pptx.md` is the path;
> the stage packs below add procedural depth inside it.
> Never mix procedures across modes (SKILL.md hard rule).

## The path

- `workflows/generate-pptx.md` — full 11-phase procedure + §quick-build
  for drafts (research capped, motion/verify/ship always full).
- `workflows/stages/topic-research.md` — gap-driven research: 2-source
  rule, version verification, source logs, stop condition.
- `workflows/stages/image-review.md` — photo pipeline: sourcing ladder,
  PIL prep, credits, budgets, verify script.
- `workflows/stages/visual-review.md` — render-by-eye walkthrough of
  the built deck before shipping.
- `workflows/stages/refine-spec.md` — revision rounds: classifying
  feedback and re-running only affected phases.
- `workflows/stages/export-verify.md` — renders + handout PDF checks
  before shipping.
- `workflows/governance/failure-recovery.md` — failure catalog:
  symptom, owning layer, recovery, re-verify gate.
- `references/verify-checklist.md` — the 15 ship gates every stage
  resolves to; fail one, do not ship.

## Upgrade and downgrade rules

- Quick-build upgrades to the full path when investors, execs, or
  external clients appear mid-request.
- Full path never downgrades mid-build; finish the gates, then decide
  if the next deck earns the fast path.
- Any stage may invoke `governance/failure-recovery.md` on a red gate;
  recovery never skips its re-verify gate.

## Stage handoff convention

- Each stage ends with a one-line handoff stating what is verified and
  what runs next.
- Example: `Research done: 6/6 stats sourced, 0 [unverified] — outline
  may proceed.`
- Copy the handoff into the delivery note so the next stage starts
  from evidence, not memory.
