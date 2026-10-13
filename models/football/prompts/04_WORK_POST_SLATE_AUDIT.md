# /audit — Football C + C2 post-slate audit

## Active authority

- Football C = official.
- Football C2 = shadow only.
- C3/C4 are historical only.
- Current workflow = V4.
- Active model base = appbzxqXYf0lKfD4P.
- Physical user P/L = Actual Bets — Current only.

Read:

- models/football/CURRENT_MODEL.md
- models/football/procedures/FOOTBALL_C_C2_ACTIVE_PAIR.md
- models/football/procedures/FOOTBALL_AUDIT_HINDSIGHT_INTEGRITY.md
- models/football/procedures/FOOTBALL_MODEL_BET_ACCOUNTING.md
- models/football/airtable/ACTIVE_MODEL_ROUTING.json

## Scope

Audit every recorded assessed fixture that matters to the requested slate,
not only Website Picks or wins/losses.

Current V4 funnel:

SOURCE-VISIBLE FIXTURES
-> EXCLUSIONS / REGISTRY / DISCOVERY
-> GOAL_PRIORITY / visible pending-watch lanes
-> V4_SWEEP_READY
-> ORIGINAL-SOURCE REPLAY + FRESH FULL-COHORT STATUS
-> C+C2 RANK
-> V4_RANK_PERSISTENCE_VERIFIED
-> C+C2 FOOTBALL ASSESSMENT
-> optional OBSERVED QUOTE comparison OR STRICT PRICE DECISION
-> FT
-> model accounting / Actual Bets separately

Old V1–V3 capacity/work_ready/repair/ZIP rules are historical only and apply
only when reconstructing a record genuinely produced by that workflow.

## Source/result reconciliation

For every assessed fixture:

- verify canonical match identity;
- verify regulation-time FT;
- reconcile reassessment epochs without double counting;
- preserve the exact frozen model/version/evidence epoch;
- distinguish model decision, official publication, shadow state and actual
  user bet.

Never infer FT from an in-play score.

## Hindsight integrity

Use the format:

FROZEN:
- exact board/action/support/evidence state.

OBSERVED:
- verified later score/events/settlement.

DIAGNOSIS:
- evidence-bounded model/process/execution diagnosis.

P&L STATUS:
- genuine model exposure/accounting;
- C2 shadow separately;
- actual user P/L separately.

Outcome alone cannot rewrite a frozen state.

A diagnosis that depends mainly on the later result must be labeled:

RETROSPECTIVE HYPOTHESIS ONLY — DO NOT RE-GRADE HISTORICAL STATE

## Current V4 process checks

Check:

- source completeness/provenance;
- correct exclusion/registry/discovery treatment;
- GOAL_PRIORITY qualification vs pending/watch visibility;
- original-source replay at rank;
- fresh full-cohort status and no retroactive prematch rank;
- C/C2 independent supported burdens/policy fields;
- exact Step1 engine-result readback;
- routine /xi verified rank+persistence authority or explicit exception;
- current quote-free football assessment;
- screenshot exact line/odds preserved with zero replacement searches;
- observed quote marked non-executable;
- strict price action only when strict execution requirements actually cleared;
- one Decision State readback;
- official publication only after final freshness/readback check;
- no synthetic WATCH or unresolved WAIT exposure;
- Actual Bets separation.

Routine /xi does not repeat the rank-time source replay.

Started/live analysis uses the same current C/C2 football path. Do not audit a
missing standalone transition state machine as a defect.

## C model audit

Review prospectively frozen C cases for recurring patterns such as:

- false-positive FOCUS/FOLLOW;
- high-scoring false-negative WATCH/PASS/STOP;
- third-goal funding failures;
- O2.5/O2.75 two-goal endpoints;
- O3+ upper-tail failures;
- carrier-led vs two-sided stall behavior;
- same-kickoff rank/lane opportunity cost;
- FOLLOW candidates failing at current XI/price stage;
- O2.25 calibration behavior.

Do not call a lane wrong merely because FT was high/low; identify the
contemporaneous evidence conflict.

## C2 audit

Where C2 genuinely executed prospectively, compare:

- rank/state;
- independently frozen supported burden;
- independent C2 leakage evidence when used;
- quote-policy action;
- WAIT reachability;
- settlement only when actual prospective terms existed.

Do not copy C line/price into C2, and never treat C2-INCOMPLETE as PASS.

## WAIT/WATCH accounting

Current policy:

- WATCH -> no exposure;
- unresolved WAIT -> no exposure;
- confirmed reached WAIT -> reconcile actual confirmed reached terms;
- direct strict BET -> use actual observed executable terms.

Do not create current WAIT_ASSUMED/WATCH_ASSUMED rows.

Historical assumed-exposure rows remain historical and must be labeled rather
than rewritten.

## User P/L

Only user-confirmed Actual Bets — Current rows count.

Do not derive user P/L from:

- C action;
- Website Pick;
- C2 shadow;
- screenshot;
- WATCH;
- WAIT target.

## Competition/process learning

Audit may identify prospective improvements, but any model/filter change must
be proposed/applied prospectively after the audit. Never retroactively mutate
the audited record.

## Output

Report:

- audited window and data coverage;
- V4 funnel counts;
- C official results/diagnoses;
- C2 shadow comparison on valid rows;
- process and execution defects;
- recurring failure modes;
- actual model accounting where terms really existed;
- actual user P/L separately;
- any explicit historical appendix only when requested/relevant;
- evidence limitations.

Do not manufacture missing model executions or prices.
