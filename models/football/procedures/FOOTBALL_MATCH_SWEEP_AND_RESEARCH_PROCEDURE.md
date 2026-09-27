# Football Match Sweep and Research Procedure

**Status:** ACTIVE  
**Official model:** Football A — current active stack  
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

The research stage must populate the fixed evidence channels required by:

`models/football/procedures/FOOTBALL_PRE_DECISION_SPEC.md`

For each team collect, where available:

- CQ — chance quality / creation;
- REP — current repeatability;
- MECH — independent scoring mechanism;
- CTX — relevant home/away/competition context;
- supporting-only OPP / FORM / NAME / H2H / STATE evidence;
- negative SUPPRESS / MECH_BREAK / ROLE_RISK / FATIGUE_ROTATION / DATA_CONFLICT evidence;
- source quality and explicit UNKNOWN items.

Do not assign the route state while research is still incomplete. Evidence collection and football judgment remain separate operations.

### 7.1 Compiled PRE judgment — mandatory

After the evidence packet is frozen, execute `FOOTBALL_PRE_DECISION_SPEC.md` exactly:

`HOME ROUTE -> AWAY ROUTE -> SECOND-ROUTE INDEPENDENCE -> PRACTICAL CARRIER -> FAILURE/VETO -> GRADE -> BOARD TIER -> PASS RESCUE -> SUPPORTED BURDEN -> RANK FACTORS`

The compiled spec is final Step-1 authority where older procedure/rule wording conflicts or is ambiguous.

### 7.2 Price/XI boundary

The Work PRE stage is **price-blind and confirmed-XI-blind**.

- do not use bookmaker price/line/market movement to improve PRE;
- do not fetch or use confirmed XI to clear a Step-1 tier;
- do not manufacture post-XI EGE/current-PRE states at Work;
- preserve XI sensitivity as a later-rerank field.

A `SUPPORTED + SUPPORTED` A2 is therefore Step-1 WATCHLIST maximum under the compiled spec. Step 2 may create a fresh current state only under its active XI/post-XI rules.

---

## 8. Board output and freeze

Give every actionable fixture exactly one PRE disposition:

- `FOCUS`
- `WATCHLIST`
- `PASS`
- `UNRESOLVED`

Every actionable fixture must freeze the complete `FOOTBALL_PRE_DECISION_SPEC_V1` trace before ranking.

PRE Structural Rank uses only the compiled Practical Ceiling order:

`PRACTICAL SELF-FUNDED 3+ CEILING -> OPPONENT FAILURE COMPATIBILITY -> CHANCE QUALITY/URGENCY -> FAILURE RESISTANCE -> SECONDARY-ROUTE QUALITY -> ROUTE SYMMETRY/GRADE -> SUPPORTED-BURDEN FIT -> EVIDENCE CONFIDENCE`

Do **not** use the superseded automatic hierarchy `QUALITY-PROVEN TWO-SIDED > CC+ ELITE CARRIER > ...` as an independent rank rule.

A VERIFIED B+ carrier may rank above an ordinary A2 when the practical 3+ path is stronger. A CANDIDATE carrier may not receive that rank privilege.

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

Once a fixture is in the frozen PRE board, later XI/odds/live stages may use user screenshots and normal research evidence, but **Step 2 XI+odds has an additional mandatory post-XI football web-research gate** under `MODEL_RULES_FOOTBALL_A_POST_XI_WEB_RESEARCH_GATE.md`.

For Step 2, after the supplied confirmed XI is read and before the final prematch verdict, Normal Chat must make a targeted fixture-specific web-research attempt. This is separate from the market-history watch and cannot be satisfied by frozen PRE/Airtable/model files alone.

That fresh evidence may validate, downgrade, rerank, or qualify a strict `CARRIER REOPEN — XI CONFIRMED`, post-XI EGE burden, carrier state, or other current assessment according to the active model, but it must not silently rewrite what PRE originally was.

For just-started/live Step-2 states, verdict-first changes ordering only: surface the first action, then run the mandatory targeted research attempt in the same assessment unless it was already completed for the current XI epoch.

Live evidence validates or invalidates history; it does not rewrite history.

---

## 13. PRE compiler authority

For all new Work boards, `FOOTBALL_PRE_DECISION_SPEC.md` replaces duplicated in-procedure route/tier/ranking matrices.

Mandatory consistency assertions before publication:

1. each team has an explicit route state from the compiler;
2. no supporting-only proxy creates SUPPORTED/PROVEN by itself;
3. every A2 two-route case has INDEPENDENT or CONDITIONAL weaker-route state;
4. SUPPORTED+SUPPORTED is Step-1 WATCHLIST maximum;
5. VERIFIED/CANDIDATE/UNVERIFIED carrier state is explicit;
6. every provisional PASS eligible for rescue received exactly one rescue screen;
7. HARD VETO cannot be averaged away;
8. LOW evidence/burden confidence cannot produce FOCUS;
9. PRE Structural Rank follows the compiled lexicographic order;
10. no price or confirmed-XI evidence contaminated PRE.

Use `AISCORE:<fixture_id>` as the preferred unique key. If no ID exists, use competition + normalized teams + kickoff_utc.

Before freezing or publishing, block conflicting duplicate identities:

`COVERAGE IDENTITY CONFLICT — PUBLICATION BLOCKED`

No unresolved duplicate may appear twice in a ranking pool or on two slate dates.

---

## 14. Frozen structural-rank output

Within every practical kickoff window, freeze the full candidate order only **after** all fixture compiler traces are complete.

For each surviving candidate record:

- Structural Rank;
- route pair;
- weaker-route independence state;
- practical-carrier state;
- chance-quality state;
- dominant failure mode + severity;
- supported burden/range + basis;
- evidence confidence;
- exact cross-grade inversion reason when applicable.

Do not create a price-derived HOLD during Work. At Step 2, a structurally qualified candidate with an unavailable/too-short target offer may become a qualified execution wait under the active Step-2 rules; a candidate with failed football gates becomes STRUCTURAL HOLD. Those later states must not rewrite frozen PRE.
