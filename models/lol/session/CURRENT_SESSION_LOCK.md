# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-25-E11-NAVI-FNC-0004-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-25 00:04 UTC+7`  
**Scope:** `LEC 2026 Summer — Natus Vincere vs Fnatic remaining series / current slate`  
**Default expiry:** `NAVI–FNC series completion or explicit relock; hard stop 2026-08-25 03:30 UTC+7`  
**Authority commit:** `67ba101919a5b96b0c237dd8abcb0d6a887a6b1d`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR`  
**KH directional calibration:** `ACTIVE`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`  
**Minimum accepted odds:** `1.60`

## Authorization

On 2026-08-25 at approximately 00:04 UTC+7, after a Kill Handicap directional-bias review, the user explicitly instructed:

**“Lock this slate. And adjust the model with your recommendations.”**

This explicitly authorizes a new authority epoch for the current slate and immediate activation of the 2026-08-25 Kill Handicap side-neutral margin-engine amendment.

This E11 epoch supersedes E10 for the current NAVI–FNC slate. It does **not** authorize LoL v0.3.59 or v0.3.60; those remain retired. Canonical analytical model remains **LoL v0.3.58**.

## Frozen authority

All model-certified analysis under this epoch uses frozen authority commit:

`67ba101919a5b96b0c237dd8abcb0d6a887a6b1d`

The frozen authority includes:

- professional-play Draft Reading Layer (PDRL);
- DIM / UDKC / KPA-KMS / RLD / UCS / LAC controls;
- DOVC, FRP, FCR and Live ML DPS/LRO controls;
- PRE_TAKE mechanical validator;
- **Kill Handicap Side-Neutral Margin Engine (`KH_MARGIN_CERT`)**;
- **PRE_TAKE_CERT Kill Handicap Margin Extension**;
- `KH_DIRECTIONAL_CALIBRATION = ACTIVE`.

Mandatory new KH procedures:

- `models/lol/procedures/LOL_KILL_HANDICAP_SIDE_NEUTRAL_MARGIN_ENGINE_2026-08-25.md`
- `models/lol/procedures/LOL_PRE_TAKE_CERT_KH_MARGIN_EXTENSION_2026-08-25.md`

Reference review:

`models/lol/reviews/KILL_HANDICAP_DIRECTIONAL_BIAS_AND_MARGIN_ENGINE_REVIEW_2026-08-25.md`

## Live / series state carry-forward rule

This relock changes analytical authority, not historical or live state.

The last E10 authority-carried series state was:

- NAVI led the series `1-0` entering Game 2;
- Game 1 final: NAVI 15-11 FNC;
- source displayed Game 1 final clock 48:57 with standing source correction of **subtract 50 seconds**, producing model ledger clock 48:07;
- Game 1 Fearless-used champions:
  - FNC: `Ambessa / Nocturne / Locke / Ezreal / Seraphine`
  - NAVI: `Rumble / Zaahen / Orianna / Kai'Sa / Shen`.

Do **not** assume that 1-0 is still the current series score if a later Game 2 result exists. Before the next live/map verdict, use the latest applicable live handoff, user evidence and canonical Airtable map/snapshot/position state to restore the current series/map state. Authority lock changes never overwrite game state.

For Game 2+ professional draft analysis, PDRL must retain format/Fearless state, prior-game champion depletion, lane priority, jungle-support coupling, tempo transitions, objective-sequence projection, player fit, execution burden, WCSR, series-pool pressure, adaptation and the pro adversarial pass before CLEAR/STRONG draft labels.

## Execution integrity

The visible word `TAKE` is protected.

Every candidate must pass the complete applicable PRE_TAKE_CERT mechanical validator with no failed fields, unresolved fields or contradictions before TAKE may be emitted.

Core controls:

- shadow stake `0.25u`; actual exposure `0u`;
- minimum accepted odds `1.60`;
- pregame/immediate-postdraft ML/KH/TK TAKEs disabled;
- live ML/KH/TK require at least two usable synchronized live snapshots;
- maximum one TAKE per map/market family: ML / Kill Handicap / Total Kills / Duration;
- current synchronized sportsbook state/price controls;
- greyed or genuinely stale markets are non-executable;
- exact signed kill-margin arithmetic is mandatory;
- position-blind reassessment is mandatory;
- HOLD/PASS creates no Position;
- no price, cushion, prior result, tower lead or narrative confidence may override a failed mandatory gate.

