# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-25-E12-G2-GX-0037-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-25 00:37 UTC+7`  
**Scope:** `LEC 2026 Summer — GIANTX vs G2 Esports — Game 2 / remaining series`  
**Default expiry:** `G2–GX series completion or explicit relock; hard stop 2026-08-25 04:00 UTC+7`  
**Authority commit:** `67ba101919a5b96b0c237dd8abcb0d6a887a6b1d`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR`  
**PDRL:** `ACTIVE`  
**KH directional calibration:** `ACTIVE`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`  
**Minimum accepted odds:** `1.60`

## Authorization

On 2026-08-25 at approximately 00:37 UTC+7, after NAVI–FNC was closed, the user explicitly instructed:

**“Lock g2 vs gx, prep game 2 under new model changes”**

This explicitly authorizes an immediate relock/new slate epoch for GIANTX vs G2 Esports and carries forward the already-authorized 2026-08-25 Kill Handicap side-neutral margin-engine amendment.

This E12 epoch supersedes E11 for the active slate. It does **not** authorize LoL v0.3.59 or v0.3.60; those remain retired. Canonical analytical model remains **LoL v0.3.58**.

## Frozen authority

All model-certified analysis under E12 uses frozen authority commit:

`67ba101919a5b96b0c237dd8abcb0d6a887a6b1d`

Repository verification before this relock established that the only commit after this authority commit on `main` modified `models/lol/session/CURRENT_SESSION_LOCK.md`; no analytical/procedural file changed. Therefore `67ba101...` remains the correct frozen analytical authority for E12.

Frozen authority includes:

- canonical LoL v0.3.58 retained stack;
- DIM + professional-play Draft Reading Layer (PDRL);
- DOVC, FRP, FCR and Live ML DPS/LRO controls;
- UDKC / KPA-KMS / RLD / UCS / LAC controls;
- PRE_TAKE mechanical validator;
- Kill Handicap Side-Neutral Margin Engine (`KH_MARGIN_CERT` / KHMC);
- PRE_TAKE_CERT Kill Handicap Margin Extension;
- `KH_DIRECTIONAL_CALIBRATION = ACTIVE`.

Mandatory new KH procedures:

- `models/lol/procedures/LOL_KILL_HANDICAP_SIDE_NEUTRAL_MARGIN_ENGINE_2026-08-25.md`
- `models/lol/procedures/LOL_PRE_TAKE_CERT_KH_MARGIN_EXTENSION_2026-08-25.md`

Reference review:

- `models/lol/reviews/KILL_HANDICAP_DIRECTIONAL_BIAS_AND_MARGIN_ENGINE_REVIEW_2026-08-25.md`

## G2–GX Game 2 prep state

At lock creation, the exact completed Game 1 draft / Fearless depletion and final series score were **not yet canonicalized in Airtable or the active handoff**.

Therefore before any Game 2 model-certified draft edge:

1. restore the exact Game 1 winner / series score from user evidence or a verified current result;
2. restore all ten Game 1 used champions and exact role assignments;
3. confirm Game 2 side/selection rights when available;
4. treat Game 2 as a restricted-pool/Fearless draft — never as an isolated full-pool draft;
5. do not infer Game 1 champion depletion from generic team pools or historical drafts.

Provisional saved LEC rosters at lock creation:

**G2 Esports** — BrokenBlade / SkewMond / Caps / Hans Sama / Labrov.  
**GIANTX** — Oscarinin / Isma / Jackies / Flakked / Jun.

These are prep context only. Live lobby/user-confirmed match evidence controls if a substitution or role change appears.

## Professional Game 2 draft requirements

For Game 2, run **DIM + PDRL** before assigning any draft-derived prior.

PDRL must explicitly account for:

- Fearless/restricted-pool state from Game 1;
- side/selection rights;
- lane priority by phase rather than generic counter labels;
- jungle/support coupling and first two roam/objective windows;
- tempo transitions and likely objective sequence;
- player-specific professional champion fit;
- execution burden under pro coordination;
- WCSR / fallback robustness;
- remaining-series pool pressure;
- same-series adaptation from Game 1;
- pro adversarial pass.

