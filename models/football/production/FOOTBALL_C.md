# Football C — Production Model Semantics

**Status:** ACTIVE OFFICIAL MODEL  
**Model:** Football C only  
**Purpose:** predictive/decision semantics only

Operational routing is owned by `models/football/CURRENT_MODEL.md`. Source and
rank procedure are owned by `stages_v4/SWEEP.md` and `stages_v4/RANK.md`.
XI execution is owned by `engine/core.py`, `engine/adapter.py` and
`engine/xi_portable.py`. This file must not redefine workflow caps, storage,
retired-model behavior or a second ACT/BOOK/PASS policy.

## 1. Football-first assessment

Football C assesses the current matchup before price.

Research the current scoring mechanism, route reliability, chance quality,
carrier capacity, burden completion, continuation, opponent leakage, stall
risk, failure resistance, availability, relevant H2H and tournament incentive.
Odds never create a scoring route or goal certificate.

Availability is symmetric. An absence may reduce a route only after checking
replacement creators/finishers, opponent independent scoring routes and
defensive-rotation leakage.

H2H is context only. It never creates a route. Suppressive H2H is material only
when it is transferable to the current matchup and independently corroborated by
current football evidence.

Tournament/qualifier incentive must be resolved whenever qualification,
aggregate state, draw resolution, margin/tiebreaks or simultaneous results can
change continuation. LIMITED/UNKNOWN incentive is incompleteness, not a
football-quality PASS.

## 2. Football C state

The researched football state is exactly one of:

- `C-FOCUS`
- `C-WATCH`
- `C-PASS`

FOCUS/WATCH/PASS is predictive football selection. FOLLOW/RESERVE/STOP is a
separate operational workload lane and must not become a second prediction
model.

Machine/frozen receipts retain `C-WATCH` for compatibility. User-facing
surfaces render it as **REVIEW_ONLY**. REVIEW_ONLY is rank/research metadata,
not an execution instruction and never a final /xi verdict.

There is no predictive board-size target and no fixed V4 rank-board cap.
Unfinished research remains unresolved/checkpointed rather than being converted
into PASS merely to finish a board.

## 3. Deterministic supported-burden compiler

Supported burden is compiled from explicit goal certificates:

- G3 -> O2.50
- G4 -> O3.50
- G5 -> O4.50
- G6 -> O5.50
- no G3 -> no certified burden

Asian .75 lines require the next certificate for a **full-win certificate**.

The certificate is a protected football burden, not a universal execution
ceiling. For G3-only C-FOCUS rows, the deterministic execution layer may issue
a non-exposure `BOOK` order at O2.75/O3.00/O3.25 when the current football
quality clears the settlement-aware extension contract:

- O2.75: exactly 3 goals = half win; pilot minimum price 1.85;
- O3.00: exactly 3 goals = push; pilot minimum price 1.90;
- O3.25: exactly 3 goals = half loss; pilot minimum price 2.00 and a stronger
  G3 structure is required;
- O3.50: still requires funded G4.

BOOK never upgrades G3 to G4 and never creates exposure until a fill is
independently confirmed. The researcher-declared line/basis remains audit
metadata only. The deterministic compiler owns production burden.

## 4. G3 mechanisms

G3 may be funded only through the existing deterministic Football C mechanisms,
including carrier, independent two-route/distributed completion, and permitted
matchup-leakage structures.

A plausible 1-1 is not sufficient by itself. The assessment must identify the
goal that clears the burden and the mechanism that supplies it.

## 5. G4+ transferability and comparable context

Whenever an independent upper tail is asserted, freeze:

- `upper_tail_transferability = LOW / MEDIUM / HIGH`;
- a non-empty transferability basis;
- `upper_tail_comparable_context_signal = SUPPORTIVE / MIXED / SUPPRESSIVE / UNAVAILABLE`;
- a non-empty comparable-context basis.

Evidence priority is prospective:

1. same competition / continental context;
2. closely comparable senior opponent/competition strength;
3. less-comparable domestic/cup history as corroboration.

SUPPRESSIVE forces effective transferability LOW. MIXED caps effective
transferability at MEDIUM. Raw scoreline frequency cannot override a closer
contradictory context.

G4 completion still requires the deterministic carrier/distributed/reply,
continuation and failure-resistance rules in the engine. This evidence contract
does not lower a certificate threshold.

## 6. G4 research completeness

Whenever G3 is funded, the G4 investigation must carry one explicit state:

- `G4_RESEARCH_INCOMPLETE`
- `G4_RESEARCH_EVIDENCE_LIMITED`
- `G4_RESEARCH_COMPLETE_MIXED`
- `G4_RESEARCH_COMPLETE_REJECTED`
- `G4_RESEARCH_COMPLETE_FUNDED`

Use `G4_NOT_APPLICABLE` only when G3 is not funded.

A complete investigation checks the plausible carrier four-goal path,
distributed 3+1/2+2 path, reply-assisted path, continuation after goal three,
transferability/comparable context and shared failure/stall mechanisms.

An unavailable source/path is not automatically negative evidence. Follow
`procedures/FOOTBALL_C_G4_EVIDENCE_CONTRACT.md`.

