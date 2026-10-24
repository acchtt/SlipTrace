# Football C — Coordinated coherence, context and execution repair

**Date:** 2026-10-25 ICT  
**Repository:** acchtt/SlipTrace  
**Authority:** Football C only  
**Production branch:** main  
**Repair class:** coordinated model-coherence / context / burden / execution repair  
**Outcome fitting:** prohibited  
**Historical action rewrite:** prohibited

## Why this repair was required

The 2026-10-24 18:00–00:00 ICT slate exposed several independent defects that
could make a good selection surface produce poor realized exposure:

1. non-visible custom BOOK targets were previously confused with screenshot
   reachability;
2. the O2.50 certificate could be operationally too low when the tradable
   opening market was already O3.25+;
3. G3 rejection was too cliff-like for some high-signal two-USABLE-route rows,
   while a single-carrier G4 could be comparatively permissive in MEDIUM/MIXED
   tail context;
4. Chelsea–Tottenham exposed overlapping G3 extension policies with different
   robustness standards;
5. rivalry/derby, rest, congestion, travel/recovery and verified fatigue were
   not first-class deterministic context inputs;
6. Football C policy could change inside a sealed slate, so fixtures from one
   board could be executed under materially different engine rules.

The repair addresses all six as one authority problem rather than tuning
thresholds from final scores.

## Implemented repairs

### 1. One canonical G3 intermediate-burden policy

`c_intermediate_burden_profile()` is now the single active authority for both
visible ACT and custom/non-visible BOOK extension. The former independent
BOOK-only extension helper delegates to this same profile.

- O2.75 minimum price: 1.85
- O3.00 minimum price: 1.90
- O3.25 minimum price: 2.00
- O3.50 still requires a funded G4 certificate

FRAGILE G3 has no intermediate extension.

CONDITIONAL G3 may reach O2.75 and may reach O3.00 only with a NEAR_FUNDED
fourth-goal shape.

ROBUST G3 may also reach O3.00 through independent transferable fourth-goal
evidence.

O3.25 is a strict ROBUST-only near-G4 middle state because exactly three goals
is a half-loss. It requires independent transferable fourth-goal evidence,
HIGH current continuation / route reliability / chance quality / burden
completion, at least MEDIUM failure resistance, and the tighter frozen
historical tail/trap controls. O3.25 never implies a full O3.50/G4 certificate.

This removes the Chelsea branch-order conflict.

### 2. Custom BOOK is independent of screenshot visibility

A custom BOOK target is a zero-exposure target instruction. It does not need to
appear in the screenshot ladder and screenshot odds are never transferred to
the unseen target.

The legacy one-step decay-WAIT compatibility path remains limited to 0.25 goals,
but that limit does not govern direct custom BOOK. A 0.50+ market/certificate
disagreement still requires the independent football recheck before a lower
custom target can be published.

### 3. G4 MEDIUM/MIXED carrier promotion tightened

When effective upper-tail transferability is only MEDIUM and the closest
comparable context is MIXED, a single-carrier G4 now additionally requires at
least one independent corroborator:

- HIGH failure resistance; or
- HIGH independent-route quality; or
- two independently STRONG routes with HIGH independent-route quality.

This prevents a HamKam-like single-carrier MEDIUM/MIXED shape from receiving
O3.50 merely because the carrier path is otherwise strong.

### 4. Structured contextual football layer

New production rank rows must now freeze source-backed:

- rivalry / derby context;
- rest-day differential and congestion;
- continental / intercontinental travel and recovery load;
- verified fatigue;
- an evidence-backed net context effect.

The review state is explicitly either CHECKED_NEUTRAL or VERIFIED_MATERIAL.
"Not checked" is distinct from neutral.

The net effect may be EXPANSIVE, SUPPRESSIVE or MIXED only from verified
evidence. A derby, short rest or travel load has no automatic direction.

Verified context can modify continuation and stall risk by at most one grade.
Positive context cannot manufacture a scoring route. Suppressive context can
reduce continuation / increase stall risk without automatically becoming a
route-destruction veto.

The contextual state is emitted in prospective engine output for later audit.

### 5. High-signal G3 challenger review

A bounded second review is mandatory before sealing a high-signal no-G3 row
when all of the following hold:

- mean O2 >= 0.70;
- mean O3 >= 0.55;
- low-draw trap <= 0.15;
- both current scoring routes are USABLE;
- neither current route is STRONG;
- carrier is at least USABLE;
- independent-route quality is not HIGH;
- no material suppression or route-destroying failure.

The review must freeze `g3_challenger_reviewed=true` and a non-empty basis.

This is not an automatic promotion from historical rates. It exists to prevent
Willem-type rows from silently falling through a binary G3 cliff without a
second current-football check.

### 6. Slate policy fingerprint lock