Any skipped mandatory field, ignored contradiction, stale certificate, wrong authority/model or narrative/price override of a failed gate triggers the procedural circuit breaker.

## Kill Handicap parent enforcement — new E11 rule

Before **either** +kills or -kills can be selected, resolve the common parent certificate:

`2SNAP | KH_MARGIN_CERT | FAVORITE | CURRENT_SIGNED_MARGIN | MAP_WIN_RANGE | TOTAL_KILLS_RANGE | FAIR_CENTRAL_MARGIN | FINAL_MARGIN_BINS | KCV | RFI | STRUCTURE_MODE | WIDE_MARGIN_HAZARD | DIST_LOCKED_BEFORE_LINE | BOTH_SIDES_PRICED/N-A | WMS | SIGN_SELECTED_AFTER_DIST | SELECTED_SIDE_COVER_RANGE | SELECTED_SIDE_LOWER_BOUND | SELECTED_SIDE_BREAK_EVEN | RETAINED_PHASE_BUFFER | EDGE_AFTER_BUFFER`

Hard rules:

1. predict final signed kill margin **before** choosing handicap sign;
2. use one side-neutral distribution for both sides;
3. price both executable sides from that same distribution when available;
4. represent a materially probable serial favorite cascade through WMS inside the distribution;
5. NKB/RNE are arithmetic only, not probability evidence;
6. `FAVORITE -H FAIL` gives zero positive evidence for `UNDERDOG +H`, and vice versa;
7. `SIGN_SELECTED_AFTER_DIST = PASS` is mandatory;
8. selected-side lower-bound cover probability must clear break-even plus the retained phase/uncertainty buffer;
9. if side-specific mechanism analysis materially changes the distribution, discard the certificate, rebuild it from zero and re-price both sides;
10. `KH_DIRECTIONAL_CALIBRATION = ACTIVE` does not force favorites; it forbids sign-first / cushion-first reasoning.

### Underdog +kills downstream validator

Only after the common KH parent certificate identifies the dog side as the preliminary qualifying side may the positive-handicap stack run:

`DIM | PDRL/N-A | TAM | CAS | UDKC_STABLE | KPA | KMS | RLD_DRAFT | FALSE_STABLE_INACTIVE | LIVE_PRESERVATION | LIVE_RLD | LAC | LAC_PRESSURE_CLASS | UCS | SCNE | SIGNED_MARGIN | FAILURE_THRESHOLD | EXACT_NKB | DOG_TAIL_RECONCILED | PRICE`

`LAC_PRESSURE_CLASS` must distinguish:

- `EXPANSION_OPPORTUNITY_SUPPRESSED` — positive evidence;
- `NO_EXPANSION_OPPORTUNITY` — neutral;
- `EXPANSION_OPPORTUNITY_CONVERTED` — negative;
- `UNRESOLVED` — fail closed.

A flat margin with no representative favorite expansion opportunity is not anti-cascade proof.

### Favorite -kills downstream validator

Only after the common KH parent certificate identifies favorite -kills as the preliminary qualifying side may the negative-handicap stack run:

`SIGNED_MARGIN | COVER_THRESHOLD | RNE | FFD | KCV | RFI | ROLE_WEIGHTED_LEAD_QUALITY | REMAINING_FORCED_FIGHTS | STRUCTURE_SUBSTITUTION | SAFE_CONCEDE_TEST | CONTINUATION_CLEANUP_ACCESS | retained NKB/RFI/KCV | FAV_TAIL_RECONCILED | PRICE`

A blocked dog side does not create a favorite TAKE.

### Mandatory persisted compact parent block

Every KH TAKE must retain:

`KHMC[DIST=P;BOTH=P/N-A;WMS=P;SIGN_AFTER_DIST=P;LB=<x>;BE=<y>;BUF=<z>;EDGE=P;DIRCAL=A]`

Omission is a mechanical execution failure.

## Other market-family enforcement

### Live Moneyline

