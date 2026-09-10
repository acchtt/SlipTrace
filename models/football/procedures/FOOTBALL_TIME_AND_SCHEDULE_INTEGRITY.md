# Football Time and Schedule Integrity Procedure

**Status:** ACTIVE  
**Effective:** 2026-09-10 ICT  
**Canonical timezone:** `Asia/Ho_Chi_Minh` (ICT, UTC+7)  
**Fixture authority:** AiScore only

This procedure fixes timezone, stale-upcoming, wrong-date and schedule-ingestion faults. It is authoritative for all fixture timestamps, slate dates, schedule displays and Airtable kickoff reads/writes.

---

## 1. Canonical timestamp contract

Every fixture must carry two distinct timestamp meanings:

- `kickoff_utc` — canonical machine timestamp in ISO-8601 UTC, e.g. `2026-09-10T02:30:00Z`;
- `kickoff_ict` — derived display/scheduling timestamp after converting `kickoff_utc` exactly once to `Asia/Ho_Chi_Minh`.

`Z` always means **UTC**. A timestamp ending in `Z` must never be interpreted as ICT.

Never:

- add +7 to a timestamp already explicitly expressed in ICT;
- treat an Airtable serialized `...Z` value as local time;
- convert the same timestamp to ICT twice.

The human-facing schedule is always shown in ICT unless the user explicitly asks for another timezone.

---

## 2. Required fixture-time fields

For every AiScore fixture handoff, preserve where available:

- AiScore fixture/match ID or canonical match URL;
- competition;
- home team;
- away team;
- AiScore listing date used for discovery;
- raw/source kickoff text;
- `kickoff_utc`;
- `kickoff_ict`;
- `slate_date_ict` derived from `kickoff_ict`;
- status at fetch: `NOT STARTED`, `LIVE`, `HT`, `FT`, `POSTPONED`, `CANCELLED`, or `UNKNOWN`.

`slate_date_ict` must never be copied from an AiScore page label without checking the normalized kickoff.

---

## 3. Date-integrity gate

Before a fixture can enter the actionable board, verify all of:

1. normalized `kickoff_ict` falls inside the requested ICT window;
2. the AiScore daily listing and AiScore match page refer to the same fixture identity;
3. the match-page date/time is consistent with the normalized kickoff;
4. the derived `slate_date_ict` is the correct ICT calendar date;
5. the fixture is not merely a future match surfaced through a competition page or stale listing.

If any date/time identity remains inconsistent, classify:

`UNRESOLVED — SCHEDULE INTEGRITY`

and do not send the fixture to FOCUS/WATCHLIST betting evaluation until corrected.

A future fixture outside the requested window must never appear on the current board simply because it was found while browsing the same competition.

---

## 4. Airtable datetime rule

Airtable/API serialization may return a datetime as UTC with a trailing `Z` even when the Airtable field is configured to display in `Asia/Ho_Chi_Minh`.

Therefore:

- write datetime values as canonical UTC ISO-8601 where the API expects a timestamp;
- on read, treat every trailing-`Z` value as UTC;
- convert it exactly once to `Asia/Ho_Chi_Minh` before presenting or scheduling;
- derive `Slate Date` from the ICT-converted kickoff, not from the raw UTC date.

The field name `Kickoff ICT` describes intended human display semantics; it does **not** change the meaning of a serialized `Z` timestamp.

---

## 5. Upcoming-schedule gate

When the user asks for `next matches`, `upcoming matches`, a schedule, or similar:

1. resolve the current time in ICT at the moment of the request;
2. read the frozen board/Airtable state;
3. revalidate near-term fixture status against AiScore before presenting the schedule;
4. include only fixtures that are genuinely `NOT STARTED` and whose corrected `kickoff_ict` is still in the future;
5. remove fixtures already `LIVE`, `HT`, `FT`, postponed or cancelled from the upcoming list;
6. sort only by corrected `kickoff_ict`;
7. show the calendar date whenever the list crosses midnight or contains more than one ICT date.

Do not build an upcoming schedule from stored kickoff timestamps alone when the match is close to kickoff.

---

## 6. Near-kickoff revalidation

For a candidate inside **90 minutes of stored kickoff**, recheck AiScore before using the stored time as operational truth for:

- lineup timing;
- countdowns;
- `next match` responses;
- market-review scheduling;
- same-window grouping.

Revalidate again when practical inside **30 minutes** of kickoff if the user is actively preparing XI/odds.

If AiScore shows the match already live while the stored schedule says upcoming, the live state wins and the stored schedule is a fault to correct.

---

## 7. Kickoff-change and stale-state handling

If a recheck finds a meaningful discrepancy:

- update the operational kickoff/status;
- preserve the original frozen PRE history;
- annotate the correction rather than silently rewriting history.

Use one of these fault labels:

- `TIMEZONE NORMALIZATION FAULT`
- `SCHEDULE DATE MISMATCH`
- `STALE UPCOMING STATE`
- `KICKOFF CHANGE`
- `FIXTURE IDENTITY / HOME-AWAY MISMATCH`

A schedule correction is not a structural rerank by itself.

---

## 8. Fixture identity rule

Prefer the AiScore fixture/match ID as the canonical identity key.

If no stable ID is available, use a fallback identity built from:

`competition + normalized home + normalized away + kickoff_utc`

Do not let a secondary source silently reverse home/away or move the fixture date. Secondary sources may flag a discrepancy, but AiScore must be rechecked because it remains fixture authority.

If AiScore itself exposes contradictory home/away/date representations, mark the fixture unresolved until the match page resolves the identity.

---

## 9. Same-window grouping

Same-window comparison must use **corrected ICT kickoff**, not raw Airtable UTC strings or stale scheduled times.

Recommended practical groups are based on actual corrected kickoff proximity, not just identical displayed hours.

If a kickoff correction moves a match out of a group, rerank the operational attention order but do not rewrite its frozen PRE grade.

---

## 10. Schedule publication checks

Before publishing a FOCUS/WATCHLIST schedule, verify:

- every displayed time has been converted exactly once from UTC to ICT;
- no live/finished match is described as upcoming;
- every displayed fixture belongs to the requested ICT date/window;
- the sort order uses corrected ICT time;
- future-date fixtures outside the window are absent;
- date labels are shown where ambiguity is possible.

If any of these checks fail, do not claim the schedule is final. State:

`SCHEDULE INTEGRITY CHECK FAILED — revalidation required`

---

## 11. Historical corrections

When a past board is found to contain the wrong date/time:

- do not delete or backdate the original PRE decision;
- annotate the coverage/audit record with the schedule fault;
- correct future operational schedule data;
- exclude not-yet-played future fixtures from historical board-performance denominators.

Historical P/L and PRE history remain tied to what was actually assessed and placed.

---

## 12. Authority

This procedure overrides older football instructions wherever they are ambiguous about UTC-vs-ICT serialization, slate-date derivation, upcoming-match status, or schedule revalidation.

The invariant is simple:

`AISCORE IDENTITY → UTC CANONICAL TIMESTAMP → ONE ICT CONVERSION → ICT SLATE DATE → STATUS REVALIDATION → DISPLAY / SCHEDULE`
