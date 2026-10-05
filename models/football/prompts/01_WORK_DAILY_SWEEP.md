# 01 — Work: Football C Official + C2/C3 + C4 Step-1 Shadow

**Command alias:** `/rank`

Read upstream:
- `models/football/procedures/FOOTBALL_CAPACITY_REPLENISHMENT.md`
- `models/football/CURRENT_MODEL.md`
- `models/football/production/FOOTBALL_C.md`
- `models/football/challengers/football-c2/FOOTBALL_C2_SPEC.md`
- `models/football/challengers/football-c2/TEST_PROTOCOL.md`
- `models/football/challengers/football-c3/FOOTBALL_C3_SPEC.md`
- `models/football/challengers/football-c3/TEST_PROTOCOL.md`
- `models/football/challengers/football-c4/FOOTBALL_C4_SPEC.md`
- `models/football/challengers/football-c4/TEST_PROTOCOL.md`
- `models/football/airtable/FOOTBALL_C4_AIRTABLE.md`
- `models/football/procedures/FOOTBALL_TOURNAMENT_INCENTIVE_INTEGRITY.md`
- `models/football/procedures/FOOTBALL_OPERATIONAL_VIABILITY_GATE.md`
- `models/football/procedures/FOOTBALL_COMPETITION_RELIABILITY_MEMORY.md`
- `models/football/procedures/FOOTBALL_BURDEN_COMPLETION_SELECTION.md`
- `models/football/procedures/FOOTBALL_WOMENS_TOP_FLIGHT_COVERAGE.md`
- `models/football/procedures/FOOTBALL_REQUIRED_COMPETITION_COVERAGE.md`
- `models/football/procedures/FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md`
- `models/football/procedures/FOOTBALL_MODEL_BET_ACCOUNTING.md`
- `models/football/procedures/FOOTBALL_REPAIRED_HANDOFF_AUTHORITY.md`
- `models/football/procedures/FOOTBALL_RANK_TERMINAL_STATUS.md`

Use the attached `AISCORE_FIXTURES_*.zip` from Step 0.

If the attached file is a completed repaired sweep, apply `FOOTBALL_REPAIRED_HANDOFF_AUTHORITY.md` **before any web research**.

First run the local repaired-handoff metadata normalizer. Duplicate `disposition` vs `final_step0_disposition`, stale women counters, or non-boolean `women_top_flight` values must be normalized locally when the complete fixture-level manifest makes the canonical value deterministic.

Once accepted, its fixture identity, kickoff, canonical Step-0 dispositions and capacity queue are frozen for /rank.

Require:
`sweep_scope_mode=RESEARCHABLE_SENIOR_PRODUCTION`

Accept either:
- native fixture-exact completeness with `global_raw_exact=true`; or
- `coverage_mode=FALLBACK_PRODUCTION_SCOPE`, `global_raw_exact=false`, and `production_scope_complete=true`.

Fallback production-scope mode is valid only when protected/required competition manifests and the senior women's top-flight manifest are still fixture-exact, every plausible A/B candidate has a Step-0 disposition, and the admitted array satisfies the normal operational gate. Do not fail merely because the all-level global raw count is intentionally unavailable.

If package/completeness fails:
`HANDOFF INCOMPLETE — RESEARCHABLE SENIOR COVERAGE GAP`

Do not rebuild the raw universe in Work.

For an accepted repaired handoff, do not re-verify kickoff/fixture identity on the web and do not run Step-0 repair inside /rank.

Metadata alias/counter normalization under `repaired_handoff_normalize.py` is explicitly allowed because it changes no fixture identity, kickoff, operational evidence, queue rank, or final disposition.

If a material non-metadata contradiction is discovered incidentally during Step-1 research, emit `REPAIRED HANDOFF CONFLICT — RETURN TO STEP0 REPAIR` rather than repairing it here.

## 0A. Required competition coverage preflight — fail closed

Before ranking, require:
- `required_competition_manifest_version = required-competition-manifest-v1`;
- protected block `NED_EERSTE_DIVISIE` present exactly once;
- status = CHECKED_WITH_FIXTURES or CHECKED_NO_IN_WINDOW_FIXTURES;
- no SOURCE_BLOCKED protected block;
- fixture_count equals the listed fixture array;
- every listed fixture has a normal Step-0 disposition;
- `Required Competition Blocks Complete = true`.

If absent, stale, unresolved or inconsistent:

`HANDOFF INCOMPLETE — REQUIRED COMPETITION COVERAGE GAP`

For a missing Eerste block:

`HANDOFF INCOMPLETE — NETHERLANDS EERSTE DIVISIE COVERAGE GAP`

Do not silently rebuild/rank around the missing block. Repair Step 0 first.

## 0. Operational handoff gate — fail closed

Before full football research, verify the Step-0 contract:

- admitted fixture count <= 15;
- every admitted fixture has `operational_viability_grade = A / B`;
- every admitted fixture has `xi_expected`, `market_observability`, `team_news_observability`, and `operational_viability_reason`;
- every admitted fixture has `competition_reliability_state` and `competition_reliability_reason`;
- CAUTION is never above B and DEMOTED is present only as an allowed B probation fixture;
- no C/D fixture appears in the normal Work array;
- all six women's-top-flight counters are present;
- `women_top_flight_unresolved_count = 0`;
- `women_top_flight_raw_count` equals admitted + operational excluded + researchability excluded + capacity deferred + unresolved;
- `women_top_flight_disposition_manifest` is present and contains every discovered senior women's domestic top-flight fixture.

If a C/D fixture leaks in:

`ASSESSMENT BLOCKED — LOW OPERATIONAL OBSERVABILITY`

If the handoff contains more than 15 normal admissions:

`HANDOFF INCOMPLETE — OPERATIONAL CAPACITY BREACH`

If women's-top-flight counters/manifest are absent, inconsistent, unresolved, or omit a visible block:

`HANDOFF INCOMPLETE — WOMEN TOP-FLIGHT COVERAGE GAP`

Do not rescue Step-0 operational exclusions or capacity-deferred fixtures with deep Work research unless the user explicitly declares an exception.

## 1. Common evidence freeze — mandatory

Research each **researchability-admitted** senior fixture **once**. Do not reopen Step-0 researchability-excluded obscure blocks unless the user explicitly overrides that exclusion.

### Tournament-incentive applicability gate — mandatory first

For **every fixture**, explicitly set:

- `tournament_incentive_required = true / false`.

If false, persist all tournament fields as `NOT_APPLICABLE`.

If true, complete the mandatory tournament-format/incentive procedure **before** route/failure/supported-burden classification is finalized. Persist:

- `tournament_format_status = VERIFIED / LIMITED / UNKNOWN`;
- `competition_stage`;
- `competition_format`;
- `draw_resolution`;
- `aggregate_state`;
- `qualification_state` — exact current advancement/elimination requirement;
- `simultaneous_results_status = VERIFIED / NOT_APPLICABLE / LIMITED / UNKNOWN`;
- `simultaneous_results_note`;
- `home_incentive`;
- `away_incentive`;
- `tiebreak_margin_relevance = YES / NO / UNKNOWN`;
- `incentive_effect = EXPANSIVE / NEUTRAL / SUPPRESSIVE / MIXED / UNKNOWN`.

If an applicable fixture is missing any field:

`ASSESSMENT INCOMPLETE — TOURNAMENT INCENTIVE CHECK MISSING`

If fields are present but any material incentive element remains LIMITED / UNKNOWN / unresolved:

`ASSESSMENT BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED`

A tournament fixture is resolved for Step 1 only if format status is VERIFIED, qualification state is explicit, home/away incentives are resolved, tiebreak/margin relevance is YES/NO, simultaneous-result impact is VERIFIED or genuinely NOT_APPLICABLE, and incentive effect is resolved.

Until then place it in a separate `INCENTIVE-INCOMPLETE` table. It receives **no C/C2/C3/C4 state, no rank, no supported line, and no follow-through lane**. Continue processing other fixtures.

An incentive quarantine is **fixture-local**, not a board-level `/rank` failure. It does not consume FOLLOW/RESERVE capacity. If deferred prematch A/B candidates exist, normal Step-1 replenishment remains mandatory. If the queue is exhausted and no ranked fixture remains, the valid terminal state is `/rank complete — no ranked eligible fixtures`, not `/rank blocked`.

A user-declared exception may reopen research but **never bypasses the incentive-resolution gate**.

Freeze one common **football-fact** evidence state before any model applies policy.

Also apply:
`models/football/procedures/FOOTBALL_STEP1_BOARD_RECONCILIATION.md`.

Every admitted fixture must include a non-empty `common_evidence_basis` describing the shared Step-1 research epoch used to freeze the common grades.

