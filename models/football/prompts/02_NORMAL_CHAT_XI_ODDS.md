# 02 — Normal Chat: Football C Official + C2/C3 Shadow XI/Odds + C4 Step-1 Snapshot

**Command alias:** `/xi`

Read upstream:
- `models/football/procedures/FOOTBALL_HANDOFF_FRESHNESS_BOOTSTRAP.md`
- `models/football/CURRENT_MODEL.md`
- `models/football/production/FOOTBALL_C.md`
- `models/football/challengers/football-c2/FOOTBALL_C2_SPEC.md`
- `models/football/challengers/football-c3/FOOTBALL_C3_SPEC.md`
- `models/football/challengers/football-c4/FOOTBALL_C4_SPEC.md`
- `models/football/airtable/FOOTBALL_C4_AIRTABLE.md`
- `models/football/procedures/FOOTBALL_TOURNAMENT_INCENTIVE_INTEGRITY.md`
- `models/football/procedures/FOOTBALL_OPERATIONAL_VIABILITY_GATE.md`
- `models/football/procedures/FOOTBALL_BURDEN_COMPLETION_SELECTION.md`
- `models/football/procedures/FOOTBALL_MARKET_HISTORY_RECHECK.md`
- `models/football/procedures/FOOTBALL_WAIT_ASSUMED_EXPOSURE.md`
- `models/football/procedures/FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md`
- `models/football/procedures/FOOTBALL_ENGINE_EXECUTION_BOOTSTRAP.md`

Football C is the only active official model. C2 and C3 are Step-2 shadow models. C4 remains Step-1-only, but its prospectively frozen Step-1 snapshot is mandatory visibility in every material `/xi` match block.

Use the user's confirmed XI and current executable Asian-total odds as the current evidence epoch.

A preserved scoring route is not enough. Recheck the burden-completion layer after XI/research: where the clearing goal now comes from, whether the carrier can still self-fund, whether opponent leakage remains active, whether continuation after 1-0 / 1-1 / 2-0 is still credible, and whether stall risk has risen to HIGH. If stall risk becomes HIGH or completion/continuation materially degrades, a frozen FOLLOW lane does not force C-BET.

## 1. Retrieve all frozen board states

For each supplied fixture retrieve:
- frozen operational viability grade and Step-0 XI/market/team-news observability;
- frozen completion mode, burden-completion quality, continuation quality, opponent leakage and burden-stall risk;
- Football C official board state/rank and independently frozen C supported line;
- Football C2 shadow state/rank and independently frozen C2 supported line if present;
- Football C3 shadow state/rank/lane, independently frozen C3 supported line and burden-funding fields if present;
- Football C4 frozen Step-1 shadow state/rank/supported line, route/carrier/funding/control summary, compiler revision, and C4 Board N/5 status if present;
- the frozen common board evidence.

If C2 shadow state is missing, continue Football C officially and mark C2 comparison unavailable. Never replace the C board with a C2 board.

If C2 state exists but its supported line was not independently frozen:
`C2 COMPARISON INCOMPLETE — SUPPORTED BURDEN NOT INDEPENDENTLY FROZEN`
Continue Football C; do not manufacture C2's line from C.

If C3 exists without an independently frozen supported line/funding block:
`C3 COMPARISON INCOMPLETE — BURDEN-FUNDING STATE NOT INDEPENDENTLY FROZEN`
Continue Football C/C2 normally; do not reconstruct C3 from their outputs.

If no prospective C4 Step-1 freeze exists for this fixture:
`SHADOW C4 (STEP1): UNAVAILABLE — NO PROSPECTIVE C4 FREEZE`

If C4 fields exist but the compiler/result block is incomplete:
`SHADOW C4 (STEP1): COMPARISON INCOMPLETE — STRUCTURED EVIDENCE / COMPILER OUTPUT INCOMPLETE`

Never synthesize a C4 Step-2 action from XI evidence. C4 visibility is a read-only frozen Step-1 comparison.

## 1A. Follow-through lane authority

Before spending Step-2 research time, retrieve the frozen official operational lane.

- `FOLLOW` — normal Step-2 processing.
- `RESERVE` — process only when activated because FOLLOW candidates collapsed or the user explicitly requests it. This includes B-grade operational candidates, which were intentionally prevented from routine FOLLOW.
- `STOP` — do not run routine Step-2; require an explicit exception request.

