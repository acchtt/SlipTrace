# 00 — Normal Chat: AiScore Researchable Senior Intake

**Command alias:** `/sweep`

**Use in:** Normal Chat, high reasoning.

Read upstream `models/football/CURRENT_MODEL.md` first.

Football C is the active official model.

## Purpose

Build a trustworthy **OPERATIONALLY VIABLE, RESEARCHABLE SENIOR** AiScore universe for the requested window.

The objective is the middle ground between the old narrow allowlist and the later over-broad senior sweep:

- do not miss meaningful senior blocks such as international qualifiers;
- do not send obscure, weak-data competitions to Work when there is not enough current evidence to assess them responsibly.

Operational principle:

`SOURCE ACQUISITION (EXACT OR BOUNDED) -> SENIOR DISCOVERY -> HARD SCOPE FILTER -> OPERATIONAL VIABILITY GATE -> RESEARCHABILITY GATE -> CAPACITY GATE -> VERIFIED TIME/IDENTITY -> PACKAGE -> FOOTBALL C`

This intake is about **information quality and later executability**, not whether a competition is historically high-scoring.

Read and apply:
- `models/football/procedures/FOOTBALL_AISCORE_SOURCE_ACQUISITION.md`
- `models/football/procedures/FOOTBALL_SWEEP_CHECKPOINT_EXECUTION.md`
- `models/football/procedures/FOOTBALL_SWEEP_REPAIR_MODE.md` when the command is `/sweep repair ...`
- `models/football/procedures/FOOTBALL_OPERATIONAL_VIABILITY_GATE.md`
- `models/football/procedures/FOOTBALL_COMPETITION_RELIABILITY_MEMORY.md`
- `models/football/procedures/FOOTBALL_WOMENS_TOP_FLIGHT_COVERAGE.md`
- `models/football/procedures/FOOTBALL_REQUIRED_COMPETITION_COVERAGE.md`
- `models/football/procedures/FOOTBALL_CAPACITY_REPLENISHMENT.md`
- `models/football/airtable/FOOTBALL_COMPETITION_RELIABILITY_AIRTABLE.md`

The operational gate is mandatory for every surviving senior fixture before deep Work research.

## Default mode

`sweep_scope_mode=RESEARCHABLE_SENIOR_PRODUCTION`

If the command is `/sweep repair ...`:
- set `repair_mode=true`;
- do **not** execute the normal full discovery path for rows/blocks already complete in the target sweep;
- follow `FOOTBALL_SWEEP_REPAIR_MODE.md`;
- reuse the target run's source-acquisition state when still valid;
- build a finite repair set and stop when it is resolved/closed/unresolved;
- never keep browsing beyond the repair verification budget.

Do not use:
- legacy `NARROW_CORE` / PRIORITY-NORMAL-CONDITIONAL as the primary admission rule;
- unrestricted `BROAD_SENIOR_PRODUCTION`.

A prior sweep may be reused only if it was completed under RESEARCHABLE_SENIOR_PRODUCTION for a covering window.

## Checkpointed execution — mandatory

Fresh Step 0 is resumable.

For a new sweep:
- resolve the stable Run ID/window;
- **before any source/provider call or progress response**, create/update the Sweep Runs row;
- set `Run Status = RUNNING`;
- initialize `Checkpoint Version = football-sweep-checkpoint-v1`;
- initialize `Sweep Chunk Number = 1`;
- persist a valid `SOURCE_ACQUISITION / UNTRIED` Resume Cursor;
- only after that persistence succeeds may source acquisition begin.

If initialization persistence fails, return `SWEEP START FAILED — CHECKPOINT NOT PERSISTED` and do not acquire sources. A fresh sweep must never return "work remains" without a resumable RUNNING cursor.

For `/sweep resume`:
- load the matching resumable Sweep Run first;
- continue from its `Resume Cursor`;
- a BLOCKED run is resumable only for `SOURCE_ACQUISITION / SOURCE_BLOCKED`; apply the recovery-lease decision and restore RUNNING status when a retry is authorized.
- reuse completed Daily Coverage rows and block evidence;
- never restart an unchanged ACQUIRED source epoch;
- never create a replacement Run ID merely because the previous chat turn ended.

External targeted verification is limited to **6 competition/date blocks per invocation**. Use:

`python models/football/engine/sweep_checkpoint_cli.py select --input <checkpoint.json>`

when deterministic execution is available.

After each externally verified block, persist its result and advance the cursor. When six external blocks have been processed and work remains, stop cleanly with:

`SWEEP CHECKPOINT SAVED — /sweep resume`

This is a normal RUNNING checkpoint, not `BLOCKED`, and no provisional Work ZIP is emitted.

Cheap source-local enumeration, hard exclusions, already-supported C/D block classifications, and persisted-state reads do not consume the six-block external budget.

## Source authority

