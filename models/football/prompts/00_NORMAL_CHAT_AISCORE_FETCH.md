# 00 — Normal Chat: AiScore Fetch + Coverage

**Use in:** Normal Chat, high reasoning.

## Purpose
Build a trustworthy **actionable senior AiScore universe** for the requested window, apply the active quality/sweep filters cheaply, persist the minimal coverage skeleton, and export only genuinely actionable fixtures to Work.

Operational principle:

`NORMALIZE WINDOW BOUNDARIES ONCE -> DISCOVER BROADLY -> PRESERVE RAW AISCORE TIME -> EXCLUDE CHEAPLY -> REVALIDATE EVERY WORK-ADMITTED FIXTURE AGAINST AUTHORITATIVE AISCORE UTC/OFFSET -> CONVERT ADMITTED SET ONCE TO ICT -> PROVE WINDOW MEMBERSHIP -> PACKAGE HANDOFF`

Do not convert every raw discovered fixture. However, **requested-window boundary normalization, deterministic date-envelope traversal, terminal-interval verification, and one final authoritative time normalization pass over the surviving Work-admitted set are mandatory Step-0 work.**

## Source of truth
Repository: `acchtt/SlipTrace`

Always read upstream/default-branch:

1. `models/football/CURRENT_MODEL.md`
2. `models/football/procedures/FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`
3. `models/football/procedures/FOOTBALL_SWEEP_SCOPE.md`
4. `models/football/procedures/FOOTBALL_LEAGUE_ENVIRONMENT_REGISTRY.md`

The active time procedure uses **source-time preservation for fixtures plus mandatory one-time normalization of the requested window boundaries**. If an older subordinate file says every fixture must be converted to ICT during discovery, the active time procedure wins.

## Airtable
Base: `SlipTrace Football Decision Control`

- Base ID: `appWyZJjitSBATXAU`
- Daily Coverage Ledger: `tblcl1UAyMqZT6Ub0`
- Decision States: `tblQmUpd5WjBLQ38X`
- Website Picks: `tblg3J5sbJYbzuTYD`
- Sweep Runs: `tblUnGHHe0MVaalDL`

Use these IDs directly unless one actually fails.

## Authoritative resumable execution state

`Sweep Runs` is the **source of truth for Step-0 execution progress**. Chat history is not an execution checkpoint and must never be used as the sole basis for deciding where to resume.

For an **explicit absolute ICT window**, derive one deterministic run ID:

`SWEEP-YYYYMMDD-HHMM-YYYYMMDD-HHMM`

using the exact requested ICT start/end minute. The same exact absolute window reuses the same Run ID.

### Relative-start coalescing — mandatory

For requests whose start is relative, such as `now`, `from now`, or equivalent, **do not immediately create a new Run ID from the new clock minute**.

Before creating a run:

1. search `Sweep Runs` for non-complete `RUNNING` or `BLOCKED` rows whose requested end boundary matches the newly requested end boundary and whose window overlaps the current time;
2. if exactly one compatible active run exists, reuse/resume it;
3. if multiple compatible active runs exist, use the **most recently Updated At** row as the canonical run and do not create another;
4. older compatible rows with no validated handoff package may be marked `ABANDONED` with `SUPERSEDED BY <canonical Run ID>` in Checkpoint Notes;
5. create a fresh relative-start Run ID only when no compatible active run exists, or when the user explicitly says `new sweep`, `restart from now`, `discard the old run`, or equivalent.

This rule prevents repeated `from now till 03:00` launches from spawning overlapping sweeps every time the chat is restarted.

### START behavior

Before any AiScore traversal:

1. find the `Sweep Runs` row for the deterministic Run ID;
2. if none exists, create it with:
   - `Run Status = RUNNING`;
   - `Current Stage = CORE DISCOVERY`;
   - exact Window Start/End ICT;
   - active Model Version;
   - zeroed counts;
   - all completion flags false;
   - deterministic discovery envelope;
   - `Resume Cursor` set to the first required discovery block;
   - empty `Retry Queue`;
3. if a row exists with `RUNNING` or `BLOCKED`, continue from its persisted state instead of starting over;
4. if a row is already `COMPLETE`, do not silently rerun it. Return/report the completed package unless the user explicitly requests a rerun/rebuild.

### RESUME / CONTINUE behavior

When the user says `resume`, `resume the sweep`, `continue`, or equivalent:

1. load the matching current-window `Sweep Runs` row first;
2. if the current chat does not contain an explicit window, use the newest non-complete `Sweep Runs` row only when it is unambiguous;
3. trust persisted stage flags, `Listing Blocks Checked`, `Resume Cursor`, `Retry Queue`, counts and checkpoint notes over conversational recollection;
4. continue from the exact `Resume Cursor`;
5. never restart an already-completed stage merely because the conversation was interrupted;
6. never infer a missing cursor from prose if Airtable has a persisted cursor.

If no resumable row can be identified, report `NO RESUMABLE SWEEP RUN FOUND` rather than inventing state.

### REPORT / STATUS behavior

When the user asks `report`, `status`, or equivalent during a sweep, **do not run AiScore discovery**. Read the `Sweep Runs` row and return only:

- Run ID;
- requested ICT window;
- Run Status;
- Current Stage;
- completed stage flags;
- discovered/admitted/excluded/unresolved counts;
- current `Resume Cursor`;
- retry-queue count/content summary;
- last checkpoint time;
- handoff package if already produced;
- blocking fault, if any.

### Mandatory checkpoint cadence

Checkpoint state to `Sweep Runs` **sparingly**:

- after every 20 successfully processed listing/competition blocks;
- immediately after every stage transition;
- immediately before and after the European cup audit;
- immediately before and after the terminal sentinel;
- immediately before admitted-set time proof/reconciliation;
- immediately before packaging;
- immediately after packaging;
- immediately when a genuinely blocking fault is discovered.

Do **not** checkpoint after every small web/AiScore batch, every fixture, or every retry. Within a stage, keep working in-memory between checkpoints and use the persisted cursor only at the cadence above.

Every checkpoint must persist, where applicable:

- `Run Status`;
- `Current Stage`;
- all stage completion flags;
- counts;
- `Discovery Envelope`;
- cumulative `Listing Blocks Checked`;
- `Resume Cursor` = exact next unprocessed block;
- `Retry Queue`;
- `Checkpoint Notes`;
- `Updated At`.

Keep checkpoint payloads compact. `Listing Blocks Checked` should use canonical block identifiers rather than repeated narrative prose. `Checkpoint Notes` should contain only the material delta/fault since the previous checkpoint, not a full sweep recap.

A checkpoint is committed **after** a block's Airtable coverage writes succeed. This makes replay idempotent and prevents the cursor from advancing past unpersisted work.

### Retry and transient-failure behavior

A single failed web/AiScore/tool call must not terminate the whole sweep.

For a transient failure:

1. retry that block once when safe;
2. if it still fails, append the exact block + reason to `Retry Queue`;
3. keep enough cursor information to revisit it;
4. continue with independent blocks when completeness is not yet being asserted;
5. drain `Retry Queue` before marking the current stage complete.

If a queued block remains unresolved and could contain actionable senior fixtures, set `Run Status = BLOCKED`, keep the exact `Current Stage` and cursor, persist the blocker, and do not set `work_ready=true`.

Excluded/non-blocking raw categories may remain documented raw gaps under the existing two-tier completeness contract.

### Idempotence rules

- `Sweep Runs` upserts by deterministic Run ID.
- Daily Coverage Ledger continues to upsert by Coverage ID.
- Reprocessing the current cursor after an interruption must be harmless.
- Counts must be recomputed/reconciled from persisted fixture state rather than blindly incremented on retries.
- `Listing Blocks Checked` is cumulative and must not duplicate the same canonical block.
- Stage completion flags move false -> true only after the stage's persistence/checks pass.

### Stage machine

Use the existing `Current Stage` values in this order:

`CORE DISCOVERY -> CONDITIONAL GATES -> EUROPEAN CUP AUDIT -> TERMINAL SENTINEL -> RECONCILIATION -> PACKAGING -> COMPLETE`

The final admitted-set authoritative time proof belongs to `RECONCILIATION`.

Do not enter a later stage until its prerequisite stage is complete. `Run Status = COMPLETE` is allowed only when packaging is validated and all mandatory stage flags are true.

On a genuine missed-fixture recovery, preserve the existing missed-fixture rules below **and** reopen the same deterministic Run ID: set `Run Status = RUNNING`, reset `Current Stage = CORE DISCOVERY`, clear affected/downstream completion flags, rebuild the required envelope/sentinel proof, and replace the old package only after the repaired run passes all gates.

