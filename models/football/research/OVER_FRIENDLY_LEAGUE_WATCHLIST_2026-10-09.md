# Over-friendly League Watchlist — research-only v0.1

**Snapshot:** 2026-10-09 (ICT). **Status:** RESEARCH ONLY / NO AUTOMATIC ADMISSION OR RANKING. **Model:** Football C official, Football C2 shadow. **Repository:** acchtt/SlipTrace.

## Purpose and authority

This is the next step after identifying historically goal-heavy competitions: separate **league-level goal environment** from **match-level goal routes** (repeatable two-sided scoring versus one-sided mismatch or outlier-driven score totals).

**Do not** modify or override:
- the active `/sweep` launcher, its live checkpoint, exclusions, or required competition and women's top-flight discovery;
- the current `RESEARCHABLE_SENIOR_PRODUCTION` source → operational A/B/C/D → researchability → capacity sequence;
- the 15-fixture Work capacity cap, C/C2 selection, Step 2 current XI, tournament-incentive or Asian-market checks;
- explicit standing user exclusions (Israel, Kenya, Iraq, Wales, Kuwait *domestic* leagues and cups; **German 3. Liga only**) or existing verified model scopes.

League O2.5 rates **must never be substituted for fixture-specific evidence, market price, or an expected goals probability.** Historical results cannot create an operational Step 0 A/B grade. This file is not an admission registry; `FOOTBALL_LEAGUE_ENVIRONMENT_REGISTRY.md` contains **older narrow-core/hard-exclusion instructions that conflict with current `CURRENT_MODEL.md` and Step 0 launcher**. Do not reactivate its older production behavior merely because it names a league. If production integration is later proposed, reconcile the authority explicitly and require deliberate approval/QA before changing a single selection rule.

## A. Verified observational shortlist

All percentages below are **full-time Over 2.5**, from live third-party statistical snapshots; these snapshots have **different sample windows and update cadence**. Rounded figures are descriptive *observations*, not predicted probabilities or future fixture classifications. In particular the current 2026/27 season is early for European leagues. All tiers are **research priority only**.

| Research priority | Competition | Current season | Matches | O2.5 | Historical counter-check | Source |
|---|---|---|---:|---:|---|---|
| Historical core | Germany Bundesliga | 2026/27 | 36 | 77.8% | 2021/22–2025/26: 61.0% of 1,530 | S1, S2 |
| Historical core | Netherlands Eredivisie | 2026/27 | 63 | 76.2% | 2021/22–2025/26: 59.1% of 1,530 | S1, S2 |
| Current-season high | Switzerland Super League | 2026/27 | 54 | 77.8% | multi-year validation pending | S1 |
| Current-season high | Norway First Division / OBOS | 2026 | 191 | 71.2% | multi-year validation pending | S1 |
| Current-season high | Iceland Úrvalsdeild / Besta | 2026 | 144 | 70.1% | 72% BTTS of 144, distinct from O2.5 | S1, S4 |
| Current-season high | Netherlands Eerste Divisie | 2026/27 | 90 | 67.8% | 71% BTTS of 90; mandatory protected discovery remains | S1, S5 |
| Monitor only | Slovakia Super Liga | 2026/27 | 52 | 67.3% | multi-year validation pending | S1 |
| Monitor only | Germany 2. Bundesliga | 2026/27 | 54 | 64.8% | multi-year validation pending | S1 |
| Monitor only | Austria Bundesliga | 2026/27 | 42 | 64.3% | multi-year validation pending | S1 |
| Counterexample / monitor | England Championship | 2026/27 | 95 | 64.2% | 2021/22–2025/26: just 47.6% of 2,760; **do not infer enduring over environment** | S1, S2 |
| Baseline monitor | Norway Eliteserien | 2026 | 168 | 62% | second source agrees at ~62% and 3.16 goals/match | S3 |

**Important discrepancy:** the recent Bundesliga and Eredivisie observations (~78%/~76%) are *much higher* than their five-season O2.5 baselines (~61%/~59%). This is precisely why observed league goals should not alter model ranks. Another example is the Championship, where early 2026/27 ~64% conflicts with a five-season ~48% baseline. Compare the same league across comparable season windows before making claims of stable goal environment. If a data source changes (fixtures added, season switched), re-freeze the observation and denominator, not simply its headline percentage.

### Data source manifest (public, read-only)

- **S1**: https://nofluffpicks.com/statistics/over-25 — active/recent seasons, league rates and counts with minimum 30 games; read on 2026-10-09.
- **S2**: https://footinsights.com/blog/over-25-goals-rates-by-league/ — independently stated five-season results database and denominators, updated September 2026.
- **S3**: https://www.probettinghub.com/en-US/betting-stats/over-under/leagues/norway/eliteserien — 2026 Eliteserien rate and denominator.
- **S4**: https://footystats.org/iceland/urvalsdeild — Iceland 2026 goal count and BTTS.
- **S5**: https://footystats.org/netherlands/eerste-divisie — Eerste Divisie 2026/27 goals and BTTS.
- **S6**: https://footystats.org/netherlands/eredivisie — Eredivisie 2026/27 BTTS and scoreline frequency (a high league total alone is not a route).
- **S7**: https://www.footymetrics.com/stats-hub/best-leagues-for-over-25-goals — additional 2026/27 cross-check for Switzerland/Eredivisie/Eerste/2.Bundesliga; changed denominators possible.
- **S8**: https://footinsights.com/blog/over-under-25-goals-guide/ — O1.5/O2.5/O3.5 distribution rationale.
- **S9**: https://www.soccerwidow.com/football-gambling/betting-knowledge/over-2-5-goals-odds-epl-limited-history/ — pricing and sample-size caution.