A WATCH/STOP fixture becoming attractive merely because of price does not automatically reopen it.

This lane is operational only; it does not rewrite the official C board state.

### Step-2 due-set manifest — mandatory

Before research begins, freeze the current session due set under:
`models/football/procedures/FOOTBALL_STEP2_SESSION_RECONCILIATION.md`.

Include:
- every FOLLOW whose XI/odds decision window is open;
- every RESERVE explicitly activated for this session;
- every user-declared exception.

C2/C3/C4 never add fixtures to this set.

Before any Step-2 Python command, execute the common runtime bootstrap with stage=`xi`. Probe Python and the current GitHub repository source in this turn.

Primary XI runtime:
1. fetch exact-current `models/football/engine/xi_portable.py`;
2. write that single file locally;
3. run `python xi_portable.py self-check`;
4. require `XI PORTABLE RUNTIME: PASS`;
5. write the frozen C/C2/C3 payloads;
6. execute the portable triplet.

Do not use multi-file materialization when the portable self-check passes. A missing checkout or container network/DNS failure is not GitHub/repository unavailability.

At the end of the session run:
`python xi_portable.py reconcile --input <step2_reconcile.json>`

Use `step2_reconcile_cli.py` only on the documented multi-file fallback path.

Do not call the Step-2 session complete unless:
`STEP2 RECONCILIATION STATUS: PASS`

A missing due fixture is:
`STEP2 RECONCILIATION FAILED — SILENT OMISSION`

## 2. Common XI/research evidence freeze

Perform this **once** for the fixture:

1. verify fixture/status and set `fixture_status = PREMATCH_CONFIRMED / STARTED / POSTPONED / CANCELLED / FINISHED / UNKNOWN`; only PREMATCH_CONFIRMED may continue through prematch Step 2, while STARTED routes to the live workflow;
2. require an actual confirmed/reliable XI for a routine final prematch decision; Step-0 `xi_expected` is not a substitute;
3. inspect confirmed XI and map changes to route functions **before reading market history**;
4. run **MANDATORY FRESH POST-XI FOOTBALL WEB RESEARCH**;
5. run the **MANDATORY MARKET-HISTORY ATTEMPT**: `OPEN -> PRE-XI -> POST-XI / CURRENT PREMATCH`;
6. run the **MANDATORY TOURNAMENT FORMAT & INCENTIVE CHECK** when applicable;
7. perform/recheck relevant H2H/matchup context;
8. run the market-history conflict recheck when movement/current market materially disagrees with XI or frozen support;
9. update the shared route/mechanism facts once, then derive each model's owned current policy fields separately: Football C completion/continuation/stall diagnostics, C2 route-quality/selection-floor state, and C3 funding/control state;
10. classify thesis state = PRESERVED / DEGRADED / BROKEN;
11. freeze the current executable user quote;
12. immediately before deterministic execution, revalidate that the quoted line/odds are still executable and set `quote_revalidated = true`; if the quote moved/disappeared, update the quote and rerun or block C-BET.

Persist one post-XI research status:
- `POST-XI RESEARCH = FOUND`
- `POST-XI RESEARCH = LIMITED`
- `POST-XI RESEARCH = UNAVAILABLE — ATTEMPTED`

Also persist a non-empty `post_xi_research_note` describing the fresh football information actually checked after XI confirmation. Market-history lookup alone cannot satisfy this note.

Persist one market-history status:
- `MARKET HISTORY = FOUND`
- `MARKET HISTORY = PARTIAL`
- `MARKET HISTORY = UNAVAILABLE — ATTEMPTED`

When found, show OPEN / PRE-XI / CURRENT totals, movement direction and source/timestamp note. The user's supplied current executable quote remains execution authority.

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
- `C Exposure Basis`;
- `C Exposure Line`;
- `C Exposure Odds`;
- `WAIT Resolution`;
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
2. set `C Exposure Basis = DIRECT_BET`;
3. publish/reconcile one Website Pick at the direct quote;
4. set `WAIT Resolution = NOT_APPLICABLE`;
5. verify no duplicate official pick.

For C-WAIT:
1. preserve `C Action = C-WAIT`;
2. use engine `wait_target_line` + `wait_min_odds`;
3. set `C Exposure Basis = WAIT_ASSUMED`;
4. set `C Exposure Line/Odds = WAIT target/minimum`;
5. set `WAIT Resolution = ASSUMED_REACHED`;
6. publish/reconcile one Website Pick immediately at target/minimum, normally 1u;
7. verify no duplicate official pick.

