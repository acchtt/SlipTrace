# 01 — Work: Football C2 Integrated Board

Read upstream:
- `models/football/CURRENT_MODEL.md`
- `models/football/challengers/football-c2/FOOTBALL_C2_SPEC.md`
- `models/football/challengers/football-c2/TEST_PROTOCOL.md`

Do **not** load the legacy `models/football/production/FOOTBALL_C.md` for this Work ranking pass.

Use the attached `AISCORE_FIXTURES_*.zip` from Step 0.

Require:
`sweep_scope_mode=BROAD_SENIOR_PRODUCTION`

If the package is invalid, incomplete, or still uses legacy narrow-core filtering, stop:

`HANDOFF INCOMPLETE — BROAD SENIOR COVERAGE GAP`

Do not rebuild the raw universe in Work.

## Task

Run **one integrated Football C2 screen/research/rank pass over every admitted senior fixture**.

Do not re-apply league registries, low-goal country exclusions, small-cup exclusions, conditional gates, or Football A rules.

For every fixture:
1. verify identity/time/status;
2. research current football evidence;
3. routes = STRONG / USABLE / WEAK;
4. carrier = STRONG / USABLE / NONE;
5. assess chance quality;
6. run relevant H2H/matchup check, prioritizing recent same-venue transferable evidence;
7. state dominant failure mode;
8. choose initial supported burden before price;
9. run the **C2 selection-quality floor**;
10. rank against the full admitted slate;
11. assign `C2-FOCUS / C2-WATCH / C2-PASS`;
12. run the **protected-line inversion guard** before any WATCH can later become exposure;
13. for high-quality FOCUS candidates whose market is +0.25/+0.50 above the initial burden, flag them for the **Focus Market-Gap Bridge** at XI/odds rather than defaulting to an unreachable WAIT.

No fixed board-size cap. Quality first.

## C2 ranking order

Rank survivors by:
1. route reliability;
2. independent route quality / self-funded carrier strength;
3. current chance quality;
4. failure-mode resistance;
5. XI robustness when known;
6. evidence confidence;
7. burden protection.

**Price does not create rank.**

A lower protected line must not push a weaker match above a stronger football environment.

## Selection-quality floor

A future direct C2-BET must eventually satisfy one of:

### Two-route floor
- both routes at least USABLE;
- at least one route STRONG;
- no unresolved failure mode directly attacks either scoring route.

### Carrier floor
- one STRONG CARRIER;
- independent current upper-tail proof;
- opponent route may be WEAK only if the carrier can plausibly self-fund the selected burden.

During Work ranking, record whether the fixture currently looks:
- `FLOOR CLEAR`
- `FLOOR BORDERLINE`
- `FLOOR FAIL`

A low O2.0/O2.25 burden does not waive the floor.

## Focus Market-Gap readiness

For each C2-FOCUS, record whether independent football evidence could support a future +0.25 or +0.50 bridge if the XI/odds market sits above the initial burden.

Classify:
- `BRIDGE READY +0.25`
- `BRIDGE READY +0.50`
- `BRIDGE NOT PROVEN`

This is football-only evidence. Market magnitude itself can never prove the bridge.

## Persistence

Persist **every admitted fixture**, including C2-PASS, to Daily Coverage Ledger.

Preserve:
- Football C2 model identity;
- ordinal C2 rank where applicable;
- C2-PASS/WATCH/FOCUS;
- routes;
- carrier;
- initial supported line;
- failure mode;
- H2H state;
- evidence confidence;
- selection-floor state;
- bridge-readiness state.

Do not overwrite historical Football A or Football C1 rows.

Football C2 is **SHADOW ONLY**:
- no official exposure;
- no Website Pick;
- no real-bet instruction from Work ranking.

## Output

Return:

`FOOTBALL C2 BOARD <window>`

| Rank | Match | C2 state | Routes | Carrier | Supported line | Selection floor | Bridge readiness | Main failure | Initial action |
|---|---|---|---|---|---|---|---|---|---|

Initial action is normally `REVIEW AT XI` or `PASS`.

Also report:

`ADMITTED TO C2 -> C2-PASS -> C2-WATCH -> C2-FOCUS`

And explicitly flag:
- any **selection inversion risk** where a weaker protected-line match could outrank a stronger football environment;
- any **potential unreachable-WAIT risk** where a C2-FOCUS looks likely to open +0.50 or more above supported burden.

Keep the report compact while preserving the full rejected-fixture ledger for false-negative audit.
