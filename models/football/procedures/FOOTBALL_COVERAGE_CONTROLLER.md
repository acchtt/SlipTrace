# Football Coverage Controller

**Status:** ACTIVE  
**Official model:** Football v0.2.49  
**Coverage authority:** AiScore fixture universe + current senior-quality overlay

The coverage controller prevents silent fixture omission and prevents downstream stages from replacing a frozen Work PRE state with a second screen.

---

## 1. Production sequence

The required sequence is:

`AISCORE UNIVERSE → SENIOR-QUALITY ELIGIBILITY → SCREEN EVERY ACTIONABLE FIXTURE → FOCUS/WATCHLIST/PASS/UNRESOLVED → FREEZE PRE → PERSIST → USER-SUPPLIED XI RERANK → GOAL BURDEN → USER-SUPPLIED PRICE → OFFICIAL/SHADOW VERDICTS`

Do not begin by selecting a few credible candidates. Every actionable fixture must be screened first.

**SHORTEN THE DISPLAY, NEVER THE SCREENED UNIVERSE.**

---

## 2. AiScore traversal gate

Coverage cannot pass until the entire requested ICT window is accounted for on AiScore.

Required checks:

- every AiScore calendar-date listing touched by the window is traversed;
- overnight continuation is explicitly traversed rather than inferred;
- terminal requested kickoff interval/cutoff is checked;
- every discovered fixture is normalized to ICT and counted once;
- no known AiScore competition/league block inside the window remains unvisited or unresolved.

If a window crosses midnight, both calendar dates are mandatory traversal targets. If the cutoff is 03:00 ICT, verify the 03:00 interval even when the latest discovered fixture is earlier.

If this gate fails:

`COVERAGE INCOMPLETE — AiScore sweep incomplete`

No other schedule provider may backfill the universe.

---

## 3. Current eligibility gate — senior-quality overlay

For the normal actionable betting board, exclude:

- youth/Uxx: U17, U18, U19, U20, U21, U23 and equivalent youth competitions;
- academy/junior competitions;
- reserve/B-team/development competitions;
- amateur/semi-professional competitions;
- regional/state/provincial leagues;
- very small/obscure weak-data leagues;
- domestic lower divisions below top flight unless explicitly user-approved or explicitly whitelisted;
- **all Finnish domestic league competitions at every tier/category, including men's and women's leagues — hard exclusion effective 2026-09-09 ICT onward.**

The Finnish-league rule is prospective. All Finnish domestic league fixtures remain in the raw AiScore universe but must be marked `EXCLUDED`; they must never receive FOCUS/WATCHLIST status or reach official betting evaluation. This includes Veikkausliiga and all lower-tier Finnish leagues. Finnish Cup and UEFA club competitions involving Finnish clubs are not excluded by this rule unless another active eligibility rule removes them.

These fixtures remain part of the raw AiScore universe but must be marked excluded rather than silently omitted.

Do not inherit legacy blanket exclusions for continental football or cup labels. Senior first-team continental competitions are actionable when otherwise eligible, including UEFA Champions League, UEFA Europa League, and UEFA Conference League.

Do not weaken the overlay because the slate is small.

---

## 4. Screening requirement

Every actionable fixture receives:

- competition and kickoff ICT;
- PRE grade;
- structural archetype;
- primary scoring route;
- secondary route/opponent contribution where relevant;
- main failure mode;
- XI sensitivity;
- structural total range/ceiling when supportable;
- one board state: `FOCUS`, `WATCHLIST`, `PASS`, or `UNRESOLVED`.

Use the current official model hierarchy. For comparable v0.2.49 grades:

`TWO-SIDED > ELITE CARRIER > CARRIER-LED > FRAGILE / OTHER`

Price is not part of PRE ranking.

---

## 5. FOCUS / WATCHLIST / PASS semantics

### FOCUS

The strongest provisional candidates deserving first XI/market attention. FOCUS is not automatically a bet.

### WATCHLIST

