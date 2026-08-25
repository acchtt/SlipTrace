# LoL Pro Meta + Kill-Handicap Asymmetry Calibration — 2026-08-25

Status: PENDING CANONICAL ACTIVATION until referenced by `models/lol/CURRENT_MODEL.md`.

## Scope

This procedure codifies calibration lessons from professional / officially sanctioned semi-professional League of Legends shadow auditing on 2026-08-25. It supplements, and does not replace, DIM, PDRL, KHMC, UDKC/UCS/LAC, DOVC, FRP, FCR, CFC, LRO, PRE_TAKE_CERT, exact signed kill-margin arithmetic, and all active session-lock governance.

## 1. Professional Meta Layer (PML)

For pro/semi-pro draft reading, PDRL must include a dedicated Professional Meta Layer. Do not use solo-queue tier lists or generic champion strength to satisfy this layer.

For each drafted or materially available champion, resolve where evidence is available:

- `PRO_META_PRIORITY`: current professional pick/ban priority on the competition patch and relevant region/tier;
- `ROLE_FLEX_VALUE`: credible role flexibility or draft ambiguity in professional play;
- `BLIND_SAFETY`: professional blind-pick resilience and punishability;
- `PAIRING_DEPENDENCY`: whether value depends on a specific jungle/support, mid/jungle, or bot/support partner;
- `PRO_FUNCTION`: the professional function supplied: lane priority, first move, engage, disengage, front line, waveclear, objective DPS, side pressure, pick threat, backline access, carry protection, terrain/choke control, reset, or siege;
- `PLAYER_STAGE_FIT`: recent stage evidence for the player on the champion/archetype;
- `POCKET_TAX`: execution/uncertainty tax for low-priority or player-specific pocket picks unless recent stage evidence supports them;
- `FEARLESS_SCARCITY_VALUE`: value of preserving or consuming a scarce remaining archetype in restricted-pool/Fearless series.

High pro presence is not itself proof of draft superiority. Presence can come from flexibility, blind safety, ban strategy, role scarcity, or system fit. A meta champion can still be poor in a specific composition.

## 2. Archetype inventory over champion counting

For Game 2+ Fearless/restricted-pool drafts, maintain remaining functional inventory, not only champion lists. At minimum track whether each team still has credible access to:

- reliable engage;
- disengage/reset;
- front line;
- lane priority by phase;
- jungle/support coupling;
- mid/jungle first move;
- bot-lane stability/carry protection;
- waveclear;
- objective DPS;
- side-lane pressure;
- pick threat;
- backline access.

Burning multiple champions that provide the same scarce function is a series-pool pressure event even if many legal champions remain.

## 3. Draft-read causal order

When exact roles are known, prefer this causal sequence over champion-reputation summaries:

`LANE STATES -> JUNGLE/SUPPORT ACCESS -> FIRST-MOVE WINDOWS -> OBJECTIVE-SEQUENCE PROJECTION -> TRANSITION QUALITY -> 2/3-ITEM FIGHT SHAPE -> WCSR -> EXECUTION BURDEN -> SERIES-POOL PRESSURE -> ADVERSARIAL PASS`.

Do not conclude from standalone labels such as "more scaling", "more engage", "more tanks", "three winning lanes", "counterpick", or "more meta champions".

## 4. Small kill-handicap asymmetry

The side-neutral KH margin distribution remains the parent gate and must be built before sign selection. This calibration is a downstream structural filter; it does not authorize sign selection before `KH_MARGIN_CERT`.

### 4.1 Underdog small positive handicaps

A small positive kill handicap on an underdog is generally poor protection because one ordinary late fight/cleanup sequence can erase the cushion while the price is materially shorter than ML.

Before PRE_TAKE_CERT, classify `DOG_CUSHION_CLASS` using exact current state and the model's live one-fight/cascade tail:

