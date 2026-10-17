# /sweep — Football V4 source-backed fixture intake

> **Work conversation role — SWEEP ONLY.** This conversation is dedicated to
> Football C V4 fixture intake and sweep checkpoint/resume for the user's
> requested window. Load this launcher from current SlipTrace main before
> executing `/sweep`. Do not silently continue into `/rank`, `/xi`,
> `/live`, `/audit`, or code maintenance. Produce the native source-backed
> sweep receipt (or an explicit pending/blocker state) and hand it to a separate
> rank conversation. A user explicitly changing the task requires reloading the
> corresponding canonical launcher; never reuse sweep assumptions as authority.
> This is the SlipTrace production route, not FOM.


This is the only current /sweep launcher. Do not load the retired
`00_NORMAL_CHAT_AISCORE_FETCH.md` or V1–V3 Step0 engines.

## Work execution route — resolve before acquisition

A missing local checkout is a setup task, not a reason to abandon `/sweep`.
Use current `acchtt/SlipTrace` main and one of these executable routes:

1. With shell/Python, run the repository-owned adapter:
   `python models/football/stages_v4/tools/work_sweep.py --request REQUEST.json --output NEW_OUTPUT_DIRECTORY`.
2. Without local execution, commit
   `models/football/stages_v4/acquisition_requests/<V4-run-id>.json` using the
   connected GitHub write capability on authorized production `main`. Exact fields:
   `run_id`, `window_start_ict`, `window_end_ict`, with timezone-aware ISO times.
   A push changing this request on `main` invokes
   `.github/workflows/football-v4-work-acquisition.yml` (**Football V4 Work native
   sweep**). Confirm the actual workflow run and `sweep` job, not merely a
   successful file write. Feature branches require explicit dispatch with
   `request_file`; merging a tested request into main is the automatic trigger.

The runner acquires full LiveScore date arrays for ICT and UTC, reconciles the
senior union and independent terminal refetch, researches both teams' recent
competitive results in native priority order, refreshes fixture status, calls
native `stage.sweep`, and publishes the exact source/receipt/checkpoint bundle.
This is an independent provider fallback, not AiScore evidence. AiScore remains
preferred when its complete surfaces are available. No repeated loading-page
loop is needed. The old raw-download helper is diagnostic only.

Retrieve the `v4-work-<job-index>-<workflow-run-id>-<attempt>` artifact and its
Actions job-summary link. Inspect `rank-handoff.json`, `checkpoint.json`,
`source.json` and `v4_sweep_ready.json`. Artifacts are retained for 90 days;
include the workflow run/artifact link and source run ID in the sweep response
so a separate rank chat can discover the same bundle. Do not claim publication
until the upload step succeeds. A `BLOCKED` checkpoint has exact failure evidence
and must never be substituted for a native receipt.

`V4_SWEEP_READY` alone does not complete the work. Report the separate
`RESEARCH_COMPLETE` / `RESEARCH_PENDING` checkpoint state and pending rows.
The adapter does not certify researchability from a generic `hasStats` or
`hasLineups` flag. Fixtures still needing actual current mechanism/stat/news
coverage or official cup-format evidence remain pending for targeted research.
Continue that work within the requested task; do not ask the user to resubmit
matches or silently lower the evidence standard.

For a saved source, add `--source PATH` locally, or use dispatch `source_file`
with its committed recovery path. This preserves an exact original copy and
never repeats date discovery. A resume derives a new source and receipt in a
fresh directory; it does not overwrite the earlier bundle. Existing native
freshness checks still apply: stale evidence produces an explicit checkpoint,
never a backdated live receipt. An archival replay is a different operation and
still requires fresh full-cohort status before rank.

Code-only pushes and pull requests run offline tests without acquiring fixtures.
Changed requests are scoped to that push; expired requests fail before network
access. If neither local execution nor a GitHub write/dispatch is available,
report the exact missing capability and preserve the request. Never imply that
changing repository instructions installs a runner inside an inaccessible chat.

## Check execution capability before acquiring fixtures

A new Work chat may have an empty workspace. **A missing local checkout is not
proof that native V4 execution is unavailable.** Resolve the execution route
before spending resources on fixture acquisition:

