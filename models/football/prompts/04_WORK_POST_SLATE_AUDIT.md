# 04 — Work: Football C / C2 / C3 / C4 / Engine Post-Slate Audit

**Command alias:** `/audit`

Read `models/football/CURRENT_MODEL.md` first.

Also read:
- `models/football/procedures/FOOTBALL_COMPETITION_RELIABILITY_MEMORY.md`;
- `models/football/airtable/FOOTBALL_COMPETITION_RELIABILITY_AIRTABLE.md`;
- `models/football/procedures/FOOTBALL_BURDEN_COMPLETION_SELECTION.md`;
- `models/football/procedures/FOOTBALL_AUDIT_HINDSIGHT_INTEGRITY.md`;
- `models/football/procedures/FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md`;
- `models/football/challengers/football-c4/TEST_PROTOCOL.md`;
- `models/football/airtable/FOOTBALL_C4_AIRTABLE.md`.

Use the model/version that actually produced each historical decision.

## Source hierarchy

1. user bet slip = physical execution truth;
2. Decision States = model decision history;
3. Website Picks = official Football C exposure;
4. Daily Coverage Ledger = frozen board/funnel history.

## Full funnel

For every current board report:

`RAW SENIOR -> HARD EXCLUDED -> OPERATIONAL EXCLUDED -> RESEARCHABILITY EXCLUDED -> CAPACITY DEFERRED -> ADMITTED -> C OFFICIAL BOARD -> FOLLOW/RESERVE/STOP -> C2 SHADOW BOARD -> C3 SHADOW BOARD -> C4 STEP1 SHADOW -> C OFFICIAL ACTION -> C2/C3 SHADOW ACTION -> PYTHON C/C2/C3 + C4 COMPILER -> FT`

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
- C vs C3 ranking/lane differences;
- C vs C3 supported-line differences;
- C3 second-route-role disagreements;
- C3 goal-3/goal-4 funding blocks;
- C3 two-goal endpoint rate;
- C3 false negatives;
- C4 vs C rank/state inversions;
- C4 vs C supported-line disagreement;
- C4-FOCUS two-goal endpoint rate;
- C-FOCUS -> C4-WATCH/PASS false-positive candidates;
- C-PASS/WATCH -> C4-FOCUS false-negative candidates;
- carrier-led winners retained or lost by C4;
- C4 deterministic replay reproducibility;
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
3. never write FT goals, C/C2/C3/C4 result, settlement or P/L into the reliability event;
4. for each affected competition, load the latest 10 countable events;
5. run `models/football/engine/competition_reliability.py`;
6. upsert the `Competition Reliability` summary row (`tbl1KShXxXErUdVKW`);
7. preserve Manual Override unless the user explicitly changed it.

Report state transitions explicitly, for example:

`NEUTRAL -> CAUTION — XI usable 67% over latest 6 checked observations`

or:

`CAUTION -> DEMOTED — third consecutive critical operational failure`

A profitable or high-scoring match cannot rescue a competition from an operational demotion. A losing/low-scoring match cannot cause one.

## Prospective C4 boundary

C4 confirmatory counting starts from the C4 activation merge commit.

C4 has its own five-board Step-1 counter and does not reset or alter C2/C3.

Historical boards have zero confirmatory C4 weight.

For each C4 board audit:
- verify the structured anchors were frozen before outcome;
- verify every anchor carried a non-empty basis;
- verify C4 ranked universe/common evidence basis reconciled with Football C;
- verify the deterministic compiler revision was preserved;
- compare C vs C4 rank/state/supported line;
- count C4-FOCUS two-goal endpoints;
- identify C-FOCUS -> C4-WATCH/PASS false-positive candidates;
- identify C-PASS/WATCH -> C4-FOCUS false-negative candidates;
- track carrier-led winners retained/lost;
- replay the frozen structured input and require the same C4 output.

A board advances the C4 counter only when its full ranked eligible universe was prospectively complete.

C4 has no Step-2 action and therefore no counterfactual betting P/L in this test.

## Prospective C3 boundary

C3 confirmatory counting starts from the C3 activation merge commit.

C3 has its **own** five-board counter and does not reset or alter C2's current test.

Historical two-goal examples are design motivation only and carry zero C3 confirmatory weight.

