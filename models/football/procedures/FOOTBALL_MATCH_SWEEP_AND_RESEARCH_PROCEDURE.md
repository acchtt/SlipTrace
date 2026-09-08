# Football Match Sweep and Research Procedure

**Status:** ACTIVE  
**Official model:** Football v0.2.49  
**Fixture authority:** AiScore only  
**Timezone:** Asia/Ho_Chi_Minh (ICT)

This procedure separates **fixture discovery** from **match research**. It also enforces the current senior-quality actionable overlay and prevents overnight/date-boundary omissions.

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
4. Normalize every discovered kickoff to ICT.
5. Keep only fixtures whose normalized kickoff falls inside the requested window.
6. Deduplicate the same fixture if AiScore exposes it through more than one listing/view.
7. Do not stop when enough attractive matches have been found.

### Cross-midnight rule

If the window crosses midnight, browsing only the starting date is incomplete. Every date touched by the window must be traversed.

Example: an evening slate that continues through 03:00 ICT requires explicit traversal of both the evening date and the following date.

A last-found kickoff before the requested cutoff is **not evidence that no later block exists**. Verify the terminal interval/date listing itself.

---

## 3. Completeness audit before filtering

Before the raw AiScore handoff can say `audit.complete = true`, verify:

- all AiScore date listings touched by the ICT window were traversed;
- the start and terminal cutoff blocks were checked;
- every discovered fixture was normalized and counted once;
- no known AiScore competition block inside the window is unaccounted for;
- no pagination/lazy-loading/league-section traversal remains unresolved.

If any item is unresolved, state:

`COVERAGE INCOMPLETE — AiScore sweep incomplete`

and set completeness false. Do not backfill from another provider.

A sweep ending at 03:00 ICT cannot infer completeness merely because its latest captured fixture is 02:00. The 03:00 interval must be explicitly verified.

---

## 4. Current actionable competition overlay

Apply the user’s **senior-quality-only** overlay after the raw AiScore universe is complete.

Exclude:

- U17/U18/U19/U20/U21/U23 and other youth/Uxx competitions;
- academy/junior competitions;
- reserve/B-team/development competitions;
- amateur/semi-professional competitions;
- regional/state/provincial leagues;
- very small/obscure weak-data leagues;
- domestic lower divisions below top flight unless explicitly user-approved or explicitly whitelisted.

Do not weaken this overlay to fill the slate.

Do **not** apply an old generic “continental competitions excluded” rule. Senior first-team continental competitions remain actionable when they otherwise clear the overlay, explicitly including UEFA Champions League, UEFA Europa League, and UEFA Conference League.

Do not exclude an otherwise qualifying senior competition merely because its name contains `Cup`, `League Cup`, or `continental` terminology.

Every removal must remain auditable as an explicit exclusion rather than a silent omission.

---

## 5. Handoff contract

A fixture handoff used by Work must identify at minimum:

- requested ICT window;
- source = AiScore;
- raw fixture count;
- actionable eligible count;
- excluded count and exclusion reasons/categories;
- `actionable_overlay = senior_quality_only`;
- `audit.complete`;
- the complete actionable fixture list with ICT kickoffs and competition names.

Required invariant:

`Raw AiScore universe = Actionable eligible + Excluded`

If the invariant fails, the handoff is provisional and must not be treated as a complete board input.

---

## 6. Structural research stage

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

---

## 7. Board output and freeze

Give every actionable fixture exactly one PRE disposition:

- `FOCUS`
- `WATCHLIST`
- `PASS`
- `UNRESOLVED`

Use the current PRE grades/types defined by the active model.

Rank surviving FOCUS + WATCHLIST candidates under v0.2.49. For comparable grades:

`TWO-SIDED > ELITE CARRIER > CARRIER-LED > FRAGILE / OTHER`

The Work output is a **frozen structural PRE board**, not an official betting card.

Until user-supplied XI + odds arrive:

- XI status = user will supply later;
- market status = user will supply later;
- price status = not evaluated;
- no official line;
- no OFFICIAL LOCK.

---

## 8. Frozen-state persistence

Persist the Work screen to the Daily Coverage Ledger without re-screening it.

Publishing is a state-copy/upsert operation:

- preserve PRE grade;
- preserve structural type;
- preserve FOCUS/WATCHLIST/PASS/UNRESOLVED exactly;
- preserve the frozen thesis/failure mode in the available summary/notes fields;
- mark XI/market pending as appropriate.

A downstream publish step must not independently downgrade a Work WATCHLIST/FOCUS row to PASS.

If persisted Airtable state conflicts with the original frozen Work board, flag a synchronization fault and preserve the original frozen thesis until the persistence error is corrected.

---

## 9. Coverage reconciliation

Before claiming the structural board is complete, verify:

`Universe = Actionable eligible + Excluded`

`Actionable eligible = Focus + Watchlist + Pass + Unresolved`

Also verify:

- no skipped actionable fixture;
- no duplicate processing;
- no excluded youth/reserve/lower/small fixture survived;
- all FOCUS/WATCHLIST candidates are persisted for the later XI stage;
- cross-midnight/date-page completeness remains true.

If any check fails, state:

`COVERAGE INCOMPLETE — board provisional`

---

## 10. Research-source rule after freeze

Once a fixture is in the frozen PRE board, later XI/odds/live stages may use user screenshots and normal research evidence. That evidence may validate, downgrade, or rerank the frozen thesis according to the current model, but it must not silently rewrite what PRE originally was.

Live evidence validates or invalidates history; it does not rewrite history.
