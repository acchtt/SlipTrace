# Current Live Handoff — KT Rolster Challengers vs DRX/KRX Challengers — 2026-08-31

**State only — not analytical authority**

## Series
- Competition: `LCK CL 2026 Season`
- Stage: `Playoffs — Upper Round 1`
- Match: `KT Rolster Challengers vs DRX Challengers / KRX Challengers`
- Format: `Bo5 Fearless Draft`
- Scheduled: `2026-08-31 12:00 UTC+7 / 14:00 KST`
- Series score: `not supplied / do not infer`
- Current map: `Game 1 expected underway; exact state not supplied`
- Blue/Red: `not supplied`

## Active authority
- Model: `LoL v1.3 — Hierarchy Moneyline + Duration Core`
- Active lock: `LOL-2026-08-31-V13-KTC-KRXC-BENCH-1205-UTC7`
- Frozen authority commit: `ce84ef31eb743e8002603cdd083c871c28787221`
- Team benchmark: `Gol.gg league-relative benchmark ACTIVE`
- Causal thesis gate: `selected-side C>0; price cannot create the bet`
- Circuit breaker: `CLEAR`
- Active markets: `Moneyline + Duration Over/Under`
- KH/TK: `RETIRED_FROM_BETTING`
- Actual exposure: `0u`
- Shadow stake: `0.25u`
- Minimum odds: `1.60`
- ML edge threshold: `+5.0pp`
- Duration edge threshold: `+7.5pp`
- Accepted v1.3 ML samples entering series: `ML_SAMPLE_N=3`
- Duration samples: `0`

## Frozen team benchmark
Primary current window: `LCK CL 2026 Rounds 3-4`.  
Previous comparable window: `LCK CL 2026 Rounds 1-2`.

Participant current split scores:
- `B_current(KRX)=+1.666`
- `B_current(KT)=-0.206`

Previous scores:
- `B_previous(KRX)=-0.127`
- `B_previous(KT)=+0.765`

Roster adjustment:
- KT current expected five matches the R1-2 core five -> `70/30` current/previous.
- KRX current expected five has one material bot change `Jiwoo -> Vincenzo` -> `85/15` current/previous.

Participant raw blends:
- `B_raw(KRX)=+1.397`
- `B_raw(KT)=+0.085`

Nominal peer re-standardization:
- `B(KRX)=+1.623`
- `B(KT)=+0.069`
- `GAP(KRX-KT)=+1.554 SD`

Tier robustness check: varying every nonparticipant peer among allowed 70/30, 85/15, or current-only roster adjustments keeps the KRX-KT gap around `+1.430 to +1.653 SD`, always above the +1.25 major-edge threshold.

Frozen prior:
- `KRX/DRX K=+2 / P0=60%`
- `KT K=-2 / P0=40%`

Same-series results and prices do not change K/P0.

## Expected current lineups — live card overrides
KT Rolster Challengers:
- Sero — top
- Sylvie — jungle
- Hwichan — mid
- FenRir — bot
- Pollu — support

DRX/KRX Challengers, latest reliable pre-series Play-In five:
- Frog — top
- Winner — jungle
- AKaJe — mid
- Vincenzo — bot
- Minous — support

An unexpected additional starter change is decision-critical for ML benchmark certification and requires review before TAKE.

## Workflow
1. Receive current Game 1 scoreboard/draft + synchronized market.
2. Resolve exact live lineup and Blue/Red from user evidence.
3. Lock map-specific draft `D` price-blind; no immediate-postdraft TAKE.
4. On synchronized live state, score ML `D_eff/R/X/O/T`, selected-side `C`, probability, then price.
5. If selected-side `C<=0`, PASS regardless of attractive odds.
6. Duration independently scores `V/Q/H/T/F` before line/price.
7. Verdict first and compact.
8. Exact user confirmation required before accepted Position.
9. Defer Airtable writes until map end.
10. Track Fearless consumed champions after each map.

## Bootstrap next continuation
Fetch default `models/lol/CURRENT_MODEL.md`, load `LOL_SESSION_BOOTSTRAP.md`, fetch lock `LOL-2026-08-31-V13-KTC-KRXC-BENCH-1205-UTC7`, re-fetch CURRENT_MODEL at authority `ce84ef31eb743e8002603cdd083c871c28787221`, load exact benchmark-aware v1.3 stack, then this or a newer KT.C-KRX.C handoff last.
