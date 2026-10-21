# Football v2 / SlipTrace — Coordinated Repair and Deep Audit

**Audit date:** 2026-10-21  
**Authority:** Football C only  
**Replay window:** 2026-10-19 00:00 ICT through 2026-10-21 03:00 ICT  
**Order applied:** repair → replay → diagnose  
**Predictive rule changes implemented:** none

## Executive decision

Infrastructure Gates A and B pass on the repaired code and regression fixtures. The corrected source surface recovers the 20 October UEFA Champions League block at 16:45 UTC and 19:00 UTC; the latter is 02:00 ICT on 21 October and remains inside a `[start, end)` window ending 03:00 ICT. FootballInfo is no longer a canonical kickoff source. LiveScore and SofaScore remain preferred canonical sources, FotMob is the explicit-UTC broad fallback, and ESPN is the mandatory independent priority-fixture validator.

The corrected replay does not create retroactive official predictions. Fenerbahçe–Slavia retains its frozen WATCH assessment. Sabah–Dortmund and the seven 19:00 UTC UCL fixtures are coverage-loss rows because no adequate frozen normal-sweep research contract exists for a deterministic prospective reconstruction.

The predictive sample therefore remains 37 ranked assessments: 19 FOCUS and 18 WATCH. FOCUS retained a small G3 separation but inverted at 4+: 57.9% versus 50.0% for 3+, and 26.3% versus 44.4% for 4+. Frozen O2.5 certificates reached in 8/11 cases; frozen O3.5 certificates reached in 2/8. The G4 sample identifies a weak branch pattern but does not distinguish its two successes from its failures, so no production G4 rule is changed in this pass.

## 1. Infrastructure root-cause matrix

| Defect | Reproduction | Code path | Root cause | Impact | Exact repair | Regression | Status |
|---|---|---|---|---|---|---|---|
| `SOURCE_TIMEZONE_NORMALIZATION_FAILURE` | FootballInfo stored Fenerbahçe–Slavia at 17:45 UTC and the late UCL block at 20:00 UTC | `stages_v4/tools/work_sweep.py` FootballInfo fixture-card parser and `acquire()` | A timezone-free displayed clock was interpreted as UTC | Fixtures shifted +1 hour | Removed FootballInfo from canonical kickoff fallback; added FotMob `status.utcTime` parser | `test_fotmob_explicit_utc_preserves_ucl_boundary` | PASS |
| `WINDOW_BOUNDARY_FIXTURE_LOSS` | 19:00 UTC became 20:00 UTC / 03:00 ICT, equal to the exclusive end | provider acquisition → `[start,end)` membership | Bad source instant altered membership | Seven late UCL fixtures disappeared before research | Explicit-UTC canonical fallback plus independent UTC conflict gate | `test_fotmob_ucl_regression_keeps_full_early_and_late_blocks` | PASS |
| Priority surface omission | Independent provider has a priority fixture missing from canonical surface | `verify_priority_surface()` and `source_completeness.py` | Previous manifest proved only provider-internal extraction | Missing blocks could still be called complete | ESPN all-soccer comparison blocks with `SWEEP_COMPLETENESS_BLOCKED`; new source receipts require independent verification | `test_priority_validator_blocks_missing_fixture_and_kickoff_conflict`; `test_new_source_requires_independent_priority_verification` | PASS |
| False global completion | Active target set completed while deferred source rows remained | `tools/normal_finalize.py`; `tools/work_sweep.py` | One status string conflated batch, queue, and surface completion | `/rank` could treat partial scope as globally complete | Added explicit batch/queue/surface/deferred/priority fields; renamed terminal states | `test_normal_finalize`; `test_work_sweep` | PASS |
| `SCREENING_THRESHOLD_CLIFF` | Viborg priority 49 versus review cutoff 50 | `discovery_goal_gate.py` | A one-point cutoff ignored an independently visible carrier route | Viable G3 candidate was permanently deferred | Added secondary-review-only lane: score ≥49, carrier ≥1.75, 3+ rate ≥0.50, 4+ rate ≥0.30, trap ≤0.25 | `test_viborg_shape_enters_targeted_secondary_review`; generic 49 control stays deferred | PASS |
| `XI_RANK_INHERITANCE_FAILURE` / `MANUAL_FALLBACK_OVERRIDE` | Ranked Al-Nassr–NEOM was rebuilt as WATCH | `engine/xi_runtime_backend.py` | Runtime accepted a free-standing `c_football` object without sealed rank authority | Frozen FOCUS/O2.5 authority could be discarded silently | XI request v2 requires `RANKED` sealed package or explicit `EXCEPTION`; ranked rows inherit frozen evidence and undeclared overrides fail | `test_ranked_fixture_without_sealed_receipt_fails_closed`; `test_ranked_fixture_cannot_silently_override_frozen_c_evidence` | PASS |
| Below-floor BOOK authorization | O2.75 @1.81 or @1.63 and O3 @1.85 returned BOOK | `engine/core.py::evaluate_c_quote`; adapter; XI portable | Target existence was treated as current price authorization | Output looked executable below policy floor | Added `BOOK_TARGET_AVAILABLE` and `current_price_clears_book_target`; below-floor quote returns PASS / NO ACTION while retaining target | adapter/core BOOK regressions | PASS |
| `ACTUAL_BET_PERSISTENCE_GAP` | Confirmed Tai Po physical bet absent; only two migrated rows present | `google_sheets/route.py` and `Actual Bets — Current` | Confirmed-slip writes from `/xi` were disallowed by routing even though XI is where confirmations occur | Physical P/L authority omitted confirmed exposure | Allow `/xi` write only with `confirmed_user_slip=True`; persisted and independently read back Tai Po row | `test_actual_bets_require_confirmed_slip`; live readback A4:P4 | PASS for confirmed Tai Po; other history unreconciled |

