# Football Coverage Controller

**Status:** ACTIVE  
**Official model:** Football v0.2.51  
**Coverage authority:** AiScore fixture universe + current senior-quality overlay  
**Time authority:** `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`

The coverage controller prevents silent fixture omission, wrong-date schedule contamination, timezone drift, wasteful Work research on incomplete fixture universes, and downstream replacement of a frozen Work PRE state with a second screen.

---

## 1. Production sequence

The required sequence is:

`AISCORE UNIVERSE → TIME/SCHEDULE INTEGRITY → SENIOR-QUALITY ELIGIBILITY → STEP-0 RECONCILIATION / WORK_READY GATE → WORK SCREEN EVERY ACTIONABLE FIXTURE → FOCUS/WATCHLIST/PASS/UNRESOLVED → FREEZE PRE → PERSIST → USER-SUPPLIED XI RERANK → GOAL BURDEN / EGE / MCE WHEN ELIGIBLE → USER-SUPPLIED PRICE → OFFICIAL/SHADOW VERDICTS`

Do not begin by selecting a few credible candidates. Every actionable fixture must be screened first, **but Work screening cannot begin until Step 0 has produced a complete reconciled universe.**

**SHORTEN THE DISPLAY, NEVER THE SCREENED UNIVERSE.**

---

## 2. AiScore traversal gate

Coverage cannot pass until the entire requested ICT window is accounted for on AiScore.

Required checks:

- every AiScore calendar-date listing touched by the window is traversed;
- overnight continuation is explicitly traversed rather than inferred;
- terminal requested kickoff interval/cutoff is checked;
- every discovered fixture is normalized and counted once;
- no known AiScore competition/league block inside the window remains unvisited or unresolved.

If a window crosses midnight, both calendar dates are mandatory traversal targets. If the cutoff is 03:00 ICT, verify the 03:00 interval even when the latest discovered fixture is earlier.

If this gate fails:

`COVERAGE INCOMPLETE — AiScore sweep incomplete`

No other schedule provider may backfill the universe.

### 2.1 Work-readiness hard gate

Step 0 may not export a normal Work handoff until traversal and reconciliation pass.

A Work handoff is valid only when it explicitly carries:

- `complete = true`;
- `work_ready = true`;
- reconciliation PASS;
- terminal date/interval traversal PASS;
- scope/registry audit PASS;
- no schedule-integrity unresolved fixture inside the Work array;
- admitted count equal to the actual Work fixture array.

If any item is false, absent, contradictory or provisional:

`HANDOFF INCOMPLETE — RERUN NORMAL CHAT STEP 0`

This is a **hard downstream stop**. Work must research **zero fixtures** and must not publish a provisional PRE board from the confirmed subset. It must not perform its own fixture sweep or broad web backfill.

The purpose of this gate is both integrity and usage control: expensive Work research begins only once the cheap Normal Chat discovery/filter stage is complete.

---

## 3. Time and schedule integrity gate

Before eligibility or PRE screening, every fixture must satisfy the authoritative timestamp contract:

- preserve AiScore fixture identity;
- normalize to `kickoff_utc`;
- convert exactly once to `kickoff_ict` using `Asia/Ho_Chi_Minh`;
- derive `slate_date_ict` from the converted kickoff;
- verify the normalized kickoff lies inside the requested ICT window;
- verify AiScore listing identity and match-page date/time are consistent;
- reject stale/future fixtures outside the requested window.

A trailing `Z` means UTC. It must never be displayed as ICT without conversion.

If identity/date/time remain contradictory:

`UNRESOLVED — SCHEDULE INTEGRITY`

That fixture remains accounted for in coverage reconciliation but cannot enter the Work actionable array until corrected or excluded with a valid reason.

---

## 4. Current eligibility gate — senior-quality overlay

For the normal actionable betting board, exclude:

- youth/Uxx: U17, U18, U19, U20, U21, U23 and equivalent youth competitions;
- academy/junior competitions;
- reserve/B-team/development competitions;
- amateur/semi-professional competitions;
- regional/state/provincial leagues;
- very small/obscure weak-data leagues;
- domestic lower divisions below top flight unless explicitly user-approved or explicitly whitelisted;
- **all Finnish domestic league competitions at every tier/category, including men's and women's leagues — hard exclusion effective 2026-09-09 ICT onward.**

The Finnish-league rule is prospective. All Finnish domestic league fixtures remain in the raw AiScore universe but must be marked `EXCLUDED`; they must never receive FOCUS/WATCHLIST status or reach official betting evaluation. Finnish Cup and UEFA club competitions involving Finnish clubs are not excluded by this rule unless another active eligibility rule removes them.

Do not inherit legacy blanket exclusions for continental football or cup labels. Senior first-team continental competitions are actionable when otherwise eligible, including UEFA Champions League, UEFA Europa League, and UEFA Conference League.

Do not weaken the overlay because the slate is small.

---

## 5. Screening requirement

After the Work-readiness hard gate passes, every Work-admitted actionable fixture receives:

- canonical fixture identity;
- corrected kickoff ICT;
- competition;
- PRE grade;
- structural archetype;
- primary scoring route;
- secondary route/opponent contribution where relevant;
- main failure mode;
- XI sensitivity;
- structural total range/ceiling when supportable;
- one board state: `FOCUS`, `WATCHLIST`, `PASS`, or `UNRESOLVED`.

Use the current official model hierarchy. For comparable grades:

`TWO-SIDED > ELITE CARRIER > CARRIER-LED > FRAGILE / OTHER`

Price is not part of PRE ranking.

EGE and MCE are later-stage gates and are not assigned during the frozen PRE sweep.

---

## 6. FOCUS / WATCHLIST / PASS semantics

### FOCUS

The strongest provisional candidates deserving first XI/market attention. FOCUS is not automatically a bet.

### WATCHLIST

Structurally live candidates with one or more material failure modes or sensitivity points. WATCHLIST survives to the confirmed-XI stage unless explicitly downgraded by new material evidence.

### PASS

The structural route did not clear the current PRE standard. Price or recognizable XI names may not resurrect a genuine PRE PASS without a documented material structural change.

### UNRESOLVED

Required information is insufficient to classify confidently. Do not convert uncertainty into PASS merely to reconcile counts.

---

## 7. Frozen PRE rule

When Work completes the structural screen, that board becomes the **frozen PRE artifact** for the later user-supplied XI/odds workflow.

The frozen record includes at least:

- PRE grade;
- structural archetype;
- board tier/state;
- primary/secondary routes;
- main failure mode;
- XI sensitivity;
- structural burden/range;
- canonical corrected kickoff semantics.

Downstream stages may rerank or downgrade based on new evidence, and active post-XI rules may open documented EGE/MCE assessment epochs, but neither may reconstruct a different frozen PRE from scratch.

---

## 8. Airtable publication rule

Publishing the Work screen to `Daily Coverage Ledger` is a **copy/upsert of the frozen screen**, not another model run.

The publish step must preserve Work output exactly in the fields available in the Airtable contract.

For datetime fields:

- write canonical UTC ISO where required by the API;
- interpret any returned trailing-`Z` value as UTC;
- convert to ICT exactly once for human display;
- derive Slate Date from the ICT kickoff.

Forbidden behavior:

- Work says `WATCHLIST` but Airtable publisher independently writes `PASS`;
- Work says `A2` but publisher independently rewrites `B / PASS`;
- publisher substitutes a fresh secondary-source thesis for the frozen Work thesis;
- publisher copies a future/out-of-window fixture into the current slate because a raw date string was misread.

If the persisted row conflicts with the original Work board, classify:

`PERSISTENCE SYNC FAULT — frozen PRE preserved`

Correct the persistence layer rather than treating the bad row as decision authority.

---

## 9. Count invariants

