# Football C — coordinated selection challenger V1 and replay (26 October 2026)

**Status: FAILED PREDICTIVE PROMOTION — CHALLENGER ONLY. DO NOT MERGE TO MAIN.**  
**Scope:** Football C only; /xi, screenshot-only prices, BOOK vs Actual Bets, women's scope, Africa exclusion and the coordinated 26-Oct G5 proof gate remain unchanged.  
**Base production:** `5e48b05cadf3f789d261c4065eb559ab79b37e80`.  
**Research horizon:** the nine sealed 23–26 Oct boards, 152 frozen assessment epochs and the separately verified 44 distinct /xi fixture receipts.

## One coordinated candidate

The code on `challenger/20261026-coordinated-goal-selection` implements an *isolated, no-authority* alternative research selection, never a change to the production portfolio.

1. `selection_quality_profile`: combine current scoring-route quality with **stacked moderate endpoint caution** (completion, continuation, failure resistance, reliability, chance), control/trap exposure, route independence, and the missing single-route reply.
2. `grade_provenance_dependency`: report overlap when HIGH reliability, chance, failure resistance, completion and continuation cite the **same source list**. Repeating one scoreline sample in many grade boxes must not count as several independent football mechanisms; reused citations alone are a warning, not a fabricated hard failure.
3. `_independent_g4_path_quality`: separately report whether a sourced current fourth-goal path is recorded. This reports *sources recorded*, not verified proof of a separate fourth goal, and does not rewrite the production G4 certificate.
4. `entry_readiness`: UTC-safe kickoff-minus-evidence time, `RESEARCH_LEAD_READY` (>=60 min), `AT_RISK` (15–<60), `CRITICAL` (<15), `CLOSED`, or `UNKNOWN`. **Never** infer real-time bookmaker availability from elapsed time.
5. `shadow_follow_allocation`: high-conviction, risk-adjusted global shortlist, max seven per board and three per exact kickoff; no forced fills. Keeps every historical G3/production rank and all live C actions unchanged.

The main /rank output still owns official `FOLLOW`, `RESERVE`, `FOCUS_UNFOLLOWED`, `CONTROL_REVIEW`, certificates and engine interpretation. The new `selection_challenger` output is explicitly non-executable.

## Exact nine-package structural replay

| Date / board | Frozen assessed | Production eligible after CONTROL_REVIEW | Shadow HIGH | Shadow FOLLOW | Production FOLLOW |
|---|---:|---:|---:|---:|---:|
| Oct 23 15:00–21:00 | 7 | 6 | 0 | 0 | 6 |
| Oct 23 21:00–03:00 | 20 | 10 | 0 | 0 | 6 |
| Oct 24 07:26–12:00 | 5 | 2 | 0 | 0 | 2 |
| Oct 24 10:46–12:00 | 7 | 4 | 0 | 0 | 3 |
| Oct 24 18:00–00:00 | 27 | 18 | 0 | 0 | 7 |
| Oct 25 00:00–07:30 | 18 | 9 | 0 | 0 | 7 |
| Oct 25 09:09–12:00 | 12 | 2 | 0 | 0 | 2 |
| Oct 25 main 15:00–03:00 | 54 | 42 | 10 | 7 | 7 |
| Oct 26 07:44–11:00 | 2 | 1 | 0 | 0 | 1 |
| **Total** | **152** | **94** | **10** | **7** | **41** |

Full disposition: 49 research epochs not on the old production board; nine CONTROL_REVIEW zero-authority; among 94 production eligible, ten HIGH, 65 CONDITIONAL and 19 REVIEW. Note these are rank-input *epochs*, not 152 different /xi actions. Deterministic mirror uses the same published scoring weights and frozen rank timestamps; it is **not** an independently executed native `run_board` against all nine sealed external packages, which remain local Library attachments.

In the 41 old FOLLOW epochs with rank time present, 32 had >=60 minutes prematch lead, seven had 15–<60, and two had <15; even the 32 are **not quote-verified bookability**. The 44 /xi historical receipts are a separately selected cohort, not a substitute for all 152 final scores.

### 25-Oct main slate actual score overlay

| Model cohort | FOLLOW | 3+ FT goals | Protected certificate clears |
|---|---:|---:|---:|
| Production repaired champion | 7 | 4/7 | **4/7 (57.1%)** |
| V1 strict challenger | 7 | 5/7 | **3/7 (42.9%)** |

Shadow cohort and original full-time scores: Barcelona–Real Madrid 1–2 (O3.5 loss); Freiburg–Bayern 1–3 (O3.5 clear); Basel–Grasshopper 0–0 (O2.5 loss); Sparta–Ajax 1–2 (O3.5 loss); AC Horsens–SønderjyskE 5–1 (O3.5 clear); Liverpool–Brighton 2–0 (O3.5 loss); Club Brugge–Sint-Truiden 3–2 (O3.5 clear). Sources: 25-Oct LiveScore historical date results (https://www.livescore.mobi/football/2026-10-25/), Barcelona official results (https://www.fcbarcelona.com/en/futbol/primer-equip/resultats), and original sealed replay. Production winners: Thun–Lugano, Inter–Fiorentina, Genk–Standard and Norrby–Norrköping.

**Do not claim an improvement by dividing three clears by only the seven surviving predictions.** The challenger drops all opportunities on eight boards and lowers the known exact-clear result even on its one active board. It has **not passed** any multi-day recall gate or entry-verified comparison.

### Selection evidence collapse (new actionable discovery)

The seven shadow candidates all had multiple predictive dimensions marked HIGH using **exactly the same evidence-reference set** for the three grade groups where references were embedded. Examples: Barcelona–Real Madrid, Freiburg–Bayern, Basel–Grasshopper, Sparta–Ajax, Horsens–SønderjyskE, Liverpool–Brighton and Brugge–Sint-Truiden. Their researcher explanations also recycle the same short seven-result scoring history to justify route reliability, third/fourth-goal completion, chance quality and continuation.

This **does not prove the original facts wrong**; a single official source can support multiple distinct observations. It does show that the current rank receipt **does not independently demonstrate** why those HIGH grades represent distinct scoring mechanisms. Recombining those same grades with a new weighted score will not solve selection inversion.

## CI / safety

- New unit tests verify stacked-MEDIUM demotion without deleting a real G3, G5/other certified line untouched, challenger NEVER edits champion FOLLOW, timezone-aware readiness and recycled-source diagnostic.
- GitHub active engine and C production invariant CI: **PASS** on challenger branch.
- **No main merge, no current-board rerank, no /xi policy change.**
- No hindsight alteration to `goal3_funded` or G4 compiler; the user's screenshot prices and verified bet accounting were never touched.

## Required next gate before production deployment

This V1 is rejected. The next useful upstream work is **prospective independent route fact collection**, not another ordinal coefficient adjustment. The V4 rank input needs named, source-attested, separable facts for (a) how the third goal completes after expected defensive adjustment, (b) opponent's independent reply versus a one-sided 2–0 stop, (c) whether post-third fourth-goal completion truly remains likely despite 3–0/2–1 control, and (d) a source-separated risk counterargument. At least one new slate should record these *before* final outcomes are known.

Only then compare both the same-information frozen 152 inputs and a new holdout with certified burden, false positive/negative, entry timing, first-goal timing where sourced and priced entry accessibility. Retain the model as **shadow** unless it improves independent multi-day performance without suppressing legitimate goal-route recall. Do not label historical high grades as new evidence or backfill proof after FT.

**Decision: FAIL / NO PROMOTION.**
