# /xi

> **One-command /xi:** Assess C + C2 immediately; use supplied verified odds automatically where eligible, otherwise deliver the football read without requesting more quotes. See `models/football/procedures/FOOTBALL_SIMPLE_ASSESS_AND_BET.md`.

> **Active model Airtable route (Oct 11):** Load `models/football/airtable/ACTIVE_MODEL_ROUTING.md` and `ACTIVE_MODEL_ROUTING.json`. All model, accounting and reporting reads/writes go to `appbzxqXYf0lKfD4P` using the corresponding NEW table IDs and source-key readback. Do not use old-base IDs for writes. **Do not modify `/sweep` routing, source checkpoint or Step0 handoff.** Actual Bets are only from confirmed user slips; C official, C2 shadow.

Short wrapper only.

On **every invocation**, re-read `models/football/procedures/FOOTBALL_HANDOFF_FRESHNESS_BOOTSTRAP.md`, `models/football/CURRENT_MODEL.md`, `models/football/prompts/COMMAND_ALIASES.md`, and `models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md` from current repository authority before using prior-chat launcher text.

Run the single /xi flow in `models/football/procedures/FOOTBALL_SIMPLE_ASSESS_AND_BET.md`. Never require a second /bet command. With a genuinely current quote already in evidence, include an authorized price comparison automatically; without it, finish the football assessment immediately.

Use supplied XI/score/football and any actual quoted line/odds as evidence. Do NOT ask for odds just to assess. Market screenshots permit evaluating only actual, current and independently verified prices under strict executable-bet safeguards. Preserve exception wording exactly.

Every material XI result must expose the current authority revision/runtime status and the required OFFICIAL C + SHADOW C2 visibility defined by the launcher.

This wrapper does not redefine Step 2.
