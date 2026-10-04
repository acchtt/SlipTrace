# Current Football Model

**Active official model:** Football **C**  
**Shadow challengers:** Football **C2**, Football **C3**, and Football **C4** (Step-1-only structured-evidence challenger)  
**Effective:** 2026-09-29 ICT  
**Fixture authority:** AiScore  
**Operational timezone:** Asia/Ho_Chi_Minh (ICT, UTC+7)

This file is the canonical entry point for all new football work.

## Short command router

Read `models/football/prompts/COMMAND_ALIASES.md`.

When the first token of a user message is a recognized short alias, route it directly:

- `/sweep` -> `00_NORMAL_CHAT_AISCORE_FETCH.md`
- `/rank` -> `01_WORK_DAILY_SWEEP.md`
- `/xi` -> `02_NORMAL_CHAT_XI_ODDS.md`
- `/live` -> `03_NORMAL_CHAT_LIVE.md`
- `/audit` -> `04_WORK_POST_SLATE_AUDIT.md`
- `/report` -> `06_NORMAL_CHAT_REPORT.md`
- `/help` -> show the alias cheat sheet only

Everything after the alias is an argument to that launcher and same-message attachments are launcher inputs.

The aliases are an ergonomic routing layer only. All canonical model/integrity rules remain unchanged, and the old explicit launcher-file form remains valid.

## Model authority

- **Football C** is the only official production model.
- **Football C2** is a frozen shadow challenger only. It may never create a Website Pick or authorize real exposure.
- **Football C3** is a separate burden-funding shadow challenger only. It may never create a Website Pick or authorize real exposure.
- **Football C4** is a prospective structured-evidence challenger for Step 1 only. It may never create Step-2 workload, a Website Pick, live exposure, or real exposure. When a fixture reaches `/xi`, its prospectively frozen C4 Step-1 snapshot must still be shown for comparison; this visibility is not a C4 Step-2 action.
- **Python deterministic engine** is a shadow validation layer for C, C2 and C3; C4 uses the separate deterministic structured-evidence compiler.
- Historical Football A decisions remain historical/rollback only.
- `FOOTBALL_PRE_DECISION_SPEC.md`, `FOOTBALL_STEP2_EXECUTION_SPEC.md`, and `05_NORMAL_CHAT_FOOTBALL_C.md` are retired historical Football A/shadow artifacts and must not control new production.

Do not use a C2, C3 or C4 board as the official input to a Football C decision.

## Active production sequence

`SENIOR AISCORE DISCOVERY -> COMPETITION RELIABILITY MEMORY -> CURRENT OPERATIONAL VIABILITY -> RESEARCHABILITY/CAPACITY GATE -> COMMON FOOTBALL FACT FREEZE -> C4 STRUCTURED ANCHOR FREEZE -> [C BURDEN-COMPLETION + C2 OWN BURDEN + C3 CLEARING-GOAL FUNDING + C4 STRUCTURED COMPILATION] -> [C OFFICIAL BOARD + C2 SHADOW BOARD + C3 SHADOW BOARD + C4 STEP1 SHADOW] -> C SAME-KICKOFF FOLLOW GUARD -> COMMON XI/RESEARCH FACT FREEZE -> [C OFFICIAL ACTION + C2 SHADOW ACTION + C3 SHADOW ACTION + C4 FROZEN STEP1 SNAPSHOT VISIBILITY] -> C OFFICIAL LIVE/WAIT + C2/C3 SHADOW WAIT -> AUDIT`

The comparison must isolate **policy differences**, not accidental research differences.

## Shared evidence rule

For each fixture/epoch, perform the football research once and freeze a common semantic evidence object before any model applies its policy.

Common factual evidence includes:
- fixture identity/status;
- home/away route strength;
- carrier strength/self-fund state;
- continuation evidence;
- opponent leakage;
- chance quality;
- failure mode / suppression state;
- relevant H2H transferability;
- `tournament_incentive_required`;
- competition stage/format, draw resolution, aggregate/table state when applicable;
- home/away incentive state, margin/tiebreak relevance and incentive effect;
- evidence confidence;
- XI mechanism state at Step 2;
- current executable quote at Step 2.

