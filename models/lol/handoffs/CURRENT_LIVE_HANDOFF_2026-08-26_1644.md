# LoL Live Handoff — KT Rolster vs HANJIN BRION — 2026-08-26 16:44 UTC+7

**Status:** `ACTIVE LIVE HANDOFF`  
**Session lock:** `LOL-2026-08-26-E14-KT-BRO-1432-UTC7`  
**Series:** `LCK 2026 Play-In — KT Rolster vs HANJIN BRION — BO5`  
**Current series score:** `KT 1-1 BRO`  
**Next map:** `Game 3 — pending`  
**Frozen authority commit:** `95af8bcde298772e28f963818a71f0653d602a69`  
**Model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR`  
**PML:** `ACTIVE`  
**KH directional calibration:** `ACTIVE`  
**Shadow stake:** `0.25u`  
**Actual exposure:** `0u`  
**Minimum odds:** `1.60`

## User screenshot synchronization rule — mandatory

User correction is authoritative for this series and future live handling unless explicitly revoked:

- screenshots supplied in the same user message are presumed synchronized;
- ignore bookmaker/header/feed clock differences for synchronization purposes;
- only declare `STATE CONFLICT` when the underlying game state materially contradicts across the supplied frames or the user explicitly identifies a stale frame;
- do not delay a live verdict solely because sportsbook/header time differs from scoreboard game clock.

This rule was added to the default-branch procedures after the Game 2 latency miss.

## Airtable cadence — mandatory

- Do **not** call Airtable during an active map.
- Buffer meaningful snapshots, qualified TAKEs, expiry/process incidents, final state and settlement in-chat.
- At map end, batch-write and then verify the exact `Maps`, `Snapshots`, and `Positions` state before clearing the buffer.
- A qualified live TAKE may be treated as a buffered shadow position for map-end persistence; an unavailable line must never be backfilled.

## Game 1 final

KT won Game 1.

Final supplied state:
- 39:17
- KT 24-11 BRO
- KT +16k gold
- towers KT 10-3 BRO
- dragons KT 4-1 BRO
- Barons KT 2-0 BRO
- inhibitors KT 1-0 BRO

No Game 1 shadow position existed. Airtable map-end batch and review completed.

### Game 1 Fearless depletion

KT completed champions:
- Olaf
- Nocturne
- Ryze
- Miss Fortune
- Nautilus

BRO completed champions:
- Kled
- Jarvan IV
- Anivia
- Lucian
- Milio

## Game 2 draft

KT:
- Perfect — Ornn
- Cuzz — Naafiri
- Bdd — Syndra
- Jiwoo — Yunara
- Effort — Lulu

BRO:
- Casting — Rumble
- GIDEON — Vi
- Roamer — Ahri
- Teddy — Kalista
- Namgung — Renata Glasc

## Game 2 process incident

At synchronized 18:37:
- KT 6-1 BRO
- KT +2.4k gold
- towers KT 2-1 BRO
- dragons BRO 3-0
- KH BRO +11.5 @1.998 was visible and available

The assistant incorrectly treated the sportsbook/header time difference as a sync conflict and delayed certification. After the user corrected the synchronization rule, the line was no longer available.

Correct accounting:
- process/latency miss only;
- no TAKE;
- no backfill;
- no Position row;
- 0u P/L.

## Game 2 later state

At 27:47:
- BRO 7-6 KT
- BRO +4.6k gold
- towers BRO 4-3 KT
- dragons BRO 4-0 KT
- Baron count BRO 1-0 KT, buff expired
- no inhibitor yet

Verdict: HOLD/PASS across active markets. KT +5.5 failed the small-H dog cushion/cascade gate; BRO -5.5 lacked sufficient future margin support; Duration 32 lacked full certification.

## Game 2 final

User confirmed BRO won Game 2.

Final supplied state:
- 30:44
- BRO 12-6 KT
- BRO +10k gold
- towers BRO 7-3 KT
- dragons BRO 5-0 KT
- Barons BRO 1-0 KT
- inhibitors BRO 1-0 KT

No Game 2 shadow position existed. Airtable batch completed with four meaningful snapshots, one completed map row, zero Position rows, and the false sync-conflict latency miss preserved in review.

### Game 2 Fearless depletion

KT completed champions:
- Ornn
- Naafiri
- Syndra
- Yunara
- Lulu

BRO completed champions:
- Rumble
- Vi
- Ahri
- Kalista
- Renata Glasc

## Fearless state entering Game 3

KT depleted after Games 1-2:
`Olaf, Nocturne, Ryze, Miss Fortune, Nautilus, Ornn, Naafiri, Syndra, Yunara, Lulu`

BRO depleted after Games 1-2:
`Kled, Jarvan IV, Anivia, Lucian, Milio, Rumble, Vi, Ahri, Kalista, Renata Glasc`

For Game 3 continue `DIM -> PDRL -> PML` and evaluate remaining functional archetype inventory, not champion count alone.

## Position state entering Game 3

- Open shadow positions: none.
- Game 1 P/L: 0u.
- Game 2 P/L: 0u.
- Actual exposure: 0u.
- Pregame/immediate-postdraft ML/KH/TK TAKE remains disabled.
- Live ML/KH/TK require the retained synchronized-snapshot gates, with same-message user screenshot pairs presumed synchronized under the user correction above.
- Duration retains its own full DOVC/FCR requirements.

## New-chat continuation

Bootstrap exactly from `CURRENT_SESSION_LOCK.md`, using the frozen E14 authority chain, then load this handoff last. Resume at Game 3 with series score KT 1-1 BRO and the completed Fearless depletion above.
