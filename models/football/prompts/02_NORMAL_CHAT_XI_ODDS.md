# /xi — Football C + C2 assessment

**Command alias:** /xi  
**Exception alias:** /xi exception

## Active roster

- Football C = official.
- Football C2 = shadow only.
- C3/C4 are retired for new work.

Use the thin shared runtime:

python models/football/engine/xi_portable.py xi --c c_football.json --c2 c2_football.json

Odds are not required to complete the football assessment.

## 1. Establish authority

### Routine V4 match

Load the verified V4 rank receipt, the matching
V4_RANK_PERSISTENCE_VERIFIED receipt and the exact ranked board row.

Run step2_queue_guard.py with schema football-step2-queue-v2.

Do **not** carry the original sweep source/status payloads into /xi and do not
replay Step 1 again. Step 1 already performed source replay, fresh status
verification, C/C2 execution and exact Airtable readback.

### /xi exception

An explicit user exception can be assessed without routine board authority.
Research/freeze independent C and C2 evidence from the current match epoch.

Do not manufacture a prematch decision after kickoff.

## 2. Research current football state

Assess current football evidence first:

- actual fixture status/kickoff;
- XI/team-news/mechanism state when available;
- current routes/carrier/chance/failure evidence;
- H2H only when materially transferable/corroborated;
- tournament format/incentive state when applicable;
- current score/minute/material event after kickoff;
- model-specific WAIT reachability when a decay plan is plausible.

C2 model-owned leakage evidence must remain independent from C. When current
C2 leakage is used, freeze both c2_opponent_leakage and a non-empty
c2_opponent_leakage_basis. Otherwise omit both.

For WAIT research, record independently for each model:

- wait_reachable = true/false;
- wait_reachability_basis when true;
- wait_requires_negative_info = true/false;
- wait_negative_info_basis when material;
- top_ranked_focus when relevant.

A missing/unproven reachability assessment must not be converted into WAIT.

## 3. Execute football assessment

Run both independent stage=football_assessment payloads.

A successful result is:

EXECUTED_C_C2_FOOTBALL_ONLY

This is a complete football assessment even when no price exists.

Do not ask the user for odds to finish football analysis.

## 4. Optional observed quote / screenshot

If the user supplied a screenshot, use **only that screenshot's exact line and
odds**.

Rules:

- evidence_mode = USER_SCREENSHOT_ONLY;
- source = USER_SCREENSHOT;
- preserve the original capture reference/time when known;
- never search for a replacement bookmaker quote;
- never overwrite capture time with analysis time;
- never request a fresh screenshot merely because processing took time.

The runtime calls adapter.evaluate_observed_quote() independently for C and C2.
That function reuses the exact same pure quote-policy functions used by strict
run_decision().

Therefore the screenshot may yield conditional model ACT / WAIT / PASS.

But screenshot/observed-price evaluation always has:

- execution_authorized = false;
- publication_authorized = false;
- model_exposure_created = false;
- no Actual Bet.

A screenshot cannot independently prove the offer remains executable.

Persist a successful observed comparison using the normal evaluated line/odds
fields plus the regular C/C2 assessment readback. Do not serialize a separate
screenshot receipt into Evidence Summary.

## 5. WAIT

WAIT comes only from core model policy.

Never use a wrapper-specific fixed decay-gap threshold.

For a healthy WAIT:

- the football thesis/mechanism remains intact;
- no material veto remains;
- wait_reachable=true is supported by current research;
- wait_requires_negative_info=false.

The deterministic target/minimum price is returned by the core policy:

- target = the applicable protected/model-supported burden;
- normal minimum price = 1.65;
- top-ranked FOCUS soft-zone minimum = 1.60 where permitted by the core.

A WAIT is a plan only. It creates no assumed exposure.

If a goal, red card, major injury or material tactical/route change occurs,
reassess the current football state before acting.

## 6. Optional strict executable price decision

Only when a genuinely current executable prematch quote and all strict current
evidence already exist, run independent stage=decision C and C2 payloads in the
same /xi turn.

The strict decision path adds execution authorization around the same model
quote policy. It does not replace the football assessment.

If the strict price gate fails, keep and report the completed football result.
Do not turn it into an engine failure.

If the strict pair succeeds:

1. persist the Decision State once;
2. independently refetch once;
3. immediately before official publication verify the pair receipt/readback,
   current evidence epoch, fixture state and executable quote using
   step2_publication_guard.py.

C2 is shadow-only and cannot create Website Picks.

## 7. Started match / live state

When kickoff has passed, keep running the same C/C2 football assessment with
the actual score/minute/events.

Do not recreate a prematch ACT/WAIT/PASS.

A user live screenshot may be compared to the frozen burden as current
information, but it does not become a prematch executable action.

There is no separate active kickoff-transition router.

## 8. Result-first response

Give the user the useful verdict first.

For each model show:

- C official football state and supported line;
- C2 shadow football state and supported line;
- if a quote was supplied: conditional ACT / WAIT / PASS;
- for WAIT: target line, minimum odds and reachability basis;
- any current material blocker/recheck.

Then state execution status:

- observed screenshot only -> conditional, non-executable;
- verified strict price pair -> eligible for persistence/publication checks;
- no price -> No bet price checked.

Never invent a price, frozen line, lineup or bet.

## 9. Persistence/accounting

Persist/refetch the active Decision State once when required.

WATCH and unresolved WAIT are not model bets.

Physical user profit/loss is read only from confirmed Actual Bets — Current
rows. Do not infer a user bet from C action, Website Pick, screenshot or WAIT.