Once frozen, C, C2 and C3 may not change those shared factual fields merely because another model or Python engine disagrees.

C4 consumes the same research epoch but freezes its own lower-level structured evidence anchors before any C4 output is calculated. C4 may not read C/C2/C3 rank, state or supported burden while freezing those anchors.

Model-owned policy fields are then derived separately:
- Football C: completion mode/quality, continuation grade, stall risk and C supported line;
- Football C2: independently frozen C2 supported line and frozen C2 route-quality ranking policy.
- Football C3: independently frozen C3 supported line, second-route role, goal-3/goal-4 funding source/basis, control-endpoint risk and C3 forced-chaos verification.
- Football C4: deterministic route/carrier/quality/control/funding compilation from the separately frozen structured evidence anchors in `FOOTBALL_C4_SPEC.md`.

C2 must not inherit C's supported line or C's burden-completion ranking key.
C3 must not inherit C/C2 supported lines, C completion labels, or C2 route-quality ranking. Two-sidedness has no positive C3 value by itself.

The deterministic adapter enforces the same ownership boundary: C-owned `completion_mode`, `burden_completion_quality`, `continuation_quality`, `opponent_leakage`, and `burden_stall_risk` are mandatory for `model=c` but are not parser requirements or output fields for `model=c2` / `model=c3`.

Semantic verdict-changing declarations must also follow `models/football/procedures/FOOTBALL_SEMANTIC_DECISION_BASIS.md`. Bare booleans/states are insufficient: H2H, carrier self-funding, independent upper-tail, failure-route attack, material suppression, thesis state, primary-mechanism integrity, WAIT reachability/negative-info dependence and material veto each carry a contemporaneous non-empty evidence basis. These basis fields have zero independent predictive weight.

## Required competition coverage invariant

Step 0 must run `models/football/procedures/FOOTBALL_REQUIRED_COMPETITION_COVERAGE.md` in addition to broad discovery.

Current protected manifest version:
`required-competition-manifest-v1`

Protected block:
- `NED_EERSTE_DIVISIE`.

The block must be explicitly checked for every relevant sweep window even when broad discovery does not surface it.

A missing required competition block makes `work_ready=false` and contaminates the board for challenger clean-board counting.

This is coverage plumbing only and does not promote a fixture into Football C.

## Step 0 — researchable senior intake

Use:
`models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md`

Before discovery, apply:
`models/football/procedures/FOOTBALL_AISCORE_SOURCE_ACQUISITION.md`

For `/sweep repair ...`, also apply:
`models/football/procedures/FOOTBALL_SWEEP_REPAIR_MODE.md`

Repair mode is a bounded delta over one existing sweep, not a fresh open-ended rediscovery pass. It reuses complete persisted rows, excludes already-started fixtures before deep verification, caps unresolved competition verification at two authoritative attempts, and returns a compact unresolved list rather than continuing indefinitely.

Step 0 must acquire a complete AiScore date universe before fixture-level discovery. If the source gate is SOURCE_BLOCKED, stop once and persist the blocker fingerprint; repeated `/sweep resume` calls with the same fingerprint must not repeat manual reconstruction.

When the authorized LiveScore + Flashscore/Soccerway fallback is active, Step 0 may use `coverage_mode=FALLBACK_PRODUCTION_SCOPE`: keep protected blocks, required competition coverage, senior women's top-flight coverage, and **every plausible A/B senior candidate fixture-exact**; summarize only blocks already demonstrably below the A/B candidate threshold. This is an efficiency/audit-granularity rule only.

The 15-fixture limit applies only to the **initial Work wave**. It must not short-circuit discovery of later A/B candidates. Build and persist the complete deterministic A/B capacity queue first; ranks 16+ remain available for mandatory Step-1 replenishment. Women's rows that started during a prolonged Step-0 repair remain in the women raw manifest as `OPERATIONAL_EXCLUDED — PREMATCH WINDOW CLOSED DURING STEP0`.

Default intake is `RESEARCHABLE_SENIOR_PRODUCTION`.

