# Football Women's Senior Top-Flight Coverage

**Status:** mandatory Step-0 coverage invariant  
**Scope:** senior women's domestic top-flight leagues visible on AiScore in the requested sweep window  
**Purpose:** prevent senior women's top-flight blocks from disappearing during discovery, domestic-block filtering, or persistence.

## 1. Mandatory discovery class

Every senior women's domestic **top-flight league** block visible on AiScore in the requested window must be discovered and accounted for.

Examples of the intended class include a country's highest senior women's domestic league. The rule is classification-based, not a hardcoded league-name allowlist.

Do not classify a competition as lower-division, development, reserve, academy, amateur, or obscure merely because it is women's football.

Youth/Uxx, reserve/B-team/development, academy, amateur/semi-professional micro, regional/state/provincial and lower-division women's competitions remain subject to the normal hard-scope rules.

## 2. Discovery is not automatic admission

Women's top-flight status guarantees **coverage/accounting**, not automatic Work admission.

After discovery, every fixture still receives the normal current rules:

1. identity/time integrity;
2. competition reliability memory;
3. operational viability A/B/C/D;
4. researchability;
5. 15-fixture capacity gate.

Therefore a discovered women's top-flight fixture may end as:

- `ADMITTED_TO_C`;
- `OPERATIONAL_EXCLUDED`;
- `RESEARCHABILITY_EXCLUDED`;
- `OPERATIONAL_CAPACITY_DEFERRED`;
- `UNRESOLVED`.

It must not disappear without one of those dispositions.

### Prematch window closed during Step-0 repair

If a fixture was legitimately in the requested sweep window but has already kicked off by the final Step-0 handoff freeze because source acquisition/reconciliation took too long, keep it in the women's raw manifest and record:

`OPERATIONAL_EXCLUDED — PREMATCH WINDOW CLOSED DURING STEP0`

This is a run-time executability disposition, not a negative judgment of the competition's normal observability. Do not drop the fixture and do not capacity-defer an already-started match.

## 3. Researchability parity

Apply the same researchability standard used for men's senior top-flight domestic leagues.

Do not fail Required A/B/C because:
- the league name contains Women / Women's / Frauen / Féminine / Femenina / Dam / Kvinner / Ladies or equivalent;
- the league has a smaller audience;
- the competition is unfamiliar.

Fail only when the actual current evidence is insufficient.

Women's top-flight competitions do **not** automatically bypass the operational viability gate. If XI, market, team-news or mechanism evidence is genuinely weak, preserve the explicit operational/researchability exclusion.

### Current prospective intake proof standard

Preserve every visible senior women's top-flight fixture in discovery and its disposition manifest. New compact or explicitly marked unfinished sweeps use `FOOTBALL_XI_MARKET_FIRST_INTAKE.md`: admission requires the same both-team verified lineup source, current Asian-total market and news evidence as men's fixtures. If evidence is missing, exclude or hold **from Work**, not from coverage or because it is women's football. Compact initial Work limit is 8; legacy frozen handoff limit remains 15.

## 4. Capacity parity

The 15-fixture Work cap remains active.

Within equal operational quality, do not use gender as a negative tiebreaker.

If a women's top-flight fixture clears A/B + researchability but falls outside the 15-fixture cap, preserve:

`OPERATIONAL CAPACITY DEFERRED — STEP0`

That is not a coverage miss.

## 5. Required sweep accounting

Persist:

- `women_top_flight_raw_count`;
- `women_top_flight_admitted_count`;
- `women_top_flight_operational_excluded_count`;
- `women_top_flight_researchability_excluded_count`;
- `women_top_flight_capacity_deferred_count`;
- `women_top_flight_unresolved_count`.

Required equality:

`women_top_flight_raw_count = admitted + operational_excluded + researchability_excluded + capacity_deferred + unresolved`

Also persist a fixture-level `women_top_flight_disposition_manifest` containing every discovered fixture in this class with:
- AiScore ID;
- competition;
- match;
- kickoff ICT;
- final Step-0 disposition;
- operational grade when applicable;
- compact exclusion/defer reason when not admitted.

If the equality fails, or a visible women's top-flight block has no fixture/disposition record:

`HANDOFF INCOMPLETE — WOMEN TOP-FLIGHT COVERAGE GAP`

Do not emit `work_ready=true`.

## 6. Airtable persistence

For every Daily Coverage row belonging to this class, set:

`Senior Women's Top Flight = true`

Sweep Runs stores the six women's-top-flight counters.

This flag is classification/audit metadata only. It must never promote C state, supported burden, FOLLOW lane, or exposure.

## 7. Audit

Post-slate audit must distinguish:

- women's top-flight discovery miss;
- incorrect hard exclusion;
- incorrect operational exclusion;
- incorrect researchability exclusion;
- legitimate capacity deferral;
- admitted predictive false positive/negative.

Do not judge the coverage fix by FT goals or betting P/L.
