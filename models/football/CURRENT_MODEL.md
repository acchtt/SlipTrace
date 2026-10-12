# Current Football Model

## Prospective V4 goals-first intake — same standard for every league

**Routine league registration does not qualify an Over match.** All
source-visible genuine future competitive matches enter the source
ledger; their goals evidence gets a uniform quantified screen, independent
of league familiarity. C/C2 rank-eligible `eligible_queue` now contains
only source-backed `GOAL_PRIORITY` matches. Missing competitive results,
weak route, or draw-trap matches remain auditable and researchable in
`goal_research_queue` instead of automatically being ranked or labelled
model PASS. Use `GOAL_SIGNAL_FIRST_V1` to put scored goal potential ahead
of KO urgency. No compulsory XI/odds history for initial goals research,
no arbitrary 8 cap, no retrospective prematch. Historical Oct12 receipt
replay remains unchanged. Reference `stages_v4/goals_first_intake.py`.

## V4 open-league goal discovery — source-first (2026-10-12)

**No registry-only hard exclusion for otherwise eligible official domestic
competitions.** First obtain all source-visible, window-specific senior
competitive fixtures, then retain nonregistered leagues/official cups as
`DISCOVERY`. Only source-backed scoring form for both teams and real
current researchability/format evidence can promote a discovery match
into the C/C2 football research queue. Missing proof/low signal remains
`PENDING_DISCOVERY` in the ledger/watchlist rather than disappearing or
being labelled model PASS. Preserve explicit country/league bans,
friendlies, immutable fixture IDs and clock gates. See
`models/football/stages_v4/discovery_goal_gate.py` and V4 SOP.
Historical sealed receipts retain their original admission status.

## Current replacement — V4 /sweep and /rank (approved 2026-10-11)

**ACTIVE NEW STAGES:** `models/football/stages_v4/SWEEP.md`
and `models/football/stages_v4/RANK.md`, implemented in
`models/football/stages_v4/stage.py` and the explicitly researched
country+league registry `league_registry.py`. User approved a NEW
workflow after retiring V1–V3. V4 does **not** reactivate the old CLIs
or previous source epochs. Existing old Step0/Step1 executables stay
`SWEEP_RANK_RETIRED` for legacy use.

V4 /sweep obtains a genuinely current single window-scoped source
snapshot, freezes all canonical fixture IDs and kickoffs, includes the
researched league tiers (Big Five, Netherlands/Eerste, Norway OBOS,
Sweden, Denmark, Poland, Czech, Malaysia, Hong Kong, UAE, Qatar,
Saudi, Thailand, Indonesia, Japan and approved lower leagues),
and includes verified women's senior top flights. Excluded domestic
leagues and friendlies remain excluded. No worldwide completeness
precondition, unsupported discovery tokens or arbitrary 8-match cap.

V4 /rank uses the frozen V4 receipt, source-backed actual goal-route
research (including dynamic high-scoring team routes and draw-trap
penalty), calls the real independent C and C2 model engines together,
and requires actual Airtable persistence/readback before publication.
Odds are not needed for football-only ranking; executable bets still
require genuine current prices in /xi. No made-up XI, lines, ranked
records or retroactive prematch decisions. The existing /xi,
`/live`, `/audit`, `/report`, user-verified Actual Bets and archived
financial ledger remain unchanged.

## Historical status — retired V1/V2/V3 only (2026-10-11)

**The user scrapped both current Step0 /sweep and Step1 /rank.**
Production stage status: `SWEEP_RANK_RETIRED`; any V1/V2/V3 source,
checkpoint, package, paired board or official rank publishing instruction
below is historical only and MUST NOT run again.
Do not start a new Sweep Runs record, reopen a terminal checkpoint,
create an official ZIP or publish new Website Picks from old boards.
No hidden automatic /sweep or /rank should continue.
The historical pure validators/engines remain in GitHub for audit and
future redesign; they do NOT authorize official operational output.
A replacement needs a new explicit user instruction and reviewed
re-enablement. **/xi, /xi exception, /live, /audit and /report remain
unchanged.** The active official model is C and C2 is shadow only.
Do not delete or backfill historical coverage, boards, decisions or
Actual Bets.

