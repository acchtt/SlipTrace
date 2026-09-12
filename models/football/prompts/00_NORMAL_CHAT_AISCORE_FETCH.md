# 00 — Normal Chat: AiScore Fetch + Coverage

**Use in:** Normal Chat, high reasoning.

## Purpose
Build a trustworthy **actionable senior AiScore universe** for the requested ICT window, apply the active quality/sweep filters cheaply, persist the minimal coverage skeleton to Airtable, and export only genuinely actionable fixtures to Work.

The main operational objective is to save Work usage without making Step 0 impossible when AiScore exposes excluded youth/lower/reserve fixtures only through fragmented dynamic snapshots:

`DISCOVER BROADLY -> PROVE ACTIONABLE COMPLETENESS -> FILTER CHEAPLY -> DEEP-RESEARCH NARROWLY`

## Source of truth
Repository: `acchtt/SlipTrace`

Always read the **upstream/default-branch** `models/football/CURRENT_MODEL.md` first.

Do **not** infer the active model version from this prompt or a stale local/cache copy. If local/cache differs from upstream, upstream wins immediately.

Use the official model, active patches, canonical timezone, fixture authority, competition rules, and load order declared by `CURRENT_MODEL.md` at execution time.

For this stage, also load:

- `models/football/procedures/FOOTBALL_SWEEP_SCOPE.md`
- `models/football/procedures/FOOTBALL_LEAGUE_ENVIRONMENT_REGISTRY.md`

These are the active operational filters controlling which domestic leagues are allowed to consume Work research. `CURRENT_MODEL.md` remains higher authority if there is a direct conflict.

Load only the files relevant to fixture discovery, time/schedule integrity, coverage, sweep scope, league admission, and eligibility. Do not load downstream betting/live files unless a genuine integrity fault requires them.

## Airtable
Base: `SlipTrace Football Decision Control`

- Base ID: `appWyZJjitSBATXAU`
- Daily Coverage Ledger: `tblcl1UAyMqZT6Ub0`
- Decision States: `tblQmUpd5WjBLQ38X`
- Website Picks: `tblg3J5sbJYbzuTYD`

Use these IDs directly unless one actually fails.

## Strict stage boundary
This stage:
1. traverses the AiScore date/time blocks needed to account for the requested ICT window;
2. proves coverage of every **potentially actionable senior block** in scope;
3. normalizes fixture identity and time under the current time/schedule integrity procedure;
4. deduplicates once;
5. applies the active senior-quality exclusions;
6. applies `FOOTBALL_SWEEP_SCOPE.md` and `FOOTBALL_LEAGUE_ENVIRONMENT_REGISTRY.md`;
7. runs only the cheap conditional-league admission test where required;
8. batch-upserts the cheap coverage skeleton for fixtures actually discovered;
9. creates a compact **scope-pruned actionable handoff** for Work once the actionable-completeness gate passes.

This stage does **not**:
- perform full match structural research;
- assign PRE grades or board ranks;
- fetch confirmed XI or bookmaker odds;
- evaluate official goal burden, regime, or price;
- create Decision States;
- read/write Website Picks;
- run shadow verdicts;
- issue betting decisions.

## AiScore coverage and schedule integrity
AiScore is the sole fixture-discovery authority unless `CURRENT_MODEL.md` explicitly changes that rule.

For every discovered fixture, preserve where available:
- AiScore fixture ID or canonical match URL;
- listing date used for discovery;
- raw/source kickoff;
- canonical `kickoff_utc`;
- exactly-once converted `kickoff_ict`;
- `slate_date_ict` derived from corrected ICT kickoff;
- status at fetch.

A trailing `Z` is UTC. Never add +7 twice. Never derive Slate Date from raw UTC when the ICT date differs.

If time/date/identity remains inconsistent, keep the discovered row for audit and classify it as schedule-integrity unresolved. Do not send it to Work as actionable.

## Two-tier completeness contract

AiScore may expose the date index through fragmented/dynamic search snapshots. Therefore distinguish:

- `actionable_complete` — every potentially actionable **senior** competition/block in the requested ICT window has been checked and every actionable fixture found is accounted for;
- `raw_audit_complete` — every raw AiScore fixture on the touched date pages, including youth/reserve/lower/amateur/regional/hard-excluded blocks, has been individually enumerated.

`raw_audit_complete=false` is **not automatically a blocker** for Work.

### Blocking gaps

Step 0 must remain `work_ready=false` if any of these remain:

- a PRIORITY or NORMAL senior league block in the requested window is unverified;
- an eligible senior continental/cup block is unverified;
- a senior CONDITIONAL league block is visible/relevant but its cheap gate was not resolved;
- the requested terminal kickoff interval/date boundary was not checked;
- a known potentially actionable senior fixture has unresolved identity/time;
- scope/registry filtering is contradictory;
- admitted count does not match the Work fixture array.

In that case return:

`STEP 0 INCOMPLETE — ACTIONABLE COVERAGE GAP — do not send to Work.`

### Non-blocking raw gaps

Do **not** hold the entire workflow hostage merely because AiScore will not expose an exact one-by-one count for fixtures that are already outside model scope, such as:

- youth/Uxx;
- reserves/B/development;
- amateur/semi-pro;
- regional/state/provincial;
- unapproved lower divisions;
- very weak/obscure competitions;
- LOW-GOAL EXCLUDE domestic leagues;
- Finnish domestic leagues;
- other blocks that are unambiguously hard-excluded before Work.

When such exact raw enumeration is unavailable, record:

- `raw_audit_complete=false`;
- `raw_count_mode=lower_bound`;
- `nonblocking_raw_gaps=[...]` describing the excluded block/category.

Do **not** fabricate an exact raw count.

