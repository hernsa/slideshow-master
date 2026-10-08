# Topic Research — Gap-Driven Research Procedure

> Research serves the outline, not curiosity. Every lookup must resolve
> a planning-critical factual gap from `workflows/generate-deck.md` step 4.
> When the gap list is empty, research is done.

## 1. When this stage runs

- Full path: `generate-deck.md` step 4, after style lock, before the outline approval gate.
- Fast path: skipped — every stat ships marked `[unverified]` in notes (`quick-generate.md`).
- Re-entry: `stages/refine-spec.md` sends stat corrections back here for re-sourcing.

## 2. Extract planning-critical factual gaps

Read the draft outline (one line per slide: title + point + visual) and circle
every claim the audience could challenge in Q&A. Five gap classes:

| Class | Outline example (Acme Q3 talk) | Needs |
|---|---|---|
| Headline stat | "p95 fell 41% in six weeks" | 2 sources + method |
| Money/ratio | "NRR 128%, churn 1.1%" | 2 sources, same period |
| API/flag/version | "`staleWhileRevalidate: 90`" | current docs + installed version |
| Quote/attribution | "Ada: deploy day is routine" | named speaker + date |
| Date/event | "shield rollout week of Aug 4" | changelog or deploy log |

Non-gaps (do not research): vibe copy, transitions, layout choices,
speaker opinions labeled as opinions. Write the gap list one line per gap:

```markdown
GAP-1 stat: p95 412ms → 243ms, six weeks (slide 4)
GAP-2 stat: NRR 128% Q3 (slide 5)
GAP-3 api: shield.enable signature + flag names (slide 6)
GAP-4 version: Slidev export --format pdf in v52 (slide 9)
```

## 3. The 2-source rule

Every headline stat needs two independent sources. Independent means different
pipelines: an edge-log query plus a billing export counts; two screenshots
of the same dashboard do not. Procedure per gap:

1. Source A: the primary record (query id, dashboard URL, export filename, teammate confirm with date).
2. Source B: the corroboration (second query, rerun on a later date, finance sign-off).
3. Record both in the per-slide source log (§5).
4. If source B contradicts A beyond the talk's rounding (41% vs 34%), stop and
   re-pull — never average two disagreeing sources on a slide.

Worked pass on GAP-1:

- A: Acme edge logs, Jun 14 → Sep 2, query `q-8821`, p95 412ms → 243ms (−41%).
- B: billing export Sep 3 reruns the same window at −39%; Jonas confirms the 2pp gap is sampling error.
- Slide copy keeps "−41%" with the caption naming both records.

## 4. Verify APIs, flags, and versions against current docs

Never trust memory for anything executable. Pins live in `references/engines.md`:

| Package | Pin | Verify command |
|---|---|---|
| `reveal.js` | `^6.0.0` | `node -e "console.log(require('reveal.js/package.json').version)"` |
| `@slidev/cli` | `^52.0.0` | `npx slidev --version` |
| `@marp-team/marp-cli` | `^4.1.0` | `npx marp --version` |
| node | `>=20` | `node --version` |

Flag inventory — confirm each in the current docs before the slide claims it:

| Engine | Flags and switches on the slide |
|---|---|
| reveal.js 6 | `?print-pdf`, decktape `--load-pause`, `data-auto-animate` + matching `data-id` |
| Slidev 52 | `export --format pdf/pptx/png`, `build --out`, `v-click` paging in export |
| Marp 4 | `--allow-local-files`, `--bespoke.transition`, `--images png`, `--theme-set` |
| Chromium | `npx playwright install chromium` present before any PDF or PPTX run |

Procedure per API/flag gap:

1. Open the current docs (or `--help` of the installed version) and confirm the flag exists with the exact spelling — e.g. Marp `--bespoke.transition`, `--allow-local-files`; Slidev `export --format pdf`; decktape `reveal` target with `?print-pdf`.
2. Confirm the code snippet runs: paste the ≤12-line slide snippet into a scratch file and execute or typecheck it before it enters the deck.
3. Record doc URL + access date in the source log; docs drift, and the log proves what was true on research day.
4. If docs and installed version disagree, the installed version wins and the slide carries the pinned version number ("Slidev 52").

Worked pass on GAP-3: the `shield.enable({ staleWhileRevalidate: 90 })` call is
checked against the Acme edge-config reference (accessed 2026-10-06) and run once
in staging by Maria — flag names confirmed, staging hit rate logged at 83%.

## 5. Per-slide source log format

Log sources on the slide itself as an HTML comment (per engine below), and put
the speakable provenance in presenter notes. Caption the visible source on
data slides at 14px muted, per Gate 2.

reveal.js — comment inside the `<section>`, provenance in notes:

```html
<section>
  <h2>p95 down 41%</h2>
  <!-- sources: p95 412→243ms — edge logs Jun 14→Sep 2 (q-8821); billing export Sep 3 -->
  <aside class="notes">Say: p95 fell 41% in six weeks. Provenance: query q-8821, rerun 2026-10-06, ±2pp sampling error.</aside>
</section>
```

Slidev — `<!-- -->` comment plus speaker comment on the same page:

```markdown
# p95 down 41%

<!-- sources: p95 412→243ms — edge logs Jun 14→Sep 2 (q-8821); billing export Sep 3 -->

<!--
Say: p95 fell 41% in six weeks. Then: July was ugly — next slide. Provenance: q-8821 ±2pp.
-->
```

Marp — HTML comment on the slide; presenter-note comment per project convention:

```markdown
## p95 down 41%

<!-- sources: p95 412→243ms — edge logs Jun 14→Sep 2 (q-8821); billing export Sep 3 -->

<!-- presenter note: Say the number, pause, then the shield story. Provenance q-8821. -->
```

## 6. The `[unverified]` marking rule

A claim with only one source ships marked `[unverified]` — in notes, never as
fact on the slide. Rewrite the slide copy to match the evidence level:

- One survey wave (n=41) says NPS 72 → notes carry `NPS 72 [unverified — one wave, n=41]`; slide copy reads "NPS holding in the low 70s (early signal)".
- A teammate's memory of the Aug 4 rollout with no deploy log → slide says "early August" with `[unverified]` in notes until the changelog confirms it.
- Estimates are labeled `~` with the method in notes ("~$410 CAC, Blended, CRM export Sep 1, excludes self-serve").
- Fast-path decks mark every stat `[unverified]` in notes by default and fix it only on upgrade.

## 7. Research stop condition

Stop when every gap line resolves to one of two states: sourced twice with a
log entry, or marked `[unverified]` with weakened slide copy. Hard cap: 45 minutes
of lookup per deck — remaining gaps take `[unverified]` and the handoff records
the cap. Research never blocks on nice-to-have context; if the outline does not
need it in Q&A, it is not a gap.

## 8. Handoff

Paste one line into the delivery note: `Research done: 4/4 gaps closed (3 sourced ×2, 1 [unverified]) — outline may proceed.` Keep the gap list and source
logs in the note; the outline gate and `stages/visual-review.md` both re-check them.
