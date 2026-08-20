# LoL Underdog +Kills Draft-Lock Guard — 2026-08-19

**Status:** MANDATORY GOVERNANCE / EXECUTION GUARD  
**Applies to:** canonical LoL v0.3.58  
**Amended:** 2026-08-20 UTC+7  
**Purpose:** prevent live-state hindsight, line-buffer anchoring, and incomplete fallback certification from creating false underdog +kills TAKEs without imposing an unnecessary timestamp lock.

This procedure strengthens enforcement of the existing fallback-floor rules. It does not create a new analytical model version.

## 1. Core hard rule

An underdog +kills market is **not TAKE-eligible** unless a complete draft-locked certification exists before the TAKE decision.

The certification must be based on draft/team inputs only. Live score, gold, objectives, market movement, displayed handicap size, and current net-kill burden cannot be used to create or upgrade the draft fallback classification.

**The certificate does not have to be created before the game clock starts.** If the exact locked draft is first received after live play has begun, including inside a live screenshot or in a new chat that starts mid-map, the analyst may still create the UDKC by running a strict **Draft-Isolation Pass** before using live evidence for the +kills decision.

If the exact draft cannot be established reliably, or the Draft-Isolation Pass is incomplete, the family is locked:

`UNCERTIFIED — HOLD/PASS FOR THIS MAP`

Only a genuine correction to the recorded draft inputs may reopen a failed draft-input certification.

## 2. Mandatory certificate — UDKC

Create an internal **UDKC — Underdog +Kills Draft Certificate** for the potential underdog before any +kills TAKE.

Every field must be resolved:

- underdog team;
- DER;
- FRI;
- SRI;
- FER = PASS / FAIL;
- PDC = PASS / FAIL;
- PST = PASS / FAIL;
- ARI = PASS / FAIL;
- KPA = PASS / FAIL;
- KMS = PASS / FAIL;
- RLD = PASS / FAIL;
- False-Stable Guard = ACTIVE / INACTIVE;
- DCR;
- FF = STABLE / FRAGILE / ABSENT;
- hard Draft-Collapse Veto = ACTIVE / INACTIVE.

`UNRESOLVED`, omitted, implied, or narrative-only fields do not count as certification.

For TAKE eligibility:

- FER/PDC/PST/ARI/KPA/KMS/RLD must all PASS;
- False-Stable Guard must be INACTIVE;
- FF must be STABLE;
- hard Draft-Collapse Veto must be INACTIVE.

Anything else => HOLD/PASS.

## 3. Draft-Isolation Pass / late reconstruction

The purpose of draft lock is to keep the certificate **draft-only**, not to make eligibility depend on when the screenshot arrived.

A UDKC may be created after live play has started only when all of the following are true:

1. the exact ten-champion locked draft and team sides are known from reliable evidence;
2. the analyst explicitly resets to a **position-blind, line-blind draft read**;
3. DER / FRI / SRI / FER / PDC / PST / ARI / KPA / KMS / RLD / False-Stable Guard / DCR / FF / Draft-Collapse Veto are resolved using only draft/team-strength inputs available independently of the current live state;
4. current kills, gold, objectives, structures, current odds, current handicap size, and current margin are excluded from the certificate;
5. the completed certificate is persisted before any underdog +kills TAKE is issued.

If one screenshot contains both the draft and live state, process it in two phases:

**Phase A — Draft Isolation:** certify the draft using champion/team inputs only.  
**Phase B — Live Reassessment:** apply the live state, two-snapshot gate, exact margin arithmetic, RLD preservation/downgrade, and pricing.

A new chat that begins mid-map may reconstruct a missing UDKC from an exact recorded draft. It must not reconstruct the certificate from the scoreboard itself.

If exact draft evidence is unavailable or ambiguous, use `UNCERTIFIED — HOLD/PASS`.

## 4. Persistence

The UDKC should be persisted in the map audit trail or latest live handoff as soon as it is completed so future chats can reuse the draft-only certificate.

A persisted UDKC is preferred because it reduces repeated work and hindsight risk, but **absence of a persisted pre-live certificate is not itself a market veto** when the exact draft can be recovered and a valid Draft-Isolation Pass can be completed.

Do not let a current +kills line or attractive buffer motivate the certificate. Certification must be completed before line-value reasoning.

## 5. KMS proof burden — repeatable-route test

