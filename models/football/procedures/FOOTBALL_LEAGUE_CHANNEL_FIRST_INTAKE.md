> **V4 AUTHORITY NOTICE (2026-10-12):** This document contains historical V1–V3 or Football A operational instructions. Its legacy `ACTIVE` labels, Step0/Step1 capacity limits, AiScore-only rules, pre-XI fixture-specific odds/lineup blockers and old-model claims do **not** govern current `/sweep` or `/rank`. Canonical replacement: `models/football/stages_v4/SWEEP.md` and `RANK.md`; current C/C2 authority: `CURRENT_MODEL.md`. Only football safety guidance explicitly imported by those V4 launchers remains applicable. Historical receipts remain immutable.

# League-channel-first Step 0 admission — v1

**Effective:** new sweeps after merge only. `strict_intake_policy=LEAGUE_CHANNEL_FIRST_V1`.

## Intent

Stop researching the current bookmaker total and each team's previous/current
lineup channel **for every fixture** in a verified professional league. For
registered Tier-1 country+league pairs, standard lineup and Asian-total
availability is an **expected operational property**, not a historical-proof
blocker at Step 0. Non-Tier-1 leagues still need a genuine league-season
publication profile. All fixtures still require verified identities, kickoff
times, user scope and existing operational quality/reliability gates.

**Tier 1 is a data-coverage designation, NOT an automatic bet, goal signal,
A grade or exemption from a user league exclusion.** Source-backed channel
availability is not an executable market. Do not invent odds, XI or price
timestamps to make a fixture look researched.

## Deterministic profile contract

For `PROVEN_LEAGUE`, a genuinely verified league-season profile must be
attached unchanged to every candidate from the same league. For registered
`TIER1_STANDARD` country+league pairs, the profile is **optional** in new
prospective Step0 sweeps: the exact code registration establishes expected
publication availability, so no historic XI fixtures, Asian-total markets,
provider URLs or 30-day attestation timestamp are needed. If profiles are
supplied, contradictory fixture-by-fixture profiles are still rejected.
Every A/B candidate must carry `intake_evidence_scope=LEAGUE_CHANNEL_ONLY`.
Never mislabel inferred standard availability as `VERIFIED_CHANNELS`.

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

The example above is a fully evidenced profile shape, **not** mandatory for
registered Tier-1 competitions. For other leagues, a profile must be dated
within 30 days before kickoff, match the competition and season and show
working credible HTTPS lineup, Asian-total and team-news source channels.
A generic fixture schedule alone does not establish a bookmaker or XI feed.
No per-fixture executable line, price, book timestamp or confirmed XI is
required **at Step 0** for either profile type.

The Tier-1 bypass is allowed only for precise **country + competition** pairs
in `sweep_intake_evidence.TIER1_STANDARD_COUNTRY_LEAGUES`, and only in the
new prospective `LEAGUE_CHANNEL_FIRST_V1` Step0 path. Generic words such as
“Premier League,” “Bundesliga” or “Serie A” from another country are not Tier-1.
No self-declared label, missing country, cup, women/youth league, or lower
professional division receives this bypass.
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
- competition-official fixture source and per-fixture operational reasons;
  `PROVEN_LEAGUE` also requires its historic source-backed profile.

All hard exclusions, friendlies, league registry/user bans, identity/time
conflicts, protected/women required manifests and finite source retries
remain unchanged. Full A/B queue is retained, with 8 initial Work fixtures
and standard/adaptive replenishment policy unchanged.

## 2026-10-11 second-division pilot gate — future Step0 only

Norway **OBOS-ligaen / 1. divisjon** is also NORMAL/direct to *operational screening* for prospective new sweeps, not automatic Work readiness or Tier1. Require season-specific `PROVEN_LEAGUE` evidence of two different games with confirmed home/away XIs and two different games with genuinely observed Asian total ladders. Revisit the evidence URLs and time, retain raw identity/kickoff, news and pre-KO XI recheck; do not reuse a cached old bookmaker quote. Source examples: `models/football/research/OBOS_LEAGUE_CHANNEL_PROOF_2026-10-11.md`. Ranheim and any other team's historical Over frequency is a research lead, not an intake prediction or promised market price.

German **2. Bundesliga** is newly NORMAL/direct to *operational screening*, not automatic Work readiness. Use `PROVEN_LEAGUE`, not `TIER1_STANDARD`. Two+ genuine recent previous fixture XI publications and two+ independent Asian-total fixture observations are required for its reusable league/season profile. Do not invent source evidence or current quotes.

Hong Kong **senior Premier League** and Malaysia **senior Liga Super** are new source-local CONDITIONAL pilots for future /sweep, never Tier1 or unconditional A/B. Season-correct PROVEN_LEAGUE needs two completed senior fixture XIs and two actual Asian total fixture markets; each in-window fixture adds `asia_topflight_recent_goal_evidence` with 3–5 unique past completed competitive games per side, observed <=7 days pre-KO, goals for/against and independently checked HTTPS sources. Require either credible two-sided or carrier routes, rejecting repeated 0–0/1–1 and <=2 goal stalls; do not use static JDT/Lee Man/Kitchee bonuses or create executable quote values. See `research/HONG_KONG_MALAYSIA_SOURCE_PILOT_2026-10-11.md`.

Poland **Ekstraklasa** remains CONDITIONAL and gains one source-local FAST_PRODUCTION scan, not automatic full-league coverage. Every qualifying fixture requires country Poland, both teams' historical actual `poland_ekstraklasa_recent_goal_evidence`, five verified competitive past games each with fixture ID/kickoff/score and HTTPS source captured within seven days prior KO. Reject three or more 0-0/1-1 traps or four <=2-goal stalls on either side, or absent combined five-match route support. Require normal PROVEN_LEAGUE (two actual past XI and Asian-total publication examples), A/B viability, fixture identity/KO and independent match-specific /rank and /xi evidence. See `research/POLAND_EKSTRAKLASA_CONDITIONAL_PILOT_2026-10-11.md`.

English **Championship** is selectively CONDITIONAL and must also use `PROVEN_LEAGUE`. The special `championship_recent_goal_evidence` fixture payload must include `captured_at_utc`, and `home`/`away` each with `source_url` and `recent_competitive_matches` (five objects with `match_id`, `kickoff_utc`, `goals_for`, `goals_against`, `competitive: true`). Every recorded match precedes the candidate's kickoff and capture epoch. Captured evidence must be within seven days before KO. Reject repeated or insufficient history, either side with three 0-0/1-1s or four low-total <=2 matches, and fixtures failing the cheap O2.5/average gate from the league registry. This enforces research suitability **only**, not model predictions. In FAST_PRODUCTION, inspect the Championship only once at source block level and avoid full per-fixture lineup/market searches before this cheap gate. Every eligible fixture *also* must pass the normal A/B and league-profile evidence validators.

No additional automatic second-tier admissions: Spain Segunda, Italy Serie B, France Ligue 2 remain research/explicit-exception only. Germany 3. Liga remains excluded. Existing/frozen runs retain old classification and source hashes.

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
4. bind the researched match-specific data to the exact frozen Step0
   fixture (match ID, league, UTC kickoff, original A/B grade and exclusions),
   serialize `{"source_intake_policy":"LEAGUE_CHANNEL_FIRST_V1",
   "frozen_step0_candidate":{...},"researched_fixture":{...}}`, and run
   `python models/football/engine/step1_fixture_intake_cli.py --input <file.json>`;
   it executes the original `XI_MARKET_FIRST_V1` strict check for real
   bookmaker/line/timestamp, XI channels and news before C/C2 scoring;
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
