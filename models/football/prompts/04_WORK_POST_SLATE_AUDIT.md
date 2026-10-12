# 04 — Work: Football C + C2 Post-Slate Audit

> **ACTIVE MODEL AIRTABLE ROUTING — 2026-10-11 (/audit):** Before the first Airtable model read/write, load `models/football/airtable/ACTIVE_MODEL_ROUTING.md` and `ACTIVE_MODEL_ROUTING.json`. All new model board, C/C2 decision, live, audit, report, calibration, Website Picks and user-verified Actual Bets operations use base `appbzxqXYf0lKfD4P` and its mapped table IDs. Field names must be resolved against the new schema; old record/field/table IDs are never write targets. **The `/sweep` launcher and its Airtable routing are explicitly unchanged**, including existing Step0 handoff receipts. Do not reroute Sweep Runs or rewrite frozen Step0 rows. Model writes require same-base readback with original Coverage/Assessment/Pick/Actual Bet identity. No implicit fallback to legacy base.

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

## V4 production intake audit amendment (2026-10-12)

Current V4 audit funnel is: raw source-visible senior fixtures → hard excluded → registered/discovery candidate lane → `GOAL_PRIORITY` / `PENDING_GOAL_RESEARCH` / `PENDING_DISCOVERY` / `PENDING_RESEARCHABILITY` / low-goal watch → authentic `V4_SWEEP_READY` + original-source replay → current fixture-status refreshed C/C2 rank → `V4_RANK_PERSISTENCE_VERIFIED` → XI C/C2 football → screenshot-only conditional price (if supplied) → live/outcome → model accounting separated from confirmed Actual Bets. Old Step0 CAPACITY/8-fixture and `work_ready`/ZIP claims are historical context, not V4 eligibility. The original-source JSON hash is NOT proof of actual external provider acquisition; audit its source provenance independently. Record missed high-scoring unranked fixtures separately from model PASS, without retroactive bets.

## 1. Audit scope

Audit **all recorded assessed matches**, not only LOCK/FOLLOW/Website Pick rows.

Reconstruct the production funnel according to the **workflow generation that
actually produced the record**.

Current V4:
`SOURCE-VISIBLE SENIOR -> HARD EXCLUDED / REGISTERED / DISCOVERY -> GOAL_PRIORITY / PENDING_GOAL_RESEARCH / PENDING_DISCOVERY / LOW-GOAL WATCH -> V4_SWEEP_READY -> ORIGINAL-SOURCE REPLAY + FRESH FULL-COHORT STATUS -> C+C2 RANK -> VERIFIED AIRTABLE READBACK -> XI C+C2 FOOTBALL -> OPTIONAL SCREENSHOT CONDITIONAL PRICE -> LIVE FOOTBALL -> FT -> ACCOUNTING`

Historical V1–V3 only:
`RAW SENIOR -> OPERATIONAL/RESEARCHABILITY -> CAPACITY/REPLENISHMENT -> BOARD -> STEP2 -> LIVE/WAIT -> FT -> ACCOUNTING`

Never audit a V4 record against retired capacity, repaired-ZIP, required-block
or replenishment rules unless that exact field was prospectively frozen by the
historical workflow being reconstructed.

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

For **current V4**, check only:
- provider/source provenance and immutable fixture identity;
- explicit hard exclusions/friendlies;
- registered vs DISCOVERY classification;
- source-backed goal-screen status and pending-research visibility;
- original-source replay integrity;
- complete <=10-minute rank status refresh and no retroactive prematch rank;
- common evidence freeze and tournament-incentive completeness where applicable;
- genuinely independent C/C2 supported burdens and atomic rank execution;
- V4 rank persistence/readback;
- V4 routine /xi provenance chain, or explicit exception authority;
- quote-free C+C2 football execution/readback;
- USER_SCREENSHOT_ONLY exact-price preservation and no replacement market search;
- live football transition and the current no-live-priced-action-engine boundary;
- Website Pick/Decision State reconciliation only for exposures that were genuinely authorized.

For **historical V1–V3** records, additionally audit their then-current
required-competition, women's-coverage, operational viability, capacity,
replenishment, repaired handoff and market-history rules from the frozen
historical epoch. Do not project those controls onto V4.

Market-history handling is mode-specific. For `USER_SCREENSHOT_ONLY`,
`MARKET_HISTORY_NOT_RESEARCHED_USER_SCREENSHOT_ONLY` is the correct
limitation and **not** a process defect. A mandatory market-history attempt
applies only to historical/non-screenshot priced paths that actually required
it.

An all-model exception after the active-roster boundary is successful only when C and C2 both execute/persist from the same evidence epoch.

## 9. Competition reliability memory update — diagnostic for current V4

After process reconstruction, update the operational reliability memory for
diagnostic continuity. Current V4 intake does **not** consume this memory as an
admission/cap/ranking gate, so never claim that an audit update changed a V4
future shortlist. Historical V1–V3 audits retain their original gating
interpretation when reconstructing those frozen epochs.

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