## Unified /sweep and /rank V3

The current Step0-to-Step1 coordinator is
`models/football/engine/sweep_rank_pipeline.py`. Follow
`models/football/procedures/FOOTBALL_SWEEP_RANK_UNIFIED_V3.md`.
A source-backed preview starts football research before complete global
reconciliation, but cannot publish an official board. A final validated
ZIP and independent C/C2 engine execution plus fresh Airtable readback
are required. No separate Work-chat transfer is mandatory.
Retain the V2 15-minute discovery budget, full required/women coverage,
C official/C2 shadow only, and one-command quote-free /xi.

## One-command /xi — user-facing authority

**/xi works as one assessment, just as before.** Read
`models/football/procedures/FOOTBALL_SIMPLE_ASSESS_AND_BET.md`.
Assess both C (official) and C2 (shadow) without asking for odds. If
a genuinely current total and price are already provided, check them
automatically as part of the same /xi response. The user does not
need to request /bet separately. If a price is unavailable, still
complete the football analysis and say `No bet price checked`.
This supersedes older contradictory quote-first/opt-in price-check
instructions for user-facing /xi. Never invent a price or authorize
an executable bet without valid current evidence.

## Airtable operational base routing (2026-10-11)

**Current LIVE base for new /sweep, /rank, /xi, /live, model decisions, website picks and official Actual Bets:** `appbzxqXYf0lKfD4P` (Football v2 — Active Operations 2026-10-11). **Previous base `appWyZJjitSBATXAU` is read-only historical ARCHIVE** (4,539 original records, untouched, over Free tier per-base cap). Never append to the archived base. All 10 live tables have fresh table and field IDs; before any Airtable read/write consult `models/football/airtable/ACTIVE_BASE_ROUTING_20261011.md` for the full 368-field migration map. Current base includes two physical Actual Bets with live Profit and ROI formulas, 7 Circuit Breakers, 28 Manual Scores, 72 recent Decision States, and new sweep 2026-10-11 08:58–12:00 ICT. Historical sweeps and remaining decisions should be sourced from archive, never assumed copied to current. Do not silently delete archive rows.

> **ACTIVE ROSTER (2026-10-06):** Football C is official; Football C2 is the only shadow challenger. C3 and C4 are retired from new/current execution. Historical C3/C4 records remain immutable audit history.

**Active official model:** Football **C**  
**Only active shadow challenger:** Football **C2**  
**Fixture authority:** AiScore primary, with the documented bounded source fallback  
**Operational timezone:** Asia/Ho_Chi_Minh (ICT, UTC+7)

This file is the canonical entry point for current football work.

**Standing /sweep scope exclusions (2026-10-09):** In addition to Israel, Kenya, Iraq, Wales and Kuwait **domestic football** and Germany **3. Liga only**, exclude **ALL noncompetitive friendlies** (senior international women/men, club, exhibition, preseason) from both the current unfinished sweep and all future ordinary sweeps. Such rows already acquired must be preserved only for exclusion audit, not Work. Competition-block prefilter avoids wasting lineup/odds research on friendlies. This does not remove **official competitive international qualification, Nations League, cup/continental fixtures or women's top-flight domestic matches**. A named explicit user exception is the only re-opening route. See `prompts/00_NORMAL_CHAT_AISCORE_FETCH.md` §2B.

## Fast Step0 time-budget authority — October 11, 2026

**NEW production /sweep runs use `FAST_FINISH_V2`: at most 15 minutes
of bounded discovery/verification work from the originally persisted
start (3 minutes source acquisition, 5 discovery classification, 12
verification, 15 final reconciliation/package).** Check deterministic
`sweep_checkpoint_cli.py deadline --input RESUME_CURSOR.json --now <verified UTC>`
before external calls, after each parallel verification batch, on every
resume and before final state writes. The V2 `select` and `advance`
CLI require `--now` and reject over-budget calls. Only eight logical
verification blocks are selected per batch; one failed attempt closes
a source path as explicitly unresolved. Source family/league-season
evidence is reused when independently valid for this exact source epoch.

