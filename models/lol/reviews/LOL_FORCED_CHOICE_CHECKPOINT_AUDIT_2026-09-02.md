# LoL Draft-Only Forced-Choice Checkpoint Audit — 2026-09-02

**Status:** CHECKPOINT AUDIT COMPLETE — NO STRUCTURAL MODEL CHANGE AUTHORIZED BY THIS REVIEW

## Scope

Audit the canonical forced-choice cohort after five settled maps / twenty unique forced-choice Positions across four enabled market families.

Maps:
1. NS Challengers vs DNS Challengers — Game 4 — 2026-08-31
2. Gen.G vs KT Rolster — Game 3 — 2026-09-01
3. HLE vs T1 — Game 1 — 2026-09-02
4. HLE vs T1 — Game 2 — 2026-09-02
5. HLE vs T1 — Game 3 — 2026-09-02

Each map has one canonical Position per family: Moneyline, Kill Handicap, Duration, Total Kills. Shadow stake is 0.25u per Position; actual exposure is 0u.

Airtable duplicate cleanup was completed during this audit: duplicate HLE-T1 G1 map/Position rows were removed so the canonical cohort contains exactly 20 unique Positions.

## Cohort result

- Settled Positions: `20`
- Wins / Losses: `10-10`
- Shadow stake: `5.00u`
- Shadow P/L: `-0.3340u`
- ROI on shadow stake: `-6.68%`
- Actual exposure: `0u`

### By market family

| Family | W-L | P/L | Stake | ROI |
|---|---:|---:|---:|---:|
| Moneyline | 0-5 | -1.2500u | 1.25u | -100.00% |
| Kill Handicap | 3-2 | +0.1525u | 1.25u | +12.20% |
| Duration | 4-1 | +0.5795u | 1.25u | +46.36% |
| Total Kills | 3-2 | +0.1840u | 1.25u | +14.72% |
| **Total** | **10-10** | **-0.3340u** | **5.00u** | **-6.68%** |

The entire cohort loss is concentrated in Moneyline. The other three families combine for `+0.9160u`.

## Moneyline audit

Canonical selected-side results were 0-5.

Selected-side locked ML probabilities / raw implied probabilities where available:
- NS G4: NS `59.5%` vs `60.98%` implied — `-1.48pp` model edge — LOSS.
- GEN-KT G3: KT `44.5%` vs `36.46%` implied — `+8.04pp` — LOSS.
- HLE-T1 G1: HLE `59.5%` vs `60.98%` implied — `-1.48pp` — LOSS.
- HLE-T1 G2: HLE `59.5%` vs `62.89%` implied — `-3.39pp` — LOSS.
- HLE-T1 G3: T1 `49.5%` vs `43.96%` implied — `+5.54pp` — LOSS.

Important interpretation:
- three of five ML selections were knowingly negative raw model edge and existed only because the user-directed forced-choice override disables PASS;
- therefore 0-5 ML Position performance is not a clean test of the underlying selective ML strategy;
- however the two positive-edge ML selections also lost, so the family still warrants scrutiny.

The price-blind overall model winner was not 0-5: benchmark plus draft favored GEN over KT in GEN-KT G3 and HLE over T1 in HLE-T1 G3, both of which won. The more alarming signal is the **draft-edge label itself**.

## Draft-edge audit — primary alarm

The price-blind draft edge (`D`) pointed toward the losing team in all five audited maps:
- NS-DNS G4: `SLIGHT NS` -> DNS won.
- GEN-KT G3: `SLIGHT KT` -> GEN won.
- HLE-T1 G1: `SLIGHT HLE` -> T1 won.
- HLE-T1 G2: `SLIGHT HLE` -> T1 won.
- HLE-T1 G3: `SLIGHT T1` -> HLE won.

Observed draft-edge direction: `0/5`.

This is a strong warning, but five maps are still too few to justify coefficient-fitting. Under a simple independent 50/50 null, five consecutive wrong directions occur 3.125% of the time; real map outcomes are not independent coin flips, so this is diagnostic rather than proof.

### Root-cause pattern

The map reviews repeatedly show the same failure mode: overvaluing abstract composition shape such as `cleaner front-to-back`, `easier neutral 5v5`, or generic engage, while underweighting the opponent's actual repeatable mechanism and the state after first control is gained.

Examples:
- GEN-KT G3: theoretical KT engage was overcredited versus GEN TF/Skarner/Syndra pick control, Sivir/Karma disengage, and stronger execution prior.
- HLE-T1 G1: HLE catch/teamfight layering was overcredited versus T1 Pantheon/Ryze/Kalista/Renata tempo and ranged map pressure.
- HLE-T1 G2: HLE protected front-to-back was overcredited versus Blitzcrank/Qiyana/Anivia pick/choke geometry plus Gwen side pressure.
- HLE-T1 G3: T1 neutral 5v5 ease was overcredited versus HLE Camille/Sejuani/Shen multi-angle access, Akali follow-up, and Miss Fortune zone damage.

