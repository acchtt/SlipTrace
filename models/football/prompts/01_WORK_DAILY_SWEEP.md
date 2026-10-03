# 01 — Work: Football C Official + C2 Shadow Board

**Command alias:** `/rank`

Read upstream:
- `models/football/CURRENT_MODEL.md`
- `models/football/production/FOOTBALL_C.md`
- `models/football/challengers/football-c2/FOOTBALL_C2_SPEC.md`
- `models/football/challengers/football-c2/TEST_PROTOCOL.md`
- `models/football/procedures/FOOTBALL_TOURNAMENT_INCENTIVE_INTEGRITY.md`
- `models/football/procedures/FOOTBALL_OPERATIONAL_VIABILITY_GATE.md`
- `models/football/procedures/FOOTBALL_COMPETITION_RELIABILITY_MEMORY.md`
- `models/football/procedures/FOOTBALL_BURDEN_COMPLETION_SELECTION.md`
- `models/football/procedures/FOOTBALL_WOMENS_TOP_FLIGHT_COVERAGE.md`

Use the attached `AISCORE_FIXTURES_*.zip` from Step 0.

Require:
`sweep_scope_mode=RESEARCHABLE_SENIOR_PRODUCTION`

If package/completeness fails:
`HANDOFF INCOMPLETE — RESEARCHABLE SENIOR COVERAGE GAP`

Do not rebuild the raw universe in Work.

## 0. Operational handoff gate — fail closed

Before full football research, verify the Step-0 contract:

- admitted fixture count <= 15;
- every admitted fixture has `operational_viability_grade = A / B`;
- every admitted fixture has `xi_expected`, `market_observability`, `team_news_observability`, and `operational_viability_reason`;
- every admitted fixture has `competition_reliability_state` and `competition_reliability_reason`;
- CAUTION is never above B and DEMOTED is present only as an allowed B probation fixture;
- no C/D fixture appears in the normal Work array;
- all six women's-top-flight counters are present;
- `women_top_flight_unresolved_count = 0`;
- `women_top_flight_raw_count` equals admitted + operational excluded + researchability excluded + capacity deferred + unresolved;
- `women_top_flight_disposition_manifest` is present and contains every discovered senior women's domestic top-flight fixture.

If a C/D fixture leaks in:

`ASSESSMENT BLOCKED — LOW OPERATIONAL OBSERVABILITY`

If the handoff contains more than 15 normal admissions:

`HANDOFF INCOMPLETE — OPERATIONAL CAPACITY BREACH`

If women's-top-flight counters/manifest are absent, inconsistent, unresolved, or omit a visible block:

`HANDOFF INCOMPLETE — WOMEN TOP-FLIGHT COVERAGE GAP`

Do not rescue Step-0 operational exclusions or capacity-deferred fixtures with deep Work research unless the user explicitly declares an exception.

## 1. Common evidence freeze — mandatory

Research each **researchability-admitted** senior fixture **once**. Do not reopen Step-0 researchability-excluded obscure blocks unless the user explicitly overrides that exclusion.

### Tournament-incentive applicability gate — mandatory first

For **every fixture**, explicitly set:

- `tournament_incentive_required = true / false`.

If false, persist all tournament fields as `NOT_APPLICABLE`.

If true, complete the mandatory tournament-format/incentive procedure **before** route/failure/supported-burden classification is finalized. Persist:

- `tournament_format_status = VERIFIED / LIMITED / UNKNOWN`;
- `competition_stage`;
- `competition_format`;
- `draw_resolution`;
- `aggregate_state`;
- `qualification_state` — exact current advancement/elimination requirement;
- `simultaneous_results_status = VERIFIED / NOT_APPLICABLE / LIMITED / UNKNOWN`;
- `simultaneous_results_note`;
- `home_incentive`;
- `away_incentive`;
- `tiebreak_margin_relevance = YES / NO / UNKNOWN`;
- `incentive_effect = EXPANSIVE / NEUTRAL / SUPPRESSIVE / MIXED / UNKNOWN`.

If an applicable fixture is missing any field:

`ASSESSMENT INCOMPLETE — TOURNAMENT INCENTIVE CHECK MISSING`

