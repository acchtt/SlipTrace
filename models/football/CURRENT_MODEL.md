# Current Football Model

**Canonical namespace:** `models/football/`

- Active model: **Football v0.2.43 — AUDIT MODE**
- Organized loading guide: `models/football/ORGANIZED_FILE_LOADING_GUIDE.md`
- Main procedure: `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
- Procedure addendum: `models/football/procedures/FOOTBALL_BETTING_PROCEDURE_ADDENDUM_2026-08-01.md`
- Mandatory validator: `models/football/procedures/FOOTBALL_PRE_VERDICT_VALIDATOR.md`
- Airtable control map: `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`
- Active rule directory: `models/football/rules/`
- Active audit: `models/football/reviews/FOOTBALL_DIRECTIONAL_AUDIT_2026-08-11.md`
- Parallel early-totals benchmark: `models/football/reviews/FOOTBALL_V026_V029_BENCHMARK_PROTOCOL_2026-08-11.md`
- Active cross-chat handoff: `models/football/handoffs/CHAT_TRANSFER_HANDOFF_2026-08-12.md`
- Historical baseline: `models/LEGACY_MODEL_CHANGELOG.md`
- Authoritative betting feed: `/ledger.json`

## Required load order

Load the following in this order, applying newer rules over older conflicts:

1. `models/football/ORGANIZED_FILE_LOADING_GUIDE.md`
2. `models/LEGACY_MODEL_CHANGELOG.md` for the retained pre-v0.2.5 baseline
3. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
4. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE_ADDENDUM_2026-08-01.md`
5. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.5.md` through `MODEL_RULES_FOOTBALL_V0.2.43.md`, in ascending version order
6. `models/football/procedures/FOOTBALL_PRE_VERDICT_VALIDATOR.md`
7. `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`
8. `models/football/reviews/FOOTBALL_DIRECTIONAL_AUDIT_2026-08-11.md`
9. `models/football/reviews/FOOTBALL_V026_V029_BENCHMARK_PROTOCOL_2026-08-11.md`
10. `models/football/handoffs/CHAT_TRANSFER_HANDOFF_2026-08-12.md`
11. `/ledger.json` when official record, bankroll, exposure, placement or settlement status is relevant

The older `CHAT_TRANSFER_HANDOFF_2026-08-06.md` is historical context only and must not override this file, v0.2.43, or the 2026-08-12 handoff.

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

## Mandatory style layer — v0.2.43

This layer is STRICT and applies to current and future chats.

Before every serious match preview, and before the first live recommendation in a match, both teams must have an evidence-based style profile covering:

- base build-up and tempo;
- primary attacking routes;
- defensive block/press;
- transition behaviour;
- chance-generation signature;
- typical behaviour after taking a lead;
- typical behaviour after falling behind;
- expected matchup-specific adaptation;
- confidence/sample caveat.

Always distinguish `Base style` from `Expected matchup style`. Reputation alone is insufficient.

If the style profile is materially incomplete, use `STYLE PROFILE INCOMPLETE` and cap the prematch verdict at `NO BET — HOLD`.

Every goal causes a tactical/state reset. After a goal, no live candidate may be justified merely by generic chase/counter logic. Before any shadow candidate, explicitly report:

- `Prematch style expectation:`
- `Leader post-goal behaviour:`
- `Trailer post-goal behaviour:`
- `Style deviation:`
- `Post-goal persistence:`
- `Market implication:`

Normally require two comparable post-goal observations, or one observation plus strong event-level evidence across a meaningful interval. Compare actual behaviour with the prematch profile and classify it as `AS EXPECTED`, `MORE OPEN THAN EXPECTED`, `MORE CLOSED THAN EXPECTED`, or `STYLE BREAK / UNRESOLVED`.

## Parallel benchmark mode

Every suitable synchronized live football checkpoint with an available totals board now supports two shadow-only research outputs:

- **Arm A — Current audit model:** Football v0.2.43 with all active validator, style and audit controls. It still scans all major market families, but directional markets remain quarantined.
- **Arm B — Early totals benchmark:** reconstructs the narrower v0.2.6-v0.2.9 live-total philosophy using current synchronization, provider-quality and v0.2.43 style controls. It evaluates totals only and may output `BENCHMARK SHADOW` or `BENCHMARK NO BET`.

The benchmark does **not** roll the active model back to v0.2.6 or v0.2.9. Historical samples are too small, and v0.2.7 itself was negative. The purpose is to test whether live totals plus settlement protection have more stable signal than directional handicap selection.

For Arm B, prioritize exact score/minute, remaining-goal branches, adjacent total lines, boundary protection, state resets, competition utility, reliable non-xG forward evidence, team-specific post-goal behaviour and NO BET discipline. Evaluate both Over and Under; do not create a new automatic Under or Over bias.

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

For new live checkpoints, also score Arm B under `FOOTBALL_V026_V029_BENCHMARK_PROTOCOL_2026-08-11.md` when the totals board and settlement scope are sufficiently synchronized. Track the v0.2.43 style expectation and post-goal deviation prospectively rather than backfilling after the result.

## Exit criteria

Official football betting cannot resume until all of the following are satisfied:

- at least 20 newly assessed shadow decisions after audit start;
- at least 10 directional-eligible decision points;
- no retrospective rewriting of decision states;
- directional shadow ROI non-negative over the audit sample OR a clearly superior non-directional market family is demonstrated with adequate sample;
- no unresolved repeated structural loss pattern;
- a formal simplification review states which rules are retained, removed or consolidated;
- explicit user approval to restore official betting.

The early-totals benchmark cannot shorten the audit. Its first review requires 20 synchronized live decision points and, if naturally generated, at least 10 benchmark shadow selections. Promotion consideration requires a materially larger settled sample as defined in its protocol.

The v0.2.43 style layer requires a prospective review after 20 qualifying live checkpoints including at least 10 post-goal states.

## Existing model controls retained

- Full synchronization after every material event.
- Hard pre-verdict validator and Airtable decision-state logging remain required for any Arm A shadow candidate.
- One best expression per assessment.
- Competition-format and utility verification.
- Side-versus-total comparison under v0.2.42.
- Protected-underdog burden and favorite-first-goal branch requirements under v0.2.41.
- Directional persistence and reset logic under v0.2.33-v0.2.40.
- Mandatory team-style and post-goal behaviour profiling under v0.2.43.

## Response behavior during audit

- Use `SHADOW LEAN — DO NOT PLACE` only when an Arm A candidate clears the validator and v0.2.43 style gate and is being logged for audit purposes.
- Otherwise use `NO BET` or `NO BET — HOLD` for Arm A.
- When enough synchronized total-market information exists, also report the Arm B research verdict separately as `BENCHMARK SHADOW — DO NOT PLACE` or `BENCHMARK NO BET`.
- Do not issue `OFFICIAL BET` while audit mode is active.
- For directional candidates, explicitly distinguish absolute superiority from relative improvement.
- If the opponent's decisive-event branch remains credible and a total expresses the evidence more cleanly, the side fails best-expression selection.
- After any goal, satisfy the mandatory v0.2.43 post-goal fields before issuing a new shadow candidate.

## Write boundary

All football audit material, reviews, procedures and model updates remain under `models/football/`. `/ledger.json` remains authoritative for official accounting when writes are authorized.
