# SlipTrace Football Model

This directory contains the **current executable football model stack**.

## Active stack

- **Official model:** Football v0.2.52
- **Base:** Football v0.2.47 CLEAN
- **Official patches:**
  - `rules/MODEL_RULES_FOOTBALL_V0.2.49.md` — Two-Sided Priority
  - `rules/MODEL_RULES_FOOTBALL_V0.2.50.md` — Extreme Goal Environment / Persistent High-Line
  - `rules/MODEL_RULES_FOOTBALL_V0.2.51.md` — Chance-Quality + Market-Confirmation Calibration
  - `rules/MODEL_RULES_FOOTBALL_V0.2.52.md` — Carrier Ceiling + B+ Evidence Hardening
- **Shadow comparisons:** v0.2.47 CLEAN and v0.2.48-SHADOW
- **Fixture authority:** AiScore only
- **Canonical timezone:** Asia/Ho_Chi_Minh (ICT, UTC+7)
- **Actionable scope:** senior-quality overlay
- **Execution workflow:** frozen structural PRE + route-quality/CC+ audit → user-supplied XI + odds → market-history conflict check → final XI / carrier reopen → burden/MCE → official verdict

The authoritative entry point is:

`models/football/CURRENT_MODEL.md`

Do not infer current rules from historical chat handoffs or old model files. Historical versions remain available through Git history rather than the active football tree.

## Canonical files

### Rules

- `rules/MODEL_RULES_FOOTBALL_V0.2.47.md` — immutable clean base inherited by the official model.
- `rules/MODEL_RULES_FOOTBALL_V0.2.49.md` — active official Two-Sided Priority patch.
- `rules/MODEL_RULES_FOOTBALL_V0.2.50.md` — active official Extreme Goal Environment / Persistent High-Line patch.
- `rules/MODEL_RULES_FOOTBALL_V0.2.51.md` — active official chance-quality / market-confirmation calibration.
- `rules/MODEL_RULES_FOOTBALL_V0.2.52.md` — active official carrier-ceiling / B+ evidence-hardening calibration.
- `rules/MODEL_RULES_FOOTBALL_V0.2.48-SHADOW.md` — active shadow comparison rules.

### Procedures

- `procedures/FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md` — authoritative UTC↔ICT normalization, slate-date integrity, near-kickoff status revalidation, and upcoming-schedule rules.
- `procedures/FOOTBALL_MATCH_SWEEP_AND_RESEARCH_PROCEDURE.md` — AiScore-only universe creation, cross-midnight completeness, structural research, route-quality split and mandatory CC+ audit before strong-carrier PASS states.
- `procedures/FOOTBALL_COVERAGE_CONTROLLER.md` — complete-slate screening, FOCUS/WATCHLIST/PASS state, frozen PRE, and coverage invariants.
- `procedures/FOOTBALL_BETTING_PROCEDURE.md` — XI/market-history/carrier-reopen/goal-burden/price/LOCK workflow and live/settlement boundary.

### Airtable contracts

- `airtable/FOOTBALL_COVERAGE_AIRTABLE.md` — Daily Coverage Ledger contract and frozen Work-board persistence, including route-quality/CC+ notes.
- `airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md` — material decision-state logging for official and shadow tracks, including v0.2.52 carrier-reopen and B+ hold states.

## Current operating overlays

The current user-level overlays are part of the canonical operating state:

- exclude youth/Uxx, academy, reserve/B-team/development, amateur/semi-pro, regional/state/provincial, weak small-data leagues, and unapproved domestic lower divisions;
- **exclude every Finnish domestic league competition at every tier/category from 2026-09-09 ICT onward**, including men's and women's leagues; keep these fixtures in raw AiScore coverage as explicit exclusions;
- senior first-team continental competitions are not generically excluded; UCL, UEL and UECL are actionable when otherwise eligible;
- hard executable odds floor 1.65, preferred 1.70+;
- never stretch the total merely to improve price;
- confirmed XI and odds are normally supplied by the user; no official lock without the required current XI + price;
- Work produces and freezes the structural board; later stages preserve PRE history rather than reconstruct it;
- **v0.2.50 EGE:** exceptional high-end goal environments may reopen the supported burden after XI when structure + team profile + XI independently justify it;
- **v0.2.51 MCE:** narrow +0.25 market-confirmed exception only for already-supported A2/B+ TWO-SIDED cases;
- **v0.2.52 route-quality split:** distinguish `TWO-SIDED — QUALITY PROVEN` from `TWO-SIDED — NOMINAL / WEAK SECONDARY`;
- **v0.2.52 CC+:** preserve a secondary `CC+ — CARRIER CEILING` lane for credible self-funded 3+ team-goal potential;
- **v0.2.52 B+ hardening:** XI preservation plus a protected line is not enough to LOCK a fragile B+ compression case; require an independent positive gate;
- **v0.2.52 carrier reopen:** a frozen B/PASS may reopen only through a strict football-led `CARRIER REOPEN — XI CONFIRMED`, never market movement alone;
- early goal-driven line expansion remains a no-chase state;
- Airtable `Z` timestamps are UTC and must be converted exactly once to ICT for display/scheduling;
- upcoming schedules require AiScore status revalidation so already-live or wrong-date fixtures are not presented as upcoming.

## Core hierarchy

Two-Sided Tier A remains the primary lane. For comparable non-Tier-A official v0.2.52 candidates:

`QUALITY-PROVEN TWO-SIDED > CC+ ELITE CARRIER > NOMINAL / WEAK-SECONDARY TWO-SIDED > ordinary CARRIER-LED > FRAGILE / OTHER`

Price is downstream of structure and cannot rescue a structurally weaker candidate.

For goal-burden execution, classify after XI:

`STANDARD` or `EGE — EXTREME GOAL ENVIRONMENT`

EGE changes the supported burden only through documented structural/XI evidence; it is not a price shortcut.