For each C3 board audit:
- verify C3 fields were frozen before outcome;
- verify C3 supported line was independent of C/C2;
- verify second-route role and funding basis were complete;
- compare C vs C3 same-kickoff ordering;
- count two-goal endpoints among C3-FOLLOW/C3-RESERVE;
- count cases where C/C2 promoted a two-route shape but C3 classified the second route EXCHANGE_ONLY/STATE_DEPENDENT;
- count C3 false negatives where C3 STOP/PASS and the frozen C support cleared;
- preserve C2 metrics separately.

For C3 Board N/5, judge cleanliness on the **ranked eligible universe**:
- an isolated prospectively quarantined HOLD/exclusion outside C/C2/C3 ranking does not block the counter;
- an unresolved fixture that was ranked does block it;
- a missing required competition block / silently omitted eligible fixture does block it because the ranked universe is incomplete.

A contaminated C3 board does not advance C3 Board N/5.

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

## Audit hindsight integrity — mandatory

Every fixture audit must separate:
1. `FROZEN` — immutable prospective state;
2. `OBSERVED` — HT/FT and what actually materialized;
3. `DIAGNOSIS` — evidence-bounded audit classification;
4. `P&L STATUS` — official C model exposure, actual user execution, C2 shadow and C3 shadow separately.

Never retroactively rewrite a frozen grade after seeing the result.

Use only canonical frozen enums. For current Football C:
- `LOW / MEDIUM / HIGH`;
- `WEAK / USABLE / STRONG`;
- `NONE / TWO_SIDED / CARRIER_LED / FORCED_CHAOS / MIXED`.

Never invent `MEDIUM-HIGH`, `LOW-MEDIUM`, `HIGH+`, or similar compound grades.

FT/HT alone may show that a frozen continuation/completion thesis failed to materialize. It does **not** prove what the grade "should have been".

A statement that the pre-match read was wrong requires a specific contemporaneous pre-freeze evidence miss. Otherwise use:
`RETROSPECTIVE HYPOTHESIS ONLY — DO NOT RE-GRADE HISTORICAL STATE`

Scoreline alone also does not prove causal claims such as "they stopped pushing" or "the second route disappeared"; such mechanism claims require contemporaneous match evidence.

## Settlement

Settle exact recorded line/odds only.

Do not assign hypothetical P/L to a PASS/WAIT-no-entry merely because FT crossed an imagined line.

Official C model P/L and actual user P/L are separate:
- official C model P/L uses an official published/reconciled Website Pick/exposure with exact line/odds;
- actual user P/L uses the user's exact bet slip;
- a user not placing an already-published official C pick does not erase the model win/loss;
- a C-BET that failed official publication is an official decision but `NO OFFICIAL EXPOSURE / NO MODEL P&L`.

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
- C3 shadow board preserved separately;
- C4 Step-1 structured shadow preserved separately when prospectively available;
- no C2/C3/C4 overwrite of C fields;
- C4 did not create Step-2 workload, Decision States, Website Picks, live exposure or P/L;
- mandatory post-XI football research;
- tournament-incentive completeness at Step 1;
- tournament-incentive recheck at Step 2;
- live incentive-epoch recomputation after every goal/red card/material table change;
- count and classify `TOURNAMENT INCENTIVE MISS` / `FORMAT DATA MISSING` / `STALE INCENTIVE EPOCH`;
- H2H handling;
- exact quote epoch;
- C official action;
- C2 shadow action;
- C3 shadow action when fixture received Step 2;
- C3 burden-funding fields and shadow lane;
- Python C uses C ranking and Python C2 uses frozen C2 ranking;
- C2 supported burden was independently frozen before paired evaluation;
- Python C/C2/C3 comparison;
- live wait state integrity;
- persistence agreement;
- actual bet-slip reconciliation.

## Required competition coverage audit

For every audited board, verify the Step-0 required competition manifest.

Current protected block:
- `NED_EERSTE_DIVISIE`.

If the block was omitted, SOURCE_BLOCKED, or fixtures disappeared before disposition:

`PROCESS MISS — REQUIRED COMPETITION COVERAGE GAP`

and specifically:

`HANDOFF INCOMPLETE — NETHERLANDS EERSTE DIVISIE COVERAGE GAP`

A missing protected block contaminates the board-level C2/C3 confirmation sample because the eligible ranked universe is incomplete.

A correctly enumerated fixture that was later hard/operational/researchability/capacity excluded with an explicit disposition is not a coverage miss.

## Step-2 deterministic execution audit

For every completed Step-2 decision, verify:
- `Engine Execution Status = EXECUTED_ALL_THREE`; or
- `Engine Execution Status = FAILED_AFTER_ATTEMPT` with an exact technical failure reason and preserved C/C2/C3 inputs.