## Strict stage boundary
Step 0 is executed through the persisted stage machine above. The conversational session is only the controller; `Sweep Runs` is execution memory.

Step 0:

1. resolves the requested window start/end in ICT and UTC **once**;
2. builds the deterministic discovery-date envelope required by `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`;
3. traverses every AiScore date/competition block needed to cover that envelope;
4. performs a second dedicated AiScore terminal-interval sentinel sweep covering the final six hours of the requested window (or the entire window if shorter);
5. performs a separate European domestic-cup audit across the touched date envelope;
6. proves coverage of every **potentially actionable senior block**;
7. preserves fixture identity and source kickoff/timezone/offset exactly as supplied by AiScore;
8. deduplicates once;
9. applies senior-quality exclusions;
10. applies sweep scope and league registry;
11. runs only the cheap conditional-league admission test where required;
12. batch-upserts the cheap coverage skeleton for actually discovered fixtures;
13. revalidates every surviving Work-admitted fixture against an authoritative AiScore timestamp with explicit UTC/offset provenance;
14. normalizes the admitted set once to verified UTC and ICT, prunes true out-of-window fixtures, and blocks unresolved time/identity conflicts;
15. creates a compact scope-pruned Work handoff **only after the coverage and admitted-set time-integrity gates pass**;
16. packages the canonical handoff text file into the required ZIP archive and returns the ZIP as the user-facing sweep artifact.

Step 0 does **not**:

- convert every **raw discovered** fixture kickoff to ICT; it must convert the final Work-admitted set before handoff packaging;
- perform full structural match research;
- assign PRE grades or board ranks;
- fetch confirmed XI or bookmaker odds;
- create Decision States;
- touch Website Picks;
- issue betting decisions.

## Mandatory window boundary + discovery-envelope proof

Before discovery begins, resolve and record:

- `window_start_ict`;
- `window_end_ict`;
- `window_start_utc`;
- `window_end_utc`;
- `ict_dates_touched`;
- `utc_dates_touched`.

Then build the discovery-date envelope as required by the time procedure:

`ICT dates touched + UTC dates touched + one UTC date before + one UTC date after`

Traverse the relevant AiScore date/listing blocks across that envelope. The buffer dates are for discovery only; they do not expand the user's requested window.

For any window that crosses midnight or ends between `00:00` and `06:00` ICT, explicitly inspect:

- the terminal ICT calendar date; and
- the UTC date containing `window_end_utc`.

A start-date-only sweep is automatically incomplete.

## Mandatory terminal-interval sentinel

Define:

`terminal_interval_ict = max(window_start_ict, window_end_ict - 6 hours) -> window_end_ict`

Run a **second independent AiScore-only discovery pass** specifically for that interval after the broad pass.

The terminal sentinel must record:

- `terminal_interval_ict`;
- terminal ICT date(s) checked;
- terminal UTC date(s) checked;
- AiScore listing/date blocks checked;
- potentially actionable senior competition blocks found;
- admitted count from the terminal pass;
- actionable excluded/unresolved count from the terminal pass;
- `terminal_scan_complete=true|false`.

If the terminal pass returns zero actionable fixtures, that is valid only when the pass itself is documented as complete.

**Never infer terminal completeness from the latest kickoff already found.** A file whose last listed fixture is at 22:30 cannot claim a 03:00 cutoff is covered merely because nothing later appeared in the first pass.

Do not use another provider to add fixtures. Web search may be used only as a way to locate AiScore pages; every fixture entering the universe must resolve to AiScore identity.

## Mandatory European domestic-cup audit

After the broad date-envelope pass and before actionable completeness, run a separate **AiScore-only European domestic-cup audit** across every touched ICT/UTC listing date.

This pass exists because domestic cup blocks can be omitted from generic league traversal even when senior first-team fixtures fall inside the requested window.

At minimum:

- inspect senior domestic cup blocks under UEFA-member associations that can place fixtures inside the window;
- treat Norway NM Cup, Danish Cup and equivalent UEFA national/league cups as actionable competition blocks unless another independent exclusion applies;
- record every European cup block checked, plus admitted/excluded/unresolved counts;
- do not infer "no cup fixtures" merely because the main pass returned none;
- if a relevant European domestic cup block was not checked, set `actionable_complete=false` and `work_ready=false`.

