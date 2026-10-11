# Big Five goal-environment and team-intake research — 2026-10-11

**Status:** RESEARCH ONLY · no production intake, C/C2, odds, STEP0 freeze or official betting changes.
**Observation cut-off:** completed domestic league matches through **2026-10-10**; current season 2026/27.
**Research scope:** England Premier League, Spain La Liga, Italy Serie A, Germany Bundesliga, France Ligue 1.
**Source authority:** Third-party statistics are observational and never override AiScore fixture ID/KO, official provider status, fresh market quotes or verified XI channels.

## 1. League-level baseline

| Competition | Current FT matches | Goals/game | Current O2.5 | Current O3.5 | Completed 2025/26 O2.5 |
|---|---:|---:|---:|---:|---:|
| Bundesliga | 43 | 3.86 | 77% | 63% | 63.7% (306/306) |
| La Liga | 73 | 3.00 | 56% | 37% | 50.0% (380/380) |
| Serie A | 53 | 2.91 | 57% | 26% | 45.8% (380/380) |
| Ligue 1 | 51 | 2.88 | 61% | 35% | 52.6% (306/306) |
| Premier League | 56 | 2.88 | 54% | 34% | 55.0% (380/380) |

Current tables: [Bundesliga](https://compactstats.com/league/ger-bundesliga/), [La Liga](https://compactstats.com/league/esp-la-liga/), [Serie A](https://compactstats.com/league/ita-serie-a/), [Ligue 1](https://compactstats.com/league/fra-ligue-1/), [Premier League](https://compactstats.com/league/eng-premier-league/).
Completed-season counter-check: [eScored Big Five 2025/26](https://escored.com/features/which-football-leagues-have-the-most-goals-2025-26-ranked/).
Percentages are rounded by providers; samples are current as stated, NOT projected goals probabilities. Bundesliga has the clearest league-wide two-season strength. Italy's current increase needs to survive more rounds.

## 2. Teams to monitor first

**Reading key:** N = current completed league matches; GF:GA = actual team league goals scored/conceded; O2.5 and O3.5 are percentages of that team's finished league fixtures; BTTS = percentage with both teams scoring. The route class is a **screening hypothesis**, not proof of attacking mechanism. All current-season N are only 5–8.

### Bundesliga

| Club | N | GF:GA | Goals/game | O2.5 | O3.5 | BTTS | Research shape |
|---|---:|---:|---:|---:|---:|---:|---|
| Werder Bremen | 5 | 10:10 | 4.00 | 80% | 80% | 100% | TWO_SIDED_CANDIDATE |
| Augsburg | 5 | 13:8 | 4.20 | 100% | 80% | 80% | TWO_SIDED_CANDIDATE |
| Hoffenheim | 5 | 9:13 | 4.40 | 100% | 80% | 100% | LEAKAGE_AND_TWO_SIDED |
| Bayer Leverkusen | 5 | 14:8 | 4.40 | 80% | 80% | 60% | MIXED_UPPER_TAIL |
| Bayern Munich | 5 | 16:4 | 4.00 | 80% | 60% | 60% | STRONG_CARRIER_CHECK_OPPONENT |
| RB Leipzig | 5 | 15:5 | 4.00 | 80% | 60% | 20% | ONE_SIDED_CARRIER_CANDIDATE |
| Eintracht Frankfurt | 5 | 9:16 | 5.00 | 100% | 100% | 80% | EXTREME_TAIL_SENSITIVITY |

**Historical anchor:** Bayern 32/34 = 94% O2.5 in 2025/26; Dortmund 19/34 = 56% despite its present top-table standing ([WinDrawWin](https://www.windrawwin.com/statistics/over-under-25-goals/germany-bundesliga/2025-2026/)). Frankfurt's 0–6 loss to Leipzig on Oct 10 shows why to winsorize/extreme-result-check before making a fixture route claim.

### Premier League

| Club | N | GF:GA | Goals/game | O2.5 | O3.5 | BTTS | Research shape |
|---|---:|---:|---:|---:|---:|---:|---|
| Chelsea | 6 | 15:13 | 4.67 | 100% | 67% | 83% | TWO_SIDED_CANDIDATE |
| Newcastle | 5 | 9:9 | 3.60 | 80% | 60% | 80% | TWO_SIDED_CANDIDATE |
| Brighton | 6 | 18:5 | 3.83 | 67% | 50% | 33% | ONE_SIDED_CARRIER_CANDIDATE |
| Manchester City | 5 | 13:5 | 3.60 | 60% | 40% | 60% | CARRIER_WITH_LINE_RISK |
| Bournemouth | 6 | 7:13 | 3.33 | 67% | 50% | 83% | LEAKAGE_AND_TWO_SIDED |

**Cross-season:** Chelsea 25/38 = 66% and Newcastle 24/38 = 63% O2.5 in 2025/26, stronger than Brighton's 19/38 = 50% ([WinDrawWin](https://www.windrawwin.com/statistics/over-under-25-goals/england-premier-league/2025-2026/)). Do not infer Chelsea's 6/6 persists; goal-friendly does not mean every bet at the available line is attractive.

### La Liga

| Club | N | GF:GA | Goals/game | O2.5 | O3.5 | BTTS | Research shape |
|---|---:|---:|---:|---:|---:|---:|---|
| Barcelona | 8 | 34:7 | 5.13 | 88% | 75% | 50% | STRONG_CARRIER_HIGH_LINE_RISK |
| Villarreal | 8 | 13:13 | 3.25 | 75% | 63% | 75% | TWO_SIDED_CANDIDATE |
| Real Madrid | 8 | 19:8 | 3.38 | 75% | 50% | 63% | CARRIER_AND_SECOND_ROUTE_CHECK |
| Racing Santander | 7 | 11:21 | 4.57 | 86% | 71% | 71% | LARGE_OPPONENT_LEAKAGE |
| Elche | 7 | 11:17 | 4.00 | 71% | 71% | 86% | LARGE_OPPONENT_LEAKAGE |
| Atlético Madrid | 8 | 18:8 | 3.25 | 88% | 38% | 50% | O2.5_CONTEXT_NOT_AUTO_O3.5 |

**Cross-season:** Barcelona 28/38 = 74%, Villarreal 22/38 = 58%, Real Madrid 21/38 = 55% O2.5 in 2025/26. Real Betis currently has only 29% O2.5 and Getafe 25%; league-wide La Liga strength must not force their fixtures upward ([WinDrawWin](https://www.windrawwin.com/statistics/over-under-25-goals/spain-la-liga/2025-2026/)).

### Serie A

| Club | N | GF:GA | Goals/game | O2.5 | O3.5 | BTTS | Research shape |
|---|---:|---:|---:|---:|---:|---:|---|
| Inter | 6 | 18:8 | 4.33 | 83% | 67% | 67% | CARRIER_AND_SECOND_ROUTE_CHECK |
| Sassuolo | 5 | 9:9 | 3.60 | 100% | 40% | 100% | TWO_SIDED_O3.5_RECHECK |
| Monza | 5 | 8:12 | 4.00 | 80% | 60% | 100% | LEAKAGE_AND_TWO_SIDED |
| Roma | 5 | 14:3 | 3.40 | 80% | 60% | 40% | ONE_SIDED_CARRIER_CANDIDATE |
| Fiorentina | 6 | 7:14 | 3.50 | 83% | 33% | 67% | OPPONENT_LEAKAGE_NOT_CARRIER |

**Cross-season:** Inter 21/38 = 55% O2.5 in 2025/26 ([WinDrawWin](https://www.windrawwin.com/statistics/over-under-25-goals/italy-serie-a/2025-2026/)). Juventus, Cagliari and Bologna each have only 20% O2.5 in the present small sample. Avoid general Serie A promotion or a blanket 'big club' preference.

### Ligue 1

| Club | N | GF:GA | Goals/game | O2.5 | O3.5 | BTTS | Research shape |
|---|---:|---:|---:|---:|---:|---:|---|
| PSG | 6 | 11:8 | 3.17 | 83% | 50% | 83% | TWO_SIDED_CANDIDATE |
| Brest | 6 | 12:9 | 3.50 | 83% | 50% | 83% | TWO_SIDED_CANDIDATE |
| Lens | 6 | 11:10 | 3.50 | 83% | 33% | 83% | THIRD_GOAL_STALL_RECHECK |
| Strasbourg | 5 | 10:10 | 4.00 | 80% | 40% | 80% | TWO_SIDED_CANDIDATE |
| Rennes | 5 | 8:9 | 3.40 | 80% | 60% | 60% | MIXED_UPPER_TAIL |
| Le Mans | 6 | 10:12 | 3.67 | 83% | 67% | 100% | SMALL_SAMPLE_EARLY_SEASON |

**Cross-season:** Rennes 24/34 = 71%, Strasbourg 22/34 = 65%, Lens 22/34 = 65%, PSG 21/34 = 62% O2.5 in 2025/26 ([WinDrawWin](https://www.windrawwin.com/statistics/over-under-25-goals/france-ligue-1/2025-2026/)). Monaco currently has only 50% O2.5 and 17% O3.5 despite leading the table. Match form, not league position, is relevant.

## 3. Intake integration proposal — no production change yet

1. **Preserve Step0.** Every properly sourced Big Five senior fixture should remain eligible under normal league profile and existing source/operational gates. No matches excluded solely because team historical O2.5 is low; no fixture gets an A/B grade from this table. All standing country, friends, lower-division and tournament rules remain.
2. **Use as Step1 research watchlist, not automatic model ranks.** The current GOAL_FIRST_STEP1_RESEARCH_V1 already scores current source-backed last 4–10 games across the entire A/B queue. Do not replace these verified rolling samples with static team averages. During Step1 evidence collection, fetch high-priority team results early when the league fixture is in the frozen queue. Original source hash, fixture ranks and dispositions remain unchanged.
3. **Separate goal routes:** two-sided repeatable chance creation; dominant carrier and opponent leakage; late continuation after 1–0/1–1; 0–0/1–1 trap; extreme tails. Team O2.5, O3.5 and BTTS summary are diagnostic flags, not sufficient evidence to declare routes or executable odds.
4. **Do not overpay popular attacks.** For carrier sides with high market totals, preserve the model's true supported line and target threshold; do not invent a plausible wait to a distant line, do not claim a bet after goals occurred, and do not reuse historical market quote.
5. **Test forward:** freeze match-level sample and route prediction before kickoff; measure selected vs missed 3+/4+, false-positive 0–0/1–1, operational research completion, and actual availability of an actionable line. At least multiple slates before promoting any static fallback into code. Compare C and C2 independently.

## 4. Data cautions

- Early-season totals of 5–8 fixtures per team are high variance and some teams are newly promoted; old seasons may be from different divisions.
- Extreme results (Leipzig 6–0 Frankfurt; Chelsea 5–1 Bournemouth; Barcelona's heavy early scoring) can inflate apparent environment strength.
- Goal scoring/conceding numbers are not xG, shot quality or independent route verification.
- This file records **observed historical results**. Future fixture handling requires pre-kickoff-only snapshot, same-match ID, current XI/market evidence, tournament incentives and normal C/C2 gates.
- The Big Five are already in scope. The present task is research prioritization **within** scope, not league registry promotion or automatic inclusion of a team-based bet.
