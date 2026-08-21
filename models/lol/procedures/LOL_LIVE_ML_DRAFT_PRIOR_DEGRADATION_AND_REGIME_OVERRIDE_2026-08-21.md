# LoL Live ML — Draft Prior Degradation & Live Regime Override — 2026-08-21

**Status:** ACTIVE when included in the applicable Session Authority Lock  
**Analytical model:** LoL v0.3.58 in-place amendment  
**Scope:** live Moneyline only  
**Purpose:** prevent a correct pregame/draft prior from becoming a hidden permanent veto after repeated coherent live evidence shows that the prior's actual mechanisms are not functioning.

This procedure does not create a new model version. It refines the retained Live ML Lead Decomposition / CFC framework.

## 1. Core principle — draft is a prior, not a permanent live veto

For Live ML, the exact draft and DIM remain important priors. They do not remain mechanically dominant after the game supplies repeated, mechanism-relevant contrary evidence.

A draft edge may be:

- `DPS = INTACT` — the claimed draft mechanisms are functioning or remain clearly available at current live leverage;
- `DPS = DEGRADED` — some claimed mechanisms are impaired, but a realistic near-term route remains for them to reassert;
- `DPS = BROKEN` — repeated live interactions show that the mechanisms supporting the original draft edge are not functioning at the current role/economy state and the opposing live regime has become the more relevant control description.

`DPS` means **Draft Prior State**. It does not rewrite the original draft grade. The original draft read remains historically recorded; `DPS` describes how much weight that prior should carry now for live ML.

## 2. Neutral-setup stress uses current live leverage

The retained neutral-setup compulsory-fight stress test must use:

- current items / completed components where known;
- current levels;
- current role-weighted economy;
- current objective schedule;
- current wave/structure access;
- current carry and facilitator leverage.

`Neutral setup` means approximately neutral **positioning/entry**, not hypothetical equal gold and not a reset back to the post-draft state.

Do not ask which draft wins at equal economy when evaluating a live ML at 10–20 minutes. Ask which side controls the next approximately neutral setup **with the current live state preserved**.

## 3. Standard Live ML path

If the contemplated ML selection:

- aligns with the original CLEAR/STRONG draft edge; or
- the original draft edge was only SLIGHT/EVEN/UNCLEAR,

then the retained Live ML path applies:

- two usable live snapshots;
- Lead Decomposition;
- `CFC_CURRENT = PASS`;
- current-state neutral-fight stress = PASS;
- retained price / execution / SMR requirements.

For this path, `LRO = N/A` is valid.

## 4. Opposing a CLEAR/STRONG draft edge — mandatory Live Regime Override

A Live ML TAKE **against** an original `CLEAR` or `STRONG` draft edge is forbidden unless `LRO = PASS`.

### 4.1 Additional evidence floor

`LRO = PASS` requires:

1. `3SNAP = PASS` — at least three distinct usable live snapshots;
2. `2CYCLE = PASS` — at least two distinct meaningful contact/objective cycles have occurred since the draft read;
3. the contrary live regime is not the product of one isolated level-1 event, one single fight, or a scoreboard-only lead.

This intentionally keeps the ordinary two-snapshot Live ML rule while adding one extra snapshot only when the analyst is overturning a CLEAR/STRONG draft prior.

### 4.2 Regime Persistence

`REGIME_PERSISTENCE = PASS` requires the contrary side's control to remain coherent across the qualifying snapshots/cycles.

Support includes:

- resource/control lead is stable or expanding rather than instantly mean-reverting;
- the same side repeatedly obtains first move, objective entry, carry access, or safer damage continuation;
- the next objective/contact schedule still benefits the live leader under the current state.

A larger gold number by itself is insufficient.

### 4.3 Multi-Role Leverage

`MULTI_ROLE_LEVERAGE = PASS` requires the live advantage to be strategically distributed rather than isolated in a low-conversion pocket.

Normally this means:

- at least two decision-relevant roles materially support the live regime; and
- at least one of those roles is a primary carry or primary fight/engage facilitator for the next compulsory cycles.

Isolated top-lane economy, grubs, or one support kill do not automatically satisfy this field.

### 4.4 Primary Mechanism Failure

To set `DPS = BROKEN`, identify the exact mechanism(s) that supported the original CLEAR/STRONG draft edge and test whether they have actually functioned.

Examples:

- claimed protected DPS is materially behind and cannot safely maintain uptime;
- claimed engage pair repeatedly fails to control first contact or continuation;
- claimed objective-setup geometry is repeatedly ceded to the opponent;
- the opposing team's actual kill/control mechanism repeatedly converts through the supposed answer.

