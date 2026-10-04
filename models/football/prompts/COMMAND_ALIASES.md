# Football Short Command Aliases

**Status:** ACTIVE ROUTER CONTRACT  
**Authority:** semantic aliases for the canonical football launchers  
**Scope:** messages in the FB v2 / SlipTrace football workflow

These aliases are intentionally short so the user does not need to remember launcher filenames.

They are project-level text commands, not a dependency on ChatGPT's built-in slash-command UI. The user can simply type them as ordinary chat text.

## Command map

| Command | Canonical action |
|---|---|
| `/sweep` | Execute `models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md` |
| `/rank` | Execute `models/football/prompts/01_WORK_DAILY_SWEEP.md` |
| `/xi` | Execute `models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md` |
| `/live` | Execute `models/football/prompts/03_NORMAL_CHAT_LIVE.md` |
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

The output remains the canonical AiScore handoff/ZIP defined by Step 0.

### `/rank`

Runs Step 1 against the attached/current canonical AiScore handoff.

Examples:
- attach the sweep ZIP, then type `/rank`;
- `/rank reassess` means rerun the current attached board input under the current model authority.

Do not interpret `/rank` as a request for a casual subjective ranking. It invokes the full Football C official + C2/C3 shadow board workflow.

### `/xi`

Runs Step 2 for the supplied/referenced match(es).

Examples:
- attach XI + odds screenshots, then type `/xi`;
- `/xi exception` preserves the user's explicit exception declaration for the supplied match(es), but does not waive tournament-incentive, evidence, identity, XI or market integrity gates.

### `/live`

Runs the live/wait launcher for the supplied current match state.

Examples:
- attach live screenshots, then type `/live`;
- `/live exception` is an explicit user live-exception declaration for the supplied exact match/epoch, subject to all mandatory integrity gates.

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
- C official / C2/C3 shadow separation;
- new-chat / handoff freshness bootstrap;
- persistence and audit rules.

If alias text conflicts with a mandatory model integrity gate, the gate wins.


## Handoff freshness

When a command is invoked in a new chat that contains a handoff or copied prior response, the handoff is context only.

Always reload the current model roster and launcher semantics first. An older handoff that only mentions C/C2 must not cause C3 to disappear from a current /xi or /live response.

For /xi and /live, C2 and C3 must be visible even when their correct status is UNAVAILABLE / COMPARISON INCOMPLETE.
