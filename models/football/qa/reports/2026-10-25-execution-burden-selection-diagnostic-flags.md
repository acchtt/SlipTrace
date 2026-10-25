# Football C — execution/burden/selection diagnostic flags

**Date flagged:** 2026-10-25 ICT  
**Evidence surface:** V4-20261024-1800-20261025-0000-PRIORITYFIX  
**Authority:** Football C only  
**Selection authority:** ZERO  
**Backfill prohibited:** YES  
**Severity:** HIGH diagnostic

## Flag 1 — custom-line reachability / execution-path defect

Mainz 05 — Werder Bremen and RB Leipzig — Elversberg were assessed with `wait_reachable=false` because the desired target was not visible in the submitted screenshot. That assumption was operationally wrong for this user/bookmaker context: custom total line + odds orders are available and do not require the target to be visible in the screenshot.

Required audit label:

`CUSTOM_LINE_REACHABILITY_FALSE_NEGATIVE_20261024_SLATE`

Audit requirement: custom-line capability must be persistent execution context. Screenshot visibility governs observed odds only; it must not determine whether a football-authorized custom BOOK target is reachable.

## Flag 2 — certificate-to-execution burden gap

A large share of strong C selections in the 18:00-00:00 slate carried only a compiled O2.50 burden while the tradable prematch market was already commonly O3.25 or higher. Waiting for O2.50 or a low O2.75/O3.00 bridge can therefore leave the strongest fast-scoring trajectories non-executable until after the opportunity is gone.

This is not permission to let market lines create football authority. The audit must determine whether Football C needs a settlement-aware execution ceiling/band for O2.75 / O3.00 / O3.25 derived only from frozen football evidence, distinct from the minimum protected certificate.

Required audit label:

`CERTIFICATE_TO_EXECUTION_BURDEN_GAP_O325_20261024_SLATE`

## Flag 3 — G3 rejection versus G4 promotion asymmetry

Willem II — Cambuur was researcher-declared FOCUS with a strong frozen goal signal, but the deterministic compiler rejected every G3 mechanism and converted it to WATCH/STOP with no supported burden.

HamKam — Rosenborg, on the same frozen slate, was promoted to funded G4 / O3.50 despite several supporting dimensions remaining MEDIUM/MIXED. The comparison raises a prospective calibration question: whether G3 admission is too binary for high-signal two-USABLE-route cases while the carrier-led G4 branch is comparatively permissive.

Required audit label:

`G3_REJECTION_G4_PROMOTION_ASYMMETRY_20261024_SLATE`

## Guardrails

- Do not use eventual match outcomes to manufacture retrospective ACTs or change frozen evidence.
- Replays must use the exact pre-kickoff evidence epochs and then compare resulting board/execution states.
- Keep selection recall, certified burden, execution ceiling, market price, and realized exposure as separate audit layers.
- A repair is acceptable only if frozen replay controls improve without broadly promoting weak/high-risk matches.

## Required follow-up

Run one coordinated frozen replay evaluating:
1. persistent custom-line reachability;
2. a football-only intermediate execution burden policy including O3.25;
3. symmetric G3/G4 mechanism calibration using same-slate controls.

No production threshold change is authorized by this flag alone.


## Flag 4 — overlapping G3 extension policies / Chelsea BOOK path conflict

Chelsea — Tottenham (match 1793619) exposed two active Football C extension policies with different robustness standards.

The evaluated Chelsea state was:
- compiled certificate O2.50 / G3 funded;
- G4 rejected;
- certificate robustness CONDITIONAL;
- credible tail NEAR_FUNDED;
- STRONG self-funded carrier;
- chance quality HIGH;
- continuation MEDIUM;
- upper-tail control pressure MODERATE.

`c_intermediate_burden_profile()` accepts CONDITIONAL-or-better rows and authorized O2.75 plus O3.00 for this profile. `evaluate_c_quote()` evaluates that intermediate profile first, so visible O3.00 @1.80 became BOOK O3.00 @1.90+.

