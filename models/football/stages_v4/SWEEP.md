# /sweep — Football V4 source-backed fixture intake

> **Normal chat role — SWEEP ONLY.** This conversation is dedicated to
> Football C V4 fixture intake for the user's requested window. Load this
> launcher from current SlipTrace main before executing `/sweep`. Do not
> silently continue into `/rank`, `/xi`, `/live`, `/audit`, or code
> maintenance. Produce the native source-backed sweep receipt only after the
> targeted research obligation is complete, or return an explicit resumable
> checkpoint. This is the SlipTrace production route, not FOM.

This is the only current /sweep launcher. Do not load the retired
`00_NORMAL_CHAT_AISCORE_FETCH.md` or V1–V3 Step0 engines.

## Normal-chat execution route

1. Freeze the requested ICT window and acquire each required provider date
   surface once. Preserve the exact original source snapshot and provenance.
   **Persist that source before any deep research starts.**
2. Run V4 discovery/goals-first screening from that snapshot.
3. Create a durable research checkpoint containing the exact research order,
   source SHA256, resolved fixture IDs and unresolved queue.
4. Research GOAL_PRIORITY first, then GOAL_REVIEW. Fetch only missing
   fixture-specific football facts. Persist progress after at most **4 fixture
   dispositions** (and before any expected tool/conversation boundary).
5. Continue until every actionable research row is qualified, explicitly
   evidence-limited with a real trace, or status-excluded.
6. Execute the native V4 sweep/receipt code against the saved source when a
   local/runtime Python route is available.
7. If native Python is unavailable, use original-source replay/attestation
   **after** research completion. This is validation fallback, not a reason to
   switch the sweep into a Work orchestration task.

Do not use `.github/workflows/football-v4-work-acquisition.yml` or commit an
`acquisition_requests` file as the default way to perform a new sweep.
Historical Work-native artifacts remain valid when provenance checks pass.

### Durable checkpoint and resume contract

The active normal-chat checkpoint schema is
`football-v4-sweep-research-checkpoint-v2`. Persist it under the current run
(or an equivalent durable attachment) with:

- immutable run/window and original-source SHA256;
- `research_order`;
- per-fixture `research_disposition` = `COMPLETE`,
  `EVIDENCE_LIMITED`, `STATUS_EXCLUDED` or `RESEARCH_PENDING`;
- attempt count and concrete pending/evidence-limit reasons;
- `resume_queue` containing **only unresolved fixture IDs**;
- completed/reused counts and the last checkpoint time.

`/resume` must load this checkpoint first. It must not restart date-surface
discovery, repeat resolved fixture research, or recreate an empty research
queue from chat history. The repository runner supports this with
`tools/work_sweep.py --resume-from <previous-output-or-checkpoint>`; the same
semantics apply when normal chat performs the research directly.

A transient research failure gets one retry. If the same source-backed gap
remains after the retry, freeze it as `EVIDENCE_LIMITED` with the real attempt
trace instead of looping indefinitely.

If the immutable source has become too old for native V4 freshness validation,
perform **one bounded fresh source refresh** for the same requested window,
create a new source epoch, and reuse prior research by canonical match ID only
when teams and kickoff still match. Started/changed fixtures become explicit
status/source exclusions. Do not re-research successfully mapped fixtures.

If the user narrows the end of the window, preserve research already completed
inside the new window and mark later fixtures DEFERRED_OUTSIDE_WINDOW. Do not
reacquire a date surface merely because the requested end became earlier when
the saved complete surface already covers the narrower interval.

### Completion boundary

`V4_SWEEP_READY` is structural readiness, not permission to hide unfinished
research. A completed user-facing sweep handoff requires no actionable upstream
research rows left unresolved. If time/tool limits interrupt research:

- save the source snapshot and v2 research checkpoint;
- report `RESEARCH_PENDING` with exact pending count and fixture identities;
- resume **only the checkpoint's `resume_queue`**;
- do not reacquire the date surface unless freshness/source validation explicitly
  requires the one bounded refresh described above;
- do not repeat resolved research;
- do not present the partial handoff as the completed newest sweep.

A user may explicitly send a partial verified subset to `/rank`, but it must
remain labelled PARTIAL on both sides and its pending upstream count must stay
visible. Rank must never make that partial board look like a completed window.

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


## Mandatory source-attested export for downstream Work /rank

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
error. Give the downstream Work /rank chat the GitHub Actions run URL and the original
run ID. Do NOT invent source completeness from the Google Sheets ledger or historical Airtable records.

For an older derived intake, preserve both original `source.json`
and `intake-unattested.json` under that run ID; the replay checker
will compare every business field and attested SHA256 before export.
Replaying a former source snapshot is NOT verification that its fixtures
remain before kickoff **now**. Match status and original KO must be
rechecked when Work performs /rank. An already-started match cannot
receive a retroactive prematch C selection.

**Open-league discovery rule:** Fetch the source's complete available senior competitive fixture listing for the requested window BEFORE applying the league registry. Do not query only registered leagues or discard a Brazilian, Mexican or other unfamiliar official fixture at acquisition. The fixture calendar can be bounded by time/provider; it need not prove every fixture worldwide. Country and competition labels are required to distinguish friendlies and explicit exclusions. The new `DISCOVERY` lane screens an unregistered match's real recent four-to-ten competitive results for both teams and retains low/unknown signals in `discovery_watchlist`, not EXCLUDED. Only an independently source-backed scoring signal PLUS current match publishing/researchability proof permits discovery qualification for /rank. Unregistered official cups also require current competition-format/incentive proof. Report discovery-qualified and discovery-pending separately; never silently delete them. **User exclusion (2026-10-13): all African domestic leagues, women's domestic top flights, and domestic cups are classified EXCLUDED after source acquisition and before goal-history/deep research. Preserve them in the source ledger with reason `USER_AFRICA_DOMESTIC_EXCLUSION`. CAF/other continental club competitions and protected official internationals remain eligible for their normal format/incentive path.** Explicitly banned leagues and friendlies remain excluded.

## Operational grade is evidence-derived

Keep `registry_lane` separate from `operational_grade`. ROUTINE is not the
only path to grade A. A CONDITIONAL/PILOT/DISCOVERY fixture with current
fixture-bound `researchability_status=VERIFIED` and checked channels may be A;
do not carry a permanent B cap merely because of league registry classification.
B must represent a real unresolved operational limitation, not source category.

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
