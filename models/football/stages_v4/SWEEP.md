# /sweep — Football V4 source-backed fixture intake

This is the only current /sweep launcher. Do not load the retired
`00_NORMAL_CHAT_AISCORE_FETCH.md` or V1–V3 Step0 engines.

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
run ID. Do NOT ask Work to invent completion from Airtable records.

For an older derived intake, preserve both original `source.json`
and `intake-unattested.json` under that run ID; the replay checker
will compare every business field and attested SHA256 before export.
Replaying a former source snapshot is NOT verification that its fixtures
remain before kickoff **now**. Match status and original KO must be
rechecked when Work performs /rank. An already-started match cannot
receive a retroactive prematch C/C2 selection.

**Open-league discovery rule:** Fetch the source's complete available senior competitive fixture listing for the requested window BEFORE applying the league registry. Do not query only registered leagues or discard a Brazilian, Mexican or other unfamiliar official fixture at acquisition. The fixture calendar can be bounded by time/provider; it need not prove every fixture worldwide. Country and competition labels are required to distinguish friendlies and explicit exclusions. The new `DISCOVERY` lane screens an unregistered match's real recent four-to-ten competitive results for both teams and retains low/unknown signals in `discovery_watchlist`, not EXCLUDED. Only an independently source-backed scoring signal PLUS current match publishing/researchability proof permits discovery qualification for /rank. Unregistered official cups also require current competition-format/incentive proof. Report discovery-qualified and discovery-pending separately; never silently delete them. Explicitly banned leagues and friendlies remain excluded.

## GOALS-FIRST admission (supersedes routine-league auto-admission)

A registered fixture is **not** automatically Over-friendly. After collecting
all source-visible future competitive fixtures, collect genuine recent four-to-ten
competitive results for BOTH teams where possible (actual goals for/against,
finished match dates, HTTPS result source, and observation time). Apply the **same**
`GOAL_SIGNAL_FIRST_V1` / `EQUAL_SOURCE_BACKED_GOAL_SIGNAL_ALL_LEAGUES_V1`
standard to routine, conditional, pilot and unregistered DISCOVERY leagues.
Only quantified strong goals potential plus any required match researchability
enters `eligible_queue` / the prospective `/rank` shortlist. Registered matches
with no usable scoring data go into `goal_research_queue` as
`PENDING_GOAL_RESEARCH`, not automatic eligible; source-backed low-goals or
0-0/1-1 trap signals stay as a watchlist, not model PASS.

**Research order:** examine quantified goal-positive matches FIRST, regardless
of registered status or imminent KO. Remaining missing-goals-history fixtures
follow for targeted research, then genuinely weak goal-signal fixtures.
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
**research priorities, not betting picks**. Maintain true C/C2 model
execution only at `/rank` with real source-backed football data. Missing
Asian-total quotes do not block goal-history screening or initial research.

Read `league_registry.py` and `README.md`. Interpret the requested
sweep window in ICT; start at the actual current time unless an explicit
future start is given, and never include already-started fixtures.

Fetch one appropriately bounded current fixture feed (AiScore if
available; an independently checkable source otherwise), gather actual
match IDs, teams, source URLs, current kickoff and prematch statuses
within the window. Include the researched country's league tiers,
women's senior top flights and legitimate official competitions.
Do NOT require every women's league worldwide to be enumerated.
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
Airtable writes only when a genuine live source/run receipt is available.
