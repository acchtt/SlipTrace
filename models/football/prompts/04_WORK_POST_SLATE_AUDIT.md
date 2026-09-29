# 04 — Work: Football C Post-Slate Audit

Read `models/football/CURRENT_MODEL.md` first.

For decisions made after Football C activation, use `models/football/production/FOOTBALL_C.md` as the production authority.

For older decisions, use the model/version that actually produced them. Never relabel Football A history as Football C.

## Source hierarchy

1. user bet slip = physical execution truth;
2. Decision States = model decision history;
3. Website Picks = official model exposure/persistence surface;
4. Daily Coverage Ledger = frozen board/structural history.

Reconcile disagreements explicitly rather than silently choosing one.

## Football C audit groups

Separate:
- C-BET direct;
- C-WAIT reached + executed;
- C-WAIT cancelled — thesis decay;
- C-WAIT never reached;
- C-PASS;
- actual user execution deviations.

Settle exact recorded line/odds only.

Do not assign hypothetical P/L to held/pass cases merely because FT crossed an imagined line. A counterfactual is valid only when an exact contemporaneous quote and frozen counterfactual action were recorded.

## Required checks

For each material case:
- fixture/time identity;
- frozen C rank/state;
- routes/carrier/supported burden;
- H2H handling;
- XI mechanism;
- mandatory post-XI football research compliance;
- current line/price;
- action;
- WAIT target/reach/cancellation and thesis-health check;
- persistence agreement;
- final settlement.

Audit operational performance too:
- board size and followability;
- time to complete board;
- time from XI/odds to action;
- resumptions/retries;
- persistence corrections;
- verdict reversals.

## Model-change boundary

Do not patch Football C from one slate or a memorable result.

If repeated evidence suggests a permanent threshold/rule change, create a new challenger/version prospectively under the QA procedure.

## Output

Report:
- actual exposure P/L;
- model official P/L;
- direct vs WAIT results;
- C-PASS/C-WAIT opportunity observations separately;
- process/compliance faults;
- repeated failure modes;
- whether evidence is sufficient to propose a new challenger.

Historical Football A audits must remain version-faithful.