However, `c_g3_book_extension_profile()` separately states that FRAGILE and CONDITIONAL G3 rows may not extend above O2.50 and requires ROBUST football. Because the intermediate branch returns first, the stricter ROBUST-only branch never governs Chelsea.

Required audit label:

`OVERLAPPING_G3_EXTENSION_POLICY_CHELSEA_20261024`

Audit requirement: collapse these overlapping extension authorities into one settlement-aware policy with one explicit robustness standard. Preserve the distinction between O3.00 push-at-three and O3.25 half-loss-at-three, but do not allow branch ordering to decide which risk standard applies.

No retrospective settlement or exposure rewrite is authorized by this flag.


## Flag 5 — contextual football load is not first-class in Football C

The active MatchAssessment schema contains structured tournament-format/incentive fields, but it has no dedicated deterministic fields for:
- derby/rivalry state and rivalry-specific control/tempo risk;
- rest-days differential;
- schedule congestion;
- continental/intercontinental travel load and time-zone recovery;
- cumulative minutes / fatigue burden;
- recovery disadvantage after a short turnaround.

RANK.md requires tournament format/incentive where applicable, but does not require derby, rest, travel or congestion as first-class frozen fields. These factors may appear opportunistically in prose/team-news research, yet the deterministic compiler cannot distinguish "researched and neutral" from "never checked" and cannot apply them consistently to continuation, stall, failure resistance or burden ceilings.

Chelsea — Tottenham (1793619) is a control example. The frozen Football C record classified tournament incentive as NOT_APPLICABLE and contained no structured derby/rest-load modifier. Public pre-match information identified the fixture as a London derby and Tottenham's coach explicitly reported player fatigue after the Monday league match. These contextual facts were not represented as named deterministic inputs in the frozen assessment.

Required audit label:

`CONTEXTUAL_LOAD_DERBY_FATIGUE_GAP_20261024_SLATE`

Required repair investigation:
1. add a market-independent context layer frozen before pricing;
2. distinguish checked-neutral from unchecked;
3. represent rivalry/derby, rest differential, congestion, travel/recovery and cumulative fatigue;
4. map verified context conservatively into continuation, stall risk, failure resistance and upper-tail control;
5. do not assume a derby is automatically suppressive or expansive—direction must be evidence-backed;
6. do not double-count lineup absences that already capture the same fatigue mechanism;
7. replay on frozen same-information controls before production adoption.

No retrospective action rewrite is authorized by this flag.


## Flag 6 — Portland–Charlotte negative market-disagreement / draw-control suppression

**Fixture:** Portland Timbers — Charlotte FC (1696739)  
**Prematch exception epoch:** 2026-10-25 09:28 ICT  
**Frozen rank state:** WATCH / REVIEW_ONLY  
**Exception result:** WATCH / PASS, no G3 certificate  
**Observed early state for audit only:** 1-1 at 10'  
**Backfill prohibited:** YES

The prematch exception retained HIGH effective stall risk and rejected G3 even though the visible bookmaker ladder was centered materially higher than the comparable San Diego FC — Seattle Sounders fixture assessed immediately beforehand.

Common visible lines:
- Portland — Charlotte: O3.00 @1.57, O3.25 @1.78, O3.50 @2.01;
- San Diego — Seattle: O3.00 @1.61, O3.25 @1.83, O3.50 @2.05.

Thus the market assigned at least as much, and slightly more, upper-goal pressure to Portland — Charlotte. Football C nevertheless produced the reverse football ordering:
- San Diego — Seattle: FOCUS, G3 funded, O2.50 certificate, O2.75 bridge authorized;
- Portland — Charlotte: WATCH, G3 not funded, no certified burden, PASS.

This is not evidence that market pricing should create football authority. It is a disagreement-control failure candidate: when Football C has **no G3 certificate** while the observed market is centered around O3.00/O3.25 or higher, the current runtime can report `market_disagreement_recheck_required=false` because there is no certified burden to compare against. That prevents a forced football recheck in the exact negative-disagreement case where the model may be over-suppressing a plausible third-goal route.

