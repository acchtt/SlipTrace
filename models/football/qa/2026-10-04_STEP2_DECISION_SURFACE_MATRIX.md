# Step-2 Decision-Surface QA Matrix — 2026-10-04

**Stage audited:** Step 2 — XI + odds  
**Authority:** `CURRENT_MODEL.md` -> `02_NORMAL_CHAT_XI_ODDS.md` + Football C/C2/C3 specs + engine adapter/core + persistence contracts  
**Repair classification:** PROCESS COMPLIANCE FIX  
**Predictive-rule changes:** none

This matrix implements `FOOTBALL_DECISION_SURFACE_QA.md` for the active Step-2 surface.

| # | Input / surface | Collection / epoch | Interpretation / allowed effect | Missing-data behavior | Persistence / QA assertion | Status |
|---:|---|---|---|---|---|---|
| 1 | Canonical fixture identity | frozen Step 1 + current revalidation | selects the same fixture only | identity conflict blocks | frozen board + Decision State | FULLY TRACED |
| 2 | Fixture status | current prematch | only PREMATCH_CONFIRMED may use prematch Step 2 | STARTED -> live; other non-prematch states block | engine result; `test_non_prematch_fixture_blocks_step2` | FULLY TRACED |
| 3 | Official C board state | frozen Step 1 | official production state; cannot be rewritten by Step 2 | missing blocks payload | decision input/result | FULLY TRACED |
| 4 | Official FOLLOW/RESERVE/STOP lane | frozen Step 1 | controls Step-2 workload only | mismatch blocks | `official_follow_lane`; lane authorization tests | FULLY TRACED |
| 5 | Step-2 authorization | session start | ROUTINE_FOLLOW / RESERVE_ACTIVATED / USER_EXCEPTION only | mismatch blocks | triplet + session reconciliation | FULLY TRACED |
| 6 | XI state | current post-lineup | CONFIRMED/RELIABLE required for final prematch decision | UNAVAILABLE blocks | engine result | FULLY TRACED |
| 7 | Fresh post-XI football research | current post-XI | updates football evidence; market research cannot substitute | missing status/note blocks | status + non-empty note | FULLY TRACED |
| 8 | Market-history attempt | current prematch | context/conflict signal only; does not manufacture football quality | attempt must be declared; unavailable -> UNCLEAR | market-history fields | FULLY TRACED |
| 9 | Tournament incentive | current format/table epoch | can block or constrain burden/action | applicable LIMITED/UNKNOWN blocks | dedicated tournament fields | FULLY TRACED |
| 10 | H2H review status | current Step-2 recheck | declares usability only | missing recheck blocks | context/result | FULLY TRACED |
| 11 | H2H effect | current research | SUPPRESSIVE / OPEN / MIXED / NOT_MATERIAL / UNAVAILABLE | missing blocks payload | `h2h_effect` | FULLY TRACED |
| 12 | H2H transferability | current research | material H2H effect requires VERIFIED | non-VERIFIED cannot create material H2H effect | `validate_h2h_semantics` | FULLY TRACED |
| 13 | H2H current corroboration | current research | material H2H effect requires VERIFIED current corroboration | missing/non-verified cannot create material H2H effect | H2H semantic tests | FULLY TRACED |
| 14 | H2H material-effect declaration | current research | only suppressive + transferable + corroborated H2H may be material | invalid combination blocks | `h2h_material_effect` + basis | FULLY TRACED |
| 15 | H2H recency wording | research ordering | `recent` orders evidence review; it is not a numeric execution threshold | no invented cutoff | semantic-basis contract | EXPLICITLY NON-MATERIAL AS NUMERIC THRESHOLD |
| 16 | Main failure mode | common current evidence | describes strongest failure risk | missing/blank blocks | assessment/result trace | FULLY TRACED |
| 17 | Carrier self-fund | common evidence | existing carrier policy input | bare bool without basis invalid | value + `carrier_self_fund_basis` | FULLY TRACED |
| 18 | Independent upper-tail | common evidence | existing upper-tail policy input | bare bool without basis invalid | value + basis | FULLY TRACED |
| 19 | Failure attacks route | common evidence | existing veto/selection input | bare bool without basis invalid | value + basis | FULLY TRACED |
| 20 | Material suppression | common evidence | existing veto/selection input | bare bool without basis invalid | value + basis | FULLY TRACED |
| 21 | C completion/continuation/stall fields | current C policy epoch | C-only burden-completion validation | missing blocks model=c | C fields + C recheck | FULLY TRACED |
| 22 | C2 route-quality state | current C2 shadow epoch | C2-only floor/bridge policy | missing C2 recheck blocks C2 | C2 result + reasons | FULLY TRACED |
| 23 | C3 funding/control state | current C3 shadow epoch | C3-only funding/control policy | missing C3 recheck blocks C3 | C3 fields + basis | FULLY TRACED |
| 24 | Thesis state | current common evidence | PRESERVED / DEGRADED / BROKEN directly affects action | missing state/basis blocks | `thesis_state_basis` | FULLY TRACED |
| 25 | Primary mechanism intact | current evidence | false blocks BET under existing policy | bare bool without basis invalid | value + basis | FULLY TRACED |
| 26 | Current executable quote | user/current market epoch | line/odds used for price/burden comparison | missing quote blocks | exact line/odds | FULLY TRACED |
| 27 | Quote revalidation | immediately pre-engine | proves quote still exists at decision epoch | false blocks | `quote_revalidated` | FULLY TRACED |
| 28 | WAIT reachability | current execution planning | permits WAIT only when target is realistically reachable | bare bool without basis invalid | value + `wait_reachability_basis` | FULLY TRACED |
| 29 | WAIT negative-information dependence | current execution planning | WAIT cannot rely on expected thesis deterioration | bare bool without basis invalid | value + `wait_negative_info_basis` | FULLY TRACED |
| 30 | Material veto | current synthesis | existing hard veto input | bare bool without basis invalid | value + `material_veto_basis` | FULLY TRACED |
| 31 | Price floor | current quote | >=1.65 normal; 1.60-1.64 existing soft-zone conditions; lower normally WAIT/PASS | deterministic | core tests | FULLY TRACED |
| 32 | Supported burden | frozen/model-owned | current quote cannot manufacture higher burden | model-specific line required | separate C/C2/C3 line fields | FULLY TRACED |
| 33 | Engine execution | final Step-2 | C/C2/C3 all execute from same factual epoch | failed attempt recorded, no fake fallback | execution status + source revision | FULLY TRACED |
| 34 | Decision State persistence | post-decision | stores current epoch without rewriting frozen board | sync fault if write fails | Decision States | FULLY TRACED |
| 35 | Website Pick publication | C-BET only | only official C may create exposure | publication failure => no official exposure/P&L | Website Pick + duplicate guard | FULLY TRACED |
| 36 | Step-2 due-set completeness | session boundary | every due FOLLOW/activated RESERVE/exception gets one disposition | silent omission hard-fails | `step2_reconcile_cli.py` | FULLY TRACED |

