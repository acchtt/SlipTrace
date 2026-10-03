# 04 — Work: Football C / C2 / Engine Post-Slate Audit

**Command alias:** `/audit`

Read `models/football/CURRENT_MODEL.md` first.

Also read:
- `models/football/procedures/FOOTBALL_COMPETITION_RELIABILITY_MEMORY.md`;
- `models/football/airtable/FOOTBALL_COMPETITION_RELIABILITY_AIRTABLE.md`;
- `models/football/procedures/FOOTBALL_BURDEN_COMPLETION_SELECTION.md`.

Use the model/version that actually produced each historical decision.

## Source hierarchy

1. user bet slip = physical execution truth;
2. Decision States = model decision history;
3. Website Picks = official Football C exposure;
4. Daily Coverage Ledger = frozen board/funnel history.

## Full funnel

For every new dual-track board report:

`RAW SENIOR -> HARD EXCLUDED -> OPERATIONAL EXCLUDED -> RESEARCHABILITY EXCLUDED -> CAPACITY DEFERRED -> ADMITTED -> C OFFICIAL BOARD -> FOLLOW/RESERVE/STOP -> C2 SHADOW BOARD -> C OFFICIAL ACTION -> C2 SHADOW ACTION -> PYTHON C/C2 -> FT`

Track separately:
- coverage failures;
- women's senior top-flight discovery/accounting misses;
- women's top-flight incorrect hard/operational/researchability exclusions versus legitimate capacity deferrals;
- operational exclusions that should have been admitted;
- `xi_expected` predictions that proved wrong;
- competitions repeatedly producing no usable XI/market despite A/B grading;
- capacity-deferred fixtures that would have been operationally useful;
- researchability exclusions that should have been admitted;
- Work time wasted on low-observability competitions that should have failed the Step-0 operational/researchability gates;
- high-scoring C-PASS false negatives;
- C-PASS carrier contradictions where a weak second route hid a high-completion carrier path;
- two-sided stall failures, especially 0-0 / 1-1 / 2-0 outcomes;
- carrier-led clears and carrier-led failures;
- exact-same-kickoff priority inversions;
- FOLLOW/RESERVE/STOP allocation;
- FOLLOW candidates that failed at XI/price;
- RESERVE candidates activated or left unused;
- STOP matches that later scored highly, reported as operational opportunity cost rather than retroactive model error;
- low-scoring C-FOCUS false positives;
- C vs C2 ranking differences under their separate ranking policies;
- C vs C2 supported-line differences;
- C vs C2 exposure differences;
- C2 selection-floor blocks;
- C2 bridge attempts;
- text C vs code C disagreements;
- text C2 vs code C2 disagreements;
- direct C-BET;
- C-WAIT executed/cancelled/not reached;
- actual user execution deviations.

## Competition reliability memory update — mandatory

After process reconstruction and **before** using the audit for future Step-0 selection:

1. write one canonical operational event per observed fixture/epoch to Airtable `Competition Reliability Events` (`tblD0ZHqT772H25Uv`);
2. use only XI, market, team-news, identity/time and Step-2 process outcomes;
3. never write FT goals, C/C2 result, settlement or P/L into the reliability event;
4. for each affected competition, load the latest 10 countable events;
5. run `models/football/engine/competition_reliability.py`;
6. upsert the `Competition Reliability` summary row (`tbl1KShXxXErUdVKW`);
7. preserve Manual Override unless the user explicitly changed it.

Report state transitions explicitly, for example:

`NEUTRAL -> CAUTION — XI usable 67% over latest 6 checked observations`

or:

`CAUTION -> DEMOTED — third consecutive critical operational failure`

A profitable or high-scoring match cannot rescue a competition from an operational demotion. A losing/low-scoring match cannot cause one.

## Confirmatory C2 boundary

Confirmatory C-vs-C2 counting restarts from the **Step-2 fail-closed validator repair activation commit**.

Earlier C2 records remain debugging/history only because at least one comparison-era plumbing fault applied:
- original C2 Step-1 / Football C Step-2 mixing;
- wrong champion declaration;
- Python C2 inheriting Football C's burden-completion ranking;
- C2 supported burden not guaranteed to be independently frozen;
- Step-2 machine decision created without mandatory XI/research/H2H/completion recheck proof or with omitted safety booleans.

Before the repair boundary:
- paired-return metrics = excluded;
- Python C2 agreement metrics = excluded;
- independently unproven C2 burden = `C2 COMPARISON CONTAMINATED`.

The five-board C2 checkpoint remains at zero until that repair activation, then restarts from board 1.

## Settlement

Settle exact recorded line/odds only.

Do not assign hypothetical P/L to a PASS/WAIT-no-entry merely because FT crossed an imagined line.

## Required process checks

- broad-senior completeness;
- every visible senior women's domestic top-flight block was discovered and given a fixture-level disposition;
- women's-top-flight raw/admitted/excluded/deferred/unresolved counters reconcile exactly;
- missing women's top-flight coverage is classified `HANDOFF INCOMPLETE — WOMEN TOP-FLIGHT COVERAGE GAP`;
- operational A/B/C/D disposition present for every surviving senior fixture;
- frozen competition reliability state/reason present for every admitted fixture;
- reliability events contain no FT/predictive/P&L leakage;
- latest affected competition summaries were recomputed from the rolling operational sample;
- admitted count <= 15 and capacity overflow explicitly deferred;
- no C/D fixture entered routine Work without a user exception;
- B-grade fixtures did not receive routine FOLLOW;
- common evidence freeze present;
- C official board preserved;
- follow-through lane preserved separately from C state;
- max 6 FOLLOW / max 4 RESERVE respected;
- max 2 routine FOLLOW per exact scheduled kickoff minute respected;
- burden-completion/continuation/stall fields were frozen prospectively before outcome;
- no retrospective assignment of the new completion fields;
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
- Python C uses C ranking and Python C2 uses frozen C2 ranking;
- C2 supported burden was independently frozen before paired evaluation;
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

1. Step 1 contained a **VERIFIED, resolved** format/incentive block before C/C2 classification — merely present LIMITED/UNKNOWN fields fail this check;
2. Step 2 explicitly recorded `tournament_incentive_rechecked=true` **and** `tournament_incentive_recheck_status=VERIFIED` before any action;
3. every material live epoch recomputed incentive before execution;
4. no supported-burden upgrade was justified solely by XI strength while incentive was suppressive/unknown.

Any missing stage is a **process failure even if the eventual result was profitable**.

Classify as:
- `TOURNAMENT INCENTIVE MISS`;
- `FORMAT DATA MISSING`;
- `STALE INCENTIVE EPOCH`;
- `INCENTIVE RESOLUTION BYPASS` — C/C2 state, rank, follow lane, supported burden, or action created while the applicable block was LIMITED/UNKNOWN.
