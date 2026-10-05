# 00 — Normal Chat: AiScore Researchable Senior Intake

**Command alias:** `/sweep`

**Use in:** Normal Chat, high reasoning.

Read upstream `models/football/CURRENT_MODEL.md` first.

Football C is the active official model.

## Purpose

Build a trustworthy **OPERATIONALLY VIABLE, RESEARCHABLE SENIOR** AiScore universe for the requested window.

The objective is the middle ground between the old narrow allowlist and the later over-broad senior sweep:

- do not miss meaningful senior blocks such as international qualifiers;
- do not send obscure, weak-data competitions to Work when there is not enough current evidence to assess them responsibly.

Operational principle:

`AISCORE SOURCE ACQUISITION -> AISCORE SENIOR DISCOVERY -> HARD SCOPE FILTER -> OPERATIONAL VIABILITY GATE -> RESEARCHABILITY GATE -> CAPACITY GATE -> VERIFIED TIME/IDENTITY -> PACKAGE -> FOOTBALL C`

This intake is about **information quality and later executability**, not whether a competition is historically high-scoring.

Read and apply:
- `models/football/procedures/FOOTBALL_AISCORE_SOURCE_ACQUISITION.md`
- `models/football/procedures/FOOTBALL_SWEEP_CHECKPOINT_EXECUTION.md`
- `models/football/procedures/FOOTBALL_SWEEP_REPAIR_MODE.md` when the command is `/sweep repair ...`
- `models/football/procedures/FOOTBALL_OPERATIONAL_VIABILITY_GATE.md`
- `models/football/procedures/FOOTBALL_COMPETITION_RELIABILITY_MEMORY.md`
- `models/football/procedures/FOOTBALL_WOMENS_TOP_FLIGHT_COVERAGE.md`
- `models/football/procedures/FOOTBALL_REQUIRED_COMPETITION_COVERAGE.md`
- `models/football/procedures/FOOTBALL_CAPACITY_REPLENISHMENT.md`
- `models/football/airtable/FOOTBALL_COMPETITION_RELIABILITY_AIRTABLE.md`

The operational gate is mandatory for every surviving senior fixture before deep Work research.

## Default mode

`sweep_scope_mode=RESEARCHABLE_SENIOR_PRODUCTION`

If the command is `/sweep repair ...`:
- set `repair_mode=true`;
- do **not** execute the normal full discovery path for rows/blocks already complete in the target sweep;
- follow `FOOTBALL_SWEEP_REPAIR_MODE.md`;
- reuse the target run's source-acquisition state when still valid;
- build a finite repair set and stop when it is resolved/closed/unresolved;
- never keep browsing beyond the repair verification budget.

Do not use:
- legacy `NARROW_CORE` / PRIORITY-NORMAL-CONDITIONAL as the primary admission rule;
- unrestricted `BROAD_SENIOR_PRODUCTION`.

A prior sweep may be reused only if it was completed under RESEARCHABLE_SENIOR_PRODUCTION for a covering window.

## Checkpointed execution — mandatory

Fresh Step 0 is resumable.

For a new sweep:
- create/update the Sweep Runs row immediately after resolving the stable Run ID/window;
- set `Run Status = RUNNING`;
- initialize `Checkpoint Version = football-sweep-checkpoint-v1`;
- initialize `Sweep Chunk Number = 1`;
- persist `Resume Cursor` before opening expensive external research.

For `/sweep resume`:
- load the matching RUNNING Sweep Run first;
- continue from its `Resume Cursor`;
- reuse completed Daily Coverage rows and block evidence;
- never restart an unchanged ACQUIRED source epoch;
- never create a replacement Run ID merely because the previous chat turn ended.

External targeted verification is limited to **6 competition/date blocks per invocation**. Use:

`python models/football/engine/sweep_checkpoint_cli.py select --input <checkpoint.json>`

when deterministic execution is available.

After each externally verified block, persist its result and advance the cursor. When six external blocks have been processed and work remains, stop cleanly with:

`SWEEP CHECKPOINT SAVED — /sweep resume`

This is a normal RUNNING checkpoint, not `BLOCKED`, and no provisional Work ZIP is emitted.

Cheap source-local enumeration, hard exclusions, already-supported C/D block classifications, and persisted-state reads do not consume the six-block external budget.

