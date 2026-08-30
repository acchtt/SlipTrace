# LoL v1.3 Team Benchmark — Gol.gg League-Relative Strength Construction — 2026-08-30

**Status:** ACTIVE WHEN DECLARED BY `CURRENT_MODEL.md`  
**Purpose:** construct the pre-series Moneyline team-strength tier `K` from reproducible, price-independent team data instead of loose subjective benchmarking.

---

# 1. Source and freeze point

Primary statistical source: **Games of Legends / gol.gg team tournament tables**.

For each professional series, freeze the benchmark immediately before Game 1 using only information that existed before the series started.

Forbidden inputs:
- sportsbook odds or implied probabilities;
- current-series map results;
- current-map state;
- hindsight from later series outcomes.

If gol.gg is unavailable or the relevant tournament table is materially incomplete, use `HOLD` for benchmark certification until a reliable equivalent source is available. Do not silently substitute market price.

---

# 2. Peer set

Standardize every metric within the **same current league/tournament peer set**.

Examples:
- LEC Summer teams are standardized against the other LEC Summer teams;
- LCK Playoffs teams use the applicable current LCK competitive peer set;
- do not compare raw LEC values directly with raw LCK values.

Use population z-scores across the peer set:

`z(x_team) = (x_team - league_mean) / league_population_sd`

If a metric has zero variance or is unavailable for a material share of the peer set, omit that metric and renormalize the remaining weights proportionally.

---

# 3. Split benchmark score

For each team and tournament split, calculate:

`TOWER_DIFF = Towers killed per game - Towers lost per game`

Then:

`B_split = 0.30*z(WinRate) + 0.30*z(GDM) + 0.20*z(GD@15) + 0.10*z(TOWER_DIFF) + 0.05*z(DRA%) + 0.05*z(NASH%)`

Interpretation:
- WinRate: realized map-level success;
- GDM: full-game resource superiority/deficit;
- GD@15: early-state strength independent of final result;
- TOWER_DIFF: repeatable structural conversion;
- DRA% and NASH%: lower-weight objective-control confirmation.

Do not add KDA, DPM or raw kills to the core score during the frozen validation epoch. They are more style-sensitive and would materially double-count resource/fight dominance already represented by WinRate/GDM/GD@15.

---

# 4. Current / previous split blend

Let `G` be current-split games played before the series.

Use:

- `G >= 15`: `B_raw = 0.70*B_current + 0.30*B_previous`
- `8 <= G <= 14`: `B_raw = 0.55*B_current + 0.45*B_previous`
- `G < 8`: `B_raw = 0.40*B_current + 0.60*B_previous`

If no directly comparable previous split exists, use the current split alone once `G >= 8`; with fewer than 8 current games and no comparable prior, benchmark confidence is insufficient for a certified `K=±2` unless explicit governance authorizes an alternative historical window.

### Roster continuity adjustment

Previous-split weight is only valid when the team retains meaningful competitive continuity.

- no decision-critical roster change: use the normal blend above;
- one material starter/role change: halve the previous-split weight and transfer the removed weight to current split;
- two or more material starter/role changes or a major role-system rebuild: previous split is descriptive context only; benchmark from current split and use `K=±2` only when current sample is at least 15 games and the gap clears the threshold.

This adjustment must be determined without sportsbook input.

---

# 5. Re-standardize blended benchmark

After every team in the peer set has a `B_raw`, standardize the blended scores again:

`B = z(B_raw)`

This makes the final team benchmark explicitly league-relative and lets pairwise gaps use a consistent unit.

For teams A and B:

`GAP = B(A) - B(B)`

---

# 6. Convert benchmark gap to K

From Team A perspective:

- `|GAP| < 0.50` -> `K=0`
- `0.50 <= |GAP| < 1.25` -> `K=sign(GAP)*1`
- `|GAP| >= 1.25` -> `K=sign(GAP)*2`

Therefore:
- `K=±1` = meaningful but moderate league-relative strength gap;
- `K=±2` = clear major persistent strength gap supported by the benchmark.

`P0(A)=50%+5*K pp` remains unchanged under v1.3.

The benchmark determines `K`; bookmaker favoritism does not.

---

# 7. Pre-series benchmark record

Before the first model-certified live Moneyline decision of a series, preserve:

`TEAM_BENCH[LEAGUE=...;CURRENT=...;PREVIOUS=...;G=...;B_CUR_A=...;B_CUR_B=...;B_PREV_A=...;B_PREV_B=...;BLEND_A=...;BLEND_B=...;B_A=...;B_B=...;GAP=...;K_A=...;K_B=...;ROSTER_ADJ=...;PRICE_USED=N]`

Round only for display; use full available precision for classification.

---

# 8. TH vs MKOI worked calibration example

Using the gol.gg LEC 2026 Summer team table available before the Aug 30 TH vs MKOI series and the LEC 2026 Spring table:

Current Summer core inputs included:
- MKOI: 20 games, 40.0% WinRate, GDM -21, GD@15 +912, Towers 5.6-6.5, DRA% 56.3, NASH% 43.3;
- TH: 17 games, 23.5% WinRate, GDM -176, GD@15 -1262, Towers 3.5-7.8, DRA% 40.0, NASH% 25.0.

League-relative split scores under this formula:
- `B_current(MKOI) ≈ +0.018`
- `B_current(TH) ≈ -1.355`

Spring split scores:
- `B_previous(MKOI) ≈ +0.758`
- `B_previous(TH) ≈ -1.696`

Both had at least 15 current-split games, so the 70/30 blend gives:
- `B_raw(MKOI) ≈ +0.240`
- `B_raw(TH) ≈ -1.457`

After re-standardizing all LEC blended scores:
- `B(MKOI) ≈ +0.262`
- `B(TH) ≈ -1.590`
- pairwise `GAP ≈ +1.852 SD` from MKOI perspective.

Therefore the benchmark classifies:
- `MKOI K=+2 / P0=60%`
- `TH K=-2 / P0=40%`

This example is a prospective calibration demonstration of the benchmark construction. It does not retroactively rewrite already accepted historical positions.

---

# 9. Governance

- freeze benchmark before Game 1;
- same-series results never change `K`;
- price never changes `K`;
- normal one-map win/loss never changes benchmark weights;
- changes to metrics, weights, sample blending or K thresholds require explicit model authorization and a new authority lock;
- preserve the source snapshot/date or enough source values to reconstruct the classification.
