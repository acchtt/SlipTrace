# Current Live Handoff — 2026-08-25 15:42 UTC+7

**State-only handoff. This file does not override CURRENT_MODEL.md or CURRENT_SESSION_LOCK.md.**

## Active session

- Lock ID: `LOL-2026-08-25-E13-KRXC-BFXY-1542-UTC7`
- Match scope: `LCK Challengers League 2026 — KRX Challengers vs BNK FEARX Youth — Game 1 / remaining series`
- Model: `LoL v0.3.58`
- Frozen authority commit: `67ba101919a5b96b0c237dd8abcb0d6a887a6b1d`
- Circuit breaker: `CLEAR`
- PDRL: `ACTIVE`
- KH directional calibration: `ACTIVE`
- Shadow only: `0.25u` default simulated stake, `0u` actual exposure
- Minimum odds: `1.60`
- PRE_TAKE_CERT interlock: `ACTIVE`
- KHMC / side-neutral margin parent: `ACTIVE`
- Same-map policy: maximum one TAKE per market family; ML / KH / TK / Duration are separate families.
- Airtable live-map policy: map-end batching.

## Series format / state

- Match: KRX Challengers vs BNK FEARX Youth.
- Format: Best-of-5, Hard Fearless for Game 2+ restricted-pool state.
- Current map: Game 1 live.
- Current series score before Game 1 completion: 0-0.

## Exact Game 1 draft

### BNK FEARX Youth
- Top: Kangin — Olaf
- Jungle: Grizzly — Vi
- Mid: MG — Akali
- ADC: Slayer — Ezreal
- Support: Luon — Karma

### KRX Challengers
- Top: Frog — Jax
- Jungle: Winner — Jarvan IV
- Mid: AKaJe — Orianna
- ADC: Vincenzo — Jhin
- Support: Minous — Bard

Game 1 Hard Fearless depletion for future maps is therefore:

- BFX.Y used: Olaf / Vi / Akali / Ezreal / Karma
- KRX.C used: Jax / Jarvan IV / Orianna / Jhin / Bard

## Last user-supplied Game 1 live snapshot before lock

Displayed clock: `35:17`

- Kills: BFX.Y 8 — 11 KRX.C
- Gold: KRX.C +1.9k
- Towers: BFX.Y 2 — 4 KRX.C
- Dragons: BFX.Y 3 — 1 KRX.C
- Barons: 0 — 0
- Inhibitors: 0 — 0

Player rows shown:

BFX.Y:
- Kangin Olaf 2/2/2, 249 CS, Lv16
- Grizzly Vi 0/2/5, 217 CS, Lv15
- MG Akali 4/2/3, 249 CS, Lv15
- Slayer Ezreal 2/4/0, 242 CS, Lv13
- Luon Karma 0/1/3, 52 CS, Lv10

KRX.C:
- Frog Jax 3/2/2, 225 CS, Lv15
- Winner Jarvan IV 0/1/7, 212 CS, Lv15
- AKaJe Orianna 5/2/2, 250 CS, Lv16
- Vincenzo Jhin 3/1/4, 219 CS, Lv14
- Minous Bard 0/2/6, 40 CS, Lv10

No source-specific clock correction is active; use displayed game time unless the user supplies one.

## Draft reconstruction rule

Because the Game 1 draft arrived after live play had progressed, any draft-only certificate must run a strict Draft Isolation Pass before using live state:

- exclude current kills/gold/objectives/structures/odds/handicap/current margin from draft-only DIM/UDKC/PDRL mechanism certification;
- only after draft-only certification may the current live state preserve/downgrade those mechanisms;
- live evidence may not manufacture missing draft proof.

## Game 2+ PDRL / Fearless requirements

Do not grade future maps as isolated full-pool drafts.

For every Game 2+ draft:

1. update exact used-champion depletion from all completed prior games;
2. record current series score;
3. resolve side/selection rights when available;
4. run DIM on exact roles;
5. run PDRL including lane-priority phases, jungle/support coupling, tempo transitions, projected objective sequencing, player-specific professional fit, execution burden, WCSR, series-pool pressure, same-series adaptation and pro adversarial pass;
6. keep DIM_EDGE / PRO_MAP_EDGE / PRO_EXEC_EDGE / SERIES_DRAFT_EDGE / FINAL_PRO_DRAFT_EDGE distinct;
7. immediate-postdraft ML/KH/TK TAKE remains disabled.

## Live execution state

- Live ML/KH/TK require at least two usable synchronized snapshots.
- Contrary CLEAR/STRONG draft ML requires retained LRO where applicable.
- KH must use side-neutral `KH_MARGIN_CERT` first, price both sides from one distribution, run WMS, then select sign and apply the sign-specific downstream validator.
- Total Kills Under requires FRP PASS.
- Duration Over requires full DOVC.
- Duration Under retains FCR.
- Greyed/stale markets are non-executable.
- Position-blind reassessment is mandatory.
- Exact signed kill-margin arithmetic is mandatory.
- Full PRE_TAKE_CERT + contradiction scan + mechanical validator required before TAKE.
- Verdict first; once bootstrap/lock is loaded, no connector/web/GitHub/Airtable calls belong in the critical live-decision path.

## Source handling

- `Barons X-Y` is historical Baron-take count, not proof of an active Baron buff.
- Tower count is not a standalone ML/KH signal.
- `DELAYED DATA / FEED NOT UPDATING` banners alone are not stale signals.
- User source-specific clock corrections control immediately when supplied.

## Next evidence

Preferred next input:

- a current synchronized Game 1 scoreboard + market screenshot if Game 1 is still live; or
- Game 1 final if it has ended, so series score and Game 2 Fearless/PDRL state can be advanced immediately.