Step 0 discovers the senior slate, including the mandatory senior women's domestic top-flight class defined by `models/football/procedures/FOOTBALL_WOMENS_TOP_FLIGHT_COVERAGE.md`, applies hard scope exclusions, loads the persistent **competition operational reliability memory** from `models/football/procedures/FOOTBALL_COMPETITION_RELIABILITY_MEMORY.md`, then applies the mandatory current-fixture operational viability gate before the cheap researchability gate.

Every surviving fixture receives a raw current A/B/C/D viability plus explicit XI expectation, market observability and team-news observability. The persistent competition state may only cap/demote that raw grade; it may never promote it.

- A = executable and eligible for normal follow-through.
- B = conditional and may be admitted, but is capped at RESERVE at board time.
- C/D = excluded before Work unless explicitly reopened by the user.
- CAUTION competition history caps raw A to B.
- DEMOTED competition history defaults the fixture to C, with at most one fully clean raw-A probation fixture per competition per sweep admitted as B.
- Step 0 globally ranks the complete A/B operational candidate pool and sends only the first 15 as the **initial Work batch**; overflow is preserved as `OPERATIONAL CAPACITY DEFERRED — STEP0` with a deterministic queue rank.
- The 15-fixture limit is not a terminal slate exclusion. Step 1 must replenish from the deferred queue when STOP/PASS/started/invalid fixtures leave unused FOLLOW/RESERVE capacity.

Protected senior international qualifiers/tournaments and major continental club competitions bypass the ordinary domestic researchability exclusion when identity/time are valid, but not the operational viability declaration.

For ordinary domestic/small blocks, admit only when operational viability is A/B **and** current evidence is sufficient for both teams to support Football C's research schema: recent form, competition context, and at least one usable mechanism/stat/news layer.

## Step 1 — official board + three shadow comparisons

Use:
`models/football/prompts/01_WORK_DAILY_SWEEP.md`

Also apply:
`models/football/procedures/FOOTBALL_STEP1_BOARD_RECONCILIATION.md`

One common research/evidence pass is frozen first. Every ranked fixture carries a non-empty `common_evidence_basis`; each model-owned supported burden carries `supported_line_basis`; C/C2 semantic board states carry `board_state_basis`.

Then:
- Football C creates the **official** C-PASS / C-WATCH / C-FOCUS board.
- Football C2 independently applies its frozen shadow route-quality rules.
- Football C3 independently applies its burden-funding rules and creates C3-PASS / C3-WATCH / C3-FOCUS plus a shadow C3 lane.
- Football C4 compiles its structured Step-1 shadow state/rank/line from its prospectively frozen anchors.
- Python runs model=`c`, model=`c2` and model=`c3` against the reconciled common factual evidence; C4 runs separately through `c4_semantic_cli.py` and reconciles its ranked universe/common evidence basis with the C board.

Football C's board/lane is the only board that controls routine Step-2 workload or official exposure. C2/C3 shadow lanes and the C4 Step-1 shadow never create extra mandatory monitoring.

C/C2/C3 board engine validation must run through `board_triplet_cli.py`, which fails closed on ranked-universe mismatch, common-evidence drift, or model-policy field leakage. A contaminated triplet does not advance C2/C3 prospective counters.

C4 must then run:
`python models/football/engine/c4_semantic_cli.py --input <c4.json> --c-board <c.json>`

The first C4 confirmatory window is the next **5 complete clean Step-1 boards** after the C4 activation merge. C4 starts at **0/5**. C4 counter eligibility is independent of C2/C3.

After each Step-1 wave is frozen, the burden-completion follow-through guard assigns `FOLLOW / RESERVE / STOP`. It compares exact-same-kickoff candidates against each other, caps routine FOLLOW at two per kickoff minute, and does not change the underlying C state. Only FOLLOW receives routine Step-2 attention; RESERVE is conditional; STOP requires explicit override.

### Step-1 capacity replenishment

Operational lane capacity is:
- max FOLLOW = 6;
- max retained RESERVE = 4.

If `FOLLOW + RESERVE < 10` after a completed wave and prematch A/B fixtures remain in the Step0 capacity queue, Step 1 must pull the next deferred fixtures in ascending `Step0 Capacity Queue Rank` and assess them as the next replenishment wave.

