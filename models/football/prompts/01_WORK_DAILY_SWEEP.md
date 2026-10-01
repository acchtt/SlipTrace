# 01 — Work: Football C Official + C2 Shadow Board

Read upstream:
- `models/football/CURRENT_MODEL.md`
- `models/football/production/FOOTBALL_C.md`
- `models/football/challengers/football-c2/FOOTBALL_C2_SPEC.md`
- `models/football/challengers/football-c2/TEST_PROTOCOL.md`

Use the attached `AISCORE_FIXTURES_*.zip` from Step 0.

Require:
`sweep_scope_mode=RESEARCHABLE_SENIOR_PRODUCTION`

If package/completeness fails:
`HANDOFF INCOMPLETE — RESEARCHABLE SENIOR COVERAGE GAP`

Do not rebuild the raw universe in Work.

## 1. Common evidence freeze — mandatory

Research each **researchability-admitted** senior fixture **once**. Do not reopen Step-0 researchability-excluded obscure blocks unless the user explicitly overrides that exclusion.

Freeze one common semantic evidence state before either model ranks the slate:

- match_id / identity / kickoff;
- home_route = WEAK / USABLE / STRONG;
- away_route = WEAK / USABLE / STRONG;
- carrier = NONE / USABLE / STRONG;
- carrier_self_fund;
- route_reliability = LOW / MEDIUM / HIGH;
- independent_route_quality = LOW / MEDIUM / HIGH;
- chance_quality = LOW / MEDIUM / HIGH;
- failure_resistance = LOW / MEDIUM / HIGH;
- evidence_confidence = LOW / MEDIUM / HIGH;
- burden_protection = LOW / MEDIUM / HIGH;
- failure_attacks_route;
- material_suppression;
- independent_upper_tail;
- relevant H2H state/transferability;
- main failure mode;
- initial supported_line.

At board time set `xi_robustness` from currently known lineup robustness; if XI is not confirmed, use the same evidence-based pre-XI value for both tracks.

**Do not run separate C and C2 research passes.**  
The experiment compares model policy, not two independently drifting research interpretations.

Once frozen, do not edit common evidence after seeing either model's ranking or the Python output.

## 2. Football C official board

Apply `models/football/production/FOOTBALL_C.md` to the common evidence.

Produce:
- C-PASS
- C-WATCH
- C-FOCUS
- official C ordinal rank
- C supported burden / failure summary

This is the **only official board** for Step 2.

Persist Football C as the canonical Daily Coverage state.

## 3. Football C2 shadow board

Apply the C2 challenger rules to the **same frozen common evidence**.

Compute:
- C2-PASS / C2-WATCH / C2-FOCUS;
- C2 ordinal rank;
- selection-quality floor;
- protected-line inversion diagnostics;
- bridge readiness.

C2 is shadow-only:
- no Website Pick;
- no official exposure;
- do not overwrite Football C official fields.

Persist C2 shadow in dedicated shadow fields/notes when available. If only one canonical coverage row exists, preserve official C fields and store C2 state as clearly labelled `C2_SHADOW` metadata rather than replacing C.

## 4. Python engine — both tracks

Serialize the same frozen evidence twice using:

`models/football/engine/schema.json`

Run:

`model = c`

and

`model = c2`

Board command:

`python models/football/engine/cli.py board --input <payload.json>`

The assessment fields must be identical across C and C2 payloads except for model-specific `board_state` after each text policy has classified the fixture.

Python is shadow validation only.

If text/code disagree:

`ENGINE DISAGREEMENT — PRESERVE BOTH`

Do not mutate the frozen semantic evidence.

## 5. Output

Primary table — official production board:

`FOOTBALL C OFFICIAL BOARD <window>`

| C Rank | Match | C state | Routes | Carrier | Supported line | Main failure | Initial action |
|---|---|---|---|---|---|---|---|

Then comparison table:

`FOOTBALL C2 SHADOW DELTA`

| Match | C rank/state | C2 rank/state | C2 floor | Bridge readiness | Material difference |
|---|---|---|---|---|---|

Report funnel:

`ADMITTED -> C-PASS/C-WATCH/C-FOCUS -> C2-PASS/C2-WATCH/C2-FOCUS`

Also report any:
- C vs C2 rank inversion;
- C2 selection-floor block;
- potential unreachable-WAIT risk;
- text-vs-code disagreement.

## 6. Required machine appendix

Include:
- `FOOTBALL_ENGINE_C_INPUT`
- `FOOTBALL_ENGINE_C_RESULT`
- `FOOTBALL_ENGINE_C2_INPUT`
- `FOOTBALL_ENGINE_C2_RESULT`

If runtime execution is unavailable:
`ENGINE NOT EXECUTED — STRUCTURED INPUT PRESERVED`

## 7. Non-negotiable separation

- Football C official board feeds official Step 2.
- C2 shadow board never substitutes for C.
- C2 may not create real-bet instructions.
- Both tracks use the same frozen common evidence epoch.


## 5. Operational follow-through guard — mandatory

The Football C board itself remains uncapped for audit. **Operational follow-through is capacity-limited.**

After the official C board is frozen, assign every official C fixture one operational lane using `models/football/engine/core.py::follow_through_lane`:

### FOLLOW
Routine XI/odds follow-through is allowed only when all are true:
- C-FOCUS;
- both routes at least USABLE;
- at least one route STRONG;
- carrier STRONG;
- route reliability HIGH;
- independent route quality HIGH;
- chance quality HIGH;
- failure resistance HIGH;
- evidence confidence HIGH;
- supported line <= O3.0;
- no route-attacking failure or material suppression.

### RESERVE
A C-FOCUS may be RESERVE when the same core structure clears but:
- failure resistance is MEDIUM; and
- burden protection is HIGH.

RESERVE does not consume routine Step-2 attention. Activate it only when:
- FOLLOW candidates collapse at XI/price; or
- the user explicitly asks for the reserve match.

### STOP
All other C-FOCUS, every C-WATCH and every C-PASS remain frozen for audit but do not receive routine XI/odds/live follow-through.

This is an **operational capacity rule**, not a reclassification of C-PASS/WATCH/FOCUS.

### Capacity

After quality gating:
- maximum routine `FOLLOW = 6`;
- maximum retained `RESERVE = 4`.

If more qualify, preserve official C rank and demote overflow in rank order:
`FOLLOW overflow -> RESERVE -> STOP`.

Never alter the underlying C state to satisfy the capacity limit.

## 6. Revised output

Show the operational queue first:

`FOOTBALL C FOLLOW-THROUGH QUEUE`

| Queue | C rank | Match | C state | Routes | Carrier | Supported line | Why |
|---|---:|---|---|---|---|---:|---|

Order:
1. FOLLOW
2. RESERVE
3. compact count only for STOP unless the user asks for the full board.

Then keep the full board persisted for audit.

Report:

`SERIOUS CANDIDATES -> FOLLOW -> RESERVE -> STOP`

The normal user-facing schedule should contain only FOLLOW fixtures. RESERVE may be shown separately but is not part of routine monitoring.


## Prospective elite upper-tail observer — non-predictive

Read:
`models/football/trials/FOOTBALL_C_ELITE_UPPER_TAIL_OBSERVER_2026-10-01.md`

After the common evidence freeze, tag `ELITE_UPPER_TAIL_OBSERVER` when the frozen fixture satisfies every observer trigger.

The tag:
- must be assigned before outcome;
- does not alter C state, rank, supported burden or follow-through lane;
- does not authorize exposure;
- is carried forward only for prospective audit.
