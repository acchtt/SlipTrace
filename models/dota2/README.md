# SlipTrace Dota 2 Shadow Audit

This namespace is an independent Dota 2 live/shadow decision-control project modeled on the operational architecture of the LoL project, not on its game-specific analytical rules.

## Canonical architecture

- **GitHub:** model, rules, procedures, authority lock, saved context, handoffs, reviews.
- **Airtable:** mutable live map/snapshot/position/roster ledger.
- **Web:** patch, roster, schedule, team-context and calibration research when needed.
- **Optional Calendar / automations:** slate reminders, patch/roster checks and review cadence; never a substitute for synchronized live evidence.

## Start every new Dota 2 chat with

1. `models/dota2/CURRENT_MODEL.md`
2. `models/dota2/procedures/DOTA2_SESSION_BOOTSTRAP.md`
3. follow the exact load order in `CURRENT_MODEL.md`
4. load the latest applicable handoff last

If live evidence arrives before bootstrap is complete, visible status must be:

`MODEL NOT LOADED — HOLD`

before any connector call.

## Current model

`Dota 2 v0.1.0-experimental` — shadow only.

Initial market families:

- Moneyline
- Kill Handicap
- Total Kills
- Duration

Pregame TAKEs are disabled during calibration.

## Airtable

Canonical base: **SlipTrace Dota 2 Live Tracker** (`appoyQ7VAvJcUVJo2`)

Tables:

- Maps
- Snapshots
- Positions
- Rosters

Dota-specific snapshot fields include Roshan/Aegis, buybacks, barracks, high-ground state, net-worth lead, and patch-dependent objectives in addition to kills/clock/price.

## Recommended namespace growth

As evidence accumulates, add:

- `models/dota2/context/` — patch notes, roster cards, tournament formats, team-specific durable context
- `models/dota2/handoffs/` — state transfer between chats
- `models/dota2/reviews/` — postgame mechanism audits
- `models/dota2/procedures/` — narrowly scoped execution controls discovered through review
- `models/dota2/rules/` — versioned analytical rules only when explicitly promoted

Do not create a new analytical version from a single result. Prefer mechanism-specific reviews, then promote only validated changes through `CURRENT_MODEL.md`.