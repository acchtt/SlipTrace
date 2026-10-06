# Football Step-0 Source Acquisition / Production-Discovery Gate

**Status:** ACTIVE  
**Effective:** 2026-10-06 ICT  
**Applies to:** Step 0 `/sweep` before senior discovery  
**Primary fixture authority:** AiScore when available  
**Default mode:** FAST_PRODUCTION  
**Strict mode:** FULL_AUDIT

## Purpose

Step 0 must be trustworthy **and usable**.

The source layer has two jobs:
1. prefer an exact date-level fixture universe when the runtime can obtain one;
2. when exact date transport is unavailable in FAST_PRODUCTION, obtain enough independent current evidence to run a bounded production-scope discovery without pretending the global raw universe is exact.

The source gate must fail closed on **coverage integrity**, not on one provider or one transport mechanism.

The normal execution shape is:

`SOURCE ACQUISITION -> DISCOVERY -> RECONCILIATION -> PACKAGING`

The source layer may produce either:
- `EXACT_DATE_UNIVERSE`; or
- `BOUNDED_PRODUCTION_DISCOVERY`.

Only FULL_AUDIT requires the exact-date path.

For `/sweep repair ...`, apply `FOOTBALL_SWEEP_REPAIR_MODE.md`: reuse a valid previously acquired source epoch and only revalidate the finite repair set. Repair mode must not restart broad acquisition/discovery when the target run already has a valid source base.

## 1. Exact-date universe — preferred path

For each listing date required by the active time-integrity mode, try in order:

1. a reusable COMPLETE covering sweep / persisted source payload;
2. native AiScore date acquisition;
3. approved direct-date fallback carriers.

Preferred exact-date fallback order:
- FootballFixtures.org: `https://www.footballfixtures.org/fixtures/YYYY-MM-DD`;
- FootballInfo: `https://www.footballinfo.net/Fixtures?date=YYYY-MM-DD`;
- LivescoresX: `https://livescoresx.com/fixtures/YYYY-MM-DD`;
- LiveScore date surface;
- Flashscore date/all-matches surface;
- Soccerway date/fixtures surface.

### Search-to-open transport recovery

For an HTML date carrier:
- navigate the literal date URL first;
- if literal navigation returns `Invalid URL`, cache miss, stale generic page, or another transport-local failure, run **one** domain-scoped exact-date search;
- use that search only to locate the canonical provider/date result;
- OPEN the returned result;
- accept it only if OPEN returns the full canonical date page.

A search/index snippet alone never proves completeness.

Persist carrier provenance as:
- `DIRECT_DATE_URL`; or
- `SEARCH_LOCATED_FULL_PAGE`.

A failure from one provider is never terminal by itself.

### Exact carrier acceptance

A date carrier must identify the requested date and expose enough fixture rows/identity to reconcile the date universe.

For FootballFixtures.org:
- requested date must be visible;
- declared `All N` must be visible;
- enumerated fixture rows must reconcile to `All N`.

On mismatch:

`DATE_CARRIER_COUNT_MISMATCH`

and continue to the next carrier.

When exact acquisition succeeds, persist:
- `source_acquisition_state = ACQUIRED`;
- `source_scope = EXACT_DATE_UNIVERSE`;
- source transport/provenance;
- source payload/manifest hash;
- listing dates;
- acquisition timestamp.

Then continue to `DISCOVERY_CLASSIFICATION`.

## 2. FAST_PRODUCTION bounded production-discovery fallback

If no exact date universe is obtainable after the bounded carrier pass, **FAST_PRODUCTION must not stop merely because the transport layer is weak**.

Instead, switch immediately to:

`source_scope = BOUNDED_PRODUCTION_DISCOVERY`

and:

`source_transport = MULTISOURCE_BOUNDED_PRODUCTION_DISCOVERY`

This is the replacement for the audit-era all-or-nothing pre-discovery hard gate.

### 2.1 Minimum source seed

For each required listing date or requested bounded terminal interval, establish at least **two independent current discovery surfaces** from different provider/source families.

Allowed discovery surfaces include:
- current provider/date search indexes;
- provider competition/date pages;
- official league/competition schedules;
- official club/association fixture pages;
- opened full provider pages;
- other current fixture indexes with identifiable date/competition/teams.

Search snippets are allowed **only as discovery seeds** in this mode. They do not prove global completeness, kickoff authority, or omission.

