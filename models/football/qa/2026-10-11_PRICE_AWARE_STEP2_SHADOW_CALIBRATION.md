# Football Step 2 — price-aware C/C2 goal-funding shadow calibration (2026-10-11)

**Status:** prospective diagnostic experiment, not a production selection threshold change. The existing C official and C2 shadow decisions and their publication/actual-bet accounting remain authoritative. No after-kickoff retro-bets.

## Why this experiment is necessary

The Oct-10 frozen board `B-20261010-2200-20261011-0600` contained five C-FOCUS/FOLLOW fixtures, all independently C2-FOCUS, yet **zero of five in either model** cleared the deterministic goal-funding predicate at its **own frozen supported Asian total**. C and C2 each have independently defined gates. At three user-reported early checkpoints Inter was 2-0, Leipzig 2-0 and Barcelona 1-0, but this says nothing decisive about full-match O3.25/3.5/4.5 pricing or return.

| Fixture | C support | C2 support | Researcher home+away central | Step1 bookmaker centre |
|---|---:|---:|---:|---:|
| Inter–Parma | O2.75 | O3.0 | 3.30 | 3.25 |
| Leipzig–Frankfurt | O3.0 | O3.25 | 3.40 | 3.75 |
| Barcelona–Getafe | O2.75 | O3.0 | 3.40 | 3.75 |
| Feyenoord–AZ | O3.0 | O3.25 | 3.70 | 3.50 |
| Fortuna–Twente | O2.75 | O3.0 | 3.10 | 3.50 |

A model-supported Asian burden is **not** a probabilistic mean, nor is the bookmaker centre proof of a profitable price. Inter's 3.30 vs market 3.25 is close but **not positive-EV evidence**. The true missing ingredient is an independently validated **goal-total probability distribution** anchored to teams, market alternatives and XI, not yet supplied by the researcher scenario.

## Bounded next experiment

`models/football/engine/step2_price_aware_shadow.py` accepts independent C/C2 factor snapshots from the same frozen evidence epoch, current verified match state and **actual pre-kickoff Asian Over offers** (price, quarter line, source, observed time). The 120-second quote window prevents stale odds masquerading as tradable quotes.

For each model independently:
- Evaluate the exact current production `clearing_goal_funded` or `c2_clearing_goal_funded` at the frozen supported line, and again at the actual quoted effective burden.
- Compare a **narrow experimental funding hypothesis** that admits a source-backed HIGH completion / MEDIUM continuation two-route case for C O2.25–2.75, and requires exceptional two-route or carrier persistence at O3.0+. For C2, independently test whether MEDIUM failure-resistance can still merit research when the C2 route-quality floor is CLEAR and independent routes and upper-tail evidence support continuation. These are **shadow hypotheses**, not automatic promotions.
- If the only quotes are above the supported line, say `MARKET_ABOVE_FROZEN_SUPPORT_RECHECK_NO_INFERRED_WAIT`; do not invent an alternative O2.75 quote or assume price decay. Above-support price never auto-increases the frozen line or moves to betting.
- When an observed price at/below support is fresh, >=1.65 and the old funding rule alone prevents it, label `SHADOW_PRICE_AWARE_ELIGIBILITY_ONLY`. This means **put the candidate in prospective value-validation research**, NOT `BET`, not `WAIT`, not positive EV. A current authorisation never comes from this sidecar.
- Compute exact conditional Asian-quarter settlement at two, three, four, five goals. The tool **does not** infer probabilities from home+away `central` goals; consequently its `expected_value` is null and it cannot declare +EV.
- Missing current quote is reported as unquoted. Missing genuine XI/primary mechanism makes a shadow research candidate noneligible. A score change or started fixture **must** follow the normal `/live` current-epoch workflow instead of this prematch-only script.

**Sampling plan**: collect immutable prospective paired C/C2 snapshots and full quotes before KO for enough matches to estimate quote-conditional value and missed opportunities; then track FT goals, actual settled quotes and early-goal onset separately. Keep all previously flagged cases in a retrospective *audit only* bucket. Do not treat after-goal scores as input for pre-goal classification. Stop shadow expansion if its out-of-sample false positives/edge worsens.

## Operational invocation

```bash
python models/football/engine/step2_price_aware_shadow.py \
  --input current_frozen_pair_and_real_quotes.json \
  --output step2_price_shadow.json
```

Use payload `schema_version=football-step2-price-calibration-shadow-v1`, `mode=PROSPECTIVE_PREMATCH_SHADOW`, `fixture` with frozen evidence epoch, confirmed pre-kickoff status, current verified time, `xi_status`, `thesis_state`, current mechanism and material-veto checks; `models.c` and `models.c2` with separately frozen `frozen_factors`, line, state, and model freeze timestamp; `quotes[]` with observed `market_phase=PREMATCH`, supported Asian line, decimal odds, live URL and quote timestamp (or empty if unquoted). A quantified forecast is optional but, if included, must be frozen before the pricing epoch and market-independent.

**Run after, never instead of, the real Step 2 C+C2 paired decision.** Do not add a blocking research pass while odds are expiring; the sidecar is deterministic/local and optional when its required frozen inputs are available. Include shadow diagnostic status in the report, clearly distinguished from production actions and Actual Bets. No additional permissions or revisions of prior frozen picks.

## Promotion requirements

The alternative cannot enter official C until separately tested on a sufficiently large **prospective**, source/quote-timed, XI-verified sample with real settlement and a calibrated price-to-probability comparison. C2 must be promoted via its own independently frozen trial. If no calibrated distribution is available, there is **no go** on altering thresholds, regardless of spectacular first ten minutes or a recent winning Over result.