**V2 bounded-scope correctness (2026-10-11 repair):** V2 is an
accepted official Step0 handoff/export policy, with all the same required
competition and Airtable admission readback obligations as V1. Where the
source epoch is explicitly `BOUNDED_PRODUCTION_DISCOVERY`, certify and
reconcile every **source-observed** senior women's top-flight fixture
using two independent opened women's-source window checks and the
fixture-level manifest; never falsely demand a worldwide exact AiScore
count, and never claim `global_raw_exact=true`. A source-visible
missing women's match, unresolved senior A/B fixture, unverifiable
source identity/KO, missing mandatory protected/required block or
unsupported source inventory still blocks the ZIP. See
`FOOTBALL_AISCORE_SOURCE_ACQUISITION.md` and
`bounded_womens_coverage.py`.

When the budget or a required provider blocks certification, persist
**BLOCKED** immediately with exact terminal source/protected/women/
canonical-inventory problems; retain all evidence and do not fabricate
a valid ZIP, rank, odds, XI or bet. A 15-minute cap limits work, not
requirements for source/competition/women integrity; no full-source
claim from a partial discovery seed. The tool cannot automatically
alter Airtable outside a real running invocation.

**All previously saved `FAST_FINISH_V1` source epochs retain their original
60-minute deadline, two-attempt semantics and original hash/queue**;
do not reinterpret or silently shorten the 21:07 existing run. Truly
old non-fast runs preserve their legacy six-block selector. Historical
completed boards, model results, and Actual Bets stay immutable. See
`FOOTBALL_SWEEP_CHECKPOINT_EXECUTION.md`.

## Hong Kong and Malaysia senior top-flight intake pilot — 2026-10-11

New source-verified source-local CONDITIONAL Step0 pilots: Hong Kong senior Premier League and Malaysia Liga Super. Country/competition matched; no automatic Work admission, Tier1 designation or fixed-club scoring preference. Fresh PROVEN_LEAGUE evidence >=2 historic senior games with both XIs and >=2 games with published Asian total menus. Per-fixture `asia_topflight_recent_goal_evidence` includes 3–5 actual pre-KO completed competitive scores per team and genuine sources, reject 0–0/1–1/low-total stalls. Real fixture/time, operational A/B viability, later current match-specific bookmaker and XI/news research still mandatory. All source hashes, historical boards, official C and shadow C2 and previous country/friendly exclusions unchanged. See `research/HONG_KONG_MALAYSIA_SOURCE_PILOT_2026-10-11.md`.

## Poland Ekstraklasa conditional source-local intake — 2026-10-11

For NEW prospective /sweep only, Polish **Ekstraklasa** stays conditional but is included in one source-local competition-block scan, analogous to the England Championship exception. Require per-fixture `poland_ekstraklasa_recent_goal_evidence` with five verifiable pre-KO completed competitive scorelines per team, sourced ID and time, <=7-day-fresh evidence capture, qualified recent goal routes and rejects for repeated 0–0/1–1 or <=2-goal stalls. Only Poland+Ekstraklasa qualifies. All PROVEN_LEAGUE (two actual historical fixture XI + two Asian-total publishing examples), current operational A/B/market/team-news/identity gates still apply. No team-name bonus, no automatic league admission, no implied future book quote. Poland I Liga and all standing exclusions stay unchanged. Original Step0 source hashes, queue ranks, decisions and Airtable immutable. C official, C2 shadow. See `models/football/procedures/FOOTBALL_LEAGUE_ENVIRONMENT_REGISTRY.md`.

## Norway OBOS-ligaen intake pilot — 2026-10-11

