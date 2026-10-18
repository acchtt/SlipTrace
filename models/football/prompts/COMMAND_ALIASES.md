# Football v2 — Command aliases

## Active router

Only the first slash command routes the message.

| Command | Active authority |
|---|---|
| /sweep [window] | V4 source-backed intake: models/football/stages_v4/SWEEP.md |
| /rank | V4 Football C rank: models/football/stages_v4/RANK.md |
| /xi | One Football C assessment with optional observed/executable price check |
| /xi exception | Explicit user-requested C assessment outside routine board authority |
| /live | Same Football C assessment using current started-match state |
| /audit | Normal-chat lightweight audit with automatic deep escalation |
| /audit deep | Work-only structural audit; normally entered only from an audit handoff |
| /report | Read-only current report |

Aliases are case-insensitive. Text after the command is normal launcher input.

## Conversation routing

| Stage | Conversation surface | Canonical launcher |
|---|---|---|
| SWEEP | **Normal chat** | `models/football/stages_v4/SWEEP.md` |
| RANK | **ChatGPT Work** | `models/football/stages_v4/RANK.md` |
| XI / XI exception | **Normal chat** | `models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md` |
| LIVE | **Normal chat** | `models/football/prompts/03_NORMAL_CHAT_LIVE.md` |
| AUDIT | **Normal chat** | `models/football/prompts/04_NORMAL_CHAT_AUDIT.md` |
| AUDIT DEEP | **ChatGPT Work** | `models/football/prompts/04_WORK_POST_SLATE_AUDIT.md` |
| REPORT | **Normal chat** | `models/football/prompts/06_NORMAL_CHAT_REPORT.md` |

Normal chat does not mean free-form model decisions. `/xi` and `/live` must
still use the current deterministic Football C runtime wherever that runtime
has authority. For `/xi`, inability to call Python locally must trigger the
on-demand GitHub XI backend, not an immediate ANALYSIS_ONLY fallback.
ANALYSIS_ONLY is permitted only after both direct execution and the backend are
unavailable or the backend returns a concrete failure. Never substitute
conversational judgment for an official engine receipt.

Each stage loads its current canonical launcher and transfers validated
receipts/evidence, not previous-chat reasoning. Do not silently chain stages.

## /sweep

Use V4 only. Start from the actual requested/current ICT window and never
retroactively admit already-started fixtures.

The sweep acquires complete provider date surfaces before registry/filtering.
A new normal-chat sweep must first reach `SOURCE_READY_FOR_RESEARCH`; if local
acquisition is unavailable it uses the dedicated source-only GitHub backend
(`normal_source_requests/` -> `football-v4-normal-source.yml`). Manual web
research cannot substitute for this source gate. Only then apply exclusions,
research priority and goals-first qualification.
Finish targeted upstream research in the same normal sweep invocation before
calling the handoff complete. Persist the immutable source before research and a
durable v2 checkpoint after at most four fixture dispositions. Source
attestation/native finalization are internal backend phases and must not require
a user /resume. If a genuine tool failure interrupts research, /resume processes
only the stored unresolved queue; resolved fixtures are never re-researched.
Reacquire only when source freshness/validation requires one bounded new source
epoch, then remap reusable research by exact fixture identity.

Do not invoke retired V1-V3 checkpoint, repair, ZIP or capacity workflows, and
do not use Work acquisition orchestration as the default new-sweep route.

## /rank

Use the newest/explicit native V4_SWEEP_READY receipt.

The rank stage performs original-source replay and a fresh full-cohort status
check before executing the single official Football C board, then independently
verifies Google Sheets persistence once.

Repeated `/rank` for the same source epoch resolves its latest native research
checkpoint automatically, reuses completed factual inputs, and continues the
ordered unresolved queue. Report full cohort dispositions and research
completeness separately from persistence. A partial saved board uses
`V4_RANK_PARTIAL_PERSISTENCE_VERIFIED`; no user resubmission of omitted IDs is
needed. This does not schedule background work.

Routine Step 2 trusts the resulting verified C rank+persistence receipt; it
does not repeat source replay.

## /xi

/xi is one command. The user does not need separate assess/bet commands.

Order:

1. current Football C assessment, no odds required;
2. if the user supplied a screenshot/observed quote, evaluate that exact
   line/odds through the shared C quote policy;
3. if a genuinely current executable quote and all strict execution evidence
   exist, run the strict C decision;
4. persist/read back once when persistence is required.

A user screenshot is the sole price source for that comparison. Do not search
for replacement odds, re-time it, or request a new screenshot merely because
processing took time.

Observed-quote ACT/WAIT/PASS is conditional only. It never authorizes
publication/exposure by itself.

If direct runtime execution is unavailable, normal chat writes one
`football-c-xi-runtime-request-v1` request, waits for the deterministic
`XI Football C deterministic runtime` workflow, reads the persisted
`xi_runtime_results/<request-id>.json`, and continues in the same turn. The
user should not have to type `/resume` to obtain the engine result.

WAIT requires an explicitly evidenced reachable target. A lone screenshot does
not prove same-line odds will improve.

## /xi exception

An explicit exception can assess a STOP/non-board fixture from independently
researched Football C evidence. It does not authorize retrospective prematch
action after kickoff.

## /live

/live uses the same Football C assessment with actual current score/minute and
material events. Do not recreate prematch action after kickoff.

## /audit

The user normally uses only `/audit`. Run it in normal chat and inspect the
smallest relevant set of frozen receipts, board rows, decisions and outcomes.
Diagnose the incident before considering implementation.

Escalate automatically only when the issue is structural: repeated across
fixtures/slates, caused by conflicting authority, unresolved source/runtime/
persistence integrity, or requiring code/repository inspection and regression
tests. In that case finish with `DEEP AUDIT REQUIRED` plus the compact handoff
defined by the audit launcher.

The user should not have to decide between routine and deep audit.

## /audit deep

Work-only escalation target. Consume the normal-audit handoff rather than
re-reading the whole conversation. Perform repository-wide/rule/runtime
inspection and regression testing only for the named defect scope. Never rewrite
historical decisions. Retired C2/C3/C4 records are read-only audit material.

## /report

Read only from active operational state. User P/L comes only from
Actual Bets — Current.

## Active model and data boundaries

- Football C: official and only active model.
- C2/C3/C4: retired for all new work.
- Active operational workbook: Google Sheets `Football v2 — Active Operations` (`1ojWKj5aT3VEJUyX3NSbAOZNTaUM0Mb8I8e4lvFy7kGM`).
- Historical retired-model fields/receipts remain immutable and read-only.
- WATCH and unresolved WAIT create no synthetic active exposure.
- Actual Bets — Current is the only authority for physical user P/L.

## Retired command/model semantics

Old V1-V3 sweep/resume/repair/ZIP/compact-capacity semantics and all C2/C3/C4
execution paths are historical only. If an old handoff mentions them, reload
this router and use the current V4 + Football C workflow.