These are third-party observational sources and are **not AiScore fixture identity or kickoff authorities**. For a production match, adhere to the active AiScore canonical fixture/time policy.

## B. Route-shape classification pilot

Classify **individual fixtures / measured competition scoreline samples**, not league names from O2.5% alone. Suggested flags and research hypotheses:

1. `BIDIRECTIONAL_CONTRIBUTION`: both teams are realistically capable of scoring; track *joint* BTTS ∩ Over 2.5 (1–2, 2–1, 2–2, etc.), each team's scoring probability/evidence and whether both contribute multiple chances. BTTS alone includes low-total 1–1 and **does not** establish O2.5.
2. `ONE_SIDED_CARRIER`: high match totals mainly arise from a dominant attack (3–0, 4–0, 4–1). Track winner goal share, clean-sheet rate of Over 2.5 fixtures, imbalance in shots/xG and opponent contribution. A prolific team is not proof it will cover a high Asian-total line.
3. `OUTLIER_TAIL`: league goals average inflated by unusual 5+, 6+ fixtures while most fixtures are lower total. Check median and central buckets, Over 3.5/4.5 share, top decile and opponent mismatch.
4. `LOW_GOAL_DRAW_TRAP`: one/both teams regularly produce 0–0, 1–0, or 1–1 despite superficially good O2.5 rate. Check low-total scorelines, draw utility/tournament incentives and whether 1–1 is a common terminal state.
5. `MIXED_OR_UNVERIFIED`: insufficient scoreline/home–away/current tactical evidence; **default rather than forcing a mechanism**.

*Do not assign definitive route tags at league level merely from an O2.5 and BTTS aggregate.* For example, high Icelandic or Eerste Divisie BTTS may justify examining bidirectional routes, but it does not prove every matchup is open. Routes must be supported by team-level form, current roster and chance-generation evidence.

## C. Pilot evaluation protocol (no production writes)

For each prioritized competition, build a **historical matched-sample** and **prospective read-only observation set** with:
- competition normalized key, season, number of verified FT games, source URL, frozen as-of date;
- O1.5, O2.5, O3.5 and O4.5 proportions and total goals distribution 0 / 1 / 2 / 3 / 4 / 5+;
- BTTS; `BTTS & O2.5` joint rate; of the Overs, 3+ goals by only one side versus both sides scoring;
- scoreline frequencies (0–0, 1–1, 2–1, 1–2, 2–2, 3–0, 0–3, 4–0, 0–4, 3–1, 1–3, high-tail 5+), team home/away splits;
- opening and closing Asian total line where **actual historical quotes are available**, do not substitute the over-2.5 rate or bookmaker closing line as an unbiased pre-match probability;
- team form and fixture-level route supporting evidence (pre-match only), fair-market vs model disagreements, missingness and source conflicts.

**Bias protection:** Freeze league environment with *only matches completed before the scored fixture*; prospective predictions must not use later scores, reclassified FT routes or future team sheets. Use a completed prior season as background with a prior-year sample before the current-season overlay. Backtest any hypothetical new feature out-of-time; report performance separately for `BIDIRECTIONAL`, `CARRIER`, `TRAP`, `MIXED`, and no-data, with C and C2 independently. Measure calibration, CLV where real quotes exist, route failures, opportunity cost, false positive 1–1/0–0 and actual executable line availability. Never select only winning overs in retrospective samples.

**No next-step gating modifications:** Do not raise A/B, circumvent C/D/researchability, favor one league in the mandatory operational 15-fixture queue, change tournament protection, auto-promote FOLLOW or suppress user-excluded leagues based on this pilot. Any potential ranking use is a *separate future proposal after prospective audit*, not activated here.

## D. Read-only next work units

1. Verify **prior completed season** and current-season match counts for the 6 first-pass leagues (Bundesliga, Eredivisie, Swiss Super League, Norway First Division, Iceland Úrvalsdeild, Eerste Divisie) using a consistent source/dataset, preserving unmatched records instead of imputing.
2. Calculate joint `BTTS & O2.5` and one-sided clean-sheet-Over fractions from individual canonical FT scorelines for those leagues, with denominator and as-of date. Aim to separate *mechanism* from volume.
3. Do a historical/prospective paper evaluation against actual C/C2 fixtures; do not silently reclassify incomplete exceptions or change outcomes.
4. Only after the evidence and sample-size audit, propose a small additive **research context flag** at Step 1 (not Step 0); leave its weight at zero unless separately approved.

**Current sweep:** `SWEEP-20261009-1300-20261010-0300` remains **PAUSED BY USER**, persisted RUNNING Chunk 12, three pending blocks; do not resume or mutate its Airtable checkpoint because of this watchlist.