Before Step 0 can set `complete:true` / `work_ready:true`:

`Universe = Work-admitted actionable + Excluded`

After Work research begins, the Work board cannot be called complete until:

`Work-admitted actionable = Focus + Watchlist + Pass + Unresolved`

Also verify:

- each fixture appears once;
- all exclusions have a reason;
- all Work-admitted fixtures have a PRE disposition;
- all FOCUS + WATCHLIST rows are persisted;
- no youth/reserve/lower/small fixture survives the actionable overlay;
- no Finnish domestic league fixture survives the actionable overlay from 2026-09-09 ICT onward;
- no date/competition block within the requested AiScore window is unaccounted for;
- no fixture outside the requested corrected ICT window appears on the board;
- no schedule-integrity unresolved fixture appears in the Work array.

If Step-0 counts or coverage fail:

`HANDOFF INCOMPLETE — RERUN NORMAL CHAT STEP 0`

**Do not start Work PRE research.**

If Step 0 passed but the Work disposition counts fail after research:

`WORK RECONCILIATION FAILED — frozen board incomplete`

---

## 10. Same-window survival and rerank

At confirmed XI, compare all surviving FOCUS/WATCHLIST candidates in the same practical kickoff window rather than reviewing them in isolation.

Use corrected `kickoff_ict`, not raw Airtable `Z` timestamps, to define the window.

The official v0.2.51 order is governed by `CURRENT_MODEL.md` and the active patches, including chance-quality hardening and the post-XI market-history/MCE logic where eligible.

Confirmed XI is the first legitimate rerank gate after frozen PRE.

---

## 11. Current user-supplied-input boundary

Normal pre-kickoff execution does not automatically fetch XI or bookmaker current odds.

Until the user supplies the required current XI + odds:

- FOCUS/WATCHLIST remains provisional;
- market/price remains unevaluated;
- no official line is selected;
- no OFFICIAL LOCK is issued.

Only search externally for XI/current executable odds when the user explicitly asks for external verification. The separate historical market-watch exception is governed by the active Normal Chat XI/odds procedure.

---

## 12. Upcoming schedule controller

When asked for `next matches`, `upcoming matches`, or a schedule:

1. resolve current time in ICT;
2. read the frozen board/Airtable bridge;
3. for fixtures inside 90 minutes of stored kickoff, recheck AiScore status/time;
4. revalidate again inside 30 minutes when actively preparing XI/odds where practical;
5. remove LIVE/HT/FT/postponed/cancelled fixtures from the upcoming list;
6. correct kickoff changes without rewriting frozen PRE;
7. sort only by corrected ICT kickoff;
8. show the date if the list crosses midnight or multiple ICT dates.

If stored Airtable time says upcoming but AiScore shows LIVE, classify:

`STALE UPCOMING STATE`

and use the live state operationally.

---

## 13. Missed-fixture and schedule-fault recovery

If an eligible fixture is discovered after a board was claimed complete:

1. classify the original coverage claim as a coverage failure;
2. determine which traversal/filter/persistence step failed;
3. if still prematch, return to Step 0 and rebuild/reconcile the Work handoff before additional Work deep research;
4. if already started, label it a `MISSED PREMATCH OPPORTUNITY` and do not rewrite history;
5. fix the root cause before the next board is called complete.

If a historical board contains the wrong fixture date/time:

- preserve the original PRE record;
- annotate the schedule fault;
- correct future operational schedule data;
- exclude not-yet-played future fixtures from historical performance denominators.

A live result must never be used to pretend the omitted match would certainly have been selected prematch.

---

## 14. Authority

This controller is subordinate to upstream `CURRENT_MODEL.md`, `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`, and the active rule files, but it supersedes old coverage instructions that allow Work to research a provisional/incomplete handoff, rely on multi-source fixture unions, raw-UTC schedule display, stale upcoming timestamps, legacy competition whitelists, or a second structural screen during Airtable publication.