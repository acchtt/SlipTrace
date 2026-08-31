# Current Live Handoff — KT Rolster Challengers vs DRX/KRX Challengers — 2026-08-31

**State only — not analytical authority**

## Series
- Competition: `LCK CL 2026 Season`
- Stage: `Playoffs — Upper Round 1`
- Match: `KT Rolster Challengers vs DRX/KRX Challengers`
- Format: `Bo5 Fearless Draft`
- Series score: `not supplied / do not infer`
- Current map: `Game 1 final draft known`

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
- ML minimum odds `1.50` — corrected from the mistakenly recorded `0.5`
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

## Game 1 confirmed lineups/draft
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

Visible postdraft board supplied by user:
- ML: `KT.C 1.571 / KDRX.C 2.332`
- Duration: `Over 31 @1.494 / Under 31 @2.558`
- Total Kills: `Over 30.5 @1.822 / Under 30.5 @1.956`
- Kill Handicap: `KT.C -6.5 @1.944 / KDRX.C +6.5 @1.816`

## Workflow
1. Complete DIM / mechanism read before price use.
2. Build ML/KH/Duration/TK projections or distributions price-blind.
3. Compare exact postdraft board.
4. Verdict first and compact.
5. Exact user confirmation for any TAKE CANDIDATE before map start.
6. No live prediction updates after map start.
7. Airtable only at map end.

## Bootstrap next continuation
Fetch default `models/lol/CURRENT_MODEL.md`, load `LOL_SESSION_BOOTSTRAP.md`, fetch lock `LOL-2026-08-31-V13-KTC-KRXC-DRAFTONLY`, re-fetch CURRENT_MODEL at authority `3e11a3a2b94a710dbc2d9ef16d88c3ac4ea0335c`, load the benchmark-aware v1.3 stack plus `LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md` and finally the lock-scoped `LOL_DRAFT_ONLY_EXECUTION_MODE_2026-08-31.md`, then this or a newer handoff last.
