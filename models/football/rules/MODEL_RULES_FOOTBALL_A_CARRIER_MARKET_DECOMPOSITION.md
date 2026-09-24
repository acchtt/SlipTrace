# Football A — Carrier Market Decomposition + Market-Calibrated PRE

**Status:** ACTIVE prospectively from 2026-09-24 ICT  
**Scope:** Football A senior-match PRE/XI/odds workflow  
**Historical rule:** Never rewrite a frozen historical decision or backfill a bet.

## Why this patch exists

The Sep-23/24 audit showed a recurring anti-selection failure:

- elite/extreme carrier matches were structurally identified but assigned PRE burdens far below the actual scoring environment;
- decay-first then waited for lines that were functionally unreachable before a goal;
- lower-ceiling matches were easier to execute merely because O2.25/O2.5 was accessible.

This patch makes **Asian handicap + total + 1X2** core carrier-identification inputs after XI is known.

## 1. Preserve structural PRE, add market-calibrated current PRE

Work/frozen PRE remains the historical price-blind structural snapshot.

At XI + user-odds stage, create a separate:

`MARKET-CALIBRATED CURRENT PRE`

This current PRE may raise or lower the actionable burden when football + XI + market decomposition jointly justify it. Persist both values separately. Never overwrite the frozen PRE.

## 2. Mandatory market decomposition

Use the main Asian total `T`, the favorite Asian handicap magnitude `H`, and the 1X2 favorite price.

For carrier screening only:

`MARKET CARRIER LOAD (MCL) ≈ (T + H) / 2`

`MARKET OPPONENT SHARE (MOS) ≈ max(0, (T - H) / 2)`

These are **decomposition heuristics, not literal xG estimates**.

Interpretation:

- high total + modest handicap = more two-sided;
- high total + large favorite handicap = carrier-led;
- high total + extreme handicap + very short 1X2 = favorite expected to fund most of the total.

## 3. Carrier screen tiers

### ELITE MARKET-CARRIER RE-SCREEN

Mandatory when either:

- `MCL >= 3.25` and `MOS <= 1.00`, with favorite `<= 1.12`; or
- Asian handicap is `-2.50` or stronger and the total is `3.75+`.

This forces a football/XI carrier re-screen. It does not automatically create a bet.

### EXTREME MARKET CARRIER

Eligible when all are true:

- `MCL >= 3.50`;
- `MOS <= 0.75`;
- favorite is normally `<= 1.08` **or** handicap is `-3.00` or stronger;
- confirmed XI preserves the attacking mechanism;
- no specific mechanism-compatible suppression veto remains.

A current score sample that lacks recent 3+ outputs may **not by itself** block this lane when the total, handicap and favorite price jointly imply a dominant carrier and the XI supports that interpretation.

Persist:

`MARKET CARRIER = ELITE / EXTREME / NOT CLEARED`

and the calculated MCL/MOS.

## 4. XI / absence mechanism test

Do not downgrade by number of changes or absences alone.

Assess whether the carrier still retains enough of:

1. primary chance creators;
2. progression / runners;
3. penalty-box finishers;
4. set-piece / secondary scoring channels;
5. bench or rotation depth capable of sustaining pressure.

Use:

- `MECHANISM PRESERVED`;
- `MECHANISM PARTIALLY PRESERVED`;
- `MECHANISM DAMAGED`.

Large headcount rotation may remain eligible when the mechanism is preserved. Small numerical rotation may still be damaging when key roles disappear.

## 5. Market-calibrated carrier burden

When ELITE/EXTREME carrier status clears:

1. Re-estimate the structural scoring band using football evidence + XI + MCL/MOS.
2. Do **not** apply the old fixed +0.25/+0.50/+0.75 uplift cap.
3. Do **not** force the actionable line back to the old frozen burden merely because it is safer.
4. The normal initial carrier-line anchor is:

`PREFERRED CURRENT PRE ≈ MARKET CENTER - 0.25`

subject to football support.

5. The balanced market-center total itself may be the **upper execution boundary** when:
   - carrier status is EXTREME or strongly ELITE;
   - XI mechanism is preserved;
   - no specific suppression veto remains;
   - price clears the active floor.

The market may corroborate and calibrate a verified carrier, but **market alone cannot rescue a broken XI or a genuine suppression branch**.

## 6. Execution authority

For a cleared ELITE/EXTREME carrier lane, this patch overrides conflicting decay-first language that would otherwise require return to the old frozen burden.

Execution order becomes:

`FOOTBALL STRUCTURE -> XI MECHANISM -> TOTAL + AH + 1X2 DECOMPOSITION -> CURRENT PRE BAND -> LOWEST AVAILABLE LINE INSIDE BAND THAT CLEARS FLOOR -> PRICE`

If the preferred current PRE line is available at `>=1.65`, it is directly executable subject to the normal exposure gate.

If the preferred line is below the price floor but the market-center line is within the verified carrier band and clears `>=1.65`, the market-center line may execute as:

`DIRECT LOCK ELIGIBLE — MARKET-CALIBRATED ELITE CARRIER`

Do not wait for an artificially low raw frozen burden.

## 7. Unreachable-decay guard

For every WAIT decision, calculate:

`DECAY GAP = current market center - target line`

If `DECAY GAP >= 1.00`, ordinary 0-0 decay is presumed potentially unreachable before a score-state change.

If `DECAY GAP >= 1.50`, a raw-burden WAIT is prohibited unless there is a documented reason the current market is distorted.

The system must instead:

- run this carrier decomposition;
- establish a market-calibrated current PRE if justified; or
- PASS/HOLD.

Never create a qualified plan whose target is only theoretically attractive but practically unavailable.

## 8. B+ leakage-only caution

For ordinary B+ carrier-led matches outside ELITE/EXTREME status:

- an opponent who is only `LEAKAGE/FAILURE SUPPORT` is not an independent scoring route;
- direct exposure at the protected line requires stronger carrier failure-resistance;
- prefer repeatable self-funded 3+ capacity or strong current chance-quality evidence.

This prevents accessible low lines from outranking much stronger carrier environments merely because they are easier to buy.

## 9. Cup / first-leg handling

Cup or first-leg status is **context**, not an automatic suppression downgrade.

Apply a burden reduction only when a specific control/compression mechanism is supported by current evidence: tactical incentive, matchup history that matches current mechanisms, expected game-state management, or relevant XI structure.

## 10. Ranking and selection invariant

Selection priority is now:

`STRUCTURAL CEILING -> CARRIER IDENTITY -> XI MECHANISM -> REALISTIC EXECUTABLE BURDEN -> PRICE`

Never:

`EASIEST LOW LINE TO REACH -> SELECTION`

A lower protected line does not make a weaker scoring environment a better selection.

## 11. Required persisted fields / notes

Whenever this patch is triggered, persist:

- frozen structural PRE;
- market total center;
- Asian handicap;
- 1X2 favorite price;
- MCL;
- MOS;
- market-carrier tier;
- XI mechanism state;
- market-calibrated current PRE preferred line;
- upper execution boundary;
- decay gap if a WAIT is considered;
- specific suppression veto, if any;
- final execution class and exposure decision.

## 12. Historical calibration examples — audit only

Sep-23/24 audit examples that motivated the patch, not retroactive bets:

- Lyon: extreme carrier profile;
- Wolfsburg: extreme carrier profile;
- Ajax: elite/extreme carrier profile;
- Barcelona: extreme carrier profile;
- Chelsea: extreme carrier profile and losing counterexample;
- Manchester United: extreme carrier profile that the old recent-score test wrongly left at B+.

Final scores must never be used to decide whether a future match qualifies.