A European cup fixture may be excluded for youth/reserve/amateur status, out-of-window time, a direct user hard exclusion, or a resolved current AiScore status. It may not be silently omitted because the competition is a cup.

## Source-time capture + final admitted-set time proof

During broad discovery, preserve for every fixture where available:

- AiScore fixture ID/canonical match URL;
- listing date used for discovery;
- raw/source kickoff text;
- `kickoff_source_local`;
- `source_timezone` and/or `source_utc_offset`;
- AiScore-supplied UTC only when explicitly present;
- status at fetch.

Do **not** guess a timezone from geography and do **not** append `UTC` to a bare AiScore display clock.

A localized/display heading such as `Competition YYYY/MM/DD HH:mm:ss`, a date-listing clock, team-fixture clock, or search snippet without an explicit timezone is **discovery evidence only**. It is not authoritative UTC.

Before the final Work handoff is created, revalidate **every surviving Work-admitted fixture** using the current canonical AiScore match identity and accept time only from:

1. Match Info / About The Match explicitly labeled `UTC`;
2. AiScore machine-readable epoch / ISO timestamp with explicit zone;
3. AiScore timestamp with an explicit UTC offset.

Persist for every admitted fixture:

- `kickoff_time_provenance = MATCH_INFO_UTC | API_EPOCH | EXPLICIT_OFFSET`;
- `kickoff_utc_verified`;
- `kickoff_ict_verified`;
- `time_verified_at`;
- canonical AiScore fixture ID/URL used.

Convert the verified instant exactly once to `Asia/Ho_Chi_Minh`. Then prove the converted kickoff is inside `window_start_ict -> window_end_ict`.

During broad discovery a fixture may temporarily be `WINDOW STATUS = PENDING CONVERSION`; **no Work-admitted fixture may remain pending at handoff packaging**.

If the canonical match identity/time conflicts with a listing/team surface, use `UNRESOLVED — SOURCE TIME INTEGRITY` until the current AiScore authority is resolved. Do not guess, average, or silently choose the convenient time.

## Two-tier completeness contract
Distinguish:

- `actionable_complete` — every potentially actionable senior competition/block relevant to the requested sweep has been checked and every admitted fixture is accounted for **with date-envelope and terminal-sentinel proof**;
- `raw_audit_complete` — every raw AiScore fixture, including already excluded youth/lower/reserve/amateur/regional blocks, was individually enumerated.

`raw_audit_complete=false` is non-blocking when gaps are confined to categories already outside model scope.

### Blocking gaps
`work_ready=false` when any actionable requirement remains unresolved, including:

- discovery date envelope not fully traversed;
- terminal sentinel not explicitly completed;
- European domestic-cup audit not explicitly completed;
- terminal ICT date or UTC end-date block not checked for a cross-midnight/early-morning window;
- PRIORITY/NORMAL senior block not checked;
- eligible senior cup/continental block not checked;
- relevant CONDITIONAL senior block not cheap-gated;
- scope/registry contradiction;
- fixture identity/source-time contradiction;
- any Work-admitted fixture lacks `kickoff_time_provenance`, `kickoff_utc_verified`, or `kickoff_ict_verified`;
- any Work-admitted fixture converts outside the requested ICT window;
- any Work-admitted fixture remains `PENDING CONVERSION`;
- admitted count does not match the Work array.

Do **not** block Work because excluded micro/youth/lower fixtures were not individually enumerated.

### Non-blocking raw gaps
Examples:

- youth/Uxx, except official Netherlands Eerste Divisie Jong/U21 participant fixtures under the explicit competition-scoped exception;
- academy/junior;
- reserves/B/development, except official Netherlands Eerste Divisie Jong/U21 participant fixtures under the explicit competition-scoped exception;
- amateur/semi-pro;
- regional/state/provincial;
- unapproved lower divisions;
- very weak/obscure competitions;
- LOW-GOAL EXCLUDE leagues;
- HARD EXCLUDE domestic leagues.

Record:

- `raw_audit_complete=false`;
- `raw_count_mode=lower_bound`;
- `nonblocking_raw_gaps=[...]`.

Never fabricate an exact raw count.

## Quality exclusions first
Before any conditional cheap gate, remove fixtures already excluded by the active senior-quality overlay:

- youth/Uxx / academy / junior;
- reserve/B/development;
- amateur/semi-pro;
- regional/state/provincial;
- domestic lower divisions unless explicitly approved;
- very small/obscure weak-data environments.

