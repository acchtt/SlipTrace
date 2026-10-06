# Football AiScore Source Acquisition Gate

**Status:** ACTIVE  
**Effective:** 2026-10-06 ICT  
**Applies to:** Step 0 `/sweep` before senior discovery  
**Primary fixture authority:** AiScore  
**Fallback authority:** verified date-level multi-source consensus. Preferred browser/server carrier: FootballFixtures.org date page; legacy LiveScore/Flashscore/Soccerway remain permitted; FootballInfo/LivescoresX may corroborate.

## Purpose

Prevent Step 0 from spending repeated resumes reconstructing a supposedly complete fixture universe from search snippets, league pages, or partial caches when the authoritative AiScore date universe is unavailable.

For `/sweep repair ...`, this source gate is applied through `FOOTBALL_SWEEP_REPAIR_MODE.md`: a valid previously acquired target sweep may be reused as the source base, and only the finite repair set is revalidated. Repair mode must not restart broad acquisition/discovery when the target run already has a valid acquired universe.

The gate is deliberately **bounded**:

`SOURCE ACQUISITION -> DISCOVERY`

No fixture research, women-block reconstruction, required-competition repair, operational grading, researchability work, capacity selection, or packaging may begin until source acquisition is either **ACQUIRED** or a covering previously COMPLETE AiScore universe is validly reused.

## 1. What counts as an acquired universe

An acquired source universe should represent the complete fixture listing for the **minimum listing-date set required by the active time-integrity mode**. In FAST_PRODUCTION, do not automatically require a second provider date universe merely because the ICT window crosses midnight. Acquire the primary listing date(s) needed for discovery, then prove any cross-midnight/terminal remainder with the bounded terminal-interval procedure below. FULL_AUDIT may require the broader date envelope from the time-integrity procedure.

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

1. acquire at least one **date-level fallback universe carrier** for each required listing date. Preferred order is now:
   - FootballFixtures.org `https://www.footballfixtures.org/fixtures/YYYY-MM-DD`;
   - LiveScore date-level feed/surface;
   - Flashscore date/all-matches surface;
   - Soccerway date/fixtures surface.
2. use an independent corroborator for protected/required blocks, women's top-flight blocks, and material identity/time disagreements. Preferred corroborators when reachable are FootballInfo `https://www.footballinfo.net/Fixtures?date=YYYY-MM-DD`, LivescoresX `https://livescoresx.com/fixtures/YYYY-MM-DD`, then the unused legacy providers above;
3. use another provider only when the first corroborator disagrees or does not cover a mandatory block.

A fallback carrier is acceptable only when it is a provider-level date/all-matches listing capable of enumerating the production senior scope. Search snippets and individually discovered fixture pages are not carriers.

### Direct-navigation + search-to-open rule for chat/web runtimes

For every permitted HTML date carrier, **navigate the literal date URL directly first**.

Primary exact URLs:
- FootballFixtures.org: `https://www.footballfixtures.org/fixtures/YYYY-MM-DD`
- FootballInfo: `https://www.footballinfo.net/Fixtures?date=YYYY-MM-DD`
- LivescoresX: `https://livescoresx.com/fixtures/YYYY-MM-DD`

If literal navigation succeeds, validate the returned full page normally.

If literal navigation returns a transport-local error such as `Invalid URL`, cache miss, stale generic page, or fetch failure, use **one search-to-open locator recovery** for that provider/date before abandoning it:

1. run a domain-scoped exact-date query for the provider/date;
2. use the search result **only to recover a canonical result reference/URL**;
3. OPEN the returned result;
4. accept it only if OPEN returns the **full date page content**, not a snippet, and the page satisfies that carrier's normal date/universe checks.

A search/index **snippet by itself** may never certify completeness. A search-located result that is subsequently opened into the full canonical date page is a normal webpage carrier and may certify completeness if its contents satisfy the same checks as literal navigation.

Persist transport provenance:
- `DIRECT_DATE_URL` when literal navigation worked;
- `SEARCH_LOCATED_FULL_PAGE` when search was only the locator and OPEN returned the complete canonical page.

If one provider still fails after its direct attempt plus one search-to-open recovery:
- do **not** immediately declare SOURCE_BLOCKED;
- attempt the next permitted date carrier;
- treat the failure as provider/transport-local, not as proof that the date universe is unavailable.

SOURCE_BLOCKED is allowed only after every currently permitted date carrier has been attempted in the bounded fallback pass and none produced an acceptable full-page universe.


