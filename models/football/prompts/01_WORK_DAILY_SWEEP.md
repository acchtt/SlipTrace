# 01 — Work: Football C Official + C2 Shadow Board

> **ACTIVE ROSTER (2026-10-06):** Football C is official; Football C2 is the only shadow challenger. C3 and C4 are retired from new/current execution.

**Command alias:** `/rank`

Read before execution:
- `models/football/CURRENT_MODEL.md`
- `models/football/procedures/FOOTBALL_C_C2_ACTIVE_PAIR.md`
- `models/football/production/FOOTBALL_C.md`
- `models/football/challengers/football-c2/FOOTBALL_C2_SPEC.md`
- `models/football/challengers/football-c2/TEST_PROTOCOL.md`
- `models/football/procedures/FOOTBALL_TOURNAMENT_INCENTIVE_INTEGRITY.md`
- `models/football/procedures/FOOTBALL_OPERATIONAL_VIABILITY_GATE.md`
- `models/football/procedures/FOOTBALL_COMPETITION_RELIABILITY_MEMORY.md`
- `models/football/procedures/FOOTBALL_BURDEN_COMPLETION_SELECTION.md`
- `models/football/procedures/FOOTBALL_REQUIRED_COMPETITION_COVERAGE.md`
- `models/football/procedures/FOOTBALL_WOMENS_TOP_FLIGHT_COVERAGE.md`
- `models/football/procedures/FOOTBALL_REPAIRED_HANDOFF_AUTHORITY.md`
- `models/football/procedures/FOOTBALL_STEP1_BOARD_RECONCILIATION.md`
- `models/football/procedures/FOOTBALL_CAPACITY_REPLENISHMENT.md`
- `models/football/procedures/FOOTBALL_RANK_TERMINAL_STATUS.md`
- `models/football/procedures/FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md`

Use the attached `AISCORE_FIXTURES_*.zip` / repaired Step-0 handoff as the frozen intake.

## 0. Machine handoff validation

For `football-step0-handoff-v2`, require root-level:

`STEP0_HANDOFF.json`

Run:

`python models/football/engine/step0_handoff_cli.py --input STEP0_HANDOFF.json --consumer rank`

Do not begin ranking if the validator fails.

Do not reconstruct:
- missing match IDs;
- missing capacity queue rows;
- missing queue ranks;
- missing frozen operational fields.

Return the exact Step-0 validator error instead.

For a transitional completed bounded handoff created before source-manifest persistence was enforced, `--consumer rank` may return `source_manifest_status = LEGACY_MISSING_DISCOVERY_SEED_MANIFEST` or `LEGACY_MISSING_BLOCK_EXCLUDED_SUMMARY`. These are **audit-provenance warnings, not ranking blockers**, provided all final Step-0 production-universe, queue, coverage, operational, identity/time, count and work-readiness checks still pass. Do not send the user back through source acquisition merely to repair missing provenance metadata.

### Step-0 source-scope compatibility

The new FAST_PRODUCTION Step 0 may hand off either:
- `source_scope = EXACT_DATE_UNIVERSE`; or
- `source_scope = BOUNDED_PRODUCTION_DISCOVERY`.

For `BOUNDED_PRODUCTION_DISCOVERY`, require the machine handoff validator to confirm:
- `source_transport = MULTISOURCE_BOUNDED_PRODUCTION_DISCOVERY`;
- `coverage_mode = FALLBACK_PRODUCTION_SCOPE`;
- `global_raw_exact = false`;
- `production_scope_complete = true`;
- a frozen `discovery_seed_manifest` with at least two independent source families;
- exact `production_universe_count`;
- `block_excluded_summary`.

Once that bounded Step-0 handoff passes, **do not restart source acquisition or demand an exact global raw fixture count in /rank**. Missing transitional source-manifest audit metadata must not discard an otherwise fully frozen, reconciled Step-0 production universe. Step 1 consumes the frozen production universe, complete A/B capacity queue, manifests, identities, kickoffs and dispositions exactly as packaged.

The weaker global-raw claim must not weaken Step-1 integrity: protected/required/women coverage, every plausible A/B candidate, queue ranks and fixture identity/time must already be exact before `work_ready=true`.

## 1. Repaired handoff authority

If the attached file is a completed repaired sweep, apply `FOOTBALL_REPAIRED_HANDOFF_AUTHORITY.md` **before any web research**.

Run the local repaired-handoff metadata normalizer first.

Once accepted:
- fixture identity is frozen;
- kickoff is frozen;
- Step-0 disposition is frozen;
- capacity queue membership/rank is frozen.

