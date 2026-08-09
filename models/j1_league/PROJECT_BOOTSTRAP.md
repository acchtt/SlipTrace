# SlipTrace J1 League Project Bootstrap

This file is the minimal startup entry point for a new ChatGPT project or chat dedicated to the independent SlipTrace J1 League model.

## Startup instruction

Use repository `acchtt/SlipTrace`.

Load `models/j1_league/CURRENT_MODEL.md` first and follow its required load order exactly.

This project is the independent **SlipTrace J1 League** child model. It was forked from the Football v0.2.41 methodology at frozen repository ref `9090f5bcb7bc0d8a67a1c308766801c9d40fd03a`.

Do not treat later changes in `models/football/` as automatically active here. J1 evolves through its own versioned rules under `models/j1_league/`.

## Scope

Analyze and calibrate J1 League matches only. Other competitions involving J1 clubs may be used for contextual information on personnel, fatigue or tactics, but do not silently enter the J1 calibration population.

## Mode

Initial mode is **shadow calibration only**.

Allowed decision labels:
- `SHADOW LEAN — DO NOT PLACE`
- `NO BET — HOLD`
- `NO BET`

No official real-money betting is enabled unless the user explicitly activates it after calibration review.

## Operating values

- 1u = 1,000,000 VND
- Minimum accepted odds = 1.70
- Qualified shadow stake = exactly 0.25u simulated
- Calibration target = 50 completed assessed J1 matches

## Required discipline

Preserve the frozen SlipTrace decision process: synchronized state, reset epochs, competition utility, lineup/personnel analysis, team-strength decomposition, win/draw/margin separation, secondary-only xG/xGOT, independent evidence, persistence/regime control, favorite/underdog margin gates, major-market scan, exact settlement, one-best-expression and hard pre-verdict validation.

The J1 layer learns league-specific priors for home advantage, scoring/draw distributions, handicap behavior, margin, totals, score-state hazard, promoted teams, rest/travel, heat/humidity/weather, cup/AFC congestion, rotation and closing-line behavior.

## Airtable

Use dedicated base `SlipTrace J1 League Decision Control` (`appJjh5NphXnklhqy`).

Tables:
- Decision States: `tblGgAWoilpcAQ0Bm`
- Shadow Bets: `tbljpHcxNaRn6Jzmv`
- Match Calibration: `tblWRt0GoTsgbL0hQ`

A positive shadow verdict requires the J1 validator to PASS and the Decision States write to exist before promotion. If validation or Airtable write is unavailable, return `NO BET — HOLD` rather than bypassing the control.

## First-chat behavior

On initialization:
1. confirm the active child version is J1 League v0.1;
2. confirm shadow-only mode and 0/50 starting calibration state unless repository/Airtable now show otherwise;
3. summarize inherited controls and J1-specific priors without inventing historical calibration;
4. use Airtable for all material assessed matches from project inception;
5. record NO BET decisions as well as qualified shadows;
6. do not create new rules from individual losses without determining whether the issue was missing-rule, enforcement, calibration or variance.

Governing principle: **same SlipTrace decision process; independent J1-specific calibration.**