## 2. Source-provider decision

Production roles are:

1. **LiveScore** — first canonical date surface when healthy. Its requested timezone is explicitly converted to UTC before date-surface merging.
2. **SofaScore** — second canonical surface. Epoch timestamps are normalized to UTC.
3. **FotMob** — broad canonical fallback. Only `status.utcTime` is accepted; missing or naive time fails closed.
4. **ESPN all-soccer** — mandatory independent priority-fixture and UTC validator. A missing canonical fixture or a kickoff conflict blocks the sweep.
5. **FOX Sports UCL** — priority-competition diagnostic sentinel retained in the provider probe workflow. It is not allowed to override a UTC-explicit canonical row and is not the sole completeness proof.
6. **FootballInfo** — supplementary history/research only. It has no kickoff or window-membership authority.
7. **FoxScore** — experimental. HTTP 503 from the runner prevents production promotion.

Transport uses a 12-second request timeout, at most five bounded attempts, capped backoff, and immediate route failure for client/auth/rate-limit responses. Canonical failure advances to the next canonical provider. Internal surface reconciliation and independent priority conflicts fail closed. The time contract is an aware ISO-8601 instant normalized to UTC, with window membership evaluated as `[start, end)`.

## 3. Sweep integrity result

The mandatory regression surface is:

| Block | Fixtures | UTC | ICT | Replay classification |
|---|---|---:|---:|---|
| Early | Fenerbahçe–Slavia; Sabah–Dortmund | 16:45 | 23:45 | Fener retained frozen WATCH; Sabah coverage loss |
| Late | Roma–Slovan Bratislava; Porto–PSV; Liverpool–Villarreal; Manchester City–AEK; Napoli–Bodø/Glimt; PSG–Barcelona; Stuttgart–Atlético Madrid | 19:00 | 02:00 next day | Seven coverage-loss rows |

`19:00 UTC == 02:00 ICT on 21 Oct` is now a regression assertion. The seven late fixtures are inside the requested window and cannot move to the 03:00 exclusive boundary.

Viborg’s frozen discovery shape (49 priority, 1.75 carrier, 0.50 3+ rate, 0.35 4+ rate, 0.25 draw-trap rate) now enters `NEAR_CUTOFF_CARRIER_SECONDARY_REVIEW`. The global review cutoff remains 50.

Completion semantics now distinguish:

- `active_batch_complete`
- `active_research_queue_complete`
- `whole_requested_surface_complete`
- `unresolved_or_deferred_candidates_remain`
- `deferred_source_backlog_count`
- `priority_completeness_verified`

The bounded normal finalizer emits `ACTIVE_RESEARCH_QUEUE_COMPLETE`; the uncapped full runner emits `WHOLE_REQUESTED_SURFACE_COMPLETE` or `WHOLE_REQUESTED_SURFACE_COMPLETE_WITH_EVIDENCE_LIMITS`. It no longer labels active-cap completion as global `RESEARCH_COMPLETE`.

## 4. XI authority result

**Before, Al-Nassr–NEOM:** frozen rank was C-FOCUS, rank 3, FOLLOW, certified O2.5, strong self-funded carrier, G3 funded, G4 unfunded. A later normal-chat XI call accepted a manually reconstructed payload and returned WATCH / “G3 plausible.”

