> **Live Airtable routing effective 2026-10-11:** base `appbzxqXYf0lKfD4P`, new operational table/field IDs below. Original base `appWyZJjitSBATXAU` remains read-only historical archive. For full 368-field translation consult [ACTIVE_BASE_ROUTING_20261011.md](ACTIVE_BASE_ROUTING_20261011.md). Do not write to archive.\n\n# Football Competition Reliability — Airtable Contract

**Status:** ACTIVE  
**Base:** `SlipTrace Football Decision Control`  
**Base ID:** `appbzxqXYf0lKfD4P`

## Tables

### Competition Reliability

Table ID: `tbl8ZRExZfMce7lqY`

One summary row per normalized competition. This is the Step-0 persistent operational-memory read surface.

Required fields:

- Competition Key
- Competition
- Reliability State
- Rolling Sample
- XI Usable %
- Market Usable %
- Team News Usable %
- Step2 Completion %
- Identity Time Faults
- Consecutive Critical Failures
- Last Observed At
- State Reason
- Manual Override
- Updated At

### Competition Reliability Events

Table ID: `tblg3uz2Bvz6bcCm9`

Append-only operational observations.

Required fields:

- Event ID
- Competition Key
- Competition
- Observed At
- Board ID
- Match
- Observation Type
- Preflight Grade
- XI Outcome
- Market Outcome
- Team News Outcome
- Identity Time Outcome
- Step2 Outcome
- Critical Failure
- Failure Classes
- Notes

No final score, goals, settlement, model result, or P/L field belongs in this table.

## Daily Coverage Ledger additions

The existing `Daily Coverage Ledger` now also carries:

- Operational Grade
- XI Expected
- Team News Observability
- Competition Reliability State
- Competition Reliability Reason
- Operational Disposition

`Market Status` remains the fixture-level market status surface.

These fields preserve the Step-0 snapshot. Later audit updates to competition reliability do not rewrite the historical fixture snapshot.

## Sweep Runs additions

The existing `Sweep Runs` table now carries:

- Operational Excluded Count
- Researchability Excluded Count
- Capacity Deferred Count

These counts make the new Step-0 funnel durable across chat resumptions.

## Write ownership

- Step 0 reads Competition Reliability and writes the Daily Coverage snapshot.
- Step 2 records decision-state execution truth as before.
- Post-slate audit owns canonical Competition Reliability Events and recomputes/upserts Competition Reliability summary rows.
- Manual Override changes require an explicit user/maintainer instruction.

Use the rules in:
`models/football/procedures/FOOTBALL_COMPETITION_RELIABILITY_MEMORY.md`
