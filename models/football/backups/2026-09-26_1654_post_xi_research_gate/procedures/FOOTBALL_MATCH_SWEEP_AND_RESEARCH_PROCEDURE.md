# Football Match Sweep and Research Procedure

**Status:** ACTIVE  
**Official model:** Football A — active v0.2.55 stack  
**Fixture authority:** AiScore only  
**Timezone:** Asia/Ho_Chi_Minh (ICT)  
**Time authority:** `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`

This procedure separates **fixture discovery** from **match research**, enforces the current senior-quality actionable overlay, prevents overnight/date-boundary omissions, and uses durable staged checkpoints so long AiScore sweeps can resume after a tool/chat interruption without restarting completed work.

---

## 1. Authority boundary

### Fixture discovery

Only AiScore may establish a fixture in the requested slate:

- `aiscore.com`
- `m.aiscore.com`
- AiScore daily/live listings
- AiScore match pages

Do not build a fixture union from Soccerway, FotMob, Google/web search, BSD/Bzzoiro, league sites, bookmaker pages, or another schedule provider.

If another source shows a match, it may enter the slate only after the same fixture is verified on AiScore.

### Match research

After AiScore establishes the fixture, research is source-flexible. Use the strongest available match-level evidence, including official competition/club sources, Soccerway, FotMob, FBref, BSD/Bzzoiro where supported, reputable statistics/news sources, and user-supplied screenshots.

Research may refine the thesis; it may not expand the fixture universe.

---

## 2. Requested-window traversal

Follow `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md` exactly.

1. Resolve `window_start_ict`, `window_end_ict`, `window_start_utc`, and `window_end_utc` once.
2. Record every ICT and UTC calendar date touched.
3. Build the deterministic discovery envelope: ICT dates touched + UTC dates touched + one UTC date before + one UTC date after.
4. Traverse all relevant AiScore date/listing blocks across that envelope.
5. For every discovered fixture preserve AiScore identity, discovery listing date, raw/source kickoff text, source local time, timezone/offset, AiScore-supplied UTC when explicitly available, and fetch status.
6. Do **not** convert every fixture to ICT during normal discovery.
7. If AiScore supplies UTC, compare it directly to the normalized requested UTC window for cheap membership testing.
8. If AiScore supplies an explicit offset, an ephemeral UTC value may be used only for membership testing while preserving source fields.
9. Carry boundary cases as `WINDOW STATUS = PENDING CONVERSION` when later schedule normalization is required.
10. Deduplicate by AiScore fixture ID where available; otherwise use competition + normalized teams + safe source-time identity.
11. Do not stop when enough attractive matches have been found.

A timestamp ending in `Z` is UTC, not ICT. Exact fixture ICT conversion belongs to the later scheduling stage.

### Cross-midnight rule

If the window crosses midnight or ends between 00:00 and 06:00 ICT, explicitly inspect the terminal ICT calendar date and the UTC date containing `window_end_utc`.

A last-found kickoff before the requested cutoff is **not evidence that no later block exists**. Run the independent terminal sentinel described below.

---

## 2.1 Durable restart-safe stage sequence

Use Airtable `Sweep Runs` (`tblUnGHHe0MVaalDL`) as the run-level checkpoint store.

For each requested sweep create/reuse one stable Run ID and execute:

`CORE DISCOVERY → CONDITIONAL GATES → EUROPEAN CUP AUDIT → TERMINAL SENTINEL → RECONCILIATION → PACKAGING`

Checkpoint each completed stage before beginning the next. Persist fixture rows discovered by that stage to `Daily Coverage Ledger` in batches. If execution stops, resume from the first incomplete Sweep Runs stage; do not repeat completed stages.

Stage boundaries:

- **CORE DISCOVERY:** boundary math, discovery envelope, direct senior blocks, early exclusions, source-time/identity capture, fixture-ledger upserts.
- **CONDITIONAL GATES:** cheap current registry tests only; persist pass/fail.
- **EUROPEAN CUP AUDIT:** separate AiScore-only UEFA domestic-cup traversal over touched dates.
- **TERMINAL SENTINEL:** independent `max(window_start, window_end - 6h) -> window_end` AiScore pass.
- **RECONCILIATION:** identity/dedupe/source-time conflicts, actionable equations, admitted-array equality, completeness flags.
- **PACKAGING:** canonical UTF-8 handoff text followed by exactly-one-file ZIP validation.

