# 00 — Normal Chat: AiScore Fetch + Coverage

**Use in:** Normal Chat, high reasoning.

## Purpose
Build the complete AiScore fixture universe for the requested ICT window, apply the active quality/sweep filters cheaply, persist the minimal coverage skeleton to Airtable, and export only genuinely actionable fixtures to Work.

The main operational objective is to save Work usage:

`DISCOVER BROADLY -> FILTER CHEAPLY -> DEEP-RESEARCH NARROWLY`

## Source of truth
Repository: `acchtt/SlipTrace`

Always read `models/football/CURRENT_MODEL.md` first.

Do **not** infer the active model version from this prompt. Use the official model, active patches, canonical timezone, fixture authority, competition rules, and load order declared by `CURRENT_MODEL.md` at execution time.

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
1. traverses every AiScore calendar-date block touched by the requested ICT window;
2. normalizes fixture identity and time under the current time/schedule integrity procedure;
3. deduplicates once;
4. applies the active senior-quality exclusions;
5. applies `FOOTBALL_SWEEP_SCOPE.md` and `FOOTBALL_LEAGUE_ENVIRONMENT_REGISTRY.md`;
6. runs only the cheap conditional-league admission test where required;
7. batch-upserts the cheap coverage skeleton to Daily Coverage Ledger;
8. creates a compact **scope-pruned actionable handoff** for Work.

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

If time/date/identity remains inconsistent, keep the row for audit and classify it as schedule-integrity unresolved. Do not send it to Work as actionable.

If the requested AiScore window cannot be fully traversed:
`COVERAGE INCOMPLETE — AiScore sweep incomplete`

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

If it fails, or the necessary cheap evidence is not readily obtainable, retain the row in coverage but exclude it from Work as:

`CONDITIONAL LEAGUE — NO CHEAP OVER SIGNAL`

Do not turn this into a PRE PASS; no full structural verdict has been made.

### LOW-GOAL EXCLUDE
Keep in raw coverage, exclude before Work as:

`LOW-GOAL NATIONAL LEAGUE — EXCLUDED`

### HARD EXCLUDE
All Finnish domestic leagues remain hard excluded under the active registry and existing model rule:

`FINNISH DOMESTIC LEAGUE — HARD EXCLUSION`

## Important survival rule
Do not accidentally remove Norway Eliteserien, Sweden Allsvenskan, Denmark Superliga, Iceland top flight, or Scotland Premiership merely because they are smaller competitions. They are directly admitted by the current registry when otherwise eligible.

## Continental/cup boundary
The domestic-league registry does not automatically exclude independently eligible senior cups or continental competitions. Apply `CURRENT_MODEL.md` and `FOOTBALL_SWEEP_SCOPE.md` to those competitions.

## Airtable coverage skeleton
Batch-upsert **every raw AiScore fixture**, including scope-excluded and schedule-integrity-unresolved rows, so coverage remains auditable.

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
- one final reconciliation is enough;
- do not touch Decision States or Website Picks.

## Compact Work handoff
Create `AISCORE_FIXTURES_YYYY-MM-DD.txt`.

Use compact JSON-compatible text. Include:
- ICT slate date/window;
- model version read from `CURRENT_MODEL.md`;
- source = AiScore;
- sweep scope = `FOOTBALL_SWEEP_SCOPE.md`;
- league registry = `FOOTBALL_LEAGUE_ENVIRONMENT_REGISTRY.md`;
- only fixtures admitted to Work;
- AiScore identity/time fields where available;
- audit counts: raw, direct-admit, conditional-checked, conditional-admit, conditional-excluded, low-goal-excluded, Finnish-hard-excluded, other-quality-excluded, duplicates, unresolved, complete, coverage skeleton published.

The Work fixture array must contain only schedule-integrity-cleared fixtures that survived the active scope.

## Reconciliation
Before `complete:true`:

`Universe = Work-admitted actionable + Excluded`

Verify every raw fixture is accounted for exactly once and every touched AiScore date block/terminal interval was checked.

Also verify:
- no LOW-GOAL EXCLUDE league survived into Work;
- no Finnish domestic league survived into Work;
- no CONDITIONAL league fixture survived without a recorded cheap-gate PASS;
- no quality-excluded youth/reserve/lower/weak-data fixture survived;
- Nordic/Scottish direct-admit leagues were not removed merely for league size.

## Output
Reply compactly:

`AiScore ready — X to Work / Y raw; Z excluded; C conditional checked (A admitted); N unresolved; Airtable coverage skeleton PASS/FAIL.`

Attach the handoff file. Do not print the full fixture list unless the user asks.