KMS is not a synonym for "can fight back" or "has safe champions."

Before `KMS = PASS`, explicitly enumerate the favorite's independent repeatable margin-expansion routes, including where applicable:

- range/zone control;
- reliable first contact;
- pick threat;
- re-engage/continuation;
- protected carry DPS;
- siege forcing defensive entry;
- side-lane/global overload;
- objective-entry control;
- dive/base-defense kill collection;
- repeated punishment of the same underdog failure cluster.

Then identify a concrete underdog suppression mechanism for those routes.

The following are **supporting tools only** and cannot independently establish KMS:

- safe ADC / long range;
- waveclear;
- peel or utility;
- generic engage/counter-engage;
- scaling;
- theoretical return kills;
- small current kill margin;
- a large displayed +kills buffer;
- 0-0 towers;
- grubs;
- isolated lane gold.

If the analysis cannot explain how the underdog suppresses repeated **net kill-margin expansion**, set `KMS = FAIL`.

## 6. Line-blind order of operations

For underdog +kills the order is mandatory:

1. establish the exact locked draft;
2. complete the draft-only UDKC, using Draft Isolation if already live;
3. persist UDKC;
4. observe/review live snapshots;
5. verify two-snapshot eligibility;
6. reassess whether the certified STABLE fallback is still intact;
7. calculate exact signed margin and NKB;
8. only then price the displayed handicap.

Do not start from the displayed line and reason backward toward certification.

Exact kill-margin arithmetic describes the hurdle. **It is never evidence that the hurdle is unlikely enough to bet.**

## 7. Live evidence can preserve or downgrade, not create draft proof

A draft-certified `STABLE` UDKC may remain STABLE or be downgraded by live evidence.

Live evidence may never:

- turn a draft `FRAGILE` into `STABLE`;
- turn a draft `ABSENT` into `STABLE`;
- fill a missing draft field;
- convert a safe-ADC / peel narrative into KMS proof;
- be used as evidence inside the Draft-Isolation Pass.

If live play reveals the favorite's repeatable routes are stronger than expected, downgrade immediately. Once downgraded for the map, ordinary live evidence cannot re-upgrade it.

## 8. Role-Leverage Decomposition remains mandatory

Draft RLD asks whether the composition has independent suppression routes and where likely grouped leverage sits. Live RLD then checks where the actual economy has concentrated and may preserve or downgrade the certificate.

Carry-centered favorite economy plus cleaner grouped control can invalidate a previously STABLE fallback.

Isolated top/grub resistance cannot create KMS where none was draft-certified.

## 9. Same-series SMR hardening

If an underdog +kills TAKE in the same series is audit-invalidated because UDKC/KMS was missing or false, the next map's underdog +kills candidate requires a brand-new complete UDKC before TAKE.

Do not use "different champions" or "healthier-looking fallback" as shorthand certification.

The UDKC may be completed pre-live or through a valid Draft-Isolation Pass after live starts. If the full certificate is not completed, HOLD/PASS.

## 10. New-chat bootstrap assertion

Every new LoL chat must internally assert before any underdog +kills TAKE:

`UDKC FOUND OR RECONSTRUCTED FROM EXACT DRAFT = YES`

and

`DRAFT-ISOLATED = YES`

and

`FF = STABLE`

and

`KMS = PASS`

and

`RLD = PASS`

If any assertion is NO or unknown:

`HOLD/PASS — UNDERDOG +KILLS UNCERTIFIED`

This guard is fail-closed on **draft quality and mechanism proof**, not on screenshot timing.

## 11. Reference incidents / amendment rationale

DNS vs BRO Game 2, 2026-08-19:

A DNS +7.5 kills TAKE was issued at 5:48 after live evidence was used to say KMS/RLD passed even though the draft-only mechanism proof had not actually been completed. The error was the **quality and completeness of certification**, not the mere fact that the clock had started.

On 2026-08-20 the user clarified that timing should not override accurate draft and game-state reading. The guard was therefore amended so an exact draft received after live start may be certified through Draft Isolation, while live facts remain forbidden as certification evidence.

References:
- `models/lol/reviews/DNS_BRO_G2_UNDERDOG_PLUSKILLS_DRAFT_LOCK_EXECUTION_REVIEW_2026-08-19.md`
- `models/lol/reviews/UDKC_DRAFT_ISOLATION_AMENDMENT_2026-08-20.md`