A timeout never converts an incomplete stage to complete, but it also never invalidates previously completed checkpoint stages unless a later missed-fixture audit triggers the formal recovery rule.

---

## 3. Schedule/date integrity gate

Before a discovered fixture can proceed to eligibility or structural screening, verify:

- source-time identity is interpretable under the active time procedure;
- when AiScore supplies UTC/offset, cheap membership testing places the fixture inside the requested normalized window or marks it pending conversion;
- AiScore daily-listing identity and match-page identity agree;
- no contradictory source-time state prevents later one-time ICT conversion;
- the fixture is not a stale/future match surfaced through a competition page outside the requested window.

If any of these fail or remain contradictory:

`UNRESOLVED — SCHEDULE INTEGRITY`

Do not send that fixture into FOCUS/WATCHLIST betting evaluation until corrected.

---

## 4. Completeness audit before filtering

Before the raw AiScore handoff can say `audit.complete = true`, verify:

- all AiScore date listings touched by the ICT window were traversed;
- the start and terminal cutoff blocks were checked;
- every discovered fixture was normalized and counted once;
- no known AiScore competition block inside the window is unaccounted for;
- no pagination/lazy-loading/league-section traversal remains unresolved;
- all included fixtures passed schedule/date integrity.

If any item is unresolved, state:

`COVERAGE INCOMPLETE — AiScore sweep incomplete`

and set completeness false. Do not backfill from another provider.

---

## 5. Current actionable competition overlay

Apply the user’s **senior-quality-only** overlay after the raw AiScore universe and time-integrity checks are complete.

Exclude:

- U17/U18/U19/U20/U21/U23 and other youth/Uxx competitions;
- academy/junior competitions;
- reserve/B-team/development competitions;
- amateur/semi-professional competitions;
- regional/state/provincial leagues;
- very small/obscure weak-data leagues;
- domestic lower divisions below top flight unless explicitly user-approved or explicitly whitelisted;
- **all Finnish domestic league competitions at every tier/category, including men's and women's leagues — hard exclusion effective 2026-09-09 ICT onward.**

### Netherlands Eerste Divisie Jong/U21 participant exception — effective 2026-09-19 ICT

The Netherlands **Eerste Divisie** is an explicitly approved lower division. Official Eerste Divisie fixtures involving participant teams whose names contain **Jong**, **U21**, or equivalent reserve/development branding are now **included in the normal actionable sweep**.

This includes, where they are official Eerste Divisie participants, teams such as Jong Ajax, Jong PSV, Jong AZ, Jong FC Utrecht, and equivalent U21-labelled entrants.

This is a **competition-scoped participant exception only**:

- it applies only when the fixture itself is an official Netherlands Eerste Divisie league match;
- it overrides the generic youth/Uxx/reserve/development exclusion for those Eerste Divisie participants;
- it does **not** whitelist separate youth/U21/reserve/development competitions, friendlies, cups, or reserve leagues;
- it provides no PRE grade, structural, ranking, or betting bonus. Normal match-level screening still applies.

An official Eerste Divisie fixture must not be excluded merely because one or both clubs are Jong/U21/reserve-branded.

The Finnish-league exclusion is prospective. Keep all Finnish domestic league fixtures in the raw AiScore universe for reconciliation, but classify them as excluded before structural screening. Finnish Cup and UEFA club competitions involving Finnish clubs remain governed by the normal overlay.

Do not weaken this overlay to fill the slate.

Senior first-team continental competitions remain actionable when they otherwise clear the overlay, explicitly including UEFA Champions League, UEFA Europa League, and UEFA Conference League.

Every removal must remain auditable as an explicit exclusion rather than a silent omission.

---

## 6. Handoff contract

A fixture handoff used by Work must identify at minimum:

- requested ICT window;
- source = AiScore;
- raw fixture count;
- actionable eligible count;
- excluded count and exclusion reasons/categories;
- `actionable_overlay = senior_quality_only`;
- `audit.complete`;
- complete actionable fixture list with competition names;
- AiScore fixture ID or canonical match identity where available;
- source kickoff local time/text;
- source timezone/offset where supplied;
- AiScore-supplied UTC when explicitly available;
- `window_status=confirmed|pending_conversion`;
- status at fetch.

