# Football C Deterministic Engine — Phase 1

This directory begins the migration from a prose-only football model toward a hybrid coded model.

## Why this exists

Football C still needs an LLM/research layer for tasks that are genuinely semantic:

- interpreting current team news;
- assigning route strength from current football evidence;
- deciding whether H2H is transferable;
- mapping XI changes to mechanisms;
- judging whether live attacking quality is still healthy.

But once those judgments are expressed as structured fields, deterministic rules should not be reinterpreted differently from run to run.

Phase 1 therefore codes:

- the Football C/C2 qualitative data contract;
- deterministic lexicographic ranking;
- C2 selection-quality floor;
- Football C price/burden execution;
- C2 Focus Market-Gap Bridge eligibility;
- WAIT reachability vs negative-information check;
- Asian-total settlement.

## What this does NOT do

It does not:

- manufacture probabilities;
- invent xG from text;
- replace research with arbitrary weights;
- train an ML model;
- automatically become production authority.

The current text model remains authoritative until the coded engine is validated.

## Architecture

```text
web / XI / H2H research
        ↓
LLM produces structured MatchAssessment
        ↓
engine/core.py
        ↓
deterministic rank / floor / execution / settlement
        ↓
audit comparison against text decision
```

## Ranking

The first coded ranking intentionally uses a lexicographic tuple matching the declared Football C/C2 priority rather than a weighted score:

1. route reliability
2. independent route quality
3. carrier strength
4. chance quality
5. failure resistance
6. XI robustness
7. evidence confidence
8. burden protection

This avoids pretending that an unvalidated coefficient such as "route = 35%" is meaningful.

## Structured bridge

Files:
- `schema.json` — contract for board and XI/odds inputs.
- `adapter.py` — strict parser from JSON to engine dataclasses.
- `cli.py` — stdin/file CLI for deterministic board ranking and decisions.
- `examples/board_input.json` — minimal example.

Single board:

`python models/football/engine/cli.py board --input models/football/engine/examples/board_input.json`

Mandatory Step-1 C/C2/C3 board reconciliation:

`python models/football/engine/board_triplet_cli.py --c c.json --c2 c2.json --c3 c3.json`

The triplet runner requires the same ranked eligible universe and exact equality of the common factual evidence across C/C2/C3. Model-owned supported burden/state/funding fields may differ. It rejects common-evidence drift and policy-field leakage before running the three board validators.

Step-1-only C4 structured compiler:

`python models/football/engine/c4_semantic_cli.py --input c4.json --c-board c.json`

C4 consumes prospectively frozen lower-level evidence anchors from the same research epoch, reconciles its match universe and `common_evidence_basis` with Football C, and deterministically compiles route/carrier/quality/control/funding/state/rank. C4 has no Step-2 or exposure authority.

Every board assessment also carries:
- non-empty `common_evidence_basis`;
- model-owned `supported_line_basis`;
- C/C2 `board_state_basis`;
- C3 second-route and forced-chaos bases in addition to the existing funding/control bases.

These are traceability fields with zero independent ranking weight.

Decision:

`python models/football/engine/cli.py decision --input decision.json`

Mandatory Step-2 triplet:

`python models/football/engine/decision_triplet_cli.py --c c.json --c2 c2.json --c3 c3.json`

Mandatory Step-2 session reconciliation:

`python models/football/engine/step2_reconcile_cli.py --input step2_reconcile.json`

For completed Step-2 decisions, the launcher must execute C/C2/C3 through the deterministic engine. Use `decision_triplet_cli.py` to run all three payloads as one fail-closed unit. The session reconciliation then proves every due FOLLOW, activated RESERVE and user exception received exactly one explicit disposition.

Each decision payload also carries the official Football C workload lane plus its authorization:
- `official_follow_lane = FOLLOW / RESERVE / STOP`;
- `step2_authorization = ROUTINE_FOLLOW / RESERVE_ACTIVATED / USER_EXCEPTION`.

Routine FOLLOW and activated RESERVE must match the persisted official lane. STOP requires `USER_EXCEPTION`. The triplet runner rejects mixed authorization across C/C2/C3, preventing a shadow model from silently creating its own Step-2 workload.

### All-model WATCH/WAIT accounting

Run:

`python models/football/engine/model_bet_accounting_cli.py --input model_accounting.json`

One fixture payload contains C/C2/C3/C4. The deterministic ledger applies:

`DIRECT BET > COUNTABLE WAIT > WATCH > NONE`

- WATCH: model's own supported line @1.65, 1u;
- WAIT: C/C2/C3 model-specific target/minimum odds;
- direct BET: exact Step-2 quote;
- C official model-accounting; C2/C3/C4 shadow-only;
- C4 participates through WATCH only because C4 has no Step-2 action policy.

The portable XI runtime exposes the same compiler:

`python xi_portable.py accounting --input model_accounting.json`

### WAIT engine output

A deterministic WAIT keeps `action=WAIT` but also emits:
- `wait_target_line`;
- `wait_min_odds`;
- `model_accounting_status`;
- `model_accounting_line`;
- `model_accounting_odds`;
- `wait_resolution_default`.

For Football C, the default is `WAIT_ASSUMED / ASSUMED_REACHED`; C2/C3 use `SHADOW_WAIT_ASSUMED`. The all-model ledger resolves these together with prospectively frozen WATCH state.

This is accounting only and does not change deterministic state/action selection.

Lack of an already-existing local checkout is not runtime unavailability. If current source is accessible and Python is available, materialize/setup a runnable workspace first.

Only after an actual setup/execution attempt fails may the workflow fall back, and the exact technical reason must be preserved. The generic `ENGINE NOT EXECUTED — STRUCTURED INPUT PRESERVED` fallback is forbidden.

## Validation authority

The coded engine is currently a **shadow validator**, not production authority.

On disagreement:
- preserve prose output;
- preserve coded output;
- preserve exact JSON input;
- label the disagreement;
- do not edit structured fields after seeing the coded result.

This is how we determine whether inconsistency comes from semantic research inputs or from deterministic rule application.

## C4 structured-evidence boundary

C4 does not receive Football C/C2/C3 semantic grades as its authoritative input. It freezes explicit route evidence anchors (creation repeatability, dangerous access, service/finishing continuity, matched leakage, personnel integrity, suppression, multi-goal repeatability) plus match-level coverage/continuation/control/failure/upper-tail anchors.

The C4 compiler contains no weighted score. Its state, supported burden and rank are deterministic decision-tree outputs defined by `FOOTBALL_C4_SPEC.md`.

C4 is intentionally excluded from `decision_triplet_cli.py`, `step2_reconcile_cli.py`, live execution and Website Picks.

## Policy-field isolation

The shared assessment carries common route/mechanism evidence. Step-1 common evidence must be frozen once and reconciled through `board_triplet_cli.py`; three unrelated successful board calls do not prove a clean comparison.

Football C's completion diagnostics are C-owned policy fields:
`completion_mode`, `burden_completion_quality`, `continuation_quality`, `opponent_leakage`, and `burden_stall_risk`.

The adapter requires them for `model=c` and deliberately does not parse or emit them for `model=c2` / `model=c3`. C2 therefore cannot accidentally inherit C's burden-completion labels through the generic parser, while C3 relies on its own funding/control fields.

Step-2 policy recheck proof is also model-owned:
- C requires `completion_rechecked=true`;
- C2 requires `c2_route_quality_rechecked=true`;
- C3 requires `c3_funding_rechecked=true`.

All prematch decision payloads additionally require `fixture_status=PREMATCH_CONFIRMED`, a non-empty `post_xi_research_note`, and `quote_revalidated=true`.

## Next milestones

1. Run structured text-vs-code comparisons on real boards.
2. Measure disagreement frequency and causes.
3. Add board/decision audit storage for the JSON payload/result.
4. Only then consider making deterministic code authoritative for ranking/execution.
5. After enough clean rows, add numerical football features and separately test a statistical probability model.


## Tournament-incentive contract gate

Every structured assessment must explicitly declare whether
`FOOTBALL_TOURNAMENT_INCENTIVE_INTEGRITY.md` applies.

The engine fails closed if `tournament_incentive_required` is omitted.
Applicable tournament/cup/qualifier/final-round fixtures must carry the complete
format/incentive block; ordinary fixtures must explicitly use
`NOT_APPLICABLE`.

At decision time an applicable fixture also requires
`tournament_incentive_rechecked=true`. Otherwise the deterministic adapter
returns:

`DECISION BLOCKED — TOURNAMENT INCENTIVE RECHECK MISSING`

This is an evidence-completeness guard. It does not alter C/C2 predictive
thresholds or make the Python engine production authority.
