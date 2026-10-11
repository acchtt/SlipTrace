# Football v2 — New /sweep and /rank V4

**User authorization:** "Make a new sweep and rank stage. Includes leagues that we researched."
**Previous V1–V3 production CLIs stay permanently retired.** This is a
new `models/football/stages_v4/` implementation, not a patch or resume.
Only C official + independent C2 shadow; /xi stays one command.

## Minimal stage design

`/sweep` = find source-backed **future** fixtures in the requested ICT
window from the researched league registry, freeze their IDs, kickoff
and original sources, return a single inclusive research queue.

`/rank` = use that same frozen V4 source receipt, acquire football
form/news/incentives once, execute the existing **real C and C2 engines**
together and produce a board. No Step0 Work ZIP, no separate Work chat,
no global "prove there are no other women's fixtures worldwide" task,
no compulsory first-eight admission, no historical bookmaker odds
or published XI requirement for ordinary Tier-1 intake.

The current implementation is **deterministic and local**. A conversation
operator must actually query fixtures/results from AiScore or a suitable
independent source and supply real evidence in the input JSON. Code
does NOT scrape providers, verify the truth of a claimed URL remotely,
read the user's clock automatically when given a test override, or
write Airtable by itself. The official result remains
`V4_RANK_EXECUTED_AWAITING_AIRTABLE_READBACK` until the actual active
base write/readback is completed. Never say a board has been published
just because C/C2 were executed.

## Researched league registry

Stored in `league_registry.py`: match country AND competition. Tier
means operational research priority, **not** intrinsic goal propensity.

- **Routine**: English Premier League, German Bundesliga and
  2. Bundesliga, Spanish La Liga, Italian Serie A, French Ligue 1;
  Dutch Eredivisie/Eerste Divisie; Norway Eliteserien/OBOS;
  Sweden Allsvenskan, Denmark Superliga; Belgium Pro League,
  Portugal Primeira Liga, Austria Bundesliga, Scottish Premiership,
  Swiss Super League, Japan J1/J2, Korea K1 and Saudi Pro League.
- **Conditional**: England Championship, Spanish Segunda,
  Polish Ekstraklasa, Czech First League/FNL, Hong Kong Premier
  League, Malaysian Liga Super, UAE Pro League, Qatar Stars League,
  Korea K2, Greek Super League, senior women's top flights and
  major senior official cups/continental competitions.
- **Pilots**: Thailand Thai League 1/2, Indonesia Liga 1,
  Swedish Superettan, Denmark First Division and Saudi First
  Division. They are **searched and retained**, but require
  current source-backed match/league researchability to reach rank.
- **Explicit exclusions preserved**: noncompetitive friendlies;
  Bangladesh, Israel, Kenya, Iraq, Wales, Kuwait and Finland
  domestic leagues; Germany 3. Liga, Italy Serie B, France
  Ligue 2, Norway 2./3. divisjon and unregistered obscure leagues.
  A future explicit user instruction can update these in a new PR.
  Protected official tournaments are not excluded merely because
  domestic leagues from the same country are excluded.

Recent high-scoring **teams are dynamic**, not hardcoded names.
Actual recent 4–10 source-backed competitive scorelines for each
team, when available, feed the existing goal-route prescreen:
carrier contribution, second route, Over 3 tail, 0–0/1–1 trap and
prolonged two-goal stalls. Big Five and Netherlands use the existing
dynamic researched overlays. Missing form does not pretend a team
is low scoring; its fixture remains eligible for football research.

## /sweep inputs and outputs

Operator fetches **one date/window scoped fixture listing** (do not
loop over all leagues serially), supplemented only where source data
are actually missing. For each fixture capture real immutable
`match_id`, full country, named competition, `competition_kind`,
home/away, `kickoff_utc`, prematch status, original HTTPS source
and `observed_at_utc`. At source level record provider family,
opened HTTPS listing URL, checked timestamp and requested window.
Use independent corroboration when identities conflict; a search
snippet is not a verified fixture status.

