# Football C — independent goal-route research repair and frozen proof-gap replay

**Date:** 2026-10-26 ICT  
**Status:** IMPLEMENTED ON TRIAL BRANCH / NOT PREDICTIVELY PROMOTED  
**Base:** production main `5e48b05cadf3f789d261c4065eb559ab79b37e80`  
**Scope:** /rank source evidence, not C predictive grades or /xi. C2/C3/C4 stay retired.

## Implementation

- `models/football/engine/goal_route_proof.py`: versioned, prospective source-level evidence proof `SOURCE_INDEPENDENT_GOAL_PATHS_V1`. Requires specific fact IDs + source references + prematch observation times for goal-three primary, independent reply or independently self-funded carrier, two-goal endpoint, fourth-goal continuation and main failure. Maps reliability, chance, failure, completion and continuation grades to explicit facts.
- Research fails closed on recycled **identical fact IDs** for main and independently claimed opponent reply, on G4 using only the same primary-goal facts, or on all five predictive grade dimensions reusing the exact same factual set. Repeated *web URLs alone* remain a warning, not a veto: one official report can describe several separate facts.
- `models/football/stages_v4/stage.py`: explicit opt-in `c.goal_route_proof_contract=SOURCE_INDEPENDENT_GOAL_PATHS_V1`; reviews **every** assessed fixture (including C-WATCH/PASS) before G4 preflight, checkpoints incomplete rows as `GOAL_ROUTE_PROOF_PENDING`, preserves full-cohort accounting, frozen input, exact missing-fields, and source-window checks. Incomplete means **unresolved research**, not loss or C-PASS.
- `models/football/stages_v4/RANK.md`: required source-fact workflow and sample field semantics.
- Existing compiled C G3/G4/G5, production ranking/FOLLOW, screenshot odds, XI, no backfill and actual bet accounting **unchanged**. Legacy sealed rank payloads without the opt-in contract are unaffected.

## Sealed-board readiness replay

| Board | Frozen C assessment epochs | New source-proof present | Three-plus predictive grades sharing an exact reference set |
|---|---:|---:|---:|
| Oct 23 15:00–21:00 | 7 | 0 | 7 |
| Oct 23 21:00–03:00 | 20 | 0 | 20 |
| Oct 24 07:26–12:00 | 5 | 0 | 2 |
| Oct 24 10:46–12:00 | 7 | 0 | 4 |
| Oct 24 18:00–00:00 | 27 | 0 | 19 |
| Oct 25 00:00–07:30 | 18 | 0 | 11 |
| Oct 25 09:09–12:00 | 12 | 0 | 5 |
| Oct 25 main 15:00–03:00 | 54 | 0 | 45 |
| Oct 26 07:44–11:00 | 2 | 0 | 1 |
| **Total** | **152** | **0** | **114** |

**Method:** reopened the nine original sealed rank JSON files, extracted each receipt's `frozen_model_input.matches` without changing evidence, and counted exact repeated `evidence_refs` sets across at least three of five quality dimensions (`route_reliability`, `chance_quality`, `failure_resistance`, `burden_completion_quality`, `continuation_quality`). For a historical row without the newly introduced `goal_route_proof` object, an *opted-in counterfactual new contract* would return `GOAL_ROUTE_PROOF_PENDING`, not a reconstructed negative decision.

The 114 source-set duplicates **do not mean** 114 faulty predictions or that source citations themselves must be separate. They mean the frozen record does not demonstrate factual independence from citation lists alone. The original 152 have no new fact-ID proof, so **0 can be retrospectively validated as fully research-complete under the proposed source contract** without collecting new evidence. This is a research-readiness audit, not a proof of prediction lift.

## Existing result baseline is not overwritten

- The previously reconciled 44 /xi distinct fixtures contain 37 funded G3+, 20 reached 3+, and 16 full repaired certificate clears. This prospective proof schema does not regrade or recalculate these outcomes.
- Earlier production FOLLOW replay has 41 slots and 23 original protected certificate clears (56.1%). No claimed improvement from the new proof schema is justified yet.
- The rejected V1 numerical selection challenger (draft PR #199) selected 7 matches, all on one slate, and deteriorated Oct 25 certificate clears to 3/7 versus repaired production 4/7. This repair does **not** promote it.

## Promotion gate

1. Obtain real, separately identifiable current football facts during fresh prematch /rank research across multiple days. The required dated route, reply, endpoint and failure evidence must be collected before kickoff and before reading outcomes.
2. Run the new opt-in field contract prospectively in one parallel Work /rank branch, preserving production behavior. Record `COMPLETE` versus `GOAL_ROUTE_PROOF_PENDING`; use a bounded source pass and never delete unexplained pending fixtures.
3. Re-evaluate **matched** proposed-vs-production candidates on common evidence. Measure rejected 3+/4+ winners, promoted failures, exact Asian burden settlement, timestamped quote availability and first-goal time. Missing bookmaker screenshots remain unknown rather than invented.
4. Do not make stricter proof automatically equal STOP or G3 lost. Deploy predictive rule changes only after a holdout demonstrates multi-day improvements without destroying recall. An old final score is never evidence for a new prospective route.
5. Maintain the scope: non-African women's top flights included; Africa/friendlies excluded; no /xi modifications.

**Decision:** The source-independence evidence contract passes deterministic research-validity tests, but no predictive improvement is demonstrable from the existing frozen inputs. This is a ready-to-test upstream research repair, not approval to change production selection or place bets.
