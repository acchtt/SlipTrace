# Kill Handicap Directional Recalibration Review — 2026-08-26

**Status:** canonical audit supporting immediate user-authorized recalibration  
**User authorization:** 2026-08-26 ~17:54 UTC+7 — “Recalibrate now”  
**Model:** LoL v0.3.58 remains unchanged  
**Scope:** Kill Handicap sign selection, final-margin tails, underdog +kills live anti-cascade proof, and favorite -kills evaluation

## 1. Batch evidence

Airtable Positions audit for the Aug 19–26 guard era shows 16 settled underdog +kills selections:

- Wins: 4
- Losses: 12
- Shadow P/L: -2.0665u
- Settled stake: 4.0u
- ROI: -51.7%

The ten most recent logged Kill Handicap picks were all positive-handicap selections. Their outcomes were 2 Wins, 7 Losses, 1 Void.

This is not used as a raw empirical probability model and does not justify blindly selecting favorite -kills. It is strong evidence that the active execution stack has continued to produce directional selection bias despite the 2026-08-25 side-neutral parent engine.

## 2. Repeated mechanism failure

The recurring failure is not simply that an underdog later lost by a wide margin. The repeated process pattern is:

1. a large displayed +H cushion is noticed;
2. exact NKB arithmetic makes the cushion sound deep;
3. theoretical waveclear, peel, disengage, counter-engage, side pressure, scaling or return-kill tools are listed;
4. those theoretical tools are treated as if they establish live anti-cascade suppression;
5. the favorite’s actual repeatable margin-expansion mechanism is not matched against a demonstrated underdog answer;
6. one or two ordinary professional objective/contact cycles consume the supposedly deep cushion.

Game 3 KT +9.5 vs BRO is the reference incident. At entry BRO led 5-2 and +3.1k with one dragon. BRO needed +7 additional future net kills to defeat KT +9.5 and finished 13-3, expanding the margin by exactly +7. KT’s Wukong/Bard/Sivir/Yorick theoretical fallback inventory did not directly suppress BRO’s actual Jayce/LeBlanc/Ezreal/Elise pre-contact poke/pick/range mechanism.

## 3. Diagnosis

### 3.1 NKB was being used as psychological probability evidence

The written model says NKB/RNE are arithmetic only, but execution repeatedly treated “needs another +7/+8/+10” as implicitly unlikely. Kill margins are serially dependent. A fight can create objective control, deeper vision, a second forced entry and base-defense exposure. Therefore the correct question is not how many net kills remain in isolation, but whether the ordinary one- or two-cycle favorite cascade can cross the failure threshold.

### 3.2 LAC was insufficiently mechanism-matched

The active LAC procedure already forbids theoretical utility from substituting for live proof. Execution still passed dog positions using generic anti-cascade language. Recalibration therefore needs mechanical fields that identify:

`FAVORITE_EXPANSION_MECHANISM`

`UNDERDOG_DIRECT_ANSWER`

`MATCHED_SUPPRESSION_EVIDENCE_ID`

If the underdog answer does not directly address the favorite’s repeatable expansion route, LAC cannot pass.

### 3.3 One observed event is too permissive during directional calibration

The older LAC wording allows a single favorable event to pass if sufficiently strong. Given the batch evidence, that exception is suspended while directional probation is active. A dog +H TAKE must demonstrate mechanism-matched suppression in two distinct representative expansion-opportunity windows.

### 3.4 Cushion classification must use cycle-crossability

A visually large +9.5/+11.5/+14.5 line can still be functionally thin when the current favorite margin plus an ordinary one- or two-cycle cascade reaches the failure threshold. Cushion labels must therefore be conditioned on WMS and forced-cycle crossability, not absolute H.

### 3.5 Favorite -H has been under-considered, not merely under-selected

The fix is not a favorite quota. Favorite -H remains eligible only when the same locked margin distribution and favorite-tail validator clear the line. But the system must not reject favorite -H merely because a safe-concede route exists after the favorite can plausibly bank the required margin earlier in the map. The new validator therefore distinguishes `COVER_BEFORE_CLOSE` from terminal concede behavior.

## 4. Immediate recalibration design

Activate `KH_DOG_DIRECTIONAL_PROBATION = ACTIVE`.

While active, underdog +H requires all retained gates plus:

- `DOG_CUSHION_CLASS = LARGE`; MATERIAL is no longer TAKE-eligible during probation;
- two distinct mechanism-matched live suppression windows;
- explicit favorite expansion mechanism and direct underdog answer;
- one-cycle and two-cycle WMS margin ranges;
- `DOG_FAILURE_THRESHOLD_CROSSABLE = NO` for any MATERIAL/HIGH ordinary WMS branch, or else automatic PASS;
- an additional 5 percentage-point dog calibration buffer on top of the retained base phase/uncertainty buffer;
- no single-event LAC exception;
- no credit for 0-0 towers, elapsed quiet, theoretical utility, current cushion or NKB by themselves.

Favorite -H keeps the normal retained buffer and gains an explicit `COVER_BEFORE_CLOSE` test so late safe-concede risk is not incorrectly applied to margin that can be realized before terminal structure closure.

## 5. Anti-overfit guard

This recalibration does not:

- force favorite picks;
- impose a directional quota;
- convert historical losses into HOLDs;
- use the 4-12 sample as direct cover probability;
- create a universal numeric definition of LARGE H;
- relax favorite mechanism proof;
- remove side-neutral distribution-first pricing.

The purpose is to stop the process from treating theoretical underdog survivability and large displayed cushions as observed live margin suppression.

## 6. Clearing condition

`KH_DOG_DIRECTIONAL_PROBATION` does not auto-clear from one win or one favorite selection. It requires a future explicit aggregate KH review after a meaningful prospective sample. Sign distribution is diagnostic only; there is no required favorite/dog quota.
