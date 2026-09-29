# 01 — Work: Football C Integrated Board

Read upstream `models/football/CURRENT_MODEL.md` and `models/football/production/FOOTBALL_C.md`.

Use the attached `AISCORE_FIXTURES_*.zip` from Step 0.

Require:
`sweep_scope_mode=BROAD_SENIOR_PRODUCTION`

If the package is invalid, incomplete, or still uses legacy narrow-core filtering, stop:

`HANDOFF INCOMPLETE — BROAD SENIOR COVERAGE GAP`

Do not rebuild the raw universe in Work.

## Task

Run **one integrated Football C screen/research/rank pass over every admitted senior fixture**.

Do not re-apply league registries, low-goal country exclusions, small-cup exclusions, conditional gates, or Football A rules.

For every fixture:
1. verify identity/time/status;
2. research current football evidence;
3. routes = STRONG / USABLE / WEAK;
4. carrier = STRONG / USABLE / NONE;
5. assess chance quality;
6. run relevant H2H/matchup check, prioritizing recent same-venue transferable evidence;
7. state dominant failure mode;
8. choose supported burden before price;
9. rank against the full admitted slate;
10. assign C-FOCUS / C-WATCH / C-PASS.

No fixed board-size cap. Quality first.

## Persistence

Persist **every admitted fixture**, including C-PASS, to Daily Coverage Ledger.

Preserve:
- Football C model identity;
- ordinal C rank where applicable;
- C-PASS/WATCH/FOCUS;
- routes;
- carrier;
- supported line;
- failure mode;
- H2H state;
- evidence confidence.

Do not overwrite historical Football A rows.

## Output

Return:

`FOOTBALL C BOARD <window>`

| Rank | Match | C state | Routes | Carrier | Supported line | Main failure | Initial action |
|---|---|---|---|---|---|---|---|

Initial action is normally REVIEW AT XI or PASS.

Also report:

`ADMITTED TO C -> C-PASS -> C-WATCH -> C-FOCUS`

Keep the report compact while preserving the full rejected-fixture ledger for false-negative audit.
