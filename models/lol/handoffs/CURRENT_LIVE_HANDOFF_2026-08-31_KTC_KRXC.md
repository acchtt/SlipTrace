# Current Live Handoff — KT Rolster Challengers vs KRX Challengers — 2026-08-31

**State only — not analytical authority**

## Series
- Competition: `LCK CL 2026 Season`
- Stage: `Playoffs — Upper Round 1`
- Match: `KT Rolster Challengers vs KRX Challengers`
- Format: `Bo5 Fearless Draft`
- Series score: `KT.C 1-0 KRX.C`
- Game 1: KT.C win, `31:59`, kills `19-6`
- Current map: `Game 2`

## Active authority
- Lock: `LOL-2026-08-31-V13-KTC-KRXC-DRAFTONLY`
- Authority commit: `3e11a3a2b94a710dbc2d9ef16d88c3ac4ea0335c`
- Mode: `POSTDRAFT-ONLY INPUTS / IGNORE DISPLAYED MATCH CLOCK`
- Actual exposure: `0u`
- Shadow stake: `0.25u`
- ML min odds `1.50`, edge `+5.0pp`
- KH / Duration / Total Kills min odds `1.60`, edge `+7.5pp`
- Price cannot create the bet.

## Timing override
User instruction: `ignore match time`.

For this session:
- displayed map clock does not veto a postdraft evaluation or shadow recording;
- if final draft + market board are supplied after the clock has started, treat them as the intended postdraft decision snapshot;
- **never use the in-map kills/gold/objectives/structures/role resources to improve or alter the prediction**;
- all predictions remain benchmark + final draft/mechanisms + market board only.

## Frozen benchmark
- `B(KRX)=+1.623`
- `B(KT)=+0.069`
- `GAP(KRX-KT)=+1.554 SD`
- `KRX K=+2 / P0=60%`
- `KT K=-2 / P0=40%`
- Same-series results/prices do not update K/P0.

## Game 1 settled shadow positions
- KRX +6.5 kills @1.816 — LOSS `-0.25u`
- Under 31 @2.558 — LOSS `-0.25u`
- Over 30.5 kills @1.822 — LOSS `-0.25u`
- G1 shadow P/L `-0.75u`
- Primary review: `PROBABILITY/CALIBRATION ERROR`; KT clean-cascade branch and low-KRX-return-kill branch were underweighted.

## Fearless consumed after Game 1
`Rumble / Wukong / Ahri / Xayah / Milio / Olaf / Qiyana / Viktor / Lucian / Nautilus`

## Game 2 final draft
KT.C:
- Sero — K'Sante
- Sylvie — Maokai
- Hwichan — Tristana
- FenRir — Kalista
- Pollu — Renata

KRX.C:
- Frog — Camille
- Winner — Pantheon
- AKaJe — Orianna
- Vincenzo — Yunara
- Minous — Lulu

Price-blind draft verdict: `EVEN` — KT has cleaner early objective/engage structure and front line; KRX has stronger side-lane + scaling/ball-delivery ceiling. Neither side gets a discrete ML draft edge.

## Game 2 supplied board
- ML: `KT.C 1.410 / KRX.C 2.809`
- Duration: `Over 32 @2.070 / Under 32 @1.732`
- Total Kills: `Over 30.5 @1.807 / Under 30.5 @1.973`
- Kill Handicap: `KT.C -7.5 @1.829 / KRX.C +7.5 @1.928`

Displayed scoreboard time `2:09` is ignored for eligibility. The 0-0/even live state is also ignored analytically.

## Game 2 postdraft assessment
- ML: `KRX 60% / KT 40%` from frozen benchmark and `D=0`. Both PASS for execution because selected-side positive draft thesis is absent; KT also fails min odds at 1.410.
- KH: clean-cascade stress explicitly increased KT blowout branch versus G1 methodology, but KRX still has Lulu/Yunara protection, Camille side-lane and Pantheon/Orianna return-kill routes. Price-blind estimate `KRX +7.5 cover ~68%`. At 1.928 (51.87% break-even), this is a **TAKE CANDIDATE** under the timing override.
- Duration: draft-only `V=0,Q=0,H=0,T=+1`, `F≈31.75m`. At line 32: Over ~48.25%, Under ~51.75%; both PASS.
- Total Kills: retain pre-series `TK0≈34.5` but apply downward draft adjustment for Renata/Lulu peel plus plausible clean objective-control branches; locked Over 30.5 estimate ~61%. At 1.807 (55.34% break-even), edge ~+5.7pp, below +7.5pp => PASS.

## Game 2 execution status
- `KRX.C +7.5 kills @1.928` — TAKE CANDIDATE, exact user confirmation pending.
- Other supplied markets — PASS.
- Airtable only at map end.

## Audit cadence
- Micro-review every settled map.
- Checkpoint audit after 10 accepted postdraft bets total.
- Formal calibration/model audit after 20-30 accepted bets per market family unless a procedural bug requires immediate repair.
