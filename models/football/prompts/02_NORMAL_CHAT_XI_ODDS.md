# 02 — Normal Chat: Football C Official + C2/C3 Shadow XI/Odds

**Command alias:** `/xi`

Read upstream:
- `models/football/CURRENT_MODEL.md`
- `models/football/production/FOOTBALL_C.md`
- `models/football/challengers/football-c2/FOOTBALL_C2_SPEC.md`
- `models/football/challengers/football-c3/FOOTBALL_C3_SPEC.md`
- `models/football/procedures/FOOTBALL_TOURNAMENT_INCENTIVE_INTEGRITY.md`
- `models/football/procedures/FOOTBALL_OPERATIONAL_VIABILITY_GATE.md`
- `models/football/procedures/FOOTBALL_BURDEN_COMPLETION_SELECTION.md`

Football C is the only active official model. C2 and C3 are shadow-only.

Use the user's confirmed XI and current executable Asian-total odds as the current evidence epoch.

A preserved scoring route is not enough. Recheck the burden-completion layer after XI/research: where the clearing goal now comes from, whether the carrier can still self-fund, whether opponent leakage remains active, whether continuation after 1-0 / 1-1 / 2-0 is still credible, and whether stall risk has risen to HIGH. If stall risk becomes HIGH or completion/continuation materially degrades, a frozen FOLLOW lane does not force C-BET.

## 1. Retrieve all frozen board states

For each supplied fixture retrieve:
- frozen operational viability grade and Step-0 XI/market/team-news observability;
- frozen completion mode, burden-completion quality, continuation quality, opponent leakage and burden-stall risk;
- Football C official board state/rank and independently frozen C supported line;
- Football C2 shadow state/rank and independently frozen C2 supported line if present;
- Football C3 shadow state/rank/lane, independently frozen C3 supported line and burden-funding fields if present;
- the frozen common board evidence.

If C2 shadow state is missing, continue Football C officially and mark C2 comparison unavailable. Never replace the C board with a C2 board.

If C2 state exists but its supported line was not independently frozen:
`C2 COMPARISON INCOMPLETE — SUPPORTED BURDEN NOT INDEPENDENTLY FROZEN`
Continue Football C; do not manufacture C2's line from C.

If C3 exists without an independently frozen supported line/funding block:
`C3 COMPARISON INCOMPLETE — BURDEN-FUNDING STATE NOT INDEPENDENTLY FROZEN`
Continue Football C/C2 normally; do not reconstruct C3 from their outputs.

## 1A. Follow-through lane authority

Before spending Step-2 research time, retrieve the frozen official operational lane.

- `FOLLOW` — normal Step-2 processing.
- `RESERVE` — process only when activated because FOLLOW candidates collapsed or the user explicitly requests it. This includes B-grade operational candidates, which were intentionally prevented from routine FOLLOW.
- `STOP` — do not run routine Step-2; require an explicit exception request.

A WATCH/STOP fixture becoming attractive merely because of price does not automatically reopen it.

This lane is operational only; it does not rewrite the official C board state.

## 2. Common XI/research evidence freeze

Perform this **once** for the fixture:

1. verify fixture/status;
2. require an actual confirmed/reliable XI for a routine final prematch decision; Step-0 `xi_expected` is not a substitute;
3. inspect confirmed XI and map changes to route functions;
4. run **MANDATORY FRESH POST-XI FOOTBALL WEB RESEARCH**;
5. run the **MANDATORY TOURNAMENT FORMAT & INCENTIVE CHECK** when applicable;
6. perform/recheck relevant H2H/matchup context;
7. update the structured common semantic evidence, including current completion mode/quality, continuation quality, opponent leakage and stall risk;
8. classify thesis state = PRESERVED / DEGRADED / BROKEN;
9. freeze current quote.

Persist one of:
- `POST-XI RESEARCH = FOUND`
- `POST-XI RESEARCH = LIMITED`
- `POST-XI RESEARCH = UNAVAILABLE — ATTEMPTED`

Odds/history lookup does **not** satisfy the football-research gate.

Carry forward `tournament_incentive_required` for **every fixture**.

- If false: record `Tournament incentive = NOT APPLICABLE`.
- If true: perform the fresh current-format/current-table incentive recheck regardless of whether XI changed, set `tournament_incentive_rechecked = true`, and persist `tournament_incentive_recheck_status = VERIFIED / LIMITED / UNKNOWN`.

If an applicable fixture has not been rechecked:

`DECISION BLOCKED — TOURNAMENT INCENTIVE RECHECK MISSING`

If it was rechecked but any material qualification/tiebreak/margin/simultaneous-result item remains LIMITED / UNKNOWN:

`DECISION BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED`

Do not issue C-BET/C-WAIT/C-PASS or C2/C3 shadow action from an unresolved mandatory integrity state. An explicit user exception does not waive this requirement.

For tournament/cup/qualifier/two-leg/final-round contexts persist:
- `TOURNAMENT FORMAT = VERIFIED / LIMITED / UNKNOWN`;
- `QUALIFICATION STATE = <exact current requirement>`;
- `TIEBREAK/MARGIN = YES / NO / UNKNOWN`;
- `SIMULTANEOUS RESULTS = VERIFIED / NOT_APPLICABLE / LIMITED / UNKNOWN`;
- `INCENTIVE STATE = <home> / <away>`;
- `INCENTIVE EFFECT = EXPANSIVE / NEUTRAL / SUPPRESSIVE / MIXED / UNKNOWN`;
- `INCENTIVE RECHECK STATUS = VERIFIED / LIMITED / UNKNOWN`.

Before any post-XI supported-line upgrade, apply the burden-upgrade veto from the tournament procedure. Stronger XI alone cannot raise burden if draw/aggregate/penalty/table incentives make control or parity strategically acceptable.

Once this common XI evidence is frozen, C, C2 and C3 apply their policies independently. Do not change shared evidence because one track disagrees.

## 3. Football C official action

Apply Football C production rules to:
- C official board state;
- common frozen XI/research/H2H state;
- current executable quote.

Issue exactly one:
- `C-BET`
- `C-WAIT`
- `C-PASS`

Only Football C may create official exposure.

For every C-BET/C-WAIT/C-PASS Decision State persist:
- `C Action` = exact current official action;
- `C Supported Line`;
- `C2 Supported Line` when independently frozen;
- `C2 Shadow Action` when available;
- `C3 Supported Line` when independently frozen;
- `C3 Shadow Action` and current C3 funding/control fields when available;
- `Current Completion Mode`;
- `Current Completion Quality`;
- `Current Continuation Quality`;
- `Current Opponent Leakage`;
- `Current Stall Risk`.

Do not map current C actions onto legacy Football A `Verdict` choices.

For C-BET:
1. persist Decision State;
2. publish/reconcile Website Pick;
3. verify no duplicate official pick.

For C-WAIT/C-PASS:
- Decision State only.

## 4. Football C2 shadow action

Apply C2 rules independently to:
- C2 shadow board state;
- the same common XI/research/H2H evidence;
- the same current quote.

Evaluate:
- C2 selection-quality floor;
- protected-line inversion guard;
- Focus Market-Gap Bridge when eligible;
- unreachable-WAIT condition.

Issue:
- `C2-BET — SHADOW`
- `C2-WAIT — SHADOW`
- `C2-PASS — SHADOW`

C2 must never:
- publish Website Pick;
- authorize user exposure;
- replace the official C action.

Persist C2 in Decision States under:
`Football C2 — SHADOW`

## 5. Football C3 burden-funding shadow action

Only evaluate C3 at Step 2 when the fixture is already receiving normal C-driven XI/odds assessment or an explicit user exception.

Recheck from the same current evidence epoch:
- second-route role;
- goal-3 funding/source/basis;
- goal-4 funding/source/basis when required;
- control-endpoint risk/basis;
- C3 forced-chaos verification.

C3 direct shadow BET requires:
- C3-FOCUS;
- required clearing-goal funding VERIFIED;
- control-endpoint risk LOW;
- primary funding mechanism intact;
- no material veto;
- current quote at/below C3 supported line;
- normal C price floor.

C3 has **no C2 market-gap bridge**.

Persist:
- `C3-BET — SHADOW`;
- `C3-WAIT — SHADOW`;
- `C3-PASS — SHADOW`.

Never create a Website Pick or extra mandatory monitoring from C3.

## 6. Python engine comparison — three tracks

Every decision payload must explicitly prove the current Step-2 evidence epoch.