For an accepted repaired handoff, **do not re-verify kickoff/fixture identity on the web**.

A non-metadata contradiction discovered incidentally during football research must return:

`REPAIRED HANDOFF CONFLICT — RETURN TO STEP0 REPAIR`

Do not repair Step 0 inside /rank.

If required operational fields are absent:

`HANDOFF INCOMPLETE — STEP0 OPERATIONAL CONTRACT MISSING`

## 2. Required competition coverage preflight — fail closed

Require:
- `required_competition_manifest_version = required-competition-manifest-v1`;
- protected block `NED_EERSTE_DIVISIE` exactly once;
- status `CHECKED_WITH_FIXTURES` or `CHECKED_NO_IN_WINDOW_FIXTURES`;
- no `SOURCE_BLOCKED` protected block;
- fixture_count/list reconciliation;
- every listed fixture with a valid Step-0 disposition;
- `Required Competition Blocks Complete = true`.

Failure:

`HANDOFF INCOMPLETE — REQUIRED COMPETITION COVERAGE GAP`

Specific missing Eerste block:

`HANDOFF INCOMPLETE — NETHERLANDS EERSTE DIVISIE COVERAGE GAP`

Do not rank around a missing protected block.

## 3. Operational handoff gate

Before deep football research verify:
- the accepted Step-0 source scope is preserved and is not upgraded/downgraded by /rank;
- for bounded-production handoffs, `production_scope_complete=true` and `global_raw_exact=false` are preserved without attempting raw-universe reconstruction;
- initial admitted count <= 15;
- every admitted row is operational A/B;
- every admitted and capacity-deferred A/B row has:
  - `xi_expected`;
  - `market_observability`;
  - `team_news_observability`;
  - `operational_viability_reason`;
  - `competition_reliability_state`;
  - `competition_reliability_reason`;
- complete A/B capacity queue is present;
- Step0 Capacity Queue Rank values are unique, positive and contiguous;
- no C/D row appears in normal Work;
- senior women's top-flight counters/manifest reconcile;
- unresolved women count = 0.

CAUTION may cap a raw A to B. DEMOTED probation may only appear under the documented competition-reliability rule.

If this contract is incomplete, stop. /rank does not recreate missing Step-0 operational evidence.

## 4. Current-turn runtime precheck

Before deterministic board execution, apply:

`models/football/procedures/FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md`

with stage=`rank`.

Preserve:

`FOOTBALL_RUNTIME_EXECUTION_RECORD`

Do not infer Python/repository unavailability from a missing checkout or container network failure.

## 5. One common Step-1 research epoch

Perform one football research pass per admitted/replenished fixture and freeze the factual state **before** applying C or C2 policy.

Common evidence must cover, as available/applicable:
- recent competitive form;
- home/away route quality;
- carrier strength/self-funding;
- chance creation/access;
- finishing/service continuity;
- opponent leakage;
- continuation after first goal;
- failure/stall/control mechanisms;
- relevant H2H transferability;
- personnel/tactical integrity;
- competition/tournament context;
- qualification/relegation/draw/margin incentive;
- evidence confidence.

Every ranked fixture must carry a non-empty:

`common_evidence_basis`

Do not search differently for C and C2 after one model's provisional output is seen.

## 6. Tournament incentive — mandatory where applicable

When the match context makes tournament incentive material, establish before finalizing board state:
- competition stage/format;
- aggregate/table state;
- qualification/relegation state;
- draw utility;
- tiebreak/GD/margin relevance;
- simultaneous-result effects;
- home incentive;
- away incentive;
- net incentive effect.

If required fields remain LIMITED/UNKNOWN, use the documented fixture-local hold/incomplete disposition. Do not turn unresolved incentive into a normal actionable board state.

## 7. Football C official board

Football C creates the official:
- `C-PASS`;
- `C-WATCH`;
- `C-FOCUS`.

Freeze independently:
- C supported line;
- C supported-line basis;
- C board-state basis;
- completion mode;
- burden-completion quality;
- continuation quality;
- opponent leakage;
- burden stall risk;
- main failure.

The **Football C official board** is the only board that controls routine Step-2 workload.

### Clearing-goal funding

FOCUS is broader than FOLLOW.

For burdens requiring a third goal, especially O2.5/O2.75:
- identify who actually funds the clearing goal;
- do not treat "carrier can score two" as automatic evidence for goal three;
- do not treat a merely usable second route as automatic independent clearing-goal funding;
- require credible continuation beyond a natural 2-goal endpoint;
- downgrade the operational lane when the third-goal mechanism is not strongly funded even if the fixture remains C-FOCUS.

