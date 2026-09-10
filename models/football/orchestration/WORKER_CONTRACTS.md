# Football Orchestration Worker Contracts

**Status:** EXPERIMENTAL  
**Authority:** `models/football/CURRENT_MODEL.md` and its active load order.  
**Purpose:** constrain delegated workers so parallelism reduces usage without creating multiple competing football judges.

## Universal worker rules

Every worker must:

- work only on explicitly assigned fixtures / lanes;
- preserve AiScore fixture identity from the supplied handoff;
- use `Asia/Ho_Chi_Minh` for normalized display time when time is needed;
- distinguish observed facts from inference;
- cite or identify the source for externally researched facts;
- state `UNKNOWN` rather than invent missing data;
- return compact structured output;
- avoid bookmaker odds and confirmed-XI evidence during PRE unless the Main Agent explicitly invokes a later-stage task;
- avoid final betting language.

Forbidden worker outputs during PRE:

- `A1`, `A2`, `B+`, `B`, or another official PRE grade;
- `TWO-SIDED`, `ELITE CARRIER`, `CARRIER-LED`, or another official archetype as a final classification;
- `FOCUS`, `WATCHLIST`, `PASS`, `UNRESOLVED` as a final board state;
- an official rank;
- `EGE` as a final regime classification;
- a recommended Asian-total line or price;
- `LOCK`, `HOLD`, `PASS` as a betting action.

Workers may report evidence *relevant to* those concepts, e.g. `evidence_for_independent_away_scoring_route`, but the Main Agent owns the classification.

---

## Contract A — Handoff / Scope Executor

### Input

- attached AiScore handoff;
- current model authority files;
- `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`;
- `FOOTBALL_SWEEP_SCOPE.md`;
- `FOOTBALL_LEAGUE_ENVIRONMENT_REGISTRY.md`.

### Job

Perform only deterministic validation and scope application.

### Return

```yaml
run:
  source: AiScore
  requested_window_ict: <value>
  handoff_complete: true|false
  time_integrity: PASS|FAIL
  scope_integrity: PASS|FAIL
counts:
  raw_received: <n>
  excluded_quality: <n>
  excluded_low_goal: <n>
  excluded_hard: <n>
  excluded_conditional_no_signal: <n>
  work_admitted: <n>
work_admitted_fixtures:
  - fixture_id: <AiScore identity>
    kickoff_ict: <time>
    competition: <name>
    home: <team>
    away: <team>
    admission_class: PRIORITY|NORMAL|CONDITIONAL_PASS|CUP_CONTINENTAL
excluded_fixtures:
  - fixture_id: <id>
    reason: <exact active exclusion reason>
faults:
  - <fault or NONE>
```

Do not structurally assess matches.

---

## Contract B — Match Research Investigator

### Input

A small batch of Work-admitted fixtures, ideally 3–6 when independent research is practical.

### Job

Collect the strongest available price/XI-blind evidence needed by the active model.

### Return per fixture

```yaml
fixture_id: <AiScore identity>
identity:
  competition: <name>
  home: <team>
  away: <team>
  kickoff_ict: <time>
team_profile:
  home_season_gf_ga: <fact or UNKNOWN>
  away_season_gf_ga: <fact or UNKNOWN>
  home_recent_gf_ga: <fact or UNKNOWN>
  away_recent_gf_ga: <fact or UNKNOWN>
  home_scoring_2plus_frequency: <fact or UNKNOWN>
  away_scoring_2plus_frequency: <fact or UNKNOWN>
  home_conceding_2plus_frequency: <fact or UNKNOWN>
  away_conceding_2plus_frequency: <fact or UNKNOWN>
  relevant_home_away_splits: <fact or UNKNOWN>
route_evidence:
  home_independent_scoring_route:
    evidence: <compact facts>
    confidence: HIGH|MEDIUM|LOW|UNKNOWN
  away_independent_scoring_route:
    evidence: <compact facts>
    confidence: HIGH|MEDIUM|LOW|UNKNOWN
carrier_evidence:
  home_self_funding_3plus_evidence: <compact facts or NONE>
  away_self_funding_3plus_evidence: <compact facts or NONE>
chance_quality:
  home: <big chances/xG/xGOT/box access/etc or UNKNOWN>
  away: <same>
context:
  competition_incentive: <fact/inference>
  tactical_context: <fact/inference>
failure_evidence:
  - <candidate failure mode evidence>
xi_sensitivity_evidence:
  - <which routes/personnel appear sensitive, without using confirmed XI>
data_confidence: HIGH|MEDIUM|LOW
unknowns:
  - <missing item>
sources:
  - <source + what it supports>
```

Do not output a match recommendation.

---

## Contract C — Evidence Consolidation Companion

### Input

- worker research packets;
- current run manifest.

### Job

Compress duplicate facts, flag contradictions, and prepare one clean evidence packet per fixture for Main-Agent judgment.

### Return

