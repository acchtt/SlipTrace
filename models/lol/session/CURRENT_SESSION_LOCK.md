# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-26-E14-KT-BRO-1432-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-26 14:32 UTC+7`  
**Scope:** `LCK 2026 Play-In — KT Rolster vs HANJIN BRION — full BO5 series`  
**Scheduled start:** `2026-08-26 15:00 UTC+7` (`17:00 KST`)  
**Default expiry:** `KT–BRO series completion or explicit relock; hard stop 2026-08-26 23:59 UTC+7`  
**Authority commit:** `95af8bcde298772e28f963818a71f0653d602a69`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR`  
**PDRL:** `ACTIVE`  
**PML:** `ACTIVE`  
**KH directional calibration:** `ACTIVE`  
**Small-H asymmetry calibration:** `ACTIVE`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`  
**Minimum accepted odds:** `1.60`

## Authorization

On 2026-08-26 at approximately 14:32 UTC+7, the user explicitly instructed:

**“Lock todays lck match”**

Current external schedule evidence identifies today's LCK match as **KT Rolster vs HANJIN BRION**, LCK 2026 Play-In, BO5, scheduled 17:00 KST / 15:00 UTC+7.

This instruction authorizes a new slate/session authority epoch for the full KT–BRO series.

## Frozen authority

All model-certified analysis under E14 must use analytical/procedural files frozen at:

`95af8bcde298772e28f963818a71f0653d602a69`

This commit is the default-branch authority immediately after the 2026-08-25 afternoon calibration activation and includes:

- canonical LoL v0.3.58 retained stack;
- DIM + PDRL;
- Professional Meta Layer (PML);
- professional meta / handicap asymmetry calibration;
- Fearless archetype-inventory requirement;
- KH side-neutral margin engine (KHMC);
- KH directional calibration;
- small underdog +H cushion asymmetry / `DOG_CUSHION_CLASS`;
- screenshot-sync provenance clarification;
- workload-context clarification;
- DOVC, FRP, FCR, Live ML DPS/LRO controls;
- UDKC / KPA-KMS / RLD / UCS / LAC controls;
- PRE_TAKE mechanical validator;
- PRE_TAKE KH margin extension;
- PRE_TAKE afternoon calibration extension.

LoL v0.3.59 and v0.3.60 remain retired and must not be loaded or blended.

## Match format / Fearless state

Series: `KT Rolster vs HANJIN BRION`, Best-of-5, LCK 2026 Play-In.

Fearless Draft is active for the series. No champion may be played more than once by the same series-wide draft pool under the competition format.

For Game 2+:

- do not grade drafts as isolated full-pool drafts;
- track all prior used champions;
- maintain functional **archetype inventory**, not champion count alone;
- explicitly track reliable engage, disengage/reset, front line, lane-priority access, jungle/support coupling, mid/jungle first move, bot stability/carry protection, waveclear, objective DPS, side pressure, pick threat and backline access;
- include remaining-series pool pressure and same-series adaptation in PDRL/PML.

## Starting-lineup state

No saved match-specific KT–BRO LCK lineup exists in `models/lol/context/lineups/` at lock creation.

Therefore:

- exact Game 1 starters are **UNCONFIRMED at lock creation**;
- do not apply a numeric team-strength prior that assumes specific substitutes/role assignments until a current official lineup, user-confirmed five, or equivalent current match evidence is available;
- a user-supplied official lineup card or exact five-player correction controls over generic roster pages;
- once current starters are confirmed, persist them in the live handoff/state before using player-specific PML fit.

## Professional draft enforcement — E14

Every exact pro draft must run:

`DIM -> PDRL -> PML`

PML must use pro-relevant evidence rather than solo-queue tiering and resolve where available:

- competition-patch pick/ban priority;
- blind safety / punishability;
- credible flex value;
- pair/trio dependency;
- professional functional contribution;
- player recent stage fit;
- pocket-pick uncertainty tax;
- Fearless scarcity value.

Preferred causal draft order:

`LANE STATES -> JUNGLE/SUPPORT ACCESS -> FIRST MOVE -> OBJECTIVE SEQUENCE -> TRANSITION QUALITY -> 2/3-ITEM FIGHT SHAPE -> WCSR -> EXECUTION BURDEN -> SERIES-POOL PRESSURE -> PRO ADVERSARIAL PASS`

High pro presence, “more meta champions”, “more scaling”, “more engage”, “more tanks”, “three winning lanes” or “counterpick” is never standalone proof of a draft edge.

## Kill Handicap parent enforcement — E14

Before either `+kills` or `-kills` can be selected, resolve the common side-neutral margin distribution and lock `KH_MARGIN_CERT` before line/sign selection.

Mandatory parent fields include:

`2SNAP | KH_MARGIN_CERT | FAVORITE | CURRENT_SIGNED_MARGIN | MAP_WIN_RANGE | TOTAL_KILLS_RANGE | FAIR_CENTRAL_MARGIN | FINAL_MARGIN_BINS | KCV | RFI | STRUCTURE_MODE | WIDE_MARGIN_HAZARD | DIST_LOCKED_BEFORE_LINE | BOTH_SIDES_PRICED/N-A | WMS | SIGN_SELECTED_AFTER_DIST | SELECTED_SIDE_COVER_RANGE | SELECTED_SIDE_LOWER_BOUND | SELECTED_SIDE_BREAK_EVEN | RETAINED_PHASE_BUFFER | EDGE_AFTER_BUFFER`

