# LoL v1.0 Frozen Validation Protocol — 2026-08-29

**Status:** CANDIDATE UNTIL `CURRENT_MODEL.md` ACTIVATION  
**Model:** LoL v1.0 — Moneyline Core  
**Purpose:** prevent outcome-driven rule growth while establishing initial Moneyline calibration.

## 1. Initial evaluation sample

After v1.0 activation, freeze the analytical core for an initial sample of user-confirmed executable Moneyline Positions.

Target:

- minimum architectural review point: **20 confirmed Positions**;
- preferred full first review: **30 confirmed Positions**.

Only accepted Positions count toward the sample.

Do **not** count:

- HOLD;
- PASS;
- unconfirmed TAKE CANDIDATE;
- disappeared/moved lines that were never accepted;
- historical v0.x positions;
- Kill Handicap, Total Kills or Duration records.

## 2. What is frozen

Unless the user explicitly ends the freeze, do not change during the initial sample:

- the four live variables `R/X/O/T`;
- their `-2..+2` scale;
- draft unit `D = -1/0/+1`;
- mechanism states `INTACT / WEAKENING / BROKEN / REPLACED`;
- `D_eff` treatment;
- probability formula:
  `S = 1.0*D_eff + 1.5*R + 1.5*X + 1.25*O + 1.0*T`;
- `P = clamp(50% + 3*S pp, 15%, 85%)`;
- raw book implied probability `1/odds`;
- required edge `+5.0pp`;
- minimum accepted decimal odds `1.60`;
- live Moneyline-only scope;
- default shadow stake `0.25u`, actual exposure `0u`;
- user line-existence confirmation before Position creation.

An ordinary loss, win streak, one missed opportunity or one dramatic game does not justify changing these items.

## 3. Allowed changes during the freeze

Only the following may be corrected without treating the sample as a new model generation:

1. **governance/data-integrity repair** — broken file path, logging schema mismatch, stale authority pointer, impossible arithmetic typo, connector-writing bug;
2. **factual context correction** — wrong roster, patch, side, series format, exact draft or screenshot transcription;
3. **explicit user override** — the user directly authorizes ending or changing the freeze.

A factual correction must not be disguised analytical re-weighting.

If a material analytical formula/threshold change is explicitly authorized before the sample completes, close the current sample and start a new calibration epoch rather than mixing results silently.

## 4. Small audit taxonomy

Every reviewed accepted Position gets at most one primary error label when a meaningful miss is diagnosed:

- `DRAFT READ ERROR`
- `LIVE STATE ERROR`
- `PROBABILITY/CALIBRATION ERROR`
- `PRICE/EXECUTION ERROR`

### DRAFT READ ERROR

The pre-live professional mechanism/prior was materially wrong given information available at the time.

### LIVE STATE ERROR

The draft prior was reasonable, but `R/X/O/T`, mechanism contradiction, synchronization or causal interpretation of the current state was materially wrong.

### PROBABILITY/CALIBRATION ERROR

The state classification was reasonable but the probability mapping/weighting was systematically too high/low or the uncertainty buffer was miscalibrated.

### PRICE/EXECUTION ERROR

The probability estimate may be reasonable, but price use, line synchronization, executability, confirmation, logging or entry handling was wrong.

Do not create new named analytical gates as error labels.

## 5. Review cadence

### After each Position

Record contemporaneous:

- model probability for selected team;
- book implied probability;
- edge in percentage points;
- `D/MC/R/X/O/T`;
- odds and entry clock;
- user line confirmation;
- result after settlement.

Do not change the model because of that single result.

### At 10 confirmed Positions

Produce a **diagnostic-only** checkpoint:

- outcome count;
- average model probability;
- average implied probability;
- average quoted edge;
- Brier score if the data is complete;
- error-taxonomy counts;
- repeated qualitative patterns.

No architectural change by default.

### At 20 confirmed Positions

A preliminary architecture review is permitted, but the preferred default remains to continue to 30 unless there is a clear repeated failure pattern.

### At 30 confirmed Positions

Run the first full calibration review.

## 6. Evidence threshold for architectural change

A model change should normally require one of these:

1. **Repeated causal failure:** at least 3 independent accepted Positions, spanning at least 2 different series/matchups, show the same underlying causal error; or
2. **Calibration pattern:** a meaningful probability bias persists across at least 10 accepted Positions or a sufficiently populated probability band, rather than one result; or
3. **Clear mechanical defect:** the formula or procedure contains an objective implementation error rather than a prediction miss.

The purpose of these thresholds is not statistical proof. It is to prevent one-rule-per-loss mutation.

## 7. Calibration metrics

Primary model quality questions:

1. Are higher model probabilities actually winning more often than lower ones?
2. Is the model systematically overconfident or underconfident?
3. Do quoted +5pp edges persist across different teams/leagues rather than one matchup type?
4. Which of the four error categories repeats?

Track when possible:

- win/loss count;
- Brier score: `(p - outcome)^2`, with outcome 1 for win and 0 for loss;
- average model probability;
- observed win rate by broad probability band when sample size permits;
- average model edge at entry;
- shadow P/L as descriptive execution output.

Shadow P/L alone does not determine whether the model is calibrated.

## 8. Probability bands

For descriptive review only, group accepted selections into broad bands when enough observations exist:

- 40–49%
- 50–59%
- 60–69%
- 70–79%
- 80–85%

Do not create a new threshold because one band has one loss.

## 9. Miss review standard

Review using only information available at entry first.

The final result may tell us that the prediction lost, but it cannot prove which pre-entry mechanism was wrong.

Keep separate:

- `PREDICTION_RESULT = WIN / LOSS / PUSH / VOID`;
- `PROCESS_VALIDITY = VALID / INVALID`;
- optional primary error taxonomy.

A valid loss remains a loss. An invalid process does not erase the historical prediction.

## 10. Historical integrity

Do not relabel historical v0.x positions as v1.0.

Do not delete or rewrite:

- Airtable maps;
- snapshots;
- Positions;
- screenshots;
- reviews;
- historical P/L;
- old GitHub model/procedure files.

v0.3.58 and its overlays become historical/audit authority only after v1.0 activation.

## 11. Sample restart rule

If the user authorizes a material analytical change to the probability engine, edge threshold or variable definitions before completion, record the old sample as a closed calibration epoch and begin a fresh sample under the new authority.

Do not merge performance across materially different analytical cores as though they were one frozen model.
