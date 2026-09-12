# Football Time and Schedule Integrity Procedure

**Status:** ACTIVE  
**Effective:** 2026-09-12 ICT  
**Operational display timezone:** `Asia/Ho_Chi_Minh` (ICT, UTC+7)  
**Fixture authority:** AiScore only

This procedure separates **fixture-time capture** from **schedule-time conversion**. Step 0 must preserve the kickoff exactly in the timezone/offset supplied by AiScore and must not spend discovery time converting every fixture to ICT. Conversion to ICT happens later, when an operational schedule, same-window comparison, countdown, or kickoff-order view is actually needed.

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

Do not calculate `kickoff_ict` during normal Step 0 discovery.

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
- status at fetch: `NOT STARTED`, `LIVE`, `HT`, `FT`, `POSTPONED`, `CANCELLED`, or `UNKNOWN`.

At Step 0, `kickoff_ict` and `slate_date_ict` are optional and normally left unset.

---

## 3. Step-0 time-integrity gate

Step 0 checks **source integrity**, not cross-zone schedule conversion.

Verify:

1. AiScore daily-listing identity and match-page identity refer to the same fixture;
2. the preserved kickoff text/time is internally consistent with the AiScore source being used;
3. the page's timezone/offset label is preserved when shown;
4. the fixture is not duplicated under another identity;
5. obvious stale/live/finished status contradictions are resolved when practical.

Do **not** block actionable completeness merely because fixtures come from different local zones or because `kickoff_ict` has not yet been calculated.

If the source timestamp itself is contradictory or lacks enough timezone information to be interpreted later, classify:

`UNRESOLVED — SOURCE TIME INTEGRITY`

---

## 4. Requested-window handling during discovery

When the user gives an ICT/GMT+7 window, Step 0 should traverse the AiScore date blocks needed to cover that period **plus reasonable boundary coverage** where source-zone differences may shift a fixture across midnight.

Step 0 may carry boundary fixtures forward with:

`WINDOW STATUS = PENDING CONVERSION`

rather than performing match-by-match timezone conversion during discovery.

The later schedule-normalization pass converts only the surviving actionable set and removes fixtures that fall outside the requested ICT window.

This is intentional: discovery should not become bottlenecked by timezone conversion across dozens of leagues.

---

## 5. Later ICT conversion gate

Convert a fixture to ICT only when required for:

- a FOCUS/WATCHLIST schedule;
- same-window ranking;
- lineup-review timing;
- countdowns / next-match answers;
- market-review scheduling;
- final requested-window pruning;
- human-facing chronological display.

At that point:

1. use the preserved source local time plus its explicit timezone/offset, or AiScore-supplied UTC;
2. convert exactly once to `Asia/Ho_Chi_Minh`;
3. derive `slate_date_ict` from the converted kickoff;
4. record the derived `kickoff_ict` separately from the original source time;
5. never overwrite or discard the preserved source-time fields.

A trailing `Z` always means UTC.

---

## 6. Airtable datetime rule

The Daily Coverage Ledger currently has a `Kickoff ICT` datetime field. During Step 0:

- do **not** write a locally displayed foreign-zone kickoff into `Kickoff ICT`;
- leave `Kickoff ICT` unset until an actual ICT conversion has been performed;
- preserve source kickoff/timezone information in the handoff and, where needed, in coverage notes/source fields.

When ICT conversion is later performed, write the API datetime in the canonical timestamp form expected by Airtable. If Airtable returns a trailing `Z`, treat it as UTC serialization and convert once for human display.

---

## 7. Upcoming-schedule gate

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

## 8. Near-kickoff revalidation

For a candidate inside **90 minutes of converted kickoff**, recheck AiScore before using the time for lineup timing, countdowns, next-match answers, or market review. Revalidate again inside **30 minutes** when practical if the user is actively preparing XI/odds.

If AiScore status conflicts with the converted schedule, the current AiScore status wins.

---

## 9. Kickoff-change and stale-state handling

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

## 10. Fixture identity rule

Prefer the AiScore fixture/match ID as the canonical identity key.

If no stable ID is available, use a fallback identity built from:

`competition + normalized home + normalized away + preserved source kickoff/timezone`

Do not let another schedule provider silently reverse home/away or change the fixture date. Secondary sources may flag a discrepancy, but AiScore remains fixture authority.

---

## 11. Same-window grouping and publication

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

## 12. Authority

This procedure supersedes older instructions that force UTC→ICT normalization during Step 0.

The current invariant is:

`AISCORE IDENTITY → PRESERVE SOURCE LOCAL TIME + ZONE/OFFSET → ACTIONABLE FILTER/WORK HANDOFF → LATER ICT CONVERSION WHEN SCHEDULING → STATUS REVALIDATION → DISPLAY`

**Preserve first; convert later.**