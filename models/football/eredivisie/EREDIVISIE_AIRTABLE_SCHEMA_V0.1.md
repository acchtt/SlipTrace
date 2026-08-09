# Eredivisie Airtable Schema v0.1

**Status:** Design specification  
**Purpose:** Add league-specific calibration storage without changing the SlipTrace core validator architecture.

## 1. Architectural rule

Do not replace or duplicate the parent football enforcement layer.

The existing `SlipTrace Football Decision Control` base remains the Layer 1 control plane. Its `Decision States` table remains mandatory for every material football assessment that could produce a side, total, derivative or shadow selection. The existing hard validator and its required fields remain unchanged.

Eredivisie-specific storage is Layer 2. It should link to the core decision-state record rather than bypass it.

Recommended design inside the same Airtable base:

1. existing `Decision States` — unchanged core validator state;
2. existing `Circuit Breaker` — unchanged parent circuit-breaker tracking;
3. new `Eredivisie Matches` — one record per eligible Eredivisie match;
4. new `Eredivisie Assessments` — one record per material Eredivisie assessment;
5. new `Eredivisie Prior Snapshots` — versioned league-calibration outputs.

The 50-match Eredivisie calibration run is separate from the parent four-match football circuit breaker. If the parent circuit breaker is active, a qualifying Eredivisie shadow selection must still satisfy the parent `Circuit Breaker` requirements in addition to the league calibration record.

## 2. Table: Eredivisie Matches

**Granularity:** one record per verified eligible match.  
**Primary field:** `Eredivisie Match ID`.

Recommended ID format:

`ERED-{season}-{yyyymmdd}-{home-slug}-{away-slug}`

### Identity and universe fields

- `Eredivisie Match ID` — single line text, primary.
- `Competition` — single select; initially only `Netherlands Eredivisie` is valid for calibration inclusion.
- `Competition Verified` — checkbox.
- `Season` — single line text.
- `Match Date` — date.
- `Home Team` — single line text.
- `Away Team` — single line text.
- `Venue` — single line text.
- `Home/Away Verified` — checkbox.
- `Calibration Eligible` — checkbox.
- `Exclusion Reason` — multiline text.
- `Promoted Home Team` — checkbox.
- `Promoted Away Team` — checkbox.

`Calibration Eligible = true` only after competition membership and home/away identity are verified. Cup, European, friendly, Eerste Divisie, youth/reserve and international matches must remain false even when an Eredivisie club is involved.

### Final outcome fields

- `Final Home Goals` — number.
- `Final Away Goals` — number.
- `Halftime Home Goals` — number.
- `Halftime Away Goals` — number.
- `Home Result` — single select: Win / Draw / Loss.
- `Winning Margin` — number, absolute goals for winning side; 0 for draw.
- `Home Red Cards` — number.
- `Away Red Cards` — number.
- `First Goal Minute` — number or single line text when stoppage-time notation must be preserved.
- `First Goal Team` — single select: Home / Away / None.
- `Late Goal 76+` — checkbox.
- `Comeback Occurred` — checkbox.

### Closing-market fields

Preserve raw close information rather than forcing one synthetic CLV number.

- `Closing Favorite` — single line text.
- `Closing AH Line` — single line text.
- `Closing AH Favorite Odds` — number.
- `Closing AH Underdog Odds` — number.
- `Closing Total Line` — single line text.
- `Closing Over Odds` — number.
- `Closing Under Odds` — number.
- `Closing Market Timestamp` — dateTime.
- `Closing Market Source` — single line text.
- `Closing Data Quality` — single select: Verified / Partial / Unavailable.

Do not infer missing closing prices from final results or later retrospective commentary.

## 3. Table: Eredivisie Assessments

**Granularity:** one record per material assessment, including `NO BET` and `NO BET — HOLD`.  
**Primary field:** `Eredivisie Assessment ID`.

Recommended ID format:

`ERED-ASMT-{match-id}-{reset-epoch}-{sequence}`

### Core-link fields

