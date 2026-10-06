# /sweep

Short wrapper only.

Read `models/football/procedures/FOOTBALL_HANDOFF_FRESHNESS_BOOTSTRAP.md`, `models/football/CURRENT_MODEL.md`, and `models/football/prompts/COMMAND_ALIASES.md`.

Always read and apply `models/football/procedures/FOOTBALL_SWEEP_CHECKPOINT_EXECUTION.md`.

If the preserved user arguments begin with `repair`, also read and apply `models/football/procedures/FOOTBALL_SWEEP_REPAIR_MODE.md` **before** executing Step 0. Repair mode overrides the normal fresh-discovery loop where the repair procedure says to reuse persisted state.

If the preserved user arguments begin with `resume`, enter fresh-sweep resume mode:
- resolve the existing matching Sweep Run first;
- accept either a normal `RUNNING` checkpoint or a `BLOCKED` run whose Resume Cursor is `SOURCE_ACQUISITION / SOURCE_BLOCKED`;
- for a blocked source run, evaluate the deterministic source-recovery lease before returning the stored blocker;
- if retry is authorized, set `Run Status = RUNNING` before any provider call, then execute exactly one bounded recovery acquisition pass;
- load its authoritative `Resume Cursor` + persisted coverage rows;
- continue from the next unfinished phase/block;
- do not create a new Run ID;
- do not restart source acquisition when the persisted source epoch is still ACQUIRED.

Otherwise execute `models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md` as a new checkpointed sweep.

Preserve all user text after `/sweep` as the requested sweep-window/instructions and use same-message attachments as inputs.

This wrapper does not redefine Step 0. Checkpoint boundaries are normal execution control and do not weaken coverage.