Shared facts stop before model-owned policy. Football C, C2 and C3 consume the same semantic routes/carrier/chance/failure/H2H/incentive evidence, then independently derive model-owned burden/selection fields.

C4 uses the **same research epoch** but does not consume C/C2/C3 semantic grades as authority. Before seeing any C/C2/C3 output, freeze the C4 structured evidence anchors required by `FOOTBALL_C4_SPEC.md`: creation repeatability, dangerous access, service/finishing continuity, matched opponent leakage, personnel integrity, route-specific suppression and multi-goal repeatability for each side, plus coverage, continuation, control, failure/suppression and upper-tail anchors. Every anchor must carry a non-empty basis.

Freeze these shared facts:

- match_id / identity / kickoff;
- operational_viability_grade = A / B;
- xi_expected = YES / UNCERTAIN;
- market_observability = HIGH / MEDIUM;
- team_news_observability = HIGH / MEDIUM;
- operational_viability_reason;
- raw_operational_viability_grade;
- competition_reliability_state;
- competition_reliability_reason;
- competition_reliability_manual_override;
- demoted_probation;
- home_route = WEAK / USABLE / STRONG;
- away_route = WEAK / USABLE / STRONG;
- carrier = NONE / USABLE / STRONG;
- carrier_self_fund;
- route_reliability = LOW / MEDIUM / HIGH;
- independent_route_quality = LOW / MEDIUM / HIGH;
- chance_quality = LOW / MEDIUM / HIGH;
- failure_resistance = LOW / MEDIUM / HIGH;
- evidence_confidence = LOW / MEDIUM / HIGH;
- burden_protection = LOW / MEDIUM / HIGH;
- opponent_leakage = LOW / MEDIUM / HIGH;
- continuation evidence sufficient to let each model apply its own policy;
- failure_attacks_route;
- material_suppression;
- independent_upper_tail;
- relevant H2H state/transferability;
- competition stage/format when applicable;
- draw_resolution / aggregate_state;
- home_incentive / away_incentive;
- tiebreak_margin_relevance;
- incentive_effect = EXPANSIVE / NEUTRAL / SUPPRESSIVE / MIXED / UNKNOWN;
- main failure mode.

Do **not** freeze one shared `supported_line` as common policy evidence.

After the common facts are frozen:
- Football C derives and freezes `c_supported_line` + non-empty `supported_line_basis`, plus its model-owned machine fields `completion_mode`, `burden_completion_quality`, `continuation_quality`, and `burden_stall_risk` under the active burden-completion procedure;
- Football C2 independently derives and freezes `c2_supported_line` + non-empty `supported_line_basis` under Section 5 of its frozen challenger specification;
- Football C3 independently derives `c3_supported_line` + non-empty `supported_line_basis`, second-route role + `c3_second_route_role_basis`, goal-3/goal-4 funding source/basis, control-endpoint risk and `c3_forced_chaos_verified` + `c3_forced_chaos_basis`.
- neither model may copy the other model's line simply for payload/persistence convenience.

For Football C and C2, every frozen PASS/WATCH/FOCUS state must also include a non-empty `board_state_basis`. This makes the current semantic classification auditable; it does not introduce a new state threshold.

At board time set `xi_robustness` from currently known lineup robustness; if XI is not confirmed, use the same evidence-based pre-XI value for C/C2/C3. C4 does not read this semantic grade; it compiles from its own structured anchors.

For cups/tournaments/qualifiers/two-leg ties/final-round incentive states, the format-and-incentive check is mandatory before freezing supported burden. Do not mark suppression or expansion from recent scores alone. If the incentive state is LIMITED/UNKNOWN, do not freeze an official supported burden at all; keep the fixture INCENTIVE-INCOMPLETE until resolved.

**Do not run separate C, C2, C3 or C4 research passes.**  
The experiment compares model policy/compilation, not independently drifting research interpretations. C4 may structure the same evidence differently, but it may not perform a later result-aware research pass.

Once frozen, do not edit common evidence after seeing any model's ranking or the Python output.

## 2. Football C official board

Apply `models/football/production/FOOTBALL_C.md` to the common evidence.

Before final C state/rank, derive the Football C-owned completion fields and `c_supported_line`, then answer for every fixture:

`WHERE DOES THE GOAL THAT CLEARS THE SUPPORTED BURDEN COME FROM?`