If a completed Step-2 decision has neither:

`PROCESS MISS — MANDATORY ENGINE VALIDATION NOT EXECUTED`

If the recorded reason is merely no local checkout / GitHub-only access / runtime not prepared, the fallback is invalid:

`PROCESS MISS — ENGINE SETUP SKIPPED, NOT UNAVAILABLE`

Do not change the historical text verdict from this process finding. Preserve any later rerun as a separate audit/validation repair.

## Factor calibration update — mandatory for eligible frozen rows

Read:
- `models/football/procedures/FOOTBALL_FACTOR_CALIBRATION_OBSERVER.md`;
- `models/football/airtable/FOOTBALL_FACTOR_CALIBRATION_AIRTABLE.md`.

For each audited fixture with an eligible prospective calibration row:
1. read the immutable frozen factor vector;
2. append FT Total Goals;
3. settle the exact frozen supported line;
4. append only observed materialization labels;
5. compute Trace Score from the frozen vector;
6. never rewrite any frozen factor.

For calibration runs, analyze only eligible rows. Keep process faults and missing-factor rows out of factor-weight conclusions.

Always report:
- eligible calibration N;
- factor buckets with N < 5 as `INSUFFICIENT SAMPLE`;
- no `OVERWEIGHT CANDIDATE` or `UNDERWEIGHT CANDIDATE` until the observer's prospective thresholds are met.

Before any audit/factor-calibration Python command, execute the common runtime bootstrap with stage=`audit`. Preserve the resulting `FOOTBALL_RUNTIME_EXECUTION_RECORD`.

A missing local checkout, container network/DNS failure, or engine files not yet materialized is setup state—not evidence that Python/GitHub/engine is unavailable.

Use:
`python models/football/engine/factor_calibration_cli.py --input <observations.json>`

The analyzer has zero production authority.

## Output

For every material fixture, first report:
- `FROZEN:` exact state/line/grades/action;
- `OBSERVED:` HT/FT and materialization/settlement facts;
- `DIAGNOSIS:` canonical audit tag + prospectively detectable evidence miss only when proven;
- `P&L STATUS:` official C model exposure/P&L, actual user execution/P&L, C2 and C3 shadows separately.

Then include one `FOOTBALL_AUDIT_RECORD` JSON object using the deterministic audit schema and validate it with:

`python models/football/engine/cli.py audit --input <payload.json>`

The audit is not complete until the machine record passes. If it fails:

`AUDIT RECORD INVALID — DO NOT FINALIZE DIAGNOSIS`

The machine record is specifically intended to reject:
- non-canonical grades such as `MEDIUM-HIGH`;
- retrospective field rewrites;
- ungrounded pre-freeze evidence-miss claims;
- official model P/L without official exposure;
- user P/L without user execution.

Then report slate totals:
- Football C official model P/L;
- actual user P/L;
- C2 shadow counterfactual P/L on exact shadow entries;
- C3 shadow counterfactual P/L only on exact shadow entries actually produced at Step 2;
- C4 **no P/L** — Step-1 comparison only;
- paired C-vs-C2 action matrix;
- paired C-vs-C3 selection matrix;
- paired C-vs-C4 Step-1 state/rank/line matrix;
- C4 replay reproducibility count;
- text-vs-code disagreement counts;
- missed/avoided cases;
- processing time / resumptions / corrections;
- whether C2 remains worth continuing;
- C3 board counter and whether the burden-funding hypothesis remains worth continuing;
- C4 board counter and whether structured semantic compilation remains worth continuing.

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

1. Step 1 contained a **VERIFIED, resolved** format/incentive block before C/C2/C3 classification — merely present LIMITED/UNKNOWN fields fail this check;
2. Step 2 explicitly recorded `tournament_incentive_rechecked=true` **and** `tournament_incentive_recheck_status=VERIFIED` before any action;
3. every material live epoch recomputed incentive before execution;
4. no supported-burden upgrade was justified solely by XI strength while incentive was suppressive/unknown.

Any missing stage is a **process failure even if the eventual result was profitable**.

Classify as:
- `TOURNAMENT INCENTIVE MISS`;
- `FORMAT DATA MISSING`;
- `STALE INCENTIVE EPOCH`;
- `INCENTIVE RESOLUTION BYPASS` — C/C2/C3 state, rank, lane, supported burden, or action created while the applicable block was LIMITED/UNKNOWN.