**After:** a ranked XI request must carry an exact `V4_RANK_PERSISTENCE_VERIFIED` or partial verified package, exact match ID, board row, and frozen model input. The runtime inherits the frozen row. Only fields named in `material_evidence_updates` may differ. Missing authority returns `RANK_RECEIPT_REQUIRED`; an undeclared FOCUS→WATCH override also returns `RANK_RECEIPT_REQUIRED`. Explicit exceptions use `authority.mode = EXCEPTION` and a non-empty exception reference.

## 5. BOOK semantics result

| Example | Target floor | Old apparent state | New state |
|---|---:|---|---|
| Presov O2.75 @1.81 | 1.85 | BOOK | PASS / NO ACTION; target remains visible |
| Bursaspor O2.75 @1.63 | 1.85 | BOOK | PASS / NO ACTION; target remains visible |
| Viborg O3.00 @1.85 | 1.90 | BOOK | PASS / NO ACTION; target remains visible |
| O2.75 @1.85 | 1.85 | BOOK target | BOOK target; current price clears floor |

The G3 extension thresholds are unchanged. BOOK remains a target order and never creates exposure by itself.

## 6. Accounting result

`Actual Bets — Current` contained only two migrated baseline rows. The confirmed Tai Po bet is now persisted as row 4 with immutable Bet ID `USER-20261020-TAIPO-SOUTHERN-O275`, match ID `1865810`, O2.75 @2.00, stake 333,333 VND, FT 4–2, WIN, profit +333,333 VND, ROI 100%, and `Confirmed User Slip = TRUE`. Placement and settlement timestamps remain blank because no exact timestamps were supplied.

No other historical physical bet was backfilled. Model assessment, screenshot quote, BOOK target, model exposure, physical user bet, and settled physical result remain separate states. The remaining reconciliation gap is the set of any other user-confirmed bets not supplied with verifiable execution evidence.

## 7. Corrected two-day audit

### Ranked sample

| Metric | Corrected result |
|---|---:|
| Total ranked assessments | 37 |
| FOCUS | 19 |
| WATCH | 18 |
| FOCUS 3+ reach | 11/19 = 57.9% |
| WATCH 3+ reach | 9/18 = 50.0% |
| FOCUS 4+ reach | 5/19 = 26.3% |
| WATCH 4+ reach | 8/18 = 44.4% |
| Frozen O2.5 certificate reach | 8/11 = 72.7% |
| Frozen O3.5 certificate reach | 2/8 = 25.0% |
| All FOCUS supported-burden reach | 10/19 = 52.6% |

No new official ranked prediction is added for the eight recovered UCL coverage-loss rows. Adding them to the denominator as retroactive predictions would fabricate prematch evidence.

### Exception controls

Eight named exception controls have outcome evidence: NEC–Fortuna, Viborg–Midtjylland, Deportivo Cali–Junior, Deportivo Pasto–Alianza, PSG U19–Barcelona U19, Stuttgart U19–Atlético U19, Liverpool U19–Villarreal U19, and Roma U19–Slovan U19. Seven were actionable FOCUS/ACT-style calls and one was PASS. Three of seven actionable burdens reached (NEC, Viborg, Stuttgart U19), while Roma U19 was a PASS that finished 5–0. This 3/7 result is a control sample, not an exhaustive count of every exception issued during the period; exception receipts are not centrally enumerable in one sealed cohort.

The exception controls are materially less stable than the normal frozen contract. They contain both high-confidence misses (Cali, Pasto, PSG U19, Liverpool U19) and a severe PASS false negative (Roma U19). That supports keeping exception authority explicit and outside normal rank inheritance.

### False positives and false negatives

- G4 false positives: RFS–Tukums (2–0), Al Hilal–Al Hazm (1–0), Al Taawon–Al-Qadisiyah (0–1), Luton–Barnsley (2–1).
- Valuable XI downgrades: Presov–Zilina B to O2.5 (1–1), Trabzonspor–Besiktas to O2.5 (2–0). Al Feiha–Al Ahli also downgraded to O2.5 and reached five goals; the downgrade remains prospectively justified by its reduced upper-tail evidence.
- WATCH 4+ controls: NEC–Fortuna 2–2, Lee Man–Kitchee 1–5, Spartak Subotica–Borac 3–3, Fenerbahçe–Slavia 2–2, Bromley–Leicester 0–4, Cambridge–Wycombe 2–2. Outcomes alone do not prove those rows should have been FOCUS.

### Ranking inversion diagnosis

