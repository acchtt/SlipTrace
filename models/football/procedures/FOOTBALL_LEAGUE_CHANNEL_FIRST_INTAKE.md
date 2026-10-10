# League-channel-first Step 0 admission — v1

**Effective:** new sweeps after merge only. `strict_intake_policy=LEAGUE_CHANNEL_FIRST_V1`.

## Intent

Stop researching the current bookmaker total and each team's previous/current
lineup channel **for every fixture** in a verified professional league. Step 0
should establish that a league's publication ecosystem works, once per
competition/season/source refresh, then cheaply classify all in-window fixtures
using verified identities, kickoff times, user scope and existing operational
quality/competition-reliability gates.

**Tier 1 is a data-coverage designation, NOT an automatic bet, goal signal,
A grade or exemption from a user league exclusion.** Source-backed channel
availability is not an executable market. Do not invent odds, XI or price
timestamps to make a fixture look researched.

## Deterministic profile contract

One real provider-verified league profile can be attached unchanged to multiple
in-window fixture rows and persisted once in the competition block's evidence
manifest. Each admitted/deferred row references the frozen same profile and
carries `intake_evidence_scope=LEAGUE_CHANNEL_ONLY`.

Example **shape only** (URLs and dates below are placeholders; replace with
actually visited/confirmed sources, never claim the example is verified):

```json
{
  "strict_intake_policy": "LEAGUE_CHANNEL_FIRST_V1",
  "competition_name": "Premier League",
  "intake_evidence_scope": "LEAGUE_CHANNEL_ONLY",
  "league_channel_profile": {
    "competition_name": "Premier League",
    "profile_type": "TIER1_STANDARD",
    "season": "2026/27",
    "coverage_status": "VERIFIED_CHANNELS",
    "evidence_checked_at_utc": "2026-10-09T12:00:00Z",
    "evidence_basis": "Recent league-level verified XI, bookmaker Asian totals and news publication channels",
    "xi_provider_url": "https://provider.example.org/league-xi",
    "asian_total_provider_url": "https://book.example.org/league-odds",
    "team_news_provider_url": "https://news.example.org/league"
  }
}
```

The profile must be dated within 30 days before kickoff, match the actual
fixture's competition, show working credible HTTPS source channels, and
record the current competition season. A generic league fixture schedule
alone is **not** proof of an Asian-total sportsbook feed or lineup channel.
It must be independently source-backed. No per-fixture offered line, price,
bookmaker timestamp or confirmed starting XI is required **at Step 0**.

For `TIER1_STANDARD`, the code only allows explicitly named Tier 1 coverage
competitions in `sweep_intake_evidence.TIER1_CHANNEL_LEAGUES`. Do not
self-declare obscure cups, unknown competitions or unlisted leagues Tier 1.
For `PROVEN_LEAGUE`, require evidence of **at least two** league fixtures
with real published XI and independently observed Asian totals in the current
ecosystem; fill `recent_xi_fixture_count` and
`recent_asian_total_fixture_count` from genuine evidence. This includes
credible women's top flights and approved professional lower divisions where
the proof exists. Absent evidence means no league-first queue admission;
use the existing bounded exclusion/hold process or explicit user exception,
never a guessed market quote.

For each fixture still require:
- canonical fixture ID and independently verified timezone-aware UTC kickoff;
- in-window, prematch and currently permitted senior competition/scope;
- legitimate A/B grade after actual competition reliability cap, not
  inferred from Tier 1;
- `xi_expected=YES` or conditional `UNCERTAIN` only with B;
- `market_observability=HIGH/MEDIUM` and
  `team_news_observability=HIGH/MEDIUM` explicitly understood as
  **league-channel expected coverage**, not observed match quotations;
- a near-kickoff `xi_recheck_due_utc` 30–180 min before KO;
- source-backed profile and per-fixture reasons.

All hard exclusions, friendlies, league registry/user bans, identity/time
conflicts, protected/women required manifests and finite source retries
remain unchanged. Full A/B queue is retained, with 8 initial Work fixtures
and standard/adaptive replenishment policy unchanged.

## Step 01 /rank — mandatory fixture-specific discovery

On receipt of a new league-first handoff, **do not interpret the league
profile as a current bookmaker line or an XI confirmation**. Before C/C2
predictive scoring for each candidate, Work must:
1. retrieve the real fixture's identity/KO again and actual current teams,
   formation/news/absences from credible sources;
2. locate a match-specific Asian total with real bookmaker, `match_id`,
   quoted line, source URL and observation time (<=72h pre-KO); record
   `MARKET_SOURCE_NOT_AVAILABLE` if unable;
3. verify actual two-sided lineup publication channels/starting XI state,
   retaining `UNCERTAIN` when XI is not released;
4. serialize the original `XI_MARKET_FIRST_V1` fixture evidence contract
   and run the existing strict `validate_work_candidate` on it;
5. run both C official/C2 shadow only after that check passes. If fixture
   proof is missing or the market is stale, classify `STEP1_RESEARCH_BLOCKED`
   and continue ordered replenishment without a model claim; do not send an
   unverified bet, wait or supported line to /xi.

Step 02 /xi still requires current confirmed XI checks and executable Asian
total quote, completion/burden funding and paired model execution.

## Existing runs and accountability

The policy is **new and explicit**. A previously saved RUNNING cursor using
`XI_MARKET_FIRST_V1` must not be silently converted, including the
`SWEEP-20261010-0743-20261010-1500` diagnostic run. Its original source
hash, prior grades, admissions and blockers remain intact unless the user
separately authorizes a prospective repair.

Add a separate note in final sweep package distinguishing
`LEAGUE_CHANNEL_ONLY` fixtures from fixtures that already possess
`MATCH_SPECIFIC` quote evidence. Never present league-only proof as a
quote, stake, BET or guaranteed availability.
