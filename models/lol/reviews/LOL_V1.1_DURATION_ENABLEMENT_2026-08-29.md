# LoL v1.1 Duration Enablement Record — 2026-08-29

**Status:** CANDIDATE TRANSITION RECORD UNTIL ACTIVATION  
**From:** LoL v1.0 — Moneyline Core  
**To:** LoL v1.1 — Moneyline + Duration Core

## Authorization

On 2026-08-29 UTC+7 the user explicitly requested:

`odds for mnl is very low, enable duration as well`

This is treated as explicit authorization to end the Moneyline-only market-scope freeze and open a new calibration epoch with Duration active alongside Moneyline.

At the time of authorization, the v1.0 accepted Moneyline validation sample contained **0 confirmed Positions**, so no accepted v1.0 outcomes are mixed into the new epoch.

---

# 1. What remains unchanged

The v1.0 Moneyline Core analytical formula and controls remain unchanged inside v1.1:

- compact professional Draft Prior;
- `R/X/O/T` live state;
- mechanism contradiction;
- ML probability formula;
- minimum odds 1.60;
- ML required edge +5.0pp;
- synchronized evidence;
- position-blind reassessment;
- user line confirmation before Position creation;
- 0u actual exposure and fixed shadow stake policy.

Duration enablement is not permission to loosen ML because favorite odds are unattractive. Low ML price creates no analytical evidence.

---

# 2. Why Duration returns as a new core rather than legacy restoration

The v1.0 clean rebuild retired Duration because derivative/time forecasting introduced extra assumptions and the historical v0.3.58 implementation had accumulated a large certificate tree.

The user has now explicitly chosen to re-enable the family. The correct response is a small independent Duration model, not restoration of historical DOVC/FCR/FRP machinery.

Historical Duration materials remain useful research evidence but are not active authority.

---

# 3. Historical lesson retained

The 2026-08-23 FNC–SHFT / SK–MKOI review identified two important Duration errors:

1. FNC–SHFT Game 2 Over 34 @2.269 lost at 33 minutes after theoretical Taliyah/Tristana waveclear was treated as if it were observed conversion denial.
2. SK–MKOI Game 1 Over 32 @2.128 lost after low kills, close gold, 0–0 towers and neutral objectives were treated as positive stall evidence even though no meaningful conversion opportunity had actually failed.

The useful principle is absorbed into one continuous variable:

- `V — Net conversion velocity`

Absent conversion is neutral. Demonstrated stalled/failed conversion produces negative `V`; demonstrated serial conversion produces positive `V`.

There is no separate DOVC certificate.

Reference historical review:
`models/lol/reviews/LEC_FNC_SHFT_SK_MKOI_SESSION_REVIEW_2026-08-23.md`.

---

# 4. Initial Duration calibration anchor

Airtable was used as historical ledger evidence.

At activation research time, 31 completed August 2026 LCK Maps records had usable Duration fields. Derived descriptive statistics:

- median approximately `30:55`;
- mean approximately `31:59`;
- population standard deviation approximately `5.0 minutes`.

The neutral anchor is therefore fixed at **31.0 minutes** for the initial validation epoch.

The central duration model is:

`R0(t) = max(5.0, 31.0 - t)`

`ER = max(2.0, R0 - 1.5*V + 1.0*Q + 1.0*H + 0.75*T)`

`F = t + ER`

where:

- `V` = net conversion velocity;
- `Q` = compulsory-cycle spacing;
- `H` = terminal path depth;
- `T` = terminal trajectory.

All are scored on `-2..+2`.

---

# 5. Probability mapping

After central final estimate `F` is locked, offered Duration line `L` is read:

`P(OVER) = clamp(50% + 7*(F-L) pp, 15%, 85%)`

`P(UNDER) = 100% - P(OVER)`

The `7pp/min` slope is intentionally slightly flatter than the roughly 8pp/min center slope suggested by a normal-like distribution with ~5 minute standard deviation.

This is a conservative initial mapping, not a fitted claim of statistical optimality.

---

# 6. Price threshold

Duration uses:

- minimum odds `1.60`;
- required edge `+7.5pp` versus raw implied probability.

The higher edge requirement than ML reflects greater uncertainty in final-clock projection.

One ordinary `Q` or `H` scoring step changes probability by ~7pp; one `V` step changes it by ~10.5pp. The +7.5pp threshold is therefore approximately one ordinary state-step uncertainty buffer.

---

# 7. Active / retired scope after activation

Active:

- Moneyline;
- Duration Over / Under.

Retired:

- Kill Handicap;
- Total Kills.

Historical files/records/screenshots/reviews/results/P&L remain unchanged.

---

# 8. Validation

v1.1 starts fresh family-specific sample counts:

- `ML_SAMPLE_N = 0`;
- `DURATION_SAMPLE_N = 0`.

Review each family at 10 diagnostic, 20 minimum architecture review, 30 preferred full calibration review.

Do not add one new rule after one Duration loss.

Primary error taxonomy remains:

- DRAFT READ ERROR;
- LIVE STATE ERROR;
- PROBABILITY/CALIBRATION ERROR;
- PRICE/EXECUTION ERROR.

---

# 9. Activation condition

v1.1 becomes active only when:

1. Duration rules exist;
2. Duration live procedure exists;
3. v1.1 validation protocol exists;
4. v1.1 authority/execution governance exists;
5. `CURRENT_MODEL.md` activates Moneyline + Duration;
6. a fresh Session Authority Lock freezes an authority commit containing the complete stack.

Until all six are complete:

`MODEL REBUILD IN PROGRESS — HOLD`
