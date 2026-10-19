# /rank — Football V4 single-C rank

> **Work conversation role — RANK ONLY.** This conversation is dedicated to
> Football C V4 ranking of an explicitly supplied or canonical newest sweep
> receipt. Load this launcher from current SlipTrace main. Verify original
> source replay and full-cohort status, execute the official C rank, and
> persist/verify the ranked board as required by this procedure. Do not run
> a new `/sweep`, issue `/xi` or `/live` verdicts, or conduct a
> post-slate `/audit` in this conversation. If upstream evidence is invalid,
> return the exact blocker and route it to the sweep conversation. A user
> explicitly changing stages requires the other canonical launcher.
> This is the SlipTrace production route, not FOM.


This is the only active /rank procedure.

Apply `../procedures/FOOTBALL_C_G4_EVIDENCE_CONTRACT.md` to explicit completed
G4 claims. Missing evidence and unavailable paths remain checkpointed research;
mixed evidence is distinct from negative evidence. Consume native diagnostics
and QA flags. Bind scope metadata to the original source; never substitute
new competition labels to admit an excluded fixture.

## Runtime availability

A new Work task may not already contain a repository checkout. If shell/Python
is callable, obtain the current SlipTrace checkout and its engine/V4 dependencies
from one revision, read repository authority, and confirm `stage.py --help`
before reporting the runner unavailable. Do not confuse missing files with
missing execution capability. If execution tools genuinely are unavailable,
report that exact limitation and preserve the source/evidence checkpoint; do
not fabricate a native rank result. This setup does not execute a new sweep.

## Input authority

Use one native V4 rank handoff from one of these provenance-preserving routes:

- **Normal-chat native sweep bundle (preferred for new runs):** saved
  `source.json`, `v4_sweep_ready.json`, `rank-handoff.json` and
  `checkpoint.json`, produced by current V4 execution or the original-source
  attestation fallback.
- Original-source replay: `v4-original-source-attested-receipts` artifact,
  containing `<run>-source.json`, `<run>-v4_sweep_ready.json` and its handoff.
- Existing historical **Work-native sweep** artifacts remain acceptable when
  provenance checks pass, but Work acquisition is no longer the default sweep.

For `/rank newest receipt`, resolve the newest canonical sweep handoff for the
requested window/source run, preferably the exact bundle linked by normal
`/sweep`. Verify source hash and receipt integrity. A failed or newer partial
run is an explicit state; never silently substitute an older source run.

The resolver does not search historical runs to substitute a different source
bundle. A failed or partial newest run remains explicit rather than falling back
silently.

A `RESEARCH_PENDING` sweep bundle may rank its verified eligible subset only
as a **PARTIAL** board. The rank response must state the exact upstream pending
count and must not describe the date window as fully ranked. Zero verified
eligible fixtures is not a ranked board. Do not equate `V4_SWEEP_READY` with
completed goal research.

Do not reconstruct receipts from Google Sheets, historical Airtable, or ledger
rows. Do not require the user to manually resubmit fixtures already in the bundle.

## Upstream completeness boundary

Upstream sweep-pending rows and rank-research-pending rows are different states.
If the sweep checkpoint reports unresolved upstream research, /rank may assess
only the verified eligible cohort it actually received and must report:

`PARTIAL — <N> FIXTURES STILL PENDING UPSTREAM SWEEP RESEARCH`

It must preserve those fixture identities for sweep resume, must not convert
them into PASS/WATCH, must not call the window complete, and must not ask the
user to manually resubmit them.

## Mandatory original-source replay and full-cohort status

Before Football C execution:

1. replay unchanged source.json through native V4;
2. require the replayed receipt to match V4_SWEEP_READY;
3. refresh every eligible fixture's kickoff/status;
4. require freshness within the V4 bound;
5. reject changed-kickoff/source fixtures;
6. mark already-started fixtures PREMATCH_WINDOW_CLOSED.

The native CLI is:

python models/football/stages_v4/stage.py --output v4_rank.json rank --sweep v4_sweep.json --source source.json --status-refresh status_refresh.json --c c.json --unranked unranked.json

## Rank cohort

Use the frozen V4 eligible_queue as the **research cohort**, not as the
official board. The queue may contain `GOAL_PRIORITY` and `GOAL_REVIEW` rows;
both require full Football C research, and the review lane carries no positive
certificate assumption. Research the complete cohort in goals-first order,
with priority rows before review rows. Do not silently skip a higher-priority
fixture without an explicit allowed evidence/status reason.

