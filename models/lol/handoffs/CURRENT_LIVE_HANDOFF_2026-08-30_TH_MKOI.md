# Current Live Handoff — Team Heretics vs Movistar KOI — 2026-08-30

**State only — not analytical authority**

## Series
- Competition: `LEC 2026 Summer`
- Stage: `Week 6 / Regular Season`
- Match: `Team Heretics vs Movistar KOI`
- Format: `Bo3 Fearless Draft`
- Scheduled: `2026-08-30 21:15 UTC+7 / 16:15 CEST`
- Series score: `not supplied / do not infer`
- Current map: `Game 2 completed — Movistar KOI won`
- Blue/Red: `not explicitly supplied; do not infer from scoreboard orientation`

## Active model
- Model: `LoL v1.3 — Hierarchy Moneyline + Duration Core`
- Active lock: `LOL-2026-08-30-V13-TH-MKOI-THESIS-2227-UTC7`
- Frozen authority commit: `369babb212e806ad4ac251f75c8f909009ea8eed`
- Circuit breaker: `CLEAR`
- Active markets: `Moneyline + Duration Over/Under`
- Kill Handicap / Total Kills: `RETIRED_FROM_BETTING`
- Actual exposure: `0u`
- Shadow stake: `0.25u`
- Minimum odds: `1.60`
- ML edge threshold: `+5.0pp`
- Duration edge threshold: `+7.5pp`
- Accepted v1.3 samples after Game 2: `ML_SAMPLE_N=3; DURATION_SAMPLE_N=0`

## Prospectively active execution gate
User instruction after Game 2:

> Do not take a bet just because the price looks good.

Implemented prospectively as:

`C = 1.5*D_eff + 1.5*R + 1.5*X + 1.25*O + 1.0*T`

For the selected ML side:
- require `C>0` before price is used as betting evidence;
- require a coherent, currently reachable draft/live win mechanism;
- strength prior alone cannot satisfy this gate;
- if `C<=0`, `PASS` even when apparent model-vs-book edge exceeds +5pp;
- price validates value only after positive non-price causality exists.

Earlier accepted v1.3 positions remain historical under the rules active at entry and are not retroactively invalidated.

## Series-frozen strength prior
Price-independent and frozen before same-series results:
- Team Heretics: `K=-1 / P0=45%`
- Movistar KOI: `K=+1 / P0=55%`

Same-series results and prices must not change K/P0.

## Confirmed live lineups from Game 2 scoreboard
TH:
- Tracyn — top
- Daglas — jungle
- Serin — mid
- Hype — ADC
- Way — support

MKOI:
- Myrwn — top
- Elyoya — jungle
- Jojopyun — mid
- Supa — ADC
- Alvaro — support

## Game 2 draft
TH:
- Aatrox / Xin Zhao / Syndra / Ezreal / Karma

MKOI:
- Ambessa / Skarner / Viktor / Ashe / Seraphine

Game 2 draft prior used from TH perspective:
- `D=-1` — MKOI draft edge.
- Mechanism initially `INTACT`.

## Game 2 confirmed position and settlement
Decision window at `03:50`:
- kills `0-0`
- towers `0-0`
- dragons `0-0`
- barons `0-0`
- MKOI held about `+322g` overall

Price-blind ML state from TH perspective:
- `K=-1 / P0=45%`
- `D=-1`
- `MC=INTACT`
- `R=-1`
- `X=0`
- `O=0`
- `T=0`
- old-rule model `TH 36.0% / MKOI 64.0%`

Market:
- MKOI `1.289`
- TH `3.396` -> book implied `29.45%`
- TH edge `+6.55pp`

Verdict under the rules then active:
- `TAKE CANDIDATE — TH ML @3.396`
- user explicitly confirmed exact line;
- result `LOSS`; shadow P/L `-0.25u`; actual exposure `0u`.

Under the new prospective causal thesis gate, this exact state would have failed because selected-side TH had `C=-3.0`, so price would not be allowed to create the bet. Do not retroactively change the historical record.

Airtable map-end logging completed:
- Position record: `recxJWOaEYGhaf0N4`
- Map record: `recaTAM7cHvQAZOmC`
- Snapshot record: `receTc67nmlpfuhhW`

## Validation running context
Known v1.3 accepted ML positions through this Game 2:
1. KT ML @4.259 vs DK — WIN `+0.81475u`
2. DK ML @3.114 vs KT — LOSS `-0.25u`
3. TH ML @3.396 vs MKOI — LOSS `-0.25u`

Running known v1.3 ML shadow P/L: `+0.31475u`.

## User workflow preference
- `VERDICT FIRST` on live assessments.
- Keep visible verdict compact.
- No Airtable writes during a map; perform snapshot/position/map logging at map end.
- Exact user confirmation still required before accepted Position.
- Never TAKE from price alone; selected-side causal thesis must already be positive.

## Next workflow
1. If series continues, receive current series score/map and Blue/Red.
2. Resolve Fearless consumed pool from Games 1-2; Game 1 draft/result still need user supply if not already available elsewhere.
3. Lock map-specific `D` price-blind after draft.
4. No immediate-postdraft TAKE.
5. On synchronized live state + executable market, score ML `D_eff/R/X/O/T`, compute selected-side `C`, and reject price-only sides with `C<=0` before looking for value.
6. Duration remains unchanged.
7. Verdict first, compact.
8. Candidate requires exact line confirmation; material state change expires it.
9. Defer Airtable writes to map end.

## Bootstrap next continuation
Fetch default `models/lol/CURRENT_MODEL.md`, load `LOL_SESSION_BOOTSTRAP.md`, fetch lock `LOL-2026-08-30-V13-TH-MKOI-THESIS-2227-UTC7`, re-fetch `CURRENT_MODEL.md` at authority `369babb212e806ad4ac251f75c8f909009ea8eed`, load exact v1.3 authority stack, then this or a newer TH-MKOI handoff last.
