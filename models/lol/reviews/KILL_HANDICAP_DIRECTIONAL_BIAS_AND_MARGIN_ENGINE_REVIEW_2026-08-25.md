# Kill Handicap Directional Bias & Margin-Engine Review — 2026-08-25

**Status:** CANONICAL REVIEW / v0.3.58 in-place amendment input  
**Date:** 2026-08-25 UTC+7  
**Scope:** Kill Handicap family only  
**Model:** LoL v0.3.58 remains canonical  
**Historical positions:** preserve exactly as recorded; this review does not rewrite any historical TAKE, result, P/L, or process-validity label.

## 1. User instruction

User instruction after reviewing repeated handicap losses:

> “Lock this slate. And adjust the model with your recommendations.”

This explicitly authorizes a new authority epoch for the current slate and an in-place v0.3.58 Kill Handicap amendment. It does not authorize v0.3.59/v0.3.60 or a new analytical version number.

## 2. Aggregate finding

The canonical Airtable Kill Handicap ledger shows a persistent directional skew toward positive handicaps.

At review time:

- settled underdog / positive-kill handicaps: **27 wins / 35 losses (43.5%)**;
- settled favorite / negative-kill handicaps: **2 total (1-1)**;
- approximately **97% of settled Kill Handicap selections** were on the positive-kill side;
- the recent 2026-08-20 through 2026-08-24 positive-handicap slice remained materially negative even after separating later process-invalidated losses from process-valid predictions.

The losses were not confined to thin cushions. Losing positive handicaps occurred across +3.5, +4.5, +5.5, +6.5, +7.5, +8.5, +10.5, +11.5, +12.5 and +14.5.

Therefore the primary problem is not a single cushion band. It is a systematic selection/calibration issue.

## 3. Existing rule that already identified the bias

`MODEL_RULES_LOL_V0.3.44.md` was created after the earlier handicap ledger reached 12/12 positive-side selections with a poor settled record.

Its central requirements were:

1. define a favorite independently of the displayed handicap;
2. construct one **side-neutral signed final kill-margin distribution**;
3. lock that distribution before using the displayed handicap as evidence;
4. price **both** +kills and -kills from the same distribution;
5. treat NKB / “favorite needs another X kills” as arithmetic only, never as probability evidence;
6. audit directional skew when one sign dominates selections.

Those requirements remain conceptually correct.

## 4. Rule-stack drift

Later v0.3.58 amendments correctly added strong positive-handicap mechanism controls:

`DCR / FF -> UDKC -> KPA/KMS -> RLD -> DIM/TAM/CAS -> UCS -> LAC -> LIVE_RLD`

These controls improved the model's ability to reject false underdog resilience.

However, execution gradually centered on answering:

> “Can the underdog survive this displayed cushion?”

rather than first answering:

> “What is the side-neutral final kill-margin distribution from this state?”

The current PRE_TAKE_CERT family manifest strongly enumerates underdog-resilience fields but does not explicitly force the complete v0.3.44 parent sequence of:

`MARGIN DISTRIBUTION -> BOTH SIDES PRICED -> LOWER-BOUND COVER -> BUFFER -> SIGN SELECTED AFTER DISTRIBUTION`.

This created a practical hierarchy inversion: tail-validation machinery became the source of the initial sign preference.

## 5. Predictive failure mechanism

### 5.1 KMS/LAC can be true locally but insufficient globally

A composition may possess real reset, return-kill, range or protected-DPS mechanisms and may even demonstrate them in one window, while the favorite still owns a meaningful serial wide-margin branch.

The handicap variable is final signed kill margin, not whether an underdog tool exists.

Therefore resilience mechanisms must modify a pre-existing margin distribution; they must not create the distribution themselves.

### 5.2 Deep NKB is being over-read

A favorite needing +7, +8, +10 or more additional net kills does not need to accumulate them as independent isolated events.

Professional kill margins are serially dependent:

`first winning contact -> cleanup -> objective -> deeper vision / map compression -> next forced entry -> structures -> base defense / terminal kills`.

Two ordinary linked 3-0 / 4-1 type cycles can erase a numerically deep cushion.

NKB is therefore a hurdle descriptor only.

### 5.3 Flat margin is not necessarily suppression

The model must distinguish:

- `NO_EXPANSION_OPPORTUNITY` — the favorite did not receive a representative pressured chance to expand the margin; from
- `EXPANSION_OPPORTUNITY_SUPPRESSED` — the favorite obtained meaningful pressure/contact leverage and the underdog concretely bounded the resulting net margin through reset, disengage, return kills, protected continuation, structural denial, or another repeatable mechanism.

Only the second is positive live anti-cascade evidence.

Elapsed time with a flat margin, passive farming, ordinary objective trading, 0-0 towers, or a lack of fights is not positive suppression proof.

### 5.4 Directional timing bias

