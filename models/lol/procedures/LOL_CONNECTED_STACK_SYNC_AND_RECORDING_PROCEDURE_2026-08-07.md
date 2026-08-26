# LoL Connected Stack Sync and Recording Procedure

**Status:** Mandatory active procedure  
**Effective:** 2026-08-07 16:39 UTC+7  
**Applies to:** all LoL pregame, live, shadow-circuit-breaker, settlement, review, and cross-chat continuation work  
**Authority:** supplements the active LoL model and procedures; GitHub remains the rules/policy authority

## 1. Purpose

Prevent decision drift, stale tracker state, false recorded positions, and cross-chat accounting errors by requiring explicit separation between:

- current live evidence;
- analytical verdict/thesis;
- recorded position state;
- tracker synchronization;
- settlement evidence;
- calibration/review state.

This procedure was added after an audit found that GitHub was current while Airtable and the Google calibration workbook had fallen behind, and chat responses sometimes described conditional leans as recorded positions.

## 2. Connected analytical stack and authority

### A. Live evidence

The current synchronized screenshot, current odds screenshot, and explicit user correction are the primary sources for the live map state.

A newer explicit user correction overrides stale telemetry. A verified final/result screen overrides earlier live-state telemetry for settlement.

### B. GitHub — authoritative rules and operating state

Repository: `acchtt/SlipTrace`.

GitHub is authoritative for:

- active model version;
- model rules and procedures;
- circuit-breaker requirements;
- official probation and stake policy references;
- cross-chat handoffs;
- reviewed/corrected accounting summaries.

GitHub is not a substitute for current live telemetry.

### C. Airtable — mandatory live structured tracker

Base: `SlipTrace LoL Live Tracker`.

Tables:

- `Maps` — one record per tracked circuit-breaker map;
- `Snapshots` — synchronized live states used in analysis;
- `Positions` — exact shadow entries and settlements.

Airtable is the required operational record for whether a shadow position is actually **recorded**.

### D. Google Drive / Sheets — calibration mirror

Workbook: `SlipTrace LoL Calibration Workbook` in `SlipTrace LoL Model Lab`.

Sheets are the calibration/review mirror, not the critical-path live verdict source. They should be synchronized after settlement/review and used to check longer-run calibration patterns.

If Google Sheets is stale or temporarily unavailable, do not delay a live verdict, but state that calibration synchronization is pending.

## 3. Mandatory startup sync audit in every new chat

After loading the required GitHub files and before treating historical tracker state as current:

1. inspect the latest Airtable `Maps` and `Positions` records;
2. inspect the latest relevant rows in the calibration workbook;
3. compare both with `models/lol/CURRENT_MODEL.md` and the latest handoff;
4. identify the latest common completed map and latest recorded position;
5. if Airtable or Sheets is behind GitHub, explicitly label it `TRACKER LAG` and do not quote the stale tracker as current truth;
6. if a live map requires an immediate verdict, give the verdict first from synchronized live evidence plus GitHub rules, then complete the audit immediately afterward.

Do not say or imply that the connected stack is synchronized unless the relevant sources were actually checked.

## 4. Mandatory live-decision sequence

For every synchronized live decision:

1. **VERDICT FIRST** — apply the active model to the current screenshot/user correction and current line.
2. Keep the response compact enough not to delay live action.
3. After the verdict, log the synchronized state to Airtable `Snapshots` when it materially informed a decision, invalidation, or settlement.
4. If a shadow lean is promoted to an entry, write the exact position to Airtable `Positions` with:
   - map ID;
   - market family;
   - exact selection/line;
   - exact odds;
   - simulated stake;
   - actual exposure (`0u` during the circuit breaker);
   - entry clock or `Pregame`;
   - entry-time evidence;
   - thesis state.
5. Do not perform repository maintenance before the verdict.

## 5. Recorded-position gate

The following states must be distinguished explicitly:

- `WATCH` — not an entry;
- `CONDITIONAL LEAN / UNRECORDED` — analytical lean exists, but price/state confirmation or tracker write is missing;
- `RECORDED SHADOW POSITION` — the exact entry exists in Airtable `Positions`;
- `RECORDED POSITION — THESIS ACTIVE/DEGRADED/INVALIDATED` — recorded state is immutable except for correction; analytical thesis may change;
- `SETTLED` — result verified and the position record updated.

**Critical rule:** a chat recommendation, conditional lean, or statement such as `shadow 0.25u` does **not** by itself create a recorded position.