Keep `DIM_EDGE`, `PRO_MAP_EDGE`, `PRO_EXEC_EDGE`, `SERIES_DRAFT_EDGE`, and `FINAL_PRO_DRAFT_EDGE` separate.

Pregame/immediate-postdraft ML/KH/TK TAKE remains disabled; the completed draft establishes priors and mechanism certificates only.

## Kill Handicap parent enforcement — E12 active

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

Every KH TAKE must persist the compact parent block:

`KHMC[DIST=P;BOTH=P/N-A;WMS=P;SIGN_AFTER_DIST=P;LB=<x>;BE=<y>;BUF=<z>;EDGE=P;DIRCAL=A]`

### Underdog +kills downstream validator

Only after KHMC selects the dog side preliminarily may the positive stack run:

`DIM | PDRL | TAM | CAS | UDKC_STABLE | KPA | KMS | RLD_DRAFT | FALSE_STABLE_INACTIVE | LIVE_PRESERVATION | LIVE_RLD | LAC | LAC_PRESSURE_CLASS | UCS | SCNE | SIGNED_MARGIN | FAILURE_THRESHOLD | EXACT_NKB | DOG_TAIL_RECONCILED | PRICE`

`LAC_PRESSURE_CLASS` must distinguish `EXPANSION_OPPORTUNITY_SUPPRESSED` from `NO_EXPANSION_OPPORTUNITY`; passive flat-margin time is not positive suppression evidence.

### Favorite -kills downstream validator

Only after KHMC selects favorite -kills preliminarily may the negative stack run:

`SIGNED_MARGIN | COVER_THRESHOLD | RNE | FFD | KCV | RFI | ROLE_WEIGHTED_LEAD_QUALITY | REMAINING_FORCED_FIGHTS | STRUCTURE_SUBSTITUTION | SAFE_CONCEDE_TEST | CONTINUATION_CLEANUP_ACCESS | retained NKB/RFI/KCV | FAV_TAIL_RECONCILED | PRICE`

A blocked dog side does not create a favorite TAKE.

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

The standing user-approved map-end batching override remains active under E12.

During Game 2:

- no Airtable calls merely to log live frames or TAKES;
- retain meaningful synchronized snapshots, market states, TAKE entry evidence and user corrections in-session.

At map end:

- batch-write meaningful snapshots and qualified TAKES;
- record final map state and settlement;
- duplicate-protect and exact-verify the batch;
- clear the in-session buffer only after successful verification.

## Source handling

Do **not** automatically inherit NAVI–FNC-specific scoreboard clock corrections into G2–GX.

For G2–GX, use the displayed clock unless the user supplies a source-specific correction. User correction controls immediately.

Retain the general source rules:

- `Barons X-Y` is historical Baron-take count, not proof of an active Baron buff;
- `DELAYED DATA / FEED NOT UPDATING` banners are not stale signals by themselves;
- tower count is not a standalone ML/KH signal;
- real chronology/state conflicts fail closed.

## New-chat / continuation requirement

While E12 is active, continuation must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch `models/lol/session/CURRENT_SESSION_LOCK.md` and verify lock `LOL-2026-08-25-E12-G2-GX-0037-UTC7`;
4. re-fetch `CURRENT_MODEL.md` at authority commit `67ba101919a5b96b0c237dd8abcb0d6a887a6b1d`;
5. load the retained stack plus PDRL, KHMC, PRE_TAKE validator and KH margin extension;
6. load the latest applicable G2–GX handoff last if one exists;
7. restore Game 1 winner and exact Fearless-used champions before final Game 2 draft certification;
8. verify `Circuit breaker = CLEAR` and `KH directional calibration = ACTIVE` before model-certified live analysis.

If authority cannot be loaded or hierarchy mismatches, use:

`MODEL LOCK MISMATCH — HOLD`
