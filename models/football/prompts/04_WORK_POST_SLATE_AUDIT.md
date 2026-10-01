# 04 — Work: Football C / C2 / Engine Post-Slate Audit

Read `models/football/CURRENT_MODEL.md` first.

Use the model/version that actually produced each historical decision.

## Source hierarchy

1. user bet slip = physical execution truth;
2. Decision States = model decision history;
3. Website Picks = official Football C exposure;
4. Daily Coverage Ledger = frozen board/funnel history.

## Full funnel

For every new dual-track board report:

`RAW SENIOR -> HARD EXCLUDED -> RESEARCHABILITY EXCLUDED -> ADMITTED -> C OFFICIAL BOARD -> FOLLOW/RESERVE/STOP -> C2 SHADOW BOARD -> C OFFICIAL ACTION -> C2 SHADOW ACTION -> PYTHON C/C2 -> FT`

Track separately:
- coverage failures;
- researchability exclusions that should have been admitted;
- Work time wasted on weak-data competitions that should have failed the Step-0 researchability gate;
- high-scoring C-PASS false negatives;
- FOLLOW/RESERVE/STOP allocation;
- FOLLOW candidates that failed at XI/price;
- RESERVE candidates activated or left unused;
- STOP matches that later scored highly, reported as operational opportunity cost rather than retroactive model error;
- low-scoring C-FOCUS false positives;
- C vs C2 ranking differences;
- C vs C2 exposure differences;
- C2 selection-floor blocks;
- C2 bridge attempts;
- text C vs code C disagreements;
- text C2 vs code C2 disagreements;
- direct C-BET;
- C-WAIT executed/cancelled/not reached;
- actual user execution deviations.

## Confirmatory C2 boundary

Only C2 decisions produced **after the dual-track fix commit** count toward the restarted confirmatory C-vs-C2 comparison.

Earlier C2 records remain debugging/history only because the workflow mixed a C2 Step-1 board with Football C Step-2 and named the wrong champion.

## Settlement

Settle exact recorded line/odds only.

Do not assign hypothetical P/L to a PASS/WAIT-no-entry merely because FT crossed an imagined line.

## Required process checks

- broad-senior completeness;
- common evidence freeze present;
- C official board preserved;
- follow-through lane preserved separately from C state;
- max 6 FOLLOW / max 4 RESERVE respected;
- routine Step 2 did not process STOP matches without explicit exception;
- C2 shadow board preserved separately;
- no C2 overwrite of C fields;
- mandatory post-XI football research;
- tournament-incentive completeness at Step 1;
- tournament-incentive recheck at Step 2;
- live incentive-epoch recomputation after every goal/red card/material table change;
- count and classify `TOURNAMENT INCENTIVE MISS` / `FORMAT DATA MISSING` / `STALE INCENTIVE EPOCH`;
- H2H handling;
- exact quote epoch;
- C official action;
- C2 shadow action;
- Python C/C2 comparison;
- live wait state integrity;
- persistence agreement;
- actual bet-slip reconciliation.

## Output

Report:
- Football C official P/L;
- actual user P/L;
- C2 shadow counterfactual P/L on exact shadow entries;
- paired C-vs-C2 action matrix;
- text-vs-code disagreement counts;
- missed/avoided cases;
- processing time / resumptions / corrections;
- whether C2 remains worth continuing.

Historical Football A/C1 audits remain version-faithful.


## Elite upper-tail observer audit

For prospective `ELITE_UPPER_TAIL_OBSERVER` rows, report separately:

- count of tagged fixtures;
- support line vs recorded market line gaps;
- exact recorded quote settlement;
- frozen-support settlement;
- FT goal distribution;
- failures where the carrier did not self-fund;
- cases where buying extra burden would have helped or hurt.

Do not use the 2026-09-30 motivating cases as confirmatory observations. They are retrospective hypothesis-generation only.


## Tournament-incentive integrity audit

For every fixture where `tournament_incentive_required=true`, verify:

1. Step 1 contained the complete frozen format/incentive block before C/C2 classification;
2. Step 2 explicitly recorded `tournament_incentive_rechecked=true` before any action;
3. every material live epoch recomputed incentive before execution;
4. no supported-burden upgrade was justified solely by XI strength while incentive was suppressive/unknown.

Any missing stage is a **process failure even if the eventual result was profitable**.

Classify as:
- `TOURNAMENT INCENTIVE MISS`;
- `FORMAT DATA MISSING`;
- `STALE INCENTIVE EPOCH`.