A position counts toward shadow record/P&L only if the exact entry was actually recorded in Airtable or the user explicitly confirms placement/recording and the tracker is then synchronized.

If the tracker write was not completed, never later refer to the position as `recorded` merely because it was discussed earlier.

## 6. Price synchronization gate

When a lean depends on a quoted price:

- the exact odds used for the decision must come from the current synchronized odds state;
- if the odds are stale or the recommendation is explicitly conditional on the price holding, the state remains `CONDITIONAL / UNRECORDED`;
- do not backfill an assumed entry price after the market moves;
- a later screenshot cannot retroactively validate an earlier unrecorded price unless the user explicitly confirms that exact entry was taken/recorded at that price.

## 7. Settlement and correction sequence

A map/result market may be settled only from valid settlement evidence under the scoreboard protocol. A mathematically determined prop may be graded earlier only when its outcome is truly fixed by a verified live state.

After verified settlement:

1. update the Airtable `Positions` record result and simulated P/L;
2. update the Airtable `Maps` record with final winner, duration, kills, review state, and primary error when applicable;
3. synchronize the corresponding Google Sheets calibration rows;
4. update GitHub operating/accounting summaries when the map materially changes the circuit-breaker state or creates a process correction;
5. only after final-state verification plus review may the map count as complete for circuit-breaker progress.

If later verified evidence or an explicit user correction conflicts with a prior settlement:

- reverse the incorrect settlement/accounting;
- update every affected tracker/source;
- record the correction rather than silently overwriting history;
- use the corrected final state as authoritative for future analysis.

## 8. Discrepancy hierarchy

For **live/final factual state**, use the strongest current evidence in this order:

1. explicit user correction tied to the current map/result;
2. verified final/result screen;
3. newer synchronized live screenshot;
4. older synchronized live screenshot;
5. Airtable/Sheets copies of those observations.

For **rules and policy**, GitHub is authoritative.

Never allow a stale tracker row to override a newer verified live/final state. Never allow an old handoff status to override a newer GitHub correction.

When two current telemetry sources are chronologically incompatible, label the state conflict and do not settle from the inconsistent pair until resolved.

## 9. Plugin/tool availability fallback

If Airtable or Google Drive cannot be accessed in a session:

- continue live analysis using synchronized screenshots/user corrections plus GitHub rules;
- explicitly state `TRACKER SYNC PENDING`;
- do not claim the stack is synchronized;
- do not call an unpersisted lean `recorded`;
- reconcile the missing tracker writes when access returns.

Tool availability must never be fabricated or implied from historical context alone.

## 10. Cross-chat handoff requirement

Every new handoff must include:

- active model/version;
- circuit-breaker progress;
- authoritative shadow record/P&L;
- open recorded positions, if any;
- conditional/unrecorded leans separately, if still relevant;
- latest synchronized map state;
- Airtable synchronization status;
- Google Sheets synchronization status;
- any known tracker lag or unresolved discrepancy.

The handoff must never collapse `conditional lean`, `recorded position`, and `current thesis` into one status.

## 11. Current audit correction that triggered this procedure

The 2026-08-07 audit found:

- GitHub was current through corrected shadow map 8;
- Airtable was only populated through map 5;
- the Google calibration workbook was further behind;
- the KT +7.5 Game 2 lean was discussed conditionally but never validly recorded.

Therefore that KT +7.5 lean is **not** part of shadow P/L. Future chats must load this procedure to prevent the same state-transition error.

## 12. Non-negotiable operating summary

**Verdict first. Evidence synchronized. Tracker write second. Only an actual tracker entry is recorded. Settlement requires verified evidence. GitHub governs rules. Discrepancies are surfaced, never silently reconciled.**

## 13. Independent Total-Kills and Duration market handling

Effective 2026-08-07, `Total Kills` and `Duration` are separate betting/analysis market families.

- Evaluate Total Kills on its own kill-inventory, fight-frequency, objective-density, comeback-shape, and reserve requirements.
- Evaluate Duration on its own structure-conversion, terminal-route, stall/anti-conversion, fast-close-branch, and duration-buffer requirements.
- A Total-Kills position or thesis must **not** automatically block a Duration position or thesis merely because both are same-map props.
- A Duration position or thesis must **not** automatically block a Total-Kills position or thesis merely because both are same-map props.
- Side moneyline and kill-handicap exposure does not suppress analysis of Total Kills or Duration; each market family receives an independent verdict.
- Correlation may still be discussed as a risk characteristic, but correlation alone is not a veto between Total Kills and Duration.
- Each market family may have its own Airtable `Positions` row if it independently clears its model gates and recording requirements.
- **Exposure policy is separate from market-family classification.** Unless the active stake policy is explicitly changed, the existing aggregate per-map exposure cap remains in force. Independent classification does not silently raise the map exposure ceiling.

