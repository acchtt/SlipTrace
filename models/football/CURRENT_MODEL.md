# Current Football Model

**Canonical namespace:** `models/football/`

- Active model: **Football v0.2.42**
- Organized loading guide: `models/football/ORGANIZED_FILE_LOADING_GUIDE.md`
- Main procedure: `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
- Procedure addendum: `models/football/procedures/FOOTBALL_BETTING_PROCEDURE_ADDENDUM_2026-08-01.md`
- Mandatory validator: `models/football/procedures/FOOTBALL_PRE_VERDICT_VALIDATOR.md`
- Airtable control map: `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`
- Active rule directory: `models/football/rules/`
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
8. `models/football/handoffs/CHAT_TRANSFER_HANDOFF_2026-08-06.md`
9. `/ledger.json` when official record, bankroll, exposure, placement or settlement status is relevant

Do not load football rules from the repository root. Root model copies were retired during the physical cleanup. The older handoff supplies historical state only and must not override newer active rules or validator controls.

## Active operating values

- 1u = 1,000,000 VND
- Minimum odds: 1.70
- Every executable or shadow LEAN uses exactly 0.25u = 250,000 VND
- **Official football betting is paused under the four-match circuit breaker**
- Circuit breaker: **2/4 completed**; only matches producing an otherwise executable LEAN can count, with at most one designated primary shadow selection per match
- During the circuit breaker use `SHADOW LEAN — DO NOT PLACE`; do not issue a new `OFFICIAL BET`
- `NO BET` matches do not consume a circuit-breaker slot
- After 4/4, review all four shadow matches and require explicit user approval before restoring official betting
- No fixed cumulative same-match exposure cap under v0.2.37 outside the circuit-breaker restriction
- Each additional same-match position normally requires a fresh synchronized assessment, independent edge, correlation disclosure, cumulative-exposure statement and incremental maximum-loss statement
- `One best expression` applies to each reassessment; issue no more than one new executable selection per decision point
- `LEAN — SMALL` is retired for future recommendations
- A wager is official only after confirmed placement and only when official betting is enabled
- Ledger writes remain on hold until explicitly approved
- Every material score, minute, line, card, penalty, substitution, injury, weather, pitch or settlement change requires independent repricing
- Same-state accepted-odds drift of up to 0.08 is permitted under v0.2.36 when the line, settlement scope, score, minute and material state are unchanged, acceptance is within 120 seconds and odds remain at least 1.70
- A decimal-odds move greater than 0.08 requires a fresh synchronized reprice
- The former 1.5-percentage-point implied-probability sub-trigger does not independently invalidate a same-state execution inside the 0.08 tolerance
- Every match-analysis message must include the v0.2.28 assessment-period field
- Every prematch assessment and material live reassessment must independently scan all available major market families under v0.2.29; do not anchor to the previously discussed market
- Before any pick, v0.2.30 requires both teams' relevant scoring/conceding profiles and verified or explicitly classified motivation/result utility
- xG and xGOT are supporting evidence only; future-goal assessment must use multiple independent forward-looking channels. Goal environment is Closed, Neutral or Open only when established; after a material reset it may remain `Unresolved` until persistence is demonstrated
- v0.2.31 separates win, draw and margin utility; requires exact event-budget analysis for goal and corner unders; strengthens high-event late-under and deep-favorite handicap gates; and requires explicit `NO BET — HOLD` unlock conditions when a mandatory gate remains unresolved
- v0.2.32 applies full model parity to reminders, automations and secondary threads; prohibits unsupported precise probabilities and informal executable labels; enforces one-best-expression controls across all surfaces; and treats user-reported cross-thread placements as official positions with ticket details pending
- v0.2.33 adds regime-persistence, directional-switch, candidate-oscillation, one-event binary-market and substitution-cluster controls; invalidating one side never automatically confirms the opposite side
- v0.2.34 requires competition-format verification, separates regulation and shootout utility, adds dual-value tie and pressure-to-urgency gates, strengthens tied-state side switching and further de-emphasizes xG/xGOT
- v0.2.35 requires a fresh LEAN-or-NO-BET decision once a stated HOLD unlock is satisfied and mandates side-versus-one-goal-over comparison when persistent pressure develops in a tied match
- v0.2.36 increases same-state execution odds tolerance to 0.08 and retires the independent implied-probability sub-trigger inside that range
- v0.2.37 removes the fixed same-match exposure cap while preserving 0.25u per executable LEAN, one new selection per reassessment and explicit correlation/exposure controls
- v0.2.38 preserves protected handicap settlement, strengthens live favourite-fade and directional-switch gates, and prohibits using shots on target alone as scoring-superiority evidence
- v0.2.39 strengthens **prematch** favourite-fade and margin-risk analysis, vetoes formation/possession narratives as standalone protection evidence, gives friendly H2H near-zero decision weight, and activates the four-match football circuit breaker
- v0.2.40 adds the **hard pre-verdict validator**, Airtable-backed decision-state write lock, xG enforcement lock, regime-consistency lock, competition-utility propagation lock and mandatory two-channel primary-evidence minimum
- v0.2.41 strengthens **protected-underdog deep-favourite validation**: at least two affirmative margin-suppression channels, mandatory favourite-first-goal branch testing, exact tiebreak-order propagation, and Airtable margin-branch fields are required before a large protected underdog can pass
- v0.2.42 strengthens **live market-expression selection**: distinguishes directional superiority from event-generation superiority, requires a side-versus-eligible-total comparison when the opponent retains a credible scoring route, forces adjacent quarter-goal totals into the scan, and requires an independent directional separator before a pressure-driven side can beat a less direction-dependent goal expression

## Hard pre-verdict enforcement

Before any `SHADOW LEAN — DO NOT PLACE`, `LEAN`, or `OFFICIAL BET`:

1. complete `FOOTBALL_PRE_VERDICT_VALIDATOR.md`;
2. create the corresponding Airtable `Decision States` record;
3. require `Validator Result = PASS`;
4. while the circuit breaker is active, output only `SHADOW LEAN — DO NOT PLACE` and create a corresponding `Circuit Breaker` record.

If validation is `HOLD` or `FAIL`, do not promote the candidate. If Airtable decision-state validation is unavailable, return `NO BET — HOLD — decision-state validation unavailable` rather than bypassing the control.

For any prematch protected-underdog candidate against a material/deep favourite, Airtable must additionally show:

- `Underdog Suppression Evidence Count >= 2`;
- `Favorite First-Goal Branch = Pass`;
- `Margin Incentive Propagated = true` when competition margin/tiebreak incentives are relevant.

Failure of any applicable condition forces `NO BET`.

For any applicable v0.2.42 live pressure-side candidate, the validator must additionally establish:

- the best eligible total expression, including adjacent quarter-goal lines when necessary;
- exact side and total settlement paths;
- the opponent threat classification;
- at least one independent directional separator beyond generic pressure/event-generation evidence.

If another goal is better supported than which team scores it, the side cannot pass the best-expression test.

## Airtable operational control

- Base: `SlipTrace Football Decision Control`
- Base ID: `appWyZJjitSBATXAU`
- Decision States table: `tblQmUpd5WjBLQ38X`
- Circuit Breaker table: `tblcJfh8zbNyzjArK`
- Full field map: `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`

Airtable is an operational decision-control log only. `/ledger.json` remains authoritative for official accounting when writes are authorized.

## Response scope and brevity

- Keep live reassessments brief and decision-first.
- Assess recent relevant H2H and home/away form only in the prematch preview.
- Do not repeat H2H or team-form sections during live reassessments unless the user explicitly requests them.
- Do not print the full validator checklist unless the user requests it; surface only decisive failed/unresolved gates and unlock conditions.

## Active position and reconciliation state

- Latest completed circuit-breaker shadows:
  - **Slot 1: Singapore +1 @1.75 vs Indonesia — WON**, simulated 0.25u; P/L **+0.1875u = +187,500 VND**; process validity: Valid.
  - **Slot 3: Deportivo Cuenca -0.5 @2.45 vs Manta — LOST**, simulated 0.25u; final score Cuenca 1-2 Manta; P/L **-0.25u = -250,000 VND**. Review classification: **model-attributed market-expression error**. Cuenca pressure was real, but the model over-promoted directional win probability from evidence that more cleanly supported continued event generation. At the synchronized snapshot, Over 2.75 @1.88 was the superior eligible expression because one further goal produced a half-win regardless of scorer while Manta retained a credible transition/scoring route.
- Circuit-breaker Slot 2: Wolves vs Port Vale, Port Vale +1 @2.00, remains counted in Airtable but result/process completion is not treated as verified here until reconciled.
- Portland Timbers vs Puebla: latest user-supplied synchronized snapshot before v0.2.40 activation was Portland 5-1 Puebla at approximately 58:01. The 5-1 goal created a new reset epoch; no post-goal shadow selection was validated and the match did not consume a circuit-breaker slot.
- Club América vs San Diego FC: **San Diego FC +1.5 @1.89 — user confirmed loss at final score América 3-1 San Diego.** Expected stake 0.25u; ticket ID, actual stake and placement timestamp remain pending. Review classification: **model-attributed prematch selection error**. The pick failed to establish two independent margin-suppression channels, did not pass a favourite-first-goal branch, overvalued nominal 5-3-2/protection and friendly H2H, underweighted San Diego's adverse away margin tail, and incompletely propagated Leagues Cup margin incentives. Ledger not updated.
- Chicago Fire vs Necaxa: Necaxa +0.5 @1.89 — user confirmed loss. Review classified the selection as a model-attributed market-promotion error: the model reduced protection from the watched +0.75 line and overweighted shots on target without sufficient high-value access. Expected stake 0.25u; ticket details and exact settlement evidence remain pending. Ledger not updated.
- Jagiellonia Białystok DNB @1.94: user confirmed win; expected stake 0.25u, ticket details pending, ledger not updated.
- Shanghai Port -0.5 @1.83: user confirmed loss; ledger reconciliation required.
- Laos vs Philippines Under 3.5 @1.87: user confirmed loss; ledger reconciliation required.
- Do not assume any current score, clock, event, lineup or market state without fresh user evidence.
- Ledger write remains unauthorized.

## Circuit-breaker state

- Football circuit breaker: **2/4 completed**.
- Slot 1: **Singapore +1 @1.75 vs Indonesia — WON, +0.1875u simulated P/L, process valid**.
- Slot 2: **Port Vale +1 @2.00 vs Wolves — counted, result/process completion pending reconciliation**.
- Slot 3: **Deportivo Cuenca -0.5 @2.45 vs Manta — LOST, -0.25u simulated P/L; market-expression error reviewed under v0.2.42**.
- New football positions are shadow only.
- A match counts only if a normal executable LEAN would otherwise clear all active rules, the hard validator returns PASS, the Airtable Decision States write exists, one primary shadow selection is designated, and the result is later verified.
- Track selection, line, odds, state, result, simulated P/L and process validity in the Airtable `Circuit Breaker` table.
- Official execution can resume only after the 4/4 review and explicit user approval.

## Write boundary

All new football rules, procedures, context, handoffs, Airtable-control documentation and reviews must be written under `models/football/`. Shared policies belong under `shared/`. Do not create new football model files at the repository root.