Required context fields:
- `xi_status = CONFIRMED / RELIABLE / UNAVAILABLE`; `UNAVAILABLE` blocks a final decision;
- `post_xi_research_status = FOUND / LIMITED / UNAVAILABLE_ATTEMPTED`;
- `h2h_review_status = REVIEWED_USABLE / REVIEWED_LIMITED / NOT_USABLE / UNAVAILABLE`;
- `h2h_rechecked = true`;
- `completion_rechecked = true`;
- `top_ranked_focus`;
- `primary_mechanism_intact`;
- `wait_reachable`;
- `wait_requires_negative_info`;
- `material_veto`;
- `tournament_incentive_rechecked`;
- `tournament_incentive_recheck_status`.

Required current assessment fields include:
- non-empty `main_failure`;
- non-empty `h2h_state`;
- explicit `carrier_self_fund`;
- explicit `independent_upper_tail`;
- explicit `failure_attacks_route`;
- explicit `material_suppression`;
- current completion/continuation/stall fields.

Do not omit a boolean because the expected answer is false. Missing safety fields are contract failures, never favorable defaults.

For an applicable tournament fixture the deterministic adapter fails closed unless rechecked=true **and** status=VERIFIED.

For Football C code validation:
- HIGH current stall risk cannot BET;
- LOW current burden-completion quality cannot BET;
- LOW current continuation quality cannot BET;
- a non-intact primary mechanism cannot BET.

These are validation of the current Football C text state, not new predictive screening rules.

Build three decision payloads from the same factual evidence epoch:

- `model = c`, using C board_state and C supported line;
- `model = c2`, using C2 board_state and independently frozen C2 supported line.
- `model = c3`, using C3 board_state, independent C3 supported line and current C3 funding/control fields.

Do not reuse C's supported line in C2 or C3 payloads.

Run:

`python models/football/engine/cli.py decision --input <payload.json>`

Compare six outputs:
- C text official;
- C code shadow;
- C2 text shadow;
- C2 code shadow;
- C3 text shadow;
- C3 code shadow.

If disagreement:

`ENGINE DISAGREEMENT — PRESERVE BOTH`

Never edit frozen input fields after seeing code output.

## 7. C-WAIT

Every official C-WAIT must state:
- target line;
- minimum odds;
- cancellation event;
- thesis-health evidence required at target.

Do not create a wait that is expected to become executable only after negative football information.

C2-WAIT and C3-WAIT must each preserve separate target/cancel conditions.

## 9. Output

Use:

`#<C rank> MATCH`

Then:

- **OFFICIAL C:** C-BET / C-WAIT / C-PASS
- **SHADOW C2:** C2-BET / C2-WAIT / C2-PASS
- **SHADOW C3:** C3-BET / C3-WAIT / C3-PASS
- XI common state: PRESERVED / DEGRADED / BROKEN
- POST-XI RESEARCH status
- H2H material state
- Completion mode + current burden-completion quality
- Current continuation quality + opponent leakage + stall risk
- Tournament incentive requirement + recheck status **always**; when applicable, also show format, draw/aggregate state, home/away incentive, margin relevance, and incentive effect
- C supported line
- C2 supported line if different
- Current line/odds
- C reason
- C2 difference/reason
- C WAIT plan if applicable
- C2 shadow WAIT plan if applicable
- Engine C result
- Engine C2 result
- C3 supported line + second-route/funding/control delta
- Engine C3 result

## 8. Required machine appendix

Include:
- `FOOTBALL_ENGINE_C_DECISION_INPUT`
- `FOOTBALL_ENGINE_C_DECISION_RESULT`
- `FOOTBALL_ENGINE_C2_DECISION_INPUT`
- `FOOTBALL_ENGINE_C2_DECISION_RESULT`
- `FOOTBALL_ENGINE_C3_DECISION_INPUT`
- `FOOTBALL_ENGINE_C3_DECISION_RESULT`

The machine appendix must preserve all required Step-2 gate fields above so QA can distinguish an actual negative declaration from an omitted field.

If execution is unavailable:
`ENGINE NOT EXECUTED — STRUCTURED INPUT PRESERVED`

## 9. Authority

In any conflict:
- Football C text decision = current production authority;
- C2 = frozen route-quality shadow challenger;
- C3 = burden-funding shadow challenger;
- Python = shadow validator;
- user bet slip = physical execution truth.


## Prospective elite upper-tail observer — quote capture only

If a fixture entered Step 2 with `ELITE_UPPER_TAIL_OBSERVER` already frozen at Step 1:

- preserve the tag;
- record the exact executable main/alternate Over lines and odds available at the decision epoch;
- record the gap from Football C supported burden;
- do not change C, C2 or C3 action because of the observer;
- do not create a hypothetical live plan solely for the observer.

The observer is data collection, not a betting rule.
