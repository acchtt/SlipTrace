# CURRENT LIVE HANDOFF — 2026-08-27 16:42 UTC+7

## Session / authority

- Active lock: `LOL-2026-08-27-E15R1-NS-BFX-G3PLUS-1641-UTC7`
- Status: ACTIVE
- Scope: LCK 2026 Play-In — Nongshim RedForce vs BNK FEARX — Games 3–5
- Frozen authority commit: `d63d372503f3c14ee058464ee77d041399de22ca`
- Base model: LoL v0.3.58
- Session overlay: `models/lol/procedures/LOL_E15R1_LIVE_SPEED_AND_OPPORTUNITY_DECAY_OVERLAY_2026-08-27.md`
- Circuit breaker: CLEAR
- Minimum odds: 1.60
- Default shadow stake: 0.25u
- Actual exposure: 0u

Load this handoff last after the frozen CURRENT_MODEL stack and the E15R1 overlay.

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

Airtable Game 2 map, six snapshots, and one settled position were exact-verified at map end.

## Why E15R1 was activated

The Game 2 audit identified an execution-timing failure mode: too many redundant confirmation requirements caused potentially actionable earlier states to be HOLD/PASSed while the eventual TAKE occurred at 24:40 after Baron, where settlement became highly terminal-event-sensitive and effectively boundary-driven. User explicitly authorized a rest-of-series speed/decay recalibration.

Historical Game 1/Game 2 calls remain frozen. Do not hindsight-backfill earlier BFX ML/KH opportunities.

## E15R1 live execution summary

For Games 3–5:

- hard `2SNAP` is replaced by `EVIDENCE_COUNT >= 2` for live ML/KH/TK;
- certified exact-role pro draft mechanism may be evidence #1 when DIM + PDRL + PML pass and causal mechanism/break condition are explicit;
- first meaningful synchronized live snapshot may be evidence #2 when it directly confirms that mechanism;
- no immediate-postdraft TAKE;
- if draft evidence is weak/ambiguous/contradicted, use two live snapshots;
- HOLD expires on next meaningful snapshot/objective/contact cycle or material reprice and must resolve TAKE/PASS;
- preferred entry window is roughly 8–20 minutes;
- 20–24: normal but terminal-event scan required;
- 24–27: +3pp late-entry buffer and explicit one-event settlement test;
- >=27: TK/Duration presumptive PASS unless exceptional/non-terminal; ML/KH +5pp buffer and CLEAR non-fragile mechanism;
- mechanism realization may outweigh isolated objective counters;
- lead concentration is discounted only after checking whether the fed role is the demonstrated conversion engine;
- favorite -H may qualify earlier from forward signed-margin distribution; do not wait for current margin to approach H;
- underdog +H remains side-neutral / anti-cascade governed; no dog default;
- visible verdict first, then 2–4 causal bullets maximum.

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
- Scout — Lissandra
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

Pregame NS BO5 edge is now `BALANCED / REASSESS FROM GAME 3 DRAFT`.

Game 1: NS strongly converted.
Game 2: BFX strongly realized its early/mid pressure mechanism through Vi/Ahri/Rumble and won 27-12.

Do not auto-favor either side from series score or previous map.

Game 3 draft focus:
- remaining reliable engage/front line/carry protection;
- BFX ability to rebuild proactive jungle/mid or jungle/support first move without Lee/Vi and Galio/Ahri;
- NS ability to rebuild reliable engage without Jarvan/Nocturne and Orianna/Lissandra;
- bot functional depth after Jhin/Yunara and Caitlyn/Ezreal;
- archetype scarcity and execution burden under 20-champion depletion per team.

## Standing controls

- Same-message user scoreboard + bookmaker screenshots presumed synchronized unless game-state contradiction exists.
- Ignore header/device/bookmaker clock differences alone.
- Position-blind reassessment mandatory.
- Exact signed kill-margin arithmetic mandatory.
- DOVC/FCR/FRP retained.
- Minimum odds 1.60.
- One TAKE max per market family per map.
- No Airtable mid-map logging; buffer and batch-write/exact-verify at map end.
- No position exists for Game 3 yet.

## Next action

Await Game 3 draft/opening odds. Run exact-role DIM + PDRL + PML. If draft mechanism is certified CLEAR with an explicit break condition, treat it as evidence point 1. On the first meaningful synchronized live confirmation, immediately evaluate TAKE/PASS without waiting for a redundant second live screenshot.