Two-sided route labels are insufficient. A HIGH carrier-led completion path may survive with a WEAK second scoring route. Conversely, a balanced TWO_SIDED profile with HIGH stall risk must not receive routine preference merely because both teams can plausibly score once.

If a proposed C-PASS has HIGH completion + HIGH continuation + STRONG self-funded carrier + independent upper-tail proof + MEDIUM/HIGH opponent leakage and no suppression, re-open the screen. Do not finalize C-PASS solely from the weak second route.

Produce:
- C-PASS
- C-WATCH
- C-FOCUS
- official C ordinal rank
- C supported burden / failure summary

This is the **only official board** for Step 2.

Persist Football C as the canonical Daily Coverage state.

## 3. Football C2 shadow board

Apply the C2 challenger rules to the **same frozen common evidence**.

First derive and freeze `c2_supported_line` independently from the shared football facts. Do not read or copy `c_supported_line` while creating it.

Compute:
- C2-PASS / C2-WATCH / C2-FOCUS;
- C2 ordinal rank under the frozen C2 ranking policy;
- C2 supported line;
- selection-quality floor;
- protected-line inversion diagnostics;
- bridge readiness.

If an independent C2 supported line cannot be frozen:
`C2 COMPARISON INCOMPLETE — SUPPORTED BURDEN NOT INDEPENDENTLY FROZEN`
and exclude that fixture from confirmatory C-vs-C2 action metrics while continuing Football C normally.

C2 is shadow-only:
- no Website Pick;
- no official exposure;
- do not overwrite Football C official fields.

Persist C2 shadow in dedicated shadow fields/notes when available. If only one canonical coverage row exists, preserve official C fields and store C2 state as clearly labelled `C2_SHADOW` metadata rather than replacing C.

## 4. Football C3 burden-funding shadow board

Apply `FOOTBALL_C3_SPEC.md` to the same frozen common facts **without reading C/C2 rank/state/line first**.

For every admitted fixture independently freeze:
- `c3_supported_line`;
- `c3_second_route_role = BURDEN_CONTRIBUTING / EXCHANGE_ONLY / STATE_DEPENDENT / NONE`;
- `c3_goal3_funding = VERIFIED / PARTIAL / NONE / NOT_REQUIRED`;
- `c3_goal3_funding_source = CARRIER / SECOND_ROUTE / FORCED_CHAOS / MIXED / NONE`;
- `c3_goal3_funding_basis`;
- `c3_goal4_funding` + source/basis;
- `c3_control_endpoint_risk = LOW / MEDIUM / HIGH`;
- `c3_control_endpoint_basis`;
- `c3_forced_chaos_verified = true/false`.

Then derive:
- C3-PASS / C3-WATCH / C3-FOCUS;
- C3 ordinal rank;
- C3-FOLLOW / C3-RESERVE / C3-STOP — SHADOW.

Hard C3 semantics:
- two usable routes alone create **zero** positive C3 value;
- EXCHANGE_ONLY/STATE_DEPENDENT cannot be treated as burden-completing;
- O2.0–O2.75 needs a real goal-3 path;
- O3.0+ needs goal-3 and goal-4 paths;
- MEDIUM control-endpoint risk caps C3 at WATCH/RESERVE;
- HIGH control-endpoint risk normally PASS/STOP.

If C3 supported burden cannot be independently frozen:
`C3 COMPARISON INCOMPLETE — SUPPORTED BURDEN NOT INDEPENDENTLY FROZEN`

C3 is shadow-only and does not create extra routine Step-2 workload.

### C3 prospective-board counter

After the complete C3 shadow board is frozen, evaluate the test-protocol integrity state.

If clean:
- set `C3 Test Board Eligible = true`;
- assign the next sequential `C3 Test Board Number = 1..5`;
- leave `C3 Contamination Reason` blank.

If contaminated:
- set `C3 Test Board Eligible = false`;
- do not advance the C3 board counter;
- persist the exact `C3 Contamination Reason`.

Board eligibility is judged on the **ranked eligible universe**.

A prospectively quarantined HOLD / INCENTIVE-INCOMPLETE / exclusion does not block the counter when it received no C/C2/C3 state/rank/line/lane and every remaining ranked fixture is complete.

A board is not clean when any C3 policy field was assigned after outcome knowledge, the C3 line was copied from C/C2, a required funding basis is missing on a ranked fixture, a mandatory integrity gate was bypassed, an unresolved fixture was ranked, or a required competition/eligible-fixture block is missing from discovery.