AiScore remains the preferred fixture-discovery authority, but normal FAST_PRODUCTION no longer depends on one exact master date page.

Apply `FOOTBALL_AISCORE_SOURCE_ACQUISITION.md`.

The source stage has two valid success modes:

1. `EXACT_DATE_UNIVERSE` — native AiScore or a reconciled complete date carrier;
2. `BOUNDED_PRODUCTION_DISCOVERY` — when exact carrier transport fails, freeze at least two independent current discovery source families and proceed with `coverage_mode=FALLBACK_PRODUCTION_SCOPE`.

For HTML carriers:
- try the literal date URL first;
- after a transport-local failure, one domain/date search may be used only as a locator;
- OPEN the located result;
- an opened full canonical page may be a carrier;
- the search snippet alone may not certify exact completeness.

**Critical FAST_PRODUCTION rule:** failure to obtain an exact date carrier is not itself SOURCE_BLOCKED. If search/provider/official discovery surfaces are still available, switch to bounded production discovery **in the same invocation**.

In bounded production discovery:
- search/index results may seed candidate competition/fixture discovery;
- `global_raw_exact=false`;
- do not fabricate a global raw count;
- every surfaced protected/required/women block and every plausible A/B senior candidate must later receive exact reconciliation/disposition;
- `production_scope_complete=true` is decided only at final reconciliation.

A true SOURCE_BLOCKED result is allowed only when neither an exact carrier nor the minimum two independent current discovery source families can be established.

When persisting a true source failure:
- `Run Status = BLOCKED`;
- `Source Acquisition State = SOURCE_BLOCKED`.

Never write `SOURCE_BLOCKED` into the Run Status single-select.

For `/sweep resume`, a true blocked source run uses the recovery lease. But an exact-carrier failure must not enter the recovery lease if bounded production discovery can still start.

## Time / identity integrity

Resolve the requested ICT/UTC window once and follow:

`models/football/procedures/FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`

Every admitted fixture must have:
- resolved AiScore/provider identity;
- authoritative zoned kickoff;
- verified UTC;
- verified ICT;
- in-window proof.

Do not guess timezone from geography or treat a bare display clock as UTC.

In repair mode, verify only fixtures with missing/conflicting time/identity or fixtures expanded from a previously block-deferred A/B block. Once a known fixture's identity and zoned kickoff are authoritatively resolved with no contradiction, stop searching for that fixture.

## 1. Mandatory senior-block discovery

This section runs after `source_acquisition_state=ACQUIRED` in either `EXACT_DATE_UNIVERSE` or `BOUNDED_PRODUCTION_DISCOVERY` mode, or after a valid covering COMPLETE source epoch has been reused.

Before applying hard scope exclusions, enumerate all visible senior competition blocks in the requested AiScore window.

Senior women's domestic top-flight leagues are a **mandatory discovery class**. Every visible fixture from the country's highest senior women's domestic league must enter the raw senior accounting before any later operational/researchability/capacity disposition.

Do not skip a block because its competition label contains Women / Women's / Ladies / Frauen / Féminine / Femenina / Dam / Kvinner or equivalent.

If a visible women's senior top-flight block has no recorded fixture/disposition:

`HANDOFF INCOMPLETE — WOMEN TOP-FLIGHT COVERAGE GAP`

## 2. Hard scope exclusions

Exclude before the researchability gate:

- youth/Uxx-only competitions;
- academy/junior competitions;
- reserve/B/development-only competitions, except reserve-branded teams participating in a normal professional senior league;
- amateur or clearly semi-professional micro competitions with unreliable identity/data;
- regional/state/provincial competitions outside the intended senior professional universe;
- school/university/military/company competitions;
- friendlies/exhibitions unless explicitly requested;
- cancelled/postponed/abandoned/already-finished fixtures for an upcoming sweep;
- unresolved fixture identity/home-away;
- unresolved authoritative kickoff;
- duplicates.

## 2B. Standing user exclusion — ALL noncompetitive friendlies (effective 2026-10-09)

**User directive:** "Skip friendlies, exclude from future sweeps as well." This is a **standing, unconditional normal-/sweep scope exclusion** for noncompetitive senior **national-team friendlies (men's/women's), club friendlies, exhibition/test/preseason matches**. Apply to the **current unfinished sweep and every subsequent /sweep** unless explicitly reversed by the user; neither an A/B historical over-rate, protected *nation*, popular club, nor available XI/odds can override this exclusion. Official **competitive** qualifiers, Nations League, tournament fixtures, international cups and women's domestic top flights are **not friendlies** and remain in their existing required/protected/accounting scope.

Apply friendly scope exclusion immediately after source-local competition classification, **before any fixture-specific kickoff disputes, XI availability or Asian bookmaker preflight**. Preserve already captured fixture rows and original source timestamps/grades for audit with `scope=EXCLUDED`, screen `EXCLUDED`, `reason=USER_SCOPE_EXCLUDED_FRIENDLY — 2026-10-09`; do not delete them or change the prior source-acquisition hash. For future new runs, close friendlies at **source block level** if only date/index evidence exists—do not spend search budget enumerating friendly fixtures. If source acquisition incidentally captures one, retain a compact exclusion record if needed for audit. Do not add them to A/B queue or any C/C2 Work payload.

