# LoL Draft-Only Forced-Choice Checkpoint Audit — 40 Positions — 2026-09-03

**Status:** CHECKPOINT COMPLETE — CANONICAL v1.3 UNCHANGED / NEXT FORCED-CHOICE OVERLAY QUARANTINE DEFINED

## 1. Scope

Audit the canonical draft-only forced-choice cohort at the planned checkpoint of exactly:
- `40 unique settled Positions`;
- `10 samples per market family`;
- `10 fully recorded maps`;
- `0.25u shadow per Position`;
- `0u actual exposure`.

The cohort is the experimental no-PASS overlay only. It is not the threshold-qualified selective v1.3 calibration sample.

The 40-position Airtable ledger was re-read at checkpoint and contains exactly 40 unique records whose Entry Evidence is tagged `FORCED-CHOICE`.

## 2. Overall result

- Settled Positions: `40`
- Wins / Losses: `17-23`
- Shadow stake: `10.00u`
- Shadow P/L: `-2.0755u`
- ROI on shadow stake: `-20.755%`
- Actual exposure: `0u`

### By family

| Family | W-L | P/L | Stake | ROI |
|---|---:|---:|---:|---:|
| Moneyline | `1-9` | `-2.0805u` | `2.50u` | `-83.22%` |
| Kill Handicap | `4-6` | `-0.6225u` | `2.50u` | `-24.90%` |
| Duration | `7-3` | `+0.7770u` | `2.50u` | `+31.08%` |
| Total Kills | `5-5` | `-0.1495u` | `2.50u` | `-5.98%` |
| **Total** | **17-23** | **-2.0755u** | **10.00u** | **-20.755%** |

The overall loss is dominated by Moneyline. Excluding ML, the other three families combine for `+0.0050u`, effectively flat.

## 3. First 20 vs second 20

The prior checkpoint at 20 Positions was `10-10 / -0.3340u`.

Incremental Positions 21-40:
- `7-13`
- `-1.7415u`

Incremental by family:
- ML: `1-4 / -0.8305u`
- KH: `1-4 / -0.7750u`
- Duration: `3-2 / +0.1975u`
- TK: `2-3 / -0.3335u`

Full-DIM enforcement therefore did not repair Moneyline or KH in the second block.

## 4. Moneyline / Draft-edge audit — primary failure

### Selected ML performance

Canonical Moneyline record is `1-9 / -2.0805u`.

This is not explained only by forced negative-EV selections.

Across the 10 ML Positions:
- forced/known negative raw-edge selections include five cases; their result is `1-4`;
- model-positive selected ML cases are `0-5`.

Therefore the no-PASS override worsens the sample, but the model-positive ML subset is also failing.

### Draft-edge direction

At the 20-position audit, nonzero `D` pointed to the losing team in all five audited maps.

In maps 6-10:
- HLE-T1 G4: `D=0`;
- HLE-T1 G5: `D=+1 HLE` -> HLE won — correct;
- DK-BFX G3: `D=0`;
- DK-BFX G4: `D=+1 BFX` -> DK won — wrong;
- DK-BFX G5: `D=+1 BFX` -> DK won — wrong.

Across the full 10-map cohort:
- nonzero certified `D` maps: `8`;
- correct `D` direction: `1`;
- wrong `D` direction: `7`;
- observed directional accuracy: `12.5%`.

The later DK-BFX G4/G5 misses occurred **after** full DIM rows and the two-independent-mechanism adversarial certification rule were enforced. The earlier diagnosis of a process-compliance gap is therefore no longer sufficient by itself.

### Interpretation

Do not conclude that draft has negative causal value in League of Legends. The sample is small, correlated by series, and forced-choice selection interacts with bookmaker prices. However, this experimental implementation has not earned a positive ML probability correction from `D`.

The failure pattern is concentrated in converting qualitative draft mechanism advantages into a fixed `+/-4.5pp` probability shift.

### Checkpoint decision — forced-choice overlay only

For the **next draft-only forced-choice validation block**:

- continue the complete `PKM / SKM / TAM / OSG / DAU / SLI / FNF / CAS / ETS / AFP` DIM;
- continue to record the certified `D` label exactly as before;
- set `D_PROBABILITY_CONTRIBUTION=0` inside the forced-choice overlay;
- forced-choice ML probability is therefore the frozen benchmark `P0` only;
- store `D_DIAGNOSTIC_ONLY=YES` on every ML record;
- do **not** change canonical v1.3 live/selective Moneyline authority from this experiment.

This is a validation quarantine of an unstable experimental correction, not fitted replacement coefficients.

Reconsider a nonzero draft-to-probability coefficient only at the next formal checkpoint with materially more nonzero-D observations.

## 5. Kill Handicap audit — calibration/tail alarm

Canonical KH result:
- `4-6 / -0.6225u`.

First five maps were `3-2`; maps 6-10 were `1-4`.

The second block contains repeated large-margin failures of plus handicaps, including:
- T1 `+6.5` losing to a 15-kill margin;
- T1 `+4.5` losing to a 13-kill margin;
- BFX `+7.5` losing to a 10-kill margin;
- BFX `+3.5` losing to a 10-kill margin.