Resolve all applicable controls including:

`2SNAP | LEAD_DECOMPOSITION | DPS | CFC_CURRENT | NEUTRAL_FIGHT_STRESS | DRP(if applicable) | LRO(if applicable) | PRICE`.

For professional play, the original draft prior is `FINAL_PRO_DRAFT_EDGE` from DIM + PDRL. A TAKE against an original CLEAR/STRONG draft prior requires the full contrary-draft LRO path.

### Duration Over

Requires complete DOVC:

`CONVERSION_CLASS | POSITIVE_CLOCK_MECH_1 | POSITIVE_CLOCK_MECH_2 | FAILED_CONVERSION_OR_EQUIVALENT | OBSERVED_STALL_EVIDENCE_ID | CLOCK_CAUSALITY | STRUCTURE_SUBSTITUTION | SHORTEST_CASCADE_TEST | SURVIVAL_HORIZON | PRICE`.

### Total Kills / Duration Under

- Total Kills Under requires `FRP = PASS`; passive quiet is insufficient.
- Total Kills Over retains recurrence/contact-pressure requirements.
- Duration Under retains FCR and shortest-close-route stress.

## Live verdict latency handling

Live execution remains strictly verdict-first:

- when the required model/lock context is already loaded, do not call Airtable, GitHub, web or another connector in the critical path before emitting the live verdict;
- complete PRE_TAKE_CERT internally from supplied synchronized evidence and cached frozen authority;
- immediately emit TAKE, HOLD or PASS with exact visible line/stake;
- if quoted price/line is gone or materially moved before the verdict reaches the user, classify the candidate latency-invalidated;
- latency-invalidated candidates are Void / Invalidated / 0u and do not consume the family.

## Airtable map-end batching

The standing user-approved map-end batching override remains active under E11.

During a live map:

- make no Airtable calls merely to log a live frame or TAKE;
- retain meaningful synchronized snapshots, HOLD/PASS states, TAKE entry clock/line/odds/stake, latency invalidations and user corrections in-session.

At map end:

- batch-write meaningful snapshots and qualified TAKES;
- record final map state and settlement;
- separate latency-invalidated counterfactuals from executable P/L;
- duplicate-protect and exact-verify the batch;
- clear the in-session map buffer only after successful verification.

If the conversation ends mid-map, preserve buffered evidence in the latest live handoff.

## Source-specific state handling

- For the current live scoreboard source, subtract **50 seconds** from displayed game time when the standing source correction applies.
- Visible `DELAYED DATA` / `FEED NOT UPDATING` banners are not decision signals by themselves.
- `Barons X-Y` is historical Baron-take count, not proof of an active Baron buff.
- Real state conflicts, impossible progression, materially mismatched clock/state or other independent staleness evidence fail closed.

## New-chat requirement

While E11 is active, a future chat must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. immediately fetch `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this `models/lol/session/CURRENT_SESSION_LOCK.md`;
4. re-fetch `CURRENT_MODEL.md` at authority commit `67ba101919a5b96b0c237dd8abcb0d6a887a6b1d`;
5. load the complete stack in the exact locked CURRENT_MODEL order from that same commit;
6. explicitly load `models/lol/procedures/LOL_PRO_PLAY_DRAFT_READING_LAYER_2026-08-24.md` for pro draft analysis;
7. explicitly load `models/lol/procedures/LOL_KILL_HANDICAP_SIDE_NEUTRAL_MARGIN_ENGINE_2026-08-25.md`;
8. explicitly load `models/lol/procedures/LOL_PRE_TAKE_CERT_MECHANICAL_VALIDATOR_2026-08-23.md` and `models/lol/procedures/LOL_PRE_TAKE_CERT_KH_MARGIN_EXTENSION_2026-08-25.md`;
9. load the latest applicable live handoff last if one exists;
10. restore the current series/map state from the latest handoff/Airtable/user evidence rather than assuming the E10 pre-Game-2 score is still current;
11. verify authority/model match, `Circuit breaker = CLEAR`, and `KH directional calibration = ACTIVE` before model-certified analysis.

If authority cannot be loaded or hierarchy mismatches, use:

`MODEL LOCK MISMATCH — HOLD`