For a resumed run with a pending **friendlies-only block**, remove that key from `pending_verification_blocks` and `retry_queue`, place it in `user_excluded_verification_blocks`, recompute counts, and persist the checkpoint. **Mark excluded by user scope, NOT externally verified/completed.** The final report separates friendly exclusions from other operational C/D and from the five pre-existing country exclusions. Explicit `/xi exception` for a **named fixture** may reopen only that one, without deleting or silently modifying the standing default rule. Do not classify an official qualifier as a friendly because a provider uses "international match" or "exhibition-like" colloquially.

## 2A. Standing user-scope domestic exclusions — effective 2026-10-09

The user explicitly directed Step 0 to **skip and exclude from subsequent sweeps** the following **domestic competition universes**, independently of the normal A/B/C/D operational gate:

- **Israel:** domestic leagues and domestic cups (including Liga Leumit).
- **Kenya:** domestic leagues and domestic cups (including Premier League).
- **Iraq:** domestic leagues and domestic cups (including Iraq Stars/Premier League).
- **Wales:** domestic leagues and domestic cups (including Cymru Premier).
- **Kuwait:** domestic leagues and domestic cups (including Kuwait Premier League).
- **Germany:** **3. Liga only**; Bundesliga, 2. Bundesliga, women's top flight, DFB-Pokal and other German competitions stay in ordinary scope.

These are explicit user **scope exclusions**, not C/D ratings, competition-reliability demotions, football predictions, or a basis for rewriting historical grades. They remain effective in new `/sweep` runs and existing `/sweep resume` runs until the user explicitly reverses them. Explicit user-directed **fixture exceptions** may reopen only the named fixture and must still pass normal integrity requirements.

Apply this filter **after source-local raw discovery/accounting, but before external block verification, operational research, queue construction or Work admission**. For newly discovered fixtures within these universes, record `USER_SCOPE_EXCLUDED — 2026-10-09` in the disposition/exclusion provenance (where a distinct Airtable select option is unavailable, use existing `EXCLUDED` plus explicit notes); do not seek unresolved kickoff/ID/XI/market information just to adjudicate an intentionally excluded fixture. Retain already persisted source records and fixture identities for audit, including earlier time conflicts or out-of-window notes, but never allow these rows into the global A/B capacity pool or into C/C2 Work payloads. The counts must distinguish user-scope exclusions from unresolved actionable rows.

For an existing cursor, remove matching **fully excluded** competition/date blocks from `pending_verification_blocks` and `retry_queue`, add them to a separate `user_excluded_verification_blocks` audit list, recompute pending counts, and persist a checkpoint before continuing. **Do not mark these blocks as externally verified/completed.** A generic block such as `GER_OTHER_SENIOR` may be removed only if its known in-scope rows are exclusively 3. Liga; otherwise keep/split the non-3. Liga remainder for screening. Continue terminal reconciliation of **the remaining in-scope** international, continental, protected, and domestic competition classes. These excluded domestic rows must not block final work readiness solely for unresolved source/time information.

This rule does **not** exclude senior national teams representing Israel, Kenya, Iraq, Wales, or Kuwait in protected official competitions; it also does not exclude cross-border continental club competitions or Germany's other senior divisions. Senior women's **domestic** top-flight fixtures within the five excluded countries still belong to raw source-visible coverage accounting where the launcher requires it; then receive explicit user-scope exclusion rather than silently disappearing.

## 3. Competition reliability memory — mandatory

After senior discovery/hard scope filtering and before final operational grading:

1. normalize a stable competition key;
2. read the matching row from Airtable `Competition Reliability` (`tbl1KShXxXErUdVKW`);
3. if no row exists, use `UNPROVEN`;
4. preserve any explicit Manual Override without inventing one;
5. calculate the raw current A/B/C/D grade from current evidence;
6. apply the deterministic historical cap from `FOOTBALL_COMPETITION_RELIABILITY_MEMORY.md`.

Historical state behavior:
- TRUSTED / NEUTRAL / UNPROVEN: no promotion and no cap;
- CAUTION: max B;
- DEMOTED: default C; allow at most one B-grade probation fixture from that competition in the sweep only when the raw current grade independently clears full A requirements.

Persist:
- `raw_operational_viability_grade`;
- `competition_reliability_state`;
- `competition_reliability_reason`;
- `competition_reliability_sample` when available;
- `competition_reliability_manual_override = NONE / <explicit override>`;
- `demoted_probation = true / false`;
- `operational_viability_grade` after the history cap.

Do not use FT score, goals, C/C2 result, betting result or P/L to set this state.