1. Inspect the actual callable tools. When shell/Python execution is available,
   use an existing clean SlipTrace checkout or obtain `acchtt/SlipTrace` from
   GitHub at current main and record its commit. Read `AGENTS.md` and current
   authority. Confirm the runner with
   `python models/football/stages_v4/stage.py --help`. Do not copy only stage.py:
   its V4 and engine imports must come from the same revision. Missing files
   require checkout/setup, not immediate abandonment of the sweep.
2. If local execution is genuinely unavailable, inspect the existing
   `.github/workflows/football-v4-replay-attestation.yml` fallback. Saving the
   original source at `models/football/stages_v4/recovery/<run-id>/source.json`
   on an authorized repository branch triggers its **push** workflow. A manual
   workflow-dispatch tool is not required. Verify the actual run and artifact;
   do not assume Actions ran merely because the file was saved. Respect any
   repository-write approval requirement; this launcher grants no bypass.
3. If neither route is available, report the exact missing capability or failed
   operation before starting expensive acquisition. Distinguish missing files,
   unavailable execution tools, repository permission, and a failed native
   validation. Do not say the runner is unavailable without checking the
   relevant capability and recovery route.

AiScore is preferred, not the exclusive provider. The existing independently
checkable-provider fallback below still applies. Preserve canonical provider
IDs/provenance; never relabel another provider's ID as an AiScore ID.

If source facts have already been acquired when execution fails, preserve the
unchanged source and exact pending acquisition/validation gaps as a recovery
checkpoint where storage is available. An incomplete source is not
`V4_SWEEP_READY` and must not be offered to rank as a valid handoff. Resume from
that evidence without asking the user to reconstruct the fixture list. Never
invent completeness, a native execution, an Actions run, or an attested receipt.

## Rebuilt acquisition contract — complete date surfaces before registry

Prospective sweeps now use `DATE_SURFACE_BATCH_V2`. The old failure mode
where an operator assembled a small fixture list and then ran the registry is
forbidden. The discovery order is:

`REQUESTED WINDOW -> COMPLETE PROVIDER DATE SURFACES -> PAGE/BLOCK RECONCILIATION -> TERMINAL REFRESH -> FULL SENIOR FIXTURE SET + UEFA YOUTH LEAGUE EXCEPTION -> REGISTRY/DISCOVERY CLASSIFICATION -> CHEAP RESEARCH-PRIORITY FILTERS -> GOALS-FIRST SCREEN`

The registry is **never** a fixture-discovery query. Do not search
Ekstraklasa, Serie A, Superliga, Veikkausliiga, etc. one by one and then call
the union a sweep. Open the provider's date/listing surfaces for every ICT and
UTC calendar date touched by the requested window, exhaust pagination, record
every source-visible senior football competition block, and only then apply
the registry locally. **Specific youth exception:** retain source-visible `UEFA Youth League` fixtures from those complete date surfaces even though the ordinary acquisition scope is senior football. Do not broaden this into generic youth-league crawling; other youth competitions remain outside the approved intake unless separately authorized.

Every new `source.json` must contain
`source_completeness_manifest.schema_version=football-v4-source-completeness-v2`
with:

- `acquisition_mode=DATE_SURFACE_BATCH_V2`;
- `league_query_mode=DATE_SURFACE_ONLY`;
- `registry_prefilter_applied=false`;
- the exact ICT+UTC `required_surface_keys`;
- one complete `date_surfaces[]` entry for every required key;
- exact provider page count and `pages_fetched=1..N`;
- exact senior competition-block count for each surface;
- exact fixture IDs and provider fixture count for every competition block;
- the complete source fixture union, which must equal `source.fixtures`;
- an independent terminal-sentinel refetch for the last six hours of the
  requested window (or the whole window when shorter).

If one required date surface, page, competition block or terminal fixture is
missing, `stage.py sweep` fails closed. It must not emit
`V4_SWEEP_READY`. A zero-match competition block or an empty window is valid
only when the provider surface itself is complete and its counts reconcile.

After this acquisition proof, `cheap_sweep_filters.py` may reorder **deep
research**, never acquisition. `PRIMARY_RESEARCH`, `SECONDARY_RESEARCH`,
`SPECIAL_RESEARCH`, `DEFERRED_RESEARCH` and `NEUTRAL_RESEARCH` are workload
priorities only. They cannot hard-exclude a valid competitive fixture and
cannot override a fresh source-backed `DISCOVERY_GOAL_QUALIFIED` signal.

