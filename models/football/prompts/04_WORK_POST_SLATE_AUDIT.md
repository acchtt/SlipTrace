# 04 — Work: Football C Post-Slate Audit

Read `models/football/CURRENT_MODEL.md` first. Use the model/version that actually produced each decision.

## Source hierarchy

1. user bet slip = physical execution truth;
2. Decision States = model decision history;
3. Website Picks = official model exposure;
4. Daily Coverage Ledger = frozen board/funnel history.

## Full intake funnel

For each Football C board report:

`RAW SENIOR -> HARD EXCLUDED -> ADMITTED TO C -> C-PASS -> C-WATCH -> C-FOCUS -> C-BET/C-WAIT`

Track separately:
- reasonable senior fixtures missing from the handoff;
- high-scoring C-PASS false negatives;
- low-scoring C-FOCUS false positives;
- C-BET direct;
- C-WAIT reached + executed;
- C-WAIT cancelled — thesis decay;
- C-WAIT never reached;
- actual user execution deviations.

A missing reasonable senior fixture is a **COVERAGE FAILURE**, not a model-ranking miss.

Use FT only after frozen decisions. Never retro-change original C states.

Do not assign hypothetical P/L to C-PASS/C-WAIT-no-entry merely because FT crossed an imagined line. Counterfactual P/L requires an exact contemporaneous frozen quote/action.

## Required checks

- fixture/time identity;
- broad-senior Step-0 completeness;
- C rank/state;
- routes/carrier/supported burden;
- H2H handling;
- XI mechanism;
- mandatory post-XI football research;
- current line/price;
- action;
- WAIT target/reach/cancellation/thesis-health;
- persistence agreement;
- final settlement.

Also report board size/followability, processing time, resumptions/retries, persistence corrections and verdict reversals.

Do not patch Football C from one slate. Repeated evidence for a permanent rule change requires a new prospectively frozen challenger/version.

Historical Football A audits remain version-faithful.
