# Football v2 — Command aliases

## Active router

Only the first slash command routes the message.

| Command | Active authority |
|---|---|
| /block [window] | **Primary low-usage selector:** sweep whole block + rank qualified survivors |
| /sweep [window] | V4 source-backed intake/supporting source capture |
| /rank | **Secondary** V4 Football C whole-slate comparison/audit board |
| /xi | Football C XI/price check using BLOCK first, RANKED second, DIRECT one-off fallback |
| /xi exception | Explicit user-requested C assessment outside routine board authority |
| /live | Same Football C assessment using current started-match state |
| /audit | Normal-chat lightweight audit with automatic deep escalation |
| /audit deep | Work-only structural audit; normally entered only from an audit handoff |
| /report | Read-only current report |

Aliases are case-insensitive. Text after the command is normal launcher input.

## Conversation routing

| Stage | Conversation surface | Canonical launcher |
|---|---|---|
| BLOCK | **Normal chat — PRIMARY** | `models/football/prompts/02A_NORMAL_CHAT_BLOCK_ASSESSMENT.md` |
| SWEEP | **Normal chat** | `models/football/stages_v4/SWEEP.md` |
| RANK | **ChatGPT Work — SECONDARY** | `models/football/stages_v4/RANK.md` |
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

Use V4 only. Default schedule when the user does not specify a window:

- **MAIN slate:** 15:00 ICT -> 03:00 ICT next day;
- **SECONDARY slate:** 03:00 ICT -> 11:00 ICT.

An explicit user window always overrides the default. Never retroactively admit
already-started fixtures.

The MAIN 15:00->03:00 surface is one ranking universe. Do not automatically
split it into 15-18 / 18-21 / 21-00 / 00-03 receipts. Research may run in
bounded batches, but all batches must remain attached to the same immutable
sweep receipt. Repeated /rank refreshes that receipt and reranks the remaining
open fixtures rather than creating a new ranking universe.

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

## /block — primary low-usage workflow

A user request such as `/block 23:00-00:00`, `assess the 23:00 block`, or
`assess matches from 23:00 to 00:00` means **combine sweep + rank inside that
kickoff block**, not deep-assess every fixture.

Resolve the complete unstarted cohort, then apply the **exact active V4 /sweep
filter policy** inside that kickoff boundary: same inclusion/exclusion rules,
user exclusions, eligibility/observability gates and goals-first qualification.
/block must not maintain a separate or looser intake filter. Rank only the
survivors using the bounded block-selection evidence. **Do not use raw /sweep
research priority as the final shortlist order.** After qualification, apply
operational promotion bands: verified senior top-flight/continental fixtures
(including verified women's top flights) ahead of comparable lower-tier
fixtures; a regional/obscure lower-tier row may overtake only when its frozen
goal signal is materially stronger (default >=15 priority-score points) AND
its current researchability/XI channels are verified. A weak top-flight signal
still cannot be rescued by league status. The block display is **up to five
matches**. In addition to rankable survivors, include any unresolved
`RESEARCH_BLOCKED` fixture whose frozen V4 goal `priority_score >= 60` (or whose
frozen goal screen is `DISCOVERY_GOAL_QUALIFIED`) as
`HIGH_SCORE_RESEARCH_BLOCKED`. Such a row may occupy a top-five display slot but
must retain its blocker and has no /xi authority until the blocker is resolved.
Also apply the Band-A `HIGH_4PLUS_RESCUE`: a `GOAL_REVIEW` /
`RESERVE_SIGNAL` row must enter the five-match promotion comparison when its
frozen mean 4+ rate is >=55%, carrier route >=1.75, low-draw-trap rate <=20%,
and fixture identity/researchability is verified with no explicit exclusion or
format blocker. This does not alter its frozen sweep lane and does not create a
Football C certificate. Within Band A, compare rescued 4+ strength before raw
priority score so a 55-59 composite score cannot be buried solely by the 60
threshold. Show fewer than five only when the block has fewer credible/high-score rows.

Do **not** run ASSESSMENT_DEPTH_V3, G4 evidence research, full H2H/failure-tree
research, Football C certificate compilation, XI runtime or Decision States
persistence for every block fixture. Those expensive steps are deferred to
`/xi` for a selected exact fixture.

A lightweight /block result is selection metadata only and has no price or
exposure authority. New lightweight block receipts do not use
`authority.mode=BLOCK`; when the user later requests `/xi`, use an existing
compatible historical BLOCK/RANKED receipt if one exists, otherwise perform the
normal exact-user DIRECT full assessment for that selected fixture.

No bookmaker odds are searched during /block. A user-supplied screenshot is
handled later by /xi under screenshot-only price authority.

## /rank

Use the newest/explicit native V4_SWEEP_READY receipt only when its requested
window is upstream-complete. A receipt with unresolved intake, PARTIAL status,
or a nonzero upstream remaining count is not rankable and must resume the same
sweep checkpoint first.

The rank stage performs original-source replay and a fresh full-cohort status
check before executing the single official Football C board, then independently
verifies Google Sheets persistence once.

Repeated `/rank` for the same source epoch resolves its latest native research
checkpoint automatically, reuses completed factual inputs, and continues the
ordered unresolved queue. Report full cohort dispositions and research
completeness separately from persistence. A partial saved board uses
`V4_RANK_PARTIAL_PERSISTENCE_VERIFIED`; no user resubmission of omitted IDs is
needed. This does not schedule background work.

Rank display has two positions. `Slate Rank` freezes only on the first
full-research cohort rank and remains immutable for that receipt.
`Current Rank` is recalculated among still-open assessed fixtures on each
status refresh. Legacy `rank` remains an alias of Current Rank. While rank
research is partial, Slate Rank is null/pending; never present a partial-cohort
rank as the final slate ordering.

Ranked Step 2 may still trust the resulting verified C rank+persistence
receipt, but primary block assessment does not depend on /rank and must not
inherit rank ordering as football evidence.

For new rank epochs, the launcher must also satisfy the prospective selection
research contracts defined by RANK.md. A strong-primary/usable-reply
REVIEW_ONLY row may require `G3_BORDERLINE_DISCRIMINATION_V2`; populate its
source-backed `selection_recheck` instead of accepting a generic MEDIUM card.
Nearby Grade-A/B credible candidates may require `BLOCK_DISCRIMINATION_V3`;
research the full block at equal depth and populate each `block_comparison`.
A pending contract resumes the exact rank checkpoint. Do not bypass it by
dropping the candidate, changing its operational grade, or copying global /rank order. Reconcile against BLOCK_PRIORITY_V1; global rank is
audit metadata only.

## /xi

/xi is one command. The user does not need separate assess/bet commands.

Authority order remains historical/full BLOCK -> RANKED -> DIRECT -> explicit EXCEPTION.
A new lightweight /block shortlist is selection metadata, not full BLOCK
authority. If the user selects one of those fixtures with /xi and no compatible
historical full BLOCK or RANKED receipt exists, perform the fresh full
ASSESSMENT_DEPTH_V3 research in that /xi turn and use DIRECT.

Order:

1. inherit only a compatible historical/full BLOCK receipt when available,
   otherwise use the verified RANKED compatibility path; a new lightweight
   /block shortlist alone does not count as BLOCK authority, so if neither full
   authority exists for an exact explicit /xi, perform fresh full research and
   use DIRECT;
2. refresh only genuinely changed Football C evidence;
3. if the user supplied a screenshot/observed quote, evaluate that exact
   line/odds through the shared C quote policy;
4. if a genuinely current executable quote and all strict execution evidence
   exist, run the strict C decision;
5. persist/read back once when persistence is required.

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
