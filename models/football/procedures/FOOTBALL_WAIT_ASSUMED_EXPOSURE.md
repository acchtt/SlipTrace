# Football WAIT exposure — legacy assumed policy retired

The former prospective WAIT_ASSUMED / SHADOW_WAIT_ASSUMED policy is retired.

## Current rule

A model WAIT is a plan only.

Declaring a target does not prove that the target was reached and does not
create model exposure, Website Pick exposure, user exposure or user P/L.

For current work:

- unresolved WAIT -> no exposure;
- target explicitly not reached -> no exposure;
- target reached/terms actually confirmed -> reconcile from those confirmed
  line/odds under the active accounting contract;
- user physical bet -> only a confirmed Actual Bets — Current row affects user
  P/L.

WATCH likewise creates no synthetic assumed bet.

## Historical records

Do not rewrite frozen historical records that were originally stored under the
old assumed-exposure convention. They remain historical artifacts and must be
labeled as such when audited.

No new current Decision State or accounting row may create WAIT_ASSUMED,
SHADOW_WAIT_ASSUMED, WATCH_ASSUMED or SHADOW_WATCH_ASSUMED.
