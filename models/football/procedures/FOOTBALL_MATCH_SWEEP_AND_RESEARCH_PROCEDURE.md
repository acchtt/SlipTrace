# Football Match Sweep and Research Procedure

**Status:** ACTIVE  
**Official model:** Football v0.2.50  
**Fixture authority:** AiScore only  
**Timezone:** Asia/Ho_Chi_Minh (ICT)  
**Time authority:** `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`

This procedure separates **fixture discovery** from **match research**, enforces the current senior-quality actionable overlay, prevents overnight/date-boundary omissions, and routes every timestamp through the canonical UTC→ICT integrity layer.

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

1. Resolve the exact requested ICT start and end.
2. Determine every **ICT calendar date touched by that window**.
3. Traverse the corresponding AiScore date listings explicitly.
4. For each discovered fixture, preserve AiScore identity, raw/source kickoff text and listing date where available.
5. Normalize to canonical `kickoff_utc`.
6. Convert `kickoff_utc` exactly once to `kickoff_ict` using `Asia/Ho_Chi_Minh`.
7. Derive `slate_date_ict` from `kickoff_ict`.
8. Keep only fixtures whose corrected `kickoff_ict` falls inside the requested window.
9. Deduplicate by AiScore fixture ID where available; otherwise use competition + normalized teams + kickoff_utc.
10. Do not stop when enough attractive matches have been found.

A timestamp ending in `Z` is UTC, not ICT.

### Cross-midnight rule

If the window crosses midnight, browsing only the starting date is incomplete. Every ICT date touched by the window must be traversed.

Example: an evening slate that continues through 03:00 ICT requires explicit traversal of both the evening date and the following date.

A last-found kickoff before the requested cutoff is **not evidence that no later block exists**. Verify the terminal interval/date listing itself.

---

## 3. Schedule/date integrity gate

Before a discovered fixture can proceed to eligibility or structural screening, verify:

- the normalized kickoff falls inside the requested ICT window;
- AiScore daily-listing identity and match-page identity agree;
- the match-page date/time is compatible with the normalized `kickoff_ict`;
- `slate_date_ict` is derived from the converted kickoff rather than copied blindly from a page label;
- the fixture is not a stale/future match surfaced through a competition page outside the requested window.

If any of these fail or remain contradictory:

`UNRESOLVED — SCHEDULE INTEGRITY`

Do not send that fixture into FOCUS/WATCHLIST betting evaluation until corrected.

This gate specifically prevents future-date fixtures from being inserted into a current daily board.

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

A sweep ending at 03:00 ICT cannot infer completeness merely because its latest captured fixture is 02:00. The 03:00 interval must be explicitly verified.

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

The Finnish-league exclusion is prospective. Keep all Finnish domestic league fixtures in the raw AiScore universe for reconciliation, but classify them as excluded before structural screening. Do not surface them as FOCUS/WATCHLIST or send them to XI/market evaluation. Finnish Cup and UEFA club competitions involving Finnish clubs remain governed by the normal overlay and are not automatically removed by this league-only rule.

Do not weaken this overlay to fill the slate.

Do **not** apply an old generic “continental competitions excluded” rule. Senior first-team continental competitions remain actionable when they otherwise clear the overlay, explicitly including UEFA Champions League, UEFA Europa League, and UEFA Conference League.

Do not exclude an otherwise qualifying senior competition merely because its name contains `Cup`, `League Cup`, or `continental` terminology.

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
- `kickoff_utc`;
- `kickoff_ict`;
- `slate_date_ict`;
- status at fetch.

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
- two-sided contribution;
- carrier/favorite ceiling;
- opponent contribution;
- failure-mode resistance;
- team GF/GA and scoring/conceding frequencies;
- home/away and competition-specific context where useful;
- chance-quality support;
- format/incentive/game-state risk;
- lineup sensitivity as a future rerank item;
- structural goal-burden ceiling/range.

The Work PRE stage is **price-blind**. Do not use bookmaker price to improve a structural grade or ranking.

Under the current user workflow, do not automatically fetch confirmed XI or bookmaker odds during this structural stage. The user supplies them later.

The EGE regime introduced in v0.2.50 is a **post-XI** classification and must not be manufactured at PRE from bookmaker totals.

---

## 8. Board output and freeze

Give every actionable fixture exactly one PRE disposition:

- `FOCUS`
- `WATCHLIST`
- `PASS`
- `UNRESOLVED`

Use the current PRE grades/types defined by the active model.

Rank surviving FOCUS + WATCHLIST candidates under the active official hierarchy. For comparable grades:

`TWO-SIDED > ELITE CARRIER > CARRIER-LED > FRAGILE / OTHER`

The Work output is a **frozen structural PRE board**, not an official betting card.

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
- preserve the frozen thesis/failure mode in the available summary/notes fields;
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
- no excluded youth/reserve/lower/small fixture survived;
- no Finnish domestic league fixture survives the actionable overlay from 2026-09-09 ICT onward;
- all FOCUS/WATCHLIST candidates are persisted for the later XI stage;
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

Once a fixture is in the frozen PRE board, later XI/odds/live stages may use user screenshots and normal research evidence. That evidence may validate, downgrade, rerank, or qualify a post-XI EGE burden according to the current model, but it must not silently rewrite what PRE originally was.

Live evidence validates or invalidates history; it does not rewrite history.
