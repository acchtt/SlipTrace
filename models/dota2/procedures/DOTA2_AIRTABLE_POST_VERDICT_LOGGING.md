# Dota 2 Airtable Post-Verdict Logging Integrity

**Status:** ACTIVE GOVERNANCE  
**Authority:** `models/dota2/CURRENT_MODEL.md`

## Purpose

Keep the Dota 2 live ledger synchronized with visible shadow-audit decisions without delaying live verdicts.

## 1. Verdict first

On an active map:

1. execute the full applicable analysis internally;
2. output the visible verdict first;
3. only then use Airtable;
4. do not let logging or web research delay the verdict.

## 2. Mandatory snapshot logging

After every valid live verdict:

- ensure the current `Maps` record exists;
- create the current `Snapshots` record;
- persist the exact synchronized state used by the verdict;
- persist the quoted live line/price used by the verdict;
- persist the visible verdict text;
- for executable TAKE only, create the exact shadow `Positions` record.

HOLD/PASS creates no Position.

## 3. Minimum verification fields

Read back the expected record and verify, as available:

- Map ID;
- clock;
- Radiant/Dire orientation;
- kills;
- net-worth lead;
- tower/barracks state;
- Roshan/Aegis state when material;
- buyback/high-ground state when material;
- exact quoted live market(s);
- verdict;
- for TAKE: market family, selection, odds, simulated stake, actual exposure.

Do not claim `logged` or `verified` until this read-back matches.

## 4. Missing-log recovery

Backfill only from the original synchronized evidence and original visible verdict. Preserve the original clock, line, state, and verdict.

- Never turn a historical HOLD/PASS into a Position.
- Never invent a TAKE, odds, timestamp, result, or state field that was not available originally.
- If an already-issued valid TAKE failed to write, restore only that exact historical shadow Position after verifying the original evidence.

## 5. Discarded verdicts

If a material fight, Roshan event, high-ground breach, barracks loss, buyback sequence, or price move invalidates the state while a verdict is being formed and the verdict is discarded:

- do not create a Position from it;
- do not log it as the valid decision snapshot;
- reassess only from a fresh synchronized state.

## 6. Finals

On a user-confirmed final:

1. settle all open Positions from that map;
2. update winner, duration, final kills, and status in `Maps`;
3. verify settlement and final map records.

Do not overwrite historical entry evidence during settlement.

## 7. Separation of authority

Airtable is the canonical live ledger, not the analytical rulebook. A logging failure must not change thresholds, add unwritten confirmation gates, or mutate GitHub authority.