A C-WAIT does **not** wait for later market confirmation before becoming a model-accounting bet.

Only update that assumed WAIT exposure when:
- the user provides an actual corresponding bet slip -> `WAIT_USER_CONFIRMED / USER_CONFIRMED` and reconcile to exact actual line/odds/stake; or
- the user explicitly says the target line never reached -> `WAIT_NOT_REACHED / USER_DECLARED_NOT_REACHED`, no model exposure.

For C-PASS:
- Decision State only with `C Exposure Basis = NONE`.

Do not auto-cancel a WAIT exposure because later market history is missing, live odds differ, or no user slip appears.

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

For audit accounting, C2-WAIT defaults to a shadow assumed bet at engine `wait_target_line / wait_min_odds`. It remains shadow-only and never creates a Website Pick.

C2 must never:
- publish Website Pick;
- authorize user exposure;
- replace the official C action.

Persist C2 in Decision States under:
`Football C2 — SHADOW`

## 5. Football C3 burden-funding shadow action

Only evaluate C3 at Step 2 when the fixture is already receiving normal C-driven XI/odds assessment or an explicit user exception.

Recheck from the same current evidence epoch:
- second-route role + non-empty second-route-role basis;
- goal-3 funding/source/basis;
- goal-4 funding/source/basis when required;
- control-endpoint risk/basis;
- C3 forced-chaos verification + non-empty forced-chaos basis.

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

For audit accounting, C3-WAIT defaults to a shadow assumed bet at engine `wait_target_line / wait_min_odds`.

Never create a Website Pick or extra mandatory monitoring from C3.

## 6. Python engine comparison — three tracks

Every decision payload must explicitly prove the current Step-2 evidence epoch.

Also apply:
`models/football/procedures/FOOTBALL_SEMANTIC_DECISION_BASIS.md`

Required common context fields:
- `fixture_status = PREMATCH_CONFIRMED`;
- `xi_status = CONFIRMED / RELIABLE / UNAVAILABLE`; `UNAVAILABLE` blocks a final decision;
- `post_xi_research_status = FOUND / LIMITED / UNAVAILABLE_ATTEMPTED`;
- non-empty `post_xi_research_note`;
- `quote_revalidated = true`;
- `market_history_status = FOUND / PARTIAL / UNAVAILABLE_ATTEMPTED`;
- non-empty `market_history_note`;
- `h2h_review_status = REVIEWED_USABLE / REVIEWED_LIMITED / NOT_USABLE / UNAVAILABLE`;
- `h2h_rechecked = true`;
- non-empty `h2h_basis`;
- `thesis_state` + non-empty `thesis_state_basis`;
- `top_ranked_focus`;
- `primary_mechanism_intact` + non-empty `primary_mechanism_basis`;
- `wait_reachable` + non-empty `wait_reachability_basis`;
- `wait_requires_negative_info` + non-empty `wait_negative_info_basis`;
- `material_veto` + non-empty `material_veto_basis`;
- `tournament_incentive_rechecked`;
- `tournament_incentive_recheck_status`.

Required model-owned recheck fields:
- Football C: `completion_rechecked = true`;
- Football C2: `c2_route_quality_rechecked = true`;
- Football C3: `c3_funding_rechecked = true`.

Do not satisfy C2/C3 by copying Football C's completion-recheck flag.

Required shared current assessment fields include:
- non-empty frozen `common_evidence_basis`;
- non-empty model-owned `supported_line_basis`;
- non-empty `main_failure`;
- non-empty `h2h_state` + `h2h_effect` + `h2h_transferability` + `h2h_current_corroboration` + explicit `h2h_material_effect` + non-empty `h2h_basis`;
- explicit `carrier_self_fund` + non-empty `carrier_self_fund_basis`;
- explicit `independent_upper_tail` + non-empty `independent_upper_tail_basis`;
- explicit `failure_attacks_route` + non-empty `failure_attacks_route_basis`;
- explicit `material_suppression` + non-empty `material_suppression_basis`.

Football C's payload additionally requires current `completion_mode`, `burden_completion_quality`, `continuation_quality`, `opponent_leakage`, and `burden_stall_risk`.

