# Football AiScore Source Acquisition Gate

**Status:** ACTIVE  
**Effective:** 2026-10-04 ICT  
**Applies to:** Step 0 `/sweep` before senior discovery  
**Fixture authority:** AiScore only

## Purpose

Prevent Step 0 from spending repeated resumes reconstructing a supposedly complete fixture universe from search snippets, league pages, or partial caches when the authoritative AiScore date universe is unavailable.

The gate is deliberately **bounded**:

`SOURCE ACQUISITION -> DISCOVERY`

No fixture research, women-block reconstruction, required-competition repair, operational grading, researchability work, capacity selection, or packaging may begin until source acquisition is either **ACQUIRED** or a covering previously COMPLETE AiScore universe is validly reused.

## 1. What counts as an acquired universe

An acquired source universe must represent the complete AiScore football listing for every listing date required by `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`.

Preferred native endpoint:

`https://api.aiscore.com/v1/web/api/matches?lang=2&sport_id=1&date=YYYY-MM-DD&tz=07:00`

A browser-capable transport may be required because the endpoint can be Cloudflare/browser-context protected and protobuf encoded.

An acquisition is valid when the decoded payload preserves enough AiScore identity to reconcile the date universe, including at minimum:

- AiScore match/event ID;
- home and away identity;
- competition identity/name;
- source kickoff representation or epoch;
- match status.

A transformed transport is allowed only when it is demonstrably carrying AiScore data and preserves AiScore match identity and source timing. **Transport is not fixture authority.**

Examples of acceptable transport:
- direct AiScore date batch/API through an authorized browser/Playwright context;
- AiScore date-page/batch capture from the same current source epoch;
- an AiScore-derived browser proxy/crawler/cache that explicitly fetches the AiScore date endpoint and preserves AiScore IDs/timestamps;
- a previously persisted COMPLETE covering sweep that satisfies the reuse rules below.

## 2. Strict acquisition order

For each required listing date:

### A. Covering COMPLETE reuse

First check for a previously COMPLETE `RESEARCHABLE_SENIOR_PRODUCTION` sweep or exact persisted AiScore date payload that covers the requested interval and is still valid under the current time-integrity rules.

Reuse requires:
- complete source universe, not a lower bound;
- exact fixture-level identities;
- no unresolved/source-blocked competition block;
- exact women manifest;
- exact required-competition manifest;
- compatible listing date / same-end semantics required by the time procedure.

A lower-bound pack such as `60+`, `29+`, generic block rows, or `raw_audit_complete=false` is **not reusable**.

### B. Native AiScore date acquisition

Attempt the native AiScore date batch through the best available authorized browser-capable route.

Do not use a plain HTTP failure as evidence that the date has no fixtures.

### C. AiScore-derived transport fallback

If B is technically unavailable, try **one** alternate AiScore-derived transport that fetches the same date universe and preserves AiScore IDs/times.

The alternate transport must not create fixtures from another provider.

If no valid transport is available, stop as SOURCE_BLOCKED.

## 3. Bounded retry budget

Per run + source epoch, the normal acquisition budget is:

- one covering-cache/reuse check;
- one native AiScore date acquisition attempt;
- one alternate AiScore-derived transport attempt.

Do not loop through public search engines, dozens of competition pages, team schedules, or country-by-country reconstruction trying to simulate the missing master list.

When all three are exhausted:

`SOURCE ACQUISITION BLOCKED — AISCORE DATE UNIVERSE UNAVAILABLE`

Set:
- `complete=false`;
- `actionable_complete=false`;
- `work_ready=false`;
- discovery/reconciliation/packaging incomplete;
- exact raw counters unset rather than estimated.

## 4. Resume no-repeat rule

Persist a blocker fingerprint containing at least:

- requested window;
- listing date(s);
- current source-acquisition procedure revision;
- transport(s) attempted;
- normalized technical failure class.

On `/sweep resume`:

- if the run is SOURCE_BLOCKED and the blocker fingerprint is unchanged, **do not repeat acquisition or manual reconstruction**;
- return the stored source-blocked status immediately;
- retry only when at least one material condition changed:
  - a browser-capable transport became available/connected;
  - the user supplied an AiScore raw date payload/valid complete handoff;
  - a persisted complete source cache became available;
  - source date/window changed;
  - source-acquisition code/config/procedure changed.

A plain user `resume` does not itself count as a changed source condition.

## 5. Search/index prohibition for completeness

Search engines, web snippets, team schedule pages, competition schedule pages, and other score providers may be used **after acquisition** to:

- verify a known fixture;
- repair a known identity/time conflict;
- assess researchability;
- establish team/competition context.

They may **not**:
- create the raw fixture universe;
- prove an omitted competition does not exist;
- convert a lower-bound universe into an exact one;
- certify `complete=true`;
- substitute for the AiScore date universe.

This prevents a long manual reconstruction from being mistaken for exhaustive discovery.

## 6. Match-page verification stays targeted

Once the source universe is acquired, apply `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md` and the timestamp-collision sentinel normally.

Individual canonical AiScore match pages remain appropriate for:
- boundary fixtures;
- missing zoned time;
- identity/status conflict;
- suspicious block timestamp reuse;
- explicit parser-fault repair.

Do not reopen every fixture merely because the master batch used a shared displayed time when no sentinel condition is triggered.

## 7. Persistence contract

Persist these source-acquisition fields when the backing store supports them:

- `source_acquisition_state = UNTRIED / ACQUIRED / SOURCE_BLOCKED`;
- `source_transport`;
- `source_attempt_count`;
- `source_payload_hash` when a payload exists;
- `source_acquired_at`;
- `source_block_reason`;
- `source_blocker_fingerprint`.

If dedicated fields are unavailable, persist the same values in the run checkpoint before stopping.

The acquisition state belongs to the **run**, not individual fixtures.

## 8. Output behavior

### ACQUIRED

Continue Step 0 normally.

### SOURCE_BLOCKED

Return a compact terminal intake status:

`HANDOFF INCOMPLETE — AISCORE SOURCE BLOCKED`

Include:
- requested window;
- required listing dates;
- transports attempted;
- exact blocker;
- whether any complete covering cache was reusable;
- what material change would allow a retry.

Do not emit a Work ZIP.

Do not continue fixture-by-fixture reconstruction in the same run.

## 9. Relationship to protected/women coverage

Required competition and women top-flight manifests remain mandatory **after** the date universe is acquired.

They are independent completeness sentinels, not substitutes for source acquisition.

A locally repaired women/protected block does not make the global universe complete when the source gate is SOURCE_BLOCKED.
