# LoL Draft-Only Execution Mode — 2026-08-31

**Status:** ACTIVE ONLY WHEN EXPLICITLY INCLUDED BY THE CURRENT SESSION LOCK  
**Model version:** unchanged — LoL v1.3  
**Authorization:** user instruction on 2026-08-31: no live predictions for now; enable Moneyline, Kill Handicap, Duration, and Total Kills after final draft + exact odds/line.

This is a temporary execution overlay. It supersedes conflicting live-only/retired-market execution clauses only while the active Session Authority Lock includes it. It does not rewrite historical positions or results.

## 1. Timing mode

`MODE = POSTDRAFT_ONLY`

- New predictions are made only after the final draft/roles are resolved and exact market lines/odds are available.
- Once the map has started, do not create or update predictions from kills, gold, objectives, structures, role gold, or other live state.
- In-map screenshots may be used for settlement/context only, not for new betting analysis.
- Same-series prior map results never change the frozen team benchmark.

## 2. Active market families

During this mode the enabled postdraft families are:

1. Moneyline;
2. Kill Handicap;
3. Duration Over/Under;
4. Total Kills Over/Under.

Each family is evaluated independently. Price cannot create a thesis. Exact line confirmation is still required before an accepted shadow Position.

Actual exposure remains `0u`; default shadow stake remains `0.25u` unless the lock states otherwise.

## 3. Draft analysis prerequisite

Resolve exact roles and run the Draft Interaction Matrix before market pricing:

`models/lol/procedures/LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`

At minimum resolve each side's primary/secondary kill mechanisms, threat-answer matching, objective setup geometry, damage access/uptime, side-lane independence, collapse asymmetry, execution burden, and adversarial second pass.

The draft/mechanism record must be locked before sportsbook odds are analytical evidence.

## 4. Moneyline — draft-only v1.3

Keep the frozen Gol.gg benchmark `K/P0`.

With no live-state variables in this mode:

`R=X=O=T=0`

`D_eff=D`

`C_draft = 1.5*D`

`P(A)=clamp(P0(A)+4.5*D pp,15%,85%)`

The selected side must still have a positive non-price draft thesis. Therefore:

- selected-side `D=+1` and a coherent reachable win mechanism are required for a TAKE candidate;
- `D=0` or `D=-1` from the selected-side perspective => PASS even if the price looks generous;
- team strength alone cannot create a bet.

Price pass:

`BOOK=1/decimal_odds`

`EDGE=P_model-BOOK`

Required ML edge remains `+5.0pp` unless the lock changes it.

### User-specified ML minimum odds

`MIN_ML_ODDS = 1.50`.

This is the corrected value supplied by the user immediately after the initial draft-only mode activation. It supersedes the mistakenly recorded `0.5` value. Do not reinterpret it as probability; it is a decimal-odds floor.

## 5. Kill Handicap — postdraft distribution mode

Kill Handicap is re-enabled after draft + exact line/odds.

Before seeing the handicap line/price, build a side-neutral final kill-margin distribution from:

- frozen team benchmark;
- completed Draft Interaction Matrix;
- primary/secondary kill mechanisms;
- target-access reliability;
- collapse asymmetry / cascade risk;
- underdog resilience / return-kill floor;
- execution burden and failure cost;
- expected compulsory-fight inventory implied by the compositions.

Use explicit signed final-margin bins whose probabilities sum to 100%. The distribution must be consistent with the draft-only ML win probability; do not select the handicap sign first and backfit the distribution.

After the distribution is locked, price both executable sides when available.

Retain these legacy safety controls where applicable:

- for favorite negative handicap `-5.5` or wider, compute `CoverShare = break-even cover probability / favorite ML win probability`;
- `CoverShare >0.70` => PASS / negative-handicap conversion veto;
- `0.60-0.70` requires at least three independent draft margin mechanisms and no strong opponent resilience cluster;
- underdog positive handicap requires at least two independent resilience/return-kill mechanisms and must survive the favorite clean-cascade stress branch;
- a theoretical multi-champion combo counts as one mechanism unless components function independently;
- better price never repairs a failed margin/resilience thesis.

Minimum KH odds remain `1.60`. Initial reactivation edge requirement is `+7.5pp` versus raw break-even probability.

## 6. Duration — postdraft-only core

Duration is re-enabled immediately after final draft + exact line/odds.

Use the v1.1 duration engine at `t=0` with draft-only scoring:

`R0=31.0`

Score `V/Q/H/T=-2..+2` only from composition mechanisms and map-conversion geometry; no live evidence exists in this mode.

`ER=max(2.0,31.0-1.5*V+1.0*Q+1.0*H+0.75*T)`

`F=ER`

Lock `F` before reading the offered duration line/price as analytical evidence.

For line `L`:

`P(OVER)=clamp(50%+7*(F-L) pp,15%,85%)`

`P(UNDER)=100%-P(OVER)`.

A postdraft Duration candidate requires:

- a coherent draft-based clock mechanism in the selected direction;
- odds >=1.60;
- edge >=+7.5pp;
- no line/price backfitting.

The prior live-only requirement for observed failed conversion/stall evidence is suspended in this postdraft-only mode because the user explicitly enabled postdraft Duration.

## 7. Total Kills — postdraft distribution mode

Total Kills is re-enabled after final draft + exact line/odds.

Before seeing the offered total line/price, construct a price-independent total-kill distribution.

Primary baseline:

`TK0 = average of each team's pre-series current-window map total-kill environment`, where a team's map total-kill environment is `team kills/game + team deaths/game` from reliable same-competition data (prefer Gol.gg). Blend a previous comparable window only when current sample/roster continuity requires it. If a reliable pre-series TK0 cannot be reconstructed, return HOLD for Total Kills rather than using the sportsbook line as the anchor.

Draft adjustment must explicitly score:

- repeatable engage/catch frequency;
- two-sided return-kill access;
- objective-fight forcing;
- reset/chase continuation;
- disengage/peel and safe concession;
- whether the likely winner closes cleanly or through repeated contested cycles.

Create total-kill bins (for example `<20`, `20-24`, `25-29`, `30-34`, `35-39`, `40+`) with probabilities summing to 100%. Lock this distribution before seeing the offered total line/odds.

After the line is revealed, derive Over/Under cover probability from the locked distribution.

Minimum Total Kills odds remain `1.60`. Initial reactivation edge requirement is `+7.5pp` versus raw break-even probability.

## 8. Price-independence / anti-price-only rule

For all four families:

- benchmark, draft mechanisms and family projection/distribution are locked before price is analytical evidence;
- odds may determine whether a valid thesis has sufficient value, but may not create the underlying thesis;
- no chase, rescue, martingale, averaging down, or opposite-side reaction to a prior loss;
- postdraft board movement may be repriced only while the draft is unchanged and the map has not begun.

## 9. Verdicts

Use compact verdict-first output:

- `TAKE CANDIDATE`
- `PASS`
- `HOLD`

No live prediction updates after map start under this mode.

For any TAKE CANDIDATE:

`USER_LINE_CONFIRMATION=PENDING — confirm exact market/line/odds still exists before map start.`

## 10. Supersession

While included by the active lock, this overlay supersedes only these conflicting clauses:

- v1.3 `LIVE MONEYLINE` timing requirement;
- v1.3 `No pregame or immediate-postdraft TAKE` clause;
- v1.3 retirement of Kill Handicap and Total Kills;
- live-state evidence requirements that are impossible by definition in postdraft-only mode.

All non-conflicting benchmark, causal-thesis, price-independence, position-blind, exposure, confirmation, and anti-chasing controls remain active.