C2 and C3 payloads must not carry those C-owned diagnostics merely to satisfy the deterministic parser. C2 uses its route-quality/selection-floor policy; C3 uses its own second-route/funding/control fields.

Do not omit a boolean because the expected answer is false. Missing safety fields are contract failures, never favorable defaults. A semantic Boolean without its contemporaneous evidence basis is also incomplete and must not be treated as a valid false/true declaration.

For an applicable tournament fixture the deterministic adapter fails closed unless rechecked=true **and** status=VERIFIED.

For H2H, a material suppressive effect is fail-closed unless `h2h_effect=SUPPRESSIVE`, transferability is VERIFIED, and current corroboration is VERIFIED. `recent` remains review priority only; no numerical H2H recency cutoff is active.

For Football C code validation:
- HIGH current stall risk cannot BET;
- LOW current burden-completion quality cannot BET;
- LOW current continuation quality cannot BET;
- a non-intact primary mechanism cannot BET.

These are validation of the current Football C text state, not new predictive screening rules.

Build three decision payloads from the same factual evidence epoch:

- `model = c`, using C board_state, C supported line, and C-owned completion/continuation/stall diagnostics;
- `model = c2`, using C2 board_state and independently frozen C2 supported line, without C-owned completion diagnostics;
- `model = c3`, using C3 board_state, independent C3 supported line and current C3 funding/control fields, without C-owned completion diagnostics.

Do not reuse C's supported line in C2 or C3 payloads.

All three payloads must also freeze the same official C workload authorization:
- `official_follow_lane = FOLLOW / RESERVE / STOP`;
- `step2_authorization = ROUTINE_FOLLOW / RESERVE_ACTIVATED / USER_EXCEPTION`.

`ROUTINE_FOLLOW` is valid only for official lane FOLLOW. `RESERVE_ACTIVATED` is valid only for official lane RESERVE. A STOP fixture may enter Step 2 only through `USER_EXCEPTION`. C2/C3 never create their own workload authorization.

Engine execution is **mandatory** for a completed Step-2 decision.

Preferred execution:

`python xi_portable.py triplet --c <c.json> --c2 <c2.json> --c3 <c3.json>`

This must execute all three frozen payloads as one fail-closed unit.

Only if exact-current `xi_portable.py self-check` itself fails may the workflow materialize the full engine tree and use:
`python models/football/engine/decision_triplet_cli.py --c <c.json> --c2 <c2.json> --c3 <c3.json>`

Only if both portable and multi-file triplet runners cannot be used, run the three individual commands:

`python models/football/engine/cli.py decision --input <c.json>`

`python models/football/engine/cli.py decision --input <c2.json>`

`python models/football/engine/cli.py decision --input <c3.json>`

A missing local checkout is **not** engine unavailability. If GitHub/files source plus a Python runtime are available, fetch the exact-current portable XI runner and execute it.

A deterministic payload/contract rejection is not a Python error. Report the exact rejected field/rule and preserve the frozen payload. Only a portable self-check/runtime failure may trigger the multi-file fallback.

Before any terminal failure claim, follow `FOOTBALL_ENGINE_EXECUTION_BOOTSTRAP.md` and make both the required portable attempt and documented repair/fallback attempt when applicable.

Compare six Step-2 decision outputs plus the frozen C4 Step-1 snapshot:
- C text official;
- C code shadow;
- C2 text shadow;
- C2 code shadow;
- C3 text shadow;
- C3 code shadow;
- C4 frozen Step-1 state/rank/line — no Step-2 action.

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

## 8. Output

### Mandatory four-model visibility

Every material match block must visibly account for Football C, C2, C3, and the frozen C4 Step-1 snapshot, even when the fixture/handoff lacks a legal prospective shadow freeze.

Never omit C2, C3, or C4 visibility.