## 4. Operational viability gate — mandatory

For every fixture surviving hard scope/identity/time checks, persist:

- `operational_viability_grade = A / B / C / D`;
- `xi_expected = YES / UNCERTAIN / NO`;
- `market_observability = HIGH / MEDIUM / LOW / NONE`;
- `team_news_observability = HIGH / MEDIUM / LOW / NONE`;
- `operational_viability_reason`.

Apply the procedure exactly:

- A = normal executable candidate.
- B = conditional candidate; may be admitted after A but cannot be routine FOLLOW at board time.
- C = `LOW OPERATIONAL OBSERVABILITY — STEP0 EXCLUDED`.
- D = `NON-OPERATIONAL FIXTURE — STEP0 EXCLUDED`.

Do not upgrade a fixture because its score history looks attractive. Small-league status alone is not a rejection; missing XI/market/team-news observability is.

## 4A. Mandatory verified-XI / match-specific Asian-total queue gate — effective 2026-10-09

Follow `models/football/procedures/FOOTBALL_XI_MARKET_FIRST_INTAKE.md`. During an entire-day sweep, **do NOT require confirmed starting XI for the upcoming fixture**. Before `ELIGIBLE`/Work queue admission, require credible source-backed **lineup publication channels** covering both teams, a scheduled near-KO XI recheck, a current fixture-specific Asian total, team news, legitimate senior competition tier and canonical identity/time. `xi_expected=YES` has strong channels for both teams. `xi_expected=UNCERTAIN` is allowed for **conditional B only** when at least one proven XI publication channel exists and the other side has dependable squad/provider news; B remains RESERVE maximum until /xi verifies the actual lineup. Teams/leagues lacking any demonstrable XI publishing ecosystem are excluded after a cheap bounded check. Preserve all protected/required/women fixture-level raw coverage. Never use historical goals alone for admission.

For the **currently user-paused** `SWEEP-20261009-1300-20261010-0300`, **do not resume or edit its Airtable records now**. When the user explicitly resumes this *still-unfinished* sweep, preserve its existing source hash, progress and legacy **15 initial / 10 replenishment capacity policy**, but perform this strict proof gate **prospectively before freezing its first Work queue**; write `strict_intake_policy=XI_MARKET_FIRST_V1` into the final handoff so the machine validator enforces it. A/B raw/provisional grades and earlier source accounting are historical evidence, not proof of Work eligibility. Do not reclassify previously frozen/COMPLETE boards.

For repeatable execution, serialize the bounded preflight candidate records into `<step0_xi_market_preflight.json>` with `{"candidates":[...]}`, then run `python models/football/engine/sweep_intake_evidence_cli.py --input <step0_xi_market_preflight.json>`. Its `ready_candidates` are the **only input** allowed into the subsequent operational A/B queue; `excluded` and `pending` remain in the existing raw coverage/disposition manifest. Persist both teams' lineup **channel** types/source URLs, the XI-availability basis, a kickoff-relative XI recheck time, optional prior confirmed XI IDs/dates **only when available**, the current Asian total line/bookmaker/time and competition-support source in structured fixture notes so /resume does not guess. Never infer proof from a generic site index or the historical league-over watchlist.

The current Oct-09 sweep, when explicitly resumed, must apply this exact preflight **prospectively** before its still-unfrozen Work queue, and serialize `strict_intake_policy=XI_MARKET_FIRST_V1` in `STEP0_HANDOFF.json`; leave the legacy capacity size unchanged. The saved source hash/coverage/previous audits must not be reset.

The raw discovery ledger, required/protected official and women's top-flight exact manifests remain comprehensive; only the **routine Work candidate view** becomes strict. Show `raw_discovered` separately from `verified_queue`; no giant undifferentiated list of obscure discovered fixtures as routine matches. Do not invent lineup source proof or bet-market quotes.

## 5. Protected senior competition classes

The following classes bypass the ordinary domestic researchability exclusion when identity/time are valid, but they still require an explicit operational viability grade:

- FIFA senior World Cup qualifiers/finals;
- senior continental national-team qualifiers/finals (AFCON, EURO, Asian Cup, Copa America/CONMEBOL, Gold Cup/CONCACAF, OFC equivalents);
- senior Nations League-style official national-team competitions;
- major senior continental club competitions administered by UEFA/AFC/CAF/CONMEBOL/CONCACAF/OFC;
- other clearly major senior international tournament blocks explicitly requested by the user.

These are protected because the previous narrow sweep missed meaningful national-team blocks.

They still receive normal Football C PASS/WATCH/FOCUS screening later.

## 6. Researchability gate — ordinary domestic / small competition blocks

For all other senior domestic league/cup fixtures, including men's and women's senior domestic top flights, run a **cheap researchability check** before admitting them to Work.

For senior women's top-flight fixtures, apply the same evidence standard as men's senior top-flight fixtures. Do not reinterpret "small/unfamiliar" as a gender proxy.