`kickoff_ict` is not required in the Step-0 handoff.

Required invariant:

`Raw AiScore universe = Actionable eligible + Excluded`

Schedule-integrity unresolved fixtures must remain explicitly accounted for; they may not disappear silently from reconciliation.

If the invariant fails, the handoff is provisional and must not be treated as a complete board input.

---

## 7. Structural research stage

The Work structural sweep processes **every actionable fixture** before display shortening.

Research/evaluate:

- structural matchup quality;
- credible independent scoring routes;
- whether two-sidedness is `QUALITY PROVEN` or only `NOMINAL / WEAK SECONDARY`;
- carrier/favorite self-funded ceiling;
- `CC+ — CARRIER CEILING` eligibility or `CC+ CANDIDATE — XI SENSITIVE` status;
- opponent contribution;
- failure-mode resistance;
- team GF/GA and scoring/conceding frequencies;
- home/away and competition-specific context where useful;
- chance-quality support;
- format/incentive/game-state risk;
- lineup sensitivity as a future rerank item;
- structural goal-burden ceiling/range.

### 7.1 Mandatory carrier-ceiling audit before B/PASS

Before assigning `B / PASS` to a fixture containing a strong favorite/carrier, explicitly answer:

1. Does either team have credible independent 3+ team-goal potential?
2. Is the recent low-scoring profile supported by true chance suppression, or could it be score outcome / finishing / schedule noise?
3. Is the ceiling repeatable enough to survive a weak opponent-contribution route?

If credible independent 3+ potential exists but XI uncertainty prevents promotion, tag:

`CC+ CANDIDATE — XI SENSITIVE`

and keep the match eligible for the later post-XI carrier review unless a separate dominant structural failure requires PASS.

Do not use a single historical 3+ result as CC+ proof.

### 7.2 Price/XI boundary

The Work PRE stage is **price-blind**. Do not use bookmaker price to improve a structural grade or ranking.

Under the current user workflow, do not automatically fetch confirmed XI or bookmaker odds during this structural stage. The user supplies them later.

The EGE regime is post-XI and must not be manufactured at PRE from bookmaker totals.

---

## 8. Board output and freeze

Give every actionable fixture exactly one PRE disposition:

- `FOCUS`
- `WATCHLIST`
- `PASS`
- `UNRESOLVED`

Use the current PRE grades/types defined by the active model.

Two-Sided Tier A remains the primary lane. For comparable non-Tier-A candidates rank:

`QUALITY-PROVEN TWO-SIDED > CC+ ELITE CARRIER > NOMINAL / WEAK-SECONDARY TWO-SIDED > ordinary CARRIER-LED > FRAGILE / OTHER`

Do **not** automatically rank a B+ nominal two-sided match above a carrier with a materially stronger self-funded ceiling.

For every FOCUS/WATCHLIST row, preserve whether the route label is quality-proven or nominal. For every strong-carrier B/PASS row, preserve why CC+ failed or whether it remains `CC+ CANDIDATE — XI SENSITIVE`.

Assign every surviving FOCUS/WATCHLIST candidate a stable same-window Structural Rank plus supported burden/range. The Work output is a **frozen structural PRE board**, not an official betting card.

Until user-supplied XI + odds arrive:

- XI status = user will supply later;
- market status = user will supply later;
- price status = not evaluated;
- no official line;
- no OFFICIAL LOCK.

---

## 9. Frozen-state persistence

Persist the Work screen to the Daily Coverage Ledger without re-screening it.

Publishing is a state-copy/upsert operation:

- preserve PRE grade;
- preserve structural type;
- preserve FOCUS/WATCHLIST/PASS/UNRESOLVED exactly;
- preserve route-quality label and CC+/CC+ candidate state in summary/notes;
- preserve the frozen thesis/failure mode;
- preserve canonical fixture identity and normalized kickoff semantics;
- mark XI/market pending as appropriate.

A downstream publish step must not independently downgrade a Work WATCHLIST/FOCUS row to PASS.

If persisted Airtable state conflicts with the original frozen Work board, flag a synchronization fault and preserve the original frozen thesis until the persistence error is corrected.

---

## 10. Coverage reconciliation

Before claiming the structural board is complete, verify:

`Universe = Actionable eligible + Excluded`

`Actionable eligible = Focus + Watchlist + Pass + Unresolved`

