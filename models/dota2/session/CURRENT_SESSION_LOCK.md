# Dota 2 Current Session Authority Lock

**Status:** ACTIVE

- `status: ACTIVE`
- `slate_id: TI15_2026-08-23_FINAL_DAY`
- `effective_date_utc7: 2026-08-23`
- `authority_commit: e21510e8d38618a389b6366b7f9650a8b61c2c55`
- `active_model: Dota 2 v0.1.0-experimental`
- `circuit_breaker_state: CLEAR`
- `pregame_execution_scope: Match Moneyline / Match Handicap (series map handicap)`
- `live_execution_scope: governed by frozen live rules when executable live betting is available`
- `actual_exposure: 0u`
- `default_simulated_stake: 0.25u`

## Frozen authority rule

For this slate, all analytical/procedural authority files must resolve from frozen commit `e21510e8d38618a389b6366b7f9650a8b61c2c55`.

Default-branch edits after this lock activation are pending and do not enter the current authority epoch unless the user explicitly authorizes a relock/new authority epoch.

Pregame TAKEs are executable in shadow mode only when all frozen pregame gates pass. A pregame price that is stale, suspended, materially changed, or already live is non-executable.

Live TAKEs remain subject to the frozen live gates and require synchronized live evidence when an executable live market is available.