# Current J1 League Model

**Canonical namespace:** `models/j1_league/`

- Active model: **J1 League v0.1**
- Parent methodology: SlipTrace Football v0.2.41
- Frozen parent repository ref: `9090f5bcb7bc0d8a67a1c308766801c9d40fd03a`
- Scope: Japan J1 League matches only
- Mode: shadow calibration only
- Calibration target: 50 completed assessed matches before strong performance claims

## Required load order

1. `models/j1_league/FORK_MANIFEST.md`
2. Frozen parent files from ref `9090f5bcb7bc0d8a67a1c308766801c9d40fd03a` in the Football v0.2.41 load order
3. `models/j1_league/rules/MODEL_RULES_J1_LEAGUE_V0.1.md`
4. `models/j1_league/procedures/J1_PRE_VERDICT_VALIDATOR.md`
5. `models/j1_league/calibration/J1_50_MATCH_PROTOCOL.md`
6. `models/j1_league/airtable/J1_AIRTABLE.md`
7. `models/j1_league/PROJECT_BOOTSTRAP.md`

Do not treat `models/football/` as a live parent after the fork. Later football-model changes are not inherited automatically. They may be selectively merged only after explicit review and a child-model version change.

## Inherited core skeleton

Preserve synchronized score/minute/market state; reset epochs; competition utility; lineup/personnel analysis; opponent-adjusted strength decomposition; win/draw/margin separation; xG/xGOT as secondary diagnostics; independent forward-looking evidence; persistence/regime controls; favorite/underdog margin gates; major-market scan; exact AH/totals settlement; one-best-expression; hard pre-verdict validation; structured decision-state logging; and post-match process review.

## J1 calibration layer

Learn and track, where data quality permits: home-field effect; home/away scoring/conceding; favorite performance by handicap band; favorite 2+ margin frequency; protected-underdog cover rates; draw frequency; totals by closing line; first-/second-half scoring; goal hazard by minute and score state; comeback and late-goal frequency; promoted-team behavior; red-card effects; goalkeeper/lineup effects; rest-day asymmetry; domestic travel; summer heat/humidity/weather; congestion from Emperor's Cup, J.League Cup and AFC competition; and closing-line value.

J2, J3, cups, continental matches, reserve/youth matches and friendlies are not part of the J1 calibration population. They may be contextual evidence only when relevant.

## Operating values

- 1u = 1,000,000 VND
- Minimum accepted odds = 1.70
- Qualified shadow stake = exactly 0.25u simulated
- Positive verdict = `SHADOW LEAN — DO NOT PLACE`
- Other verdicts = `NO BET — HOLD` or `NO BET`
- No official real-money recommendation until explicitly activated after calibration review
- Every material assessment includes `Assessment period: ...`
- Prematch previews include relevant home/away form and low-weight H2H; ordinary live reassessments do not repeat them

## Hard write lock

Before any `SHADOW LEAN — DO NOT PLACE`:
1. run the J1 validator;
2. create/update a Decision States record;
3. require `Validator Result = PASS`;
4. create the corresponding Shadow Bets record.

If Airtable validation is unavailable, output `NO BET — HOLD — decision-state validation unavailable`.

## Airtable

Base: `SlipTrace J1 League Decision Control`
Base ID: `appJjh5NphXnklhqy`

Tables:
- Decision States: `tblGgAWoilpcAQ0Bm`
- Shadow Bets: `tbljpHcxNaRn6Jzmv`
- Match Calibration: `tblWRt0GoTsgbL0hQ`

## Calibration state

- Model: J1 League v0.1
- Assessed matches: 0/50
- Shadow bets: 0
- Official betting: disabled