Every new rank receipt freezes:

- `engine_policy_fingerprint`
- `engine_policy_lock=SLATE_PINNED_V1`

The fingerprint hashes only active ranking/XI policy code. Evidence, request and
result persistence commits do not change it.

Rank resume and routine /xi must use the exact same policy fingerprint. If the
policy files changed after the slate was sealed, /xi fails closed with:

`RANK_ENGINE_POLICY_DRIFT`

This prevents a repeat of the 2026-10-24 condition where Mainz and Chelsea were
members of one frozen board but were evaluated under materially different
Football C execution policies.

Legacy receipts without the lock remain readable for historical audit.

## Same-information control replay

The following controls use the frozen prospective football shape only. No final
score is used as a model input.

### HamKam — Rosenborg

Old frozen state:
- G4 funded
- certified O3.50
- transferability MEDIUM
- comparable context MIXED
- failure resistance MEDIUM
- independent-route quality MEDIUM
- single strong self-funded carrier

Repaired state:
- G4 no longer funds because the MEDIUM/MIXED carrier branch lacks independent
  corroboration;
- G3 remains funded;
- protected certificate becomes O2.50;
- the near-G4 shape can retain at most the settlement-aware O3.00 intermediate
  ceiling under the frozen profile.

This is the intended asymmetric-risk repair: retain the strong goal selection,
remove the unjustified fully protected fourth-goal burden.

### Willem II — Cambuur

Frozen signal:
- mean O2 0.7778;
- mean O3 0.6667;
- low-draw trap 0.1111;
- home route USABLE;
- away route USABLE;
- carrier USABLE;
- independent-route quality MEDIUM;
- no material suppression / route destruction.

Repaired rank contract:
- this shape cannot silently finalize as no-G3 WATCH/STOP;
- it must complete the bounded G3 challenger review first;
- the review may confirm the rejection or correct a misgraded current-football
  dimension;
- no automatic retrospective G3 is created.

### Chelsea — Tottenham

The historical frozen row did not contain the new structured context block, so
it remains legacy context for immutable audit and is not retroactively rewritten.

The repaired canonical execution policy still reproduces the old football-only
CONDITIONAL near-G4 O3 target shape when the contextual state is neutral/legacy.

A separate regression control verifies that source-backed SUPPRESSIVE context
with derby + short recovery + verified fatigue reduces continuation, increases
stall risk, blocks the O3 intermediate extension and returns PASS at that
burden.

This proves the context layer can affect the verdict prospectively without
using the Chelsea result to rewrite the historical decision.

### O3.25 middle-state control

A ROBUST G3 with independent transferable near-G4 evidence, HIGH continuation /
reliability / chance / completion, MEDIUM failure resistance and MIXED closest
tail context:

- keeps G4/O3.50 unfunded;
- authorizes O3.25 at 2.00+;
- ACTs O3.25 @2.00;
- BOOKs O3.25 @2.00+ when the current same-line price is below the floor.

This creates the previously missing tradable middle state without letting the
market manufacture a G4 certificate.

## Regression and workflow validation

Validated on main during the repair:

- Football active deterministic engine tests — PASS
- XI Football C deterministic runtime — PASS
- Football C production invariants — PASS
- Football V4 sweep/rank stages — PASS
- Football V4 original-source replay attestation — PASS
- authority-consistency scanner now requires the context contract, canonical
  burden policy, O3.25 middle-state rule, G3 challenger and slate fingerprint
  lock, and forbids the stale conflicting language.

Representative successful runs:
- engine / XI / invariants: run family around commit
  `cc4ce7b5de73870f3e068c62038d20f7733bf3cb`;
- V4 stage contract: run 40121163086 at
  `2b73c00aa3b6aca847fdb151cee32e893149adf7`;
- original-source replay attestation: run 40120725152;
- latest authority/invariant text after O3.25 alignment: PASS through
  `8d687a9cd50bf1d5926b05f1c8782ac817ecd0c4`.

## Guardrails preserved

- Football first; market never creates a certificate.
- Screenshot-only authority for observed odds.
- Custom unseen target has no inferred current price.
- BOOK remains zero exposure until independently confirmed filled.
- No backfill or retrospective prematch action after kickoff.
- Historical decisions and confirmed actual bets remain immutable.
- Tournament incentive remains structured and is combined conservatively with
  the new match-context layer.
- Current context cannot double-count itself into a scoring route.
- O3.50 still requires funded G4.
- Outcome data is audit-only and never enters the replay ranking calculation.

## Production boundary

The repaired contracts govern new sealed rank slates after activation. New
production C rows must satisfy the checked-context and challenger contracts, and
the resulting slate is pinned to one policy fingerprint through /xi.

Historical receipts remain readable under compatibility defaults and are not
silently migrated into the new context contract.
