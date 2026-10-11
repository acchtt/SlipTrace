# Step0 / Step1 retirement — 2026-10-11

## User authority

User instruction: **"scrap current sweep and rank now."**

Production status: `SWEEP_RANK_RETIRED`.
Retired command families: `/sweep` (including resume, repair, fresh,
and direct launchers), `/rank` (including reassess and previously
attached ZIPs), and V1/V2/V3 Step0-to-Step1 coordinator paths.

This is a decommission, **not** a deletion of historical evidence.
The old stages are inactive even when referenced in older user chats,
Work handoffs, GitHub branches or attached ZIPs.

## What was disabled

- Current command router and both normal production launchers.
- Unified V3 coordinator's executable CLI.
- Standalone official Step0 final ZIP packager's executable CLI.
- Portable Step0 runnable CLI (its immutable pure regression source
  remains importable for QA).
- Paired Step1 board CLI and Step1 official Airtable rank readback CLI.
- Auto-promotion of a prepared queue or old blocked sweep to any
  current official C FOLLOW/RESERVE/STOP board.

Existing library-level validators remain importable only to audit or
unit-test original historical contracts. Do not use pure functions as
a back door to authorize a new official board.

## Latest active Airtable review

Active base: `appbzxqXYf0lKfD4P`.
At retirement review there were **zero RUNNING sweeps**.
Recent runs `SWEEP-20261011-2316-20261012-0300`,
`SWEEP-20261011-2249-20261012-0300`,
`SWEEP-20261011-2200-20261012-0300` were already BLOCKED;
older incomplete runs were ABANDONED or BLOCKED.
Existing COMPLETE history remains COMPLETE. No active Sweep Runs
records were mutated or backfilled to create retrospective decisions.

Historical base `appWyZJjitSBATXAU` stays read-only.
No Airtable Daily Coverage, Decision States, Website Picks, Actual Bets,
C2 shadow results, archived source ZIPs or user financial records
were deleted, restarted or converted to official bets.

## What stays active

- Football C official model and Football C2 independent shadow.
- Single `/xi` / `/xi exception` football assessment.
- `/live`, `/audit`, `/report` and actual-bets accounting.
- Existing historical QA, source evidence, model specifications,
  fixtures and read-only settlement/audit support.

No executable odds or betting advice is produced from retired
Step0/Step1 artifacts.

## Rebuild preconditions

A replacement is NOT started or approved by this retirement action.
It requires an explicit user instruction. Before reactivating any
production fixture selection or board publication: define the new
discovery/ranking contract, tests, source and Airtable schemas,
full end-to-end live verification, and an explicit reviewed replacement
of `sweep_rank_retired.py`. Do not silently revert the tombstone flag
or copy old launchers from earlier GitHub history.

Previous production main before decommission:
`88b138bb9b0f27e6f0c10fd93fc77598a535b5e8`.