For new /sweep source epochs only, Norway **OBOS-ligaen / 1. divisjon** joins approved NORMAL **competition-level operational screening**. It is NOT a Tier 1 automatic channel, not a C/C2 goals boost and not unconditional Work admission. Require actual season-matched `PROVEN_LEAGUE` (two real completed fixture XI publications and two match-specific Asian total publication examples), independently verified evidence checked date/URL, real upcoming fixture identity/UTC kickoff, source-supported league news/market observability and A/B operational grade. Step 1 still requires actual **match-specific** bookmaker total, XI/news and C/C2 independent research; Step 2 still needs real current odds. No changes to Norway Eliteserien, Sweden, German 3. Liga ban, excluded countries, friendlies, protected/women's fixture coverage, old ranked/frozen boards or Airtable records. See `models/football/research/OBOS_LEAGUE_CHANNEL_PROOF_2026-10-11.md`.

## Lower-division intake adjustment — prospective from 2026-10-11

For new /sweep source epochs, **Germany 2. Bundesliga** is an explicitly approved NORMAL professional second-division research league (mandatory `PROVEN_LEAGUE` channel evidence; not Tier1), and **England Championship** is a specially sourced conditional **team-/fixture-level cheap-goal-signal pilot** (mandatory `PROVEN_LEAGUE` and five source-backed pre-kickoff competitive results per side, low-total stall screening). They are *not* default official Over bets. See `FOOTBALL_LEAGUE_ENVIRONMENT_REGISTRY.md`, `FOOTBALL_LEAGUE_CHANNEL_FIRST_INTAKE.md` and the 2026-10-11 research proof manifest. Spain Segunda División, Italy Serie B and France Ligue 2 remain outside routine proactive intake until rechecked and specifically authorized; Germany 3. Liga, user country exclusions, noncompetitive friendlies and retired models remain unchanged. All frozen historical sweep hashes, ranks, source epochs, decisions and Airtable archival routes remain immutable. The current broad-senior source acquisition, protected competitions and senior women's coverage *still* have higher priority than an outdated narrow-core allowlist section.

## Command router

Read `models/football/prompts/COMMAND_ALIASES.md`.

- `/sweep` -> `00_NORMAL_CHAT_AISCORE_FETCH.md`
- `/rank` -> `01_WORK_DAILY_SWEEP.md`
- `/xi` -> `02_NORMAL_CHAT_XI_ODDS.md`
- `/live` -> `03_NORMAL_CHAT_LIVE.md`
- `/audit` -> `04_WORK_POST_SLATE_AUDIT.md`
- `/report` -> `06_NORMAL_CHAT_REPORT.md`

Everything after the alias is launcher input. Same-message attachments are launcher inputs.

A handoff is historical context, not current authority. Reload this file and the current launcher before continuing old work.

## Model authority

- Football C is the only model that may create an official Website Pick or official model exposure.
- Football C2 is shadow-only. It may be ranked, executed, persisted and audited, but may never authorize official exposure.
- C3 and C4 are retired for new work. Do not execute them, require them, display them as current tracks, populate new current fields for them, or count them in current forward metrics.
- Historical C3/C4 records remain valid only for the exact epochs in which they were prospectively frozen.
- Python deterministic code validates structured C/C2 inputs and accounting. It is not production decision authority.

The active pair contract is:

`models/football/procedures/FOOTBALL_C_C2_ACTIVE_PAIR.md`

## Active production sequence

`SENIOR DISCOVERY -> SOURCE/IDENTITY INTEGRITY -> OPERATIONAL VIABILITY -> RESEARCHABILITY/CAPACITY -> COMMON STEP-1 EVIDENCE FREEZE -> [C BOARD + C2 SHADOW BOARD] -> C FOLLOW/RESERVE/STOP -> COMMON STEP-2 XI/RESEARCH/MARKET EPOCH -> [C OFFICIAL ACTION + C2 SHADOW ACTION] -> LIVE/WAIT -> AUDIT`

C and C2 share facts, not policy.

## Shared evidence / policy separation

For each fixture and epoch, freeze one factual evidence state before model policy is applied.

Common evidence includes:
- fixture identity/status/kickoff;
- operational viability/reliability state;
- route/carrier evidence;
- chance quality;
- failure/suppression evidence;
- H2H materiality and basis;
- continuation/leakage evidence;
- tournament format/incentive state when applicable;
- current XI/mechanism state;
- current executable quote at Step 2.

