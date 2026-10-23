# 2026-10-23 — ACT execution-strength and distributed-G3 repair

**Authority:** Football C only  
**Trigger:** post-change ACT/BOOK audit plus pre-result Teleoptik control  
**Scope:** execution qualification, distributed G3 protection, Decision States publication boundary

## Findings

1. Direct ACT previously treated a funded certificate as sufficient at a normal
   price even when `certificate_robustness` was FRAGILE or CONDITIONAL.
2. `DISTRIBUTED_G3` could be funded by two merely USABLE routes with broad
   MEDIUM current grades when frozen scoreline history was strong.
3. Low-endpoint/control evidence had no deterministic middle state between
   ordinary caution and the hard `material_suppression` veto.
4. Rank/FOCUS/FOLLOW workload priority was easy to narrate as execution quality.
5. Decision States persistence was documented but not machine-visible in every
   runtime result, allowing recent /xi rows to go missing operationally.

## Repairs and classification

### ACT execution-strength gate
**Classification:** RISK-TIGHTENING QUARANTINE

- FRAGILE: no ACT/BOOK.
- CONDITIONAL: no ACT at full certified burden; direct ACT ceiling is
  certificate minus 0.25 goals and requires endpoint-control pressure NONE.
- ROBUST: normal direct ACT authority at/below certified burden.
- User exceptions use the same gate.

This quarantine is intentionally conservative pending frozen multi-board and
prospective validation. Rank/FOLLOW semantics are unchanged.

### Distributed-G3 hardening
**Classification:** RISK-TIGHTENING QUARANTINE

A C distributed G3 now additionally requires:
- failure resistance at least MEDIUM;
- effective stall no worse than MEDIUM;
- at least one STRONG route or HIGH independent-route quality.

Frozen scoreline history remains corroboration and cannot turn two merely
USABLE all-MEDIUM routes into a protected G3 by itself.

### Endpoint-control pressure
**Classification:** RISK-TIGHTENING QUARANTINE

A market-independent NONE/MODERATE/HIGH control-pressure diagnostic is compiled
from structured frozen football fields. HIGH blocks CONDITIONAL execution and
caps distributed-only robustness. It does not assert that all scoring routes
are destroyed.

### Decision States publication boundary
**Classification:** PROCESS COMPLIANCE FIX

Every /xi runtime result now emits a `decision_state_persistence` manifest.
An ACT/BOOK/PASS is not publishable until the exact emitted row is upserted by
Assessment ID and independently read back from the active Google Sheet.
Write/readback failure must remain ENGINE_EVALUATED_NOT_PUBLISHED.

## Hindsight boundary

The HAGL case motivated diagnosis, but threshold choice is not fitted to its
final score. The Teleoptik/TSC fixture supplied a pre-result negative control:
its frozen G4 certificate was FRAGILE before settlement while the old execution
path still allowed ACT. Historical result artifacts remain immutable.
