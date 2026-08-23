# Dota 2 Current Session Authority Lock

**Status:** ACTIVE

- `status: ACTIVE`
- `slate_id: TI15_2026-08-23_FINAL_DAY`
- `authority_epoch: 2`
- `effective_date_utc7: 2026-08-23`
- `authority_commit: f618a07ae859fad08dd4aeac493ccf2d5329448a`
- `active_model: Dota 2 v0.1.0-experimental`
- `circuit_breaker_state: CLEAR`
- `pregame_execution_scope: Match Moneyline / Match Handicap (series map handicap)`
- `pregame_window: pre-ban/pick and pre-Map-1; sportsbook Live/In Play label alone is not disqualifying`
- `live_execution_scope: governed by frozen live rules after first draft action or Map 1 start`
- `actual_exposure: 0u`
- `default_simulated_stake: 0.25u`
- `relock_reason: user clarified that sportsbook may label the event Live before the game and ban/pick have started`

## Frozen authority rule

For this slate, all analytical/procedural authority files must resolve from frozen commit `f618a07ae859fad08dd4aeac493ccf2d5329448a`.

Default-branch edits after this lock activation are pending and do not enter the current authority epoch unless the user explicitly authorizes another relock/new authority epoch.

Pregame TAKEs are executable in shadow mode only when all frozen pregame gates pass. A sportsbook or feed `Live` / `In Play` label does not by itself terminate pregame eligibility while the state is still clearly pre-ban/pick and Map 1 has not started. Pregame eligibility ends at the first draft action or Map 1 start, whichever occurs first. Greyed, suspended, stale, or materially changed prices remain non-executable.

Live TAKEs remain subject to the frozen live gates and require synchronized live evidence when an executable live market is available.