After Football C research, board admission is a separate deterministic step:
only rows frozen as `C-FOCUS` enter the official ranked board. `C-WATCH` and
`C-PASS` remain in the frozen research assessment for audit/review but do not
inflate the official board. There is **no fixed numeric board cap**: every
genuine C-FOCUS survives admission.

No odds quote is required at Step 1.

## Football C research

Freeze current factual football evidence including:

- fixture identity/status/kickoff;
- scoring/allowing evidence;
- home/away routes;
- carrier/chance/failure evidence;
- current team/XI information where available;
- endpoint/control risk;
- H2H only when materially transferable;
- tournament format/incentive where applicable;
- fourth/fifth/sixth-goal evidence where higher burden needs it;
- upper-tail transferability grade + basis whenever independent_upper_tail=true;
- frozen V4 priority, mean 3+, mean 4+, and low-draw trap.

C additionally owns completion mode, burden completion, continuation,
opponent leakage and stall risk.

### Mandatory G4 research completeness

Whenever G3 is funded, do not freeze O2.50 merely because the first research
pass has already found enough evidence for goal three. Persist exactly one:

- `G4_RESEARCH_INCOMPLETE`
- `G4_RESEARCH_COMPLETE_REJECTED`
- `G4_RESEARCH_COMPLETE_FUNDED`

Use `G4_NOT_APPLICABLE` only when G3 itself is not funded.

A complete G4 assessment must explicitly research and freeze:

- `g4_carrier_path = SUPPORTED / FAILED / UNAVAILABLE / NOT_APPLICABLE`;
- `g4_distributed_path = SUPPORTED / FAILED / UNAVAILABLE / NOT_APPLICABLE`;
- `g4_reply_path = SUPPORTED / FAILED / UNAVAILABLE / NOT_APPLICABLE`;
- `g4_continuation_after_g3 = HIGH / MEDIUM / LOW / UNAVAILABLE / NOT_APPLICABLE`;
- a non-empty `g4_research_basis` explaining the prospective result.

The paths mean single-team four-goal completion, distributed 2+2/3+1 completion,
and opponent-reply-assisted completion. Continue to apply the existing
upper-tail transferability, comparable-context, failure-resistance and
continuation rules. These fields document whether G4 was actually investigated;
they do not weaken or replace any Football C certificate threshold.

A generic sentence such as "no independently transferable fourth goal
established" is not a complete G4 rejection by itself.

### Bounded G4 completion pass before board finalization

For every provisional `C-FOCUS` row that funds G3, complete one bounded G4
research pass **before** treating the assessment as finished. The pass checks,
once, the plausible:

1. single-carrier four-goal path;
2. distributed 3+1 / 2+2 path;
3. opponent-reply-assisted path;
4. continuation after goal three;
5. upper-tail transferability and nearest comparable context;
6. failure resistance, stall risk and applicable tournament incentive.

Do not stop merely because O2.50 is already funded. Do not use odds or the
market to decide any of these fields.

The pass must finish as either
`G4_RESEARCH_COMPLETE_FUNDED` or
`G4_RESEARCH_COMPLETE_REJECTED`. If the available football evidence still
cannot resolve the G4 investigation, leave the fixture
`G4_RESEARCH_INCOMPLETE`; the native rank stage will checkpoint it as
`G4_RESEARCH_PENDING` and it **must not enter the completed C-FOCUS board**.

This is a bounded completion rule, not an instruction to research indefinitely.
Unresolved evidence remains visible in the resume queue and is retried only on
the normal rank-resume path.

## Ranking contract

Ranking is price-blind and deterministic.

Comparison order:

1. certificate robustness: ROBUST > CONDITIONAL > FRAGILE;
2. highest funded certificate: G6 > G5 > G4 > G3 > none;
3. endpoint/control risk;
4. frozen V4 quantitative goal signal;
5. remaining C football-mechanism quality.

A high raw scoreline history alone is insufficient. Red-card/cup/opponent-level
inflation must not be hidden inside otherwise-HIGH route grades. When C asserts
an independent upper tail, it must freeze:

- upper_tail_transferability = LOW / MEDIUM / HIGH;
- upper_tail_transferability_basis = a prospective explanation of why the
  goal-four-plus evidence does or does not transfer to this matchup.

LOW blocks G4/G5/G6. MEDIUM may fund G4+ when the other deterministic
requirements clear, but the certificate cannot be ROBUST. HIGH preserves the
normal robustness path. The market and the eventual score cannot set this field.

### Comparable-context precedence

Whenever an independent G4+ tail is asserted, also freeze:

- upper_tail_comparable_context_signal = SUPPORTIVE / MIXED / SUPPRESSIVE / UNAVAILABLE;
- upper_tail_comparable_context_basis.

