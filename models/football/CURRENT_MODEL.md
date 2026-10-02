# Current Football Model

**Active official model:** Football **C**  
**Shadow challenger:** Football **C2**  
**Effective:** 2026-09-29 ICT  
**Fixture authority:** AiScore  
**Operational timezone:** Asia/Ho_Chi_Minh (ICT, UTC+7)

This file is the canonical entry point for all new football work.

## Model authority

- **Football C** is the only official production model.
- **Football C2** is a shadow challenger only. It may never create a Website Pick or authorize real exposure.
- **Python deterministic engine** is a shadow validation layer for both C and C2.
- Historical Football A decisions remain historical/rollback only.

Do not use a C2 board as the official input to a Football C decision.

## Active production sequence

`SENIOR AISCORE DISCOVERY -> COMPETITION RELIABILITY MEMORY -> CURRENT OPERATIONAL VIABILITY -> RESEARCHABILITY/CAPACITY GATE -> COMMON FOOTBALL EVIDENCE FREEZE -> [C OFFICIAL BOARD + C2 SHADOW BOARD] -> FOLLOW-THROUGH GUARD -> COMMON XI/RESEARCH EVIDENCE FREEZE -> [C OFFICIAL ACTION + C2 SHADOW ACTION] -> C OFFICIAL LIVE/WAIT + C2 SHADOW WAIT -> AUDIT`

The comparison must isolate **policy differences**, not accidental research differences.

## Shared evidence rule

For each fixture/epoch, perform the football research once and freeze a common semantic evidence object before either model applies its policy.

Common evidence includes:
- fixture identity/status;
- home/away route strength;
- carrier strength/self-fund state;
- chance quality;
- failure mode / suppression state;
- relevant H2H transferability;
- `tournament_incentive_required`;
- competition stage/format, draw resolution, aggregate/table state when applicable;
- home/away incentive state, margin/tiebreak relevance and incentive effect;
- evidence confidence;
- supported burden;
- XI mechanism state at Step 2;
- current executable quote at Step 2.

Once frozen, neither C nor C2 may change those shared evidence fields merely because the other model or Python engine disagrees.

## Step 0 — researchable senior intake

Use:
`models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md`

Default intake is `RESEARCHABLE_SENIOR_PRODUCTION`.

Step 0 discovers the senior slate, applies hard scope exclusions, loads the persistent **competition operational reliability memory** from `models/football/procedures/FOOTBALL_COMPETITION_RELIABILITY_MEMORY.md`, then applies the mandatory current-fixture operational viability gate before the cheap researchability gate.

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

After the board is frozen, a separate operational follow-through guard assigns `FOLLOW / RESERVE / STOP`. This does not change the C state. Only FOLLOW receives routine Step-2 attention; RESERVE is conditional; STOP requires explicit override.

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

The previous C2 workflow incorrectly named Football A as champion and allowed Step 1 to become C2-only while Step 2 remained Football C.

That workflow is invalid for confirmatory C-vs-C2 comparison.

Prospective C2 comparison restarts from the dual-track fix commit. Earlier C2 rows may remain for debugging but do not count toward the new confirmatory comparison window.

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
- two usable routes with at least one STRONG;
- STRONG carrier;
- HIGH route reliability / independent route quality / chance quality / evidence confidence;
- supported burden <= O3.0;
- FOLLOW requires HIGH failure resistance;
- RESERVE permits MEDIUM failure resistance only with HIGH burden protection.

This is a followability rule, not a predictive board-size cap.


## Elite upper-tail observer

`models/football/trials/FOOTBALL_C_ELITE_UPPER_TAIL_OBSERVER_2026-10-01.md` is active as a non-predictive prospective observer.

It tracks a narrow all-HIGH two-route / self-funded STRONG-carrier class to test whether Football C's supported burden is systematically too conservative.

It has no production authority and does not change C/C2 actions or bridge limits.