A fixture is `RESEARCHABLE` only when a quick preflight can establish enough current evidence for both teams to support the Football C evidence schema.

Minimum required evidence:

### Required A — recent team evidence
For **both teams**, at least one reliable source exposes a usable recent-match sequence/current form with opponents and scores.

### Required B — competition/context evidence
At least one reliable source exposes meaningful current competition context such as standings, phase/table, recent competition results, or equivalent tournament state.

### Required C — mechanism evidence
At least one of the following must be available without deep/manual hunting:

- team-level goal/chance profile;
- shots/SOT/box/chance-quality/xG-type statistics;
- reliable match/team statistical profiles;
- credible current team news/lineup/absence information that can materially inform routes;
- another repeatable quantitative or qualitative source sufficient to assess scoring mechanisms rather than only final scores.

### Required D — matchup/H2H availability
H2H is preferred when usable, but absence of H2H alone does **not** exclude a fixture.

However, if H2H is absent **and** mechanism evidence is weak, exclude.

### Admission rule

Admit when:
- Required A = PASS;
- Required B = PASS;
- Required C = PASS;
- fixture identity/time = PASS.

Otherwise exclude as:

`INSUFFICIENT RESEARCHABILITY — STEP0 EXCLUDED`

Do not spend deep Work research trying to rescue a competition that fails this cheap preflight.

## 7. What researchability is NOT

Do not exclude a fixture merely because:

- it is a senior women's domestic top-flight fixture;
- it is expected to be low scoring;
- its league was historically LOW-GOAL;
- it is from Japan or Finland;
- it is a professional lower division;
- it is a women's senior competition;
- it is unfamiliar;
- it is a cup.

If adequate current evidence exists, admit it and let Football C decide football quality.

Likewise, do not admit an obscure league merely because it is senior/professional if usable evidence is absent.

## 8. Efficiency rule

The researchability check must stay cheap and **competition-block shared**.

Normal limit per unfamiliar competition/date block:
- one acquired/provider competition/fixture surface;
- up to two quick public-web searches for current team/competition evidence.

Acquire those evidence surfaces once for the block and reuse them for every fixture/team they actually cover. Do not repeat the same standings/form/news/market search separately for each fixture in one league/date block.

Open a team- or fixture-specific source only when the shared block evidence does not cover that fixture's required A/B/C evidence.

The fixture-level admission standard is unchanged; only duplicate evidence acquisition is removed.

If those checks cannot establish A+B+C, exclude.

Do not turn Step 0 into the full Step-1 research process.

Under `FOOTBALL_SWEEP_CHECKPOINT_EXECUTION.md`, at most six blocks requiring external verification may be researched in one invocation. Batch independent web queries in the same tool call where supported.


### Block timestamp collision sentinel — mandatory

Before `work_ready=true`, inspect admitted fixtures within each competition/date block for suspicious timestamp reuse.

Trigger a hard revalidation when either condition holds:
- 3 or more distinct fixtures in the same competition/date have the exact same verified UTC kickoff; or
- a two-legged/repeat pairing within 14 days receives the same UTC kickoff as the previous leg without a current canonical match-page proof.

When triggered:
1. do not trust the batch timestamp;
2. reopen the current AiScore canonical match page for every affected admitted fixture;
3. verify current match ID, date, home/away and Match Info UTC/API epoch individually;
4. rebuild the affected kickoff fields before packaging;
5. label any mismatch `SOURCE TIME / BLOCK PARSER FAULT`.

A uniform competition-block timestamp is never sufficient proof by itself.

### New-run compact Work budget (effective 2026-10-09 ICT)

Apply `models/football/procedures/FOOTBALL_COMPACT_SWEEP_WORK_BUDGET.md` for **fresh sweeps only**. Freeze the complete operational A/B queue as before; set `sweep_work_budget_policy=COMPACT_GOAL_ROUTE_V1` in the run cursor/handoff and initial Work admissions to **ranks 1–8**, deferring ranks 9+ with immutable capacity ranks. Use `python models/football/engine/capacity_initial_wave_cli.py --input <capacity_queue_input.json>` to generate this first-wave selection, with `budget_policy=COMPACT_GOAL_ROUTE_V1` and `candidates=[...]` in that JSON. The selected ranks and deferred ranks must agree with final Step0 handoff and are validated by `step0_handoff_cli.py`. Routine unique fixtures researched under /rank <=12 with target refill-to-4 rather than automatic refill-to-10. Existing RUNNING/frozen runs without the policy remain on the legacy 15/10 contract; do not retrofit `SWEEP-20261009-1300-20261010-0300` or its ledger. The goal-route historical pilot **disproves** a naive six-match Over 2.5 veto: never use league-wide Over percentages or recent FT results to cut source coverage, assign an A/B grade, or reorder the operational queue. Tighten B market evidence only through independently current match-specific Asian total market observability; vague historic bookmaker/O2.5 aggregates do not prove executable Asian-total access.

