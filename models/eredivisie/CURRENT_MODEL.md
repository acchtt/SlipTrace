# Current Eredivisie Model

**Canonical namespace:** `models/eredivisie/`

- Active model: **Eredivisie v0.1**
- Status: **independent shadow-calibration model**
- Scope: **Netherlands Eredivisie only**
- Parent methodology: SlipTrace Football v0.2.41, frozen at repository commit `dd5d32a24b624ab32e4b7175e572ade5e26f2a8d`
- Parent football CURRENT_MODEL latest commit at fork: `d13f03e25911e81ae5e9cd0a2d4394d4d0df06d6`
- Parent football CURRENT_MODEL blob SHA at fork: `0dd7e754366dc41f7b66917d0b46d281ce49f435`
- Fork date: 2026-08-09

## Core principle

**Same SlipTrace football decision process; narrower Eredivisie-specific calibration.**

The Eredivisie model is a fork, not a live child of the general football model. It inherits the parent football methodology at the frozen parent commit above, then evolves independently. Later changes to `models/football/` do **not** automatically apply here. A parent change must be explicitly reviewed and selectively merged into `models/eredivisie/`.

## Required load order

1. `models/eredivisie/FORK_MANIFEST.md`
2. At frozen parent ref `dd5d32a24b624ab32e4b7175e572ade5e26f2a8d`, load the inherited football methodology identified by the fork manifest.
3. `models/eredivisie/rules/MODEL_RULES_EREDIVISIE_V0.1.md`
4. `models/eredivisie/procedures/EREDIVISIE_PRE_VERDICT_VALIDATOR.md`
5. `models/eredivisie/calibration/EREDIVISIE_50_MATCH_PROTOCOL.md`
6. `models/eredivisie/airtable/EREDIVISIE_DECISION_STATE_AIRTABLE.md`
7. `models/eredivisie/PROJECT_BOOTSTRAP.md` when starting or transferring a chat/project.

Local Eredivisie rules override inherited parent rules only where they explicitly conflict. Otherwise the frozen parent methodology remains in force.

## What is inherited

The fork inherits the parent decision skeleton, including:

- synchronized state and exact match identity;
- score/minute/market/settlement verification;
- reset epochs after goals, penalties, red cards, halftime, substitution clusters, major injuries, tactical changes, weather/pitch changes and other material events;
- competition-format and result-utility analysis;
- lineup/personnel and opponent-adjusted team-strength decomposition;
- market-family scan and one-best-expression discipline;
- exact Asian-handicap and quarter-line settlement analysis;
- separation of win probability from margin probability;
- xG/xGOT as secondary diagnostics only;
- multiple independent forward-looking evidence channels;
- correlated-evidence control;
- goal-environment classification and post-reset `Unresolved` state;
- persistence requirements for directional/regime changes;
- favourite-fade and protected-underdog burden controls;
- no automatic opposite-side confirmation when one thesis fails;
- hard pre-verdict validation and structured decision-state write lock;
- post-match separation of process validity from result variance.

## What is NOT inherited as operating state

The Eredivisie model does **not** inherit the parent model's:

- current four-match football circuit-breaker count;
- current general-football shadow positions;
- official/open football positions;
- ledger/accounting state;
- match-specific current scores or recommendations;
- competition-specific priors from Leagues Cup, ASEAN, cups, internationals or other leagues.

Those may be reviewed as historical lessons, but they are not Eredivisie calibration observations.

## Eredivisie operating values

- 1u = 1,000,000 VND
- Minimum accepted odds = 1.70
- Qualified shadow selection stake = exactly 0.25u = 250,000 VND simulated
- Initial mode = **shadow only**
- Allowed positive selection label = `SHADOW LEAN — DO NOT PLACE`
- Other verdicts = `NO BET — HOLD` or `NO BET`
- No real-money official recommendation until the user explicitly activates official execution after a calibration review
- One best expression per reassessment
- Every material assessment must include `Assessment period: ...`
- Every material assessment, including NO BET/HOLD, must be written to the Eredivisie Airtable control base when available
- A positive shadow selection requires `Validator Result = PASS` before it is emitted
- If Airtable validation is unavailable, return `NO BET — HOLD — decision-state validation unavailable`

## League scope

Calibration universe: Dutch Eredivisie only.

Do not mix KNVB Cup, UEFA competitions, friendlies, Eerste Divisie, reserve/youth football or internationals into Eredivisie league priors. Such matches may inform lineup/tactical context when relevant, but must remain separately labeled and excluded from league calibration aggregates.

## Development policy

- Eredivisie versions progress independently: v0.1, v0.2, v0.3, etc.
- Do not create a new rule merely because one shadow bet loses.
- First classify whether a failure was missing-rule, application/enforcement, calibration, margin, favourite bias, underdog bias, xG misuse, reset/persistence, lineup, tactical, settlement, market-selection, execution, or normal variance.
- Prefer repeated evidence over single-match hindsight.
- Parent-football changes after the fork require explicit merge review; never inherit them silently.

## Initial calibration target

Record at least **50 properly assessed Eredivisie matches**, including NO BET decisions, before making strong performance claims. Measure market-family results, closing-line value, favourite/underdog splits, handicap depth, home/away, prematch/live, score state, entry minute and promoted-team subsets.