A second candidate defect is incentive-state handling. Charlotte could clinch with a draw, and the exception encoded `DRAW_ACCEPTABLE` on the away side while Portland remained `WIN_PREFERRED`. That mixed state contributed to HIGH stall pressure. The post-kickoff 1-1 at 10' is to be retained only as diagnostic evidence that the suppressed alternative route existed; it must not be used to backfill an ACT or to rewrite the frozen evidence epoch.

Required audit labels:

`NEGATIVE_MARKET_DISAGREEMENT_NO_G3_PORTLAND_CHARLOTTE_20261025`

`DRAW_ACCEPTABLE_STATE_DEPENDENCE_PORTLAND_CHARLOTTE_20261025`

Post-slate audit requirements:
1. compare Portland — Charlotte against San Diego — Seattle using only their frozen prematch evidence epochs;
2. test a mandatory negative-disagreement recheck when `goal3_funded=false` and the visible market burden is materially above the model's no-certificate state;
3. ensure the market can trigger re-research but cannot create or raise a football certificate;
4. make `DRAW_ACCEPTABLE` state-dependent rather than an automatic prematch suppressor when the opponent is win-seeking and both teams retain scoring routes;
5. separate base stall risk from game-state-contingent control risk;
6. replay nearby same-slate WATCH/FOCUS controls to ensure the repair does not broadly inflate G3 admission;
7. retain the 1-1 at 10' and final score only as outcome diagnostics after the frozen replay is complete.

No production threshold change, retrospective ACT, BOOK fill, or accounting rewrite is authorized by this flag alone.


### Halftime checkpoint — Portland/Charlotte vs San Diego/Seattle

**Observed HT states (audit evidence only):**
- Portland Timbers — Charlotte FC: **2-1 HT**;
- San Diego FC — Seattle Sounders: **0-0 HT**.

These outcomes do not alter the frozen prematch decisions and must not be used for retrospective ACT/BOOK fills. They are retained because they sharpen the ordering diagnostic already flagged above:

- Portland — Charlotte received **WATCH / no G3 certificate / PASS** despite the market carrying slightly higher common-line over prices than San Diego — Seattle;
- San Diego — Seattle received **FOCUS / G3 funded / O2.50 certificate / O2.75 bridge / BOOK**;
- by halftime, the rejected Portland fixture had already cleared G3, while the stronger-certified San Diego fixture had not produced a goal.

Required post-slate analysis:
1. replay both frozen prematch epochs without result leakage;
2. compare route evidence, stall/control penalties, incentive modifiers and market-disagreement triggers side by side;
3. determine whether Portland's `HIGH` prematch stall/control assessment was over-weighted relative to San Diego's route evidence;
4. determine whether San Diego's certificate relied too heavily on route availability while under-weighting plausible 0-0 control failure;
5. use HT/FT states only after the frozen replay as calibration diagnostics, never as authority for changing historical exposure.

No threshold change is authorized from this halftime snapshot alone.


### Full-time checkpoint — Portland/Charlotte vs San Diego/Seattle

**Observed FT states (audit evidence only):**
- Portland Timbers — Charlotte FC: **3-2 FT**;
- San Diego FC — Seattle Sounders: **2-2 FT**.

This resolves the halftime diagnostic in an important way:

- **Portland — Charlotte** was frozen as **WATCH / no G3 certificate / PASS** and finished with **5 goals**. The previously flagged negative-market-disagreement / draw-control case is therefore now a **confirmed G3 false negative at the football-assessment layer**. This does not prove that every higher burden was actionable, but it does prove the model rejected the third-goal mechanism incorrectly for this fixture.
- **San Diego — Seattle** was frozen as **FOCUS / G3 funded / O2.50 certificate / O2.75 bridge** and finished with **4 goals**. The 0-0 HT / low first-half production was a variance/control stress event, not a final invalidation of the prematch G3 certificate.

