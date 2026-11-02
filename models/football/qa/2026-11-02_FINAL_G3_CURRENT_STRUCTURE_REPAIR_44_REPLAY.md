# 2026-11-02 Final G3 Current-Structure Repair — 44-Match Replay

## Production result

Production merge: `65cc9d31747904910cc428d1e2ca5df8096b4031`
PR: #205

Production change surface is limited to:
- `models/football/engine/core.py`
- `models/football/engine/adapter.py`
- `models/football/stages_v4/stage.py`
- `models/football/engine/tests/test_active_c_runtime.py`

The frozen 44-match audit harness, settled outcomes and replay workflow were not merged to production.

## Repair

The repair adds an explicit source-backed current-structure G3 path.

A candidate can use that path only after bounded research freezes:
- one STRONG current scoring route;
- a separate USABLE-or-better reply route;
- a surviving USABLE-or-better carrier;
- every existing G3 control axis at least MEDIUM;
- no material suppression or route-destroying failure;
- at least two distinct frozen source references.

This does not change predictive grades and does not grant G4. Newly funded historical WATCH rows reopen G4 research and must complete that pass separately.

Verified current-structure G3 receives a distinct ranking/workload class because the research layer has independently restored information that the historical Step-0 rate gate compressed away.

For this verified class only, a 0.25 low-draw-trap rate is no longer an automatic hard endpoint veto. A 0.30 trap remains hard. All other endpoint-control rules are unchanged.

## Same-information 44 replay

Outcomes were not read until after the final board was compiled.

### Before this repair

- FOCUS: 29; 3+ = 17/29 = 58.6%
- WATCH: 15; 3+ = 13/15 = 86.7%
- FOLLOW: 8; 3+ = 5/8 = 62.5%; 4+ = 4/8 = 50.0%
- STOP: 15; 3+ = 13/15 = 86.7%

### After final repair

- FOCUS: 35; 3+ = 23/35 = 65.7%; 4+ = 16/35 = 45.7%
- WATCH: 9; 3+ = 7/9 = 77.8%; 4+ = 4/9 = 44.4%
- FOLLOW: 8; 3+ = 7/8 = 87.5%; 4+ = 5/8 = 62.5%; mean goals 3.875
- RESERVE: 4; 3+ = 2/4 = 50.0%; 4+ = 2/4 = 50.0%
- FOCUS_UNFOLLOWED: 23; 3+ = 14/23 = 60.9%; 4+ = 9/23 = 39.1%
- STOP: 9; 3+ = 7/9 = 77.8%; 4+ = 4/9 = 44.4%

### Final FOLLOW 8

1. Persib Bandung–Isenmulang Kalteng — FT 4-0
2. Portland Timbers–Houston Dynamo — FT 2-1
3. Colorado Rapids–Chicago Fire — FT 2-4
4. Monterrey–Tijuana — FT 3-3
5. Alacranes de Durango–Atlético Morelia — FT 3-1
6. Cheongju FC–Paju Citizens — FT 1-2
7. Bayern Munich–Borussia Dortmund — FT 2-2
8. SC Heerenveen–NEC Nijmegen — FT 1-0

3+ result: **7/8**
4+ result: **5/8**

The only 3+ miss is Heerenveen–NEC.

All six historical borderline false negatives are now FOCUS and ranks 1–6. They remain FRAGILE for execution; ranking priority does not manufacture stronger XI/price authority.

## Validation

Final repair branch:
- Football active deterministic engine tests — PASS
- Football C production invariants — PASS
- Football V4 sweep/rank stages — PASS
- Football V4 original-source replay attestation — PASS

The production merge was made only after those branch checks succeeded.

## Interpretation

This is a major improvement on the frozen 44 cohort, especially the scarce FOLLOW selection: 62.5% -> 87.5% at 3+.

However, the same 44 fixtures were used to diagnose and repair the failure. This is therefore not an out-of-sample accuracy claim. Fresh prospective blocks are the required next validation for whether the repaired boundary generalizes.