### FootballFixtures.org carrier acceptance

FootballFixtures.org is accepted as a date-level carrier only from the direct date page, never from a search-result snippet. The page must:
- identify the requested calendar date;
- expose a declared `All N` fixture count;
- expose the date's fixture rows/links in the fetched page rather than only a teaser subset;
- allow the enumerated fixture count to reconcile to the declared `All N` count before `ACQUIRED` is set.

If the declared count and enumerated rows do not reconcile, classify that carrier attempt as `DATE_CARRIER_COUNT_MISMATCH` and continue to the next permitted carrier. Provider display time must not be treated as an authoritative timezone until the time-integrity procedure establishes its zone; the carrier may still establish fixture identity/universe membership while kickoff is separately verified.

The alternate universe is accepted when:
- every required listing date is covered by at least one valid fallback date-level carrier;
- every protected required competition block is independently corroborated by a different fallback provider;
- every senior women's domestic top-flight block admitted/deferred is independently corroborated by a different provider, preferring FootballInfo/LivescoresX/Flashscore/Soccerway according to coverage;
- any material provider disagreement is explicitly resolved or marked UNRESOLVED;
- no unresolved material block remains before work_ready=true.

Under fallback mode, provider-native IDs may replace AiScore IDs for raw-universe accounting, but preserve provider provenance. AiScore identity is no longer mandatory when AiScore itself is inaccessible.

Set:
`source_transport = MULTISOURCE_FALLBACK_DATE_UNIVERSE`;
and persist the actual carrier/corroborator providers used.

Failure of AiScore, FootballFixtures.org, LiveScore, Flashscore, Soccerway, FootballInfo, or LivescoresX **individually** must not produce SOURCE_BLOCKED. The bounded pass must exhaust the currently permitted carrier path, including the one search-to-open recovery for an HTML date carrier after a direct transport failure. A transport-local `Invalid URL`, cache miss, or stale generic page from one provider is not terminal. If no valid alternate date-level universe can be established from any permitted full-page carrier after the bounded attempts, stop as SOURCE_BLOCKED.

### C1. FAST_PRODUCTION terminal-date exception

For a cross-midnight FAST_PRODUCTION window, failure to obtain a provider's **whole next-calendar-date** all-matches surface is not by itself SOURCE_BLOCKED when all of the following are true:

- a valid date-level carrier was acquired for the starting/primary discovery date;
- the missing date contributes only a bounded terminal interval to the requested window;
- the terminal interval is at most six hours;
- protected/required competition blocks in that terminal interval are explicitly checked;
- candidate senior blocks/fixtures in the terminal interval are established from at least two independent current providers or one provider plus an official competition fixture source;
- material provider disagreement is zero, or the affected block is UNRESOLVED;
- the terminal interval is recorded as `terminal_scan_complete=true`.

This exception certifies **only the requested terminal interval**, not the entire next calendar date. Persist:
- `source_transport = MULTISOURCE_FALLBACK_PRIMARY_DATE_PLUS_TERMINAL_INTERVAL`;
- primary carrier/date;
- terminal interval ICT/UTC;
- terminal providers checked;
- terminal fixture/block manifest;
- disagreements/unresolved count.

Do not use this exception when the missing provider date contains more than the requested terminal interval, when the terminal interval exceeds six hours, or in FULL_AUDIT mode.

## 3. Bounded retry budget

This section governs fresh acquisition. Repair-mode verification has the stricter per-competition budget in `FOOTBALL_SWEEP_REPAIR_MODE.md` and must not expand into a fresh search loop.

Per run + source epoch, the normal acquisition budget is:

- one covering-cache/reuse check;
- one native AiScore date acquisition attempt;
- one fallback acquisition pass across the permitted date-level carriers. Within that single pass, try FootballFixtures.org -> FootballInfo -> LivescoresX -> LiveScore -> Flashscore -> Soccerway until one valid carrier is acquired for each listing date. For HTML carriers, a failed literal URL may use one search-to-open locator recovery before moving on. This is one bounded fallback pass, not repeated retry loops. Corroboration calls required by the accepted carrier do not count as a new acquisition attempt.

Do not loop through public search engines, dozens of competition pages, team schedules, or country-by-country reconstruction trying to simulate the missing master list.

When all three are exhausted:

`SOURCE ACQUISITION BLOCKED — AISCORE DATE UNIVERSE UNAVAILABLE`

