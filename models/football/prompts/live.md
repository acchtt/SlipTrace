# /live

> **User-facing default:** ASSESS C+C2 without bookmaker odds for /xi and /live. Price check only if explicitly requested (/bet). Authority: `models/football/procedures/FOOTBALL_SIMPLE_ASSESS_AND_BET.md`. Older contradictory priced-step instructions apply ONLY to explicit BET CHECK.

> **Active model Airtable route (Oct 11):** Load `models/football/airtable/ACTIVE_MODEL_ROUTING.md` and `ACTIVE_MODEL_ROUTING.json`. All model, accounting and reporting reads/writes go to `appbzxqXYf0lKfD4P` using the corresponding NEW table IDs and source-key readback. Do not use old-base IDs for writes. **Do not modify `/sweep` routing, source checkpoint or Step0 handoff.** Actual Bets are only from confirmed user slips; C official, C2 shadow.

Short wrapper only.

Read `models/football/procedures/FOOTBALL_HANDOFF_FRESHNESS_BOOTSTRAP.md`, `models/football/CURRENT_MODEL.md`, `models/football/procedures/FOOTBALL_SIMPLE_ASSESS_AND_BET.md`, and `models/football/prompts/COMMAND_ALIASES.md`; execute the live launcher in default ASSESS mode (no odds). Only explicit /bet requests start priced checks.

Use available score/minute and football events. Never ask for odds just to assess, even after kickoff. Preserve exception wording exactly.

Do not require or request provider live-stat telemetry (shots, xG, big chances, dangerous attacks, possession, corners, box entries, momentum) before assessment.

This wrapper does not redefine live rules.