Generic statements such as `they are behind` are insufficient. The failure must map back to the original DIM mechanism claim.

### 4.5 Current CFC and next-cycle stress

`CFC_CURRENT = PASS` is mandatory for the contemplated live side after applying current live leverage.

Also require:

`NEXT_CYCLE_STRESS = PASS`

Meaning: from an approximately neutral positional setup at the next meaningful objective/contact cycle, while preserving current items/levels/economy, the contemplated side has the cleaner practical path to dictate or survive first contact, maintain damage access, and convert the fight/objective state.

### 4.6 Draft Recovery Path guard

`DRP = PASS` is mandatory.

Ask:

**Does the original draft-favored side still possess a low-friction, near-term route to reassert the original draft-winning mechanism despite the current live leverage?**

- If yes, `DRP = FAIL` and LRO cannot pass.
- If the route now requires multiple favorable events, a large carry recovery, or execution conditions that are no longer naturally available, `DRP` may pass.

This prevents overreacting to a temporary underdog lead while still allowing the live model to recognize when the draft prior has genuinely stopped describing the current game.

## 5. LRO certificate

For an ML TAKE against a CLEAR/STRONG draft prior, all of the following are mandatory:

- `3SNAP = PASS`
- `2CYCLE = PASS`
- `REGIME_PERSISTENCE = PASS`
- `MULTI_ROLE_LEVERAGE = PASS`
- `DPS = BROKEN`
- `CFC_CURRENT = PASS`
- `NEXT_CYCLE_STRESS = PASS`
- `DRP = PASS`
- all ordinary Live ML price / execution / family / position-blind / SMR requirements pass.

Only then:

`LRO = PASS`

Any FAIL / UNRESOLVED field means `LRO = FAIL/UNRESOLVED -> HOLD/PASS`.

## 6. Anti-overfit guards

LRO must not pass from any one signal by itself, including:

- current gold lead;
- current kill lead;
- one dragon;
- one won fight;
- market odds movement;
- team name / reputation;
- a single fed role;
- the eventual match result.

The review must be reproducible from evidence available at the decision timestamp.

## 7. Separation from draft-locked markets

This procedure applies to **Moneyline only**.

It does not allow live evidence to:

- upgrade an underdog +kills UDKC from FRAGILE/ABSENT to STABLE;
- create missing DIM/TAM/CAS draft proof;
- reclassify a draft-locked +kills market;
- bypass favorite -kills FFD/RNE;
- bypass TK or Duration gates.

Live evidence may override the **weight of a draft prior for ML** without rewriting draft-only certificates used by other market families.

## 8. Mandatory Live ML gate-signature behavior

Every Live ML TAKE must record:

`DRAFT_PRIOR_STATE`

and:

`LRO = PASS/N-A`

If taking against a CLEAR/STRONG draft edge, Entry Evidence must include a compact sub-signature such as:

`LRO[3SNAP=P;2CYCLE=P;REGIME=P;MULTI_ROLE=P;DPS=BROKEN;CFC_CURRENT=P;NEXT_CYCLE=P;DRP=P]`

If aligned with the draft prior or no CLEAR/STRONG prior exists, use `LRO=N/A` and the retained Live ML gates remain mandatory.

## 9. Reference calibration — NS vs T1A Game 1, 2026-08-21

Original post-draft read: CLEAR T1A.

Review only the evidence available through 10:33; do not use the later result to establish eligibility.

Observed sequence:

- 4:13 — NS leads 2-1, about +553g, 0-0 objectives/structures;
- 7:34 — NS leads 3-2, about +895g, first dragon, 0-0 towers;
- 10:33 — NS leads 4-3, about +1.4k, first dragon, 0-0 towers, with meaningful NS leverage visible in jungle/mid/bot/support and T1A's Xayah/Rakan control engine not functioning as the post-draft thesis expected;
- executable NS ML at 10:33: 2.094.

Under this procedure:

- 7:34 remains HOLD because a contrary CLEAR-draft ML has only two snapshots;
- 10:33 becomes the first timestamp eligible for an LRO certificate;
- if the synchronized role-economy / objective / next-cycle checks resolve exactly as above, the intended calibration verdict is `TAKE — NS ML @2.094`.

This is a calibration reference only. It does not create a retrospective position.

## 10. Governance

A normal win/loss does not auto-amend this procedure. Future changes require mechanism-level review or explicit user instruction under the session-lock governance.
