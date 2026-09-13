# Football Coverage Controller

**Status:** ACTIVE  
**Official model:** Football v0.2.54  
**Coverage authority:** AiScore actionable senior universe + current senior-quality overlay  
**Time authority:** `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`

The coverage controller prevents silent actionable-fixture omission, wrong-date schedule contamination, timezone drift, wasteful Work research on incomplete actionable universes, and downstream replacement of a frozen Work PRE state with a second screen.

---

## 1. Production sequence

The required sequence is:

`AISCORE DISCOVERY → TIME/SCHEDULE INTEGRITY → ACTIONABLE SENIOR BLOCK AUDIT → SENIOR-QUALITY ELIGIBILITY → STEP-0 ACTIONABLE RECONCILIATION / WORK_READY GATE → WORK SCREEN EVERY ADMITTED FIXTURE → ROUTE-QUALITY + CC+ AUDIT → FOCUS/WATCHLIST/PASS/UNRESOLVED → FREEZE PRE → PERSIST → USER-SUPPLIED XI RERANK / CARRIER REOPEN TEST → GOAL BURDEN / EGE / MCE WHEN ELIGIBLE → USER-SUPPLIED PRICE → OFFICIAL/SHADOW VERDICTS`

Do not begin by selecting a few credible candidates. Every actionable fixture must be screened first, **but Work screening can begin once Step 0 has proved actionable completeness even when exact enumeration of already-excluded micro/youth/raw fixtures is unavailable.**

**SHORTEN THE DISPLAY, NEVER THE ACTIONABLE SCREENED UNIVERSE.**

---

## 2. AiScore traversal and completeness gate

AiScore remains the sole fixture-discovery authority.

The system distinguishes two levels of completeness:

- `actionable_complete` — every potentially actionable senior competition/block in the requested ICT window has been checked and every actionable fixture found is accounted for;
- `raw_audit_complete` — every raw AiScore fixture on touched date pages, including excluded youth/reserve/lower/amateur/regional/hard-excluded blocks, has been individually enumerated.

Exact raw enumeration is desirable for audit but is **not required for Work readiness** when AiScore exposes excluded blocks only through fragmented/dynamic snapshots.

### 2.1 Required actionable checks

Before `actionable_complete=true`, verify:

- every PRIORITY/NORMAL senior league block that falls inside the requested window;
- every eligible senior continental/cup block visible/relevant to the window;
- every relevant senior CONDITIONAL block, with its cheap gate resolved;
- overnight continuation where applicable;
- terminal requested kickoff interval/cutoff;
- every discovered potentially actionable senior fixture normalized and counted once;
- no known actionable senior competition block remains unvisited or unresolved.

If this gate fails:

`COVERAGE INCOMPLETE — ACTIONABLE SENIOR GAP`

No other schedule provider may backfill the universe.

### 2.2 Non-blocking raw gaps

The following do not block Work merely because AiScore will not expose an exact one-by-one date-page count:

- youth/Uxx;
- academy/junior;
- reserve/B/development;
- amateur/semi-pro;
- regional/state/provincial;
- unapproved lower divisions;
- very weak/obscure competitions;
- LOW-GOAL EXCLUDE domestic leagues;
- Finnish domestic leagues;
- other blocks unambiguously excluded before Work.

When exact enumeration is unavailable, Step 0 must record:

- `raw_audit_complete=false`;
- `raw_count_mode=lower_bound`;
- `nonblocking_raw_gaps=[...]`.

Do not fabricate an exact raw count.

### 2.3 Work-readiness gate

A Work handoff is valid when it explicitly carries:

- `complete = true` meaning actionable completeness;
- `actionable_complete = true`;
- `work_ready = true`;
- actionable senior block audit PASS;
- terminal date/interval verification PASS;
- scope/registry audit PASS;
- no schedule-integrity unresolved fixture inside the Work array;
- admitted count equal to the actual Work fixture array.

