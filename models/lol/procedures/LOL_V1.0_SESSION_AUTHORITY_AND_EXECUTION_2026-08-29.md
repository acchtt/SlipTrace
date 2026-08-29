# LoL v1.0 Session Authority & Execution Governance — 2026-08-29

**Status:** CANDIDATE UNTIL `CURRENT_MODEL.md` ACTIVATION  
**Model:** LoL v1.0 — Moneyline Core

## Purpose

Provide the minimum governance needed to keep v1.0 simple, reproducible and historically honest without importing the v0.3.58 market-family gate architecture.

---

# 1. Frozen authority

Each live v1.0 validation epoch must use one active Session Authority Lock recorded in:

`models/lol/session/CURRENT_SESSION_LOCK.md`

The lock records at minimum:

- Lock ID;
- status;
- effective UTC+7 time;
- scope;
- authority commit;
- active model;
- market scope;
- circuit-breaker state;
- actual exposure policy;
- shadow stake;
- minimum odds;
- required edge;
- validation sample state.

When an ACTIVE lock exists, analytical/procedural files are loaded from its frozen authority commit. Mutable state ledgers such as the lock itself and Airtable may be newer.

If the lock cannot be matched to the active model/authority:

`MODEL LOCK MISMATCH — HOLD`

Never silently fall back to a different default-branch analytical stack.

---

# 2. No silent mutation

Within a frozen v1.0 validation epoch:

- an ordinary win/loss does not alter the analytical core;
- a missed bet does not alter the edge threshold;
- new default-branch analysis changes are not live merely because they were committed;
- material analytical changes require explicit user authorization and a new authority epoch/sample as defined by the validation protocol.

This preserves a stable 20–30 Position evaluation sample.

---

# 3. Rebuild / incomplete authority state

If a clean rebuild has been authorized but the new `CURRENT_MODEL.md`, required procedures and fresh lock are not yet complete, no TAKE is permitted.

Visible status:

`MODEL REBUILD IN PROGRESS — HOLD`

---

# 4. Compact ML execution certificate

Before the visible words `TAKE CANDIDATE`, resolve the compact v1.0 record:

`ML_CORE[D=...;MC=...;R=...;X=...;O=...;T=...;S=...;P=...;BOOK=...;EDGE=...;SYNC=P;EXEC=P;ODDS=P;POSBLIND=P;EXPOSURE=0u]`

Required checks:

1. `LOCK` — active v1.0 lock matches the loaded authority;
2. `MODEL` — exact active model is `LoL v1.0 — Moneyline Core`;
3. `SYNC` — current state and price are a usable synchronized decision window;
4. `EXEC` — live Moneyline is executable, not stale/greyed;
5. `ODDS` — decimal odds >=1.60;
6. `POSBLIND` — fresh position-blind assessment completed;
7. `P_LOCKED` — model probability completed before price was used as analytical evidence;
8. `EDGE` — model probability minus raw book implied probability >=+5.0pp;
9. `MARKET` — Moneyline only;
10. `EXPOSURE` — actual exposure remains 0u.

This is an execution interlock, not an analytical gate tree.

If one required execution fact is unresolved, verdict cannot be TAKE CANDIDATE.

---

# 5. State-change expiry

A TAKE CANDIDATE belongs to the assessed state/price decision window.

If a material game-state change occurs before user execution confirmation—fight, meaningful kill/resource swing, objective capture, material structure/control change—the candidate expires and must be rebuilt from the new state.

If only the price changes and the underlying game state is still materially unchanged, the locked model probability may be retained and the implied probability/edge recalculated at the new price.

---

# 6. User confirmation creates the Position

A visible TAKE CANDIDATE begins with:

`USER_LINE_CONFIRMATION=PENDING`

### PENDING

- no Position;
- no W/L;
- no P/L.

### CONFIRMED

The user explicitly confirms the exact quoted Moneyline/odds still exist and are executable before a material state change.

Then an accepted shadow Position may be recorded:

- default shadow stake 0.25u;
- actual exposure 0u.

### FAILED

Line does not exist / cannot be executed: no Position.

Never create a retroactive Position merely because the candidate later would have won.

---

# 7. Position and stake controls

- actual exposure remains `0u` unless the user explicitly changes policy;
- default validation shadow stake is fixed `0.25u`;
- no martingale;
- no rescue;
- no chasing;
- no stake escalation after losses or wins;
- no averaging down;
- a prior/open position cannot bias the current probability estimate.

---

# 8. Market scope hard stop

During the v1.0 initial validation epoch:

`ACTIVE BETTING MARKET = MONEYLINE ONLY`

Kill Handicap, Total Kills and Duration are retired from betting.

They may remain visible in screenshots and historical records, but:

- no TAKE CANDIDATE;
- no new Position;
- no derivative-market gate evaluation is required;
- no derivative gate may be imported into ML merely for compatibility.

---

# 9. Airtable truthfulness

GitHub is analytical/governance authority. Airtable remains canonical historical map/snapshot/position ledger.

For v1.0:

- HOLD/PASS can be logged as snapshots where useful;
- unconfirmed TAKE CANDIDATE can be logged as a snapshot but not a Position;
- confirmed Position must carry the exact accepted odds, 0.25u shadow stake, 0u actual exposure, entry clock/state and `ML_CORE[...]` record;
- settlement must preserve the original model probability and entry evidence;
- do not rewrite v0.x records or P/L.

Never claim an Airtable write/settlement occurred unless the connector write succeeded and was verified when verification is required by the current workflow.

---

# 10. Anti-hindsight

Every accepted Position retains two independent concepts:

- prediction result: WIN / LOSS / PUSH / VOID;
- process validity: VALID / INVALID.

A later loss review may classify an error but cannot rewrite a historical TAKE into a fictional PASS.

A normal valid loss does not trigger a governance circuit breaker.

---

# 11. Minimal circuit breaker

Suspend new TAKE CANDIDATE issuance when a material execution/governance failure occurs, including:

- authority/model mismatch;
- actual exposure policy violation;
- a Position was created without user line confirmation;
- a derivative-market Position was created under v1.0;
- model probability was materially back-fit from price rather than independently estimated;
- stale candidate reused after a material state change;
- missing synchronization/executability caused a false accepted entry.

Visible status:

`TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`

Analysis/PASS/HOLD may continue. Resume only after explicit correction under valid authority/new epoch as appropriate.

An ordinary prediction loss is not a circuit-breaker event.

---

# 12. Durable-fix verification

A change may be called canonical/fixed only after:

1. the relevant GitHub file is written;
2. it is fetched back and verified;
3. `CURRENT_MODEL.md` points to it when analytical authority is affected;
4. the active/new Session Authority Lock freezes an authority commit containing it.

Handoffs carry state, not authority.
