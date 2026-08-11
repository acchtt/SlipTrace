# Current Football Model

**Canonical namespace:** `models/football/`

- Active model: **Football v0.2.42 — AUDIT MODE**
- Organized loading guide: `models/football/ORGANIZED_FILE_LOADING_GUIDE.md`
- Main procedure: `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
- Procedure addendum: `models/football/procedures/FOOTBALL_BETTING_PROCEDURE_ADDENDUM_2026-08-01.md`
- Mandatory validator: `models/football/procedures/FOOTBALL_PRE_VERDICT_VALIDATOR.md`
- Airtable control map: `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`
- Active rule directory: `models/football/rules/`
- Active audit: `models/football/reviews/FOOTBALL_DIRECTIONAL_AUDIT_2026-08-11.md`
- Active cross-chat handoff: `models/football/handoffs/CHAT_TRANSFER_HANDOFF_2026-08-06.md`
- Historical baseline: `models/LEGACY_MODEL_CHANGELOG.md`
- Authoritative betting feed: `/ledger.json`

## Required load order

Load the following in this order, applying newer rules over older conflicts:

1. `models/football/ORGANIZED_FILE_LOADING_GUIDE.md`
2. `models/LEGACY_MODEL_CHANGELOG.md` for the retained pre-v0.2.5 baseline
3. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
4. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE_ADDENDUM_2026-08-01.md`
5. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.5.md` through `MODEL_RULES_FOOTBALL_V0.2.42.md`, in ascending version order
6. `models/football/procedures/FOOTBALL_PRE_VERDICT_VALIDATOR.md`
7. `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`
8. `models/football/reviews/FOOTBALL_DIRECTIONAL_AUDIT_2026-08-11.md`
9. `models/football/handoffs/CHAT_TRANSFER_HANDOFF_2026-08-06.md`
10. `/ledger.json` when official record, bankroll, exposure, placement or settlement status is relevant

## Audit-mode operating values

- 1u = 1,000,000 VND
- Minimum odds reference remains 1.70
- **Official football betting is paused.**
- **Shadow calibration only until the audit exit criteria are met and the user explicitly approves resumption.**
- Directional Asian handicaps, DNB and ML selections are under quarantine from official promotion.
- Totals are not automatically approved; they remain subject to the normal validator and audit comparison.
- No match-specific rule patch can by itself restore official betting.
- Ledger writes remain on hold until explicitly approved.
- Every assessment must continue to scan all major market families and preserve exact timestamp/state synchronization.
- xG/xGOT remain secondary only, and may be discarded entirely when the provider feed is demonstrably unreliable.

## Audit trigger

Recent verified football performance discussed in project state is materially below acceptable calibration: 2 wins and 7 losses across nine recent actual/shadow selections, including a 0-5 directional-handicap subset across Necaxa +0.5, San Diego +1.5, Port Vale +1, Deportivo Cuenca -0.5, and Tainan City -0.25.

This does not establish that fading the model is profitable. It does establish that the current directional decision boundary is not trusted for real-money execution.

## Audit protocol

For each reviewed decision, reconstruct the original timestamp using only information available at that time. Compare:

- actual model selection;
- NO BET;
- opposite side if the exact comparable market was verifiably available;
- best eligible total;
- protected side/favorite alternative where applicable.

Classify failure modes using the audit taxonomy in `FOOTBALL_DIRECTIONAL_AUDIT_2026-08-11.md`.

## Exit criteria

Official football betting cannot resume until all of the following are satisfied:

- at least 20 newly assessed shadow decisions after audit start;
- at least 10 directional-eligible decision points;
- no retrospective rewriting of decision states;
- directional shadow ROI non-negative over the audit sample OR a clearly superior non-directional market family is demonstrated with adequate sample;
- no unresolved repeated structural loss pattern;
- a formal simplification review states which rules are retained, removed or consolidated;
- explicit user approval to restore official betting.

## Existing model controls retained

- Full synchronization after every material event.
- Hard pre-verdict validator and Airtable decision-state logging remain required for any shadow candidate.
- One best expression per assessment.
- Competition-format and utility verification.
- Side-versus-total comparison under v0.2.42.
- Protected-underdog burden and favorite-first-goal branch requirements under v0.2.41.
- Directional persistence and reset logic under v0.2.33-v0.2.40.

## Response behavior during audit

- Use `SHADOW LEAN — DO NOT PLACE` only when the candidate clears the validator and is being logged for audit purposes.
- Otherwise use `NO BET` or `NO BET — HOLD`.
- Do not issue `OFFICIAL BET` while audit mode is active.
- For directional candidates, explicitly distinguish absolute superiority from relative improvement.
- If the opponent's decisive-event branch remains credible and a total expresses the evidence more cleanly, the side fails best-expression selection.

## Write boundary

All football audit material, reviews, procedures and model updates remain under `models/football/`. `/ledger.json` remains authoritative for official accounting when writes are authorized.