### Netherlands Eerste Divisie Jong/U21 exception

Effective 2026-09-19 ICT, **official Netherlands Eerste Divisie league fixtures involving Jong/U21/reserve-branded participant teams are actionable candidates**. Do not exclude an official Eerste Divisie fixture solely because a participant name contains Jong, U21, reserve, or equivalent development branding.

This exception is competition-scoped only. Separate youth/U21/reserve/development competitions, cups, friendlies, and other reserve leagues remain excluded under the normal overlay.

For actionable completeness, every official Eerste Divisie fixture in the requested window — including Jong/U21 participant fixtures — must be enumerated and passed through the normal NORMAL-lane handoff rules. Omitting them makes `actionable_complete=false`.

Do not waste conditional-gate work on excluded categories.

## League environment admission
Use `FOOTBALL_LEAGUE_ENVIRONMENT_REGISTRY.md` plus current sweep-scope hard exclusions.

### PRIORITY / NORMAL
Send surviving fixtures directly to Work.

### CONDITIONAL
Use only the cheap registry gate. If it passes, admit to Work. If it fails or evidence is not readily available, exclude before Work as:

`CONDITIONAL LEAGUE — NO CHEAP OVER SIGNAL`

This is a scope exclusion, not a PRE PASS.

### LOW-GOAL EXCLUDE
Exclude before Work:

`LOW-GOAL NATIONAL LEAGUE — EXCLUDED`

### HARD EXCLUDE
Apply the current sweep scope, including Finnish domestic leagues and the current Japanese domestic-league exclusion. Do not convert those blocks match-by-match merely for completeness.

Senior cups and continental competitions are evaluated independently; club nationality does not automatically transfer a domestic-league exclusion.

## Airtable coverage skeleton
Batch-upsert fixtures actually discovered in Step 0.

Populate where supported:

- Coverage ID
- provisional Slate Date / discovery date as appropriate
- Match
- Competition
- Eligibility
- Exclusion Reason
- Reconciled
- Source 1 = AiScore
- Coverage Status
- source kickoff/timezone details in notes

### Important datetime rule
The table field `Kickoff ICT` must **never** receive a foreign-zone/local source time or a bare clock copied from an AiScore display surface.

During broad discovery, leave it blank.

After the final admitted-set time proof:

- write the verified kickoff instant corresponding to `kickoff_ict_verified`;
- preserve raw source text, `kickoff_utc_verified`, `kickoff_ict_verified`, provenance and verification timestamp in the handoff/coverage notes;
- never reconstruct `Kickoff ICT` later by regex-parsing an unverified note.

For Work-admitted rows, leave official PRE fields untouched. XI/market remain pending.

## Work-readiness gate
A Work handoff may be created only when:

- `complete=true` meaning actionable completeness;
- `actionable_complete=true`;
- `work_ready=true`;
- `discovery_date_envelope_complete=true`;
- `terminal_scan_complete=true`;
- `european_cup_audit_complete=true`;
- all required discovery/listing dates are named in the handoff;
- all potentially actionable senior blocks were checked;
- scope/registry audit passed;
- no source-time/identity unresolved fixture appears in the Work array;
- every admitted fixture has authoritative time provenance + verified UTC + verified ICT;
- every verified ICT kickoff lies inside the requested window;
- admitted count equals the Work fixture array.

`kickoff_ict_verified` is **required for every Work-admitted fixture at final handoff packaging**.

A bare assertion such as `terminal_interval_date_verification=PASS` is **not sufficient** unless the handoff also names the terminal interval and the date/listing blocks actually checked.

## Compact Work handoff + ZIP packaging
When the actionable-completeness gate passes, create the canonical UTF-8 text handoff first, then package it into a ZIP archive.

Canonical inner handoff name:

`AISCORE_FIXTURES_YYYY-MM-DD.txt`

When the user window needs additional disambiguation, a more specific existing basename is allowed, for example:

`AISCORE_FIXTURES_2026-09-17_2043_TO_2026-09-18_1200_ICT.txt`

Required user-facing archive name:

`<canonical handoff basename>.zip`

Example:

`AISCORE_FIXTURES_2026-09-17_2043_TO_2026-09-18_1200_ICT.zip`

ZIP contract:

- the archive must contain exactly one canonical `AISCORE_FIXTURES_*.txt` Work handoff at archive root;
- do not nest the handoff inside a folder;
- do not add duplicate handoff files;
- do not add OS metadata such as `__MACOSX`, `.DS_Store`, or hidden temp files;
- compression method may be normal DEFLATE;
- the text handoff remains the semantic authority; ZIP is the transport/package format;
- attach **only the ZIP** as the normal sweep artifact; do not also attach the loose `.txt` unless the user explicitly asks for it;
- if ZIP creation or validation fails, report `HANDOFF PACKAGING FAILED — DO NOT SEND TO WORK` rather than silently falling back to a loose text artifact.

The inner text handoff must include:

- requested user window and timezone;
- model version;
- source = AiScore;
- sweep scope + league registry;
- `window_start_ict` / `window_end_ict`;
- `window_start_utc` / `window_end_utc`;
- `ict_dates_touched`;
- `utc_dates_touched`;
- `discovery_listing_dates_checked`;
- `discovery_date_envelope_complete:true`;
- `terminal_interval_ict`;
- `terminal_listing_dates_checked`;
- `terminal_scan_complete:true`;
- `complete:true`;
- `actionable_complete:true`;
- `work_ready:true`;
- `raw_audit_complete:true|false`;
- `raw_count_mode=exact|lower_bound`;
- `nonblocking_raw_gaps` when applicable;
- actionable-block audit result;
- coverage publication result;
- only fixtures admitted to Work;
- AiScore identity;
- source kickoff local time;
- source timezone/offset;
- AiScore-supplied UTC if explicitly available;
- `kickoff_time_provenance`;
- `kickoff_utc_verified`;
- `kickoff_ict_verified`;
- `time_verified_at`;
- `window_status=confirmed`;
- counts.

Do not require `kickoff_ict` in the Step-0 handoff.

## Reconciliation
Before `work_ready=true`:

`ACTIONABLE SENIOR UNIVERSE = WORK-ADMITTED + ACTIONABLE-EXCLUDED/UNRESOLVED`

Verify:

- discovery date envelope is complete;
- terminal sentinel is complete;
- European domestic-cup audit is complete;
- every required terminal date/listing block is named;
- no LOW-GOAL EXCLUDE fixture survived into Work;
- no hard-excluded domestic-league fixture survived;
- no CONDITIONAL fixture survived without a cheap-gate PASS;
- no excluded youth/reserve/lower/weak-data fixture survived, except official Netherlands Eerste Divisie Jong/U21 participant fixtures admitted by the explicit 2026-09-19 exception;
- admitted count equals the Work array;
- no source-time integrity unresolved fixture appears in Work;
- raw gaps are explicitly non-blocking and already outside scope.

Boundary fixtures may be pending only during broad discovery. Before packaging, every Work-admitted fixture must be normalized and either `window_status=confirmed` or removed/blocked.

## Missed-fixture recovery

If an actionable fixture is later found inside a window that had already been marked complete:

1. invalidate the old completeness claim;
2. classify the root cause as one of: `DATE ENVELOPE MISS`, `TERMINAL SENTINEL MISS`, `ACTIONABLE BLOCK MISS`, `FILTER/PERSISTENCE MISS`, or `SOURCE TIME FAULT`;
3. rerun the whole Step 0 envelope + terminal sentinel;
4. do **not** merely append the one discovered fixture and preserve the old `complete=true` claim;
5. publish a repaired handoff only after the coverage proof passes again.

## Output
If actionable-complete and ZIP validation passes, first persist `Packaging Complete=true`, `Current Stage=COMPLETE`, `Run Status=COMPLETE`, final counts, cleared `Resume Cursor`, empty `Retry Queue`, package name and final checkpoint timestamp.

Then return:

`AiScore actionable coverage ready — run_id=<RUN_ID>; X to Work; Y actionable senior checked; Z discovered excluded; date_envelope=PASS; terminal_scan=PASS; admitted_time_integrity=PASS; raw_audit_complete=true/false; Airtable coverage PASS; work_ready=true; admitted ICT kickoffs verified; handoff_package=ZIP.`

Attach the ZIP Work handoff only.

If an actionable gap remains:

`STEP 0 INCOMPLETE — ACTIONABLE COVERAGE GAP — do not send to Work.`

If the handoff text is valid but ZIP packaging fails:

`HANDOFF PACKAGING FAILED — DO NOT SEND TO WORK.`

Do not print the full fixture list unless the user asks.