`raw_audit_complete=false` is non-blocking when every listed raw gap is already outside model scope.

If any **actionable** requirement is false, absent, contradictory, or provisional:

`HANDOFF INCOMPLETE — ACTIONABLE COVERAGE GAP — RERUN NORMAL CHAT STEP 0`

Work must then research zero fixtures and must not perform its own fixture sweep or broad web backfill.

---

## 3. Time and schedule integrity gate

Before eligibility or PRE screening, every potentially actionable fixture must satisfy the authoritative timestamp contract:

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

A potentially actionable unresolved fixture blocks actionable completeness until corrected or validly excluded. An unresolved raw fixture already belonging to a hard-excluded category does not enter the Work array and may remain a non-blocking raw-audit gap.

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

The Finnish-league rule is prospective. Discovered Finnish domestic league fixtures remain auditable but must never receive FOCUS/WATCHLIST status or reach official betting evaluation. Exact enumeration of every Finnish/lower/youth fixture is not required to unlock Work once the block is unambiguously classified outside model scope.

Do not inherit legacy blanket exclusions for continental football or cup labels. Senior first-team continental competitions are actionable when otherwise eligible, including UEFA Champions League, UEFA Europa League, and UEFA Conference League.

Do not weaken the overlay because the slate is small.

---

## 5. Screening requirement

After the Work-readiness actionable gate passes, every Work-admitted actionable fixture receives:

- canonical fixture identity;
- corrected kickoff ICT;
- competition;
- PRE grade;
- structural archetype;
- route-quality state: `TWO-SIDED — QUALITY PROVEN` or `TWO-SIDED — NOMINAL / WEAK SECONDARY` where relevant;
- carrier-ceiling state: `CC+ — CARRIER CEILING`, `CC+ CANDIDATE — XI SENSITIVE`, or documented reason CC+ failed where relevant;
- primary scoring route;
- secondary route/opponent contribution where relevant;
- main failure mode;
- XI sensitivity;
- structural total range/ceiling when supportable;
- one board state: `FOCUS`, `WATCHLIST`, `PASS`, or `UNRESOLVED`.

### 5.1 Mandatory CC+ audit before strong-carrier PASS

Before assigning B/PASS to a fixture containing a strong favorite/carrier, Work must explicitly answer:

1. Does the carrier possess credible independent 3+ team-goal potential?
2. Are recent low scores supported by true chance suppression, or could they reflect finishing/outcome/schedule noise?
3. Does the carrier have enough repeatable attacking quality to survive weak opponent contribution?

If yes but XI uncertainty blocks promotion, use:

`CC+ CANDIDATE — XI SENSITIVE`

rather than silently burying the match.

### 5.2 PRE ranking hierarchy

Two-Sided Tier A remains the primary lane. For comparable non-Tier-A grades:

`QUALITY-PROVEN TWO-SIDED > CC+ ELITE CARRIER > NOMINAL / WEAK-SECONDARY TWO-SIDED > ordinary CARRIER-LED > FRAGILE / OTHER`

A B+ nominal two-sided candidate must not automatically outrank a materially stronger self-funded carrier.

Price is not part of PRE ranking.

EGE, MCE and `CARRIER REOPEN — XI CONFIRMED` are later-stage gates and are not assigned as final execution states during the frozen PRE sweep.

---

## 6. FOCUS / WATCHLIST / PASS semantics

### FOCUS

The strongest provisional candidates deserving first XI/market attention. FOCUS is not automatically a bet.

### WATCHLIST

Structurally live candidates with one or more material failure modes or sensitivity points. WATCHLIST survives to the confirmed-XI stage unless explicitly downgraded by new material evidence.

### PASS

The structural route did not clear the current PRE standard. Price or recognizable XI names may not resurrect a genuine PRE PASS.