```yaml
fixture_id: <id>
verified_core_facts:
  - <fact>
conflicting_evidence:
  - <conflict or NONE>
missing_model_relevant_evidence:
  - <item or NONE>
source_quality_flags:
  - <flag or NONE>
research_packet_complete: true|false
```

The Companion must not grade, rank, or recommend.

---

## Contract D — Coverage Tester

### Input

- scope executor counts;
- Main-Agent frozen PRE artifact;
- active coverage rules.

### Job

Verify process integrity after Main-Agent judgment.

### Tests

1. Every Work-admitted fixture has exactly one frozen PRE disposition.
2. No pre-Work exclusion appears in FOCUS/WATCHLIST/PASS as a structurally screened fixture.
3. `Work-admitted = Focus + Watchlist + Pass + Unresolved`.
4. No bookmaker price or confirmed-XI evidence influenced PRE.
5. Each FOCUS/WATCHLIST item has route evidence, main failure mode, and XI-sensitivity state required by the active model.
6. Fixture identity/time is consistent with the AiScore handoff.
7. No worker decision was copied as an official Main-Agent verdict without Main-Agent judgment.

### Return

```yaml
coverage_test: PASS|FAIL
count_reconciliation: PASS|FAIL
pre_leakage_test: PASS|FAIL
identity_time_test: PASS|FAIL
required_fields_test: PASS|FAIL
faults:
  - <fault or NONE>
```

The Tester may reject a malformed run but may not change a football verdict.

---

## Contract E — Airtable Persistence Executor

### Input

Only the Main-Agent-finalized frozen state plus the active Airtable contract.

### Job

Construct and write/update the appropriate Airtable records. This is a persistence task, not a second screen.

### Rules

- copy the Main-Agent state exactly into the active contract;
- upsert when required; do not create duplicate fixture/model/slate rows;
- do not read Website Picks during structural PRE;
- do not create Decision States during structural PRE unless the active contract explicitly requires it;
- never mutate frozen PRE based on later XI/price/live information;
- if the persisted row differs from the Main-Agent artifact, report `PERSISTENCE / SYNC ERROR`.

### Return

```yaml
write_status: PASS|FAIL
rows_created: <n>
rows_updated: <n>
duplicates_prevented: <n>
sync_check: PASS|FAIL
faults:
  - <fault or NONE>
```

---

## Contract F — Audit Result / Settlement Executor

### Input

- requested slate records;
- actual FT results from approved verification sources;
- active settlement rules;
- actual official Website Picks only for exposure settlement.

### Job

Perform routine factual result retrieval and settlement math.

### Return

```yaml
fixture_id: <id>
final_score: <score>
status_verified: true|false
official_exposure: <line/odds/stake or NONE>
settlement: WIN|HALF_WIN|PUSH|HALF_LOSS|LOSS|NO_OFFICIAL_EXPOSURE
pl_units: <number>
source: <result source>
```

No model lesson may be inferred here.

---

## Contract G — Audit Anomaly Investigator

### Input

Only anomalies selected by the Main Agent, such as losses, repeated false negatives, burden/regime questions, ranking misses, or process faults.

### Job

Research what happened without hindsight-rewriting frozen state.

### Return

```yaml
fixture_id: <id>
historical_state:
  model_version: <version>
  frozen_pre: <stored state>
  later_decisions: <stored material states>
observed_outcome_evidence:
  - <facts>
available_at_decision_time:
  - <facts that were knowable then>
only_known_afterward:
  - <facts that are hindsight only>
possible_error_lanes:
  process: <evidence or NONE>
  model: <evidence or NONE>
  information: <evidence or NONE>
  execution: <evidence or NONE>
  variance: <evidence or NONE>
  fixture_filter_schedule: <evidence or NONE>
  price_burden_regime: <evidence or NONE>
  persistence_sync: <evidence or NONE>
sources:
  - <source>
```

Do not recommend a rule change. The Main Agent owns learning decisions.

---

## Contract H — XI / Odds Support Worker

Use only when the Main Agent wants mechanical extraction from user-supplied screenshots/text.

### Job

Extract exactly what is visible/supplied:

```yaml
fixture_id: <id>
xi:
  home_starters: <visible list>
  away_starters: <visible list>
  formations: <visible values or UNKNOWN>
  bench_visible: true|false
odds:
  - line: <exact supplied Asian total>
    over_price: <exact supplied decimal price>
    under_price: <if visible>
extraction_uncertainty:
  - <item or NONE>
```

Do not infer missing players, odds, roles, or prices. Do not issue the final XI rerank or betting action.

---

## UYL / youth trial boundary

Normal workers must apply the active senior-quality exclusion. If the user explicitly invokes the UEFA Youth League/U19 trial, the Main Agent must load `models/football/trials/UEFA_YOUTH_LEAGUE_TRIAL.md` and label the entire run as a separate trial. Trial workers may use competition-relative high-line evidence defined there, but their output still remains evidence-only and cannot enter official senior P/L unless `CURRENT_MODEL.md` later changes that authority.