Post-slate audit interpretation:
1. do **not** use the 0-0 San Diego halftime state as evidence that its prematch G3 certificate was wrong; the FT outcome supports the certificate at the target-goal level;
2. treat Portland as the stronger confirmed selection-inversion example because its no-G3 decision failed while a nearby same-slate G3-certified fixture ultimately cleared as expected;
3. compare frozen Portland and San Diego evidence side by side to identify why Portland's control/stall penalties overrode a viable third-goal route;
4. inspect whether `DRAW_ACCEPTABLE` and other control/context signals were given too much prematch veto power relative to independent route evidence;
5. keep the market comparison as a **recheck trigger diagnostic only**: Portland carried slightly higher common-line market goal expectation, but market pricing must not manufacture the certificate;
6. preserve all historical actions, BOOK states and accounting exactly as frozen. No retrospective ACT/BOOK fill is created by these outcomes.

Confirmed audit label:

`PORTLAND_CHARLOTTE_CONFIRMED_G3_FALSE_NEGATIVE_20261025`

San Diego remains a **certificate-hit / first-half-stress control**, not a confirmed assessment failure.


## Flag 7 — four-fixture G3 endpoint cluster: certified O2.50, all stop at two goals

**Observed FT outcomes (audit evidence only):**
- Kataller Toyama — Hokkaido Consadole Sapporo: **2 total goals**;
- Seongnam FC — Suwon Bluewings: **2 total goals**;
- Nagoya Grampus — Yokohama F. Marinos: **2 total goals**;
- Sanfrecce Hiroshima Regina — AC Nagano Parceiro: **2 total goals**.

All four fixtures were assessed pre-kickoff as **FOCUS / G3 funded / O2.50 certified / FRAGILE**, and all four failed at the exact same boundary: **goal three never arrived**.

This is materially different from a G4/upper-tail miss. The model did not merely overestimate four-plus continuation; it repeatedly certified the third-goal floor and then landed one goal short across four contemporaneous fixtures.

The cluster spans two authority types:
- Toyama — Sapporo, Seongnam — Suwon and Nagoya — Yokohama were normal ranked FOCUS rows whose confirmed XIs preserved the G3 certificate;
- Hiroshima Regina — Nagano was an exception recovery from a screened-out state and was upgraded to leakage-led G3/O2.50 after confirmed-XI and exact-matchup research.

Required audit label:

`FOUR_FIXTURE_G3_ENDPOINT_CLUSTER_20261025`

Primary audit questions:
1. test whether `carrier_self_fund=true` is too permissive when route reliability, completion, continuation and failure resistance are only MEDIUM and robustness is FRAGILE;
2. inspect whether Football C is treating **route existence** as equivalent to **third-goal completion protection**;
3. inspect whether `MEDIUM` stall/control penalties are too weak at the G3 admission boundary, especially when the opposite route is only USABLE or WEAK;
4. separate "can create/scoring route exists" from "third goal is protected across plausible low-endpoint game states";
5. test whether FRAGILE G3 should require stronger independent completion evidence before O2.50 is certified, rather than merely blocking O2.75/O3 extensions;
6. compare these four misses against same-slate G3 hits, including San Diego — Seattle, to identify which evidence dimensions actually discriminated successful third-goal completion;
7. keep Hiroshima separate as a screen-to-FOCUS exception so any repair does not simply reverse the earlier recall fixes and reintroduce selection-inversion misses;
8. replay the exact frozen pre-kickoff evidence epochs before changing any threshold. Outcomes are diagnostics only and must not be fed back as retrospective evidence.

Interpretation for the post-slate audit:
- this cluster is evidence of a possible **G3 floor-calibration problem**, not an execution/BOOK problem;
- the common failure point is the **third goal**, so the audit should prioritize certificate admission and endpoint-control logic ahead of market-line extension policy;
- do not rewrite historical actions or create retrospective exposure from these results.