Only one Kill Handicap TAKE may be consumed per map.

Positive handicaps often become superficially inspectable immediately after the two-snapshot gate, while favorite negative handicaps usually require later evidence for FFD, RNE, KCV and remaining forced-fight inventory.

If the model evaluates the positive side first, an early +kills TAKE can consume the family before the favorite-side thesis has matured.

This makes **analysis order itself** a directional bias source.

The correction is not to delay every +kills bet. The correction is to force a sign-neutral distribution and both-side pricing before either side is eligible.

## 6. Correct parent hierarchy

Kill Handicap must return to the following hierarchy:

`STATE + MKT + TEAM`

`-> KH_MARGIN_CERT (side-neutral)`

`-> PRICE BOTH SIDES FROM SAME DISTRIBUTION`

`-> WIDE_MARGIN_STRESS`

`-> PRELIMINARY BEST SIDE OR PASS`

`-> side-specific mechanism validation`

`-> uncertainty / retained phase buffer`

`-> PRE_TAKE_CERT`

`-> TAKE / HOLD / PASS`

The sign may not be selected before the distribution is locked.

## 7. Side-specific validators remain active

### Positive handicap

Retain all existing hard gates:

`DIM / PDRL where applicable / TAM / CAS / UDKC / KPA / KMS / RLD_DRAFT / False-Stable / LIVE_RLD / LIVE_PRESERVATION / LAC / UCS / SCNE / exact signed margin / NKB`.

Their role is to test whether the neutral distribution has allocated too much or too little probability to close favorite wins / underdog margin survival.

They cannot create an initial +kills edge.

### Negative handicap

Retain all existing controls:

`RNE / FFD / KCV / RFI / role-weighted lead quality / remaining compulsory-fight schedule / safe-concede routes / Structure Substitution / NKB/RFI/KCV retained checks`.

Their role is to test whether the neutral distribution has allocated too much or too little probability to wide favorite wins.

They cannot become automatically valid merely because +kills failed.

## 8. Non-complementarity hard rule

The following are mandatory:

- `FAVORITE -H FAIL` provides **zero positive evidence** for `UNDERDOG +H`;
- `UNDERDOG +H FAIL` provides **zero positive evidence** for `FAVORITE -H`;
- a side is eligible only from the common side-neutral distribution plus its own mechanism validator and pricing buffer.

The betting sides are complementary at settlement for half-kill lines, but **value certification is not logically complementary** because uncertainty and required edge buffers can make both sides PASS.

## 9. Wide-Margin Stress

Before any positive-handicap TAKE, construct the favorite's strongest **ordinary realistic** margin-expansion branch from the current state:

`next compulsory setup -> first contact -> normal cleanup/continuation -> objective/structure transition -> next forced entry -> terminal/base-defense exposure where realistic`.

This is not a catastrophic-tail ace scenario. It is the strongest ordinary professional cascade reasonably supported by current draft, economy, objective schedule, access and observed conversion.

The branch must be represented inside the same final-margin distribution.

If the +kills thesis only survives by omitting a materially probable serial favorite cascade, the distribution is invalid and the candidate is HOLD/PASS.

## 10. Directional calibration mode

The existing v0.3.44 directional-skew monitor is reactivated mechanically.

At the current approximately 97% positive-side selection share with negative positive-handicap performance:

`KH_DIRECTIONAL_CALIBRATION = ACTIVE`.

This state does **not** force favorite selections and does **not** invert the model.

While active:

- every KH candidate must build a complete side-neutral `KH_MARGIN_CERT`;
- both displayed sides must be priced from that exact certificate when both are available;
- `SIGN_SELECTED_AFTER_DIST = PASS` is mandatory;
- retained phase/uncertainty cover buffers remain mandatory;
- narrative-only “large cushion,” “needs X more kills,” or “favorite -H cannot prove FFD” reasoning cannot generate a +kills TAKE;
- the next handicap audit must explicitly report positive/negative selection share and ROI.

Directional calibration may be cleared only by a future explicit aggregate review showing that the sign-selection bias has materially normalized; one or two opposite-side bets do not clear it.

## 11. No automatic favorite pivot

This review does not conclude that favorite -kills is profitable. The settled negative-handicap sample is too small.

The correction is:

> **predict the kill margin first; choose the sign second.**

If a genuinely side-neutral process later produces mostly positive handicaps, that is acceptable. Directional diversity is a diagnostic, not a quota.

## 12. Canonical action

Create and activate:

`models/lol/procedures/LOL_KILL_HANDICAP_SIDE_NEUTRAL_MARGIN_ENGINE_2026-08-25.md`

Update `CURRENT_MODEL.md` and the PRE_TAKE_CERT mechanical validator so the side-neutral margin certificate is the parent gate for **both** Kill Handicap directions.

Relock the current slate to the resulting authority commit as explicitly authorized by the user.