- `Eredivisie Assessment ID` — single line text, primary.
- `Core Assessment ID` — single line text containing the exact `Decision States.Assessment ID`.
- `Core Decision State` — optional linked-record field to the existing `Decision States` table.
- `Eredivisie Match` — linked record to `Eredivisie Matches`.
- `Parent Football Version` — single line text.
- `Eredivisie Model Version` — single line text; `v0.1` initially.
- `Assessment Time` — dateTime.

The core Decision States record must exist independently. The league table is not a substitute for the validator write lock.

### Synchronized state fields

- `Score` — single line text.
- `Minute` — single line text.
- `Assessment Period` — single line text.
- `Reset Epoch` — single line text.
- `Prematch/Live` — single select: Prematch / Live.
- `Goal Environment` — single select: Unresolved / Closed / Neutral / Open.
- `Synchronized State` — checkbox.
- `Reset Resolved` — checkbox.
- `Competition Universe Verified` — checkbox.

### Team/role fields

- `Home Team` — single line text.
- `Away Team` — single line text.
- `Favorite Team` — single line text.
- `Favorite Status` — single select: None / Slight / Material / Deep.
- `Candidate Side Role` — single select: Favorite / Underdog / Neutral / Not Applicable.
- `Home/Away Split Used` — checkbox.
- `Promoted Team Involved` — checkbox.
- `Lineup Status` — single select: Confirmed / Expected / Partial / Unknown.
- `Goalkeeper Materiality` — single select: Positive / Negative / Neutral / Unknown.
- `Centre-Back Stability` — single select: Strong / Normal / Weak / Unknown.

### Market fields

- `Market Family` — single select: Asian Handicap / Moneyline / DNB / Goals / Team Total / Corners / Other.
- `Candidate` — single line text.
- `Line` — single line text.
- `Odds` — number.
- `Minimum Accepted Odds` — number.
- `Settlement Scope` — single line text.
- `Market Timestamp` — dateTime.
- `Major Markets Scanned` — checkbox.
- `Best Expression` — single line text.

### Probability and margin fields

Populate only when the underlying model supports the precision. Blank is preferable to unsupported precision.

- `Model Win Probability` — percent.
- `Model Draw Probability` — percent.
- `Model Exactly-One Margin Probability` — percent.
- `Model Two-Plus Margin Probability` — percent.
- `Model Loss Probability` — percent.
- `Probability Support` — single select: Supported / Provisional / Insufficient.
- `Probability Interval Notes` — multiline text.
- `Fair Odds` — number.
- `Uncertainty Adjusted Edge` — percent.

For total markets, the margin fields may be left blank and the event-budget fields should carry the relevant distribution.

### Evidence fields

- `Primary Evidence Channels` — multiple select.
- `Independent Primary Channel Count` — number.
- `Evidence Summary` — multiline text.
- `xG Role` — single select: Secondary Only / Not Used / Violation.
- `Underdog Suppression Evidence Count` — number.
- `Favorite First-Goal Branch` — single select: Pass / Fail / Unresolved / Not Applicable.
- `Margin Incentive Propagated` — checkbox.
- `Directional Persistence` — single select: Established / One Snapshot / Unstable / Not Applicable.

Recommended primary-channel choices should mirror the parent validator terminology rather than invent league-specific substitutes:

- Box/Central Access
- Big/Clear Chances
- Dangerous Transitions/Cutbacks
- Sustained Set-Piece Pressure
- Defensive Degradation
- Shot-Location/Chance Structure
- Persistent Territory/Box Touches
- Tempo/Persistence
- Relevant Scoring/Conceding Profile
- Predictive Lineup/Availability

### Event-budget fields

- `Current Goal Count` — number.
- `Additional Goals Full Win` — single line text.
- `Additional Goals Half Win` — single line text.
- `Additional Goals Push` — single line text.
- `Additional Goals Half Loss` — single line text.
- `Additional Goals Full Loss` — single line text.
- `Handicap Settlement Branches` — multiline text.

Use exact branches. Do not simplify quarter lines into binary win/loss fields.

### Validator/verdict fields

- `Validator Result` — single select: PASS / HOLD / FAIL.
- `Fail/Hold Reasons` — multiline text.
- `Hold Unlock Condition` — multiline text.
- `Verdict` — single select: SHADOW LEAN — DO NOT PLACE / NO BET — HOLD / NO BET.
- `Eredivisie Shadow Mode` — checkbox; true throughout v0.1 initial calibration.
- `Parent Circuit Breaker Mode` — checkbox.
- `Primary Shadow Selection` — checkbox.
- `Simulated Stake u` — number; 0.25 when a shadow selection exists, otherwise 0.