Also verify:

- no skipped actionable fixture;
- no duplicate processing;
- no excluded youth/reserve/lower/small fixture survived, except the explicit Netherlands Eerste Divisie Jong/U21 participant exception for official Eerste Divisie league fixtures;
- no Finnish domestic league fixture survives the actionable overlay from 2026-09-09 ICT onward;
- all FOCUS/WATCHLIST candidates are persisted for the later XI stage;
- every strong-carrier PASS has a documented CC+ audit result;
- cross-midnight/date-page completeness remains true;
- every actionable row has a schedule-integrity-safe kickoff;
- no future-date fixture outside the requested window survives.

If any check fails, state:

`COVERAGE INCOMPLETE — board provisional`

---

## 11. Upcoming schedule revalidation

A frozen board is not a perpetual schedule authority.

When a later chat asks for `upcoming`, `next matches`, or a timetable:

- resolve current ICT time;
- read the frozen board/Airtable bridge;
- revalidate near-term AiScore status under `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`;
- remove LIVE/HT/FT/postponed/cancelled rows from the upcoming list;
- sort by corrected `kickoff_ict`.

Do not assume a stored kickoff is still future simply because Airtable says so.

---

## 12. Research-source rule after freeze

Once a fixture is in the frozen PRE board, later XI/odds/live stages may use user screenshots and normal research evidence. That evidence may validate, downgrade, rerank, or qualify a strict `CARRIER REOPEN — XI CONFIRMED`, post-XI EGE burden, or MCE state according to the current model, but it must not silently rewrite what PRE originally was.

Live evidence validates or invalidates history; it does not rewrite history.

---

## 13. v0.2.53 ranking-integrity overlay

This section is mandatory for every prospective sweep under Football v0.2.53.

### Route proof before tier

Grade the home and away scoring routes separately as `PROVEN`, `SUPPORTED`, `NOMINAL`, or `FAILED`. Preserve the combined pair in the frozen output.

Apply the v0.2.53 PRE caps:

- `PROVEN + PROVEN` — A1 / FOCUS eligible;
- `PROVEN + SUPPORTED` — A2 / FOCUS eligible;
- `SUPPORTED + SUPPORTED` — A2 / FOCUS only with strong chance quality and failure resistance;
- `PROVEN + NOMINAL` — WATCHLIST unless the proven route is true CC+;
- `SUPPORTED + NOMINAL` — B+ / WATCHLIST;
- `NOMINAL + NOMINAL` — PASS;
- any `FAILED` route — WATCHLIST at most and normally PASS unless true CC+ survives the failure branch;
- any data-poor substitute — A2 maximum.

FOCUS additionally requires that the supported burden survives the named dominant failure mode. Raw GF/GA, names, opponent leakage, XI preservation, or price may not compensate for a failed route gate.

### Relative ranking

Within each practical kickoff window, rerank by route pair, chance quality, CC+ ceiling, failure-mode resistance, lower supported burden, and evidence confidence. The previously printed grade is not an automatic tiebreaker.

### League gates

Apply the active league registry before promotion. Japanese domestic leagues, including J1, are hard-excluded from 2026-09-12 ICT onward.

For China Super League O3.0+ candidates, require both relevant home/away route environments to support 3+ or one true CC+ carrier. Otherwise record `CSL HIGH-BURDEN GATE FAILED`.

### Identity gate

Use `AISCORE:<fixture_id>` as the preferred unique key. If no ID exists, use competition + normalized teams + kickoff_utc.

Before freezing or publishing, block conflicting duplicate identities:

`COVERAGE IDENTITY CONFLICT — PUBLICATION BLOCKED`

No unresolved duplicate may appear twice in a ranking pool or on two slate dates.


---

## 14. v0.2.54 structural-rank output

Within every practical kickoff window, freeze the full candidate order—not only FOCUS/WATCHLIST labels. For each surviving candidate record Structural Rank, route pair, chance-quality state, CC+ state, dominant failure mode, supported burden/range and evidence confidence.

Do not create a price-derived HOLD during Work. At Step 2, a structurally qualified candidate with an unavailable/too-short target offer becomes `QUALIFIED — WAIT FOR DECAY`; a candidate with failed football gates becomes `STRUCTURAL HOLD`. These states must remain distinct for ranking and audit.