A strong-carrier PASS must contain a documented CC+ audit result. If PRE identified a plausible carrier ceiling but XI uncertainty prevented promotion, preserve `CC+ CANDIDATE — XI SENSITIVE` so the later strict v0.2.52 carrier-reopen test can distinguish it from a genuine hard PASS.

### UNRESOLVED

Required information is insufficient to classify confidently. Do not convert uncertainty into PASS merely to reconcile counts.

---

## 7. Frozen PRE rule

When Work completes the structural screen, that board becomes the **frozen PRE artifact** for the later user-supplied XI/odds workflow.

The frozen record includes at least:

- PRE grade;
- structural archetype;
- route-quality state;
- CC+/CC+ candidate state where relevant;
- board tier/state;
- primary/secondary routes;
- main failure mode;
- XI sensitivity;
- structural burden/range;
- canonical corrected kickoff semantics.

Downstream stages may rerank or downgrade based on new evidence, and active post-XI rules may open documented EGE/MCE or strict carrier-reopen assessment epochs, but none may reconstruct a different frozen PRE from scratch.

---

## 8. Airtable publication rule

Step 0 publishes the coverage skeleton for fixtures actually discovered; it must not fabricate unseen raw rows merely to satisfy a total count.

Publishing the Work screen to `Daily Coverage Ledger` is a **copy/upsert of the frozen screen**, not another model run.

The publish step must preserve Work output exactly in the fields available in the Airtable contract, including route-quality and CC+ context in summary/notes.

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

Before Step 0 can set `complete:true` / `actionable_complete:true` / `work_ready:true`:

`ACTIONABLE SENIOR UNIVERSE = WORK-ADMITTED + ACTIONABLE-EXCLUDED/UNRESOLVED`

The exact all-raw equation is required only when `raw_audit_complete=true`.

When `raw_audit_complete=false`, discovered raw counts are a documented lower bound and all gaps must be confined to pre-excluded categories.

After Work research begins, the Work board cannot be called complete until:

`Work-admitted actionable = Focus + Watchlist + Pass + Unresolved`

Also verify:

- each actionable fixture appears once;
- all actionable exclusions have a reason;
- all Work-admitted fixtures have a PRE disposition;
- all FOCUS + WATCHLIST rows are persisted;
- no youth/reserve/lower/small fixture survives the actionable overlay;
- no Finnish domestic league fixture survives the actionable overlay;
- every strong-carrier B/PASS has a documented CC+ audit result;
- no potentially actionable senior block in the requested window is unaccounted for;
- no fixture outside the requested corrected ICT window appears on the board;
- no schedule-integrity unresolved fixture appears in the Work array;
- any raw gaps are explicitly marked non-blocking and outside model scope.

If Step-0 actionable counts or coverage fail:

`HANDOFF INCOMPLETE — ACTIONABLE COVERAGE GAP — RERUN NORMAL CHAT STEP 0`

**Do not start Work PRE research.**

If Step 0 passed but the Work disposition counts fail after research:

`WORK RECONCILIATION FAILED — frozen board incomplete`

---

## 10. Same-window survival and rerank

At confirmed XI, compare all surviving FOCUS/WATCHLIST candidates and any qualifying `CC+ CANDIDATE — XI SENSITIVE` carrier-reopen cases in the same practical kickoff window rather than reviewing them in isolation.

Use corrected `kickoff_ict`, not raw Airtable `Z` timestamps, to define the window.

The official v0.2.54 order is governed by `CURRENT_MODEL.md` and active patches.

Explicitly compare:

- quality-proven vs nominal two-sidedness;
- CC+ self-funded carrier ceiling;
- chance-quality support;
- failure-mode resistance;
- dependence on weaker-team contribution;
- required burden.

Confirmed XI is the first legitimate rerank gate after frozen PRE. Under v0.2.52, `ATTACKING DEPTH PRESERVED` is neutral baseline confirmation and does not by itself create an upgrade.

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

