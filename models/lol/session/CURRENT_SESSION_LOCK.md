# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-24-E9-LEC-SLATE-2207-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-24 22:07 UTC+7`  
**Scope:** `LEC 2026 Summer — 2026-08-24 slate: NAVI vs Fnatic; GIANTX vs G2 Esports`  
**Default expiry:** `completion of the 2026-08-24 LEC slate or explicit relock; hard stop 2026-08-25 06:00 UTC+7`  
**Authority commit:** `1b6135365edee696cfa4a031f723122b8aed35d2`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`  
**Minimum accepted odds:** `1.60`

## Authorization

On 2026-08-24 at 22:07 UTC+7 the user explicitly instructed **“Lock lec.”**

The prior E8 BFXY–HLEC authority epoch expired when BNK FEARX Youth completed the series 3–0. This E9 epoch establishes one frozen authority for the remaining 2026-08-24 LEC slate, beginning with NAVI vs Fnatic and continuing through GIANTX vs G2 Esports unless explicitly relocked.

This instruction authorizes a new session authority epoch only. It does **not** authorize a model-version change or any unapproved analytical mutation. The recent discussion about tower relevance is therefore not silently promoted into canonical rules by this lock; only already-canonical v0.3.58 rules and the execution controls stated here apply.

## Frozen authority

All model-certified analysis for this LEC slate uses frozen authority commit:

`1b6135365edee696cfa4a031f723122b8aed35d2`

Canonical model remains **LoL v0.3.58**. v0.3.59 and v0.3.60 remain retired.

The frozen stack includes the active v0.3.58 rules and procedures in `CURRENT_MODEL.md`, including the mandatory mechanical execution validator:

`models/lol/procedures/LOL_PRE_TAKE_CERT_MECHANICAL_VALIDATOR_2026-08-23.md`

No default-branch analytical edit made after this authority commit affects this slate unless the user explicitly authorizes another relock/new authority epoch.

## Execution integrity

The visible word `TAKE` remains protected. Every candidate must pass the complete applicable PRE_TAKE_CERT mechanical validator with no failed fields, unresolved fields, or contradictions before a TAKE can be emitted.

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
- qualified TAKEs are shadow-only and are logged only at map-end reconciliation under the batching rule below;
- no price, numerical cushion, prior result, or narrative confidence may override a failed mandatory mechanism gate.

Any skipped mandatory field, ignored contradiction, stale certificate, wrong authority/model, or narrative/price override of a failed gate triggers the procedural circuit breaker.

## Market-family enforcement

### Live Moneyline

Resolve all applicable controls including:

`2SNAP | LEAD_DECOMPOSITION | DPS | CFC_CURRENT | NEUTRAL_FIGHT_STRESS | DRP(if applicable) | LRO(if applicable) | PRICE`

Draft remains a prior, not a permanent veto. A TAKE against an original CLEAR/STRONG draft prior requires the full contrary-draft LRO path.

### Underdog +kills

Resolve the complete sequence without compression:

`2SNAP | DIM | TAM | CAS | UDKC_STABLE | KPA | KMS | RLD_DRAFT | FALSE_STABLE_INACTIVE | LIVE_PRESERVATION | LIVE_RLD | LAC | UCS | SCNE | SIGNED_MARGIN | EXACT_NKB | PRICE`

Carry-centered favorite economy plus cleaner grouped control cannot coexist with `LIVE_PRESERVATION = PASS` or `LAC = PASS` unless strong observed live suppression of those empowered favorite routes is demonstrated.

A large +kills cushion, stable current kill margin, tower parity/lead, theoretical scaling/waveclear/peel, or correct NKB arithmetic cannot override failed KMS/RLD/LAC/UCS.

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

Per the user's standing 2026-08-24 instruction for the live scoreboard source, visible **“DELAYED DATA”** and **“FEED NOT UPDATING”** banners are excluded as decision signals by themselves.

This does not waive synchronization integrity. A real state conflict, impossible progression, materially mismatched clock/state, or other independent evidence of staleness still fails closed.

## New-chat requirement

While this lock is active, a future chat must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. fetch `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this lock;
4. re-fetch `CURRENT_MODEL.md` at authority commit `1b6135365edee696cfa4a031f723122b8aed35d2`;
5. load the complete stack in the locked CURRENT_MODEL order from that same commit;
6. additionally load `models/lol/procedures/LOL_PRE_TAKE_CERT_MECHANICAL_VALIDATOR_2026-08-23.md` from the same commit;
7. load the latest applicable live handoff last;
8. verify the authority/model match before model-certified analysis.

If authority cannot be loaded or hierarchy mismatches, use:

`MODEL LOCK MISMATCH — HOLD`
