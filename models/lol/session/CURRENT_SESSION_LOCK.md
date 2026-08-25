# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-25-E13-KRXC-BFXY-1542-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-25 15:42 UTC+7`  
**Scope:** `LCK Challengers League 2026 — KRX Challengers vs BNK FEARX Youth — Game 1 / remaining series`  
**Default expiry:** `KRX.C–BFX.Y series completion or explicit relock; hard stop 2026-08-25 21:30 UTC+7`  
**Authority commit:** `67ba101919a5b96b0c237dd8abcb0d6a887a6b1d`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR`  
**PDRL:** `ACTIVE`  
**KH directional calibration:** `ACTIVE`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`  
**Minimum accepted odds:** `1.60`

## Authorization

On 2026-08-25 at approximately 15:42 UTC+7, after the user supplied current KRX.C–BFX.Y Game 1 live/draft evidence, the user explicitly instructed:

**“Lock this series”**

This explicitly authorizes an immediate relock/new slate epoch for KRX Challengers vs BNK FEARX Youth.

E13 supersedes the expired/completed G2–GX E12 scope. It does **not** authorize LoL v0.3.59 or v0.3.60; those remain retired. Canonical analytical model remains **LoL v0.3.58**.

## Frozen authority

All model-certified analysis under E13 uses frozen authority commit:

`67ba101919a5b96b0c237dd8abcb0d6a887a6b1d`

Repository verification before this relock established that default-branch `main` is ahead of that authority commit only through prior session-state files (`models/lol/session/CURRENT_SESSION_LOCK.md` and the G2–GX live handoff). No analytical/procedural file changed after the frozen authority commit. Therefore `67ba101...` remains the correct frozen analytical authority for E13.

Frozen authority includes:

- canonical LoL v0.3.58 retained stack;
- DIM + professional-play Draft Reading Layer (PDRL), applicable to LCK CL as officially sanctioned professional/semi-professional play;
- DOVC, FRP, FCR and Live ML DPS/LRO controls;
- UDKC / KPA-KMS / RLD / UCS / LAC controls;
- PRE_TAKE mechanical validator;
- Kill Handicap Side-Neutral Margin Engine (`KH_MARGIN_CERT` / KHMC);
- PRE_TAKE_CERT Kill Handicap Margin Extension;
- `KH_DIRECTIONAL_CALIBRATION = ACTIVE`.

Mandatory new KH procedures:

- `models/lol/procedures/LOL_KILL_HANDICAP_SIDE_NEUTRAL_MARGIN_ENGINE_2026-08-25.md`
- `models/lol/procedures/LOL_PRE_TAKE_CERT_KH_MARGIN_EXTENSION_2026-08-25.md`

Mandatory pro-draft procedure:

- `models/lol/procedures/LOL_PRO_PLAY_DRAFT_READING_LAYER_2026-08-24.md`

Mandatory mechanical interlock:

- `models/lol/procedures/LOL_PRE_TAKE_CERT_MECHANICAL_VALIDATOR_2026-08-23.md`

## Match / roster state at lock creation

Series: `KRX Challengers vs BNK FEARX Youth`, Best-of-5, Hard Fearless context for Game 2+.

Current Game 1 user-supplied live evidence at lock creation:

- displayed game clock: `35:17`;
- kills: `BFX.Y 8 – 11 KRX.C`;
- gold: `KRX.C +1.9k`;
- towers: `BFX.Y 2 – 4 KRX.C`;
- dragons: `BFX.Y 3 – 1 KRX.C`;
- Barons: `0 – 0`;
- inhibitors: `0 – 0`.

Exact Game 1 draft / roles from user evidence:

**BNK FEARX Youth**
- Top: Kangin — Olaf
- Jungle: Grizzly — Vi
- Mid: MG — Akali
- ADC: Slayer — Ezreal
- Support: Luon — Karma

**KRX Challengers**
- Top: Frog — Jax
- Jungle: Winner — Jarvan IV
- Mid: AKaJe — Orianna
- ADC: Vincenzo — Jhin
- Support: Minous — Bard

This user-supplied current match evidence controls over older generic roster pages. No duplicate external roster lookup is required unless a concrete conflict appears.

## Game 1 draft handling

Because the exact draft was received after Game 1 had already progressed, any draft-only certificate reconstructed from it must use strict Draft Isolation:

- exclude current kills, gold, objectives, structures, current odds, handicap size and current margin from draft-only certification;
- run DIM + PDRL on the exact locked roles/compositions;
- keep `DIM_EDGE`, `PRO_MAP_EDGE`, `PRO_EXEC_EDGE`, `SERIES_DRAFT_EDGE`, and `FINAL_PRO_DRAFT_EDGE` conceptually separate;
- live evidence may preserve or downgrade draft-only underdog +kills proof, never manufacture missing proof.

Pregame/immediate-postdraft ML/KH/TK TAKE remains disabled; Game 1 is already live, so any live candidate must satisfy the normal synchronized-live requirements from this lock.

## Hard Fearless / Game 2+ requirements

For Game 2 and later maps, do not grade drafts as isolated full-pool drafts.

Game 1 depletion is locked as:

**BFX.Y used:** Olaf / Vi / Akali / Ezreal / Karma.  
**KRX.C used:** Jax / Jarvan IV / Orianna / Jhin / Bard.

For Game 2+ PDRL, explicitly account for:

- all prior used champions in Hard Fearless state;
- current series score;
- side/selection rights when available;
- lane priority by phase;
- jungle/support coupling and first roam/objective windows;
- tempo transitions and objective-sequence projection;
- player-specific professional champion fit;
- execution burden;
- WCSR / fallback robustness;
- remaining-series pool pressure;
- same-series adaptation;
- pro adversarial pass.

## Kill Handicap parent enforcement — E13 active

Before **either** +kills or -kills can be selected, resolve the common side-neutral parent certificate:

`2SNAP | KH_MARGIN_CERT | FAVORITE | CURRENT_SIGNED_MARGIN | MAP_WIN_RANGE | TOTAL_KILLS_RANGE | FAIR_CENTRAL_MARGIN | FINAL_MARGIN_BINS | KCV | RFI | STRUCTURE_MODE | WIDE_MARGIN_HAZARD | DIST_LOCKED_BEFORE_LINE | BOTH_SIDES_PRICED/N-A | WMS | SIGN_SELECTED_AFTER_DIST | SELECTED_SIDE_COVER_RANGE | SELECTED_SIDE_LOWER_BOUND | SELECTED_SIDE_BREAK_EVEN | RETAINED_PHASE_BUFFER | EDGE_AFTER_BUFFER`

Hard rules:

1. predict final signed kill margin before choosing handicap sign;
2. use one side-neutral distribution for both executable sides;
3. price both sides from the same distribution when both are available;
4. integrate materially probable serial favorite cascades through WMS;
5. NKB/RNE are arithmetic only, never probability evidence;
6. failure of one sign supplies zero positive evidence for the opposite sign;
7. `SIGN_SELECTED_AFTER_DIST = PASS` is mandatory;
8. selected-side lower-bound cover probability must clear break-even plus retained phase/uncertainty buffer;
9. mechanism evidence that materially changes the distribution expires the certificate and requires a full rebuild;
10. `KH_DIRECTIONAL_CALIBRATION = ACTIVE` is process-neutrality control, not a favorite quota.

Every KH TAKE must persist:

`KHMC[DIST=P;BOTH=P/N-A;WMS=P;SIGN_AFTER_DIST=P;LB=<x>;BE=<y>;BUF=<z>;EDGE=P;DIRCAL=A]`

## Other market-family enforcement

### Live Moneyline

- at least two usable synchronized snapshots;
- Lead Decomposition + `CFC_CURRENT`;
- `DPS` / draft-prior state;
- neutral-fight stress;
- contrary CLEAR/STRONG draft selection requires full LRO path and three usable snapshots.

### Total Kills

- Under requires `FRP = PASS`;
- Over requires demonstrated recurrence/contact-pressure support and exact remaining-kill arithmetic;
- low pace alone is not Under evidence.

### Duration

- Over requires complete DOVC with positive clock-consuming mechanisms and observed failed-conversion/equivalent evidence;
- Under retains FCR and shortest-close-route stress.

## Execution integrity

The visible word `TAKE` is protected.

- shadow stake `0.25u`; actual exposure `0u`;
- minimum accepted odds `1.60`;
- pregame/immediate-postdraft ML/KH/TK TAKEs disabled;
- live ML/KH/TK require at least two usable synchronized snapshots;
- maximum one TAKE per map/market family: ML / Kill Handicap / Total Kills / Duration;
- current synchronized sportsbook state/price controls;
- greyed/stale markets are non-executable;
- exact signed kill-margin arithmetic is mandatory;
- position-blind reassessment is mandatory;
- HOLD/PASS creates no Position;
- complete PRE_TAKE_CERT + contradiction scan + mechanical validator required before TAKE.

Any skipped mandatory field, ignored contradiction, wrong authority/model, sign-first KH analysis, stale certificate, or narrative/price override of a failed gate triggers the procedural circuit breaker.

## Airtable map-end batching

The standing user-approved map-end batching override remains active under E13.

During live maps:

- no Airtable calls merely to log live frames or TAKES;
- retain meaningful synchronized snapshots, market states, TAKE entry evidence and user corrections in-session.

At map end:

- batch-write meaningful snapshots and qualified TAKES;
- record final map state and settlement;
- duplicate-protect and exact-verify the batch;
- clear the in-session buffer only after successful verification.

## Source handling

No source-specific clock correction is currently locked for KRX.C–BFX.Y. Use displayed game time unless the user supplies a correction.

Retain the general source rules:

- `Barons X-Y` means historical Baron takes, not necessarily active Baron buff;
- tower count is not a standalone ML/KH signal;
- `DELAYED DATA / FEED NOT UPDATING` banners alone are not stale signals;
- real chronology/state conflicts fail closed.

## Continuation requirement

While E13 is active, continuation must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch `models/lol/session/CURRENT_SESSION_LOCK.md` and verify lock `LOL-2026-08-25-E13-KRXC-BFXY-1542-UTC7`;
4. re-fetch `CURRENT_MODEL.md` at authority commit `67ba101919a5b96b0c237dd8abcb0d6a887a6b1d`;
5. load the retained stack plus DIM, PDRL, KHMC, PRE_TAKE validator and KH margin extension;
6. load the latest applicable KRX.C–BFX.Y handoff last if one exists;
7. verify `Circuit breaker = CLEAR` and `KH directional calibration = ACTIVE` before model-certified live analysis.

If authority cannot be loaded or hierarchy mismatches, use:

`MODEL LOCK MISMATCH — HOLD`
