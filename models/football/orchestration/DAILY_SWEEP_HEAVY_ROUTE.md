# Orchestrated Daily Sweep — Heavy Route

**Status:** EXPERIMENTAL workflow trial  
**Purpose:** preserve full structural quality while moving repetitive collection/reconciliation work away from the Main Agent.  
**Model authority:** always read `models/football/CURRENT_MODEL.md` first.

## Invocation

Run from the SlipTrace project with the orchestration workflow enabled:

```text
use heavy route. Run the football orchestrated daily sweep using models/football/orchestration/DAILY_SWEEP_HEAVY_ROUTE.md and the attached/current AISCORE fixture handoff. Preserve the active CURRENT_MODEL exactly. Workers are evidence-only; the Main Agent is the only football judge.
```

Do not start if the required AiScore handoff is missing or fails the active handoff/scope integrity checks.

## 0. Main-Agent authority load

Before spawning workers, the Main Agent reads:

1. `models/football/CURRENT_MODEL.md`;
2. every stage-relevant current procedure/rule required by its load order;
3. `models/football/orchestration/README.md`;
4. `models/football/orchestration/WORKER_CONTRACTS.md`.

The Main Agent records the active official model version in the run manifest. Never infer it from this file.

If the user explicitly invokes UEFA Youth League/U19 trial work, additionally load the current trial file declared by `CURRENT_MODEL.md`. Otherwise youth remains outside the normal actionable board.

## 1. Companion — create compact run manifest

Spawn one Companion first.

Task:

- summarize the active model/procedure paths needed for this stage;
- record the requested ICT window;
- identify the active competition-scope files;
- record whether this is NORMAL SENIOR or explicit UYL TRIAL;
- maintain a compact checklist of worker batches and returned packets.

The Companion must not inspect bookmaker odds, confirmed XI, grade matches, or rank candidates.

Return a compact manifest only.

## 2. Scope Executor — validate handoff mechanically

Spawn one Default Executor using Contract A.

Task:

- validate source = AiScore;
- validate time/window identity and completeness metadata;
- apply only explicit current scope/registry rules;
- verify that pre-Work exclusions remain excluded;
- produce the Work-admitted fixture list and reconciliation counts.

If scope integrity fails, the Main Agent stops the heavy sweep with:

`HANDOFF SCOPE FAULT`

Do not waste deep research on a malformed handoff.

## 3. Partition research batches

The Main Agent groups Work-admitted fixtures into independent research batches.

Default target:

- 3–6 fixtures per Investigator when sources/data are straightforward;
- 1–3 fixtures when the match is unusually complex;
- avoid one Investigator per match unless the slate is tiny or the match needs isolated research.

Batch by competition or data-source overlap when that reduces duplicated browsing, but do not let league reputation substitute for match-level evidence.

## 4. Parallel Investigators — price/XI-blind evidence collection

Spawn as many Investigators as needed, within efficient batching limits, using Contract B.

Each Investigator researches its assigned batch deeply enough to support the active model, including where available:

- season and relevant recent GF/GA;
- scoring 2+ and conceding 2+ frequency;
- home/away splits;
- independent scoring-route evidence for each side;
- self-funding 3+ / carrier-ceiling evidence;
- chance-quality support;
- competition/incentive context;
- likely structural failure evidence;
- XI sensitivity from normal team structure, without using confirmed XI;
- source quality and unknowns.

### Hard prohibitions

Investigators must not:

- use bookmaker totals/prices;
- use user-supplied confirmed XI at this PRE stage;
- assign official grade/type/tier/rank;
- say LOCK/HOLD/PASS as a betting action;
- use current/final results when researching an already-started fixture as if they were prematch evidence;
- add fixtures that were not in the AiScore handoff.

## 5. Companion — evidence consolidation

After investigators return, the Companion applies Contract C.

It may:

- deduplicate facts;
- flag contradictory sources;
- identify missing model-relevant evidence;
- compress reports into one packet per fixture.

It may not resolve the football judgment.

If a material evidence hole remains on a potentially strong candidate, the Main Agent may dispatch one targeted Investigator follow-up. Do not automatically re-run full research.

## 6. MAIN AGENT — authoritative PRE judgment

Only now does the Main Agent perform football-model reasoning.

For every Work-admitted fixture, apply the current official structural order exactly as defined by `CURRENT_MODEL.md` and its active rules.

The Main Agent must assign every admitted fixture exactly one frozen PRE disposition, including all required active fields such as:

- PRE grade;
- structural archetype/type;
- FOCUS / WATCHLIST / PASS / UNRESOLVED;
- primary route;
- secondary route;
- main failure mode;
- XI sensitivity;
- structural burden/ceiling fields required by the active model;
- official model version.

### Ranking

After every fixture has been judged, rank all FOCUS/WATCHLIST candidates under the active hierarchy.

Do not rank while only part of the slate has been judged unless the ranking is explicitly provisional.

Price cannot alter structural rank.

### Later-regime boundary

If the active model contains a post-XI regime such as EGE, preserve evidence needed for that later gate but do not classify the later regime during PRE unless `CURRENT_MODEL.md` explicitly changes the gate.

## 7. Coverage Tester — independent process validation

Spawn one Tester using Contract D.

Required PASS before persistence:

- every Work-admitted fixture judged exactly once;
- counts reconcile;
- no excluded fixture leaked back in;
- no odds/confirmed-XI contamination of PRE;
- required evidence/fields present;
- AiScore identity/time preserved.

If Tester returns FAIL, the Main Agent fixes only the identified process gap. Do not re-run the whole slate unless necessary.

## 8. Airtable Persistence Executor

Only after the Main Agent freezes PRE and the Tester passes, spawn one Default Executor using Contract E.

Read the active Airtable contract from the current load order, then batch-upsert the Main-Agent-finalized frozen state into the required coverage table.

This worker is copying state, not judging football.

After write, run a sync check against the frozen artifact.

If mismatch:

`PERSISTENCE / SYNC ERROR`

Preserve the Main-Agent frozen artifact as historical truth until the mismatch is corrected.

## 9. Final response

Return only the useful board summary:

- active official model version;
- raw/Work-admitted fixture counts;
- FOCUS count and ranked FOCUS board;
- compact WATCHLIST;
- PASS/UNRESOLVED counts without dumping routine rows;
- coverage tester PASS/FAIL;
- Airtable persistence PASS/FAIL;
- any material research/scope fault.

Do not print all investigator reports unless the user asks.

## Usage-control acceptance criteria

The orchestration trial is successful only if all are true:

1. structural board quality is not weaker than the existing full Work sweep;
2. every Work-admitted fixture still receives a genuine model judgment;
3. high-tier Main-Agent context is spent primarily on synthesis/ranking, not raw collection;
4. exclusion/scope coverage is fully auditable;
5. frozen PRE persists exactly;
6. worker parallelism does not create duplicate/contradictory official judgments.

Track observed usage and quality across multiple slates before replacing the existing production launcher.
