# /live

> **Active model Airtable route (Oct 11):** Load `models/football/airtable/ACTIVE_MODEL_ROUTING.md` and `ACTIVE_MODEL_ROUTING.json`. All model, accounting and reporting reads/writes go to `appbzxqXYf0lKfD4P` using the corresponding NEW table IDs and source-key readback. Do not use old-base IDs for writes. **Do not modify `/sweep` routing, source checkpoint or Step0 handoff.** Actual Bets are only from confirmed user slips; C official, C2 shadow.

Short wrapper only.

Read `models/football/procedures/FOOTBALL_HANDOFF_FRESHNESS_BOOTSTRAP.md`, `models/football/CURRENT_MODEL.md`, and `models/football/prompts/COMMAND_ALIASES.md`, then execute `models/football/prompts/03_NORMAL_CHAT_LIVE.md` faithfully.

Use same-message score/minute/odds or other concrete live-state text/screenshots as the current epoch. Preserve explicit exception wording exactly.

Do not require or request provider live-stat telemetry (shots, xG, big chances, dangerous attacks, possession, corners, box entries, momentum) before assessment.

This wrapper does not redefine live rules.
