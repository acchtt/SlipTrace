# 04 — Work: Football C + C2 Post-Slate Audit

> **ACTIVE ROSTER (2026-10-06):** Football C is official; Football C2 is the only active shadow challenger. C3 and C4 are retired for new/current execution. Historical C3/C4 rows remain immutable audit history when they were genuinely frozen at the time.

**Command alias:** `/audit`

Read:
- `models/football/CURRENT_MODEL.md`;
- `models/football/procedures/FOOTBALL_C_C2_ACTIVE_PAIR.md`;
- `models/football/procedures/FOOTBALL_COMPETITION_RELIABILITY_MEMORY.md`;
- `models/football/airtable/FOOTBALL_COMPETITION_RELIABILITY_AIRTABLE.md`;
- `models/football/procedures/FOOTBALL_BURDEN_COMPLETION_SELECTION.md`;
- `models/football/procedures/FOOTBALL_AUDIT_HINDSIGHT_INTEGRITY.md`;
- `models/football/procedures/FOOTBALL_MODEL_BET_ACCOUNTING.md`;
- `models/football/procedures/FOOTBALL_WAIT_ASSUMED_EXPOSURE.md`;
- `models/football/procedures/FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md`.

Use the model/version that actually produced each historical decision. Never backfill a model that did not prospectively execute.

## 1. Audit scope

Audit **all recorded assessed matches**, not only LOCK/FOLLOW/Website Pick rows.

Reconstruct the production funnel:

`RAW SENIOR -> HARD EXCLUDED -> OPERATIONAL EXCLUDED -> RESEARCHABILITY EXCLUDED -> CAPACITY DEFERRED -> ADMITTED -> C BOARD -> FOLLOW/RESERVE/STOP -> C2 SHADOW -> STEP2 C+C2 -> LIVE/WAIT -> FT -> ACCOUNTING`

Track process failures separately from predictive/model failures.

A missing C2 result on an all-model/current C+C2 exception is an execution/process defect, not a C2 PASS and not evidence that C2 avoided a loss.

## 2. Source hierarchy

Use:
1. user bet slip / explicit user execution statement for physical execution truth;
2. explicit user statement that a WAIT target never reached;
3. frozen Decision States;
4. Website Picks for official C exposure;
5. Daily Coverage / board ledger for frozen Step-1 state;
6. strong external result sources for FT/regulation result verification.

Regulation time is the settlement basis unless the frozen market explicitly says otherwise.

Do not infer a final score from an in-play score snapshot.

## 3. Frozen-state integrity

### Audit hindsight integrity — mandatory

Every audit record separates:

`FROZEN:`
- model state/rank/lane;
- supported line;
- frozen evidence epoch;
- action/WAIT target/price;
- runtime execution status;
- prospective accounting basis.

`OBSERVED:`
- verified FT/regulation result;
- actual user execution facts;
- later operational observations.

`DIAGNOSIS:`
- evidence-bounded explanation of process/model behavior;
- confidence;
- prospective hypothesis only when justified.

`P&L STATUS:`
- official C model P&L;
- C2 shadow model P&L where lawfully countable;
- actual user P&L separately.

Historical outcome knowledge must never rewrite a frozen board state, line, rank, lane, or action.

If the frozen record is insufficient to support the proposed diagnosis:

`AUDIT RECORD INVALID — DO NOT FINALIZE DIAGNOSIS`

## 4. Result reconciliation

For every recorded assessment:
- verify fixture identity and regulation-time FT;
- reconcile duplicate/reassessment epochs;
- settle only the exposure/accounting row that actually applies;
- keep Website Picks and Decision States from double-counting the same official C exposure;
- distinguish model exposure from actual user exposure.

Asian-total quarter-line examples:
- O2.25 at exactly 2 goals = HALF LOSS / -0.5u at 1u stake;
- O2.75 at exactly 3 goals = HALF WIN / half-win half-push;
- O3.0 at exactly 3 goals = PUSH;
- O2.0 at exactly 2 goals = PUSH.

Do not turn fractional quarter-line P/L into full wins/losses.

## 5. Current C model audit

