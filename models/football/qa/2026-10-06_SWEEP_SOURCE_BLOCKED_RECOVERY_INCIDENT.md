# 2026-10-06 — Sweep SOURCE_BLOCKED permanent-latch incident

## User-visible failure

A Step-0 sweep remained:

`HANDOFF INCOMPLETE — AISCORE SOURCE BLOCKED`

across repeated resumes because the stored blocker fingerprint was unchanged.

Observed run:

`SWEEP-20261006-1145-20261007-0300`

The workflow correctly avoided repeating the same acquisition loop in one short interval, but the no-repeat rule had no expiry. That turned a transient provider/browser outage into a permanent blocked state even after external source conditions could have recovered.

## Root cause

The source-acquisition contract allowed retry only when a material fingerprint condition changed, such as:
- source window/date;
- procedure/config revision;
- connected browser transport;
- supplied complete payload/cache.

Elapsed time and source recovery were not represented. Therefore an unchanged fingerprint could remain blocked indefinitely.

## Required fix

The no-repeat rule is now a bounded **source-recovery lease**:
- blocked acquisition stores last attempt + retry-not-before;
- unchanged fingerprint is suppressed only for 30 minutes;
- after lease expiry, one bounded source-level recovery pass is allowed;
- changed fingerprint retries immediately;
- legacy blocked checkpoints without lease metadata retry immediately once;
- repeated competition-by-competition reconstruction remains forbidden.

This preserves anti-loop behavior while preventing a SOURCE_BLOCKED run from becoming a permanent latch.

## Regression requirement

Production QA must prove:
1. unchanged blocker inside lease -> no retry;
2. unchanged blocker after lease -> one retry;
3. changed blocker -> immediate retry;
4. legacy blocked checkpoint -> immediate one-time recovery probe;
5. failed recovery creates a new bounded lease.


## Follow-up: recovery lease worked, carrier set still failed

A later recovery attempt correctly bypassed the expired lease, but still failed because the entire original fallback set was inaccessible in the active runtime:

- AiScore inaccessible;
- LiveScore cache miss;
- Flashscore only generic/stale page;
- Soccerway dated URL redirected.

This proved the lease fix solved the permanent-latch bug but not the underlying transport coverage problem.

## Additional source fix

A direct date-level carrier reachable from both the ChatGPT web fetch path and GitHub runner was verified:

`https://www.footballfixtures.org/fixtures/YYYY-MM-DD`

For 2026-10-06 it exposed a dated all-fixtures page with a declared `All 144` count and server-rendered fixture rows. Independent current corroboration surfaces FootballInfo and LivescoresX were also reachable.

Production fallback now tries the count-reconciled FootballFixtures.org date page before the legacy LiveScore/Flashscore/Soccerway set. Search snippets remain forbidden for completeness; only the direct date page may act as the carrier.


## Root-cause clarification after attempt #4

Attempt #4 exposed a separate runtime mismatch: the sweep chat treated failure to fetch the newly preferred FootballFixtures.org direct page as terminal even though the source gate is supposed to be multi-carrier.

The audit hardening introduced a pre-discovery exact-universe gate on 2026-10-04. Before that change, Step 0 could build the slate from broader multi-source browsing and then reconcile it. After the change, one transport-level direct-page failure could halt the entire sweep before discovery.

This was an overcorrection. Completeness protection is still required, but no single direct carrier or one web-tool URL failure may be a hard dependency.

Current correction:
- literal direct-date navigation is mandatory;
- a provider-local Invalid URL/cache miss/generic page is non-terminal;
- all permitted direct-date carriers must be attempted within the bounded pass before SOURCE_BLOCKED;
- search/index output remains non-authoritative for completeness.


## Follow-up after attempt #5: search locator vs full-page carrier

Attempt #5 exhausted the literal direct-date URLs but still reported every provider as unavailable. The key runtime distinction is that the web/search stack can often locate and open the full canonical page even when literal URL navigation itself returns a transport-local cache miss.

The prior contract treated any search-located result as unusable, even after the canonical result could be opened into full webpage content. That was unnecessarily strict.

Correct rule:
- search snippets remain non-authoritative;
- search may recover the canonical provider/date result;
- OPEN must then return the full page;
- only the opened full page may certify the date universe, using the same count/date/fixture checks as direct navigation.

The direct FootballFixtures.org page is currently fetchable in a web runtime and exposes the requested 6 Oct 2026 date, `All 144`, and the fixture rows. FootballInfo and LivescoresX full dated pages are also retrievable. This validates search-to-open as a legitimate transport recovery rather than fixture reconstruction.

## Airtable status-enum defect

The same failed resume also exposed a persistence bug: `Run Status` and `Source Acquisition State` are different single-select enums.

Correct source-phase mapping:
- UNTRIED -> Run Status RUNNING;
- ACQUIRED -> Run Status RUNNING;
- SOURCE_BLOCKED -> Run Status BLOCKED.

`SOURCE_BLOCKED` must never be written into the Run Status field. It belongs only to Source Acquisition State and the structured Resume Cursor.