Football C owns:
- completion mode;
- burden-completion quality;
- continuation quality;
- opponent leakage;
- burden stall risk;
- C supported line;
- C official board state/rank;
- official FOLLOW/RESERVE/STOP lane;
- C Step-2 action.

Football C2 owns independently:
- C2 supported line;
- C2 route-quality ranking/selection-floor state;
- C2 shadow board state/rank;
- C2 Step-2 shadow action.

Never copy C's supported burden into C2. Never infer missing C2 from C.

## Registered Tier-1 Step0 XI/total proof non-blocking — 2026-10-11 (new sweeps)

For **new prospective Step0** with `LEAGUE_CHANNEL_FIRST_V1`, the country+league combinations explicitly listed in `models/football/engine/sweep_intake_evidence.py:TIER1_STANDARD_COUNTRY_LEAGUES` use expected standard lineup/Asian-total publication coverage without requiring historical match XI examples, past Asian-total fixture menus, league bookmaker URLs, or dated `VERIFIED_CHANNELS` attestations. An explicit `league_channel_profile` is optional for those Tier-1 registrations. This change removes only Step0 publication-proof blockers: independently established canonical fixture ID, exact competition/country/status/UTC kickoff, eligible senior scope, A/B operational and competition-reliability gates, source provenance, team-news and market observability, recheck plan, complete required/women coverage, complete A/B queue and deterministic packaging still apply. Tier-1 is not a fixture scoring advantage or auto-admission.

The waiver does **not** apply to Netherlands Eerste Divisie, Norway OBOS or Eliteserien, Germany 2. Bundesliga, Poland Ekstraklasa, England Championship, Hong Kong/Malaysia conditional pilots or any unregistered competitions. Those keep genuine `PROVEN_LEAGUE` and conditional goal-history rules. /rank must seek actual fixture-specific XI/news and bookmaker Asian totals; /xi must independently verify current executable quote and eligible XI; never fabricate a quote, price or lineups to satisfy a gate. Old frozen or BLOCKED sweep records and source hashes are not altered automatically.

## Step 0 — researchable senior intake

Use `models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md`.

Also apply:
- `FOOTBALL_AISCORE_SOURCE_ACQUISITION.md`;
- `FOOTBALL_SWEEP_CHECKPOINT_EXECUTION.md`;
- `FOOTBALL_REQUIRED_COMPETITION_COVERAGE.md`;
- `FOOTBALL_WOMENS_TOP_FLIGHT_COVERAGE.md`;
- `FOOTBALL_COMPETITION_RELIABILITY_MEMORY.md`;
- `FOOTBALL_OPERATIONAL_VIABILITY_GATE.md`.

Default scope:

`RESEARCHABLE_SENIOR_PRODUCTION`

Step 0 must:
- acquire a valid source scope under the source contract: prefer `EXACT_DATE_UNIVERSE`, otherwise use `BOUNDED_PRODUCTION_DISCOVERY` in FAST_PRODUCTION;
- complete a valid senior production universe under final reconciliation;
- preserve required/protected competition coverage;
- preserve senior women's top-flight accounting;
- apply hard scope exclusions;
- assign current operational viability A/B/C/D;
- apply competition reliability caps/demotion;
- perform cheap researchability screening;
- build the complete deterministic A/B capacity queue;
- admit only the first 15 A/B rows to the initial Work wave;
- preserve overflow A/B rows with immutable Step0 Capacity Queue Rank;
- package a valid `football-step0-handoff-v2` handoff.

A/B queue rank is operational only. It must not be based on expected goals, model attractiveness or result knowledge.

### Compact sweep Work research budget — new runs from 2026-10-09 ICT