**UEFA Youth League safeguard (2026-10-13):** `UEFA Youth League` / recognized provider aliases are an explicit `CONDITIONAL` youth exception. They receive `SPECIAL_RESEARCH / UEFA_YOUTH_LEAGUE_MATCH_SPECIFIC_RESEARCH`, require fixture-specific recent-goal evidence, and still require the current competition path/format/incentive state to be understood at assessment. Competition identity alone never makes the match goal-positive. Generic youth competitions remain excluded.

**Big Five safeguard:** Premier League, Bundesliga, La Liga, Serie A and
Ligue 1 do not enter the active deep-research list merely because they are
`ROUTINE`. With no separate current team/event prior they default to
`DEFERRED_RESEARCH / TOP_FIVE_STATUS_NOT_A_GOAL_SIGNAL`. They remain in the
full source/audit backlog and can still jump directly to `GOAL_PRIORITY` when
fresh source-backed goal evidence qualifies the actual fixture.

This restores the useful part of the older sweep behavior—broad date-surface
enumeration and a terminal sentinel—without restoring old Work ZIPs,
capacity queues, league-by-league crawling or bookmaker/XI blockers.


## Mandatory source-attested export for next-chat Work /rank

`V4_SWEEP_READY` must come from **actual execution** of
`models/football/stages_v4/stage.py sweep` on the saved source file.
A manually rebuilt JSON with self-matching hashes must be labeled
`V4_SWEEP_DERIVED_UNATTESTED` and is NOT a completed V4 handoff.

If normal chat cannot execute the Python model locally, SAVE the
original source snapshot to
`models/football/stages_v4/recovery/<new-V4-run-id>/source.json`
on the current GitHub branch. The
`.github/workflows/football-v4-replay-attestation.yml` CI runner
will execute the real V4 algorithm and upload a
`v4-original-source-attested-receipts` artifact containing an official
`<run-id>-v4_sweep_ready.json`, or fail closed with the exact validation
error. Give Work chat the GitHub Actions run URL and the original
run ID. Do NOT invent source completeness from the Google Sheets ledger or historical Airtable records.

For an older derived intake, preserve both original `source.json`
and `intake-unattested.json` under that run ID; the replay checker
will compare every business field and attested SHA256 before export.
Replaying a former source snapshot is NOT verification that its fixtures
remain before kickoff **now**. Match status and original KO must be
rechecked when Work performs /rank. An already-started match cannot
receive a retroactive prematch C selection.

**Open-league discovery rule:** Fetch the source's complete available senior competitive fixture listing for the requested window BEFORE applying the league registry. Do not query only registered leagues or discard a Brazilian, Mexican or other unfamiliar official fixture at acquisition. The fixture calendar can be bounded by time/provider; it need not prove every fixture worldwide. Country and competition labels are required to distinguish friendlies and explicit exclusions. The new `DISCOVERY` lane screens an unregistered match's real recent four-to-ten competitive results for both teams and retains low/unknown signals in `discovery_watchlist`, not EXCLUDED. Only an independently source-backed scoring signal PLUS current match publishing/researchability proof permits discovery qualification for /rank. Unregistered official cups also require current competition-format/incentive proof. Report discovery-qualified and discovery-pending separately; never silently delete them. **User exclusion (2026-10-13): all African domestic leagues, women's domestic top flights, and domestic cups are classified EXCLUDED after source acquisition and before goal-history/deep research. Preserve them in the source ledger with reason `USER_AFRICA_DOMESTIC_EXCLUSION`. CAF/other continental club competitions and protected official internationals remain eligible for their normal format/incentive path.** Explicitly banned leagues and friendlies remain excluded.

## GOALS-FIRST admission (supersedes routine-league auto-admission)

A registered fixture is **not** automatically Over-friendly. After collecting
all source-visible future competitive fixtures, collect genuine recent four-to-ten
competitive results for BOTH teams where possible (actual goals for/against,
finished match dates, HTTPS result source, and observation time). Apply the **same**
`GOAL_SIGNAL_FIRST_V1` / `EQUAL_SOURCE_BACKED_GOAL_SIGNAL_ALL_LEAGUES_V1`
standard to routine, conditional, pilot and unregistered DISCOVERY leagues.
Strong quantified goal profiles enter `eligible_queue` as
`GOAL_PRIORITY`. A narrow source-backed safety lane also admits complete
near-threshold profiles as `GOAL_REVIEW`: priority >=50, mean 3+ >=50%, and
0-0/1-1 trap <=35%. These rows always research behind `GOAL_PRIORITY` and gain
no C certificate from Step 0. The purpose is only to prevent a threshold cliff
from hiding a potentially valid match before Football C sees it.

