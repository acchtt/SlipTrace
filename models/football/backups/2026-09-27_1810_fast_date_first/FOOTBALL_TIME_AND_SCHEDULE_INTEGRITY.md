# Football Time and Schedule Integrity Procedure

**Status:** ACTIVE  
**Effective:** 2026-09-17 ICT coverage hardening  
**Operational display timezone:** `Asia/Ho_Chi_Minh` (ICT, UTC+7)  
**Fixture authority:** AiScore only

This procedure separates **raw discovery-time capture** from **final Work-handoff time normalization**. Step 0 must preserve the kickoff exactly as supplied by AiScore during broad discovery and must not spend discovery time converting every raw fixture. However, before the final Work handoff is packaged, every Work-admitted fixture must be revalidated against an authoritative explicitly-zoned AiScore time source, normalized once to UTC, converted once to ICT, and proven inside the requested ICT window.

**Important distinction:** deferring per-fixture ICT conversion does **not** allow Step 0 to defer requested-window boundary math. Step 0 must normalize the user-requested start/end boundaries once, build a deterministic discovery-date envelope, and perform an independent terminal-interval sweep before it may claim actionable completeness.

This procedure overrides older football instructions that require Step 0 to convert every discovered fixture to UTC/ICT before Work.

---

## 1. Source-time preservation contract

For every AiScore fixture, preserve the strongest available source-time representation without changing its timezone:

- `kickoff_source_local` — the kickoff exactly as shown by the authoritative AiScore match/listing source;
- `source_timezone` — named timezone when explicitly available;
- `source_utc_offset` — explicit UTC offset when available, e.g. `+08:00`, `-03:00`;
- `kickoff_utc_source` — only when AiScore itself explicitly supplies a UTC value;
- `source_time_label` — any page/header timezone label needed to interpret the displayed kickoff;
- status at fetch.

Do **not** invent a timezone from geography when AiScore does not establish it. If the page gives an offset but no named zone, keep the offset. If it gives UTC, keep UTC. If it gives only a local-looking timestamp with no reliable zone/offset, record `SOURCE TIMEZONE UNRESOLVED` rather than guessing.

Do not calculate `kickoff_ict` during broad raw discovery.

### 1.1 Authoritative AiScore time hierarchy

For **Work-admitted fixtures**, use the strongest available current AiScore timestamp in this order:

1. canonical match-page **Match Info / About The Match** timestamp that explicitly says `UTC`;
2. AiScore machine-readable Unix epoch / ISO timestamp with an explicit zone;
3. AiScore timestamp with an explicit UTC offset.

The following are **not** UTC authority by themselves:

- page headings such as `Competition YYYY/MM/DD HH:mm:ss`;
- date-listing clocks;
- team-fixture-list clocks;
- localized language/page display times;
- search-result snippets that omit an explicit timezone label;
- a bare date/time inferred from the page locale.

AiScore pages may render a localized display clock separately from the underlying Match Info UTC timestamp. Never append `UTC` to a bare display time.

Persist:

- `kickoff_time_provenance = MATCH_INFO_UTC | API_EPOCH | EXPLICIT_OFFSET`;
- `kickoff_utc_verified`;
- `kickoff_ict_verified`;
- `time_verified_at`;
- canonical AiScore fixture/match ID or URL used for the verification.

If none of the authoritative forms is available, classify `UNRESOLVED — SOURCE TIME INTEGRITY` and do not admit the fixture to the Work handoff.

---

## 2. Required Step-0 fixture-time fields

For every Work-admitted fixture, preserve where available:

- AiScore fixture/match ID or canonical match URL;
- competition;
- home team;
- away team;
- AiScore listing date used for discovery;
- raw/source kickoff text;
- `kickoff_source_local`;
- `source_timezone` and/or `source_utc_offset`;
- `kickoff_utc_source` only if directly supplied by AiScore;
- status at fetch: `NOT STARTED`, `LIVE`, `HT`, `FT`, `POSTPONED`, `CANCELLED`, `UNKNOWN`, or `STATUS CONFLICT`.

During broad discovery, `kickoff_ict` and `slate_date_ict` may remain unset. Before final Work-handoff packaging, every Work-admitted fixture must additionally carry `kickoff_time_provenance`, `kickoff_utc_verified`, `kickoff_ict_verified`, and `time_verified_at`.

---

## 3. Step-0 time-integrity gate

