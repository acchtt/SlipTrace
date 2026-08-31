# Current Live Handoff — KT Rolster Challengers vs KRX Challengers — 2026-08-31

**State only — not analytical authority**

## Series
- Competition: `LCK CL 2026 Season`
- Stage: `Playoffs — Upper Round 1`
- Match: `KT Rolster Challengers vs KRX Challengers`
- Format: `Bo5 Fearless Draft`
- Series score: `KT.C 2-0 KRX.C`
- Game 1: KT.C win, `31:59`, kills `19-6`
- Game 2: KT.C win, `24:19`, kills `22-9`, towers `10-2`, dragons `3-0`, Barons `1-0`, inhibitors `2-0`
- Next map: `Game 3 postdraft prep`

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

Price-blind draft verdict: `EVEN` — KT had cleaner early objective/engage structure and front line; KRX had stronger side-lane + scaling/ball-delivery ceiling. Neither side got a discrete ML draft edge.

## Game 2 supplied board
- ML: `KT.C 1.410 / KRX.C 2.809`
- Duration: `Over 32 @2.070 / Under 32 @1.732`
- Total Kills: `Over 30.5 @1.807 / Under 30.5 @1.973`
- Kill Handicap: `KT.C -7.5 @1.829 / KRX.C +7.5 @1.928`

## Game 2 postdraft assessment
- ML: `KRX 60% / KT 40%` from frozen benchmark and `D=0`. Both PASS for execution because selected-side positive draft thesis was absent; KT also failed min odds at 1.410.
- KH: price-blind estimate `KRX +7.5 cover ~68%`. At 1.928 this qualified and was accepted.
- Duration: draft-only `V=0,Q=0,H=0,T=+1`, `F≈31.75m`. Both sides PASS at line 32.
- Total Kills: locked Over 30.5 estimate ~61%. At 1.807 edge ~+5.7pp, below +7.5pp => PASS.

## Game 2 accepted shadow position — SETTLED
- `LCKCL-2026-08-31-KTC-KRXC-G2-KH-KRX+7.5`
- Selection: `KRX.C +7.5 kills @1.928`
- Shadow stake: `0.25u`
- Actual exposure: `0u`
- Final kills: `KT 22-9 KRX` (KT margin +13)
- Result: `LOSS`, P/L `-0.25u`

Game 2 shadow P/L: `-0.25u`.
Cumulative draft-only shadow P/L after G2: `-1.00u`.

## Game 2 review
Primary audit label: `PROBABILITY/CALIBRATION ERROR`.

Reason:
- This was the second consecutive KRX positive-kill-handicap projection to materially underweight a KT clean-cascade branch.
- G2 model estimated KRX +7.5 cover around 68%, yet KT again won by 13 kills.
- Final map control was decisive: towers 10-2, dragons 3-0, Baron 1-0, inhibitors 2-0.
- The clean-cascade stress adjustment added after G1 was still insufficient.
- This is a strong calibration warning, but not yet enough by itself to rewrite parameters before the scheduled checkpoint unless a procedural bug is identified.

Airtable map + settled G2 KH position written at map end.

## Fearless consumed after Games 1-2
Unavailable to either side in Game 3:
`Rumble / Wukong / Ahri / Xayah / Milio / Olaf / Qiyana / Viktor / Lucian / Nautilus / K'Sante / Maokai / Tristana / Kalista / Renata / Camille / Pantheon / Orianna / Yunara / Lulu`

## Audit count
Accepted postdraft bets in this temporary mode: `4` total.
- Kill Handicap: `2` settled, `0-2`
- Duration: `1` settled, `0-1`
- Total Kills: `1` settled, `0-1`
- Moneyline: `0`
- Total shadow P/L: `-1.00u`

Audit cadence remains:
- micro-review every settled map;
- checkpoint audit after `10` accepted postdraft bets total;
- formal calibration/model audit after `20-30` accepted bets per market family unless a procedural bug requires immediate repair.

## Game 3 workflow
1. Receive final Game 3 draft/roles + exact board.
2. Complete DIM and price-blind projections/distributions.
3. Compare ML / KH / Duration / Total Kills.
4. Displayed map clock may be ignored for eligibility, but live-state variables remain analytically forbidden.
5. Airtable only at map end.