## Source authority

AiScore remains the preferred fixture-discovery authority. When AiScore is technically blocked, the source-acquisition procedure may authorize the verified LiveScore + Flashscore/Soccerway multi-source fallback.

Before any senior-block discovery, pass `FOOTBALL_AISCORE_SOURCE_ACQUISITION.md`.

A complete source universe must be acquired through AiScore or the authorized multi-source fallback before broad discovery/reconciliation begins. Public search results, competition pages, team schedules, and other providers may verify **known** fixtures after acquisition but may not be used to reconstruct or certify the raw universe.

In repair mode, a previously acquired source universe/run may be reused as the base. Verification is limited to the finite repair set; do not perform broad web rediscovery.

If the source gate is `SOURCE_BLOCKED`, stop immediately with:

`HANDOFF INCOMPLETE — AISCORE SOURCE BLOCKED`

Do not spend later resumes repeating competition-by-competition reconstruction unless the persisted blocker fingerprint materially changed.

## Time / identity integrity

Resolve the requested ICT/UTC window once and follow:

`models/football/procedures/FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`

Every admitted fixture must have:
- resolved AiScore/provider identity;
- authoritative zoned kickoff;
- verified UTC;
- verified ICT;
- in-window proof.

Do not guess timezone from geography or treat a bare display clock as UTC.

In repair mode, verify only fixtures with missing/conflicting time/identity or fixtures expanded from a previously block-deferred A/B block. Once a known fixture's identity and zoned kickoff are authoritatively resolved with no contradiction, stop searching for that fixture.

## 1. Mandatory senior-block discovery

This section runs only after `source_acquisition_state=ACQUIRED` or a valid covering COMPLETE AiScore universe has been reused.

Before applying hard scope exclusions, enumerate all visible senior competition blocks in the requested AiScore window.

Senior women's domestic top-flight leagues are a **mandatory discovery class**. Every visible fixture from the country's highest senior women's domestic league must enter the raw senior accounting before any later operational/researchability/capacity disposition.

Do not skip a block because its competition label contains Women / Women's / Ladies / Frauen / Féminine / Femenina / Dam / Kvinner or equivalent.

If a visible women's senior top-flight block has no recorded fixture/disposition:

`HANDOFF INCOMPLETE — WOMEN TOP-FLIGHT COVERAGE GAP`

## 2. Hard scope exclusions

Exclude before the researchability gate:

- youth/Uxx-only competitions;
- academy/junior competitions;
- reserve/B/development-only competitions, except reserve-branded teams participating in a normal professional senior league;
- amateur or clearly semi-professional micro competitions with unreliable identity/data;
- regional/state/provincial competitions outside the intended senior professional universe;
- school/university/military/company competitions;
- friendlies/exhibitions unless explicitly requested;
- cancelled/postponed/abandoned/already-finished fixtures for an upcoming sweep;
- unresolved fixture identity/home-away;
- unresolved authoritative kickoff;
- duplicates.

## 3. Competition reliability memory — mandatory

After senior discovery/hard scope filtering and before final operational grading:

1. normalize a stable competition key;
2. read the matching row from Airtable `Competition Reliability` (`tbl1KShXxXErUdVKW`);
3. if no row exists, use `UNPROVEN`;
4. preserve any explicit Manual Override without inventing one;
5. calculate the raw current A/B/C/D grade from current evidence;
6. apply the deterministic historical cap from `FOOTBALL_COMPETITION_RELIABILITY_MEMORY.md`.

Historical state behavior:
- TRUSTED / NEUTRAL / UNPROVEN: no promotion and no cap;
- CAUTION: max B;
- DEMOTED: default C; allow at most one B-grade probation fixture from that competition in the sweep only when the raw current grade independently clears full A requirements.

Persist:
- `raw_operational_viability_grade`;
- `competition_reliability_state`;
- `competition_reliability_reason`;
- `competition_reliability_sample` when available;
- `competition_reliability_manual_override = NONE / <explicit override>`;
- `demoted_probation = true / false`;
- `operational_viability_grade` after the history cap.

Do not use FT score, goals, C/C2 result, betting result or P/L to set this state.

## 4. Operational viability gate — mandatory

For every fixture surviving hard scope/identity/time checks, persist:

- `operational_viability_grade = A / B / C / D`;
- `xi_expected = YES / UNCERTAIN / NO`;
- `market_observability = HIGH / MEDIUM / LOW / NONE`;
- `team_news_observability = HIGH / MEDIUM / LOW / NONE`;
- `operational_viability_reason`.

Apply the procedure exactly:

- A = normal executable candidate.
- B = conditional candidate; may be admitted after A but cannot be routine FOLLOW at board time.
- C = `LOW OPERATIONAL OBSERVABILITY — STEP0 EXCLUDED`.
- D = `NON-OPERATIONAL FIXTURE — STEP0 EXCLUDED`.

Do not upgrade a fixture because its score history looks attractive. Small-league status alone is not a rejection; missing XI/market/team-news observability is.

## 5. Protected senior competition classes

The following classes bypass the ordinary domestic researchability exclusion when identity/time are valid, but they still require an explicit operational viability grade:

- FIFA senior World Cup qualifiers/finals;
- senior continental national-team qualifiers/finals (AFCON, EURO, Asian Cup, Copa America/CONMEBOL, Gold Cup/CONCACAF, OFC equivalents);
- senior Nations League-style official national-team competitions;
- major senior continental club competitions administered by UEFA/AFC/CAF/CONMEBOL/CONCACAF/OFC;
- other clearly major senior international tournament blocks explicitly requested by the user.

These are protected because the previous narrow sweep missed meaningful national-team blocks.

They still receive normal Football C PASS/WATCH/FOCUS screening later.

## 6. Researchability gate — ordinary domestic / small competition blocks

For all other senior domestic league/cup fixtures, including men's and women's senior domestic top flights, run a **cheap researchability check** before admitting them to Work.

For senior women's top-flight fixtures, apply the same evidence standard as men's senior top-flight fixtures. Do not reinterpret "small/unfamiliar" as a gender proxy.

A fixture is `RESEARCHABLE` only when a quick preflight can establish enough current evidence for both teams to support the Football C evidence schema.

Minimum required evidence:

### Required A — recent team evidence
For **both teams**, at least one reliable source exposes a usable recent-match sequence/current form with opponents and scores.

### Required B — competition/context evidence
At least one reliable source exposes meaningful current competition context such as standings, phase/table, recent competition results, or equivalent tournament state.

### Required C — mechanism evidence
At least one of the following must be available without deep/manual hunting:

- team-level goal/chance profile;
- shots/SOT/box/chance-quality/xG-type statistics;
- reliable match/team statistical profiles;
- credible current team news/lineup/absence information that can materially inform routes;
- another repeatable quantitative or qualitative source sufficient to assess scoring mechanisms rather than only final scores.

### Required D — matchup/H2H availability
H2H is preferred when usable, but absence of H2H alone does **not** exclude a fixture.

However, if H2H is absent **and** mechanism evidence is weak, exclude.

### Admission rule

Admit when:
- Required A = PASS;
- Required B = PASS;
- Required C = PASS;
- fixture identity/time = PASS.

Otherwise exclude as:

`INSUFFICIENT RESEARCHABILITY — STEP0 EXCLUDED`

Do not spend deep Work research trying to rescue a competition that fails this cheap preflight.

## 7. What researchability is NOT

Do not exclude a fixture merely because:

- it is a senior women's domestic top-flight fixture;
- it is expected to be low scoring;
- its league was historically LOW-GOAL;
- it is from Japan or Finland;
- it is a professional lower division;
- it is a women's senior competition;
- it is unfamiliar;
- it is a cup.

If adequate current evidence exists, admit it and let Football C decide football quality.

Likewise, do not admit an obscure league merely because it is senior/professional if usable evidence is absent.

## 8. Efficiency rule

The researchability check must stay cheap and **competition-block shared**.

Normal limit per unfamiliar competition/date block:
- one acquired/provider competition/fixture surface;
- up to two quick public-web searches for current team/competition evidence.

Acquire those evidence surfaces once for the block and reuse them for every fixture/team they actually cover. Do not repeat the same standings/form/news/market search separately for each fixture in one league/date block.

Open a team- or fixture-specific source only when the shared block evidence does not cover that fixture's required A/B/C evidence.

The fixture-level admission standard is unchanged; only duplicate evidence acquisition is removed.

If those checks cannot establish A+B+C, exclude.