Fill `source.json` (schema `football-stages-v4`) with:
`run_id=V4-...`, `window_start_utc`, `window_end_utc`,
`source_family`, `source_url`, `source_observed_at_utc`,
and `fixtures` (list). For each conditional/pilot/women fixture
set `researchability_status=VERIFIED` only when the current
league/team publishing channel actually checks out, and attach a
`researchability_proof` object with that same source-backed
`match_id`, a genuinely visited `source_url`,
`checked_at_utc`, and `current_channels_checked=true`.
Otherwise the fixture remains `PENDING_RESEARCHABILITY` in the ledger,
NOT a model PASS. Invalid match-specific proof becomes
`PENDING_SOURCE`; it never invalidates unrelated real fixtures.
Routine Tier-1 fixtures do not need bookmakers,
XI publication history or an `odds` field just to enter the queue.

```bash
python models/football/stages_v4/stage.py --output v4_sweep.json sweep --source source.json
```

Note: global CLI options `--output` and `--now` occur BEFORE
the `sweep` or `rank` subcommand. Normally omit `--now` so the
machine's actual UTC clock is used. All timestamps are UTC-aware.
For historical QA, `--now <ISO_UTC>` may be supplied.

Outputs a hashed complete source-visible fixture ledger and
**all eligible** source-backed candidates with goal-first research order. Unverified individual fixture IDs,
stale fixture links or malformed team-form evidence are quarantined
with their original source-row index and exact reason; they are not
silently dropped and do not block other source-backed leagues.
There is NO arbitrary eight-match cap. A run with no eligible
source-confirmed fixture is a legitimate empty sweep, not a mandatory
15-minute research loop. No global women's coverage absence scan:
any **actually observed** senior women's top-flight fixture is
included/checked and cannot be dropped silently.
The operator may store receipts in Airtable after confirming a
separate run ID and current source epoch; do not silently overwrite
old frozen records or old bets.

## /rank inputs and outputs

Use only `v4_sweep.json`, plus genuinely researched source-backed
current football data passed to C and C2. Prepare two independent
payloads conforming to existing `football-engine-v1` board schema.
They must have **exact same frozen fixture cohort and common
evidence**, with real match-specific football basis, tournament
incentives when applicable. An odds quote is optional for football
research. When odds are unavailable do not invent any or say BET.

`unranked.json` maps EVERY eligible source match ID not researched
to a genuine evidence/window/budget reason; no false C PASS.
Rank all truly assessable candidates in current time budget,
not the first eight arbitrarily. The prescreen's full research
order controls priority; source-limited/elapsed fixtures are noted.

```bash
python models/football/stages_v4/stage.py --output v4_rank.json rank \
  --sweep v4_sweep.json --c c.json --c2 c2.json --unranked unranked.json
```

This calls the real independent paired engine. Source epoch SHA256,
original fixtures, current kickoff, strict C+C2 common evidence and
decision semantics are enforced. If kickoff has already passed, do
not reconstruct a retroactive prematch ranking; /xi live assessment
is a distinct workflow.

**Persistence:** Send execution rows for C and C2 to active Airtable
`appbzxqXYf0lKfD4P` by fresh immutable per-run IDs (historical
rows untouched), store the V4 receipt hash and the official C lane,
then *independently refetch*. Use `stage.py verify --rank v4_rank.json
--readback airtable_refetch.json` only with a true refetch from active
base. It compares the actual saved fixture IDs/ranks/states/lines
to the engine results; do not generate that JSON from the submitted
write payload. Publication requires a real verified persistence receipt,
not simply the model response.

The refetched receipt must include `active_base_id`,
`method=INDEPENDENT_AIRTABLE_REFETCH`, original V4 `run_id`,
`rank_integrity_sha256`, `sweep_integrity_sha256`,
a truthful `readback_at_utc` within 30 minutes of ranking, and
`ranked_rows`. Every ranked row must contain
`coverage_id=<V4-run-id>|<match-id>`, original `match_id`,
`c_rank`, `c_board_state`, `c_supported_line`,
`c2_rank`, `c2_board_state`, `c2_supported_line` and official
`follow_lane`. This enforces stored official C FOLLOW/RESERVE/STOP
rather than guessing it from the C state or shadow C2 result.

## User-visible status output

Return quickly with `ACT / WAIT / PASS` ONLY when actual C/C2 evidence
supports such a football assessment. For incomplete coverage, show
`VERIFIED CANDIDATES` and `PENDING RESEARCH` instead of fake
bets or endless "resume" progress. Never claim runtime is in the
background: this is a current conversation execution.

Do not operate V1, V2 or V3. They remain disabled for audit.
