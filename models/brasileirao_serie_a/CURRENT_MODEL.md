# Current Brazilian Serie A Model

**Canonical namespace:** `models/brasileirao_serie_a/`

- Active model: **Brazilian Serie A v0.1**
- Parent methodology: SlipTrace Football v0.2.41
- Frozen parent repository ref: `9090f5bcb7bc0d8a67a1c308766801c9d40fd03a`
- Scope: Campeonato Brasileiro Serie A league matches only
- Mode: shadow calibration only
- Calibration target: 50 completed assessed matches before strong performance claims

## Required load order

1. `models/brasileirao_serie_a/FORK_MANIFEST.md`
2. Frozen parent files from ref `9090f5bcb7bc0d8a67a1c308766801c9d40fd03a` in the Football v0.2.41 load order
3. `models/brasileirao_serie_a/rules/MODEL_RULES_BRASILEIRAO_SERIE_A_V0.1.md`
4. `models/brasileirao_serie_a/procedures/BRASILEIRAO_PRE_VERDICT_VALIDATOR.md`
5. `models/brasileirao_serie_a/calibration/BRASILEIRAO_50_MATCH_PROTOCOL.md`
6. `models/brasileirao_serie_a/airtable/BRASILEIRAO_AIRTABLE.md`
7. `models/brasileirao_serie_a/PROJECT_BOOTSTRAP.md` for cross-chat startup behavior

Do not treat `models/football/` as a live parent after the fork. Later football-model changes are not inherited automatically. They may be selectively merged only after an explicit review and child-model version change.

## Inherited core skeleton

The child preserves the parent process for:

- synchronized score/minute/market state;
- reset epochs after goals, penalties, cards, substitutions, injuries, halftime, tactical/weather/pitch changes;
- competition/result utility;
- lineup/personnel analysis;
- opponent-adjusted team-strength decomposition;
- win/draw/margin separation;
- xG/xGOT as secondary-only diagnostics;
- independent forward-looking evidence and correlated-evidence control;
- persistence/regime controls;
- favorite/underdog margin gates;
- major-market scan;
- exact Asian-handicap and total settlement;
- one-best-expression;
- hard pre-verdict validation;
- structured decision-state logging and post-match process review.

## Brazilian Serie A calibration layer

League-specific probability formation must learn and track, where data quality permits:

- home-field effect;
- home/away scoring and conceding distributions;
- favorite performance by handicap band;
- favorite 2+ margin frequency;
- protected-underdog cover rates;
- draw frequency;
- totals by closing line;
- first-half/second-half scoring;
- goal hazard by minute and score state;
- comeback and late-goal frequency;
- promoted-team behavior;
- red-card effects;
- goalkeeper and lineup effects;
- rest-day asymmetry;
- long-travel and climate context;
- fixture congestion from Libertadores/Sudamericana/Copa do Brasil participation;
- market movement and closing-line value.

Cup, continental, state-league, Serie B, reserve/youth and friendly matches are not part of the Serie A calibration population. They may be used only as contextual evidence for personnel, fatigue or tactics when relevant.

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

1. run the Brazilian Serie A validator;
2. create/update a Decision States record;
3. require `Validator Result = PASS`;
4. create a corresponding Shadow Bets record.

If Airtable validation is unavailable, output `NO BET — HOLD — decision-state validation unavailable`.

## Airtable

Base: `SlipTrace Brazilian Serie A Decision Control`
Base ID: `appsqiBbCMEKKLqgG`

Tables:
- Decision States: `tblrTzhQhW6CND7SE`
- Shadow Bets: `tbl8qeAvOeDjvZAr6`
- Match Calibration: `tblYVM3KHohv4oVHL`

## Calibration state

- Model: Brazilian Serie A v0.1
- Assessed matches: 0/50
- Shadow bets: 0
- Official betting: disabled