Use one of:
- `SHADOW C2: C2-BET / C2-WAIT / C2-PASS`;
- `SHADOW C2: UNAVAILABLE — NO PROSPECTIVE C2 FREEZE`;
- `SHADOW C2: COMPARISON INCOMPLETE — SUPPORTED BURDEN NOT INDEPENDENTLY FROZEN`;
- `SHADOW C3: C3-BET / C3-WAIT / C3-PASS`;
- `SHADOW C3: UNAVAILABLE — BOARD PREDATES C3 / NO PROSPECTIVE C3 FREEZE`;
- `SHADOW C3: COMPARISON INCOMPLETE — BURDEN-FUNDING STATE NOT INDEPENDENTLY FROZEN`;
- `SHADOW C4 (STEP1): C4-FOCUS / C4-WATCH / C4-PASS — NO STEP2 ACTION`;
- `SHADOW C4 (STEP1): UNAVAILABLE — NO PROSPECTIVE C4 FREEZE`;
- `SHADOW C4 (STEP1): COMPARISON INCOMPLETE — STRUCTURED EVIDENCE / COMPILER OUTPUT INCOMPLETE`.

A handoff that only names C/C2/C3 is not permission to suppress C4 snapshot visibility from the current output.

Use:

`#<C rank> MATCH`

Then:

- **OFFICIAL C:** C-BET / C-WAIT / C-PASS
- **SHADOW C2:** C2-BET / C2-WAIT / C2-PASS
- **SHADOW C3:** C3-BET / C3-WAIT / C3-PASS
- **SHADOW C4 (STEP1):** C4-FOCUS / C4-WATCH / C4-PASS — NO STEP2 ACTION
- XI common state: PRESERVED / DEGRADED / BROKEN
- POST-XI RESEARCH status
- MARKET HISTORY status + OPEN / PRE-XI / CURRENT trace + movement + conflict-recheck result
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
- C3 shadow WAIT plan if applicable
- Engine execution status + source revision
- Engine C result
- Engine C2 result
- C3 supported line + second-route/funding/control delta
- C3 Board N/5 comparison status
- Engine C3 result
- C4 frozen Step-1 rank/state/supported line + route/carrier/funding/control summary
- C4 compiler revision + C4 Board N/5 status
- Engine failure reason when FAILED_AFTER_ATTEMPT

## 9. Required machine appendix

Include:
- `FOOTBALL_ENGINE_C_DECISION_INPUT`
- `FOOTBALL_ENGINE_C_DECISION_RESULT`
- `FOOTBALL_ENGINE_C2_DECISION_INPUT`
- `FOOTBALL_ENGINE_C2_DECISION_RESULT`
- `FOOTBALL_ENGINE_C3_DECISION_INPUT`
- `FOOTBALL_ENGINE_C3_DECISION_RESULT`

The machine appendix must preserve all required Step-2 gate fields above so QA can distinguish an actual negative declaration from an omitted field.

For every model result also preserve:
- `wait_target_line`;
- `wait_min_odds`;
- `model_accounting_status`;
- `model_accounting_line`;
- `model_accounting_odds`;
- `wait_resolution_default`.

Also include:
- `FOOTBALL_C4_FROZEN_STEP1_SNAPSHOT`
- `FOOTBALL_STEP2_RECONCILIATION_INPUT`
- `FOOTBALL_STEP2_RECONCILIATION_RESULT`

Execution status is mandatory.

On success:
`ENGINE EXECUTION STATUS: EXECUTED_ALL_THREE`

The legacy generic no-execution fallback is forbidden.

Only after exact-current portable self-check/execution plus any applicable documented repair/fallback genuinely fails for an unresolved technical reason may the assessment use:

`ENGINE EXECUTION STATUS: FAILED_AFTER_ATTEMPT — <exact technical reason>`

and

`ENGINE EXECUTION FAILED — ATTEMPTED — <exact technical reason>`

Preserve all three structured inputs, the source revision, attempted command/setup path, and the available error output.

"Lack of local checkout", "repo only available through GitHub", or "runtime not prepared yet" are not valid failure reasons.

## 10. Authority

In any conflict:
- Football C text decision = current production authority;
- C2 = frozen route-quality shadow challenger;
- C3 = burden-funding Step-2 shadow challenger;
- C4 = frozen Step-1 structured-evidence snapshot only; no Step-2 action;
- Python = shadow validator for C/C2/C3;
- user bet slip = physical execution truth.


## Prospective elite upper-tail observer — quote capture only

If a fixture entered Step 2 with `ELITE_UPPER_TAIL_OBSERVER` already frozen at Step 1:

- preserve the tag;
- record the exact executable main/alternate Over lines and odds available at the decision epoch;
- record the gap from Football C supported burden;
- do not change C, C2 or C3 action because of the observer;
- do not create a hypothetical live plan solely for the observer.

The observer is data collection, not a betting rule.