Use the closest available senior context first: same competition/continental
competition, then closely comparable opponent/competition strength, then less
comparable domestic/cup history.

Deterministic precedence:

- SUPPRESSIVE -> effective transferability LOW; G4/G5/G6 blocked;
- MIXED -> effective transferability capped at MEDIUM;
- SUPPORTIVE -> preserve the frozen transferability grade;
- UNAVAILABLE -> preserve a grade only when another current comparable
  mechanism independently supports it. Domestic/cup raw scoring alone cannot
  create HIGH.

Therefore a domestic scoring explosion cannot upgrade a contradictory
continental/same-competition upper-tail sample.

The magnitude of compiled burden is not itself a rank bonus or penalty.

### Post-slate completion calibration

G4 is not funded merely because `independent_upper_tail=true`. Carrier-led G4
requires HIGH route reliability unless both routes are independently STRONG.
Reply-dependent G4 with one STRONG + one USABLE route requires HIGH failure
resistance; two STRONG routes are the explicit alternative.

For G3 robustness, simultaneous MEDIUM burden completion + MEDIUM continuation
caps C at CONDITIONAL. Ranking compares current continuation/completion before
the frozen Step-0 rate signal once robustness and certificate depth are equal.

## Availability symmetry

Availability downgrades a certificate only when it attacks an identified
scoring route. Check replacement creators/scorers, opponent scoring routes,
defensive rotation and mixed effects before lowering the total thesis.

## Supplied market disagreement

Step 1 does not fetch odds. A user-supplied contemporaneous market line may
trigger one football-evidence recheck when materially above C's burden, but
the market never enters the ranking key and never manufactures a certificate.

## Supported burden compiler

Production burden is compiled from Football C goal certificates. G4+ also
requires prospectively transferable upper-tail evidence:

- G3 -> O2.50
- G4 -> O3.50
- G5 -> O4.50
- G6 -> O5.50
- no G3 -> none

Asian .75 lines require the next certificate for a full win.

Research-declared supported_line remains audit metadata only.

## Execute research assessment and admit the board

Run the deterministic Football C assessment once across the researched cohort.

- C is official.
- C2/C3/C4 are retired.
- `C-FOCUS` -> official ranked board.
- `C-WATCH` / `C-PASS` -> retained outside the official board in the frozen research assessment.
- FOLLOW / RESERVE / STOP remains the operational workload lane **inside** C's
  already-frozen football selection; it must not become a second predictive
  selector.
- there is no fixed board-size cap.
- no price or Website Pick is created by /rank.
- every eligible fixture not researched still requires an explicit allowed reason.
  An allowed reason is accounting, not proof that research was completed.

## Complete coverage without repeating research

The sweep `eligible_queue` is a research obligation, not a model selection.
Resolve the entire cohort automatically; do not ask the user to find omitted
matches or submit each one again. Start with the source-backed facts already
in the unchanged sweep/source bundle (recent results, researchability channels,
identity, goal screen). Fetch only missing C facts. Do not reacquire complete
date surfaces or refetch unchanged historical results during rank.

Research in `research_order`. Finish each fixture with C assessment, a verified
status exclusion, or a precise evidence gap. Preserve unknowns without inventing
route grades, treating missing XI as an automatic blocker, or creating PASS.
Evidence sufficiency stays governed by current C; this repair adds no football
threshold and no sweep admission filter.

`unranked.json` still maps match IDs to allowed reason strings. A bare
`RESEARCH_EVIDENCE_MISSING`, `MATCH_NEWS_UNVERIFIED` or budget reason now means
**RESEARCH_PENDING**, never an evidence-backed terminal rejection. To document
an actual evidence limitation, use an object for that match instead:

```json
{
  "example-match-id": {
    "reason": "RESEARCH_EVIDENCE_MISSING",
    "match_id": "example-match-id",
    "missing_fields": ["home_route"],
    "attempts": [{
      "source_url": "https://club.example.org/match-preview",
      "checked_at_utc": "2026-10-17T06:00:00Z",
      "fields_checked": ["home_route"],
      "finding": "This fixture's preview reports availability but no current home creation or service mechanism."
    }],
    "next_action": "Check the current home league match report for service and chance evidence."
  }
}
```

The attempt must be real, fixture-specific, within this sweep/rank epoch, and
cover every named missing field. No minimum number of searches is imposed.
The runtime checks structure/identity/time, not the truth of a fetched page;
the operator must retain honest factual findings. Generic copied notes do not
establish that a source was checked. EVIDENCE_LIMITED remains unresolved and
visible; it is neither WATCH/PASS nor a completed C assessment.