A G3-funded C-FOCUS row with G4 research still INCOMPLETE or EVIDENCE_LIMITED
is unfinished rank research and must not finalize onto the official board.
The V4 rank stage checkpoints it for bounded completion.

## 7. Ranking

Price-blind Football C ranking order is:

1. certificate robustness;
2. highest funded certificate: G6 > G5 > G4 > G3 > none;
3. endpoint/control risk;
4. frozen V4 quantitative goal signal;
5. remaining current football-mechanism quality.

Compiled burden magnitude is not an independent bonus. A fragile deeper
certificate does not automatically outrank a robust/conditional shallower one.

Within the same robustness/depth class, current completion and continuation
must not be displaced by raw historical goal rates.

## 8. XI / current football confirmation

XI repeats the football decision at the current evidence epoch without requiring
odds. Confirm whether availability actually changes named routes, whether the
primary mechanism remains intact, and whether tournament/H2H/current-context
information changes the certificate.

A ranked fixture carries its frozen board certificate and G4 research state.
A higher current certificate requires one permitted non-market path:

- verified new football evidence;
- verified completion of previously unfinished certificate research;
- verified source-backed correction of a prior certificate
  misclassification.

The market may trigger the recheck but never manufactures G3/G4/G5/G6.

## 9. Observed quote policy

User screenshots are `USER_SCREENSHOT_ONLY` observations:

- use the exact supplied line/odds;
- do not fetch a replacement quote;
- do not infer a missing price;
- do not re-time the screenshot.

Observed-price ACT/BOOK/PASS is non-executable comparison. A strict
current executable decision requires the separate runtime authorization/evidence
contract. BOOK is a target-order authorization, not a direct bet and not an
assumed future fill.

Normal acceptable price is >=1.65. The 1.60–1.64 supported-line soft zone is
available only where the deterministic C core authorizes it from already-funded
football evidence.

## 10. Material market disagreement

If the observed burden is materially above C's frozen/current certificate,
complete the required football recheck first.

If the recheck funds the market burden, evaluate it normally. If the recheck
does not fund it, the market remains unsupported as a **certificate**.

A bounded G3 BOOK extension is different: it does not accept the observed
higher burden and does not create G4. Material 0.50+ disagreement still
completes the existing football recheck first. After that recheck, C may publish
its lower settlement-aware target (maximum O3.00) even when G4 remains
unfunded/rejected; the recheck does not have to manufacture a certificate
upgrade. ACT at the materially higher observed burden still requires that
burden to be funded.

Do not use a higher market total as proof that the missing certificate should
exist.

## 11. Conditional BOOK — reachable before the first goal

Active Football C does not issue a user-facing WAIT. The legacy
`wait_reachable`, reachability-basis and negative-information fields remain
internal compatibility evidence for deciding whether a conditional target is
realistically reachable.

When the current quote is not acceptable but a valid target can be expressed,
C returns **BOOK** with the exact line and minimum odds. BOOK is a conditional
target order, not a bet and not exposure until an actual fill is independently
confirmed.

A conditional BOOK target requires:

- a prospectively reachable pre-goal target with a contemporaneous basis;
- no dependency on negative football information;
- an intact football mechanism;
- no material veto;
- an internal C-WATCH/REVIEW_ONLY exception, if explicitly assessed, to
  revalidate to ROBUST robustness. FRAGILE/CONDITIONAL may never create BOOK.

For an **unsupported higher observed line**, the target may move down to the
certified burden only when the gap is at most **0.25 goals**.

A gap of **0.50 goals or more** must not manufacture a speculative far-lower
target. After the football comparison it may:

- become funded and be evaluated at the observed burden;
- produce a bounded G3 settlement-aware BOOK target when that separate
  extension contract clears; or
- PASS.

A lone screenshot is not directional evidence that a target will become
available. If a BOOK target is not currently met, it remains
`PENDING_UNFILLED` and creates no exposure.

## 12. Live boundary

After kickoff, continue the Football C football assessment from actual
score/minute/material events. Never recreate a prematch ACT/BOOK/PASS
retrospectively.

A live quote is comparison evidence only unless a separate live execution
policy explicitly authorizes exposure.

## 13. Accounting

Current accounting is exposure-conservative:

- internal WATCH/REVIEW_ONLY -> no model bet;
- active C does not issue a user-facing WAIT; historical WAIT records remain
  immutable audit/accounting history;
- direct strict C BET/ACT -> official model exposure at actual terms;
- BOOK -> no model exposure at order creation; a later actual fill must be
  independently confirmed before reconciliation can treat it as exposure;
- physical user P/L -> `Actual Bets — Current` only.

`WAIT_ASSUMED`, `WATCH_ASSUMED` and retired-model synthetic exposure remain
historical-read-only concepts. See
`procedures/FOOTBALL_WAIT_ASSUMED_EXPOSURE.md` and
`procedures/FOOTBALL_MODEL_BET_ACCOUNTING.md`.

## 14. Audit invariant

Audit compares frozen prospective evidence with outcomes. It may identify a
selection, certificate, ranking, WAIT/execution or workflow defect, but it must
not rewrite the earlier assessment from result knowledge.

Retired C2/C3/C4 artifacts may be read only for historical audit. They have no
new production path.
