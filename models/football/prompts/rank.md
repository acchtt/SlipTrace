# /rank

> **Active model Airtable route (Oct 11):** Load `models/football/airtable/ACTIVE_MODEL_ROUTING.md` and `ACTIVE_MODEL_ROUTING.json`. All model, accounting and reporting reads/writes go to `appbzxqXYf0lKfD4P` using the corresponding NEW table IDs and source-key readback. Do not use old-base IDs for writes. **Do not modify `/sweep` routing, source checkpoint or Step0 handoff.** Actual Bets are only from confirmed user slips; C official, C2 shadow.

Short wrapper only.

Read `models/football/procedures/FOOTBALL_HANDOFF_FRESHNESS_BOOTSTRAP.md`, `models/football/CURRENT_MODEL.md`, `models/football/prompts/COMMAND_ALIASES.md`, and `models/football/procedures/FOOTBALL_REPAIRED_HANDOFF_AUTHORITY.md`, then execute `models/football/prompts/01_WORK_DAILY_SWEEP.md` faithfully.

If the user attached a completed repaired sweep, validate and accept that repaired handoff before any web research. Do not re-run fixture discovery, kickoff verification, or Step-0 repair in /rank.

Use the attached/current canonical AiScore handoff as input. Preserve any text after `/rank` as instructions.

This wrapper does not redefine Step 1.