If fields are present but any material incentive element remains LIMITED / UNKNOWN / unresolved:

`ASSESSMENT BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED`

A tournament fixture is resolved for Step 1 only if format status is VERIFIED, qualification state is explicit, home/away incentives are resolved, tiebreak/margin relevance is YES/NO, simultaneous-result impact is VERIFIED or genuinely NOT_APPLICABLE, and incentive effect is resolved.

Until then place it in a separate `INCENTIVE-INCOMPLETE` table. It receives **no C/C2 state, no rank, no supported line, and no follow-through lane**. Continue processing other fixtures.

A user-declared exception may reopen research but **never bypasses the incentive-resolution gate**.

Freeze one common **football-fact** evidence state before either model applies policy.

Shared facts stop before model-owned supported-burden selection. Football C and C2 may consume the same routes/carrier/chance/failure/H2H/incentive evidence but must independently derive any policy-owned supported burden.

Freeze these shared facts:

- match_id / identity / kickoff;
- operational_viability_grade = A / B;
- xi_expected = YES / UNCERTAIN;
- market_observability = HIGH / MEDIUM;
- team_news_observability = HIGH / MEDIUM;
- operational_viability_reason;
- raw_operational_viability_grade;
- competition_reliability_state;
- competition_reliability_reason;
- competition_reliability_manual_override;
- demoted_probation;
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
- opponent_leakage = LOW / MEDIUM / HIGH;
- continuation evidence sufficient to let each model apply its own policy;
- failure_attacks_route;
- material_suppression;
- independent_upper_tail;
- relevant H2H state/transferability;
- competition stage/format when applicable;
- draw_resolution / aggregate_state;
- home_incentive / away_incentive;
- tiebreak_margin_relevance;
- incentive_effect = EXPANSIVE / NEUTRAL / SUPPRESSIVE / MIXED / UNKNOWN;
- main failure mode.

Do **not** freeze one shared `supported_line` as common policy evidence.

After the common facts are frozen:
- Football C derives and freezes `c_supported_line` plus its model-owned machine fields `completion_mode`, `burden_completion_quality`, `continuation_quality`, and `burden_stall_risk` under the active burden-completion procedure;
- Football C2 independently derives and freezes `c2_supported_line` under Section 5 of its frozen challenger specification;
- neither model may copy the other model's line simply for payload/persistence convenience.

At board time set `xi_robustness` from currently known lineup robustness; if XI is not confirmed, use the same evidence-based pre-XI value for both tracks.

For cups/tournaments/qualifiers/two-leg ties/final-round incentive states, the format-and-incentive check is mandatory before freezing supported burden. Do not mark suppression or expansion from recent scores alone. If the incentive state is LIMITED/UNKNOWN, do not freeze an official supported burden at all; keep the fixture INCENTIVE-INCOMPLETE until resolved.

**Do not run separate C and C2 research passes.**  
The experiment compares model policy, not two independently drifting research interpretations.

Once frozen, do not edit common evidence after seeing either model's ranking or the Python output.

## 2. Football C official board

Apply `models/football/production/FOOTBALL_C.md` to the common evidence.

Before final C state/rank, derive the Football C-owned completion fields and `c_supported_line`, then answer for every fixture:

`WHERE DOES THE GOAL THAT CLEARS THE SUPPORTED BURDEN COME FROM?`

Two-sided route labels are insufficient. A HIGH carrier-led completion path may survive with a WEAK second scoring route. Conversely, a balanced TWO_SIDED profile with HIGH stall risk must not receive routine preference merely because both teams can plausibly score once.

If a proposed C-PASS has HIGH completion + HIGH continuation + STRONG self-funded carrier + independent upper-tail proof + MEDIUM/HIGH opponent leakage and no suppression, re-open the screen. Do not finalize C-PASS solely from the weak second route.

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

First derive and freeze `c2_supported_line` independently from the shared football facts. Do not read or copy `c_supported_line` while creating it.

Compute:
- C2-PASS / C2-WATCH / C2-FOCUS;
- C2 ordinal rank under the frozen C2 ranking policy;
- C2 supported line;
- selection-quality floor;
- protected-line inversion diagnostics;
- bridge readiness.