## 9. Operational capacity gate

After A/B viability and researchability are known, build the **complete fixture-level A/B capacity queue first**.

For legacy/frozen handoffs without `COMPACT_GOAL_ROUTE_V1`, the 15-fixture limit is an **initial Work batch cap**, not a terminal slate exclusion. For new compact handoffs, the initial Work cap is **8**, with at most **12** uniquely researched fixtures under the bounded routine policy.

### Global capacity queue

Every plausible A/B fixture must receive a deterministic `Step0 Capacity Queue Rank` before the first 15 are chosen.

Order by operational quality only:
1. A before B;
2. stronger XI expectation;
3. stronger market observability;
4. stronger team-news observability;
5. protected/required/major senior competition class only as an otherwise-equal operational tie-break;
6. canonical match identity as the final deterministic tie-break.

Kickoff discovery order, source-page order and block arrival order must never decide admission.

Never use Over profile, expected goals, C/C2/C3/C4 state, supported line, attractive odds or outcome knowledge to build the queue.

Initial Work handoff:
- legacy handoffs: ranks 1–15 -> `ADMITTED_TO_C`, ranks 16+ deferred;
- new `COMPACT_GOAL_ROUTE_V1` handoffs: ranks 1–8 -> `ADMITTED_TO_C`, ranks 9+ deferred;
- all deferred A/B fixtures remain in the full operational queue with immutable ranks for audit and controlled replenishment.

Persist queue rank for both admitted and deferred A/B fixtures.

### Fallback capacity short circuit

In `coverage_mode=FALLBACK_PRODUCTION_SCOPE`, block-level short-circuiting is allowed only for blocks that are already demonstrably **below the A/B candidate threshold**.

Do **not** short-circuit a block merely because 15 slots are already occupied.

Any block that could plausibly contain an A/B fixture must still be enumerated fixture-by-fixture and inserted into the global capacity queue. Protected competition blocks, required competition blocks and women's top-flight blocks remain fixture-exact regardless.

This prevents early blocks from permanently taking the 15 slots before later equal/stronger fixtures are seen.

Overflow remains recorded as:

`OPERATIONAL CAPACITY DEFERRED — STEP0`

but it is now a normal deterministic replenishment pool under Step 1 and does not require a user exception to reopen.

## 9A. Required competition-block manifest — mandatory

Independently of broad discovery, run `FOOTBALL_REQUIRED_COMPETITION_COVERAGE.md`.

Current protected block registry version:
`required-competition-manifest-v1`

At minimum, explicitly check:
- `NED_EERSTE_DIVISIE` — Netherlands Eerste Divisie / Keuken Kampioen Divisie.

Record exactly one:
- `CHECKED_WITH_FIXTURES`
- `CHECKED_NO_IN_WINDOW_FIXTURES`
- `SOURCE_BLOCKED`

If fixtures exist, enumerate every official in-window fixture before normal disposition rules.

Official Jong/U21/reserve-branded participants in the Eerste Divisie are senior league fixtures for coverage purposes and must not be dropped by generic reserve/youth-name exclusions.

If the block is absent/unresolved:

`HANDOFF INCOMPLETE — NETHERLANDS EERSTE DIVISIE COVERAGE GAP`

Do not set `work_ready=true`.

Run `validate_required_competition_manifest` from `models/football/engine/coverage_manifest.py` against the packaged manifest when execution is available.

## 10. Completeness

### Native/complete-date mode

When the native AiScore date universe or an equivalently complete fixture-level date payload is available, production completeness means:

> every potentially relevant senior block in the requested window was discovered, then hard-excluded, operationally excluded, researchability-excluded, capacity-deferred, or admitted.

### Multi-source fallback production-scope mode

When `source_transport = MULTISOURCE_FALLBACK_DATE_UNIVERSE`, `MULTISOURCE_FALLBACK_PRIMARY_DATE_PLUS_TERMINAL_INTERVAL` (or legacy `MULTISOURCE_FALLBACK_LIVESCORE_FLASHSCORE_SOCCERWAY`), do **not** force fixture-level enumeration of the entire all-level date page merely to produce a cosmetic global raw count.

Set:
- `coverage_mode=FALLBACK_PRODUCTION_SCOPE`;
- `global_raw_exact=false`;
- `production_scope_complete=true` only when all requirements below pass.

Fallback production-scope completeness requires fixture-level exactness for:
1. every protected senior competition block;
2. every required-competition manifest block;
3. every senior women's domestic top-flight fixture carried by the authorized fallback universe;
4. every fixture that survives hard-scope prefiltering and could plausibly receive operational grade A/B;
5. every admitted or capacity-deferred fixture.

