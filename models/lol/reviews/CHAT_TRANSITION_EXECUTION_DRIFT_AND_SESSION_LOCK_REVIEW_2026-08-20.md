# Chat-Transition Execution Drift & Session-Lock Review — 2026-08-20

**Model under review:** canonical LoL v0.3.58  
**Scope:** shadow-audit sequence spanning DNS-BRO, KRX-NS and LGD-BLG after chat transition  
**Conclusion:** primary failure was execution/governance drift, not sufficient evidence for a new analytical model version.

## 1. Incident summary

The audited chat produced seven visible shadow TAKES:

1. DNS +8.5 kills @2.014 — loss — later invalidated.
2. DNS-BRO G1 Over 33 @1.666 — win — later invalidated.
3. DNS +7.5 kills — loss — later invalidated.
4. KRX +11.5 kills @2.198 — win.
5. KRX +3.5 kills @1.909 — loss — later invalidated.
6. BLG ML @1.820 — loss.
7. LGD ML @1.601 — loss.

The headline result was 2-5, but the more serious finding was that four TAKES were later judged procedurally invalid under the intended canonical framework.

This means the session was not a clean test of v0.3.58 predictive performance.

## 2. Root cause

### A. Large prose stack without deterministic TAKE proof

The active system had many correct hard gates, but a TAKE could still be issued through compact narrative reasoning without a mandatory field-by-field gate signature. This allowed omitted gates to be hidden by confident prose.

### B. New-chat authority reconstruction risk

The bootstrap required CURRENT_MODEL and the load order, but there was no frozen per-slate commit lock. A later chat could therefore load a changed default branch or reconstruct an incomplete active stack.

### C. Missing persistence verification

After KRX +3.5 lost, an underdog-cushion correction was discussed: UDKC STABLE should not itself authorize a thin handicap, and NKB <=4 should be treated as THIN unless strong live anti-cascade proof exists.

A later audit showed that this safeguard had not actually been persisted into the canonical fallback procedure despite being described as fixed. Future chats fetching GitHub therefore could not inherit it.

### D. Outcome-to-patch feedback loop

Losses were followed by immediate rule discussions. Without a frozen slate, this risks changing the effective model while the same audit is still in progress and makes later performance impossible to interpret cleanly.

## 3. Required governance correction

Do not promote v0.3.59 or another analytical version from this incident.

Instead:

- freeze each shadow-audit slate to one authority commit;
- persist the lock in `models/lol/session/CURRENT_SESSION_LOCK.md`;
- require a complete TAKE gate signature for every market family;
- add UCS — Underdog Cushion Sufficiency downstream of UDKC;
- trigger a procedural circuit breaker after the first later-invalidated TAKE or other hard-gate execution failure;
- allow reviews/fixes during a locked slate but keep them pending unless the user explicitly authorizes a relock;
- require write-back verification before claiming a fix is durable.

Mandatory governance procedure:
`models/lol/procedures/LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md`

## 4. UCS correction

For underdog +kills:

- UDKC STABLE is only eligibility to inspect the live handicap;
- compute exact signed margin and exact NKB to ticket failure;
- `NKB <= 4` is THIN;
- THIN cannot TAKE merely because the draft certificate is stable;
- THIN requires observed live anti-cascade proof across meaningful contact cycles plus a surviving independent margin-suppression mechanism;
- any ordinary fight + continuation stress test that can cross the failure threshold forces HOLD;
- UCS unresolved or failed forces HOLD.

This is a governance/execution safeguard inside v0.3.58, not a new model version.

## 5. Valid loss vs execution failure

Future audits must separate:

- **VALID LOSS:** all required gates passed under the locked authority; result does not trigger automatic changes.
- **PROCEDURAL INVALIDATION:** one or more required gates were skipped/misapplied; triggers circuit breaker.

Only the latter automatically stops new TAKE issuance.

## 6. Activation

The user explicitly authorized the fix on 2026-08-20 UTC+7 after asking why the model degraded across chats and how to prevent losses followed by retrospective rule changes.

This authorization permits an immediate new lock epoch after the governance files are updated and verified.
