# /live

> **User-facing default:** ASSESS C+C2 without mandatory bookmaker odds for /xi and /live. Evaluate an already-supplied live screenshot in the SAME command as fixed price evidence without searching for replacement odds. Current V4 has no deterministic live priced-action engine, so live odds permit burden comparison only and never authorize exposure. Do not require /bet or another screenshot. Authority: `models/football/procedures/FOOTBALL_SIMPLE_ASSESS_AND_BET.md`.

> **Active model Airtable route (Oct 11):** Load `models/football/airtable/ACTIVE_MODEL_ROUTING.md` and `ACTIVE_MODEL_ROUTING.json`. All model, accounting and reporting reads/writes go to `appbzxqXYf0lKfD4P` using the corresponding NEW table IDs and source-key readback. Do not use old-base IDs for writes. **Do not modify `/sweep` routing, source checkpoint or Step0 handoff.** Actual Bets are only from confirmed user slips; C official, C2 shadow.

Short wrapper only.

Read `models/football/procedures/FOOTBALL_SIMPLE_ASSESS_AND_BET.md` first. `/live` shares `/xi`'s one-command football-first behavior; evaluate supplied current live odds if available, never request quotes merely to assess. Then read `models/football/procedures/FOOTBALL_HANDOFF_FRESHNESS_BOOTSTRAP.md`, `models/football/CURRENT_MODEL.md`, `models/football/procedures/FOOTBALL_SIMPLE_ASSESS_AND_BET.md`, and `models/football/prompts/COMMAND_ALIASES.md`; execute the live launcher in default ASSESS mode (no odds). Do not require /bet to evaluate user-provided fixed screenshot evidence. Current V4 live pricing is comparison-only; no executable live priced action is available until a separately implemented/tested live engine is promoted.

Use available score/minute and football events. Never ask for odds just to assess, even after kickoff. Preserve exception wording exactly.

Do not require or request provider live-stat telemetry (shots, xG, big chances, dangerous attacks, possession, corners, box entries, momentum) before assessment.

This wrapper does not redefine live rules.