For new /sweep runs, apply `models/football/procedures/FOOTBALL_COMPACT_SWEEP_WORK_BUDGET.md` as an explicit **prospective operational budget overlay**: `sweep_work_budget_policy=COMPACT_GOAL_ROUTE_V1`, initial Work wave 8 by the full frozen operational A/B rank, routine unique-fixture research ceiling 12, automatic replenish only below 4 active lanes. Source discovery, A/B rank ordering, protected/women/required coverage, hard exclusions and C/C2 decision logic are unchanged. Goal-rate research is context-only, **not** a Step-0 predictive hard filter or automatic league exclusion. Existing RUNNING/frozen/historical sweeps without this policy, including `SWEEP-20261009-1300-20261010-0300` Chunk 12, must retain their legacy 15/refill-to-10 semantics and must not be restarted or rewritten. Keep all A/B overflow as an auditable queue.

### Netherlands Eredivisie + Eerste Divisie dynamic goal-route Step1 scheduling — 2026-10-11

Both Dutch leagues were ALREADY approved for routine Step0 discovery; **do not rewrite this scope**. For new `GOAL_FIRST_STEP1_RESEARCH_V1` sessions only, `NETHERLANDS_DYNAMIC_GOAL_ROUTES_V1` adds the Big-Five-style source-backed carrier/two-sided, 4+ goals tail and 0–0/1–1/<=2-goal stall check to precise country=Netherlands registered Eredivisie/Eerste Divisie fixture identities, including approved senior Eerste Divisie Jong participants. Require fresh 4–10 genuinely completed competitive scores per team and pre-screen valid HTTPS references; missing form stays evidence-limited neutral. This changes deep Step1 research order **only**, never Step0 admissions, original rank, source hash, any frozen past screen/board, C official/C2 shadow results, actual bookmaker/XI requirements, Actual Bets or workload limits. No permanently favored Dutch club names. See `models/football/procedures/FOOTBALL_GOAL_FIRST_RESEARCH_SCREEN.md`.

### Big Five team research priority deployed prospectively (2026-10-11)

For **new Step1** whole-queue goal-first sessions, source-backed 4–10 game team histories under exact-country-and-league top-flight identity (England Premier League, Germany Bundesliga, Spain La Liga, Italy Serie A, France Ligue 1) receive a bounded `BIG_FIVE_DYNAMIC_GOAL_ROUTES_V1` research-order refinement: distinguish carrier vs two-sided routes; count 4+ goal tails and 0–0/1–1 draw traps; penalize repeated stalls. Do not use the fixed Oct 11 research team watchlist as a betting or Step0 rule. Missing form/identity receives no adjustment. Existing frozen decisions and original scope, Step0 source hashes, C official/C2 shadow, odds integrity and total research budget remain unchanged. See `FOOTBALL_GOAL_FIRST_RESEARCH_SCREEN.md`.

### New Step1 research priority across full A/B queue (2026-10-10)

A Step0 eight-fixture operational admission is **not** the football
selection shortlist. For each **new prospective /rank**, the
`GOAL_FIRST_STEP1_RESEARCH_V1` scheduler runs
`goal_route_prescreen_cli.py` across the entire frozen A/B queue,
before selecting eight fixtures for *deep* Step1 research. It uses
independent pre-kickoff historical team scoring/conceding and credible
continuation/stall routes. Missing sources yield `EVIDENCE_LIMITED`,
not low predicted goals. Original Step0 ranks, admission, hard exclusions,
source hash and prior boards stay frozen. The screen produces a separate
hashed Step1 research order: deep research can take a verified rank-13
football candidate before an operational rank-3 candidate. Neither is
automatically C-FOCUS, C2-FOCUS, FOLLOW or C-BET. Source/time/XI/odds
and all official C/C2 decisions remain enforced later. Older already
frozen rank boards retain their old research order.
See `models/football/procedures/FOOTBALL_GOAL_FIRST_RESEARCH_SCREEN.md`.

### XI + market proof before the Work queue