Persist a `discovery_seed_manifest` containing:
- listing date / terminal interval;
- source family;
- query/page reference;
- competition/block identities found;
- candidate fixture identities where visible;
- acquisition time;
- disagreements.

The source families must be independent. Two pages from the same provider count as one source family.

### 2.2 What this fallback may and may not claim

This fallback may:
- discover candidate senior competition blocks;
- identify candidate fixtures for exact follow-up;
- seed required/protected/women coverage checks;
- proceed to operational/researchability classification.

It may **not** claim:
- exact global raw fixture count;
- complete all-level date enumeration;
- proof that a competition omitted by every seed source does not exist.

Set:
- `global_raw_exact = false`;
- `coverage_mode = FALLBACK_PRODUCTION_SCOPE`;
- `production_scope_complete = false` until final reconciliation.

### 2.3 Acquisition state in bounded mode

Once the minimum two-source seed is frozen, source acquisition is considered sufficient to begin production discovery:

- `source_acquisition_state = ACQUIRED`;
- `source_scope = BOUNDED_PRODUCTION_DISCOVERY`;
- `source_transport = MULTISOURCE_BOUNDED_PRODUCTION_DISCOVERY`;
- `source_payload_hash` = hash of the normalized discovery-seed manifest.

This does **not** mean the full date universe is known. It means Step 0 has enough independent current evidence to begin bounded production-scope discovery.

The distinction is carried by `source_scope`, `coverage_mode`, and `global_raw_exact`.

## 3. Bounded production-scope discovery requirements

In `BOUNDED_PRODUCTION_DISCOVERY`, broad discovery must remain finite and auditable.

For every competition/block appearing on **any** seed source:
- classify senior/non-senior;
- preserve the block identity/provenance;
- enumerate fixtures if the block could plausibly contain an A/B operational candidate;
- record a block-level exclusion reason when it is clearly outside production scope.

Fixture-level exactness is mandatory for:
1. protected senior competition blocks;
2. required-competition manifest blocks;
3. senior women's domestic top-flight blocks surfaced by any seed/corroborator;
4. any fixture that could plausibly receive operational grade A/B;
5. all admitted/capacity-deferred fixtures.

Obvious youth/Uxx, academy, reserve-only, regional/state, school/university/company, amateur/micro, or clearly non-operational blocks may be closed at block level.

Do not use predictive attractiveness, expected goals, supported total, or later result knowledge to decide what gets enumerated.

## 4. Mandatory corroboration / integrity checks

Before `work_ready=true` in bounded mode:

- every candidate senior block found by one discovery source must be checked against at least one independent current source when material;
- protected/required competition blocks must reconcile exactly under `FOOTBALL_REQUIRED_COMPETITION_COVERAGE.md`;
- senior women's top-flight blocks surfaced by the source set must reconcile exactly under `FOOTBALL_WOMENS_TOP_FLIGHT_COVERAGE.md`;
- every plausible A/B candidate must have fixture identity and kickoff verified;
- material source disagreement must be resolved or the affected block marked `UNRESOLVED`;
- unresolved count must be zero for work readiness.

A missing exact global raw count is acceptable in bounded mode. A missing plausible A/B candidate disposition is not.

## 5. Completeness semantics

### EXACT_DATE_UNIVERSE

`complete=true` means the acquired date universe and all potentially relevant senior fixtures reconcile through one Step-0 disposition.

### BOUNDED_PRODUCTION_DISCOVERY

`complete=true` means **production-scope completeness**, not exact global raw completeness.

Required:
- `global_raw_exact=false`;
- `production_scope_complete=true`;
- every surfaced/required/protected/women block reconciled;
- every plausible A/B senior candidate has a fixture-level disposition;
- required competition manifest complete;
- women top-flight manifest complete for surfaced blocks;
- unresolved=0;
- capacity queue complete.

Persist:
- exact `production_universe_count`;
- `block_excluded_summary`;
- discovery seed manifest/provenance.

This is intentionally the same production-scope concept already used by fallback Step 0. The audit must not convert missing exact global raw enumeration into a terminal source failure.

## 6. When SOURCE_BLOCKED is legitimate

In FAST_PRODUCTION, SOURCE_BLOCKED is now a **last-resort transport/discovery failure**, not the normal result of losing a master date page.