Hard rules:

1. predict the signed final kill-margin distribution before choosing handicap sign;
2. price executable sides from the same distribution;
3. WMS must represent plausible serial-favorite cascades;
4. NKB/RNE are arithmetic only, not probability evidence;
5. failure of one sign is zero positive evidence for the opposite sign;
6. `SIGN_SELECTED_AFTER_DIST = PASS` is mandatory;
7. selected-side lower-bound cover probability must clear break-even plus retained buffer.

### Small underdog +H asymmetry

If the selected side is underdog `+H`, classify:

`DOG_CUSHION_CLASS = INSUFFICIENT / THIN / MATERIAL / LARGE`

- `INSUFFICIENT` => automatic SKIP;
- `THIN` => presumptive SKIP and may pass only with exceptional explicit UCS + LAC + WMS proof that the normal one-fight/cleanup expansion tail is suppressed;
- attractive price cannot rescue a thin cushion;
- `MATERIAL/LARGE` still requires all retained UDKC/UCS/LAC/KHMC gates.

A small favorite `-H` is not rejected merely because its absolute line is small when the locked common distribution and favorite-tail validator support it.

## Other market-family enforcement

### Live Moneyline

- at least two usable synchronized snapshots;
- Lead Decomposition + `CFC_CURRENT`;
- `DPS` / draft-prior state;
- neutral-fight stress;
- contrary CLEAR/STRONG draft selection requires the full LRO path and three usable snapshots.

### Total Kills

- Under requires `FRP = PASS`;
- Over requires retained recurrence/contact-pressure proof and exact remaining-kill arithmetic;
- low pace alone is not Under evidence.

### Duration

- Over requires complete DOVC including two positive clock-consuming mechanisms and observed failed-conversion/equivalent evidence;
- low kills/towers alone are neutral;
- Under retains FCR and shortest-close-route stress.

## Execution integrity

The visible word `TAKE` remains protected.

- shadow stake `0.25u`; actual exposure `0u`;
- minimum accepted odds `1.60`;
- pregame/immediate-postdraft ML/KH/TK TAKEs disabled;
- live ML/KH/TK require at least two usable synchronized snapshots;
- same-map maximum one TAKE per family: ML / Kill Handicap / Total Kills / Duration;
- current synchronized sportsbook state/price controls;
- greyed/stale markets are non-executable;
- exact signed-margin arithmetic is mandatory;
- position-blind reassessment is mandatory;
- HOLD/PASS creates no Position;
- complete PRE_TAKE_CERT + contradiction scan + mechanical validator required before TAKE;
- applicable TAKES must also satisfy the 2026-08-25 afternoon calibration PRE_TAKE extension.

Any skipped mandatory field, wrong authority/model, sign-first KH analysis, stale certificate, missing PML where required, or narrative/price override of a failed gate triggers the procedural circuit breaker.

## Screenshot synchronization

If the user explicitly confirms paired market/scoreboard screenshots represent the same live state, device/status-bar capture-time differences or capture order alone do not invalidate synchronization.

Internal game-state contradictions still fail closed.

This does not waive the two-snapshot requirement for live ML/KH/TK.

## Workload context

Previous-day play, quick turnaround, travel or long-series workload is `PRO_EXEC_CONTEXT` only. It cannot materially move a TAKE unless tied to an observable mechanism such as preparation compression, substitution/roster constraint, repeated late-series degradation, or verified schedule stress.

## Airtable logging / batching

Carry forward the standing user-approved **map-end batching override**.

During live maps:

- no Airtable calls merely to log each live frame or TAKE;
- retain meaningful synchronized snapshots, market states, TAKE entry evidence and user corrections in-session.

At map end:

- batch-write meaningful snapshots and qualified TAKES;
- record final map state and settlement;
- duplicate-protect and exact-verify the batch;
- clear the in-session buffer only after successful verification.

Never claim `logged` / `settled` without successful write and exact verification.

## Continuation requirement

While E14 is ACTIVE, every continuation/new chat must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this `models/lol/session/CURRENT_SESSION_LOCK.md` and verify lock `LOL-2026-08-26-E14-KT-BRO-1432-UTC7`;
4. re-fetch `CURRENT_MODEL.md` at authority commit `95af8bcde298772e28f963818a71f0653d602a69`;
5. load the retained stack at that same authority commit, including DIM, PDRL, PML, KHMC, KH small-H asymmetry and all PRE_TAKE extensions;
6. load the latest applicable KT–BRO live handoff last if one exists;
7. verify `Circuit breaker = CLEAR`, `PML = ACTIVE`, and `KH directional calibration = ACTIVE` before model-certified live analysis.

If authority cannot be loaded or hierarchy mismatches, use:

`MODEL LOCK MISMATCH — HOLD`