For new compact intake and explicitly marked resumed unfinished sweeps, apply `FOOTBALL_XI_MARKET_FIRST_INTAKE.md`: **expectation of XI publication**, not confirmed future starting XIs. Verify credible publishing channels and a near-KO recheck; A/YES needs strong evidence for both teams, B/UNCERTAIN may enter conditionally with sources and no routine FOLLOW until /xi validates. Require a current fixture-specific Asian total, news, competition source and identity/time. The raw discovery ledger is not the actionable board. Preserve exact required/protected/women's coverage; exclude/hold actual weak-data cases from Work only. The paused Oct-09 run remains untouched and retains legacy budget on future resume with `XI_MARKET_FIRST_V1` marker.

## Step 1 — Football C official board + Football C2 shadow board

Use `models/football/prompts/01_WORK_DAILY_SWEEP.md`.

For repaired handoffs, first apply:

`models/football/procedures/FOOTBALL_REPAIRED_HANDOFF_AUTHORITY.md`

Step 1 accepts both exact-date and bounded-production Step-0 handoffs after machine validation. A bounded handoff keeps `global_raw_exact=false` and must not trigger raw-universe rediscovery inside /rank.

Do not use /rank to rediscover or repair Step-0 identity/kickoff fields.

Freeze one common Step-1 football evidence epoch, then create:
- Football C official board;
- Football C2 shadow board.

Every ranked fixture requires:
- `common_evidence_basis`;
- C supported line + basis;
- C board state + basis;
- C2 supported line + basis;
- C2 board state + basis.

Run deterministic pair reconciliation:

`python models/football/engine/board_pair_cli.py --c <c.json> --c2 <c2.json>`

Required:
- `EXECUTED_C_C2_BOARDS`;
- `common_evidence_reconciled = true`.

Fail closed on ranked-universe mismatch, common-evidence drift, or C policy leakage into C2.

## Football C selection / clearing-goal funding

FOLLOW and RESERVE are workload priorities after the official C board, not a separate scoring verdict.

Third- and fourth-goal checks belong to the C ranking and current Step-2 decision. Lane only schedules follow-up, with no fixed goal-total ceiling.

Ranking should prioritize:
1. clearing-goal funding;
2. continuation after the first goal;
3. stall/control risk;
4. route/carrier reliability;
5. failure resistance;
6. evidence confidence;
7. burden protection.

Operational capacity does not change predictive rank.

The official lane remains:
- `FOLLOW` — routine Step 2;
- `RESERVE` — conditional;
- `STOP` — no routine Step 2 without explicit exception.

Same-kickoff guard and capacity limits remain:
- maximum routine FOLLOW = 6;
- maximum retained RESERVE = 4;
- maximum two routine FOLLOW fixtures at one exact kickoff minute.

## Step-1 capacity replenishment

The initial 15-fixture Step-0 cap is not a final board-size cap.

If `FOLLOW + RESERVE < 10` after a completed wave and prematch A/B rows remain:
- pull the next deferred rows strictly by ascending Step0 Capacity Queue Rank;
- assess them as the next replenishment wave;
- keep the original queue rank immutable.

Continue until:
1. FOLLOW + RESERVE reaches 10;
2. no prematch A/B deferred row remains; or
3. all remaining deferred rows have left the prematch window.

A STOP/PASS/started row does not permanently consume one of the initial 15 research slots.

## Mandatory deterministic runtime bootstrap

For execution-required `/rank`, `/xi`, and `/audit`, apply:

`models/football/procedures/FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md`

Tool/repository availability is a current-turn observed state.

Required record:

`FOOTBALL_RUNTIME_EXECUTION_RECORD`

The workflow must:
- probe Python;
- probe the current repository authority;
- materialize exact-current source when needed;
- run the stage runtime probe or XI portable self-check;
- attempt the actual deterministic command;
- preserve exact failure evidence.

A missing local checkout or raw container network failure is not repository unavailability while connected repository source remains accessible.

## /xi — single C+C2 match assessment

Use `models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md` with
`models/football/procedures/FOOTBALL_SIMPLE_ASSESS_AND_BET.md`.

The user only needs `/xi` or `/xi exception`.
Run `python xi_portable.py xi --c <c.json> --c2 <c2.json>`,
using independent C and C2 football factors.

- With no confirmed current quote, run `stage=football_assessment`.
  Deliver both football assessments immediately, no price requests
  and no executable bet/WAIT/price claims.