**One isolated quarantine does not invalidate the whole board. A coverage gap does.**

This counter is independent of the C2 five-board test.

## 4A. Football C4 structured-evidence Step-1 shadow

Apply `FOOTBALL_C4_SPEC.md` to the same ranked eligible universe and same contemporaneous research epoch.

C4 must freeze its structured anchors **before reading C/C2/C3 rank/state/line**.

Run the deterministic compiler:

`python models/football/engine/c4_semantic_cli.py --input <c4.json> --c-board <c.json>`

Required success:
- `c4_execution_status = EXECUTED`;
- `c4_reconciled_with_c = true`;
- same ranked eligible match IDs as Football C;
- exact matching `common_evidence_basis` per fixture.

C4 is Step-1 shadow only. It creates **no FOLLOW/RESERVE/STOP**, no automatic `/xi` workload, no live plan and no Website Pick.

### C4 prospective-board counter

C4 starts at **0/5** from its activation merge.

A board advances the C4 counter only when:
- normal Step-0 coverage is complete;
- the C/C2/C3 board triplet is clean;
- every ranked eligible fixture has a complete prospective C4 anchor payload;
- the C4 compiler executes for the complete ranked universe before outcome knowledge.

If clean:
- set `C4 Test Board Eligible = true`;
- set the next `C4 Test Board Number = 1..5`;
- leave `C4 Contamination Reason` blank.

If incomplete/contaminated:
- set `C4 Test Board Eligible = false`;
- do not advance the C4 counter;
- persist the exact contamination reason.

C4 eligibility is independent of C2/C3 counters.

### C4 persistence — mandatory before /rank completion

After the C4 compiler result is frozen, persist the prospectively generated C4 snapshot under `FOOTBALL_C4_AIRTABLE.md`.

For **every ranked eligible fixture**, write to its existing Daily Coverage row:
- `C4 Shadow State`;
- `C4 Shadow Rank`;
- `C4 Supported Line`;
- `C4 Home Route`;
- `C4 Away Route`;
- `C4 Carrier`;
- `C4 Goal3 Funding`;
- `C4 Goal4 Funding`;
- `C4 Control Risk`;
- `C4 Structured Evidence` as the exact/lossless frozen anchor JSON;
- `C4 Compiler Result` as the exact/lossless deterministic result;
- `C4 Compiler Revision`.

For the board's Sweep Runs row, write:
- `C4 Test Board Number` when eligible;
- `C4 Test Board Eligible`;
- `C4 Contamination Reason` when ineligible.

Then read back the same rows and reconcile:
- C4 ranked eligible fixture count equals the C ranked eligible fixture count;
- every eligible fixture has C4 state/rank/compiler revision;
- every non-null C4 supported line matches the frozen compiler result;
- Sweep Runs C4 eligibility/counter state matches the current test protocol.

If any required C4 field write/readback is missing:

`C4 PERSISTENCE SYNC FAULT — /RANK INCOMPLETE`

Do not report the board as a complete C4 prospective board and do not advance the C4 counter. The official Football C board remains valid, but the C4 comparison for that board is explicitly incomplete.

This persistence is what later `/xi` reads. Never reconstruct C4 at Step 2.

## 5. Python engine — C/C2/C3 board reconciliation + C4 compiler

Serialize the frozen Step-1 evidence into three model-owned payloads using:
`models/football/engine/schema.json`.

Preferred mandatory runner:

`python models/football/engine/board_triplet_cli.py --c <c.json> --c2 <c2.json> --c3 <c3.json>`

The runner:
- requires the same ranked eligible match universe in C/C2/C3;
- requires exact equality of the common factual evidence for every match;
- rejects Football C completion-policy leakage into C2/C3;
- rejects C3-only policy leakage into C/C2;
- runs all three deterministic board validators.

Success requires:
- `board_engine_execution_status = EXECUTED_ALL_THREE_BOARDS`;
- `common_evidence_reconciled = true`.

The following are model-owned and may differ:
- `model`;
- C/C2 `board_state` + `board_state_basis`;
- `supported_line` + `supported_line_basis`;
- Football C completion-policy fields;
- C3-only burden-funding/control fields.

Do not run three unrelated board commands and assume the evidence remained identical.