- `INSUFFICIENT`: cushion does not survive a realistic single-fight/cleanup swing;
- `THIN`: survives only a narrow normal-fight outcome and remains ML-like;
- `MATERIAL`: provides real protection against normal fight variance;
- `LARGE`: survives multiple realistic margin-expansion paths.

`INSUFFICIENT` => automatic SKIP for underdog +kills.

`THIN` => presumptive SKIP and may proceed only if written UCS + LAC + WMS evidence explicitly proves unusual suppression of the relevant expansion tail. Price alone cannot override this.

The exact numerical line is state-dependent; do not hard-code +1.5/+2.5/+3.5 as universally invalid. However, these lines should normally receive severe scrutiny for underdogs.

### 4.2 Favorite small negative handicaps

A small negative handicap on a certified favorite is not structurally defective merely because the absolute line is small. It can be an efficient expression of an established favorite edge if the side-neutral distribution supports the required final margin and the favorite downstream mechanism stack passes.

Thus:

`SMALL ABS(H)` is not a blanket veto.

The asymmetry is functional: small `+H` often fails to buy meaningful underdog protection, while small `-H` can still price a favorite's central winning-margin mass.

### 4.3 No sign inversion

Failure of underdog cushion sufficiency is zero evidence for favorite -H. Failure of favorite margin expansion is zero evidence for underdog +H. Both sides still derive from the same locked side-neutral margin distribution.

## 5. Screenshot synchronization clarification

Source/device capture timestamps are not by themselves a synchronization veto.

When the user explicitly states that scoreboard and market screenshots represent the same live state, treat them as synchronized unless internal game-state evidence contradicts that claim (for example materially incompatible game clocks, kills/objectives, or a market clearly belonging to a different map).

Phone status-bar time differences, capture-order differences, or UI refresh lag alone do not make a pair stale.

This clarification does not waive the requirement for two usable synchronized live snapshots for ML/KH/TK.

## 6. Recent-series workload

Playing the previous day, short turnaround, long prior series, or travel/schedule congestion may enter `PRO_EXEC_CONTEXT`, but workload is not a standalone fade or TAKE signal.

It may adjust execution burden only when tied to observable mechanisms such as reduced champion preparation, substitution/roster constraints, repeated late-series execution degradation, or verified schedule stress. Generic fatigue narratives cannot upgrade an edge.

## 7. Duration Over calibration evidence

Early dragons, low kills, low towers, close gold, or elapsed time remain neutral descriptors by themselves.

A useful Duration Over signal is repeated objective/tempo acquisition without structural conversion when actual failed conversion, defensive reset, waveclear, or another clock-consuming mechanism is observed. This remains subject to full DOVC, including Structure Substitution and shortest-cascade testing.

Do not promote the 2026-08-25 KRXC-BFXY Game 4 result into a standalone heuristic; it is supporting evidence for the existing DOVC causal framework.

## 8. PRE_TAKE_CERT additions

For professional draft-derived candidates, PRE_TAKE_CERT must confirm where applicable:

- `PML_RUN = PASS`;
- `META_SOURCE_CLASS = PRO_ONLY/PRO_RELEVANT`, never solo-queue-only;
- `ARCHETYPE_INVENTORY_UPDATED = PASS` for Fearless Game 2+;
- `PLAYER_STAGE_FIT_RESOLVED` or explicit `UNKNOWN/PENALIZED`;
- `POCKET_TAX_APPLIED` where relevant.

For underdog +kills:

- `DOG_CUSHION_CLASS` must be recorded;
- `DOG_CUSHION_CLASS = INSUFFICIENT` forbids TAKE;
- `THIN` requires explicit written exceptional proof through UCS/LAC/WMS; omission is mechanical FAIL.

For favorite -kills:

- do not reject solely because `ABS(H)` is small;
- use the locked KH distribution plus favorite-tail validator.

## 9. Governance

This procedure becomes active only when incorporated into canonical `CURRENT_MODEL.md` and, for a locked slate, only through a new authorized authority epoch/relock. Closed-slate results are preserved and never rewritten by this calibration.