The FOCUS/WATCH inversion at 4+ is best explained by a combination of **A: certificate generation**, **C: source/admission selection**, **D: XI changes**, and **E: sample composition**. There is no deterministic evidence that the ranking sort key itself misordered equal evidence. G3 still separates modestly in the intended direction. G4 certificate generation is the main predictive concern; source loss and the Viborg admission cliff affected which mechanisms entered the sample; XI downgrades correctly reduced three burdens; and the small two-day WATCH sample contains several high-tail outcomes.

## 8. G4 branch audit and conclusion

Rank-time G4-funded fixtures had these frozen branches:

| Fixture | FT goals | Completion | Completion quality | Continuation | Failure resistance | Stall | Carrier branch | Distributed branch | Reply branch | Upper-tail transfer | Comparable context |
|---|---:|---|---|---|---|---|---|---|---|---|---|
| Presov–Zilina B | 2 | MIXED | HIGH | HIGH | MEDIUM | MEDIUM | MIXED | SUPPORTED | SUPPORTED | MEDIUM | MIXED |
| Al Feiha–Al Ahli | 5 | CARRIER_LED | MEDIUM | MEDIUM | MEDIUM | MEDIUM | SUPPORTED | MIXED | MIXED | MEDIUM | MIXED |
| Trabzonspor–Besiktas | 2 | MIXED | MEDIUM | MEDIUM | MEDIUM | MEDIUM | SUPPORTED | MIXED | MIXED | MEDIUM | MIXED |
| RFS–Tukums | 2 | CARRIER_LED | MEDIUM | MEDIUM | MEDIUM | MEDIUM | SUPPORTED | MIXED | MIXED | MEDIUM | MIXED |
| Al Hilal–Al Hazm | 1 | CARRIER_LED | MEDIUM | MEDIUM | MEDIUM | MEDIUM | SUPPORTED | MIXED | MIXED | MEDIUM | MIXED |
| Omonia–Olympiakos | 4+ | CARRIER_LED | MEDIUM | MEDIUM | MEDIUM | MEDIUM | SUPPORTED | MIXED | MIXED | MEDIUM | MIXED |
| Luton–Barnsley | 3 | CARRIER_LED | MEDIUM | MEDIUM | MEDIUM | MEDIUM | SUPPORTED | MIXED | MIXED | MEDIUM | MIXED |
| Al Taawon–Al-Qadisiyah | 1 | CARRIER_LED | MEDIUM | MEDIUM | MEDIUM | MEDIUM | SUPPORTED | MIXED | MIXED | MEDIUM | MIXED |

Seven of eight were funded with failure resistance MEDIUM and stall risk MEDIUM. Six shared the exact fragile shape: carrier SUPPORTED, distributed MIXED, reply MIXED, completion/continuation/failure resistance/stall all MEDIUM. That group contained four documented failures and the two sample successes, Al Feiha and Omonia. Because the frozen categorical evidence cannot separate those successes from failures, the common root is not yet strong enough for a deterministic production threshold change.

**NO G4 CALIBRATION CHANGE REQUIRED**

A prospective challenger should test the following candidate without changing production: require either a second independent G4 branch to be SUPPORTED, or at least one of completion, continuation, or failure resistance to be HIGH when stall risk is MEDIUM. This would downgrade the six fragile carrier-only rows, including both successes, so it must prove better precision and acceptable coverage prospectively before adoption.

G3 funding thresholds, G4 funding thresholds, carrier weighting, ranking calibration, and all other predictive Football C logic remain unchanged.

## 9. Validation

- Stage/sweep suite: 161 tests passed.
- Active engine core: 85 tests passed.
- Active XI, screenshot, rank-authority, routing, and active-C tests: 62 tests passed.
- Focused BOOK adapter tests: 4 tests passed.
- Google Sheets readback verified the Tai Po row after write.
- `git diff --check` passed.

The repository also contains historical tests for retired C2/C3/C4 pair runtimes. Those tests fail against the already-active C-only retirement boundary and were not treated as production regressions.

## Final status

```text
SOURCE INTEGRITY: PASS
SWEEP INTEGRITY: PASS
RANK INTEGRITY: PASS — no ranking-key defect demonstrated
XI INHERITANCE: PASS
BOOK SEMANTICS: PASS
ACCOUNTING: PASS FOR CONFIRMED TAI PO; OTHER UNSUPPLIED BETS UNRECONCILED
G3 CALIBRATION: UNCHANGED
G4 CALIBRATION: NO G4 CALIBRATION CHANGE REQUIRED; PROSPECTIVE CHALLENGER RECOMMENDED
REMAINING DEFECTS: coverage-loss rows lack frozen prematch research; exception cohort lacks one sealed enumerable authority; FOX remains diagnostic rather than a production blocking validator
```
