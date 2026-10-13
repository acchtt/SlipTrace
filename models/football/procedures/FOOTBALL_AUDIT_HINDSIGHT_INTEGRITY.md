# Football audit hindsight integrity

## Purpose

Audit frozen Football C/C2 decisions without using later results to rewrite
what was known prospectively.

This is the current audit contract. Historical V1–V3 records must still be
interpreted under the model/workflow version that actually produced them.

## Three-layer record

Every material fixture keeps these layers separate.

### FROZEN

Copy the exact prospective state:

- model/version;
- C board state/rank/lane/supported line;
- C2 shadow state/rank/supported line when lawfully frozen;
- model-owned route/completion/continuation/leakage/stall evidence;
- evidence epoch;
- exact observed/executable quote when one existed;
- C/C2 action;
- WAIT target/minimum and reachability basis when the model actually returned
  WAIT;
- persistence/execution status.

Never rewrite these after kickoff or FT.

### OBSERVED

Record only verified later facts:

- HT/FT regulation score;
- goal/event timing when known;
- settlement of a genuinely recorded exposure;
- whether the frozen football mechanism/continuation did or did not
  materialize;
- actual user execution facts.

Do not infer final score from an in-play screenshot.

### DIAGNOSIS

Classify what the observed result means without changing the frozen state.

Useful tags:

- MODEL FALSE POSITIVE
- MODEL FALSE NEGATIVE
- FOLLOW PRIORITY MISS
- PROCESS MISS
- EXECUTION MISS
- OPERATIONAL OPPORTUNITY COST
- NO OFFICIAL EXPOSURE
- NO RETROSPECTIVE MODEL CHANGE

A later score alone is not proof that a frozen grade should have been
different.

To claim a prospectively detectable model error, identify the pre-freeze
evidence and the rule it contradicted.

Otherwise use:

RETROSPECTIVE HYPOTHESIS ONLY — DO NOT RE-GRADE HISTORICAL STATE

## Causal claims

Scoreline alone does not prove tactical intent, route disappearance or why a
team stopped attacking.

If the causal claim is not supported by contemporaneous event/stat/tactical
evidence, describe only what happened.

Example:

FROZEN: continuation=HIGH.

OBSERVED: 2-0 HT -> 2-0 FT; no third goal.

DIAGNOSIS: MODEL FALSE POSITIVE; continuation did not materialize.
RETROSPECTIVE HYPOTHESIS ONLY for any proposed tactical cause.

## Current exposure and P/L semantics

Keep four things separate:

- model decision;
- official C publication/exposure;
- C2 shadow accounting;
- actual user execution/P&L.

### Direct strict C BET

A genuinely executed/persisted strict C BET may be counted for model
performance at the exact observed executable line/odds.

If publication/exposure itself failed, label that separately.

### WAIT

Current prospective policy:

**unresolved WAIT creates no model exposure and no model P/L.**

A WAIT target is a plan, not proof the line was reached.

Only count a WAIT when reached terms were actually confirmed under the active
accounting contract. Use the confirmed line/odds; do not synthesize the model
minimum price as if it were executed.

Do not create WAIT_ASSUMED or SHADOW_WAIT_ASSUMED for new/current records.

Historical records genuinely frozen under an older assumed-WAIT convention
remain historical artifacts. Do not rewrite them, but label the old accounting
basis explicitly.

### WATCH

WATCH is classification only and creates no synthetic model exposure.

Do not create WATCH_ASSUMED or SHADOW_WATCH_ASSUMED for current records.

### C2

C2 remains shadow-only. A shadow direct decision can be analyzed only when its
actual prospective terms were frozen. C2 never becomes official user exposure.

### Actual user P/L

Physical user P/L comes only from explicit user-confirmed rows in
Actual Bets — Current.

Website Picks, model actions, screenshots, WATCH and WAIT do not prove the user
placed a wager.

## V4 process audit

For current V4 records check:

- complete source-date-surface acquisition/provenance;
- exclusions/registry/discovery correctness;
- source-backed GOAL_PRIORITY qualification;
- original-source replay at /rank;
- fresh full-cohort kickoff/status verification;
- no retroactive prematch ranking;
- C/C2 common factual epoch and independent policy fields;
- exact Step1 persistence/readback;
- routine /xi use of the verified rank+persistence receipt, or explicit
  exception authority;
- quote-free C/C2 football assessment;
- exact screenshot/observed quote preservation with no replacement search;
- canonical observed-quote policy vs strict execution authorization;
- one Decision State persistence/readback;
- strict publication freshness only when an official action was actually
  eligible;
- Actual Bets separation.

Routine /xi does not need to repeat Step1 original-source replay.

Started fixtures use the same current football assessment path. There is no
current standalone kickoff-transition state machine.

## Historical workflow fidelity

For old V1–V3 records, reconstruct only the historical controls that genuinely
existed in that frozen version.

Do not require current V4 to satisfy old work_ready, capacity, repair, ZIP or
replenishment contracts.

Do not backfill C2/C3/C4 decisions that never executed prospectively.

## Settlement

Use the exact frozen line/odds and regulation-time result unless the frozen
market explicitly specified another settlement basis.

Quarter-line settlement must remain exact; e.g.:

- O2.25 with 2 goals = half loss;
- O2.75 with 3 goals = half win/half push;
- O3.0 with 3 goals = push.

## Audit output

For each material fixture show:

FROZEN
OBSERVED
DIAGNOSIS
P&L STATUS

Then report slate-level:

- source/funnel coverage;
- C official results;
- C2 shadow comparison on valid rows;
- process/execution misses;
- recurring model diagnoses;
- model accounting only from genuine prospective terms;
- actual user P/L separately;
- explicit limitations.

Never treat an incomplete/missing shadow execution as PASS or a no-bet.
