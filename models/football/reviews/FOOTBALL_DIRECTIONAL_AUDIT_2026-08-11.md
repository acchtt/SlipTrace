# Football Directional Audit — 2026-08-11

## Trigger

Recent verified football performance is materially below an acceptable calibration threshold. The current verified sample discussed in project state is 2 wins and 7 losses across nine recent actual/shadow selections, with a 0-5 subset across the most recent directional handicap examples reviewed (Necaxa +0.5, San Diego +1.5, Port Vale +1, Deportivo Cuenca -0.5, Tainan City -0.25).

This audit is an operational safety response, not a claim that fading the model is profitable. The sample is too small to establish an inverse strategy, but large enough to suspend confidence in the current directional decision boundary.

## Immediate operating mode

Effective immediately:

- No official football betting may resume.
- Shadow calibration only.
- Directional Asian handicaps and DNB/ML side bets are under quarantine until the audit exit criteria are satisfied.
- Totals are not automatically trusted; they must still pass the full validator and audit framework.
- No new match-specific patch may restore official execution by itself.

## Audit objective

Determine whether the model has measurable edge in any of the following:

1. directional side selection;
2. goal-environment/event-generation identification;
3. market-expression choice;
4. timing/entry selection;
5. favorite/underdog classification;
6. prematch versus live decisions.

## Historical benchmark arm

The audit now includes a parallel early-totals benchmark reconstructed from the v0.2.6-v0.2.9 era.

Protocol: `models/football/reviews/FOOTBALL_V026_V029_BENCHMARK_PROTOCOL_2026-08-11.md`.

This benchmark is motivated by the strongest explicitly version-tagged positive ledger results currently identified: v0.2.6 Alajuelense-Xelaju Under 1.75 and v0.2.9 O'Higgins-Boca Under 1.25. It does not assume those versions were broadly profitable; v0.2.7 was negative in its identified sample.

The benchmark tests a narrower hypothesis: the model may have had more useful signal in live goal-environment detection plus Asian-total boundary protection than in directional side selection.

For synchronized live decision points, run in parallel:

- Arm A: current v0.2.42 audit model;
- Arm B: early-totals benchmark, totals only.

Neither arm is executable. Compare selection frequency, settlement-adjusted P/L, ROI, process validity, line protection and NO BET frequency.

## Reconstruction protocol

For each recent verified bet or counted shadow selection, reconstruct the decision using only information available at the original decision timestamp.

Capture:

- exact score and minute;
- exact line and odds;
- market settlement scope;
- pre-match favorite/underdog status;
- live directional state;
- relevant reliable primary evidence;
- xG/xGOT role, including provider-quality issues;
- opponent threat classification;
- best eligible total at the same timestamp;
- opposite/protected-side market where available;
- no-bet alternative;
- final settlement.

Do not use final-score knowledge to rewrite the decision-state evidence.

## Counterfactual policy comparison

At each reconstructed decision point, compare at least:

- actual model selection;
- NO BET;
- opposite directional side at the closest comparable settlement line where actually available;
- best eligible total expression available at that timestamp;
- market-favorite continuation where applicable;
- protected favorite/underdog expression where applicable.

A counterfactual is valid only if the exact market/price was available or can be verified from the synchronized snapshot. Do not invent unavailable prices.

## Error taxonomy

Classify each reviewed loss as one or more of:

- directional inference error;
- favorite anchoring;
- underdog protection bias;
- relative-improvement bias;
- market-expression error;
- price/timing error;
- regime-persistence error;
- competition-utility error;
- evidence-quality/provider error;
- settlement misunderstanding;
- variance / process-valid loss.

## Directional quarantine rule

Until exit criteria are met, a directional side may be tracked analytically but cannot be promoted beyond shadow research status.

For each potential side, require the model to answer:

1. What primary evidence says this team is more likely than the opponent to generate the decisive scoring events from now?
2. What independent evidence suppresses the opponent's win/scoring branch?
3. Is the evidence absolute, or merely improvement relative to an earlier poor period?
4. Does the candidate remain preferable to the best eligible total?
5. Does the candidate remain preferable to NO BET after accounting for clock decay and price?

Failure on any question prevents directional promotion.

## Exit criteria

Official football betting remains paused until all are true:

- at least 20 newly assessed shadow decisions after this audit start;
- at least 10 of those are directional-eligible decision points, even if the final output is NO BET;
- no retrospective rewriting of the decision timestamp;
- directional shadow ROI is non-negative over the audit sample OR the model demonstrates a clearly superior non-directional market family with adequate sample;
- no single market family has a loss pattern attributable to the same unresolved structural error;
- a formal review documents which rules are retained, removed, or simplified;
- explicit user approval is obtained before any official football execution resumes.

The early-totals benchmark has its own minimum sample and cannot by itself shorten these audit requirements.

## Model simplification principle

Do not respond to every loss by adding a new narrow rule. Prefer removal, consolidation, or stronger generic gates when multiple losses share the same failure mode.

The audit should test whether the model is overfit and over-complex rather than assuming more rules will improve performance.

## Current conclusion

The recent sample is insufficient to justify an inverse-betting strategy, but it is sufficient to suspend confidence in directional football selections. The model is now in shadow-only audit mode with a parallel early-totals benchmark until the exit criteria above are met.
