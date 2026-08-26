# LoL Live Handoff — KT Rolster vs HANJIN BRION — 2026-08-26 16:30 UTC+7

**Status:** `ACTIVE LIVE HANDOFF`  
**Session lock:** `LOL-2026-08-26-E14-KT-BRO-1432-UTC7`  
**Series:** `LCK 2026 Play-In — KT Rolster vs HANJIN BRION — BO5`  
**Current series score:** `KT 1-0 BRO`  
**Current map:** `Game 2 — LIVE`  
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

## Critical user-workflow corrections — ACTIVE NOW

The user explicitly established two workflow rules during Game 2. These are current-session user corrections and therefore control immediately even though the E14 model/rules authority remains frozen at the lock commit.

### 1. Same-message screenshot synchronization

When the user supplies scoreboard + sportsbook screenshots in the **same message**, treat them as synchronized by default.

- Ignore bookmaker/header/feed clock differences as a synchronization objection.
- Do not ask for same-state confirmation merely because the sportsbook clock differs from the scoreboard clock.
- Only break synchronization if there is a substantive incompatible game-state contradiction or the user explicitly identifies a frame as stale/old/expired.
- Scoreboard is the factual game-state source; paired sportsbook image is the price/executability source.

Permanent default-branch procedure updates were committed during this session:

- `LOL_LIVE_SCOREBOARD_READING_PROTOCOL_2026-08-01.md` — commit `ab9fbc1b614d39f49872ebb51ba20062ef856eb7`
- `LOL_CONNECTED_STACK_SYNC_AND_RECORDING_PROCEDURE_2026-08-07.md` — commit `e9a9f39fe4e2c87ead1ee85f28ff4d57a792a4ef`
- `LOL_SHADOW_AUTO_RECORD_ADDENDUM_2026-08-12.md` — commit `af762e4c3acf5125c0dcdd3906f15da29c459f92`

### 2. Airtable only at map end

Do **not** call Airtable during a live map.

During the map, buffer:

- material synchronized snapshots;
- qualified TAKE entries;
- exact line/odds and opposite-side benchmark when visible;
- invalidations/expiry events;
- process incidents/corrections.

At verified map end, batch-write `Maps`, `Snapshots`, any `Positions`, roster/canonical metadata if needed, settlement and review; verify exact rows before clearing the buffer.

A qualified TAKE becomes a model-attributed shadow entry at verdict time but remains `BUFFERED SHADOW POSITION — pending map-end Airtable batch` until map-end persistence.

If a line disappears before the qualified TAKE is delivered, there is no position and no backfill.

## Game 1 final / Fearless depletion

KT won Game 1 at **39:17**, final kills **KT 24-11 BRO**.

Final displayed state:

- Gold: KT +16k
- Towers: KT 10-3 BRO
- Dragons: KT 4-1 BRO
- Barons: KT 2-0 BRO
- Inhibitors: KT 1-0 BRO

No Game 1 shadow position existed. Game 1 map-end Airtable batch was completed and verified before the user's new `Airtable only at map end` instruction.

Completed Game 1 Fearless depletion:

### BRO depleted
- Kled
- Jarvan IV
- Anivia
- Lucian
- Milio

### KT depleted
- Olaf
- Nocturne
- Ryze
- Miss Fortune
- Nautilus

## Game 2 exact draft

### KT Rolster
- Perfect — **Ornn**
- Cuzz — **Naafiri**
- Bdd — **Syndra**
- Jiwoo — **Yunara**
- Effort — **Lulu**

### HANJIN BRION
- Casting — **Rumble**
- GIDEON — **Vi**
- Roamer — **Ahri**
- Teddy — **Kalista**
- Namgung — **Renata Glasc**

These Game 2 champions are current-map inventory only. Do not add them to completed Fearless depletion until Game 2 ends.

## Game 2 synchronized snapshot history

### Snapshot 1 — 4:36

User supplied scoreboard + market board in the same message.

State:

- Kills: KT 0-0 BRO
- Gold: KT +47
- Towers: 0-0
- Dragons: 0-0
- Barons: 0-0
- Inhibitors: 0-0

Markets:

- ML: KT 1.390 / BRO 2.850
- Duration 32: Over 1.704 / Under 2.069
- Total Kills 27.5: Over 2.033 / Under 1.729
- Total Kills 26.5: Over 1.890 / Under 1.847
- KH: KT -6.5 @1.819 / BRO +6.5 @1.921

Verdict: `HOLD/PASS` — first usable synchronized snapshot only; no position.

### Snapshot 2 — 18:37

User supplied scoreboard + sportsbook in the same message and later explicitly confirmed they were synchronized. Ignore the sportsbook header clock.

State:

- Kills: KT 6-1 BRO
- Gold: KT +2.4k
- Towers: KT 2-1 BRO
- Dragons: KT 0-3 BRO
- Barons: 0-0
- Inhibitors: 0-0

Markets shown:

- ML: KT 1.257 / BRO 3.641
- Duration 32: Over 1.420 / Under 2.730 — visually greyed/locked
- Total Kills 24.5: Over 1.900 / Under 1.838 — visually greyed/locked
- KH: KT -11.5 @1.755 / BRO +11.5 @1.998

Two-snapshot gate was satisfied by 4:36 -> 18:37.

## Process incident / missed line

The assistant initially issued a false `STATE/PRICE SYNC CONFLICT` HOLD because the sportsbook header showed a different clock from the scoreboard. The user then corrected that the screenshots are always synchronized.

On immediate reassessment, **BRO +11.5 kills @1.998** passed the KH read:

- current signed margin KT +5;
- BRO +11.5 loses only if KT finishes +12 or more;
- KT therefore required +7 additional future net kills from the 18:37 state;
- BRO had only a ~2.4k gold deficit and 1-tower deficit while holding 3-0 dragons;
- BRO retained executable Rumble/Vi/Ahri/Kalista/Renata return-kill/pick channels;
- dog cushion was substantial rather than thin.

However, the line was **no longer available by the time the TAKE was delivered** because of the unnecessary sync delay.

Correct record state:

- `NO POSITION`
- `NO BACKFILL`
- shadow P/L impact: `0u`
- process classification: `FALSE SYNC-CONFLICT / VERDICT LATENCY MISS`

This incident must be included in the Game 2 map-end Airtable batch/review, but Airtable must not be called before Game 2 ends.

## Current position state

- No open/buffered Game 2 shadow position exists at handoff time.
- BRO +11.5 @1.998 was a missed executable line caused by process latency and must not be graded.
- Continue position-blind reassessment from fresh user evidence.

## New-chat continuation

1. Bootstrap exactly from the active E14 session lock and frozen authority commit.
2. Load this handoff last.
3. Apply the user's same-message synchronization rule immediately.
4. Do not call Airtable while Game 2 is live.
5. Resume from the next user-supplied Game 2 evidence.
6. At Game 2 end, batch-write the full buffered map state, any later qualified TAKE(s), final result, settlement and process review, then verify.

If model/rule authority conflicts, the frozen session lock still governs model logic; explicit current-map user corrections govern factual provenance/workflow behavior.