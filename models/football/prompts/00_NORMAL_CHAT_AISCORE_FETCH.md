# 00 — Normal Chat: AiScore Fetch + Coverage

**Use in:** Normal Chat, high reasoning.

## Purpose
Build the complete AiScore fixture universe for the requested ICT window, apply the current competition-eligibility rules and active sweep-scope filter, persist the minimal coverage skeleton to Airtable, and export only actionable fixtures to Work.

## Source of truth
Repository: `acchtt/SlipTrace`

Always read `models/football/CURRENT_MODEL.md` first.

Do **not** infer the active model version from this prompt. Use the official model, active patches, canonical timezone, fixture authority, competition rules, and load order declared by `CURRENT_MODEL.md` at execution time.

For this stage, also load:

`models/football/procedures/FOOTBALL_SWEEP_SCOPE.md`

This is the active operational scope filter for national leagues. `CURRENT_MODEL.md` remains higher authority if there is ever a direct conflict.

For this stage, load only the current files relevant to fixture discovery, time/schedule integrity, coverage, sweep scope, and eligibility. At minimum include the active time/schedule integrity procedure, `FOOTBALL_SWEEP_SCOPE.md`, and coverage contract declared by the current model. Do not load downstream betting/live files unless a genuine integrity fault requires them.

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
4. applies `FOOTBALL_SWEEP_SCOPE.md`;
5. applies the competition overlay from `CURRENT_MODEL.md` exactly;
6. batch-upserts the cheap coverage skeleton to Daily Coverage Ledger;
7. creates a compact actionable handoff for Work.

This stage does **not**:
- research match quality;
- assign PRE grades or board ranks;
- fetch XI or bookmaker odds;
- evaluate goal burden, regime, or price;
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

## Sweep scope
Apply `FOOTBALL_SWEEP_SCOPE.md` before any deep structural research.

For domestic national leagues:
- only the explicit core national-league set in `FOOTBALL_SWEEP_SCOPE.md` is actionable by default;
- all other domestic national leagues are excluded as `NON-CORE NATIONAL LEAGUE` unless the user explicitly approves a temporary override;
- top-flight/professional status alone does not bypass this filter;
- all Finnish domestic leagues remain a hard exclusion at every tier/category.

Do not silently promote a league because it produced good results in a prior slate or was manually reviewed once.

The raw AiScore fixture universe must still include these excluded fixtures for reconciliation; they simply must not be sent to Work.

## Eligibility
After sweep-scope filtering, apply the current competition overlay from `CURRENT_MODEL.md` and current coverage contract.

Do not use attractiveness or match-level research to decide eligibility.

If the user explicitly requests a temporary test competition that conflicts with the repo, do not silently alter the canonical model. Either follow an already-versioned repo exception or label the request as a temporary user override for that run.

## Airtable coverage skeleton
Batch-upsert **every raw AiScore fixture**, including excluded and schedule-integrity-unresolved rows, so coverage remains auditable.

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

For actionable rows, leave official PRE fields for Work. XI/market remain pending/user-supplied later.

Efficiency:
- batch upserts up to connector limit;
- no per-row readback;
- one final reconciliation is enough;
- do not touch Decision States or Website Picks.

## Compact Work handoff
Create `AISCORE_FIXTURES_YYYY-MM-DD.txt`.

Use compact JSON-compatible text. Include:
- ICT slate date/window;
- model version read from `CURRENT_MODEL.md`;
- source = AiScore;
- sweep scope = `FOOTBALL_SWEEP_SCOPE.md`;
- actionable fixtures;
- AiScore identity/time fields where available;
- audit counts: raw, actionable, excluded, duplicates, unresolved, complete, coverage skeleton published.

Only actionable and schedule-integrity-cleared fixtures go in the Work fixture array.

## Reconciliation
Before `complete:true`:

`Universe = Actionable eligible + Excluded`

Verify every fixture is accounted for exactly once and every touched AiScore date block/terminal interval was checked.

Also verify:
- no non-core national league survived into the Work handoff without an explicit temporary override;
- no Finnish domestic league survived the sweep scope.

## Output
Reply compactly:

`AiScore ready — X actionable / Y raw; Z excluded; N unresolved; Airtable coverage skeleton PASS/FAIL.`

Attach the handoff file. Do not print the full fixture list unless the user asks.