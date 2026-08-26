# CURRENT LIVE HANDOFF — 2026-08-26 20:05 UTC+7

## Session / authority

- Last active lock: `LOL-2026-08-26-E14R2-KT-BRO-G5-1853-UTC7`
- Frozen authority commit used for Game 5: `a095385d721ffdcd62e77d6053ab241b5a8b5cdb`
- Model: LoL v0.3.58
- Game-5-only overlay: `models/lol/procedures/LOL_E14R2_G5_KH_ML_STRICTNESS_REBALANCE_2026-08-26.md`
- Actual exposure policy: 0u
- Default shadow stake: 0.25u

## Series final

LCK 2026 Play-In — KT Rolster vs HANJIN BRION

**Final series: KT Rolster 3-2 HANJIN BRION.**

Game 5 final user-authoritative state:

`45:29 | BRO 13-19 KT | towers BRO 8-7 KT | dragons BRO 1-5 KT | Barons BRO 2-0 KT | inhibitors BRO 3-1 KT | winner KT`

## Game 5 position / settlement

One certified shadow position existed:

- Market: Duration
- Selection: **Over 32**
- Odds: **1.887**
- Entry clock: **19:25**
- Entry state: `BRO 1-3 KT | KT +912g | towers 0-0 | dragons KT 2-0 | Barons 0-0`
- Shadow stake: **0.25u**
- Actual exposure: **0u**
- Result: **WIN**
- Final duration: **45:29**
- Shadow P/L: **+0.22175u**

Entry thesis: DOVC/slow-conversion evidence had become live rather than merely theoretical. From 14:05 to 19:25 KT added only one further net kill and ~452g while towers remained 0-0; the Under-32 close route required the game to end within 12:35 from a structurally undeveloped map. KT's lead was also highly concentrated in Zeri rather than broad fast-close pressure.

## Airtable verification

Game 5 map-end batch is exact-verified in `SlipTrace LoL Live Tracker`:

- 1 completed Maps row: `LCK-2026-08-26-KT-BRO-G5`
- 5 Snapshots rows: S01, S02, S03, S04-ENTRY, S05-FINAL
- 1 Position row: `LCK-2026-08-26-KT-BRO-G5-P01`
- Position settlement: Duration Over 32 @1.887, Win, +0.22175u shadow, 0u actual

## Calibration note

Do not backfill passed KH selections from Game 5 merely because final KT kill margin was +6. The E14R2 Game-5-only overlay was prospective and should be reviewed separately before reuse on a future slate. In particular, BRO +7.5 at 14:05 and BRO +9.5 at 19:25 would have covered ex post, but they were not positions and carry no P/L.

## Continuation state

This KT-BRO live series is complete. Any future session should bootstrap from GitHub normally and must not treat the 18:54 Game 5 pre-map handoff as current live state. This file supersedes `models/lol/handoffs/CURRENT_LIVE_HANDOFF_2026-08-26_1854.md` for the concluded series.