Obvious youth/Uxx, academy, reserve-only, regional/state, university/school/company, amateur/micro, and clearly non-operational competition blocks may be summarized at **block level** with a hard/operational exclusion reason. They do not need one row per fixture in fallback mode.

This exception changes audit granularity only. It must not:
- hide a plausible A/B senior fixture;
- weaken protected/required/women coverage;
- permit a C/D fixture into Work;
- use predictive attractiveness to decide what is enumerated.

In fallback mode, `raw_senior_count` may be null/UNAVAILABLE rather than fabricated. Persist instead:
- `production_universe_count` = exact fixture count after block-level hard-scope prefiltering that required fixture-level disposition;
- `block_excluded_summary` = excluded competition blocks/categories with compact reasons.

`work_ready=true` is permitted with `global_raw_exact=false` only when `production_scope_complete=true`, required competition coverage is exact, women's top-flight coverage is exact, and every plausible A/B senior candidate has a fixture-level disposition.

Additionally:
- every visible senior women's domestic top-flight block must reconcile under `FOOTBALL_WOMENS_TOP_FLIGHT_COVERAGE.md`;
- every protected required competition block must reconcile under `FOOTBALL_REQUIRED_COMPETITION_COVERAGE.md`.

Missing either class is a coverage failure even when the overall raw/admitted totals otherwise balance.

A skipped visible senior block with no recorded disposition makes the handoff incomplete.

For cross-midnight/early-morning windows, perform the normal terminal-interval recheck.

## 11. Persistence / counts

Checkpoint persistence is part of normal execution, not only final packaging.

For every RUNNING sweep keep current:
- `Checkpoint Version`;
- `Sweep Chunk Number`;
- `Resume Cursor`;
- `Retry Queue`;
- `Pending Verification Blocks`;
- `Last Completed Block`;
- `Checkpoint Notes`;
- `Updated At`.

After each external block, persist completed fixture rows/dispositions before moving to the next block. A timeout after a successful checkpoint must not force already-completed blocks to be re-researched.

At the start of each resume chunk, close already-started/finished pending fixtures before spending external research budget on them.

For every discovered in-window senior fixture preserve one disposition:

- `ADMITTED_TO_C`
- `HARD_EXCLUDED`
- `OPERATIONAL_EXCLUDED`
- `RESEARCHABILITY_EXCLUDED`
- `OPERATIONAL_CAPACITY_DEFERRED`
- `UNRESOLVED`

Record researchability reason compactly.

Required funnel counts:

`RAW SENIOR -> HARD EXCLUDED -> OPERATIONAL EXCLUDED -> RESEARCHABILITY EXCLUDED -> CAPACITY DEFERRED -> ADMITTED TO C`

Required women's-top-flight counts:
- `women_top_flight_raw_count`;
- `women_top_flight_admitted_count`;
- `women_top_flight_operational_excluded_count`;
- `women_top_flight_researchability_excluded_count`;
- `women_top_flight_capacity_deferred_count`;
- `women_top_flight_unresolved_count`.

The women's-top-flight raw count must equal the sum of its dispositions.

Persist `women_top_flight_disposition_manifest` with every fixture in the class, including excluded/deferred fixtures. This manifest is audit metadata and does not add non-admitted fixtures to the Work array.

## 12. Work-readiness gate

Package only when:

- `complete=true`
- `actionable_complete=true`
- `work_ready=true`
- every visible senior block has a disposition;
- every admitted fixture is operational grade A or B;
- every admitted fixture has a competition reliability snapshot;
- every A/B capacity-queue fixture, whether `ADMITTED_TO_C` or `OPERATIONAL_CAPACITY_DEFERRED`, carries non-empty `xi_expected`, `market_observability`, `team_news_observability`, `operational_viability_reason`, `competition_reliability_state`, and `competition_reliability_reason`;
- no CAUTION fixture is admitted above B;
- no DEMOTED fixture is admitted except the allowed B-grade probation rule;
- admitted fixture count is <= 15;
- protected senior blocks were not removed by the researchability gate without an explicit operational disposition;
- every visible senior women's domestic top-flight block has a fixture-level disposition;
- `required_competition_manifest_version = required-competition-manifest-v1`;
- every protected required competition block is explicitly present and resolved;
- `Required Competition Blocks Complete = true`;
- women's-top-flight counts reconcile exactly;
- `women_top_flight_unresolved_count = 0` before `work_ready=true`;
- every admitted fixture has resolved identity/time;
- terminal scan is complete where required;
- admitted count equals handoff array count.

If any A/B queue fixture is missing the six-field Step-0 operational/reliability contract:

`HANDOFF INCOMPLETE — STEP0 OPERATIONAL CONTRACT MISSING`

Do not infer the missing semantic fields from competition reputation, operational grade, fixture name, or later Step-1 research.

For other completeness failures:

`HANDOFF INCOMPLETE — RESEARCHABLE SENIOR COVERAGE GAP`

## 13. Canonical ZIP handoff