## Work-readiness gate

A normal Work handoff may be created when all of the following are true:

- `actionable_complete=true`;
- `work_ready=true`;
- all potentially actionable senior blocks in the requested window were checked;
- terminal interval/date verification passed;
- scope/registry audit passed;
- no schedule-integrity unresolved fixture appears in the Work array;
- every admitted fixture is accounted for exactly once;
- admitted count equals the Work fixture array.

For backward compatibility, set `complete=true` when **actionable completeness** passes. Also include `raw_audit_complete` separately so `complete=true` is never misread as a claim that every excluded micro/youth fixture was individually enumerated.

## Quality exclusions
Apply the current senior-quality overlay before league-environment admission.

Do not spend cheap conditional checks on fixtures already excluded as youth/Uxx, reserve/development, amateur/semi-pro, regional/state/provincial, unapproved lower division, or very weak/obscure data environment.

## League environment admission
Use `FOOTBALL_LEAGUE_ENVIRONMENT_REGISTRY.md`.

### PRIORITY / NORMAL
Send surviving fixtures directly to the Work handoff.

### CONDITIONAL
Do **not** send the whole league to Work.

Use only the cheap admission criteria in the registry. The purpose is to decide whether a fixture deserves expensive Work research without performing that research here.

If the cheap signal passes, admit the fixture to Work.

If it fails, or the necessary cheap evidence is not readily obtainable, retain the discovered row in coverage but exclude it from Work as:

`CONDITIONAL LEAGUE — NO CHEAP OVER SIGNAL`

Do not turn this into a PRE PASS; no full structural verdict has been made.

### LOW-GOAL EXCLUDE
Keep discovered fixtures in coverage, exclude before Work as:

`LOW-GOAL NATIONAL LEAGUE — EXCLUDED`

### HARD EXCLUDE
All Finnish domestic leagues remain hard excluded under the active registry and existing model rule:

`FINNISH DOMESTIC LEAGUE — HARD EXCLUSION`

## Important survival rule
Do not accidentally remove Norway Eliteserien, Sweden Allsvenskan, Denmark Superliga, Iceland top flight, or Scotland Premiership merely because they are smaller competitions. They are directly admitted by the current registry when otherwise eligible.

## Continental/cup boundary
The domestic-league registry does not automatically exclude independently eligible senior cups or continental competitions. Apply `CURRENT_MODEL.md` and `FOOTBALL_SWEEP_SCOPE.md` to those competitions.

## Airtable coverage skeleton
Batch-upsert every fixture actually discovered in Step 0, including discovered scope-excluded and schedule-integrity-unresolved rows, so coverage remains auditable.

Do not invent unseen raw fixtures solely to satisfy an exact total count.

Populate only coverage-stage fields needed now, including where supported:
- Coverage ID
- Slate Date
- Match
- Competition
- Kickoff ICT / canonical timestamp semantics
- Eligibility
- Exclusion Reason
- Reconciled
- Source 1 = AiScore
- Coverage Status

For Work-admitted rows, leave official PRE fields for Work. XI/market remain pending/user-supplied later.

Efficiency:
- batch upserts up to connector limit;
- no per-row readback;
- no deep research for excluded leagues;
- no deep research for conditional fixtures unless they first clear the cheap gate;
- do not touch Decision States or Website Picks.

## Compact Work handoff
Create `AISCORE_FIXTURES_YYYY-MM-DD.txt` when `complete:true`, `actionable_complete:true`, and `work_ready:true`.

Use compact JSON-compatible text. Include:
- ICT slate date/window;
- model version read from upstream `CURRENT_MODEL.md`;
- source = AiScore;
- sweep scope = `FOOTBALL_SWEEP_SCOPE.md`;
- league registry = `FOOTBALL_LEAGUE_ENVIRONMENT_REGISTRY.md`;
- `complete:true` meaning actionable completeness;
- `actionable_complete:true`;
- `work_ready:true`;
- `raw_audit_complete:true|false`;
- `raw_count_mode=exact|lower_bound`;
- `nonblocking_raw_gaps` when applicable;
- terminal interval/date traversal result;
- actionable-block audit result;
- coverage skeleton publication result;
- only fixtures admitted to Work;
- AiScore identity/time fields where available;
- counts for the actionable senior universe and discovered excluded fixtures.

The Work fixture array must contain only schedule-integrity-cleared fixtures that survived the active scope.

## Reconciliation
Before `complete:true` / `actionable_complete:true` / `work_ready:true`:

`ACTIONABLE SENIOR UNIVERSE = WORK-ADMITTED + ACTIONABLE-EXCLUDED/UNRESOLVED`

Verify every **potentially actionable senior** fixture/block in the requested window is accounted for exactly once.

Also verify:
- no LOW-GOAL EXCLUDE league survived into Work;
- no Finnish domestic league survived into Work;
- no CONDITIONAL league fixture survived without a recorded cheap-gate PASS;
- no quality-excluded youth/reserve/lower/weak-data fixture survived into Work;
- Nordic/Scottish direct-admit leagues were not removed merely for league size;
- admitted count equals the actual Work fixture array;
- no unresolved schedule-integrity fixture appears in the Work array;
- any `raw_audit_complete=false` gaps are confined to categories already excluded from Work and are listed explicitly.

## Output

If actionable-complete:

`AiScore actionable coverage ready — X to Work; Y actionable senior checked; Z discovered excluded; raw_audit_complete=true/false; Airtable coverage skeleton PASS; work_ready=true.`

Attach the normal Work handoff file.

If an actionable gap remains:

`STEP 0 INCOMPLETE — ACTIONABLE COVERAGE GAP — do not send to Work.`

Do not print the full fixture list unless the user asks.