After the C/C2/C3 triplet passes, run the C4 structured compiler against the frozen Football C board payload. C4 comparison is invalid if ranked universe or common evidence basis differs.

After compiler success, perform the mandatory C4 Airtable persistence + readback reconciliation above.

### All-model WATCH accounting — mandatory

For every ranked eligible fixture, after C/C2/C3/C4 states and supported lines are frozen, build one accounting payload containing all four models and run:

`python models/football/engine/model_bet_accounting_cli.py --input <model_accounting.json>`

At rank stage:
- C/C2/C3/C4 WATCH -> accounting bet at that model's supported line @1.65, 1u;
- non-WATCH board states -> no accounting bet yet unless later Step-2 action supplies BET/WAIT;
- C is official model-accounting;
- C2/C3/C4 are shadow-only;
- no WATCH creates Website Pick or Step-2 workload.

Persist the exact per-model JSON to:
- `C Model Accounting`;
- `C2 Shadow Accounting`;
- `C3 Shadow Accounting`;
- `C4 Shadow Accounting`;
- `Model Accounting Revision`.

A ranked board is accounting-incomplete if a WATCH exists without a supported line/accounting result.

Python remains shadow validation only.

If text/code disagree:

`ENGINE DISAGREEMENT — PRESERVE BOTH`

Do not mutate the frozen semantic evidence.

## Factor calibration observer — prospective write

Read:
- `models/football/procedures/FOOTBALL_FACTOR_CALIBRATION_OBSERVER.md`;
- `models/football/airtable/FOOTBALL_FACTOR_CALIBRATION_AIRTABLE.md`.

After the final Football C board/rank/lane/support is frozen and before any FT result is known, append one `Factor Calibration Observations` row per ranked C fixture when the full required factor vector is available.

Freeze only prospectively established fields. Outcome columns remain blank.

This observer is diagnostic only. Its Trace Score or historical performance must never alter:
- C/C2/C3 state;
- C rank;
- supported line;
- FOLLOW/RESERVE/STOP;
- Step-2 eligibility.

If a required factor was not prospectively frozen, do not infer it for calibration. Mark the observation ineligible or omit it with an explicit calibration note.

## 6. Output

Primary table — official production board:

`FOOTBALL C OFFICIAL BOARD <window>`

| C Rank | Match | C state | Routes | Carrier | Incentive | Supported line | Main failure | Initial action |
|---|---|---|---|---|---|---|---|---|

Then comparison table:

`FOOTBALL C2 SHADOW DELTA`

| Match | C rank/state | C line | C2 rank/state | C2 line | C2 floor | Bridge readiness | Material difference |
|---|---|---:|---|---:|---|---|---|

`FOOTBALL C3 BURDEN-FUNDING DELTA — BOARD <N>/5`

| Match | C rank/state/lane | C3 rank/state/lane | C3 line | 2nd-route role | Goal-3 funding | Goal-4 funding | Control risk | Material difference |
|---|---|---|---:|---|---|---|---|---|

`FOOTBALL C4 STRUCTURED-EVIDENCE DELTA — BOARD <N>/5`

| Match | C rank/state/line | C4 rank/state/line | C4 routes | Carrier | Goal-3 | Goal-4 | Control risk | Material difference |
|---|---|---|---|---|---|---|---|---|

`ALL-MODEL ACCOUNTING SNAPSHOT`

| Match | C accounting | C2 accounting | C3 accounting | C4 accounting |
|---|---|---|---|---|

Show WATCH entries as `WATCH_ASSUMED O<line> @1.65 1u` (shadow prefix for C2/C3/C4).

Report funnel:

`INITIAL ADMITTED -> STEP1 WAVE(S) -> C-PASS/C-WATCH/C-FOCUS + C2 shadow + C3 shadow + C4 Step-1 shadow -> FOLLOW/RESERVE CAPACITY SATURATED OR QUEUE EXHAUSTED`

Also report:
- initial Step-0 batch size;
- deferred A/B queue size;
- replenishment waves used;
- replenished fixtures;
- remaining deferred prematch queue count;
- final FOLLOW / RESERVE / STOP counts.

Also report any:
- C vs C2 rank inversion;
- C vs C3 rank/lane inversion;
- C3 two-route demotion caused by EXCHANGE_ONLY / STATE_DEPENDENT;
- C3 goal-3/goal-4 funding blocker;
- C4 vs C state/rank/supported-line inversion;
- C4 structured-anchor incompleteness;
- C2 selection-floor block;
- potential unreachable-WAIT risk;
- text-vs-code disagreement.

