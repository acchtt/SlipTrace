# CURRENT LIVE HANDOFF — 2026-08-26 18:54 UTC+7

## Session / authority

- Active lock: `LOL-2026-08-26-E14R2-KT-BRO-G5-1853-UTC7`
- Status: ACTIVE
- Scope: LCK 2026 Play-In — KT Rolster vs HANJIN BRION — Game 5 decider only
- Frozen authority commit: `a095385d721ffdcd62e77d6053ab241b5a8b5cdb`
- Model: LoL v0.3.58
- Circuit breaker: CLEAR — USER-AUTHORIZED G5 REBALANCE
- PDRL: ACTIVE
- PML: ACTIVE
- KH directional calibration: ACTIVE
- KH dog probation: ACTIVE — E14R2 REBALANCED
- Minimum accepted odds: 1.60
- Default shadow stake: 0.25u
- Actual exposure policy: 0u

After the frozen CURRENT_MODEL load order, explicitly load:

`models/lol/procedures/LOL_E14R2_G5_KH_ML_STRICTNESS_REBALANCE_2026-08-26.md`

Then load this handoff last.

## Series state

Series is tied `KT 2-2 HANJIN BRION` entering Game 5.

Game 4 final user-authoritative supplied state:

`33:28 | KT 17-8 BRO | KT +6.7k | towers 7-3 | dragons 3-2 | Baron 1-0 | inhibitors 1-0`

No Game 4 shadow position existed. Game 4 P/L = 0u.

Airtable Game 4 batch has been written and reviewed.

## Game 4 calibration review

User observed that E14R1 appeared too strict after a zero-TAKE map. Review conclusion is mixed, not blanket hindsight:

- several passes were correct;
- BRO -3.5 at 18:28 and 21:58 would have lost;
- displayed Total Kills Overs would have lost with 25 final kills;
- BRO ML 1.598 at 11:48 was below floor and ultimately lost;
- possible over-filtered windows were KT +3.5 and KT ML near 18:28/21:58;
- live-read correction: at 9:18 and 11:48 KT held the first dragon (`BRO 0-KT 1`), not BRO. Do not propagate the earlier misread.

Reference:

`models/lol/reviews/E14R1_GAME4_STRICTNESS_REVIEW_2026-08-26.md`

## E14R2 Game 5 rebalance

User explicitly authorized: **“Apply for g5”**.

Game-5-only overlay:

`models/lol/procedures/LOL_E14R2_G5_KH_ML_STRICTNESS_REBALANCE_2026-08-26.md`

Key changes:

1. Screenshot transitions can establish SST evidence: `COUNTER_EXPANSION`, `BOUNDED_EXPANSION`, `SUPPRESSED`, `CONVERTED`, etc.
2. Dog +H no longer requires exactly two video-like matched windows. Evidence package can pass via two matched SSTs or one strong matched SST plus independent ML/state support.
3. THIN/INSUFFICIENT dog +H still auto-passes.
4. MATERIAL dog +H may qualify only with independent ML support, passing evidence package, mechanism match, probability-weighted cycle hazard, and full pricing clearance.
5. Raw one/two-cycle mathematical crossability is no longer an automatic veto. Use `P_CROSS_ONE_CYCLE` and `P_CROSS_TWO_CYCLE`; HIGH hazard remains disqualifying.
6. Dog surcharge: LARGE Route A +3pp, LARGE Route B +4pp, MATERIAL +5pp.
7. ML/KH must explicitly decompose concentrated gold leads. EXTREME concentration can materially downgrade raw lead quality when the opposing team has objective/counter-expansion support.
8. Minimum odds floor remains 1.60.
9. Parent KH sign neutrality remains mandatory. No favorite quota, dog quota, or sign inversion shortcut.

## Fearless depletion entering Game 5

### KT used
- G1: Olaf / Nocturne / Ryze / Miss Fortune / Nautilus
- G2: Ornn / Naafiri / Syndra / Yunara / Lulu
- G3: Yorick / Wukong / Zoe / Sivir / Bard
- G4: Ambessa / Lee Sin / Lissandra / Ashe / Seraphine

### BRO used
- G1: Kled / Jarvan IV / Anivia / Lucian / Milio
- G2: Rumble / Vi / Ahri / Kalista / Renata Glasc
- G3: Jayce / Xin Zhao / LeBlanc / Ezreal / Elise
- G4: Gnar / Pantheon / Locke / Jhin / Camille

Fearless archetype-inventory tracking is mandatory. Twenty champions per team are depleted entering the deciding map.

## Live execution rules

- Same-message user scoreboard + bookmaker screenshot pairs are presumed synchronized unless underlying game state materially contradicts.
- Ignore bookmaker/header/feed clock differences alone for synchronization.
- 2SNAP remains mandatory for live ML/KH/Total Kills before TAKE.
- Duration retains its own DOVC/FCR requirements.
- No Airtable calls merely to log live Game 5 frames or TAKES; buffer during map and batch-write/verify at map end.
- Position-blind reassessment remains mandatory after any TAKE.
- No Game 5 position exists yet.

## Next action

Await Game 5 draft/opening live evidence. Analyze draft with full Fearless depletion, then establish synchronized snapshot #1 and #2 before any eligible ML/KH/TK TAKE.
