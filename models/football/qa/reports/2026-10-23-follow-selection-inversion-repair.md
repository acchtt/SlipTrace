# FOLLOW Selection Inversion Repair — 23 October 2026 ICT

## Defect

`FOLLOW_SELECTION_INVERSION`

Football C correctly retained multiple fixtures as `C-FOCUS`, but the workload
allocator consumed scarce FOLLOW slots while walking the ordinary lexicographic
rank. With `MAX_FOLLOW_PER_KICKOFF=2`, the first two eligible FOCUS rows at a
kickoff received FOLLOW even though ranking and workload allocation answer
different questions.

This also allowed a valid `C-FOCUS` outside capacity to be labelled `STOP`,
which conflated workload capacity with football rejection.

## Repair

Production certificates and board states are unchanged.

The allocator now computes a frozen, market-independent `follow_priority_profile`
for each Football C assessment:

- `follow_floor_score`: protected burden strength;
- `follow_ceiling_score`: credible scoring upside beyond the protected floor;
- `follow_priority_score`: bounded combined workload comparator;
- `follow_floor_tier` / `follow_ceiling_tier`;
- `follow_priority_profile`;
- `follow_history_support_points`, capped at 10;
- `follow_priority_market_independent=true`;
- `follow_priority_execution_authority=false`.

Historical Step-0 goal signal is supporting evidence only. It can break close
workload ties but cannot dominate materially stronger current football structure.

At an exact kickoff, A-grade FOCUS rows are nominated as a portfolio:

1. one strongest protected-floor candidate;
2. one strongest credible-ceiling candidate when available.

Global FOLLOW capacity then selects the strongest role-weighted nominations.
Remaining FOCUS rows compete for RESERVE. Any valid FOCUS still outside workload
capacity is labelled `FOCUS_UNFOLLOWED`, never `STOP`.

`STOP` is reserved for non-FOCUS rows.

## Authority boundaries

This repair does not change:

- FOCUS/WATCH/PASS classification;
- G3/G4/G5/G6 funding;
- certified supported burden;
- ACT/BOOK/PASS policy;
- screenshot-only market authority.

The existing credible-tail diagnostic can inform workload ceiling priority but
never upgrades execution authority.

A ranked `FOCUS_UNFOLLOWED` fixture remains an ordinary sealed C-FOCUS row and
can be assessed through normal ranked `/xi`; it is not an exception.

## Outcome integrity

No final score is an input to the allocator. The 22–23 October results motivated
the audit but did not define thresholds or individual promotions. Historical
receipts remain frozen and are not backfilled.

## Website semantics

The public projection now treats `cBoardState` as predictive authority.
`FOLLOW`, `RESERVE`, and `FOCUS_UNFOLLOWED` can all belong to visual FOCUS.
Workload lane no longer silently converts RESERVE to WATCHLIST or an unfollowed
FOCUS to PASS.

## Regression coverage

Tests enforce:

- exact-kickoff floor/ceiling portfolio selection;
- two-FOLLOW exact-kickoff cap;
- bounded historical signal contribution;
- FOCUS rows outside capacity become `FOCUS_UNFOLLOWED`, not STOP;
- uncapped official FOCUS board remains intact;
- strict C decision authorization still rejects unfollowed workload without an
  authorized execution path while ranked football evidence remains available.


## Immediate v2 correction after frozen replay

The first floor/ceiling allocator was replayed against the sealed 22 Oct
21:00–03:00 board using only frozen prematch evidence. It failed the replay:
certificate depth still inflated workload priority, especially for an O3.50
candidate, and the exact-kickoff cap of two remained too brittle.

Production was corrected immediately:

- FOLLOW workload now has three roles: CLEARABILITY, BALANCED, UPSIDE.
- Workload scores are normalized for certified burden; O3.50 receives a larger
  workload comparison penalty than O2.50 while the certificate itself remains
  untouched.
- exact-kickoff FOLLOW capacity is 3;
- global FOLLOW capacity is 7;
- one CLEARABILITY candidate per kickoff is protected first;
- remaining capacity is allocated to the strongest BALANCED/UPSIDE
  nominations globally.
- final scores remain excluded from every scoring field and threshold.

The sealed replay now nominates:
- 22:00: RoPS–KaPa (CLEARABILITY);
- 23:45: OFI–Leverkusen (CLEARABILITY), Trabzonspor–Hearts (BALANCED),
  Crvena Zvezda–Copenhagen (UPSIDE);
- 02:00: Monaco–Freiburg (CLEARABILITY), Beşiktaş–Crystal Palace (BALANCED),
  Hoffenheim–Lyon (UPSIDE).

The replay is diagnostic only; historical receipts remain immutable.