### Post-match and calibration fields

- `Eventual Result` — single line text.
- `Selection Settlement` — single select: Full Win / Half Win / Push / Half Loss / Full Loss / No Selection / Void.
- `Simulated P/L u` — number.
- `Closing Line` — single line text.
- `Closing Same-Line Odds` — number.
- `Line Movement Quarter Goals` — number where meaningful.
- `Same-Line Price CLV` — number or percent, only when the exact same line is available at close.
- `CLV Classification` — single select: Favorable / Neutral / Adverse / Unavailable.
- `Process Validity` — single select: Valid / Invalid / Review Required.
- `Failure Classification` — single select using the v0.1 failure taxonomy.
- `Review Notes` — multiline text.

## 4. Table: Eredivisie Prior Snapshots

**Granularity:** one record per versioned prior/cohort snapshot.  
**Primary field:** `Prior Snapshot ID`.

This table stores derived calibration outputs, never raw match observations.

### Version and scope fields

- `Prior Snapshot ID` — single line text, primary.
- `Eredivisie Model Version` — single line text.
- `Created At` — dateTime.
- `Season Window` — single line text.
- `Cohort Type` — single select: League / Home-Away / Handicap Band / Total Band / Score State / Minute Band / Promoted Team / Red Card / Other.
- `Cohort Definition` — multiline text.
- `Sample Size Matches` — number.
- `Sample Size Assessments` — number.
- `Active` — checkbox.
- `Review Status` — single select: Experimental / Reviewed / Active / Retired.

### Example prior fields

Store only the fields relevant to the cohort:

- `Home Goals Mean` — number.
- `Away Goals Mean` — number.
- `Draw Rate` — percent.
- `Favorite Win Rate` — percent.
- `Favorite Exactly-One Rate` — percent.
- `Favorite Two-Plus Rate` — percent.
- `Protected Underdog Rate` — percent.
- `First-Half Goal Rate` — percent.
- `Second-Half Goal Rate` — percent.
- `Late Goal Rate` — percent.
- `Comeback Rate` — percent.
- `Estimate Notes` — multiline text.
- `Uncertainty Notes` — multiline text.

At v0.1 creation, no snapshot is automatically active. Numeric priors remain `UNINITIALIZED` until the calibration protocol supports promotion.

## 5. Views recommended for v0.1

Create views rather than separate tables for most review slices:

- `50-Match Run — All Eligible Matches`
- `All Assessments — Including NO BET`
- `PASS Shadow Selections`
- `HOLD Assessments`
- `FAIL Assessments`
- `Protected Underdogs`
- `Deep Favorites`
- `Prematch`
- `Live`
- `Promoted Teams`
- `CLV Available`
- `Process Invalid`
- `Failure Classification`

This preserves a single assessment dataset and avoids review tables that silently omit NO BET outcomes.

## 6. Data-integrity rules

1. Never create an Eredivisie assessment without a verified eligible Eredivisie match record.
2. Never treat the Eredivisie assessment record as satisfying the parent validator write lock; the core `Decision States` record is still required.
3. Never overwrite the original entry line, odds, timestamp or synchronized state with closing or post-match information.
4. Append settlement and closing data after the event.
5. Preserve `NO BET` and `NO BET — HOLD` rows.
6. Do not backfill unsupported probability precision.
7. Closing-line fields must state `Unavailable` rather than being guessed.
8. Model-version fields must preserve the exact parent and Eredivisie versions used at assessment time.
9. A process-valid loss and a process-invalid win must remain distinguishable.
10. `/ledger.json` remains authoritative for official accounting when official betting is enabled and ledger writes are authorized; this calibration schema is not a financial ledger.

## 7. v0.1 implementation recommendation

During the first 50 matches, keep the existing core tables unchanged and add only the three league-layer tables above. This minimizes risk to the parent validator while providing enough normalized data for league priors, assessment-level calibration, NO BET analysis and closing-line review.