## 7. Required machine appendix

Every machine assessment object must include the explicit operational-viability / competition-reliability contract **and** the tournament-incentive contract. The engine must reject omission instead of defaulting it away.

Include:
- `FOOTBALL_ENGINE_C_INPUT`
- `FOOTBALL_ENGINE_C_RESULT`
- `FOOTBALL_ENGINE_C2_INPUT`
- `FOOTBALL_ENGINE_C2_RESULT`
- `FOOTBALL_ENGINE_C3_INPUT`
- `FOOTBALL_ENGINE_C3_RESULT`
- `FOOTBALL_BOARD_TRIPLET_RESULT`
- `FOOTBALL_C4_INPUT`
- `FOOTBALL_C4_RESULT`
- `FOOTBALL_MODEL_ACCOUNTING_INPUT`
- `FOOTBALL_MODEL_ACCOUNTING_RESULT`

Deterministic execution is mandatory for a completed ranked board.

Before any engine command, execute `FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md` for stage=`rank`. A missing local checkout or container network failure is not engine/repository unavailability.

The board output must include a `FOOTBALL_RUNTIME_EXECUTION_RECORD` showing:
- Python probe;
- current repository revision/source probe;
- local materialization result;
- `runtime_probe.py --stage rank` result;
- actual board-triplet/C4 command status.

The legacy generic no-execution fallback is forbidden. Do not say Python/GitHub/repository is unavailable without the bootstrap's failed-attempt evidence record.

## 8. Non-negotiable separation

- Football C official board feeds official Step 2.
- C2/C3 shadow boards never substitute for C.
- C4 is Step-1 shadow only and never feeds Step 2.
- C2/C3/C4 may not create real-bet instructions.
- C/C2/C3 use the same frozen common semantic evidence epoch; C4 uses the same research epoch but independently freezes its lower-level structured anchors before model outputs.


## 9. Operational follow-through guard — mandatory

The Football C board itself remains uncapped for audit. **Operational follow-through is capacity-limited.**

After the official C board is frozen, assign every official C fixture one operational lane using `models/football/engine/core.py::follow_through_lane`:

### FOLLOW
Routine XI/odds follow-through is allowed only when all are true:
- operational viability grade A;
- C-FOCUS;
- completion mode TWO_SIDED / CARRIER_LED / FORCED_CHAOS / MIXED;
- carrier STRONG;
- route reliability HIGH;
- burden completion HIGH;
- continuation HIGH;
- burden stall risk LOW;
- chance quality at least MEDIUM;
- failure resistance HIGH;
- evidence confidence HIGH;
- supported line <= O3.0;
- no route-attacking failure or material suppression.

TWO_SIDED requires two usable routes and at least one STRONG route.

CARRIER_LED permits a WEAK second route only when the STRONG carrier can self-fund, independent upper-tail proof is present, and opponent leakage is at least MEDIUM.

Two-sidedness alone is not a FOLLOW advantage.

### RESERVE
Operational grade B can never receive routine FOLLOW at board time; when football structure clears it is capped at RESERVE.

An A-grade C-FOCUS may also be RESERVE when the completion path remains credible and burden protection is HIGH but failure resistance, completion or continuation is MEDIUM, or stall risk is MEDIUM rather than LOW.

RESERVE does not consume routine Step-2 attention. Activate it only when:
- FOLLOW candidates collapse at XI/price; or
- the user explicitly asks for the reserve match.

### STOP
All other C-FOCUS, every C-WATCH and every C-PASS remain frozen for audit but do not receive routine XI/odds/live follow-through.

This is an **operational capacity rule**, not a reclassification of C-PASS/WATCH/FOCUS.

### Capacity

After quality gating:
- maximum routine `FOLLOW = 6`;
- maximum retained `RESERVE = 4`;
- maximum routine `FOLLOW = 2` for fixtures sharing the exact scheduled kickoff minute.

Rank exact-same-kickoff candidates by the burden-completion key before consuming FOLLOW capacity. Otherwise-qualified same-kickoff overflow goes to RESERVE, then STOP.

If more qualify, preserve official C rank and demote overflow in rank order:
`FOLLOW overflow -> RESERVE -> STOP`.

Never alter the underlying C state to satisfy the capacity limit.

### Deterministic replenishment — mandatory