Continue until one of these becomes true:
1. FOLLOW + RESERVE reaches 10;
2. no prematch A/B deferred candidate remains;
3. all remaining queued fixtures have started/left the prematch window.

Never choose replenishment candidates using C/C2/C3/C4 score, expected goals, betting appeal, or result knowledge. Queue order was frozen at Step 0 from operational quality only.

This is a workload utilization rule, not a predictive board-size target.

## Mandatory Step-2 market-history attempt

Before final C/C2/C3 action, run `models/football/procedures/FOOTBALL_MARKET_HISTORY_RECHECK.md`.

Attempt:
`OPEN -> PRE-XI -> POST-XI / CURRENT PREMATCH`

Persist FOUND / PARTIAL / UNAVAILABLE_ATTEMPTED plus movement/conflict-recheck status. Market history is a reinspection signal only; it does not create football structure or replace fresh post-XI football research.

## Mandatory deterministic runtime bootstrap

For every execution-required `/rank`, `/xi`, or `/audit` stage, first apply:

`models/football/procedures/FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md`

Tool/repository availability is a **current-turn observed state**, never an inference from environment shape or a prior handoff. The workflow must:
- run a real Python probe;
- probe the connected current repository source for `acchtt/SlipTrace`;
- for `/xi`, fetch the exact-current single-file `xi_portable.py`, run `self-check`, then execute the triplet/reconciliation through it;
- for `/rank` / `/audit`, or XI portable fallback only, materialize the exact-current stage source and run `runtime_probe.py --stage <rank|xi|audit>`;
- attempt the actual stage command;
- preserve a `FOOTBALL_RUNTIME_EXECUTION_RECORD`.

A missing local checkout or container `git clone`/DNS/network failure is not a valid "GitHub unavailable" reason while connector/project source remains accessible.

## Mandatory Step-2 deterministic execution

Before finalizing any completed `/xi` decision, run the deterministic validator for all three tracks under `models/football/procedures/FOOTBALL_ENGINE_EXECUTION_BOOTSTRAP.md` after the common runtime bootstrap.

Required result:
- C validator executed;
- C2 validator executed;
- C3 validator executed.

Preferred XI runner:
`python xi_portable.py triplet --c <c.json> --c2 <c2.json> --c3 <c3.json>`

Before it:
`python xi_portable.py self-check`

Use `decision_triplet_cli.py` only on the documented multi-file fallback path.

Each triplet freezes the same official C workload authorization:
- `official_follow_lane`;
- `step2_authorization = ROUTINE_FOLLOW / RESERVE_ACTIVATED / USER_EXCEPTION`.

The deterministic layer fails closed when authorization and the official C lane disagree. Shadow C2/C3 may compare only an officially authorized Step-2 fixture and never create extra workload.

Before deterministic execution, prematch Step 2 also requires:
- `fixture_status = PREMATCH_CONFIRMED`;
- `quote_revalidated = true`;
- non-empty `post_xi_research_note`;
- model-owned recheck proof: C `completion_rechecked`, C2 `c2_route_quality_rechecked`, C3 `c3_funding_rechecked`.

Lack of an existing local checkout is not execution unavailability. Container network failure is not repository unavailability. The common runtime bootstrap governs source retrieval/materialization and failure evidence.

The old generic `ENGINE NOT EXECUTED — STRUCTURED INPUT PRESERVED` fallback is forbidden.

Only an actual failed setup/execution attempt with a complete `FOOTBALL_RUNTIME_EXECUTION_RECORD` may use:
`ENGINE EXECUTION FAILED — ATTEMPTED — <exact technical reason>`

This is execution plumbing only. Python remains a shadow validator; Football C text remains production authority.

## Step 2 — C/C2/C3 XI actions + C4 frozen Step-1 visibility

Use:
`models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md`

Also apply:
- `models/football/procedures/FOOTBALL_STEP2_SESSION_RECONCILIATION.md`;
- `models/football/procedures/FOOTBALL_WAIT_ASSUMED_EXPOSURE.md`.

At each Step-2 session freeze the due set from official C workload: every due FOLLOW, each activated RESERVE, and each explicit user exception. Every due fixture must receive one recorded disposition; silent omission blocks session completion.