It is allowed only when:
- no exact carrier succeeds **and**
- fewer than two independent current discovery source families can be established for the requested date/window, or the web/source runtime itself is materially unavailable.

Do not SOURCE_BLOCK because:
- AiScore is unavailable;
- one or several direct date URLs return cache miss/Invalid URL;
- a date carrier cannot prove `All N`;
- search is available but exact date-page transport is not.

FULL_AUDIT may still fail closed when an exact date universe is required.

## 7. Bounded retry / recovery lease

Also apply `FOOTBALL_SWEEP_CHECKPOINT_EXECUTION.md`.

For exact-carrier acquisition, one invocation may attempt:
- one covering-cache check;
- one native AiScore attempt;
- one bounded fallback carrier pass.

If those fail in FAST_PRODUCTION, **switch to bounded production discovery in the same invocation** instead of entering a retry loop.

SOURCE_BLOCKED recovery leasing is used only when even the minimum two-source production-discovery seed cannot be established.

Persist on a true SOURCE_BLOCKED state:
- `source_blocker_fingerprint`;
- `source_last_attempt_at`;
- `source_retry_not_before = source_last_attempt_at + 30 minutes`;
- `source_recovery_attempt_count`.

Use:
- `sweep_checkpoint_cli.py source-retry`;
- `sweep_checkpoint_cli.py source-blocked`.

Changed source/config/procedure/runtime conditions retry immediately. An unchanged true blocker may retry once after the lease expires.

## 8. Cross-midnight FAST_PRODUCTION

Do not require the entire next provider calendar date when the requested next-day portion is only a bounded terminal interval.

If an exact primary date universe exists, the existing <=6-hour terminal-interval proof may be used.

If operating in `BOUNDED_PRODUCTION_DISCOVERY`, run the same two-source discovery/corroboration logic only across the requested terminal interval.

Persist:
- terminal interval ICT/UTC;
- source families checked;
- candidate fixture/block manifest;
- disagreement/unresolved state;
- `terminal_scan_complete=true` only when the requested interval is reconciled.

## 9. Search/index rule

The old audit rule — “search/index can never contribute to source acquisition” — is retired for FAST_PRODUCTION.

Current rule:

- search/index may **seed bounded production discovery**;
- search may locate a canonical full carrier page;
- search snippets may never prove exact global completeness;
- search snippets may never provide final authoritative kickoff on their own;
- fixture/competition identity must be verified before admission;
- final work readiness depends on reconciliation, not on snippet volume.

Do not manually build a cosmetic all-fixture master list merely to imitate an exact date carrier.

## 10. Match-page verification

Once the source scope is acquired, apply `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`.

Use targeted canonical/provider/official pages for:
- candidate A/B fixtures;
- boundary fixtures;
- missing/conflicting kickoff;
- suspicious timestamp collisions;
- protected/required/women blocks;
- identity/status conflicts.

Do not reopen every clearly excluded low-observability fixture.

## 11. Persistence contract

Persist when supported:
- `source_acquisition_state = UNTRIED / ACQUIRED / SOURCE_BLOCKED`;
- `source_scope = EXACT_DATE_UNIVERSE / BOUNDED_PRODUCTION_DISCOVERY`;
- `source_transport`;
- `source_attempt_count`;
- `source_payload_hash`;
- `source_acquired_at`;
- `global_raw_exact`;
- `coverage_mode`;
- `production_scope_complete`;
- `discovery_seed_manifest`;
- blocker/recovery fields only when truly SOURCE_BLOCKED.

Run Status remains a separate enum:
- UNTRIED -> RUNNING;
- ACQUIRED -> RUNNING;
- SOURCE_BLOCKED -> BLOCKED.

Never write `SOURCE_BLOCKED` into Run Status.

## 12. Output behavior

### ACQUIRED / EXACT_DATE_UNIVERSE

Continue normal Step 0.

### ACQUIRED / BOUNDED_PRODUCTION_DISCOVERY

Continue normal Step 0 in `FALLBACK_PRODUCTION_SCOPE`.

Do **not** tell the user the sweep is source-blocked merely because exact-date carrier transport failed.

### SOURCE_BLOCKED

Return:

`HANDOFF INCOMPLETE — SOURCE DISCOVERY BLOCKED`

Only when both exact carrier acquisition and the minimum bounded two-source production-discovery seed are unavailable.

Do not emit a Work ZIP until reconciliation/packaging passes.
