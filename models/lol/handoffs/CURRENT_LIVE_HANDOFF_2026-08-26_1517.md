# LoL Live Handoff — KT Rolster vs HANJIN BRION — 2026-08-26 15:17 UTC+7

**Status:** `ACTIVE LIVE HANDOFF`  
**Session lock:** `LOL-2026-08-26-E14-KT-BRO-1432-UTC7`  
**Series:** `LCK 2026 Play-In — KT Rolster vs HANJIN BRION — BO5`  
**Current series score:** `0-0`  
**Current map:** `Game 1 — LIVE`  
**Frozen authority commit:** `95af8bcde298772e28f963818a71f0653d602a69`  
**Model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR`  
**PDRL:** `ACTIVE`  
**PML:** `ACTIVE`  
**KH directional calibration:** `ACTIVE`  
**Small-H asymmetry calibration:** `ACTIVE`  
**Shadow stake:** `0.25u`  
**Actual exposure:** `0u`  
**Minimum odds:** `1.60`

## Continuation instruction

The user requested continuation in another chat and preservation of all material live state. This handoff must be loaded **last** after the exact E14 bootstrap/locked-authority sequence in `CURRENT_SESSION_LOCK.md`.

Do not perform model-certified live analysis until the E14 bootstrap is complete. If live evidence arrives first, fail closed with the lock/bootstrap HOLD language required by the active procedures.

## Confirmed Game 1 starting lineups

Current starters are now verified from the user-supplied live scoreboard and have been persisted in Airtable `Rosters — LCK`.

### KT Rolster
- Top: **Perfect**
- Jungle: **Cuzz**
- Mid: **Bdd**
- ADC: **Jiwoo**
- Support: **Effort**

### HANJIN BRION
- Top: **Casting**
- Jungle: **GIDEON**
- Mid: **Roamer**
- ADC: **Teddy**
- Support: **Namgung**

These live-scoreboard starters supersede the lock-creation state that marked lineups unconfirmed. Player-specific PML fit may now use these exact five, subject to retained evidence standards.

## Game 1 exact draft

### HANJIN BRION
- Casting — **Kled**
- GIDEON — **Jarvan IV**
- Roamer — **Anivia**
- Teddy — **Lucian**
- Namgung — **Milio**

### KT Rolster
- Perfect — **Olaf**
- Cuzz — **Nocturne**
- Bdd — **Ryze**
- Jiwoo — **Miss Fortune**
- Effort — **Nautilus**

Do **not** mark these champions as completed Fearless depletion until Game 1 ends. They are the current-map draft inventory only.

## Latest live scoreboard state

User-supplied scoreboard source at **8:36** game clock:

- Kills: **BRO 0 — 2 KT**
- Gold: **KT +805**
- Towers: **0-0**
- Dragons: **0-0**
- Barons: **0-0**
- Inhibitors: **0-0**

Lane/player state shown:
- BRO Casting Kled `0/0/0`, 37 CS vs KT Perfect Olaf `0/0/0`, 37 CS
- BRO GIDEON Jarvan IV `0/0/0`, 40 CS vs KT Cuzz Nocturne `0/0/0`, 38 CS
- BRO Roamer Anivia `0/0/0`, 42 CS vs KT Bdd Ryze `1/0/1`, 36 CS
- BRO Teddy Lucian `0/1/0`, 39 CS vs KT Jiwoo Miss Fortune `0/0/2`, 38 CS
- BRO Namgung Milio `0/1/0`, 6 CS vs KT Effort Nautilus `1/0/1`, 12 CS

Displayed lane-economy arrows are source-local comparison indicators and should not be over-interpreted independently of total gold/state.

## Latest supplied live market board

User supplied the market screenshot in the same message pair, with sportsbook in-app display around **05:32**:

- Game 1 ML: **KT 1.303 / BRO 3.303**
- Duration 32: **Over 1.806 / Under 1.936**
- Total Kills 27.5: **Over 1.875 / Under 1.863**
- Kill Handicap: **KT -8.5 @1.718 / BRO +8.5 @2.049**

### Synchronization status

`SYNC = UNRESOLVED` for certification purposes.

The scoreboard shows 8:36 while the sportsbook panel displays about 05:32. The screenshots were supplied together, but the user has **not explicitly confirmed this KT-BRO pair represents the same live state**. Do not invalidate solely because of device/status-bar capture timing, but do not count this pair as synchronized for the two-snapshot live ML/KH/TK requirement until same-state provenance is resolved.

## Pregame series baseline captured before Game 1

Cleanly labeled series prices:
- Series ML: **KT 1.291 / BRO 3.502**
- KT -1.5 @ **1.634** / BRO +1.5 @ **2.181**
- BRO -1.5 @ **5.347** / KT +1.5 @ **1.132**
- KT -2.5 @ **2.921** / BRO +2.5 @ **1.374**
- Series total 3.5: **Over 1.444 / Under 2.648**
- Series total 4.5: **Over 3.045 / Under 1.348**
- Exact score KT 3-0 **2.150**, KT 3-1 **2.540**, KT 3-2 **3.010**
- Exact score BRO 3-0 **3.977**, BRO 3-1 **5.277**, BRO 3-2 **4.664**

Pregame prices are context only and do not waive map-family live gates.

## Decision / position state

- **No TAKE has been issued in Game 1.**
- **No open shadow position exists for this series/map at handoff time.**
- The most recent visible verdict after the live screenshots was: `MODEL NOT LOADED — HOLD`, because bootstrap was incomplete when the evidence arrived.
- Do not retroactively certify a TAKE from that state.
- Pregame/immediate-postdraft ML/KH/TK TAKE remains disabled.
- Live ML/KH/TK still require two usable synchronized snapshots.
- Duration retains its own full DOVC/FCR requirements.

## Active KH calibration reminder

- Small **favorite negative** handicap is not rejected merely because the absolute line is small; it may be valid if the locked common signed-margin distribution supports it.
- Small **underdog positive** handicap must pass `DOG_CUSHION_CLASS`; `INSUFFICIENT` is automatic SKIP and `THIN` is presumptive SKIP absent exceptional explicit suppression of one-fight/cleanup tail.
- Exact signed-margin arithmetic and side-neutral KH distribution lock are mandatory before sign selection.

## Draft-reading reminder

For this pro BO5 use `DIM -> PDRL -> PML` and causal ordering:

`LANE STATES -> JUNGLE/SUPPORT ACCESS -> FIRST MOVE -> OBJECTIVE SEQUENCE -> TRANSITION QUALITY -> 2/3-ITEM FIGHT SHAPE -> WCSR -> EXECUTION BURDEN -> SERIES-POOL PRESSURE -> PRO ADVERSARIAL PASS`

For Game 2+, update Fearless depletion only from completed prior games and track remaining functional archetype inventory rather than champion count alone.

## Logging state

Standing map-end batching remains active.

- Do **not** write this live Game 1 snapshot/market frame to Airtable merely for logging mid-map.
- At map end, batch-write meaningful snapshots, any qualified TAKE entry, final state and settlement, then verify exact writes before clearing the buffer.
- The only live persistence performed at handoff time is the canonical **KT and HANJIN BRION roster upsert** in Airtable based on the verified scoreboard starters.

## New-chat bootstrap checklist

1. Fetch default-branch `models/lol/CURRENT_MODEL.md` first.
2. Immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`.
3. Fetch `models/lol/session/CURRENT_SESSION_LOCK.md` and verify `LOL-2026-08-26-E14-KT-BRO-1432-UTC7` is ACTIVE.
4. Re-fetch `CURRENT_MODEL.md` at frozen authority commit `95af8bcde298772e28f963818a71f0653d602a69`.
5. Load the exact retained stack/order required by locked CURRENT_MODEL, including DIM, PDRL, PML, KHMC, small-H asymmetry and all PRE_TAKE extensions.
6. Load this latest applicable handoff **last**.
7. Verify Circuit Breaker `CLEAR`, PML `ACTIVE`, KH directional calibration `ACTIVE`.
8. Resume Game 1 from new user evidence; position-blind reassessment applies.

If the authority hierarchy mismatches, use `MODEL LOCK MISMATCH — HOLD`.