Set:
- `complete=false`;
- `actionable_complete=false`;
- `work_ready=false`;
- discovery/reconciliation/packaging incomplete;
- exact raw counters unset rather than estimated.

## 4. Resume no-repeat + source-recovery lease

Also apply `FOOTBALL_SWEEP_CHECKPOINT_EXECUTION.md`.

When source acquisition reaches `ACQUIRED`, persist the source transport/hash/attempt state to the Sweep Run **before** broad discovery or external research. Advance the fresh-sweep cursor to `DISCOVERY_CLASSIFICATION`.

Persist a blocker fingerprint containing at least:
- requested window;
- listing date(s);
- current source-acquisition procedure revision;
- transport(s) attempted;
- normalized technical failure class.

A SOURCE_BLOCKED fingerprint prevents repeated same-turn loops, but it must **never become a permanent latch**. Provider/browser outages are transient external conditions and can recover even when the window and procedure are unchanged.

### Recovery lease

When a bounded acquisition pass ends SOURCE_BLOCKED, persist in the Resume Cursor:
- `source_blocker_fingerprint`;
- `source_last_attempt_at`;
- `source_retry_not_before = source_last_attempt_at + 30 minutes`;
- `source_recovery_attempt_count`.

Mirror these values into the dedicated Sweep Runs fields `Source Last Attempt At`, `Source Retry Not Before`, and `Source Recovery Attempt Count` when available; the Resume Cursor remains the authoritative structured state.

Use:

`python models/football/engine/sweep_checkpoint_cli.py source-blocked --input <checkpoint.json> --attempted-at <ISO8601> --fingerprint <fingerprint>`

On `/sweep resume`, before returning stored SOURCE_BLOCKED, run:

`python models/football/engine/sweep_checkpoint_cli.py source-retry --input <checkpoint.json> --now <ISO8601> --fingerprint <current-fingerprint>`

Behavior:
- if the current blocker fingerprint differs, retry immediately;
- if the stored blocked checkpoint predates this lease and has no retry timestamp, retry immediately once;
- if the fingerprint is unchanged and the 30-minute lease is still active, return the stored SOURCE_BLOCKED status without provider calls;
- if the fingerprint is unchanged but the lease expired, perform **one new bounded recovery acquisition pass**.

A recovery acquisition pass is the same bounded source-level sequence from §3:
1. covering COMPLETE/persisted-cache check;
2. one native AiScore acquisition attempt;
3. one ordered fallback carrier pass: FootballFixtures.org -> FootballInfo -> LivescoresX -> LiveScore -> Flashscore -> Soccerway, using at most one search-to-open locator recovery per HTML carrier/date after a literal URL failure, stopping once a valid carrier is obtained for each required listing date and then doing only required corroboration.

It is **not** permission for competition-by-competition reconstruction or repeated provider loops in one invocation.

If recovery succeeds:
- persist `source_acquisition_state=ACQUIRED`;
- persist source transport/payload hash;
- clear blocker/retry lease fields;
- continue to `DISCOVERY_CLASSIFICATION`.

If recovery fails:
- remain `SOURCE_BLOCKED`;
- persist the new failure fingerprint/attempt time;
- start a new 30-minute recovery lease;
- return the exact blocker.

Material conditions still permit immediate retry regardless of lease:
- browser-capable transport became available/connected;
- user supplied an AiScore raw date payload/valid complete handoff;
- a persisted complete source cache became available;
- source date/window changed;
- source-acquisition code/config/procedure changed.

A plain user `resume` does not bypass an **active** 30-minute lease, but after lease expiry it is sufficient to trigger the single bounded recovery probe.

Expected deterministic reasons include `SOURCE_RECOVERY_LEASE_ACTIVE`, `SOURCE_RECOVERY_LEASE_EXPIRED`, `BLOCKER_FINGERPRINT_CHANGED`, and `LEGACY_BLOCKED_CHECKPOINT_NO_RETRY_LEASE`.

This prevents both failure modes:
- hammering the same dead carrier loop on every resume;
- remaining SOURCE_BLOCKED forever after the external source has recovered.

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
- substitute for either the AiScore date universe or an accepted fallback date-level carrier plus independent mandatory-block corroboration.

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

Persist the acquired source epoch/checkpoint immediately, then continue Step 0 from source-local discovery/classification. If the normal sweep chunk boundary is reached later, the next `/sweep resume` must reuse this exact acquired epoch.

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
