# KRXC vs BFXY — 2026-08-25 Afternoon Calibration Review

**Implementation status:** `CANONICAL / ACTIVE PROSPECTIVELY` under default-branch `models/lol/CURRENT_MODEL.md` after the user instruction **“Ok implement them now.”**

## Purpose

Post-slate calibration review for KRX Challengers vs BNK FEARX Youth, preserving historical verdicts while extracting process lessons for future authority epochs.

## Confirmed lessons

### A. Small kill-handicap asymmetry

A small underdog `+H` can be mathematically positive while still being structurally poor protection. In Game 3, KRX +1.5 was initially promoted too aggressively. The user correctly rejected it as too small. The lesson is not that small handicaps are universally bad: a small favorite `-H` can still be an efficient expression of a favorite edge. The structural problem is usually small underdog cushion that behaves too much like ML and can be erased by one normal late fight.

Canonical implementation uses state/distribution-dependent `DOG_CUSHION_CLASS = INSUFFICIENT / THIN / MATERIAL / LARGE`, downstream of the side-neutral KH margin distribution. `INSUFFICIENT` is an automatic SKIP; `THIN` is presumptive SKIP unless exceptional UCS + LAC + WMS proof suppresses the normal one-fight/cleanup expansion tail. Small favorite `-H` remains eligible when the common margin distribution and favorite-tail validator support it.

### B. Professional meta layer

Draft reading now distinguishes professional meta priority from solo-queue strength. Relevant pro variables include pick/ban priority on the competition patch, blind safety, flex value, pairing dependency, professional system/function value, player stage comfort, pocket-pick tax, and Fearless scarcity value.

High presence is not standalone proof of draft superiority.

### C. Archetype inventory in Fearless

Functional depletion matters more than raw champion count. Repeatedly consuming reliable engage junglers/supports, waveclear, front line, carry protection, first-move tools or other scarce functions is a series-pool event even if many legal champions remain.

### D. Draft causal order

The preferred pro draft read is:

`LANE STATES -> JUNGLE/SUPPORT ACCESS -> FIRST MOVE -> OBJECTIVE SEQUENCE -> TRANSITION QUALITY -> 2/3-ITEM FIGHT SHAPE -> WCSR -> EXECUTION BURDEN -> SERIES-POOL PRESSURE -> PRO ADVERSARIAL PASS`.

Champion labels alone are insufficient.

### E. Screenshot synchronization

If the user explicitly confirms paired market and scoreboard screenshots are the same state, phone/device capture times alone do not invalidate synchronization. Internal state contradictions still fail closed. The two-snapshot requirement for live ML/KH/TK remains unchanged.

### F. Recent workload

Playing the previous day, fast turnaround, travel or a long prior series belongs in professional execution context, not as a standalone fatigue fade. It may move a verdict only through an observable mechanism.

### G. Duration Over

Game 4 supported the existing causal DOVC framework: BFX obtained early objectives but repeatedly failed to convert into structures, and the map reached 34:36. This supports, but does not replace, the rule that low tower count or low kills alone are neutral; observed failed conversion/reset/clock-consuming mechanisms are required.

## Canonical files

- `models/lol/CURRENT_MODEL.md`
- `models/lol/procedures/LOL_PRO_META_AND_HANDICAP_ASYMMETRY_CALIBRATION_2026-08-25.md`
- `models/lol/procedures/LOL_PRO_META_LAYER_2026-08-25.md`
- `models/lol/procedures/LOL_KH_SMALL_HANDICAP_ASYMMETRY_2026-08-25.md`
- `models/lol/procedures/LOL_SCREENSHOT_SYNC_AND_WORKLOAD_CONTEXT_2026-08-25.md`
- `models/lol/procedures/LOL_PRE_TAKE_CERT_AFTERNOON_CALIBRATION_EXTENSION_2026-08-25.md`

## Historical preservation

Do not rewrite prior slate predictions, positions, or P/L under these new rules. The completed E13 KRX.C–BFX.Y lock remains historically frozen to its original authority. Apply this calibration prospectively through future locks whose authority commit contains the files above.