Future chats must therefore distinguish `independent market verdict` from `additional stake permitted under the current exposure cap`.

## 14. Live-response brevity without analytical shortcuts

Effective 2026-08-07, live responses should default to a **brief operational format** so the user can act quickly.

- Brevity is a presentation rule only. It must **never** reduce, skip, or weaken any active model rule, procedure gate, price check, evidence check, market-family evaluation, dominance override, settlement rule, or tracker requirement.
- Run the full applicable analysis first; expose only the minimum decision-relevant output unless the user asks for detail or a review is required.
- Default live format: **VERDICT first**, then one compact reason/state line, then recording status when relevant.
- When multiple market families are visible, concise labels such as `SIDE/HANDICAP`, `KILLS`, and `TIME` may be used so each still receives an independent verdict without long prose.
- Do not repeat draft explanations, historical context, probability derivations, or rule text unless they materially changed the current verdict.
- `NO LEAN`, `HOLD`, `WATCH`, `RECORD`, `INVALIDATED`, and `SETTLED` should be stated explicitly and briefly.
- Corrections, process reviews, or disputed settlements may be longer because auditability takes priority over brevity.
- Tool/tracker writes remain **after the verdict** and must not delay the live answer.

**Compact output must never mean compact reasoning. The active model and all mandatory rules remain fully binding.**

## 15. User map-end Airtable batching override — 2026-08-26

**Status:** Active immediately for this project/user workflow. This section supersedes Sections 3–7 and any older procedure/addendum language requiring Airtable writes during an active map.

### Core rule

**Do not call Airtable during a live map. Airtable persistence happens only after the map ends.**

During an active map:

- prioritize live verdict latency;
- keep all material synchronized snapshots in an in-chat/session buffer;
- keep every qualified shadow TAKE in the same buffer with exact market, line, odds, entry clock, gate signature/evidence, simulated stake, actual exposure, and visible opposite-side benchmark when available;
- keep invalidations, corrections, line-expiry events, and process incidents in the buffer;
- do not create/update `Maps`, `Snapshots`, `Positions`, roster tables, or any other Airtable table mid-map;
- do not run Airtable startup/audit calls in the middle of live decision flow if a map is already underway.

At verified map end:

1. write/update the `Maps` record;
2. batch-write all material buffered `Snapshots`;
3. batch-write every qualified TAKE as a `Positions` row, including settlement when already known;
4. write any required roster/canonical metadata updates;
5. verify the exact written rows;
6. only then clear the buffer.

### Buffered shadow-position semantics

A qualified live `TAKE` still becomes a **model-attributed shadow entry at the moment of the verdict** when the execution/freshness gates pass. Physical Airtable persistence is intentionally deferred until map end.

Before map-end persistence, describe it as:

`BUFFERED SHADOW POSITION — pending map-end Airtable batch`

Do not call a merely discussed lean or an expired/missed line a buffered position. Only an actual qualified `TAKE` gets buffered as an entry.

If a line disappears before the qualified TAKE is delivered, it is **not** a position and must not be backfilled. Log it as an execution/process miss when appropriate.

### Latency precedence

No connector call, tracker audit, record write, repository maintenance, or synchronization bookkeeping may delay a live verdict. The required order is:

`READ SYNCHRONIZED EVIDENCE -> RUN MODEL GATES -> VERDICT -> BUFFER -> CONTINUE LIVE ANALYSIS -> MAP END -> AIRTABLE BATCH/VERIFY`

### User screenshot provenance interaction

For this workflow, same-message scoreboard + sportsbook screenshots are presumed synchronized unless there is a substantive game-state contradiction or the user explicitly marks one stale. Bookmaker/header/feed clock differences alone do not justify a sync HOLD.

Logged calibration incident: KT Rolster vs HANJIN BRION Game 2 on 2026-08-26. A false synchronization HOLD delayed the BRO +11.5 @1.998 verdict until the line disappeared. Future handling must trust same-message provenance and avoid tracker/tool work until map end.