If an independent C2 supported line cannot be frozen:
`C2 COMPARISON INCOMPLETE — SUPPORTED BURDEN NOT INDEPENDENTLY FROZEN`
and exclude that fixture from confirmatory C-vs-C2 action metrics while continuing Football C normally.

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

The factual assessment fields must be identical across C and C2 payloads. The following are explicitly model-owned and may differ:
- `model`;
- `board_state`;
- `supported_line` (C payload = `c_supported_line`; C2 payload = `c2_supported_line`).

The engine schema still carries Football C completion diagnostics in the shared assessment object. They are non-operative for C2 deterministic ranking/action and must never be used to overwrite C2's own supported line.

Python is shadow validation only.

If text/code disagree:

`ENGINE DISAGREEMENT — PRESERVE BOTH`

Do not mutate the frozen semantic evidence.

## 5. Output

Primary table — official production board:

`FOOTBALL C OFFICIAL BOARD <window>`

| C Rank | Match | C state | Routes | Carrier | Incentive | Supported line | Main failure | Initial action |
|---|---|---|---|---|---|---|---|---|

Then comparison table:

`FOOTBALL C2 SHADOW DELTA`

| Match | C rank/state | C line | C2 rank/state | C2 line | C2 floor | Bridge readiness | Material difference |
|---|---|---:|---|---:|---|---|---|

Report funnel:

`ADMITTED -> C-PASS/C-WATCH/C-FOCUS -> C2-PASS/C2-WATCH/C2-FOCUS`

Also report any:
- C vs C2 rank inversion;
- C2 selection-floor block;
- potential unreachable-WAIT risk;
- text-vs-code disagreement.

## 6. Required machine appendix

Every machine assessment object must include the explicit operational-viability / competition-reliability contract **and** the tournament-incentive contract. The engine must reject omission instead of defaulting it away.

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
- operational viability grade A;
- C-FOCUS;
- completion mode TWO_SIDED / CARRIER_LED / FORCED_CHAOS / MIXED;
- carrier STRONG;
- route reliability HIGH;
- burden completion HIGH;
- continuation HIGH;
- burden stall risk LOW;
- chance quality at least MEDIUM;
- failure resistance HIGH;
- evidence confidence HIGH;
- supported line <= O3.0;
- no route-attacking failure or material suppression.

TWO_SIDED requires two usable routes and at least one STRONG route.

CARRIER_LED permits a WEAK second route only when the STRONG carrier can self-fund, independent upper-tail proof is present, and opponent leakage is at least MEDIUM.

Two-sidedness alone is not a FOLLOW advantage.

### RESERVE
Operational grade B can never receive routine FOLLOW at board time; when football structure clears it is capped at RESERVE.

An A-grade C-FOCUS may also be RESERVE when the completion path remains credible and burden protection is HIGH but failure resistance, completion or continuation is MEDIUM, or stall risk is MEDIUM rather than LOW.

RESERVE does not consume routine Step-2 attention. Activate it only when:
- FOLLOW candidates collapse at XI/price; or
- the user explicitly asks for the reserve match.

### STOP
All other C-FOCUS, every C-WATCH and every C-PASS remain frozen for audit but do not receive routine XI/odds/live follow-through.

This is an **operational capacity rule**, not a reclassification of C-PASS/WATCH/FOCUS.

### Capacity

After quality gating:
- maximum routine `FOLLOW = 6`;
- maximum retained `RESERVE = 4`;
- maximum routine `FOLLOW = 2` for fixtures sharing the exact scheduled kickoff minute.

Rank exact-same-kickoff candidates by the burden-completion key before consuming FOLLOW capacity. Otherwise-qualified same-kickoff overflow goes to RESERVE, then STOP.

If more qualify, preserve official C rank and demote overflow in rank order:
`FOLLOW overflow -> RESERVE -> STOP`.

Never alter the underlying C state to satisfy the capacity limit.

## 6. Revised output

Show the operational queue first:

`FOOTBALL C FOLLOW-THROUGH QUEUE`

| Queue | C rank | Same-KO rank | Match | Op grade | C state | Completion mode | Completion | Continuation | Stall risk | Carrier | Supported line | Why |
|---|---:|---:|---|---|---|---|---|---|---|---|---:|---|

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