If an eligible fixture is discovered after a board was claimed actionable-complete:

1. classify the original actionable coverage claim as a coverage failure;
2. determine which traversal/filter/persistence step failed;
3. if still prematch, return to Step 0 and rebuild/reconcile the Work handoff before additional Work deep research;
4. if already started, label it a `MISSED PREMATCH OPPORTUNITY` and do not rewrite history;
5. fix the root cause before the next board is called actionable-complete.

A later-discovered youth/reserve/lower/hard-excluded fixture does **not** retroactively invalidate actionable completeness; add it to raw audit if useful.

If a historical board contains the wrong fixture date/time:

- preserve the original PRE record;
- annotate the schedule fault;
- correct future operational schedule data;
- exclude not-yet-played future fixtures from historical performance denominators.

A live result must never be used to pretend the omitted match would certainly have been selected prematch.

---

## 14. Authority

This controller is subordinate to upstream `CURRENT_MODEL.md`, `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`, and the active rule files, but it supersedes old coverage instructions that require exact enumeration of every excluded micro/youth/raw fixture before Work, allow Work to research a genuinely incomplete actionable handoff, rely on multi-source fixture unions, raw-UTC schedule display, stale upcoming timestamps, legacy competition whitelists, old automatic TWO-SIDED ranking, or a second structural screen during Airtable publication.

---

## 15. v0.2.53 coverage and ranking controls

### Required route fields

Every admitted fixture must carry:

- `Home Route State`: PROVEN / SUPPORTED / NOMINAL / FAILED;
- `Away Route State`: PROVEN / SUPPORTED / NOMINAL / FAILED;
- combined route pair;
- evidence confidence;
- league regime and any applicable high-burden gate result.

Apply the PRE caps and non-compensatory order in `MODEL_RULES_FOOTBALL_V0.2.53.md`. A tier cannot exceed its route-pair ceiling.

### Unique identity and conflict block

Use `AISCORE:<fixture_id>` as the canonical unique key when the ID exists. Use competition + normalized home + normalized away + kickoff_utc only as a fallback.

Before `work_ready:true`, frozen PRE publication, and schedule display:

1. collapse exact duplicate keys;
2. identify same-match rows with conflicting kickoff, slate date, grade, tier, eligibility, or completeness;
3. stop active publication/ranking for every unresolved conflict;
4. preserve the conflict rows for audit.

Required state:

`COVERAGE IDENTITY CONFLICT — PUBLICATION BLOCKED`

A conflicting row may not be treated as a second fixture, placed on two slate dates, or silently chosen by last-write-wins behavior.

### League controls

The registry hard exclusion for Japanese domestic leagues, including J1, is mandatory from 2026-09-12 ICT onward.

China Super League stays CONDITIONAL. A CSL O3.0+ or MCE candidate must also pass the v0.2.53 home/away-or-CC+ high-burden gate.

### Rolling calibration fields

For completed FOCUS/WATCHLIST rows retain route pair, chance-quality result, CC+ state, burden/regime, MCE validator result, contribution pattern, and final threshold result. The post-slate audit uses these fields to test whether FOCUS separates from WATCHLIST without reconstructing PRE.


---

## 16. v0.2.54 rank preservation

The frozen Work board must assign and persist a same-window Structural Rank for every surviving FOCUS/WATCHLIST candidate. Rank is based on route pair, chance quality, CC+, failure-mode resistance, lower supported burden and evidence confidence; price is absent.

At Step 2, keep Structural Rank separate from Execution Class. A candidate whose football clears but whose supplied line is too high or target-line price is too short becomes `QUALIFIED — WAIT FOR DECAY` and remains in the active ranked pool. A failed football/evidence gate becomes `STRUCTURAL HOLD`.

MCE/+0.25 and live/relative-decay Over states are shadow-only under v0.2.54 and cannot enter Website Picks or official P/L. They remain visible in Decision States for prospective audit.