Perform one common XI + mandatory fresh post-XI web-research + H2H update, freeze it, then derive:

- **Football C official:** C-BET / C-WAIT / C-PASS.
- **Football C2 shadow:** C2-BET / C2-WAIT / C2-PASS.
- **Football C3 shadow:** C3-BET / C3-WAIT / C3-PASS when the fixture already receives normal XI/odds assessment.
- **Football C4 Step-1 snapshot:** always display the prospectively frozen C4 state/rank/supported line when available, labeled no Step-2 action.
- **Python C/C2/C3 shadow validation** through the portable XI runtime.

Accounting convention:
- C-BET = direct official model exposure;
- C-WAIT = immediate assumed official model exposure at its deterministic WAIT target/minimum odds;
- C2/C3 WAIT = assumed shadow exposure for challenger P/L only;
- only a matching user slip or an explicit user statement that the line never reached may replace/cancel the C-WAIT assumed exposure.

Only Football C may publish an official Website Pick. Under the current accounting convention both C-BET and C-WAIT publish/reconcile one official Website Pick; C-WAIT retains `Origin C Action = C-WAIT`.

## Live

Use:
`models/football/prompts/03_NORMAL_CHAT_LIVE.md`

Resolve Football C official WAITs normally for live advisory/action purposes, but do not use later market observation to erase the already-created WAIT assumed exposure. Exposure accounting changes only under `FOOTBALL_WAIT_ASSUMED_EXPOSURE.md`: matching user slip or explicit user "line never reached".

Live assessment is independent of provider live-stat telemetry. Do not require or request shots, xG, big chances, dangerous attacks, possession, corners, box entries or momentum before a verdict. Use score/minute/current line/odds, preserved prematch/XI football evidence, concrete material events and tournament incentive when applicable.

If the same fixture also has a predeclared C2-WAIT and/or C3-WAIT, resolve each from the same live state as shadow comparison only. Do not create C3-only live monitoring.

## Factor calibration observer

`models/football/procedures/FOOTBALL_FACTOR_CALIBRATION_OBSERVER.md` is active as a **prospective diagnostic observer only**.

It records frozen factor vectors before outcome and appends outcome labels after FT to diagnose possible over/underweighting.

It has zero authority over Football C/C2 production. No trace score, bucket result, ablation result, or historical settlement may directly change a rank, state, lane, supported burden or action.

Any stable signal must be promoted into a separately versioned challenger and tested prospectively.

## Audit

Use:
`models/football/prompts/04_WORK_POST_SLATE_AUDIT.md`

Also apply:
`models/football/procedures/FOOTBALL_AUDIT_HINDSIGHT_INTEGRITY.md`

Audit:

`RAW SENIOR -> HARD EXCLUDED -> OPERATIONAL EXCLUDED -> RESEARCHABILITY EXCLUDED -> CAPACITY DEFERRED -> ADMITTED -> C board -> C2 shadow board -> C3 shadow board -> C official action -> C2/C3 shadow action -> Python C/C2/C3 -> result`

Audit WAIT accounting under `FOOTBALL_WAIT_ASSUMED_EXPOSURE.md`: unresolved C-WAITs count as model bets at target/minimum odds; C2/C3 WAITs count as shadow bets. Do not infer a missed line from absent market history.

Audit state is immutable after the fact:
- preserve exact frozen grades/states/lines;
- separate FROZEN / OBSERVED / DIAGNOSIS / P&L STATUS;
- never create retrospective compound grades such as MEDIUM-HIGH;
- FT alone cannot prove what a prospectively frozen grade should have been;
- official C model P/L is separate from actual user P/L;
- every material fixture audit emits and validates a deterministic `FOOTBALL_AUDIT_RECORD`; invalid audit records block finalization.

Separate:
- coverage failures;
- C screening/ranking errors;
- C2 shadow differences;
- C3 burden-funding/selection differences;
- text-vs-code disagreements;
- execution/persistence errors.

## Football C production invariants

