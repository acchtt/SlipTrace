> **Live Airtable routing effective 2026-10-11:** base `appbzxqXYf0lKfD4P`, new operational table/field IDs below. Original base `appWyZJjitSBATXAU` remains read-only historical archive. For full 368-field translation consult [ACTIVE_BASE_ROUTING_20261011.md](ACTIVE_BASE_ROUTING_20261011.md). Do not write to archive.\n\n# Football Website Picks Airtable Contract

**Status:** ACTIVE OFFICIAL EXPOSURE PERSISTENCE  
**Table:** `Website Picks` — `tblmGd7XwTYbceIiL`  
**Official model:** Football C

Website Picks stores operational direct C-BET exposure and assumed/reconciled C-WAIT exposure.

Read with:
- `models/football/procedures/FOOTBALL_MODEL_BET_ACCOUNTING.md`;
- `models/football/procedures/FOOTBALL_WAIT_ASSUMED_EXPOSURE.md`.

**C-WATCH accounting does not create a Website Pick.** WATCH is model-performance accounting only and is stored in Daily Coverage/all-model accounting fields.

## Core fields

Existing exposure fields:
- `Pick ID` — `fldEWkeb0WFpip8GF`
- `Match` — `fldaiHxfruUQpCefB`
- `Competition` — `fldkyImhXXDKNrSIR`
- `Kickoff` — `fldC0minlbWHOcICV`
- `Model Version` — `fldIJ7A3ia0ZxxcNE`
- `Verdict` — `fldc5murMqOjjjXcT`
- `Line` — `fldI8UHVmq6UyeLG8`
- `Odds` — `fldms9tWXWymeHgyS`
- `Stake u` — `fldFAEU7RHado60iL`
- `Result` — `fldCR2S5GkpJFK3sI`
- `P/L u` — `fldWUDBX7dcLcP9nR`
- `Recorded At` — `fldhIPj5xB9dXDYtR`
- `Website Fixture ID` — `fldnqWZX8SAFjgaO7`
- `Reason` — `fldWI4SSDf8It1QTd`

WAIT accounting fields:
- `Origin C Action` — `fldzjvFazOh88SpZY`
- `Exposure Basis` — `fldbh2WqfxySRWQQS`
- `WAIT Resolution` — `fldQUjmGojpLHpeGD`
- `WAIT Target Line` — `fldURFVzxquJb4ian`
- `WAIT Min Odds` — `fldcPT6SwPS0NmY2M`
- `Actual User Bet Confirmed` — `fldnRSvpH7krGX5xv`
- `Actual User Line` — `fld0GaiOJAzMSZwGz`
- `Actual User Odds` — `fldsRxQtOrlRC3JLI`
- `Actual User Stake u` — `fld4WOTeczJxPmIaU`
- `WAIT Reconciliation Note` — `flddQ9W1lxt5jFp0F`

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