Registered matches with no usable scoring data remain in `goal_research_queue`
as `PENDING_GOAL_RESEARCH`; genuinely weak or trap-heavy signals stay on the
watchlist, not model PASS.

The quantitative screen has **four league-neutral research-admission paths**.
The original route-composite path remains: priority score >=60, mean 3+ rate
>=55%, and 0-0/1-1 trap <=35%. The high-rate path admits a fixture when mean
3+ >=65%, mean 4+ >=45%, and the low-draw trap <=20%, even when the composite
score is below 60.

Two additional paths prevent Step 0 from demanding G4-like evidence before C
has researched whether a G3 certificate exists. The **G3 distribution** path
admits priority >=50 with mean 3+ >=67% and low-draw trap <=25%, without a 4+
minimum. The **carrier/leakage G3** path admits priority >=50 when the strongest
source-derived route is >=1.75 goals, mean 3+ >=60%, mean 4+ >=30%, and the
low-draw trap <=25%. These paths are research permission only: they do not
create G3/G4/G5/G6, supported burden, board state, or a bet. Current
availability, route transferability and tournament context are still assessed
by Football C at /rank. No league identity, market quote, live score or final
result can satisfy any admission path.

**Research order:** examine `GOAL_PRIORITY` matches first, then the narrow
`GOAL_REVIEW` safety lane. Missing-goals-history fixtures follow for targeted
research, then genuinely weak goal-signal fixtures.
Use `goal_research_order` for missing-data acquisition. Do NOT sequentially
crawl every league to satisfy all missing histories: fetch only current
source-visible, plausible fixtures in the bounded window. When form is obtained,
produce a new *native* V4 source receipt using current fixture status/KO and
fresh source timestamps, without a global discovery restart; never edit an
older signed receipt's `eligible_queue` or integrity hash. If there are zero
verified goal-positive candidates, report an honest empty goal shortlist with
the pending research pool rather than a misleading fixture-filled board.

Report separate totals: source fixtures; verified Over-research shortlist;
missing goal-history research; low-goal signals; conditional/unregistered
researchability pending; excluded friendlies/explicit bans. These are
**research priorities, not betting picks**. Maintain Football C-only model
execution only at `/rank` with real source-backed football data. Missing
Asian-total quotes do not block goal-history screening or initial research.

Read `league_registry.py` and `README.md`. Interpret the requested
sweep window in ICT; start at the actual current time unless an explicit
future start is given, and never include already-started fixtures.

Fetch complete provider **date/listing surfaces** (AiScore if available; an
independently checkable source otherwise), not a hand-picked league list.
Reconcile all pages and senior competition blocks into one immutable source
fixture union, then gather canonical IDs, teams, source URLs, kickoff and
status. Registered leagues, women's senior top flights, unregistered official
competitions and explicit exclusions are classified only after acquisition.
Do not claim worldwide completeness; prove completeness only for the exact
provider/date surfaces used for the requested window.
Preserve visible out-of-scope fixtures in audit ledger. For conditional
leagues include `researchability_status=VERIFIED` only if the actual
match/season data channels were checked, otherwise show PENDING.
No historical lineup or total-odds proof for routine leagues.

Preserve the unchanged original source.json alongside its native receipt and independently checked provider source URLs/timestamps. V4 /rank now must replay that source and refresh the entire eligible fixture-status cohort within 10 minutes. A standalone matching JSON digest is consistency evidence, not third-party source attestation.

Prepare `football-stages-v4` input and run
`python models/football/stages_v4/stage.py --output v4_sweep.json sweep --source source.json`.
Report the full verified research queue sorted by the source-backed
goal-first signals, all pending-proof fixtures, excluded reasons, and
the actual integrity hash. No 8-match cap, forced ZIP, serial
Work chat, indefinite resume, imaginary fetch or automatically placed bet.
Google Sheets `Sweep Runs` writes only when a genuine live source/run receipt is available.
