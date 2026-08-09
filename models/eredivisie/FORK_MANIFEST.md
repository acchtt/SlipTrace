# Eredivisie Fork Manifest

## Fork identity

- Child model: **SlipTrace Eredivisie v0.1**
- Fork date: 2026-08-09
- Parent repository: `acchtt/SlipTrace`
- Frozen parent repository ref: `dd5d32a24b624ab32e4b7175e572ade5e26f2a8d`
- Parent active football model at fork: **Football v0.2.41**
- Parent football CURRENT_MODEL latest commit at fork: `d13f03e25911e81ae5e9cd0a2d4394d4d0df06d6`

This ref is the methodological fork point. Do not resolve inherited files from mutable `main` when reproducing the v0.1 parent skeleton.

## Frozen inherited load set

At ref `dd5d32a24b624ab32e4b7175e572ade5e26f2a8d`, load:

1. `models/football/ORGANIZED_FILE_LOADING_GUIDE.md`
2. `models/LEGACY_MODEL_CHANGELOG.md` for the retained pre-v0.2.5 football baseline only
3. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
4. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE_ADDENDUM_2026-08-01.md`
5. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.5.md` through `MODEL_RULES_FOOTBALL_V0.2.41.md` in ascending version order
6. `models/football/procedures/FOOTBALL_PRE_VERDICT_VALIDATOR.md`

The child model inherits the **methodological rules and procedures**, subject to local Eredivisie overrides.

## Parent-state exclusions

Do not import the following as child operating state:

- general-football circuit-breaker progress;
- general-football Airtable records;
- football ledger/accounting entries;
- current official/open positions;
- current shadow positions;
- match-specific state from non-Eredivisie fixtures;
- non-Eredivisie competition priors.

The child has its own shadow-calibration mode and its own Airtable control base.

## Conflict resolution

Apply in this order:

1. frozen inherited parent methodology;
2. `models/eredivisie/rules/MODEL_RULES_EREDIVISIE_V0.1.md`;
3. newer Eredivisie rules in ascending version order when later created;
4. current Eredivisie validator and operating-state documentation.

When a frozen parent file contains an old operating value that conflicts with a newer inherited football rule or this child's explicit operating values, the newer rule/local child value controls.

## No automatic upstream sync

After this fork, changes under `models/football/` are **not automatically inherited**.

To merge a later general-football improvement into Eredivisie:

1. identify the exact upstream rule/procedure change and commit;
2. explain why it is league-agnostic and relevant to Eredivisie;
3. test for conflict with Eredivisie calibration;
4. create an explicit Eredivisie version change documenting the merge;
5. never silently move the parent ref.

## Design intent

The parent skeleton governs *how* decisions are made. The Eredivisie calibration layer learns *what priors and distributions* should feed that process for this league.
