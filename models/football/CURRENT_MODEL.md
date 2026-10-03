# Current Football Model

**Active official model:** Football **C**  
**Shadow challenger:** Football **C2**  
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
- **Football C2** is a shadow challenger only. It may never create a Website Pick or authorize real exposure.
- **Python deterministic engine** is a shadow validation layer for both C and C2.
- Historical Football A decisions remain historical/rollback only.
- `FOOTBALL_PRE_DECISION_SPEC.md`, `FOOTBALL_STEP2_EXECUTION_SPEC.md`, and `05_NORMAL_CHAT_FOOTBALL_C.md` are retired historical Football A/shadow artifacts and must not control new production.

Do not use a C2 board as the official input to a Football C decision.

## Active production sequence

`SENIOR AISCORE DISCOVERY -> COMPETITION RELIABILITY MEMORY -> CURRENT OPERATIONAL VIABILITY -> RESEARCHABILITY/CAPACITY GATE -> COMMON FOOTBALL FACT FREEZE -> [C BURDEN-COMPLETION + C2 OWN SUPPORTED BURDEN] -> [C OFFICIAL BOARD + C2 SHADOW BOARD] -> SAME-KICKOFF COMPARATIVE FOLLOW GUARD -> COMMON XI/RESEARCH FACT FREEZE -> [C OFFICIAL ACTION + C2 SHADOW ACTION] -> C OFFICIAL LIVE/WAIT + C2 SHADOW WAIT -> AUDIT`

The comparison must isolate **policy differences**, not accidental research differences.

## Shared evidence rule

For each fixture/epoch, perform the football research once and freeze a common semantic evidence object before either model applies its policy.

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

Once frozen, neither C nor C2 may change those shared factual fields merely because the other model or Python engine disagrees.

Model-owned policy fields are then derived separately:
- Football C: completion mode/quality, continuation grade, stall risk and C supported line;
- Football C2: independently frozen C2 supported line and frozen C2 route-quality ranking policy.

C2 must not inherit C's supported line or C's burden-completion ranking key.

## Step 0 — researchable senior intake

Use:
`models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md`

Default intake is `RESEARCHABLE_SENIOR_PRODUCTION`.

Step 0 discovers the senior slate, including the mandatory senior women's domestic top-flight class defined by `models/football/procedures/FOOTBALL_WOMENS_TOP_FLIGHT_COVERAGE.md`, applies hard scope exclusions, loads the persistent **competition operational reliability memory** from `models/football/procedures/FOOTBALL_COMPETITION_RELIABILITY_MEMORY.md`, then applies the mandatory current-fixture operational viability gate before the cheap researchability gate.

Every surviving fixture receives a raw current A/B/C/D viability plus explicit XI expectation, market observability and team-news observability. The persistent competition state may only cap/demote that raw grade; it may never promote it.

- A = executable and eligible for normal follow-through.
- B = conditional and may be admitted, but is capped at RESERVE at board time.
- C/D = excluded before Work unless explicitly reopened by the user.
- CAUTION competition history caps raw A to B.
- DEMOTED competition history defaults the fixture to C, with at most one fully clean raw-A probation fixture per competition per sweep admitted as B.
- Normal Work admission is capped at 15 A/B fixtures; overflow is preserved as `OPERATIONAL CAPACITY DEFERRED — STEP0`.

Protected senior international qualifiers/tournaments and major continental club competitions bypass the ordinary domestic researchability exclusion when identity/time are valid, but not the operational viability declaration.

For ordinary domestic/small blocks, admit only when operational viability is A/B **and** current evidence is sufficient for both teams to support Football C's research schema: recent form, competition context, and at least one usable mechanism/stat/news layer.

## Step 1 — dual-track board

Use:
`models/football/prompts/01_WORK_DAILY_SWEEP.md`

One common research/evidence pass is frozen first.

Then:
- Football C creates the **official** C-PASS / C-WATCH / C-FOCUS board.
- Football C2 independently applies its shadow selection/ranking rules to the same frozen evidence and creates C2-PASS / C2-WATCH / C2-FOCUS.
- Python runs model=`c` and model=`c2` against the same structured evidence.

Football C's board is the only board that can feed official Step-2 exposure.

After the board is frozen, the burden-completion follow-through guard assigns `FOLLOW / RESERVE / STOP`. It compares exact-same-kickoff candidates against each other, caps routine FOLLOW at two per kickoff minute, and does not change the underlying C state. Only FOLLOW receives routine Step-2 attention; RESERVE is conditional; STOP requires explicit override.

## Step 2 — dual-track XI + odds

Use:
`models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md`

Perform one common XI + mandatory fresh post-XI web-research + H2H update, freeze it, then derive:

- **Football C official:** C-BET / C-WAIT / C-PASS.
- **Football C2 shadow:** C2-BET / C2-WAIT / C2-PASS.
- **Python C shadow validation.**
- **Python C2 shadow validation.**

Only Football C may publish an official Website Pick.

## Live

Use:
`models/football/prompts/03_NORMAL_CHAT_LIVE.md`

Resolve Football C official WAITs normally.

If the same fixture also has a predeclared C2-WAIT, resolve the C2 wait from the same live state as a shadow comparison only.

## Audit

Use:
`models/football/prompts/04_WORK_POST_SLATE_AUDIT.md`

Audit:

`RAW SENIOR -> HARD EXCLUDED -> OPERATIONAL EXCLUDED -> RESEARCHABILITY EXCLUDED -> CAPACITY DEFERRED -> ADMITTED -> C board -> C2 shadow board -> C official action -> C2 shadow action -> Python C/C2 -> result`

Separate:
- coverage failures;
- C screening/ranking errors;
- C2 shadow differences;
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
- H2H mandatory when usable.
- Fresh post-XI public-web football research mandatory before final prematch C-BET.
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
- Target reached never auto-executes; thesis health must still be positive.
- Actual user bet slips are physical execution truth.

## Deterministic engine status

`models/football/engine/` is a shadow validator.

It receives the frozen common semantic evidence and applies deterministic ranking/execution/settlement rules.

On disagreement:
- preserve text result;
- preserve code result;
- preserve exact JSON;
- do not mutate the frozen evidence to force agreement.

## C2 comparison reset

Two plumbing faults invalidate earlier confirmatory C2 comparison windows:

1. the original workflow named Football A as champion and mixed C2 Step 1 with Football C Step 2;
2. after Football C's burden-completion ranking patch, the Python C2 validator accidentally inherited Football C's ranking key, and the workflow did not guarantee an independently frozen C2 supported burden.

Therefore confirmatory C-vs-C2 counting restarts again from the merge that activates the **QA authority/C2 validation repair**.

Before that boundary:
- rows remain available for debugging;
- do not count them toward confirmatory C-vs-C2 exposure-return metrics;
- do not count Python C2 text/code agreement;
- if C2 supported burden was copied/not independently frozen, mark the paired observation contaminated.

This reset changes comparison plumbing only. It does not change C2's frozen predictive thresholds.

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
