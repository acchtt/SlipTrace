# /sweep

Short wrapper only.

Read `models/football/procedures/FOOTBALL_HANDOFF_FRESHNESS_BOOTSTRAP.md`, `models/football/CURRENT_MODEL.md`, and `models/football/prompts/COMMAND_ALIASES.md`.

If the preserved user arguments begin with `repair`, also read and apply `models/football/procedures/FOOTBALL_SWEEP_REPAIR_MODE.md` **before** executing Step 0. Repair mode overrides the normal fresh-discovery loop where the repair procedure says to reuse persisted state.

Otherwise execute `models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md` normally.

Preserve all user text after `/sweep` as the requested sweep-window/instructions and use same-message attachments as inputs.

This wrapper does not redefine Step 0.
