# Football Website Picks Airtable Contract

**Status:** ACTIVE OFFICIAL EXPOSURE PERSISTENCE  
**Table:** `Website Picks` — `tblg3J5sbJYbzuTYD`  
**Official model:** Football C

Website Picks stores operational direct C-BET exposure and assumed/reconciled C-WAIT exposure.

Read with:
- `models/football/procedures/FOOTBALL_MODEL_BET_ACCOUNTING.md`;
- `models/football/procedures/FOOTBALL_WAIT_ASSUMED_EXPOSURE.md`.

**C-WATCH accounting does not create a Website Pick.** WATCH is model-performance accounting only and is stored in Daily Coverage/all-model accounting fields.

## Core fields

Existing exposure fields:
- `Pick ID` — `fld7LY4str9QmzCH9`
- `Match` — `fldNlufM7FENbNCv9`
- `Competition` — `fldpafuuHIiTQbpAb`
- `Kickoff` — `fld84SN2UVzuNdLO4`
- `Model Version` — `fld1oC1qxmmjdFtnz`
- `Verdict` — `fldgZWuLj8OlyB0u9`
- `Line` — `fld46kN7xgx0OGvx6`
- `Odds` — `fldtzi2BMboY8jglO`
- `Stake u` — `fldPSXw2Q425CsAoc`
- `Result` — `fldmsREbwEsW8DdmY`
- `P/L u` — `fldz0sSos3hFkGstN`
- `Recorded At` — `fld7b20x4LTZIa9On`
- `Website Fixture ID` — `fld5dRrLR4qn3hIM8`
- `Reason` — `fldnmTTgsZMuj0ENW`

WAIT accounting fields:
- `Origin C Action` — `fldavEJERSgbRphZP`
- `Exposure Basis` — `fldMXXFFBRvvP8oY0`
- `WAIT Resolution` — `fldqiojwbqh9YbjpE`
- `WAIT Target Line` — `fldevFLmEr1Ph329Q`
- `WAIT Min Odds` — `fldbi330Zr4hQXVkO`
- `Actual User Bet Confirmed` — `fldhM8zTAAd9kBB27`
- `Actual User Line` — `fldOOiyQy5cnQbIB4`
- `Actual User Odds` — `fldzXHyrSYBDGLZPh`
- `Actual User Stake u` — `fldoGOSn1im61Snuu`
- `WAIT Reconciliation Note` — `fldg6Px4yir0BYc7W`

## WATCH boundary

C-WATCH, C2-WATCH, C3-WATCH and C4-WATCH may count as model-accounting bets, but none creates a Website Pick solely because it is WATCH.

C2/C3/C4 never create Website Picks.

## Direct C-BET mapping

For C-BET:
- Origin C Action = `C-BET`
- Exposure Basis = `DIRECT_BET`
- WAIT Resolution = `NOT_APPLICABLE`
- Line/Odds = exact direct decision quote
- Stake u = official model stake
- Result = `PENDING` until settlement
- WAIT Target/Min fields blank

## C-WAIT initial mapping

Immediately when C-WAIT is issued:
- Origin C Action = `C-WAIT`
- Exposure Basis = `WAIT_ASSUMED`
- WAIT Resolution = `ASSUMED_REACHED`
- WAIT Target Line = deterministic frozen target
- WAIT Min Odds = deterministic frozen minimum odds
- Line = WAIT Target Line
- Odds = WAIT Min Odds
- Stake u = 1.0 unless explicitly different
- Result = `PENDING`
- Actual User Bet Confirmed = false

This record is an official **model-accounting exposure**, even before the line is independently observed later.

## User-confirmed reconciliation

When the user supplies a corresponding actual bet:
- keep Origin C Action = `C-WAIT`
- keep original WAIT Target Line / WAIT Min Odds
- Exposure Basis = `WAIT_USER_CONFIRMED`
- WAIT Resolution = `USER_CONFIRMED`
- Actual User Bet Confirmed = true
- store exact Actual User Line/Odds/Stake
- update primary Line/Odds/Stake to the exact corresponding actual execution for reconciled model exposure
- preserve the original target/minimum in their dedicated fields

Do not create a second duplicate Website Pick for the same model WAIT.

## Explicit line-never-reached reconciliation

Only when the user explicitly says the target line never reached:
- keep Origin C Action = `C-WAIT`
- Exposure Basis = `WAIT_NOT_REACHED`
- WAIT Resolution = `USER_DECLARED_NOT_REACHED`
- preserve WAIT Target Line / WAIT Min Odds
- Result = `VOID`
- P/L u = 0
- Actual User Bet Confirmed remains false unless separate execution evidence exists

This record remains as an audit trail but is excluded from official model exposure/P&L.

## Non-triggering evidence

Do not change WAIT_ASSUMED because:
- no slip is provided;
- later market history is incomplete;
- live screenshots show another line;
- the line is not independently reconstructed;
- the user says they personally skipped the bet without saying the target line never reached.

## Duplicate key

Use the normal canonical fixture identity plus model epoch/action to reconcile the same pick.

A user-confirmed WAIT update must mutate the existing WAIT pick rather than append a second exposure row.
