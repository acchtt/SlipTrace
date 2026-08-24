# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-24-E10-NAVI-FNC-2310-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-24 23:10 UTC+7`  
**Scope:** `LEC 2026 Summer — Natus Vincere vs Fnatic remaining series, beginning Game 2; NAVI leads 1-0`  
**Default expiry:** `NAVI–FNC series completion or explicit relock; hard stop 2026-08-25 03:30 UTC+7`  
**Authority commit:** `9f42e5a754181bdcf12c0d938d1d98249ac27247`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`  
**Minimum accepted odds:** `1.60`

## Authorization

On 2026-08-24 at 23:10 UTC+7 the user explicitly instructed **“Relock the match, use updated model”** and then requested continuation in a new chat.

This E10 epoch supersedes E9 for the current NAVI–FNC series only. It explicitly authorizes the updated default-branch canonical v0.3.58 authority that includes the professional-play Draft Reading Layer (PDRL). It does not authorize v0.3.59 or v0.3.60; those remain retired.

## Frozen authority

All model-certified analysis for the remainder of NAVI–FNC uses frozen authority commit:

`9f42e5a754181bdcf12c0d938d1d98249ac27247`

Canonical model remains **LoL v0.3.58**, with the 2026-08-24 pro-play-only PDRL in-place amendment active for this professional series.

Mandatory updated pro-draft procedure:

`models/lol/procedures/LOL_PRO_PLAY_DRAFT_READING_LAYER_2026-08-24.md`

PDRL is additive to DIM and does not bypass UDKC, KPA/KMS, RLD, LAC, UCS, DOVC, FRP, FCR, Live ML DPS/LRO, or any other retained hard gate.

## Series state carried into Game 2+

- Series score: `NAVI 1-0 FNC`.
- Game 1 final: `NAVI win 15-11`.
- Source displayed final clock `48:57`; standing user correction for this source is **subtract 50 seconds from displayed game time**, so model ledger final clock is `48:07`.
- Game 1 exact drafts used for Fearless / series-pool context:
  - FNC: `Ambessa / Nocturne / Locke / Ezreal / Seraphine`
  - NAVI: `Rumble / Zaahen / Orianna / Kai'Sa / Shen`
- Game 1 diagnostic: FNC held a material midgame lead but did not close before NAVI's stronger late coordinated 5v5 state took over. Raw tower lead is not a standalone win or kill-handicap signal.
- Scoreboard `Barons X-Y` denotes Baron takes, not necessarily a currently active Baron buff. Active buff must be independently current-state confirmed before it is used as conversion pressure.

For Game 2+ professional draft analysis, PDRL must resolve format/Fearless state, current series score, prior-game champion depletion, lane priority, jungle-support coupling, tempo transitions, objective-sequence projection, player fit, execution burden, WCSR, series-pool pressure, adaptation, and the pro adversarial pass before any CLEAR/STRONG draft label.

## Execution integrity

The visible word `TAKE` is protected. Every candidate must pass the complete applicable PRE_TAKE_CERT mechanical validator with no failed fields, unresolved fields, or contradictions before a TAKE can be emitted.

Core controls:

- shadow stake `0.25u`; actual exposure `0u`;
- minimum accepted odds `1.60`;
- pregame/immediate-postdraft ML/KH/TK TAKEs disabled;
- live ML/KH/TK require at least two usable synchronized live snapshots;
- one TAKE per market family per map: ML / Kill Handicap / Total Kills / Duration;
- current synchronized sportsbook state/price controls;
- greyed or genuinely stale markets are non-executable;
- exact signed kill-margin arithmetic is mandatory for kill handicap;
- position-blind reassessment is mandatory;
- HOLD/PASS creates no Position;
- no price, numerical cushion, prior result, tower lead, or narrative confidence may override a failed mandatory mechanism gate.

Any skipped mandatory field, ignored contradiction, stale certificate, wrong authority/model, or narrative/price override of a failed gate triggers the procedural circuit breaker.

## Market-family enforcement

### Live Moneyline

Resolve all applicable controls including:

`2SNAP | LEAD_DECOMPOSITION | DPS | CFC_CURRENT | NEUTRAL_FIGHT_STRESS | DRP(if applicable) | LRO(if applicable) | PRICE`

For this pro series, the original draft prior is `FINAL_PRO_DRAFT_EDGE` from DIM + PDRL. A TAKE against an original CLEAR/STRONG draft prior requires the full contrary-draft LRO path.

### Underdog +kills

Resolve the complete sequence without compression:

`2SNAP | DIM | PDRL | TAM | CAS | UDKC_STABLE | KPA | KMS | RLD_DRAFT | FALSE_STABLE_INACTIVE | LIVE_PRESERVATION | LIVE_RLD | LAC | UCS | SCNE | SIGNED_MARGIN | EXACT_NKB | PRICE`

Tower parity/lead is not live preservation by itself. Carry-centered favorite economy plus cleaner grouped control cannot coexist with `LIVE_PRESERVATION = PASS` or `LAC = PASS` unless strong observed live suppression of those empowered favorite routes is demonstrated.

### Favorite -kills

Resolve exact signed margin, Required Net Expansion, Forced-Fight Density, role-weighted lead quality, remaining compulsory-fight schedule, safe-concede routes, Structure Substitution, and all retained NKB/RFI/KCV controls before price.

### Duration Over

Requires complete DOVC:

`CONVERSION_CLASS | POSITIVE_CLOCK_MECH_1 | POSITIVE_CLOCK_MECH_2 | FAILED_CONVERSION_OR_EQUIVALENT | OBSERVED_STALL_EVIDENCE_ID | CLOCK_CAUSALITY | STRUCTURE_SUBSTITUTION | SHORTEST_CASCADE_TEST | SURVIVAL_HORIZON | PRICE`

Low kills, low tower count, close gold, quiet elapsed time, or theoretical waveclear are not positive stall evidence by themselves.

### Total Kills / Duration Under

- Total Kills Under requires `FRP = PASS`; passive quiet is insufficient.
- Total Kills Over retains recurrence/contact-pressure requirements.
- Duration Under retains FCR and shortest-close-route stress.

## Live verdict latency handling

Live execution is strictly **verdict-first**:

- do not call Airtable, GitHub, web, or any other connector in the critical path before emitting the live verdict when the required model/lock context is already loaded;
- complete PRE_TAKE_CERT internally from supplied synchronized screenshots and cached frozen authority;
- immediately emit `TAKE`, `HOLD`, or `PASS` with the exact visible line and stake;
- keep the explanation compressed until after the verdict;
- if quoted price/line is already gone or materially moved before the visible verdict reaches the user, classify the candidate **latency-invalidated**;
- latency-invalidated candidates are `Void / Invalidated / 0u`, do not consume the family, and are separated from executable P/L at map-end reconciliation.

## Airtable map-end batching

Standing user-approved execution override remains active for this lock despite default-branch post-verdict logging language:

During a live map:

- make **no Airtable read/write/search/create/update/verification calls merely to log a live frame or TAKE**;
- retain meaningful synchronized snapshots, HOLD/PASS states, TAKE entry clock/line/odds/stake, latency invalidations, and user corrections in-session;
- live verdict speed takes priority over ledger freshness.

At map end:

- batch-write meaningful snapshots and qualified TAKEs;
- record final map state and settlement;
- separate latency-invalidated counterfactuals from executable P/L;
- duplicate-protect and exact-verify the batch;
- clear the in-session map buffer only after successful verification.

If the conversation ends mid-map, preserve buffered evidence in the latest live handoff.

## Source-specific state handling

- For the current live scoreboard source, subtract **50 seconds** from displayed game time when the user has identified that source's clock offset as applicable.
- Visible `DELAYED DATA` and `FEED NOT UPDATING` banners are excluded as decision signals by themselves.
- `Barons X-Y` is a historical Baron-take count; do not infer active Baron buff without independent current-state confirmation.
- A real state conflict, impossible progression, materially mismatched clock/state, or other independent evidence of staleness still fails closed.

## New-chat requirement

While this lock is active, a future chat must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. immediately fetch `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this `models/lol/session/CURRENT_SESSION_LOCK.md`;
4. re-fetch `CURRENT_MODEL.md` at authority commit `9f42e5a754181bdcf12c0d938d1d98249ac27247`;
5. load the complete stack in the exact locked CURRENT_MODEL order from that same commit;
6. explicitly load `models/lol/procedures/LOL_PRO_PLAY_DRAFT_READING_LAYER_2026-08-24.md` and `models/lol/procedures/LOL_PRE_TAKE_CERT_MECHANICAL_VALIDATOR_2026-08-23.md` from the same commit;
7. load the latest applicable live handoff last if one exists;
8. verify authority/model match and `Circuit breaker = CLEAR` before model-certified analysis;
9. retain NAVI 1-0 FNC series state and Game 1 champion depletion for Game 2+ Fearless/PDRL analysis.

If authority cannot be loaded or hierarchy mismatches, use:

`MODEL LOCK MISMATCH — HOLD`
