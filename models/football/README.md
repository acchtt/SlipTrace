# SlipTrace Football Model

This directory contains the **current executable football model stack**.

## Active stack

- **Official model:** Football v0.2.49
- **Base:** Football v0.2.47 CLEAN
- **Official patch:** `rules/MODEL_RULES_FOOTBALL_V0.2.49.md`
- **Shadow comparisons:** v0.2.47 CLEAN and v0.2.48-SHADOW
- **Fixture authority:** AiScore only
- **Actionable scope:** senior-quality overlay
- **Execution workflow:** frozen structural PRE → user-supplied XI + odds → official verdict

The authoritative entry point is:

`models/football/CURRENT_MODEL.md`

Do not infer current rules from historical chat handoffs or old model files. Historical versions remain available through Git history rather than the active football tree.

## Canonical files

### Rules

- `rules/MODEL_RULES_FOOTBALL_V0.2.47.md` — immutable clean base inherited by the official model.
- `rules/MODEL_RULES_FOOTBALL_V0.2.49.md` — active official Two-Sided Priority patch.
- `rules/MODEL_RULES_FOOTBALL_V0.2.48-SHADOW.md` — active shadow comparison rules.

### Procedures

- `procedures/FOOTBALL_MATCH_SWEEP_AND_RESEARCH_PROCEDURE.md` — AiScore-only universe creation, cross-midnight completeness, research separation, and senior-quality filtering.
- `procedures/FOOTBALL_COVERAGE_CONTROLLER.md` — complete-slate screening, FOCUS/WATCHLIST/PASS state, frozen PRE, and coverage invariants.
- `procedures/FOOTBALL_BETTING_PROCEDURE.md` — XI/goal-burden/price/LOCK workflow and live/settlement boundary.

### Airtable contracts

- `airtable/FOOTBALL_COVERAGE_AIRTABLE.md` — Daily Coverage Ledger contract and frozen Work-board persistence.
- `airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md` — material decision-state logging for official and shadow tracks.

## Current operating overlays

The current user-level overlays are now part of the canonical operating state:

- exclude youth/Uxx, academy, reserve/B-team/development, amateur/semi-pro, regional/state/provincial, weak small-data leagues, and unapproved domestic lower divisions;
- **exclude every Finnish domestic league competition at every tier/category from 2026-09-09 ICT onward**, including men's and women's leagues; keep these fixtures in raw AiScore coverage as explicit exclusions;
- this Finnish-league rule includes Veikkausliiga and all lower-tier Finnish leagues, but does not automatically exclude Finnish Cup or UEFA club competitions involving Finnish clubs;
- senior first-team continental competitions are not generically excluded; UCL, UEL and UECL are actionable when otherwise eligible;
- hard executable odds floor 1.65, preferred 1.70+;
- never stretch the total merely to improve price;
- confirmed XI and odds are normally supplied by the user; no official lock without the required current XI + price;
- Work produces and freezes the structural board; later stages must preserve that PRE state rather than reconstruct it.

## Core hierarchy

For comparable official v0.2.49 grades:

`TWO-SIDED > ELITE CARRIER > CARRIER-LED > FRAGILE / OTHER`

Price is downstream of structure and cannot rescue a structurally weaker candidate.