The main error is not merely side choice. It is **tail compression / false confidence** in manually constructed signed kill-margin distributions. Reported cover probabilities such as `72%`, `85%`, and `70%` were not supported by the observed blowout frequency.

### Checkpoint decisions

Prospectively in the next forced-choice overlay:

1. Keep the user-directed portfolio rule:
   - absolute KH `<5`: selected team must align with selected ML team;
   - `+/-5.5` or wider may remain independent.
2. Keep full signed margin bins before price.
3. Require explicit numeric mass in both teams' `10+ kill` clean-cascade tails before line evaluation.
4. Apply `KH_MODEL_PROB_CAP=70%` for execution-edge reporting and side comparison until the family reaches the next checkpoint.
   - raw distribution probability is still persisted for audit;
   - `KH_CAPPED_PROB` is the probability used for `MODEL_EDGE` in forced-choice execution.
5. No fitted new variance/tail coefficients are authorized at 10 samples.

The 70% cap formalizes the confidence haircut already used on DK-BFX G5 and prevents another unsupported 80%+ cover claim while the distribution engine remains manually calibrated.

## 6. Duration audit — retain

Canonical Duration result:
- `7-3 / +0.7770u`;
- ROI `+31.08%`.

Direction split:
- Under selections: `7-0`;
- Over selections: `0-3`.

This asymmetry is diagnostic, especially because all three selected Overs failed below the line, but 10 samples are insufficient to refit the formula. Duration remains the best-performing and most mechanically constrained family.

### Decision

- keep the v1.1 formula and `31.0m` neutral anchor frozen;
- keep price-blind `V/Q/H/T/F` persistence;
- add `OVER_BRANCH_WARNING=YES` diagnostically whenever a draft-only Over is selected, until the next checkpoint;
- do not alter coefficients or the Over/Under probability slope from this sample.

## 7. Total Kills audit — near flat

Canonical TK result:
- `5-5 / -0.1495u`;
- ROI `-5.98%`.

The family is broadly near breakeven, but DK-BFX G3-G5 produced three consecutive Over misses as the maps finished with `25 / 22 / 22` total kills. G4 and G5 especially showed the same structural pattern: a one-sided fast close suppressed opponent return kills despite substantial theoretical forced-contact inventory.

### Decision

- keep `TK0` benchmark construction unchanged;
- keep full pre-price bins;
- require an explicit numeric `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` branch on every map, separate from generic clean-cascade and two-sided-brawl branches;
- no coefficient or baseline change at 10 samples.

## 8. Portfolio-coherence rule audit

The `<5 kills => ML-aligned KH` rule was introduced prospectively late in the cohort and has only one fully settled sample under the rule (DK-BFX G5).

That sample lost both BFX ML and BFX +3.5, but one sample is not evidence to remove the rule.

Decision: **retain the rule unchanged** for the next validation block.

## 9. Error taxonomy

Primary checkpoint diagnoses:

- **DRAFT READ / DRAFT-TO-PROBABILITY ERROR:** dominant ML issue; full DIM certification still produced wrong nonzero-D directions in DK-BFX G4/G5.
- **PROBABILITY/CALIBRATION ERROR:** KH tail compression and extreme cover confidence.
- **DURATION:** no structural error established; retain.
- **TOTAL KILLS:** calibration/branch-weight warning, especially one-sided return-kill suppression; no structural formula failure established.
- **PRICE/EXECUTION:** no execution integrity failure identified; all Positions were 0.25u shadow / 0u actual and map-end settlement discipline was preserved.

## 10. Canonical model boundary

`CURRENT_MODEL.md` remains canonical LoL v1.3 authority and is **not edited by this checkpoint**.

The forced-choice cohort is a lock-scoped experiment that activates retired KH/TK families and immediate postdraft execution contrary to canonical selective scope. Its results must not silently rewrite the canonical live/selective model.

The quarantine decisions in this review apply only if a future fresh Session Authority Lock explicitly activates a new draft-only forced-choice validation block.

## 11. Next cadence

At checkpoint completion:
- `40 positions / 10 per family`.

Preferred next structural calibration checkpoint:
- `80 positions / 20 per family`;
- `10 additional fully recorded maps / 40 additional Positions`.

Earlier review is permitted only for a clear implementation bug or data-integrity failure.

## 12. Series closure

DK-BFX final series state:
- DK won Game 3;
- DK won Game 4 `16-6` in `22:43`;
- user-designated final Game 5: DK won `16-6` in `24:42`;
- final series score: **Dplus KIA 3-2 BNK FearX**.

No additional DK-BFX Position may be created. The session lock must be closed/staled before any new match work.

## Bottom line

At 40 Positions the experiment is materially negative (`-2.0755u`), but the weakness is highly concentrated. Duration is profitable, TK is near flat, KH shows an overconfidence/tail problem, and ML is failing even when raw model edge is positive. Full DIM enforcement did not rescue the fixed draft probability correction.

The correct checkpoint response is **not coefficient backfitting**. It is to quarantine `D` from forced-choice ML probability, cap KH confidence, retain the portfolio rule, keep Duration frozen, strengthen explicit TK return-kill-suppression branching, close the completed series lock, and require a fresh lock before any next validation block.