- Football-quality screening belongs to the model, not Step 0. Step 0 may exclude for hard scope/identity/time, low operational observability, or insufficient researchability.
- Every admitted fixture must carry operational viability A/B plus XI/market/team-news observability and a frozen competition-reliability state/reason snapshot.
- Competition reliability uses only operational observability/process evidence; FT goals, model results and P/L are forbidden inputs.
- Historical competition reliability may only cap/demote current viability; it may never promote a current fixture.
- Normal Work admission is capped at 15 A/B fixtures; overflow is `OPERATIONAL CAPACITY DEFERRED — STEP0`, not C-PASS.
- Senior women's domestic top-flight blocks are mandatory discovery/accounting; they use the same operational/researchability rules as men's top flights and may not disappear because of gender/category labeling.
- A missing visible women's top-flight block is `HANDOFF INCOMPLETE — WOMEN TOP-FLIGHT COVERAGE GAP`, not a valid completed sweep.
- There is no fixed **predictive** board-size target after admission.
- H2H mandatory when usable; `recent` is review priority rather than a hidden numeric cutoff. Any material H2H effect requires `h2h_effect=SUPPRESSIVE`, `h2h_transferability=VERIFIED`, `h2h_current_corroboration=VERIFIED`, `h2h_material_effect=true`, plus a non-empty basis.
- Fresh post-XI public-web football research mandatory before final prematch C-BET, with a non-empty post-XI research trace.
- Prematch Step 2 requires current fixture status to be confirmed and the executable quote to be revalidated immediately before deterministic execution.
- Every due Step-2 FOLLOW/activated RESERVE/user-exception fixture must reconcile to one explicit disposition; a silent omission is a process failure.
- C/C2/C3 own separate Step-2 policy recheck flags; C2/C3 do not inherit Football C's completion-recheck proof.
- Every fixture explicitly declares `tournament_incentive_required=true/false`.
- For applicable fixtures, **presence is not enough**: format, qualification state, home/away incentive, tiebreak/margin relevance, simultaneous-result impact, and incentive effect must be resolved/VERIFIED before C/C2 state, rank, follow lane, or supported burden exists.
- LIMITED/UNKNOWN applicable fixtures are `INCENTIVE-INCOMPLETE`, not C-PASS/WATCH/FOCUS.
- Applicable Step-2 fixtures require `tournament_incentive_rechecked=true` and `tournament_incentive_recheck_status=VERIFIED` before any C/C2 action.
- A user-declared exception never waives tournament-incentive resolution; it only permits reassessment/reopening.
- Applicable live fixtures recompute the incentive epoch after every goal/red card/material simultaneous-table change before execution; unresolved epochs block action.
- Supported burden chosen before price.
- Burden-completion/continuation fields are frozen before outcome and before price selection.
- Two-sidedness is not a FOLLOW prerequisite; a verified carrier-led path may qualify with a weak second scoring route.
- HIGH burden stall risk blocks routine FOLLOW.
- A HIGH-completion carrier-led row cannot become C-PASS solely because the second route is weak.
- Market evidence informs but does not independently manufacture football quality.
- >=1.65 normal price zone.
- 1.60–1.64 soft zone only for top-ranked C-FOCUS at/below supported burden with no material veto.
- WAIT requires a healthy realistic path.
- Target reached never auto-executes; the prematch/XI thesis must remain materially intact.
- Provider live stats are not required for live assessment and are not execution/cancellation gates.
- Actual user bet slips are physical execution truth.

## Deterministic engine status

`models/football/engine/` is a shadow validator.

It receives frozen common factual evidence plus model-owned policy fields and applies deterministic C/C2/C3 ranking/execution/settlement rules.

On disagreement:
- preserve text result;
- preserve code result;
- preserve exact JSON;
- do not mutate the frozen evidence to force agreement.

## C2 comparison reset

Three plumbing faults invalidate earlier confirmatory C2 comparison windows:

1. the original workflow named Football A as champion and mixed C2 Step 1 with Football C Step 2;
2. after Football C's burden-completion ranking patch, the Python C2 validator accidentally inherited Football C's ranking key, and the workflow did not guarantee an independently frozen C2 supported burden;
3. the Step-2 deterministic contract could previously produce a decision without proving confirmed/reliable XI, fresh post-XI research, H2H recheck, current burden-completion recheck, or explicit negative safety booleans.