This **clearing-goal funding** check is part of current Football C selection/follow-through, not a retired-model reactivation.

## 8. Football C2 shadow board

Football C2 receives the same frozen common factual epoch but applies its own:
- route-quality selection floor;
- C2 ranking;
- independent C2 supported line;
- C2 board state/basis.

The **Football C2 shadow board** never controls official exposure or creates additional Step-2 workload.

Never:
- copy C supported line into C2;
- copy C completion labels into C2;
- infer a missing C2 board from C.

## 9. Deterministic C+C2 board pair

Materialize independent board payloads and run:

`python models/football/engine/board_pair_cli.py --c <c.json> --c2 <c2.json>`

Required success:

`BOARD ENGINE EXECUTION STATUS: EXECUTED_C_C2_BOARDS`

and:

`common_evidence_reconciled = true`

The pair must fail closed on:
- ranked-universe mismatch;
- common-evidence drift;
- C policy leakage into C2;
- incomplete semantic trace.

A failed pair blocks /rank completion until repaired from the same frozen evidence.

## 10. Official FOLLOW / RESERVE / STOP lane

After the C board is frozen, apply the Football C follow-through guard.

Lane meaning:
- `FOLLOW` — routine Step-2 attention;
- `RESERVE` — conditional only;
- `STOP` — no routine Step 2 without explicit user exception.

Operational capacity:
- maximum routine `FOLLOW = 6`;
- maximum retained `RESERVE = 4`;
- maximum routine FOLLOW at one exact kickoff minute = 2.

Exact-same-kickoff comparison is an operational allocation rule. It must not rewrite the underlying C state or predictive rank.

B-grade operational rows are capped at RESERVE.

## 11. Deterministic replenishment — mandatory

After each completed Step-1 wave compute:

`active_lane_count = FOLLOW + RESERVE`

If active_lane_count < 10 and prematch A/B rows remain in the frozen Step0 capacity queue, run:

`capacity_replenishment_cli.py`

Pull the lowest remaining Step0 Capacity Queue Rank values first.

For each replenished row persist:
- original Step0 Capacity Queue Rank;
- `Step1 Replenished = true`;
- `Replenishment Wave = 1, 2, ...`;
- replenishment reason.

**A STOP/PASS does not permanently consume one of the original 15 research slots**.

Continue until:
1. FOLLOW + RESERVE reaches 10;
2. no eligible prematch deferred A/B row remains; or
3. all remaining queued rows have started/left the prematch window.

Do not use model appeal, supported total, expected goals or result knowledge to choose replenishment order.

## 12. Rank terminal status

After replenishment reaches a stop condition, run the deterministic rank terminal-status check.

A board may complete with:
- no ranked eligible fixtures;
- 0 FOLLOW;
- fewer than 10 active lanes if no eligible deferred row remains.

Integrity failure is different from a legitimately sparse board.

Do not label a valid empty/zero-FOLLOW board as blocked merely because it has no actionable match.

## 13. Persistence

Persist every ranked fixture before declaring /rank complete.

Current active fields include:
- frozen Step-0 source scope / coverage mode / source transport provenance;
- common evidence basis;
- C state/rank;
- C supported line + basis;
- C board-state basis;
- C completion/continuation/stall diagnostics;
- C2 state/rank;
- C2 supported line + basis;
- C2 board-state basis;
- official FOLLOW/RESERVE/STOP lane;
- Step0 Capacity Queue Rank;
- Step1 replenishment fields where applicable;
- board-pair reconciliation status;
- runtime/source revision.

Do not populate new C3/C4 current fields. Existing historical C3/C4 fields remain untouched on historical rows.

If current persistence fails:

`PERSISTENCE SYNC FAULT — /RANK INCOMPLETE`

## 14. Result/accounting isolation

/rank is prospective.

Do not inspect FT/result knowledge to:
- promote/demote a fixture;
- reorder ranks;
- choose replenishment;
- set supported burden;
- assign FOLLOW/RESERVE/STOP.

Step-1 WATCH accounting for current active models is compiled later under `FOOTBALL_MODEL_BET_ACCOUNTING.md`.

C2 remains shadow-only.

## 15. Completion output

A complete /rank response must include:
- board window;
- admitted/replenished counts;
- Football C official ranks/states/lines;
- official FOLLOW/RESERVE/STOP lanes;
- Football C2 shadow ranks/states/lines;
- board-pair execution/reconciliation status;
- capacity/replenishment status;
- terminal status;
- exact holds/integrity blockers if any;
- persistence status.

Do not display C3/C4 as current tracks.

Historical C3/C4 records may appear only in an explicitly historical audit/report.