Audit:
- high-scoring C-PASS false negatives;
- low-scoring C-FOCUS false positives;
- clearing-goal funding quality;
- O2.5/O2.75 two-goal endpoints;
- O3 upper-tail failures;
- completion/continuation/stall classification;
- carrier-led clears and failures;
- two-sided stall failures;
- exact-same-kickoff rank inversions;
- FOLLOW/RESERVE/STOP concentration quality;
- FOLLOW candidates that failed at XI/price;
- RESERVE opportunity cost;
- STOP high scorers as operational opportunity cost, not automatic retroactive model error;
- text-vs-code C disagreements;
- current clearing-goal FOLLOW certification behavior.

Outcome alone is not sufficient to call the original lane/state wrong. Diagnose against frozen evidence.

## 6. C2 shadow audit

For every row with a lawful prospective C2 freeze, compare:
- C vs C2 rank/state;
- independently frozen supported burden;
- selection-quality floor;
- bridge use;
- Step-2 action;
- WAIT behavior;
- settlement/accounting when executable terms were prospectively frozen.

Do not:
- copy C odds/line into C2;
- treat C2-INCOMPLETE as PASS;
- replay C2 using FT/current information;
- manufacture ROI when exact frozen action/price is missing.

C2 remains shadow-only.

## 7. Retired C3/C4 historical records

C3/C4 are not part of current forward QA.

When a historical row genuinely contains a prospective C3/C4 freeze from its active era, it may be:
- preserved;
- settled/reported historically;
- used to explain an old workflow decision.

Use explicit historical accounting mode where required.

Never:
- create a new C3/C4 action;
- include retired models in a current C+C2 completeness requirement;
- count a retrospectively reconstructed C3/C4 result as confirmatory evidence.

## 8. Process-integrity audit

Check:
- Step-0 source/completeness state;
- required competition coverage;
- senior women's top-flight accounting;
- competition reliability cap;
- operational viability grading;
- admission/capacity queue integrity;
- replenishment order;
- tournament-incentive completeness;
- common evidence freeze;
- C/C2 independent supported lines;
- atomic C+C2 engine execution;
- pair persistence;
- Step-2 due-set reconciliation;
- quote revalidation;
- fresh post-XI football research;
- market-history attempt;
- live WAIT integrity;
- Website Pick/Decision State reconciliation.

An all-model exception after the active-roster boundary is successful only when C and C2 both execute/persist from the same evidence epoch.

## 9. Competition reliability memory update — mandatory

After process reconstruction and **before** using the audit for future Step-0 selection:

1. append one canonical operational event per observed fixture/epoch to `Competition Reliability Events`;
2. use only XI, market, team-news, identity/time and Step-2 process outcomes;
3. never use FT goals, settlement or P/L to promote/demote operational reliability;
4. load the latest 10 countable events per affected competition;
5. run `models/football/engine/competition_reliability.py`;
6. upsert the competition reliability summary;
7. preserve manual override unless explicitly changed by the user.

A high-scoring/profitable match cannot rescue operational reliability. A low-scoring/loss cannot demote it by itself.

## 10. Runtime / deterministic audit

Before execution-required audit commands, run `FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md` with stage=`audit`.

Persist the `FOOTBALL_RUNTIME_EXECUTION_RECORD`.

Use deterministic audit/accounting tools only on already frozen evidence. Runtime output is validation/accounting, not permission to alter history.

Current active-model accounting expects C+C2. For historical C3/C4 settlement, set the explicit historical roster mode rather than injecting retired rows into a current payload.

## 11. Factor-calibration observer

For eligible prospectively frozen C observations, update the diagnostic factor-calibration observer.

Rules:
- outcome fields remain blank before FT;
- after FT, only analyze fields genuinely frozen prospectively;
- insufficient sample remains `INSUFFICIENT SAMPLE`;
- calibration observations never silently alter production coefficients/rules.

## 12. Output

Report:
- audited date/window and source coverage;
- board/funnel counts;
- current C results;
- C2 shadow comparison on valid rows;
- process failures/incomplete rows;
- model-level recurring diagnoses;
- competition reliability changes;
- official C model P&L;
- actual user P&L separately;
- any historical retired-model appendix only when relevant;
- exact data/coverage limitations.

Do not produce a leaderboard that treats missing/incomplete shadow rows as PASSes or no-bets unless that was the frozen prospective state.
