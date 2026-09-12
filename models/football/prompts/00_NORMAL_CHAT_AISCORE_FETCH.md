# 00 — Normal Chat: AiScore Fetch + Coverage

**Use in:** Normal Chat, high reasoning.

## Purpose
Build a trustworthy **actionable senior AiScore universe** for the requested window, apply the active quality/sweep filters cheaply, persist the minimal coverage skeleton, and export only genuinely actionable fixtures to Work.

Operational principle:

`DISCOVER BROADLY -> PRESERVE SOURCE TIMEZONE -> EXCLUDE CHEAPLY -> PROVE ACTIONABLE COMPLETENESS -> DEEP-RESEARCH NARROWLY`

Do not turn Step 0 into a timezone-conversion exercise.

## Source of truth
Repository: `acchtt/SlipTrace`

Always read upstream/default-branch:

1. `models/football/CURRENT_MODEL.md`
2. `models/football/procedures/FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`
3. `models/football/procedures/FOOTBALL_SWEEP_SCOPE.md`
4. `models/football/procedures/FOOTBALL_LEAGUE_ENVIRONMENT_REGISTRY.md`

The active time procedure uses **source-time preservation at Step 0 and later ICT conversion**. If an older subordinate file still says every fixture must be converted to ICT during discovery, the active time procedure wins.

## Airtable
Base: `SlipTrace Football Decision Control`

- Base ID: `appWyZJjitSBATXAU`
- Daily Coverage Ledger: `tblcl1UAyMqZT6Ub0`
- Decision States: `tblQmUpd5WjBLQ38X`
- Website Picks: `tblg3J5sbJYbzuTYD`

Use these IDs directly unless one actually fails.

## Strict stage boundary
Step 0:

1. traverses AiScore date/competition blocks needed to cover the requested window, including reasonable timezone-boundary spillover;
2. proves coverage of every **potentially actionable senior block**;
3. preserves fixture identity and source kickoff/timezone/offset exactly as supplied by AiScore;
4. deduplicates once;
5. applies senior-quality exclusions;
6. applies sweep scope and league registry;
7. runs only the cheap conditional-league admission test where required;
8. batch-upserts the cheap coverage skeleton for actually discovered fixtures;
9. creates a compact scope-pruned Work handoff when actionable completeness passes.

Step 0 does **not**:

- convert every kickoff to ICT;
- perform full structural match research;
- assign PRE grades or board ranks;
- fetch confirmed XI or bookmaker odds;
- create Decision States;
- touch Website Picks;
- issue betting decisions.

## Source-time capture
For every discovered fixture preserve where available:

- AiScore fixture ID/canonical match URL;
- listing date used for discovery;
- raw/source kickoff text;
- `kickoff_source_local`;
- `source_timezone` and/or `source_utc_offset`;
- AiScore-supplied UTC only when explicitly present;
- status at fetch.

Do **not** guess a timezone from geography.

Do **not** calculate `kickoff_ict` during normal discovery. If the fixture lies near a date/window boundary, carry it as:

`WINDOW STATUS = PENDING CONVERSION`

The later schedule-normalization stage converts the surviving actionable set to ICT and removes out-of-window boundary fixtures.

A missing `kickoff_ict` is therefore **not** a Step-0 integrity failure.

Use `UNRESOLVED — SOURCE TIME INTEGRITY` only when the AiScore source timestamp/zone itself is contradictory or cannot be interpreted later.

## Two-tier completeness contract
Distinguish:

- `actionable_complete` — every potentially actionable senior competition/block relevant to the requested sweep has been checked and every admitted fixture is accounted for;
- `raw_audit_complete` — every raw AiScore fixture, including already excluded youth/lower/reserve/amateur/regional blocks, was individually enumerated.

`raw_audit_complete=false` is non-blocking when gaps are confined to categories already outside model scope.

### Blocking gaps
`work_ready=false` only when an **actionable** requirement remains unresolved, for example:

- PRIORITY/NORMAL senior block not checked;
- eligible senior cup/continental block not checked;
- relevant CONDITIONAL senior block not cheap-gated;
- scope/registry contradiction;
- fixture identity/source-time contradiction that prevents later interpretation;
- admitted count does not match the Work array.

Do **not** block Work because excluded micro/youth/lower fixtures were not individually enumerated.

### Non-blocking raw gaps
Examples:

- youth/Uxx;
- academy/junior;
- reserves/B/development;
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

Do not waste conditional-gate work on these.

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
The table field `Kickoff ICT` must **not** receive a foreign-zone/local source time.

During Step 0:

- leave `Kickoff ICT` blank unless a genuine ICT conversion has already been performed for another reason;
- preserve source local time + zone/offset in the handoff/coverage notes;
- fill `Kickoff ICT` later during schedule normalization.

For Work-admitted rows, leave official PRE fields untouched. XI/market remain pending.

## Work-readiness gate
A Work handoff may be created when:

- `complete=true` meaning actionable completeness;
- `actionable_complete=true`;
- `work_ready=true`;
- all potentially actionable senior blocks were checked;
- scope/registry audit passed;
- no source-time/identity unresolved fixture appears in the Work array;
- admitted count equals the Work fixture array.

`kickoff_ict` is **not required** at this stage.

## Compact Work handoff
Create `AISCORE_FIXTURES_YYYY-MM-DD.txt` when the actionable-completeness gate passes.

Include:

- requested user window and timezone;
- model version;
- source = AiScore;
- sweep scope + league registry;
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
- `window_status=confirmed|pending_conversion`;
- counts.

Do not require `kickoff_ict` in the Step-0 handoff.

## Reconciliation
Before `work_ready=true`:

`ACTIONABLE SENIOR UNIVERSE = WORK-ADMITTED + ACTIONABLE-EXCLUDED/UNRESOLVED`

Verify:

- no LOW-GOAL EXCLUDE fixture survived into Work;
- no hard-excluded domestic-league fixture survived;
- no CONDITIONAL fixture survived without a cheap-gate PASS;
- no youth/reserve/lower/weak-data fixture survived;
- admitted count equals the Work array;
- no source-time integrity unresolved fixture appears in Work;
- raw gaps are explicitly non-blocking and already outside scope.

Boundary fixtures may remain `pending_conversion`; they are pruned during the later ICT schedule-normalization pass.

## Output
If actionable-complete:

`AiScore actionable coverage ready — X to Work; Y actionable senior checked; Z discovered excluded; raw_audit_complete=true/false; Airtable coverage skeleton PASS; work_ready=true; ICT conversion deferred.`

Attach the normal Work handoff.

If an actionable gap remains:

`STEP 0 INCOMPLETE — ACTIONABLE COVERAGE GAP — do not send to Work.`

Do not print the full fixture list unless the user asks.