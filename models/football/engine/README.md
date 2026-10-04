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

Board:

`python models/football/engine/cli.py board --input models/football/engine/examples/board_input.json`

Decision:

`python models/football/engine/cli.py decision --input decision.json`

Mandatory Step-2 triplet:

`python models/football/engine/decision_triplet_cli.py --c c.json --c2 c2.json --c3 c3.json`

For completed Step-2 decisions, the launcher must execute C/C2/C3 through the deterministic engine. Use `decision_triplet_cli.py` to run all three payloads as one fail-closed unit.

Each decision payload also carries the official Football C workload lane plus its authorization:
- `official_follow_lane = FOLLOW / RESERVE / STOP`;
- `step2_authorization = ROUTINE_FOLLOW / RESERVE_ACTIVATED / USER_EXCEPTION`.

Routine FOLLOW and activated RESERVE must match the persisted official lane. STOP requires `USER_EXCEPTION`. The triplet runner rejects mixed authorization across C/C2/C3, preventing a shadow model from silently creating its own Step-2 workload.

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

## Policy-field isolation

The shared assessment carries common route/mechanism evidence. Football C's completion diagnostics are C-owned policy fields:
`completion_mode`, `burden_completion_quality`, `continuation_quality`, `opponent_leakage`, and `burden_stall_risk`.

The adapter requires them for `model=c` and deliberately does not parse or emit them for `model=c2` / `model=c3`. C2 therefore cannot accidentally inherit C's burden-completion labels through the generic parser, while C3 relies on its own funding/control fields.

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