## H2H conclusion

The previous QA gap was caused by H2H having a material effect without a machine-visible distinction between:
- merely suppressive history;
- transferable suppressive history;
- currently corroborated suppressive history;
- actual material use in the verdict.

The new contract makes those separate fields.

The word `recent` is explicitly **not** a hidden numerical threshold in Football C. Any proposal to introduce a fixed match-count/year cutoff is a model-rule change and must be tested as a challenger.

## Semantic-basis conclusion

The following verdict-changing semantic declarations now require same-epoch evidence bases:
- carrier self-funding;
- independent upper-tail;
- failure attacks route;
- material suppression;
- thesis state;
- primary mechanism integrity;
- WAIT reachability;
- WAIT negative-information dependence;
- material veto;
- H2H.

A basis has zero independent ranking/exposure weight. It exists to make the frozen declaration inspectable and reproducible.

## Stage-boundary checks

- Step-2 evidence may downgrade/currently reassess but cannot rewrite frozen Step-1 board history.
- Current price cannot manufacture supported burden.
- C2/C3 do not create Step-2 workload.
- Started fixtures route to live rather than receiving a backfilled prematch decision.
- Final results are forbidden from all fields above.

## Completion accounting

- Material inputs inventoried: **36**
- Fully traced: **35**
- Explicitly non-material as numeric threshold: **1** (`recent` H2H wording)
- Untraced material inputs: **0**
- Predictive threshold changes introduced by this QA repair: **0**

Final status is valid only if the deterministic tests and authority-enforcement checks pass on the merged implementation.
