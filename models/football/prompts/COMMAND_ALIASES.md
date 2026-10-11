# Football Short Command Aliases

> **ACTIVE MODEL AIRTABLE ROUTING — 2026-10-11 (all except /sweep):** Before the first Airtable model read/write, load `models/football/airtable/ACTIVE_MODEL_ROUTING.md` and `ACTIVE_MODEL_ROUTING.json`. All new model board, C/C2 decision, live, audit, report, calibration, Website Picks and user-verified Actual Bets operations use base `appbzxqXYf0lKfD4P` and its mapped table IDs. Field names must be resolved against the new schema; old record/field/table IDs are never write targets. **The `/sweep` launcher and its Airtable routing are explicitly unchanged**, including existing Step0 handoff receipts. Do not reroute Sweep Runs or rewrite frozen Step0 rows. Model writes require same-base readback with original Coverage/Assessment/Pick/Actual Bet identity. No implicit fallback to legacy base.

**Status:** ACTIVE ROUTER CONTRACT  
**Authority:** semantic aliases for the canonical football launchers  
**Scope:** messages in the FB v2 / SlipTrace football workflow

These aliases are intentionally short so the user does not need to remember launcher filenames.

They are project-level text commands, not a dependency on ChatGPT's built-in slash-command UI. The user can simply type them as ordinary chat text.

## Simple commands — user-facing priority

**Only two actions:**

- /xi, /xi exception, /live, /assess or “assess this match”
  = **ASSESS**. Football C and C2 independently, without odds.
  Give C/C2 promising/caution/avoid reads and reasons. Never request
  bookmaker quotes or wait for a price to finish this command.
- /bet, /xi bet, or an explicit request to evaluate a quoted entry
  = **BET CHECK**. Only here is a current total plus offered odds needed
  before BET/WAIT/PASS can be authorized.

Read models/football/procedures/FOOTBALL_SIMPLE_ASSESS_AND_BET.md
first. This rule overrides older /xi and /live text describing
“mandatory quotes,” “current odds,” or a price-based WAIT for an
ASSESS request. Price-bearing screenshots alone do not turn
/xi into BET CHECK unless the user explicitly asks for that action.

## Command map

| Command | Canonical action |
|---|---|
| `/sweep` | Execute `models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md` |
| `/rank` | Execute `models/football/prompts/01_WORK_DAILY_SWEEP.md` |
| `/xi` or `/assess` | Assess C and C2 football without bookmaker odds (default) |
| `/live` | Assess current match football without bookmaker odds (default) |
| `/bet` or `/xi bet` | Optional check whether a current actual price qualifies for a BET |
| `/audit` | Execute `models/football/prompts/04_WORK_POST_SLATE_AUDIT.md` |
| `/report` | Execute `models/football/prompts/06_NORMAL_CHAT_REPORT.md` |
| `/help` | Show this command map and concise examples; do not run a football stage |

The old `@filename` / explicit launcher-path form remains valid for compatibility.

## Parsing rule

When the first non-whitespace token of the user's message is one of the aliases above:

1. treat it as an explicit request to run the mapped launcher;
2. read `models/football/procedures/FOOTBALL_HANDOFF_FRESHNESS_BOOTSTRAP.md`;
3. read `models/football/CURRENT_MODEL.md` and the current mapped launcher before trusting any handoff/prior-chat authority text;
4. preserve all remaining user text after the command as launcher arguments/instructions;
5. treat files/images attached to the same message as inputs to that launcher;
6. do not ask the user to restate the canonical filename;
7. do not reinterpret the alias as a generic conversational slash command.

Aliases are case-insensitive, but the canonical display form is lowercase.

Only the **first** alias token routes the message. Text later in the message is normal argument text.

## Command semantics

### `/sweep [window]`

Runs Step 0.

Examples:
- `/sweep now to 3am`
- `/sweep 9pm to 6am tomorrow`
- `/sweep now to 12pm`

The supplied time expression defines the requested sweep window in ICT unless the user explicitly supplies another timezone.

The sweep is checkpointed under `FOOTBALL_SWEEP_CHECKPOINT_EXECUTION.md`. A large run may intentionally return `SWEEP CHECKPOINT SAVED — /sweep resume` instead of timing out; this is RUNNING, not BLOCKED.

### `/sweep resume [window|Run ID]`

Continues the matching RUNNING Step-0 sweep from Airtable `Resume Cursor`.

Examples:
- `/sweep resume`
- `/sweep resume SWEEP-20261005-0000-0600`

Resume mode:
- reuses the acquired source epoch;
- reuses completed block evidence/dispositions;
- processes only the next bounded verification chunk;
- never starts a new Run ID for the same continuation;
- returns another checkpoint when more verification remains;
- packages the canonical ZIP only after final reconciliation passes.