This is exactly the class of error the existing Draft Interaction Matrix is intended to prevent. The audit finds a **process-compliance gap**: recent handoffs often persisted a short mechanism summary rather than the full required DIM rows (`TAM / OSG / DAU / SLI / FNF / CAS / ETS / AFP`).

## Market-family audit

### Kill Handicap

Result: `3-2`, `+0.1525u`.

The family has been directionally better than ML, but outcomes are strongly bimodal: underdog +kills either covered comfortably / won outright, or failed in a clean cascade. This supports keeping explicit collapse-asymmetry (`CAS`) and return-kill-floor stress tests central. Five samples are insufficient for a formula change.

### Duration

Result: `4-1`, `+0.5795u` — best family in the checkpoint.

The duration engine is the most mechanically explicit and auditable family because `F` is locked before the line. Four of five maps finished below the selected line. The lone miss, HLE-T1 G2 Over 32, was a clean T1 cascade ending at ~29:23.

Recommendation: keep the duration formula frozen. Add no coefficient change from this checkpoint. Persist a diagnostic `CASCADE_CLOCK` note when one draft has a plausible fast-control branch, but do not backfit F from outcomes.

### Total Kills

Result: `3-2`, `+0.1840u`.

The family is positive but high-variance. Fast one-sided maps produced totals of 19, 25, 27, and 32 in this cohort, showing that `fast` does not map cleanly to either Over or Under. The procedure already requires a full total-kill distribution; recent handoffs sometimes persisted only a central expectation. That is insufficient for calibration audit.

Recommendation: preserve the existing TK framework, but enforce full pre-price bins on every map and explicitly separate:
- clean-cascade branch;
- two-sided brawl branch;
- controlled low-contact close branch.

## Error taxonomy summary

Canonical map primary errors in Airtable:
- `DRAFT READ ERROR`: 4 maps.
- `PROBABILITY/CALIBRATION ERROR`: 1 map (NS-DNS G4 Total Kills overprojection).
- `LIVE STATE ERROR`: 0 — live state is intentionally excluded in this mode.
- `PRICE/EXECUTION ERROR`: 0 decision-level errors identified.

Separate ledger-hygiene issue: duplicate HLE-T1 G1 map/Position rows existed in Airtable and were removed during this audit. This is not treated as a model decision error.

## Audit decisions

### 1. No formula or coefficient change yet

Each family has only five canonical samples. Do not fit new ML/Draft/KH/Duration/TK coefficients from this checkpoint. The initial architecture remains frozen.

### 2. Enforce the existing DIM in full immediately

Before the next draft verdict, persist a compact complete record:

`DIM[ROLES=P; PKM=...; SKM=...; TAM=...; OSG=...; DAU=...; SLI=...; FNF=...; CAS=...; ETS=...; AFP=...; EDGE=...]`

Do not issue `SLIGHT/CLEAR/STRONG` from generic labels such as front-to-back, engage, scaling, poke, or frontline without the interaction rows.

This is enforcement of existing authority, not a structural model change.

### 3. Tighten draft-edge certification without changing the 4.5pp coefficient

Because the observed D sign is 0/5, treat `D=+/-1` as certified only when the full DIM and adversarial pass identify at least two independent mechanism advantages with no unresolved direct counter-route. Otherwise return `D=0 / EVEN-STYLE-DEPENDENT`.

This is a procedural certification tightening consistent with the existing DIM; it is not a fitted outcome patch.

### 4. Persist auditable distributions

For every future forced-choice map:
- ML: store `P0`, `D`, final `P` before price.
- KH: store signed margin bins summing to 100% before line/price.
- Duration: store `V/Q/H/T`, `F` before line/price.
- TK: store total-kill bins summing to 100% before line/price.
- After price: store raw implied probability and `MODEL_EDGE` for selected side.
- Flag `FORCED_NEG_EV=YES/NO` so forced negative-value selections are separable from model-positive selections.

### 5. Forced-choice mode remains experimental

The user's `no PASS` instruction remains active. Negative-EV forced selections must not be mixed with threshold-qualified historical calibration. No chase, rescue, or stake escalation.

## Next audit cadence

Current family sample counts are five each.

- Next checkpoint: after **5 more maps / 20 more Positions**, reaching `10 samples per family / 40 forced-choice Positions total`.
- Structural coefficient review: prefer at least **20 samples per family / 80 forced-choice Positions total**, unless a clear mechanical implementation bug is discovered sooner.

## Bottom line

The current forced-choice cohort is slightly negative overall (`-0.3340u`), but the weakness is not broad across all families. Duration, KH, and TK are positive in this small sample. The main red flag is draft-edge classification: the `D` side lost all five maps. The correct immediate response is not coefficient backfitting; it is strict re-enforcement of the full Draft Interaction Matrix, stronger draft-edge certification, complete probability-distribution persistence, and separation of forced negative-EV selections from genuine model-positive selections.