Step 0 checks **source integrity**, not full cross-zone schedule conversion.

Verify:

1. AiScore daily-listing identity and match-page identity refer to the same fixture;
2. the preserved kickoff text/time is internally consistent with the AiScore source being used;
3. the page's timezone/offset label is preserved when shown;
4. the fixture is not duplicated under another identity;
5. obvious stale/live/finished status contradictions are resolved; a potentially actionable in-window status conflict must follow Section 3.1 and cannot be waived as merely practical.

Different local zones do not themselves block coverage. However, final `actionable_complete=true` / `work_ready=true` is forbidden until every Work-admitted fixture has passed the authoritative-time normalization gate and has a verified ICT kickoff inside the requested window.

If the source timestamp itself is contradictory or lacks enough timezone information to be interpreted later, classify:

`UNRESOLVED — SOURCE TIME INTEGRITY`

---

## 3.1 Current-status conflict gate

A status from one AiScore surface is not enough to exclude an otherwise in-window actionable fixture when another current AiScore surface conflicts.

If a competition/date listing shows `POSTPONED`, `CANCELLED`, `FT`, or another non-upcoming state but the canonical AiScore match page or current team fixture page still shows the same identity as scheduled/upcoming, classify:

`UNRESOLVED — AISCORE STATUS CONFLICT`

Then revalidate the canonical match page and at least one current AiScore fixture/team surface. Until the conflict is resolved:

- do not exclude the fixture as postponed/cancelled;
- do not admit it as normally scheduled;
- do not set `actionable_complete=true` or `work_ready=true` if the fixture is potentially actionable and inside the requested window.

When the current canonical match page and a second current AiScore surface agree, use that resolved state operationally and record the conflicting stale surface in notes.

A stale competition-schedule snapshot must never by itself remove an otherwise actionable European domestic cup fixture.

## 4. Requested-window handling during discovery

When the user gives an ICT/GMT+7 window, Step 0 must do **boundary normalization once** before fixture discovery.

### 4.1 Mandatory requested-window boundary normalization

Resolve and record:

- `window_start_ict`;
- `window_end_ict`;
- `window_start_utc`;
- `window_end_utc`;
- every ICT calendar date touched by the window;
- every UTC calendar date touched by the normalized window.

This is boundary math only. It is not per-fixture schedule conversion and therefore does not violate the Step-0 source-time preservation rule.

### 4.2 Deterministic discovery-date envelope

Build a discovery envelope from the union of:

1. every ICT date touched by the requested window;
2. every UTC date touched by `window_start_utc -> window_end_utc`;
3. one date before the earliest UTC date touched;
4. one date after the latest UTC date touched.

Traverse all relevant AiScore date/listing blocks in that envelope far enough to establish whether potentially actionable senior competition blocks can place fixtures inside the requested window.

The one-day buffer exists because AiScore surfaces fixtures through date/listing contexts that can differ from the user's ICT slate date. The buffer is discovery insurance only; out-of-window fixtures are pruned later.

Do **not** stop traversal because the latest fixture found so far is well before the requested cutoff.

### 4.3 Cross-midnight and early-morning hard rule

If the requested ICT window:

- crosses midnight; or
- ends between `00:00` and `06:00` ICT;

then Step 0 must explicitly inspect both:

- the terminal ICT calendar date; and
- the UTC calendar date containing `window_end_utc`.

A sweep of only the starting ICT date is automatically incomplete.

### 4.4 Mandatory terminal-interval sentinel sweep

Define:

`terminal_interval_ict = max(window_start_ict, window_end_ict - 6 hours) -> window_end_ict`

Before `actionable_complete=true`, perform a **second, dedicated AiScore-only discovery pass** targeted specifically at this terminal interval and its relevant date/listing blocks.

The terminal sentinel is independent of the main pass. Its job is to catch late-night/next-date blocks that the broad traversal may have skipped.

Record:

- `terminal_interval_ict`;
- terminal ICT date(s) checked;
- terminal UTC date(s) checked;
- AiScore listing/date blocks checked;
- potentially actionable senior competitions found;
- admitted/excluded/unresolved counts from the terminal pass;
- `terminal_scan_complete=true|false`.

If the terminal pass finds zero fixtures, that is acceptable **only when the pass itself is explicitly documented as complete**.

The following are never acceptable evidence that the terminal interval is empty:

- “the last fixture found was at 22:30”;
- “no more attractive matches appeared”;
- “the starting-date listing ended”;
- absence of results from a generic search query;
- a previously generated handoff that already claims completeness.

### 4.5 Window membership and admitted-set normalization

During broad discovery, fixture membership can be decided cheaply when AiScore supplies a directly comparable timestamp:

- if AiScore supplies explicit UTC, compare it directly with `window_start_utc -> window_end_utc`;
- if AiScore supplies an explicit offset, an ephemeral normalized UTC value may be calculated for preliminary in/out-of-window testing while preserving the original source fields;
- if the timestamp cannot yet be interpreted safely, carry it as `WINDOW STATUS = PENDING CONVERSION` or `UNRESOLVED — SOURCE TIME INTEGRITY` during discovery.

Before the final Work handoff is packaged, run a **canonical admitted-set time pass** over every surviving Work-admitted fixture:

1. open/revalidate the canonical AiScore match identity;
2. obtain an authoritative timestamp using Section 1.1;
3. normalize to `kickoff_utc_verified`;
4. convert exactly once to `kickoff_ict_verified`;
5. prove `window_start_ict <= kickoff_ict_verified <= window_end_ict`;
6. remove true out-of-window fixtures;
7. mark unresolved timestamp/identity conflicts as blocking.

No Work-admitted fixture may leave Step 0 as `PENDING CONVERSION`.

---

## 5. Step-0 completeness proof fields

A Step-0 handoff claiming actionable completeness must carry a coverage proof, not just a fixture count.

Required fields:

- `window_start_ict`;
- `window_end_ict`;
- `window_start_utc`;
- `window_end_utc`;
- `ict_dates_touched`;
- `utc_dates_touched`;
- `discovery_listing_dates_checked`;
- `discovery_date_envelope_complete=true|false`;
- `terminal_interval_ict`;
- `terminal_listing_dates_checked`;
- `terminal_scan_complete=true|false`;
- `actionable_senior_block_audit=PASS|FAIL`;
- admitted count;
- actionable excluded/unresolved count.

`complete=true`, `actionable_complete=true`, or `work_ready=true` is forbidden when any of the following holds:

- `discovery_date_envelope_complete != true`;
- `terminal_scan_complete != true`;
- any Work-admitted fixture lacks authoritative `kickoff_time_provenance`;
- any Work-admitted fixture lacks `kickoff_utc_verified` or `kickoff_ict_verified`;
- any Work-admitted fixture converts outside the requested ICT window;
- any admitted fixture remains `PENDING CONVERSION`.

A self-reported terminal/date verification flag without the underlying checked-date evidence is invalid.

---

## 6. Final Work-handoff ICT normalization gate

Broad raw discovery may defer conversion, but the final Work-admitted set may not.

For every admitted fixture before ZIP packaging:

1. use only the authoritative time hierarchy in Section 1.1;
2. derive one `kickoff_utc_verified`;
3. convert exactly once to `Asia/Ho_Chi_Minh` as `kickoff_ict_verified`;
4. derive `slate_date_ict` from that verified ICT kickoff;
5. verify requested-window membership;
6. preserve the original source/display fields separately;
7. never derive UTC from a localized display heading;
8. never reconvert an already verified UTC/ICT pair.

Downstream scheduling, same-window ranking, lineup timing, countdowns and market review reuse `kickoff_ict_verified`; they do not reinterpret raw display text.

A trailing `Z` always means UTC.

---

## 7. Airtable datetime rule

The Daily Coverage Ledger currently has a `Kickoff ICT` datetime field.

During raw discovery, do not write a locally displayed foreign-zone kickoff into `Kickoff ICT`.

After the final admitted-set normalization gate:

- write the verified instant corresponding to `kickoff_ict_verified` into `Kickoff ICT` using Airtable's canonical datetime format;
- preserve `kickoff_utc_verified`, `kickoff_ict_verified`, provenance and raw source text in the handoff/coverage notes;
- never populate `Kickoff ICT` by copying a bare source clock or by parsing a note that merely contains the word `UTC` without provenance.

If Airtable returns a trailing `Z`, that is UTC serialization of the same instant. Convert once for human ICT display; do not add seven hours twice.

---

## 8. Upcoming-schedule gate

When the user asks for `next matches`, `upcoming matches`, a schedule, or similar:

1. take the surviving frozen board/handoff;
2. convert preserved source times to ICT;
3. revalidate near-term fixture status against AiScore;
4. include only fixtures genuinely still upcoming;
5. remove LIVE/HT/FT/postponed/cancelled rows;
6. sort by converted ICT kickoff;
7. show the date whenever the list crosses midnight or more than one ICT date.

This is the stage where cross-zone conversion becomes operationally mandatory.

---

## 9. Near-kickoff revalidation

For a candidate inside **90 minutes of converted kickoff**, recheck AiScore before using the time for lineup timing, countdowns, next-match answers, or market review.

Inside **30 minutes**, revalidation is **mandatory before an official Step-2 exposure decision**. Verify the current AiScore:

- fixture/match ID where available;
- competition;
- home team;
- away team;
- kickoff;
- status.

Compare this identity with the frozen board and the user-supplied lineup/market surface.

If AiScore status conflicts with the converted schedule, the current AiScore status wins. If the user surface or another current source exposes a home/away, identity, kickoff or status discrepancy, resolve it against current AiScore authority before official exposure.

---

## 10. Kickoff-change and stale-state handling

If a later recheck finds a meaningful discrepancy:

- update the operational converted kickoff/status;
- preserve the original source-time capture and frozen PRE history;
- annotate the correction rather than silently rewriting history.

Use one of these labels where applicable:

- `SOURCE TIMEZONE FAULT`
- `SCHEDULE DATE MISMATCH`
- `STALE UPCOMING STATE`
- `KICKOFF CHANGE`
- `FIXTURE IDENTITY / HOME-AWAY MISMATCH`

A schedule correction is not a structural rerank by itself.

---

## 11. Fixture identity rule

Prefer the AiScore fixture/match ID as the canonical identity key.

If no stable ID is available, use a fallback identity built from:

`competition + normalized home + normalized away + preserved source kickoff/timezone`

Do not let another schedule provider silently reverse home/away or change the fixture date. Secondary sources may flag a discrepancy, but AiScore remains fixture authority.

### Official-exposure identity block

A visible unresolved discrepancy in fixture ID, home/away orientation, kickoff or status is a hard Step-2 exposure blocker.

Use:

`FIXTURE IDENTITY / HOME-AWAY MISMATCH — HOLD`

until current AiScore authority resolves the identity. Preserve frozen PRE, source-time capture, user-supplied XI/odds and any earlier historical decision; annotate the correction rather than rewriting history.

An Over market being side-symmetric does **not** waive this block because venue/home-away assumptions may have affected structural evidence.

---

## 12. Same-window grouping and publication

Same-window comparison and the final published schedule use converted ICT kickoff, but that conversion belongs to the later scheduling stage.

Before publishing a FOCUS/WATCHLIST schedule, verify:

- each displayed kickoff has a preserved source-time basis;
- each time was converted exactly once to ICT;
- no live/finished match is described as upcoming;
- final requested-window pruning has been applied;
- sort order uses converted ICT kickoff.

If those checks fail, state:

`SCHEDULE INTEGRITY CHECK FAILED — conversion/revalidation required`

---

## 13. Missed-fixture recovery trigger

If a later audit finds an actionable fixture inside a window that had already been marked complete:

1. invalidate the earlier `actionable_complete/work_ready` claim for that handoff;
2. identify whether the miss came from date-envelope traversal, terminal sentinel failure, competition-block traversal, or filtering;
3. rerun Step 0 using the full discovery-date envelope and terminal sentinel;
4. do not simply append the one known missing fixture and preserve the old completeness claim;
5. record the miss as a coverage fault so the same mechanism is not treated as verified on the next slate.

A repair is complete only after the rerun re-establishes the coverage proof fields in Section 5.

---

## 14. Authority

This procedure supersedes older instructions that force UTC→ICT normalization for every fixture during Step 0 and any vague instruction that treats “reasonable boundary coverage” as sufficient without a terminal proof.

The current invariant is:

`NORMALIZE REQUESTED WINDOW BOUNDARIES ONCE → BUILD DATE ENVELOPE → AISCORE DISCOVERY → TERMINAL SENTINEL → PRESERVE FIXTURE SOURCE TIME → ACTIONABLE FILTER / WORK HANDOFF → LATER ICT CONVERSION WHEN SCHEDULING → STATUS REVALIDATION → DISPLAY`

**Preserve fixture times; prove the window.**