The final output remains the canonical AiScore handoff/ZIP defined by Step 0.

### `/sweep repair [window]`

Runs the bounded repair path in:
`models/football/procedures/FOOTBALL_SWEEP_REPAIR_MODE.md`

Examples:
- `/sweep repair 15:00 to 00:00`
- `/sweep repair 15:00 to 00:00, exclude already-started matches`

Repair mode:
- targets the latest matching prior sweep unless a Run ID is supplied;
- reuses complete persisted rows instead of restarting discovery;
- repairs only missing/conflicting/block-deferred items;
- excludes started fixtures before deep verification;
- uses at most two authoritative verification attempts per unresolved competition block;
- terminates with an explicit unresolved list instead of continuing open-ended web search.

Do not silently route `/sweep repair` through the normal fresh-sweep discovery loop.

### `/rank`

Runs Step 1 against the attached/current canonical AiScore handoff.

Examples:
- attach the sweep ZIP, then type `/rank`;
- attach a completed repaired sweep ZIP, then type `/rank`;
- `/rank reassess` means rerun the current attached board input under the current model authority.

When a repaired sweep file is attached, apply `FOOTBALL_REPAIRED_HANDOFF_AUTHORITY.md` before web research. A structurally complete repaired handoff freezes Step-0 fixture identity, kickoff, dispositions and capacity queue for /rank.

Do not interpret `/rank` as a request for a casual subjective ranking. It invokes the full Football C official + Football C2 shadow Step-1 board workflow.

Do not use /rank to repair Step 0, re-verify repaired fixture kickoffs, or reconstruct a repaired queue from the web.

### /xi, /xi exception, /assess

Every invocation must reload the current launcher from current repository authority, including the newer simple ASSESS-first contract, rather than reuse cached Work instruction text.

**Default: ASSESS, without odds.** Use the current XI/live football
launcher, but run the pinned quote-free C+C2 assess mode FIRST.
Do not ask for any quote or new price. Supplied market screenshots
do not automatically switch the workflow into BET CHECK.

Examples: /xi, /xi exception, /assess Inter–Parma.

### /live

Identical ASSESS default, using current match score/clock when known.
A match may be assessed after kickoff or after a goal without an odds
screenshot. Explain a missing *football* fact when necessary.

### /bet, /xi bet

Explicit **BET CHECK**. Execute the same football assessment before
checking whether an actual current line/odds supports an official C
entry. If no verified current offer exists, finish the football
assessment anyway and mark only the BET CHECK unpriced.
C2 stays independent shadow; no user bet is recorded without confirmation.

### `/audit [scope]`

Runs the post-slate audit.

Examples:
- `/audit yesterday`
- `/audit last 3 boards`
- `/audit newest board`

Do not silently reduce a requested full-board audit to placed bets only.

### `/report [scope]`

Read and summarize the latest already-existing football state without rerunning Step 0/1/2.

Examples:
- `/report`
- `/report current board`
- `/report next matches`
- `/report latest decisions`

Use current persisted board/Decision State/Website Pick data and current-conversation state as applicable. Revalidate schedule/status when reporting upcoming fixtures.

`/report` must not:
- create a new sweep;
- rerank a board;
- reassess XI;
- manufacture a new model verdict.

If the user explicitly adds `refresh`, refresh only the factual current status needed for the report; do not rerun predictive stages unless they also invoke the corresponding command.

### `/help`

Return the compact command cheat sheet only.

## Input continuity

A short command may reuse an input already supplied in the **current conversation** when the intended artifact/match is unique and unambiguous.

Examples:
- a sweep ZIP was just attached, followed by `/rank`;
- XI screenshots were just posted, followed by `/xi`;
- live screenshots for the currently discussed exact match were just posted, followed by `/live`.

Do not substitute a stale board or a different similarly named fixture when identity is ambiguous.

## Authority and safety boundaries

Aliases change ergonomics only. They do not weaken or replace:
- AiScore fixture authority;
- women's top-flight coverage completeness;
- competition reliability;
- operational viability;
- tournament incentive integrity;
- burden-completion selection;
- XI/post-XI research;
- C official / C2 shadow separation;
- new-chat / handoff freshness bootstrap;
- persistence and audit rules.

If alias text conflicts with a mandatory model integrity gate, the gate wins.


## Handoff freshness

When a command is invoked in a new chat that contains a handoff or copied prior response, the handoff is context only.

Always reload the current model roster and launcher semantics first. An older handoff that names C3/C4 must not reactivate retired models in a current /rank, /xi or /live response.

For /xi and /live, Football C2 is the only current shadow action track. If a lawful C2 state cannot be produced, show the exact incomplete/unavailable reason rather than silently falling back to C-only completion.