Every new receipt carries:

- `research_coverage`: COMPLETE, EVIDENCE_LIMITED or INCOMPLETE plus reconciled
  assessed/pending/evidence-limited/status-excluded counts;
- `coverage_manifest`: the disposition of every eligible fixture;
- `resume_queue`: unresolved fixtures in original research order, including
  reusable sweep facts, exact gaps and next actions;
- `frozen_model_input`: completed C factual input for reuse, including WATCH/PASS;
- `previous_rank_sha256` and `reused_match_ids`: immutable resume lineage.

`research_complete=true` only when every candidate has a C assessment or verified
status exclusion. The official board can still be small or empty. Do not create
extra FOCUS rows to make coverage look complete.

If the rank task genuinely reaches its resource limit, save the native checkpoint
and clearly report the pending count. A receipt with zero C assessments is
`V4_RANK_RESEARCH_PENDING`: a research checkpoint only, no model board/persistence
claim. Do not fabricate an assessment merely to save progress.

### Resume the existing rank task

When `/rank` is repeated for the same sweep, resolve the latest native research
checkpoint automatically alongside its source bundle. Do not require the user
to resubmit individual fixtures. Continue unresolved work first; use the same
canonical launcher and append a new immutable receipt. This is manual invocation
of the existing Work task, not a claim of background automation.

```bash
python models/football/stages_v4/stage.py --output rank-next.json rank --sweep sweep.json --source source.json --status-refresh status-refresh.json --c newly-researched-c.json --unranked updated-gaps.json --resume-from rank-previous.json
```

Supply only newly completed or materially updated C rows in `--c`; it may have
an empty `matches` array on resume. The runtime merges preserved completed rows,
carries unresolved IDs forward, refreshes the whole cohort's status, and removes
closed fixtures from the new board. A newly closed fixture may preserve its
historical assessment only in the earlier receipt. Never recreate prematch
judgment after kickoff. The source hash/run and explicit `authority_commit` must
match. A changed model authority requires revalidation rather than silent reuse.

Reuse factual research, not a stale action. Check changed availability/incentive
facts where relevant and supply a replacement C row when they change. Keep
original source observation times; do not relabel old research as freshly
collected. XI still performs its mandatory current football confirmation.
Legacy receipts without frozen C input are audit material, not resumable native
checkpoints; reuse their sourced facts through an explicitly validated new input.

## Persist once, read back once

For each **official board** fixture persist:

- C state/rank/compiled supported burden;
- C FOLLOW/RESERVE/STOP lane;
- exact Step1 Engine C Result JSON;
- declared line/basis only as audit comparison fields.

WATCH/PASS research rows remain frozen in the rank receipt's research assessment
and board-exclusion trace; they are not persisted as ranked board rows.

Retired C2 fields may remain on historical Airtable rows, but all new rank persistence and independent readback use the Google Sheets `Daily Coverage Ledger` tab.

Then independently refetch once and run:

python models/football/stages_v4/stage.py verify --rank v4_rank.json --readback readback.json

An independently saved complete-cohort board returns
`V4_RANK_PERSISTENCE_VERIFIED`. If any research remains unresolved, it returns
`V4_RANK_PARTIAL_PERSISTENCE_VERIFIED` with the same exact C evidence, source
replay and current-status checks. Both verify the saved assessed board only;
partial never means the cohort is fully researched. Routine XI may consume
already-verified FOCUS rows from a partial board without redoing rank research.

Routine /xi consumes that verified receipt and does not replay
source.json/status_refresh.json again.

## Output

Lead with coverage, e.g. "39 eligible: 10 assessed, 24 pending, 5 status-excluded;
2 FOCUS, 8 WATCH; assessed board persistence verified, research incomplete."
Report the full `coverage_manifest` as a compact fixture/disposition table
alongside the FOCUS board, displayed by actual ICT kickoff/date. Keep full
checkpoint JSON in the saved receipt; read only needed fields and report compact
summaries during Work execution. Do not hide unresolved fixtures or describe them as
C rejection. Resume pending work in the rank task; the user supplies only the
normal command and any genuinely unavailable evidence.

Report run ID, total C-assessed count, official ranked-board count, WATCH/PASS
counts, explicit evidence/status unranked reasons, board exclusions, the
C-FOCUS official board, FOLLOW/RESERVE/STOP for those board rows, supported
burdens and persistence verification. The full research assessment remains
available for audit but is not the main ranked board.

Never invent prices, lineups, rankings or bets.
