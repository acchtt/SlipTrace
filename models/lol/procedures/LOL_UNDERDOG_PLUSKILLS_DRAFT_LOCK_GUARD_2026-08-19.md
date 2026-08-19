# LoL Underdog +Kills Draft-Lock Guard — 2026-08-19

**Status:** MANDATORY GOVERNANCE / EXECUTION GUARD  
**Applies to:** canonical LoL v0.3.58  
**Purpose:** prevent live-state hindsight, line-buffer anchoring, and incomplete fallback certification from creating false underdog +kills TAKEs.

This procedure strengthens enforcement of the existing fallback-floor rules. It does not create a new analytical model version.

## 1. Core hard rule

An underdog +kills market is **not TAKE-eligible** unless a complete draft-locked certification exists **before the first live state is used to evaluate that market**.

The certification must be based on draft/team inputs only. Live score, gold, objectives, market movement, displayed handicap size, and current net-kill burden cannot be used to create or upgrade the draft fallback classification.

If no complete pre-live certificate exists, the underdog +kills family is locked:

`UNCERTIFIED — HOLD/PASS FOR THIS MAP`

Ordinary live evidence cannot reopen it.

Only a genuine correction to the recorded draft inputs may reopen certification.

## 2. Mandatory certificate — UDKC

Create an internal **UDKC — Underdog +Kills Draft Certificate** for the potential underdog before live +kills evaluation.

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

## 3. Certification timestamp / persistence

The UDKC must be completed:

1. after draft is locked; and
2. before the first live scoreboard state is used for underdog +kills analysis.

The certificate should be persisted in the map's post-draft audit trail or latest live handoff so a new chat can verify it.

A new chat that begins mid-map must locate a complete persisted UDKC. If it cannot, it must treat underdog +kills as `UNCERTIFIED — HOLD/PASS` for that map.

Do not reconstruct a missing certificate from a live scoreboard after the fact.

## 4. KMS proof burden — repeatable-route test

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

## 5. Line-blind order of operations

For underdog +kills the order is mandatory:

1. lock draft;
2. complete UDKC;
3. persist UDKC;
4. observe live snapshots;
5. verify two-snapshot eligibility;
6. reassess whether the pre-certified STABLE fallback is still intact;
7. calculate exact signed margin and NKB;
8. only then price the displayed handicap.

Do not start from the displayed line and reason backward toward certification.

Exact kill-margin arithmetic describes the hurdle. **It is never evidence that the hurdle is unlikely enough to bet.**

## 6. Live evidence can only preserve or downgrade

A pre-live `STABLE` UDKC may remain STABLE or be downgraded by live evidence.

Live evidence may never:

- turn FRAGILE into STABLE;
- turn ABSENT into STABLE;
- turn UNCERTIFIED into STABLE;
- fill a previously missing UDKC field;
- convert a safe-ADC / peel narrative into KMS proof.

If live play reveals the favorite's repeatable routes are stronger than expected, downgrade immediately.

## 7. Role-Leverage Decomposition remains mandatory

RLD must distinguish where live economy sits, but RLD is a **live preservation/downgrade check** after the draft certificate, not a live mechanism for creating a missing certificate.

Carry-centered favorite economy plus cleaner grouped control can invalidate a previously STABLE fallback.

Isolated top/grub resistance cannot create KMS where none was draft-certified.

## 8. Same-series SMR hardening

If an underdog +kills TAKE in the same series is audit-invalidated because UDKC/KMS was missing or false, the next map's underdog +kills candidate requires a brand-new complete UDKC before live.

Do not use "different champions" or "healthier-looking fallback" as shorthand certification.

If the full certificate is not completed, HOLD/PASS.

## 9. New-chat bootstrap assertion

Every new LoL chat must internally assert before any underdog +kills TAKE:

`UDKC FOUND = YES`

and

`UDKC PRE-LIVE = YES`

and

`FF = STABLE`

and

`KMS = PASS`

and

`RLD = PASS`

If any assertion is NO or unknown:

`HOLD/PASS — UNDERDOG +KILLS UNCERTIFIED`

This guard is fail-closed and overrides narrative confidence.

## 10. Reference incident

DNS vs BRO Game 2, 2026-08-19:

A DNS +7.5 kills TAKE was issued at 5:48 after live evidence was used to say KMS/RLD passed, even though no complete pre-live UDKC had been recorded. That violated the existing draft-lock rule. The correct canonical verdict was HOLD/PASS regardless of outcome.

Reference review:
`models/lol/reviews/DNS_BRO_G2_UNDERDOG_PLUSKILLS_DRAFT_LOCK_EXECUTION_REVIEW_2026-08-19.md`
