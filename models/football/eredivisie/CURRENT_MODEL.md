# Current Eredivisie Extension

**Canonical namespace:** `models/football/eredivisie/`  
**Parent model:** always resolve from `models/football/CURRENT_MODEL.md`  
**Active extension:** **Eredivisie v0.1**  
**Execution mode:** **shadow calibration only**

## Required load order

Before any Eredivisie match analysis:

1. Open `models/football/CURRENT_MODEL.md` and load the complete active SlipTrace football model in the exact order it specifies.
2. Apply all newer parent football rules over older conflicts.
3. Load `models/football/eredivisie/EREDIVISIE_V0.1.md`.
4. Load `models/football/eredivisie/EREDIVISIE_AIRTABLE_SCHEMA_V0.1.md`.
5. Load `models/football/eredivisie/EREDIVISIE_50_MATCH_CALIBRATION_PROTOCOL_V0.1.md` while the initial calibration run is active.
6. Load any later Eredivisie prior snapshot explicitly marked `ACTIVE`; at v0.1 creation there is no activated numeric prior snapshot.

The Eredivisie layer is subordinate to the parent SlipTrace football process. It may supply league-specific priors and probability distributions, but it may not bypass synchronization, reset, evidence, utility, market-scan, settlement, validator, Airtable or record-keeping controls from the active parent model.

## Initial state

- League universe: Netherlands Eredivisie only.
- Numeric Eredivisie priors: `UNINITIALIZED` until supported by an Eredivisie-only dataset.
- Minimum accepted odds: inherited from the active parent model; at project creation this is 1.70.
- Shadow stake: inherited fixed 0.25u; at project creation 1u = 1,000,000 VND and 0.25u = 250,000 VND.
- Official Eredivisie execution: disabled during the initial calibration protocol regardless of whether the parent football circuit breaker is later lifted.
- A model-qualified selection is output as `SHADOW LEAN — DO NOT PLACE`.
- `NO BET` and `NO BET — HOLD` are first-class calibration outcomes and must be recorded.

## Governing principle

**Same SlipTrace decision process; narrower league-specific calibration.**
