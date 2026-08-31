# Current Live Handoff — KT Rolster Challengers vs DRX/KRX Challengers — 2026-08-31

**State only — not analytical authority**

## Series
- Competition: `LCK CL 2026 Season`
- Stage: `Playoffs — Upper Round 1`
- Match: `KT Rolster Challengers vs DRX/KRX Challengers`
- Format: `Bo5 Fearless Draft`
- Series score: `KT.C 1-0 KRX.C`
- Game 1 winner: `KT Challengers`
- Game 1 final: `31:59`, kills `KT 19-6 KRX`, towers `9-3`, dragons `3-1`, Barons `2-0`, inhibitors `1-0`
- Next map: `Game 2 postdraft prep`

## Active authority
- Active lock: `LOL-2026-08-31-V13-KTC-KRXC-DRAFTONLY`
- Authority commit: `3e11a3a2b94a710dbc2d9ef16d88c3ac4ea0335c`
- Execution mode: `POSTDRAFT_ONLY / NO LIVE PREDICTIONS`
- Lock-scoped overlay: `models/lol/procedures/LOL_DRAFT_ONLY_EXECUTION_MODE_2026-08-31.md`
- Team benchmark: `Gol.gg league-relative benchmark ACTIVE`
- Price rule: `price cannot create the bet`
- Actual exposure: `0u`
- Shadow stake: `0.25u`

## Enabled postdraft markets
- Moneyline
- Kill Handicap
- Duration Over/Under
- Total Kills Over/Under

Thresholds:
- ML minimum odds `1.50`
- ML edge `+5.0pp`
- KH minimum odds `1.60`, initial reactivation edge `+7.5pp`
- Duration minimum odds `1.60`, edge `+7.5pp`
- Total Kills minimum odds `1.60`, initial reactivation edge `+7.5pp`

Once a map starts, do not create or update predictions from live state. In-map evidence is settlement/context only.

## Frozen benchmark
- `B(KRX)=+1.623`
- `B(KT)=+0.069`
- `GAP(KRX-KT)=+1.554 SD`
- `KRX/DRX.C K=+2 / P0=60%`
- `KT.C K=-2 / P0=40%`

Same-series results/prices do not update K/P0.

## Game 1 draft
KT.C:
- Sero — Rumble
- Sylvie — Wukong
- Hwichan — Ahri
- FenRir — Xayah
- Pollu — Milio

KRX.C:
- Frog — Olaf
- Winner — Qiyana
- AKaJe — Viktor
- Vincenzo — Lucian
- Minous — Nautilus

Price-blind draft verdict: `SLIGHT KT.C`.

Visible postdraft board:
- ML: `KT.C 1.571 / KDRX.C 2.332`
- Duration: `Over 31 @1.494 / Under 31 @2.558`
- Total Kills: `Over 30.5 @1.822 / Under 30.5 @1.956`
- Kill Handicap: `KT.C -6.5 @1.944 / KDRX.C +6.5 @1.816`

## Game 1 recorded shadow positions — SETTLED

1. `LCKCL-2026-08-31-KTC-KRXC-G1-KH-KRX+6.5`
   - `KRX.C +6.5 kills @1.816`
   - Shadow `0.25u`, actual `0u`
   - Final kill margin: KT +13
   - Result: `LOSS`, P/L `-0.25u`

2. `LCKCL-2026-08-31-KTC-KRXC-G1-DUR-U31`
   - `Under 31 minutes @2.558`
   - Shadow `0.25u`, actual `0u`
   - Final duration: `31:59`
   - Result: `LOSS`, P/L `-0.25u`

3. `LCKCL-2026-08-31-KTC-KRXC-G1-TK-O30.5`
   - `Over 30.5 total kills @1.822`
   - Shadow `0.25u`, actual `0u`
   - Final total kills: `25`
   - Result: `LOSS`, P/L `-0.25u`

Game 1 draft-only shadow P/L: `-0.75u`.

## Game 1 review
Primary audit label: `PROBABILITY/CALIBRATION ERROR`.

Reason:
- KH distribution materially underweighted the KT clean-cascade branch; final margin was 13 kills versus the prior estimate assigning only about 24% to KT winning by 7+.
- Total Kills baseline/draft adjustment overestimated KRX return-kill participation; KRX produced only 6 kills and final total was 25 versus an Over-lean central environment around 35-37.
- Duration Under 31 was a much smaller calibration miss: final 31:59, just 59 seconds beyond the line.
- No price/execution error identified from settlement alone.

Airtable map and all three settled positions were written at map end.

## Fearless consumed after Game 1
Unavailable to either side in Game 2:
`Rumble / Wukong / Ahri / Xayah / Milio / Olaf / Qiyana / Viktor / Lucian / Nautilus`

## Game 2 workflow
1. Receive final Game 2 draft/roles plus exact board.
2. Complete DIM and price-blind market projections/distributions.
3. Compare ML / KH / Duration / Total Kills.
4. Exact user confirmation before any accepted shadow position.
5. No predictive updates after Game 2 starts.
6. Airtable only at map end.

## Bootstrap next continuation
Fetch default `models/lol/CURRENT_MODEL.md`, load `LOL_SESSION_BOOTSTRAP.md`, fetch lock `LOL-2026-08-31-V13-KTC-KRXC-DRAFTONLY`, re-fetch CURRENT_MODEL at authority `3e11a3a2b94a710dbc2d9ef16d88c3ac4ea0335c`, load the benchmark-aware v1.3 stack plus `LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md` and finally the lock-scoped `LOL_DRAFT_ONLY_EXECUTION_MODE_2026-08-31.md`, then this or a newer handoff last.