Structurally live candidates with one or more material failure modes or sensitivity points. WATCHLIST survives to the confirmed-XI stage unless explicitly downgraded by new material evidence.

### PASS

The structural route did not clear the current PRE standard. Price or recognizable XI names may not resurrect a genuine PRE PASS without a documented material structural change.

### UNRESOLVED

Required information is insufficient to classify confidently. Do not convert uncertainty into PASS merely to reconcile counts.

---

## 6. Frozen PRE rule

When Work completes the structural screen, that board becomes the **frozen PRE artifact** for the later user-supplied XI/odds workflow.

The frozen record includes at least:

- PRE grade;
- structural archetype;
- board tier/state;
- primary/secondary routes;
- main failure mode;
- XI sensitivity;
- structural burden/range.

Downstream stages may rerank or downgrade based on new evidence, but they must start from this frozen state and must not reconstruct a different PRE from scratch.

---

## 7. Airtable publication rule

Publishing the Work screen to `Daily Coverage Ledger` is a **copy/upsert of the frozen screen**, not another model run.

The publish step must preserve Work output exactly in the fields available in the Airtable contract.

Forbidden behavior:

- Work says `WATCHLIST` but Airtable publisher independently writes `PASS`;
- Work says `A2` but publisher independently rewrites `B / PASS`;
- publisher substitutes a fresh secondary-source thesis for the frozen Work thesis.

If the persisted row conflicts with the original Work board, classify:

`PERSISTENCE SYNC FAULT — frozen PRE preserved`

Correct the persistence layer rather than treating the bad row as decision authority.

---

## 8. Count invariants

The board cannot be called complete until both equations reconcile:

`Universe = Actionable eligible + Excluded`

`Actionable eligible = Focus + Watchlist + Pass + Unresolved`

Also verify:

- each fixture appears once;
- all exclusions have a reason;
- all actionable fixtures have a PRE disposition;
- all FOCUS + WATCHLIST rows are persisted;
- no youth/reserve/lower/small fixture survives the actionable overlay;
- no Finnish domestic league fixture survives the actionable overlay from 2026-09-09 ICT onward;
- no date/competition block within the requested AiScore window is unaccounted for.

If counts or coverage fail:

`COVERAGE INCOMPLETE — board provisional`

---

## 9. Same-window survival and rerank

At confirmed XI, compare all surviving FOCUS/WATCHLIST candidates in the same practical kickoff window rather than reviewing them in isolation.

The official v0.2.49 order remains:

`STRUCTURAL QUALITY → CARRIER CEILING → FAILURE-MODE RESISTANCE → TEAM GF/GA PROFILE → CHANCE QUALITY → XI RERANK → GOAL BURDEN → PRICE`

At comparable grades, keep the v0.2.49 structural archetype priority.

Confirmed XI is the first legitimate rerank gate after frozen PRE.

---

## 10. Current user-supplied-input boundary

Normal pre-kickoff execution does not automatically fetch XI or bookmaker odds.

Until the user supplies the required current XI + odds:

- FOCUS/WATCHLIST remains provisional;
- market/price remains unevaluated;
- no official line is selected;
- no OFFICIAL LOCK is issued.

Only search externally for XI/odds when the user explicitly asks for external verification.

---

## 11. Missed-fixture recovery

If an eligible fixture is discovered after a board was claimed complete:

1. classify the original coverage claim as a coverage failure;
2. determine which traversal/filter/persistence step failed;
3. if still prematch, screen it immediately and compare it against the full frozen board;
4. if already started, label it a `MISSED PREMATCH OPPORTUNITY` and do not rewrite history;
5. fix the root cause before the next board is called complete.

A live result must never be used to pretend the omitted match would certainly have been selected prematch.

---

## 12. Authority

This controller is subordinate to `CURRENT_MODEL.md` and the active rule files, but it supersedes old coverage instructions that rely on multi-source fixture unions, legacy competition whitelists, or a second structural screen during Airtable publication.
