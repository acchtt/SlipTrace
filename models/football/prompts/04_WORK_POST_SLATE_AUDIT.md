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

`RAW SENIOR -> HARD EXCLUDED -> RESEARCHABILITY EXCLUDED -> ADMITTED -> C OFFICIAL BOARD -> C2 SHADOW BOARD -> C OFFICIAL ACTION -> C2 SHADOW ACTION -> PYTHON C/C2 -> FT`

Track separately:
- coverage failures;
- researchability exclusions that should have been admitted;
- Work time wasted on weak-data competitions that should have failed the Step-0 researchability gate;
- high-scoring C-PASS false negatives;
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
- C2 shadow board preserved separately;
- no C2 overwrite of C fields;
- mandatory post-XI football research;
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
