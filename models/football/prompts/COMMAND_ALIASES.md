# Football Short Command Aliases

> **ACTIVE MODEL AIRTABLE ROUTING — 2026-10-11 (all except /sweep):** Before the first Airtable model read/write, load `models/football/airtable/ACTIVE_MODEL_ROUTING.md` and `ACTIVE_MODEL_ROUTING.json`. All new model board, C/C2 decision, live, audit, report, calibration, Website Picks and user-verified Actual Bets operations use base `appbzxqXYf0lKfD4P` and its mapped table IDs. Field names must be resolved against the new schema; old record/field/table IDs are never write targets. **The `/sweep` launcher and its Airtable routing are explicitly unchanged**, including existing Step0 handoff receipts. Do not reroute Sweep Runs or rewrite frozen Step0 rows. Model writes require same-base readback with original Coverage/Assessment/Pick/Actual Bet identity. No implicit fallback to legacy base.

**Status:** ACTIVE ROUTER CONTRACT  
**Authority:** semantic aliases for the canonical football launchers  
**Scope:** messages in the FB v2 / SlipTrace football workflow

These aliases are intentionally short so the user does not need to remember launcher filenames.

They are project-level text commands, not a dependency on ChatGPT's built-in slash-command UI. The user can simply type them as ordinary chat text.

## Simple command — /xi

`/xi` is the **one** C+C2 match assessment command (also
`/xi exception` for a user-requested exception). Assess football
without waiting for quotes. If a genuine current price is already
provided or verified, evaluate that offer automatically in the same
response; otherwise finish the football assessment without asking
for more market screenshots. Live /xi behaves the same way but
never makes a retrospective prematch bet.

`/live` uses the same football-first behavior for a started match.
The old `/assess` and `/bet` shortcuts are optional compatibility
aliases; **do not ask the user to learn or choose them**.
See `FOOTBALL_SIMPLE_ASSESS_AND_BET.md`. No unsupported executable
bets, fabricated odds, or implicit C2 official exposure.

## Command map

| Command | Canonical action |
|---|---|
| `/sweep` | Execute `models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md` |
| `/rank` | Execute `models/football/prompts/01_WORK_DAILY_SWEEP.md` |
| `/xi` | Single C+C2 football assessment; automatically use verified actual odds if available |
| `/live` | Same one-step assessment for started matches |
| `/assess`, `/bet`, `/xi bet` | Optional historical aliases; no extra command required for `/xi` |
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

### /xi and /xi exception

Run **one** match assessment. Use C and independently C2 football
evidence first, without a bookmaker quote requirement. If a valid
current offered total/odds are already available and all eligibility
guards are satisfied, automatically include the actual price-based
C action and C2 shadow comparison. Otherwise deliver C/C2 football
reads with `No bet price checked`. Never ask for another price just
to finish /xi.

### /live

Same immediate assessment, using current score/minute/events. A
valid live quote may separately support a verified current price
decision; stale prematch quotes never do.

### /assess, /bet, /xi bet

Old shortcuts continue to work for compatibility; they must not
split or interrupt a normal `/xi` request. User does not need them.

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