Do not turn Step 0 into the full Step-1 research process.

Under `FOOTBALL_SWEEP_CHECKPOINT_EXECUTION.md`, at most six blocks requiring external verification may be researched in one invocation. Batch independent web queries in the same tool call where supported.


### Block timestamp collision sentinel — mandatory

Before `work_ready=true`, inspect admitted fixtures within each competition/date block for suspicious timestamp reuse.

Trigger a hard revalidation when either condition holds:
- 3 or more distinct fixtures in the same competition/date have the exact same verified UTC kickoff; or
- a two-legged/repeat pairing within 14 days receives the same UTC kickoff as the previous leg without a current canonical match-page proof.

When triggered:
1. do not trust the batch timestamp;
2. reopen the current AiScore canonical match page for every affected admitted fixture;
3. verify current match ID, date, home/away and Match Info UTC/API epoch individually;
4. rebuild the affected kickoff fields before packaging;
5. label any mismatch `SOURCE TIME / BLOCK PARSER FAULT`.

A uniform competition-block timestamp is never sufficient proof by itself.

## 9. Operational capacity gate

After A/B viability and researchability are known, build the **complete fixture-level A/B capacity queue first**.

The 15-fixture limit is an **initial Work batch cap**, not a terminal slate exclusion.

### Global capacity queue

Every plausible A/B fixture must receive a deterministic `Step0 Capacity Queue Rank` before the first 15 are chosen.

Order by operational quality only:
1. A before B;
2. stronger XI expectation;
3. stronger market observability;
4. stronger team-news observability;
5. protected/required/major senior competition class only as an otherwise-equal operational tie-break;
6. canonical match identity as the final deterministic tie-break.

Kickoff discovery order, source-page order and block arrival order must never decide admission.

Never use Over profile, expected goals, C/C2/C3/C4 state, supported line, attractive odds or outcome knowledge to build the queue.

Initial Work handoff:
- queue ranks 1–15 -> `ADMITTED_TO_C`;
- queue ranks 16+ -> `OPERATIONAL_CAPACITY_DEFERRED`, **retained as the Step-1 replenishment queue**.

Persist queue rank for both admitted and deferred A/B fixtures.

### Fallback capacity short circuit

In `coverage_mode=FALLBACK_PRODUCTION_SCOPE`, block-level short-circuiting is allowed only for blocks that are already demonstrably **below the A/B candidate threshold**.

Do **not** short-circuit a block merely because 15 slots are already occupied.

Any block that could plausibly contain an A/B fixture must still be enumerated fixture-by-fixture and inserted into the global capacity queue. Protected competition blocks, required competition blocks and women's top-flight blocks remain fixture-exact regardless.

This prevents early blocks from permanently taking the 15 slots before later equal/stronger fixtures are seen.

Overflow remains recorded as:

`OPERATIONAL CAPACITY DEFERRED — STEP0`

but it is now a normal deterministic replenishment pool under Step 1 and does not require a user exception to reopen.

## 9A. Required competition-block manifest — mandatory

Independently of broad discovery, run `FOOTBALL_REQUIRED_COMPETITION_COVERAGE.md`.

Current protected block registry version:
`required-competition-manifest-v1`

At minimum, explicitly check:
- `NED_EERSTE_DIVISIE` — Netherlands Eerste Divisie / Keuken Kampioen Divisie.

Record exactly one:
- `CHECKED_WITH_FIXTURES`
- `CHECKED_NO_IN_WINDOW_FIXTURES`
- `SOURCE_BLOCKED`

If fixtures exist, enumerate every official in-window fixture before normal disposition rules.

Official Jong/U21/reserve-branded participants in the Eerste Divisie are senior league fixtures for coverage purposes and must not be dropped by generic reserve/youth-name exclusions.

If the block is absent/unresolved:

`HANDOFF INCOMPLETE — NETHERLANDS EERSTE DIVISIE COVERAGE GAP`

Do not set `work_ready=true`.

Run `validate_required_competition_manifest` from `models/football/engine/coverage_manifest.py` against the packaged manifest when execution is available.

## 10. Completeness

### Native/complete-date mode

When the native AiScore date universe or an equivalently complete fixture-level date payload is available, production completeness means:

> every potentially relevant senior block in the requested window was discovered, then hard-excluded, operationally excluded, researchability-excluded, capacity-deferred, or admitted.