Therefore confirmatory C-vs-C2 counting remains at zero until the merge that activates the **Step-2 fail-closed validator repair**, and the five-board window starts from that activation boundary.

Before that boundary:
- rows remain available for debugging;
- do not count them toward confirmatory C-vs-C2 exposure-return metrics;
- do not count Python C2 text/code agreement;
- if C2 supported burden was copied/not independently frozen, mark the paired observation contaminated.

This reset changes comparison/validation plumbing only. It does not change C2's frozen predictive thresholds.

After the Step-2 fail-closed validator repair activates, C2 is frozen again for the restarted five-board window.

## Rollback

Pre-C:
`archive/pre-football-c-active-2026-09-29`

Pre-broad-intake C:
`archive/pre-football-c-broad-senior-intake-2026-09-29`

Pre-dual-track fix:
`archive/pre-c-c2-dual-track-fix-2026-09-30`


## Follow-through capacity

The model board remains complete and uncapped for audit, but routine operational attention is bounded:

- max 6 FOLLOW;
- max 4 RESERVE;
- every other frozen candidate is STOP for routine follow-through.

Quality gate before capacity:
- operational grade A for routine FOLLOW; grade B is capped at RESERVE;
- C-FOCUS only;
- credible TWO_SIDED, CARRIER_LED, FORCED_CHAOS or MIXED completion path;
- STRONG carrier;
- HIGH route reliability and evidence confidence;
- chance quality at least MEDIUM;
- HIGH burden completion + HIGH continuation + LOW stall risk for FOLLOW;
- supported burden <= O3.0;
- FOLLOW requires HIGH failure resistance;
- RESERVE may absorb MEDIUM completion/continuation, MEDIUM stall risk or MEDIUM failure resistance when burden protection remains HIGH;
- exact-same-kickoff FOLLOW cap = 2 before global capacity overflow.

This is a followability rule, not a predictive board-size cap.


## Elite upper-tail observer

`models/football/trials/FOOTBALL_C_ELITE_UPPER_TAIL_OBSERVER_2026-10-01.md` is active as a non-predictive prospective observer.

It tracks a narrow all-HIGH two-route / self-funded STRONG-carrier class to test whether Football C's supported burden is systematically too conservative.

It has no production authority and does not change C/C2 actions or bridge limits.


## New-chat / handoff freshness

Any football stage resumed from a handoff, prior-chat summary, copied response, or stale board artifact must first read:

- `models/football/procedures/FOOTBALL_HANDOFF_FRESHNESS_BOOTSTRAP.md`;
- this `CURRENT_MODEL.md`;
- `models/football/prompts/COMMAND_ALIASES.md`;
- the current canonical launcher for the requested stage.

A handoff is historical state, not current execution authority.

Current visible Step-2/live outputs must account for:
- OFFICIAL C;
- SHADOW C2;
- SHADOW C3.

If a historical challenger state was never prospectively frozen, show it as UNAVAILABLE / COMPARISON INCOMPLETE. Never silently omit the track and never backfill it retrospectively.

## C3 burden-funding prospective test

Use:
- `models/football/challengers/football-c3/FOOTBALL_C3_SPEC.md`
- `models/football/challengers/football-c3/TEST_PROTOCOL.md`

C3 is a new shadow selection experiment. Its five-board counter is independent of C2.

C3's primary question is whether the clearing goal is prospectively funded:
- O2.0–O2.75 -> goal 3;
- O3.0+ -> goal 3 and goal 4.

A second route is classified `BURDEN_CONTRIBUTING / EXCHANGE_ONLY / STATE_DEPENDENT / NONE`. Only BURDEN_CONTRIBUTING has positive selection value.

The recent two-goal cluster motivated C3 but has zero confirmatory C3 weight.

### Challenger board-count integrity

C2/C3 board counters evaluate the **complete ranked eligible universe**, not every raw handoff row.

A prospectively quarantined HOLD/exclusion that receives no model output does not invalidate an otherwise complete ranked board. Missing competition coverage or a silently omitted eligible fixture does invalidate it.

This is comparison plumbing only and does not alter C, C2 or C3 predictive semantics.
