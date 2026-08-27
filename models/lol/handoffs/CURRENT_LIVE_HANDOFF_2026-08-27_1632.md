# CURRENT LIVE HANDOFF — 2026-08-27 16:32 UTC+7

## Session / authority

- Active lock: `LOL-2026-08-27-E15-NS-BFX-1547-UTC7`
- Status: ACTIVE
- Scope: LCK 2026 Play-In — Nongshim RedForce vs BNK FEARX — full BO5
- Frozen authority commit: `7ac5aa001194406da96ad63c5bbabcfc78496940`
- Model: LoL v0.3.58
- Circuit breaker: CLEAR
- Minimum odds: 1.60
- Default shadow stake: 0.25u
- Actual exposure: 0u

Load this handoff last after the frozen CURRENT_MODEL stack.

## Series state

`NS 1-1 BFX` after Game 2.

### Game 1 final

`27:53 | NS 27-8 BFX | towers NS 9-2 | dragons NS 3-1 | Baron NS 1-0 | inhibitors NS 1-0`

No Game 1 shadow position. Game 1 P/L = 0u.

### Game 2 final — user authoritative

`30:55 | BFX 27-12 NS | towers BFX 8-3 | dragons 2-2 | Baron BFX 1-0 | inhibitors BFX 1-0`

Game 2 position:
- `Total Kills OVER 39.5 @2.086`
- Entry: 24:40, shadow 0.25u, actual 0u
- Final total: 39
- Result: LOSS
- P/L: -0.25u

Airtable Game 2 map, six buffered snapshots, and one settled position were batch-written and exact-verified at map end.

## Fearless depletion through Game 2

### NS used Game 1
- Kingen — Camille
- Sponge — Jarvan IV
- Scout — Orianna
- Diable — Jhin
- Lehends — Shen

### NS used Game 2
- Kingen — Ambessa
- Sponge — Nocturne
- Scout — Locke
- Diable — Yunara
- Lehends — Lulu

### BFX used Game 1
- Clear — Jayce
- Raptor — Lee Sin
- VicLa — Galio
- Taeyoon — Caitlyn
- Kellin — Bard

### BFX used Game 2
- Clear — Rumble
- Raptor — Vi
- VicLa — Ahri
- Taeyoon — Ezreal
- Kellin — Karma

All 20 champions above are depleted for Game 3 under Fearless.

## Series-level read into Game 3

Pregame NS slight/moderate BO5 edge remains relevant but is no longer confirmed by current series state. Game 1 strongly favored NS conversion; Game 2 strongly favored BFX early/mid execution through Ahri/Rumble/Vi and ended 27-12.

Treat series prior as `BALANCED / REASSESS FROM GAME 3 DRAFT`, not as an automatic NS favorite lean.

Game 3 draft review should focus on:
- what engage/frontline/carry-protection archetypes remain after both teams have spent two full compositions;
- whether BFX can preserve proactive jungle/mid first-move pressure without Lee/Vi and Galio/Ahri;
- whether NS can rebuild reliable engage after Jarvan/Nocturne and Orianna/Locke are depleted;
- bot-lane functional depth after Jhin/Yunara and Caitlyn/Ezreal are removed.

## Execution controls

- Same-message user scoreboard + bookmaker screenshots presumed synchronized unless game-state contradiction exists.
- Ignore device/header/bookmaker clock differences alone.
- Live ML/KH/TK require two usable synchronized snapshots.
- Duration retains DOVC/FCR requirements.
- Keep visible verdict first and compact for line preservation.
- Buffer Airtable evidence during the map and batch-write/exact-verify at map end per current handoff convention.
- Position-blind reassessment mandatory.
- No Game 3 position exists yet.

## Next action

Await Game 3 draft/opening odds. Reconstruct exact roles, update Fearless archetype inventory, run DIM + PDRL + PML, then establish live snapshot #1/#2 before any ML/KH/TK TAKE.
