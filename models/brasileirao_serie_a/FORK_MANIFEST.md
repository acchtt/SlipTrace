# Brazilian Serie A Fork Manifest

## Fork identity

- Child model: **Brazilian Serie A v0.1**
- Parent model: **SlipTrace Football v0.2.41**
- Frozen parent repository ref: `9090f5bcb7bc0d8a67a1c308766801c9d40fd03a`
- Fork date: 2026-08-09
- Child namespace: `models/brasileirao_serie_a/`

## Fork principle

The child inherits the parent football reasoning skeleton once, then evolves independently.

Future changes under `models/football/` do not automatically modify the Brazilian Serie A model. Any parent improvement must be reviewed for league relevance, documented, and merged through an explicit Brazilian Serie A model version.

## Frozen parent load order

At the fork ref, load the Football v0.2.41 methodology in this order:

1. `models/football/ORGANIZED_FILE_LOADING_GUIDE.md`
2. `models/LEGACY_MODEL_CHANGELOG.md` retained football baseline only
3. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
4. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE_ADDENDUM_2026-08-01.md`
5. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.5.md` through `MODEL_RULES_FOOTBALL_V0.2.41.md` in ascending order
6. `models/football/procedures/FOOTBALL_PRE_VERDICT_VALIDATOR.md`

Child files loaded later override parent conflicts.

## Inherited methodology, not inherited calibration

Inherited unchanged at fork:

- synchronization and reset-state handling;
- lineup and tactical analysis;
- score/result/margin utility separation;
- evidence hierarchy and xG/xGOT restrictions;
- market-family comparison;
- settlement/event-budget analysis;
- persistence and regime controls;
- deep-favorite and protected-underdog gates;
- one-best-expression;
- decision-first response format;
- pre-verdict hard validation;
- process-versus-outcome review discipline.

Not inherited as permanent priors:

- generic scoring assumptions;
- cross-competition home advantage;
- generic favorite margin assumptions;
- generic underdog cover assumptions;
- generic goal hazard;
- competition-specific motivation structures.

These must be calibrated from Brazilian Serie A observations and external historical league data when reliably sourced.

## Child-specific environment

Brazilian Serie A requires explicit attention to:

- large domestic travel distances;
- climate and venue differences;
- compressed calendars;
- midweek Copa Libertadores/Sudamericana/Copa do Brasil involvement;
- rest-day asymmetry and rotation;
- promoted-team adaptation;
- home/away performance splits;
- price behavior in lower-total environments when observed rather than assumed.

These factors are context channels, not automatic betting signals. They must alter the actual probability thesis to matter.

## Isolation rule

Only Brazilian Serie A league matches enter the core child calibration sample.

Do not mix Copa do Brasil, state championships, Libertadores, Sudamericana, Serie B, friendlies, youth/reserve matches or international fixtures into the league calibration population.