### Multi-source fallback production-scope mode

When `source_transport = MULTISOURCE_FALLBACK_LIVESCORE_FLASHSCORE_SOCCERWAY`, do **not** force fixture-level enumeration of the entire all-level date page merely to produce a cosmetic global raw count.

Set:
- `coverage_mode=FALLBACK_PRODUCTION_SCOPE`;
- `global_raw_exact=false`;
- `production_scope_complete=true` only when all requirements below pass.

Fallback production-scope completeness requires fixture-level exactness for:
1. every protected senior competition block;
2. every required-competition manifest block;
3. every senior women's domestic top-flight fixture carried by the authorized fallback universe;
4. every fixture that survives hard-scope prefiltering and could plausibly receive operational grade A/B;
5. every admitted or capacity-deferred fixture.

Obvious youth/Uxx, academy, reserve-only, regional/state, university/school/company, amateur/micro, and clearly non-operational competition blocks may be summarized at **block level** with a hard/operational exclusion reason. They do not need one row per fixture in fallback mode.

This exception changes audit granularity only. It must not:
- hide a plausible A/B senior fixture;
- weaken protected/required/women coverage;
- permit a C/D fixture into Work;
- use predictive attractiveness to decide what is enumerated.

In fallback mode, `raw_senior_count` may be null/UNAVAILABLE rather than fabricated. Persist instead:
- `production_universe_count` = exact fixture count after block-level hard-scope prefiltering that required fixture-level disposition;
- `block_excluded_summary` = excluded competition blocks/categories with compact reasons.

`work_ready=true` is permitted with `global_raw_exact=false` only when `production_scope_complete=true`, required competition coverage is exact, women's top-flight coverage is exact, and every plausible A/B senior candidate has a fixture-level disposition.

Additionally:
- every visible senior women's domestic top-flight block must reconcile under `FOOTBALL_WOMENS_TOP_FLIGHT_COVERAGE.md`;
- every protected required competition block must reconcile under `FOOTBALL_REQUIRED_COMPETITION_COVERAGE.md`.

Missing either class is a coverage failure even when the overall raw/admitted totals otherwise balance.

A skipped visible senior block with no recorded disposition makes the handoff incomplete.

For cross-midnight/early-morning windows, perform the normal terminal-interval recheck.

## 11. Persistence / counts

Checkpoint persistence is part of normal execution, not only final packaging.

For every RUNNING sweep keep current:
- `Checkpoint Version`;
- `Sweep Chunk Number`;
- `Resume Cursor`;
- `Retry Queue`;
- `Pending Verification Blocks`;
- `Last Completed Block`;
- `Checkpoint Notes`;
- `Updated At`.

After each external block, persist completed fixture rows/dispositions before moving to the next block. A timeout after a successful checkpoint must not force already-completed blocks to be re-researched.

At the start of each resume chunk, close already-started/finished pending fixtures before spending external research budget on them.

For every discovered in-window senior fixture preserve one disposition:

- `ADMITTED_TO_C`
- `HARD_EXCLUDED`
- `OPERATIONAL_EXCLUDED`
- `RESEARCHABILITY_EXCLUDED`
- `OPERATIONAL_CAPACITY_DEFERRED`
- `UNRESOLVED`

Record researchability reason compactly.

Required funnel counts:

`RAW SENIOR -> HARD EXCLUDED -> OPERATIONAL EXCLUDED -> RESEARCHABILITY EXCLUDED -> CAPACITY DEFERRED -> ADMITTED TO C`

Required women's-top-flight counts:
- `women_top_flight_raw_count`;
- `women_top_flight_admitted_count`;
- `women_top_flight_operational_excluded_count`;
- `women_top_flight_researchability_excluded_count`;
- `women_top_flight_capacity_deferred_count`;
- `women_top_flight_unresolved_count`.

The women's-top-flight raw count must equal the sum of its dispositions.

Persist `women_top_flight_disposition_manifest` with every fixture in the class, including excluded/deferred fixtures. This manifest is audit metadata and does not add non-admitted fixtures to the Work array.

## 12. Work-readiness gate

Package only when:

- `complete=true`
- `actionable_complete=true`
- `work_ready=true`
- every visible senior block has a disposition;
- every admitted fixture is operational grade A or B;
- every admitted fixture has a competition reliability snapshot;
- every A/B capacity-queue fixture, whether `ADMITTED_TO_C` or `OPERATIONAL_CAPACITY_DEFERRED`, carries non-empty `xi_expected`, `market_observability`, `team_news_observability`, `operational_viability_reason`, `competition_reliability_state`, and `competition_reliability_reason`;
- no CAUTION fixture is admitted above B;
- no DEMOTED fixture is admitted except the allowed B-grade probation rule;
- admitted fixture count is <= 15;
- protected senior blocks were not removed by the researchability gate without an explicit operational disposition;
- every visible senior women's domestic top-flight block has a fixture-level disposition;
- `required_competition_manifest_version = required-competition-manifest-v1`;
- every protected required competition block is explicitly present and resolved;
- `Required Competition Blocks Complete = true`;
- women's-top-flight counts reconcile exactly;
- `women_top_flight_unresolved_count = 0` before `work_ready=true`;
- every admitted fixture has resolved identity/time;
- terminal scan is complete where required;
- admitted count equals handoff array count.

If any A/B queue fixture is missing the six-field Step-0 operational/reliability contract:

`HANDOFF INCOMPLETE — STEP0 OPERATIONAL CONTRACT MISSING`

Do not infer the missing semantic fields from competition reputation, operational grade, fixture name, or later Step-1 research.

For other completeness failures:

`HANDOFF INCOMPLETE — RESEARCHABLE SENIOR COVERAGE GAP`

## 13. Canonical ZIP handoff

Create one root-level canonical `AISCORE_FIXTURES_*.txt` inside the ZIP.

Required metadata:

- `model=Football C`
- `sweep_scope_mode=RESEARCHABLE_SENIOR_PRODUCTION`
- requested ICT/UTC window;
- listing dates checked;
- terminal scan state;
- `complete=true`;
- `actionable_complete=true`;
- `work_ready=true`;
- `raw_senior_count` when `global_raw_exact=true`, otherwise `global_raw_exact=false` + exact `production_universe_count` + `block_excluded_summary`;
- `hard_excluded_count` when fixture-exact, otherwise block-level exclusion summary;
- `operational_excluded_count`;
- `researchability_excluded_count`;
- `capacity_deferred_count`;
- `admitted_to_c_count`;
- protected-block audit result;
- women's-top-flight coverage audit result;
- all six women's-top-flight counters;
- `women_top_flight_disposition_manifest` listing every discovered women's top-flight fixture and disposition;
- admitted fixtures with identity/time provenance;
- complete deterministic A/B capacity queue for replenishment, including both admitted and capacity-deferred rows with unique `Step0 Capacity Queue Rank`;
- per admitted **and capacity-deferred A/B queue fixture**: raw operational grade, final operational grade, XI expectation, market observability, team-news observability, competition reliability state/sample/reason and operational reason.

Do not include hard-excluded, operationally excluded, or researchability-excluded fixtures in the Work array. Capacity-deferred fixtures remain outside the initial Work array but must stay in the packaged replenishment queue with the complete Step-0 contract.

## 14. Step-0 boundary

Step 0 may determine whether enough evidence exists.

It must **not** decide:

- route strength;
- carrier strength;
- chance quality;
- supported burden;
- C-PASS/WATCH/FOCUS;
- rank;
- BET/WAIT/PASS.

Those remain Football C/C2 Step-1/Step-2 decisions.

## Output

If the bounded chunk ends while external verification remains, return:

`SWEEP CHECKPOINT SAVED — /sweep resume`

with:
- Run ID;
- completed chunk number;
- current phase;
- blocks completed this chunk;
- pending verification block count;
- retry queue count;
- next block key;
- current counts when available;
- source acquisition state/transport.

Do not emit a ZIP in this state.

Only after final reconciliation + packaging pass, return:

`RESEARCHABLE SENIOR HANDOFF COMPLETE`

with:

- requested window;
- raw senior count when exact; otherwise `global_raw_exact=false` and exact production-universe count;
- women's top-flight raw / admitted / operational excluded / researchability excluded / capacity deferred / unresolved counts;
- hard excluded;
- operationally excluded;
- researchability excluded;
- capacity deferred;
- admitted to Football C;
- unresolved = 0;
- ZIP filename.
