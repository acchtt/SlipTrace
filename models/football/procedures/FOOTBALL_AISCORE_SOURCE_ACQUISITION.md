# Football AiScore Source Acquisition Gate

**Status:** ACTIVE  
**Effective:** 2026-10-04 ICT  
**Applies to:** Step 0 `/sweep` before senior discovery  
**Primary fixture authority:** AiScore  
**Fallback authority:** verified multi-source consensus (LiveScore date feed + Flashscore/Soccerway corroboration)

## Purpose

Prevent Step 0 from spending repeated resumes reconstructing a supposedly complete fixture universe from search snippets, league pages, or partial caches when the authoritative AiScore date universe is unavailable.

For `/sweep repair ...`, this source gate is applied through `FOOTBALL_SWEEP_REPAIR_MODE.md`: a valid previously acquired target sweep may be reused as the source base, and only the finite repair set is revalidated. Repair mode must not restart broad acquisition/discovery when the target run already has a valid acquired universe.

The gate is deliberately **bounded**:

`SOURCE ACQUISITION -> DISCOVERY`

No fixture research, women-block reconstruction, required-competition repair, operational grading, researchability work, capacity selection, or packaging may begin until source acquisition is either **ACQUIRED** or a covering previously COMPLETE AiScore universe is validly reused.

## 1. What counts as an acquired universe

An acquired source universe should represent the complete AiScore football listing for every listing date required by `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`. When AiScore is technically blocked, a verified alternate date-level universe may be used under the multi-source fallback below.

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

### C. Multi-source date-feed fallback

If B is technically unavailable, use this ordered alternate path:

1. LiveScore date-level football feed in the requested operational timezone as the fallback universe carrier;
2. Flashscore competition/match pages for fixture/date/time corroboration;
3. Soccerway competition fixture pages as a second independent corroboration source.

The alternate universe is accepted when:
- the LiveScore date feed covers the requested listing date and timezone;
- every protected required competition block is independently corroborated by Flashscore or Soccerway;
- every senior women's domestic top-flight block admitted/deferred is independently corroborated by Flashscore or Soccerway;
- any material provider disagreement is explicitly resolved or marked UNRESOLVED;
- no unresolved material block remains before work_ready=true.

Under fallback mode, provider-native IDs may replace AiScore IDs for raw-universe accounting, but preserve provider provenance. AiScore identity is no longer mandatory when AiScore itself is inaccessible.

Set:
`source_transport = MULTISOURCE_FALLBACK_LIVESCORE_FLASHSCORE_SOCCERWAY`.

If no valid alternate date-level universe can be established, stop as SOURCE_BLOCKED.

## 3. Bounded retry budget

This section governs fresh acquisition. Repair-mode verification has the stricter per-competition budget in `FOOTBALL_SWEEP_REPAIR_MODE.md` and must not expand into a fresh search loop.

Per run + source epoch, the normal acquisition budget is:

- one covering-cache/reuse check;
- one native AiScore date acquisition attempt;
- one alternate date-level multi-source fallback attempt.

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

Search engines, web snippets, team schedule pages, and competition pages may be used **after acquisition** to:

- verify a known fixture;
- repair a known identity/time conflict;
- assess researchability;
- establish team/competition context.

They may **not**, by themselves:
- create the raw fixture universe;
- prove an omitted competition does not exist;
- convert a lower-bound universe into an exact one;
- certify `complete=true`;
- substitute for either the AiScore date universe or the accepted LiveScore+Flashscore/Soccerway fallback universe.

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