- If a genuinely verified current PREMATCH total and odds are
  available and all mandatory betting evidence is valid, use the
  existing strict `stage=decision` priced engine automatically,
  with no second user command. Price-action policy, readback,
  publication and current XI checks apply *only* to executable
  bets, never to quote-free football assessment.
- If already started, continue quote-free live football assessment
  immediately; current in-play betting requires independent live
  price authorization, never retrospective prematch execution.
- Do not invent a C2 result when independent C2 input is missing,
  or claim a bet/actual user wager without evidence.

The historical low-level `pair` and `football-pair` commands remain
compatible. They are not additional user-facing commands.

## Active-model accounting

New/current accounting uses C + C2 only.

Priority per model/fixture:

`DIRECT BET > COUNTABLE WAIT > WATCH > NONE`

WATCH:
- own supported line;
- assumed odds 1.65;
- 1u;
- model-performance accounting only.

WAIT:
- own deterministic target/min odds;
- frozen accounting semantics under `FOOTBALL_WAIT_ASSUMED_EXPOSURE.md`.

Only C may create official Website Picks/exposure. C2 accounting is shadow-only.

### Actual-user P/L authority — reset 2026-10-08

Canonical actual-user bet ledger: Airtable table `Actual Bets — Current` (`tblGsnU4Ht0OpmdH8`, active base `appbzxqXYf0lKfD4P`).

From 2026-10-08 ICT onward:
- actual-user profit/loss, turnover, ROI and running P/L are calculated from this table only by default;
- do not mix older actual-bet records into current profit unless the user explicitly requests historical combined reporting;
- actual-user execution truth comes only from rows in this table (or a new user slip awaiting persistence);
- Website Picks, Decision States, model WATCH/WAIT accounting and C2 shadow exposure must never be counted as actual-user P/L.

Historical C3/C4 settlement must use explicit historical accounting mode and must never enter a current active-roster payload.

## Live

Use `models/football/prompts/03_NORMAL_CHAT_LIVE.md`.

Current live roster:
- Football C official;
- Football C2 shadow.

No live-stat or bookmaker-quote confirmation gate is required for ASSESS. Assess available score/minute, independent frozen C/C2 theses and material events without prices. A current quote is required only for an explicitly requested executable BET CHECK. Recompute tournament incentive at each material live epoch when applicable before any betting authorization.

C2 never creates official exposure.

## Audit

Use `models/football/prompts/04_WORK_POST_SLATE_AUDIT.md`.

Audit all recorded assessed matches, not only Website Picks or LOCK/FOLLOW rows.

Separate:
- frozen state;
- observed result;
- diagnosis;
- official C model P/L;
- C2 shadow model P/L where lawfully countable;
- actual user P/L.

Missing C2 execution in a current all-model/C+C2 exception is a workflow defect, not a C2 PASS.

Never retrospectively reconstruct missing model outputs from FT/current information.

Historical C3/C4 rows may be reported only as historical records from their original frozen epochs.

## Persistence

Current new records must keep C and C2 separate.

Daily Coverage / board persistence:
- C state/rank/line/basis;
- C2 state/rank/line/basis;
- common evidence basis;
- official C lane;
- pair reconciliation status/revision.

Decision States:
- C Action;
- C Supported Line;
- C2 Supported Line;
- C2 Shadow Action;
- Engine Execution Status;
- Engine C Result;
- Engine C2 Result;
- failure reason when applicable;
- current evidence/recheck fields;
- active-model accounting result.

Website Picks:
- Football C official exposure only.

Historical C3/C4 fields may remain in Airtable for immutable history. Do not populate them for new current rows.

## Historical fidelity

Do not rewrite:
- historical C3/C4 board states;
- historical C3/C4 supported lines/actions;
- old engine results;
- old accounting rows;
- old Football A records.

Retired files may remain for audit/history but must not be imported by current runtime or required by current launchers.

## Production principle

Current authority is simple:

**Football C decides official exposure. Football C2 challenges it prospectively. Everything else is historical.**
