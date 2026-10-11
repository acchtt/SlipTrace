# /xi

> **User-facing default:** ASSESS C+C2 without bookmaker odds for /xi and /live. Price check only if explicitly requested (/bet). Authority: `models/football/procedures/FOOTBALL_SIMPLE_ASSESS_AND_BET.md`. Older contradictory priced-step instructions apply ONLY to explicit BET CHECK.

> **Active model Airtable route (Oct 11):** Load `models/football/airtable/ACTIVE_MODEL_ROUTING.md` and `ACTIVE_MODEL_ROUTING.json`. All model, accounting and reporting reads/writes go to `appbzxqXYf0lKfD4P` using the corresponding NEW table IDs and source-key readback. Do not use old-base IDs for writes. **Do not modify `/sweep` routing, source checkpoint or Step0 handoff.** Actual Bets are only from confirmed user slips; C official, C2 shadow.

Short wrapper only.

On **every invocation**, re-read `models/football/procedures/FOOTBALL_HANDOFF_FRESHNESS_BOOTSTRAP.md`, `models/football/CURRENT_MODEL.md`, `models/football/prompts/COMMAND_ALIASES.md`, and `models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md` from current repository authority before using prior-chat launcher text.

Execute ASSESS (default, no odds) using the current XI launcher and the priority contract models/football/procedures/FOOTBALL_SIMPLE_ASSESS_AND_BET.md. Only explicit /bet or /xi bet requests execute a priced check.

Use any supplied XI/score/football context as evidence. Do NOT ask for odds to assess, even before or after kickoff; supplied market screenshots do not automatically trigger BET CHECK. Preserve exception wording exactly.

Every material XI result must expose the current authority revision/runtime status and the required OFFICIAL C + SHADOW C2 visibility defined by the launcher.

This wrapper does not redefine Step 2.