Create two root-level canonical files inside the ZIP:
- `AISCORE_FIXTURES_*.txt` — human-readable handoff;
- `STEP0_HANDOFF.json` — machine-readable authority with `handoff_version=football-step0-handoff-v2`.

The JSON must contain `admitted_fixtures` and the complete `capacity_queue`. Every admitted/deferred A/B row must have a stable non-empty `match_id`; fixture names are never a substitute for IDs.

Required metadata:

- `model=Football C`
- `sweep_scope_mode=RESEARCHABLE_SENIOR_PRODUCTION`
- `source_scope = EXACT_DATE_UNIVERSE / BOUNDED_PRODUCTION_DISCOVERY`
- `source_transport`
- `coverage_mode`
- `production_scope_complete`
- `discovery_seed_manifest` when `source_scope=BOUNDED_PRODUCTION_DISCOVERY`; supported serializations are either `{\"sources\":[...]}` or a direct `[...]` source-entry array; every source entry must carry `family` (or legacy alias `source_family`)
- requested ICT/UTC window;
- listing dates checked;
- terminal scan state;
- `complete=true`;
- `actionable_complete=true`;
- `work_ready=true`;
- `raw_senior_count` when `global_raw_exact=true`, otherwise `global_raw_exact=false` + exact `production_universe_count` + `block_excluded_summary`;
- for `BOUNDED_PRODUCTION_DISCOVERY`: `source_transport=MULTISOURCE_BOUNDED_PRODUCTION_DISCOVERY`, `coverage_mode=FALLBACK_PRODUCTION_SCOPE`, `production_scope_complete=true`, and a frozen discovery seed manifest containing at least two independent source families; the wrapper-object and direct-array manifest encodings are semantically equivalent and must validate identically;
- before final packaging, mirror bounded provenance into Sweep Runs dedicated fields: `Source Scope = BOUNDED_PRODUCTION_DISCOVERY`, `Production Scope Complete = true`, and full `Discovery Seed Manifest`; preserve the same manifest in the final COMPLETE Resume Cursor instead of dropping it during phase transition;
- `hard_excluded_count` when fixture-exact, otherwise block-level exclusion summary;
- `operational_excluded_count`;
- `researchability_excluded_count`;
- `capacity_deferred_count`;
- `admitted_to_c_count`;
- protected-block audit result;
- women's-top-flight coverage audit result;
- all six women's-top-flight counters;
- `women_top_flight_disposition_manifest` listing every discovered women's top-flight fixture and disposition;
- admitted fixtures with identity/time provenance;
- complete deterministic A/B capacity queue for replenishment, including both admitted and capacity-deferred rows with unique `Step0 Capacity Queue Rank`;
- per admitted **and capacity-deferred A/B queue fixture**: raw operational grade, final operational grade, XI expectation, market observability, team-news observability, competition reliability state/sample/reason and operational reason.

Do not include hard-excluded, operationally excluded, or researchability-excluded fixtures in the Work array. Capacity-deferred fixtures remain outside the initial Work array but must stay in the packaged replenishment queue with the complete Step-0 contract.

### Mandatory export validation

Before creating the ZIP or saying `Sweep complete`, serialize `STEP0_HANDOFF.json` and run:

`python models/football/engine/step0_handoff_cli.py --input STEP0_HANDOFF.json --consumer export`

Required result: `step0_handoff_validation_status = PASS` and `consumer = export`. New Step-0 exports remain strict: a bounded-production handoff must include its discovery seed manifest and block-exclusion summary.

If the validator fails, the sweep is not complete. Repair the export in Step 0 and rerun validation. Never emit a completed ZIP whose machine handoff fails. Never defer this repair to /rank.

## 14. Step-0 boundary

Step 0 may determine whether enough evidence exists.

It must **not** decide:

- route strength;
- carrier strength;
- chance quality;
- supported burden;
- C-PASS/WATCH/FOCUS;
- rank;
- BET/WAIT/PASS.

Those remain Football C/C2 Step-1/Step-2 decisions.

## Output

If the bounded chunk ends while external verification remains, return:

`SWEEP CHECKPOINT SAVED — /sweep resume`

with:
- Run ID;
- completed chunk number;
- current phase;
- blocks completed this chunk;
- pending verification block count;
- retry queue count;
- next block key;
- current counts when available;
- source acquisition state/transport.

Do not emit a ZIP in this state.

Only after final reconciliation + machine-handoff validation + packaging pass, return:

`RESEARCHABLE SENIOR HANDOFF COMPLETE`

with:

- requested window;
- raw senior count when exact; otherwise `global_raw_exact=false` and exact production-universe count;
- women's top-flight raw / admitted / operational excluded / researchability excluded / capacity deferred / unresolved counts;
- hard excluded;
- operationally excluded;
- researchability excluded;
- capacity deferred;
- admitted to Football C;
- unresolved = 0;
- ZIP filename.
