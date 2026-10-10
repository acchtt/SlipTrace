# Football Model QA — 2026-10-10: C/C2 FOLLOW supported-line dead end

**Audit scope:** SlipTrace main `fbeacb3a3a38ade14bb796cb028f3cbede3fca3d`; frozen board `B-20261010-2200-20261011-0600` produced under main `57be5e416198e7e88307bbfda44a16f1d42da16a`; Airtable `Daily Coverage Ledger` source `SWEEP-20261010-2200-20261011-0600`, separate `Decision States` and `Actual Bets — Current`. Report prepared after three user-reported early-score checkpoints. **Scores do not enter frozen inputs or eligibility judgments.**

## Summary: CRITICAL_SUPPORTED_LINE_FUNDING_CONTRADICTION

The frozen board contained seven complete C+C2 ranked fixtures: five official C-FOCUS/FOLLOW and two C-WATCH/STOP. One separate fixture remained on a tournament-incentive hold. All five FOCUS fixtures were independently C2-FOCUS.

At each **model's own frozen supported line**, the current exact deterministic goal funding logic yielded:

- C: **0/5** FOCUS/FOLLOW fixtures funded.
- C2: **0/5** FOCUS fixtures funded; Barcelona had C2 `selection_floor=BORDERLINE`, while the other four had CLEAR selection floor.
- All five official C snapshots had `carrier_self_fund=false` and `continuation_quality=MEDIUM`; supported C totals were O2.75 or O3.0. In `clearing_goal_funded()`, C's sole O3.0 funding route requires carrier self-funding; O2.75 funding requires either that or a two-sided HIGH-continuation route. None qualified.
- C2 requires its own independently frozen higher-tail criteria for O3.0+, including HIGH chance quality, route reliability and failure resistance. The five current C2 inputs had `failure_resistance=MEDIUM`; no C2 supported O3.0/O3.25 was funded.

The mathematically decisive issue is **not** that the five matches were certain to win a high bookmaker Over. It is that all five were advertised as FOCUS/FOLLOW with a supported line that their own unchanged Step2 gate could not presently accept at that line. A lower quote such as O2.0 could be funded in principle, but is not evidence of a real executable price; no such quote is inferred.

| Fixture | C line | C2 line | Advisory home+away goals | Published market centre at Step1 | C / C2 own-line funded |
|---|---:|---:|---:|---:|---|
| Fortuna Sittard–FC Twente | 2.75 | 3.0 | 0.95+2.15=3.10 | 3.50 | NO / NO |
| Inter Milan–Parma | 2.75 | 3.0 | 2.45+0.85=3.30 | 3.25 | NO / NO |
| Barcelona–Getafe | 2.75 | 3.0 | 3.00+0.40=3.40 | 3.75 | NO / NO |
| RB Leipzig–Frankfurt | 3.0 | 3.25 | 2.00+1.40=3.40 | 3.75 | NO / NO |
| Feyenoord–AZ | 3.0 | 3.25 | 2.65+1.05=3.70 | 3.50 | NO / NO |

**Crucial separate observation:** independent advisory goal expectations were **not** uniformly far below bookmaker centres. Inter's 3.30 forecast was slightly above the 3.25 bookmaker centre; Feyenoord's 3.70 was above 3.50. A frozen C support line is not a calibrated expectation. Source labels are prospective but those goal numbers remain *researcher estimates*, not a validated probability distribution or demonstrable EV.

## Timing / selection vs execution

- User observations entered as **checkpoint reports**, not FT settlements: Inter–Parma 2–0 around minute 19 (exact goal times unverified); Leipzig–Frankfurt 2–0 at 08:17; Barcelona–Getafe 1–0 at 04:22. These identify early home attacking conversion but not third/fourth/fifth-goal conversion.
- Step2 photo-epoch paired engine diagnostics were PASS for both C and C2 on Inter, Leipzig and Barcelona. Inter's 22:42 ICT quote was O3.25 @1.76 and paired verdict was unpublished; no current same-epoch executable quote/publication. Leipzig post-two-goal market O5.5 @1.92 would require **four more** for a full win. Barcelona post-goal O4.5 @2.02 likewise requires **four more** for a full win. Do not rewrite any missed prematch BET.
- The earlier 19:00–00:00 sweep missed Go Ahead–Sparta (original Step0 A/B rank #13), which finished 3–3. PRs #110 and #111 correct refill and research *scheduling* prospectively. They **cannot resolve this Step2 goal-funding contradiction**.
- Evidence burden remains separate: no complete confirmed executable multi-book price paths, authentic user placement, or paired prospective settlement for the three cases. Do not treat 3/4 early-goal checkpoints as return or hit-rate on an Asian line.

## Historical cross-check / why not simply remove funding gates

The separate Oct-10 historical C-factor ablation has 51 complete snapshots; 18 were O2.25, of which 17 additional funding blocks were introduced by the strict goal-three rule. Among those 17, FT goal counts were 8 >=3, 5 exactly 2, 4 <=1. These retrospective outcome labels do **not** establish that a valid pre-kickoff quote was present. C2 matched historical samples were not independently available.

## Production QA verdicts

| Subsystem | Verdict | Evidence |
|---|---|---|
| Fixture discovery and depth of rank | Repaired prospectively; real-world efficacy unverified | #110 refill, #111 whole-queue goal research priority |
| LANE | Operational only; repaired | #109 removed O3 ceiling and duplicate lane vetoes |
| C scoring identification | Encouraging route selection, **not** calibrated win probability | 5 paired FOCUS, 3 reported early-goal conversions |
| C supported-line funding alignment | **CRITICAL failure (0/5)** | Frozen factor logic at own supported line |
| C2 independent supported-line funding | **CRITICAL failure (0/5)** | C2 fourth-goal and selection-floor rules |
| Market-gap / healthy WAIT | Unresolved / needs prospective quote paths | frozen support vs market centre gaps +0.5 to +0.75; photos expire |
| XI early-live handoff | Unit-tested; no proven end-to-end action completion | #108 |
| Official user P/L | No new exposure from these three; unchanged reset ledger | Actual Bets — Current: two older user slips, total net -16,000 VND |

## Immediate repair specification (not automatic threshold relaxation)

1. On every newly frozen C+C2 board, run `follow_funding_readiness_qa.py` on the **original independent model-specific frozen factors** to disclose `own_supported_line_funded` separately from C-FOCUS/C2-FOCUS and FOLLOW. Flag any 0/N board to QA. It must never stop an assessment, downgrade FOCUS, create WAIT or generate an action.
2. **Repair calibration, not bypass safety:** compare frozen home/away football expected totals, route continuation and clearing-goal risk with the *actual price-dependent Asian quarter-line settlement*. Assess lower offered alternatives where genuinely quoted and reachable. Establish a prospective independent C threshold revision and a separate C2 shadow proposal; do not mechanically use bookmaker centre as prediction.
3. For each prospective quoted opportunity, freeze model-specific current gate vs less-restrictive gate *before kickoff*, with line, price, clock, XI and full factual revisions. Require early-goal and full-tail scoring tests separately (first/second goal vs goals 3–5). Distinguish 0–0 decay, post-first-goal repricing and no-bet.
4. **Only change C official execution requirements after matched quote-level out-of-sample testing**; C2 remains shadow-only. Do not infer profits from the 3 early scores, hypothetical lines or past final results.
5. Keep audit lightweight and deterministic. No extra remote research pass, no forced STOP, and no delays to actionable /xi work.

**QA decision: escalation required for Step2 policy/research calibration.** The new advisory readiness report is diagnostic only, not a source of official selections.