The Step-0 15-fixture handoff is the **first research wave only**.

After freezing C state/rank/lane for the current wave, compute:
`active_lane_count = FOLLOW + RESERVE`.

If `active_lane_count < 10` and prematch `OPERATIONAL_CAPACITY_DEFERRED` A/B fixtures remain:

1. if the attached repaired handoff contains the complete deferred A/B queue, use that attached queue as primary authority; otherwise load the deferred A/B queue from Daily Coverage for the same sweep;
2. serialize current lane counts + queued candidates and run:
   `python models/football/engine/capacity_replenishment_cli.py --input <capacity_replenishment.json>`;
3. require `capacity_replenishment_status = REPLENISHMENT_REQUIRED` before opening a new wave;
4. read the returned fixtures in ascending immutable `Step0 Capacity Queue Rank`;
5. skip only fixtures that have already started/left prematch, preserving that reason;
6. pull only the selector-returned fixtures into the next replenishment wave;
7. set `Step1 Replenished = true`;
8. set `Replenishment Wave = 1, 2, ...`;
9. persist `Replenishment Reason = ACTIVE LANE CAPACITY UNDERFILLED`;
10. run the full common-evidence + C/C2/C3/C4 Step-1 process on those fixtures;
11. merge them into the already-frozen board without rewriting earlier evidence;
12. recompute official C ranking/lane allocation across all still-prematch assessed fixtures;
13. repeat until FOLLOW+RESERVE reaches 10 or the deferred prematch A/B queue is exhausted.

A STOP/PASS does not permanently consume one of the original 15 research slots.

A fixture that started before its replenishment turn is recorded:
`REPLENISHMENT SKIPPED — PREMATCH WINDOW CLOSED`

Do not jump ahead in the queue because a later fixture looks more attractive. Do not use model result, price, goals profile, or FT knowledge to choose replenishment order.

This is an operational utilization rule only. It does not require Football C to manufacture 10 non-STOP selections.

An `INCENTIVE-INCOMPLETE` / prospectively quarantined fixture occupies **zero** active-lane capacity. It cannot stop replenishment while a deferred prematch A/B candidate remains.

## 9A. Deterministic terminal-status check — mandatory

After replenishment reaches a stop condition, serialize:
- `ranked_eligible_count`;
- `quarantine_count`;
- `follow_count`;
- `reserve_count`;
- `stop_count`;
- `remaining_prematch_deferred_count`;
- `board_integrity_failure`;
- `integrity_failure_reason`.

Run:

`python models/football/engine/rank_terminal_status_cli.py --input <rank_terminal.json>`

Use the returned label exactly.

Hard semantics:
- `RANK BLOCKED` is reserved for a true board/process integrity failure;
- empty ranked universe + legitimate quarantine + exhausted queue = `/rank complete — no ranked eligible fixtures`;
- ranked universe with FOLLOW=0 = `/rank complete — 0 FOLLOW`;
- remaining deferred prematch candidates with active capacity = continue replenishment.

Never write:

`/rank blocked — no FOLLOW candidates`

## 10. Revised output

Show the operational queue first:

`FOOTBALL C FOLLOW-THROUGH QUEUE`

| Queue | C rank | Same-KO rank | Match | Op grade | C state | Completion mode | Completion | Continuation | Stall risk | Carrier | Supported line | Why |
|---|---:|---:|---|---|---|---|---|---|---|---|---:|---|

Order:
1. FOLLOW
2. RESERVE
3. compact count only for STOP unless the user asks for the full board.

Then keep the full board persisted for audit.

Report the deterministic terminal label first, then:

`SERIOUS CANDIDATES -> FOLLOW -> RESERVE -> STOP`

Show `INCENTIVE-INCOMPLETE` / other prospective quarantine rows separately. Quarantines are not STOP and are not ranked.

The normal user-facing schedule should contain only FOLLOW fixtures. RESERVE may be shown separately but is not part of routine monitoring.


## Prospective elite upper-tail observer — non-predictive

Read:
`models/football/trials/FOOTBALL_C_ELITE_UPPER_TAIL_OBSERVER_2026-10-01.md`

After the common evidence freeze, tag `ELITE_UPPER_TAIL_OBSERVER` when the frozen fixture satisfies every observer trigger.

The tag:
- must be assigned before outcome;
- does not alter C state, rank, supported burden or follow-through lane;
- does not authorize exposure;
- is carried forward only for prospective audit.
