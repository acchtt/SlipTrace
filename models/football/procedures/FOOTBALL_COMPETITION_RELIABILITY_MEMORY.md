# Football Competition Operational Reliability Memory

**Status:** mandatory persistent Step-0 memory  
**Scope:** operational observability only — never predictive football quality  
**Airtable summary:** `Competition Reliability` (`tbl1KShXxXErUdVKW`)  
**Airtable events:** `Competition Reliability Events` (`tblD0ZHqT772H25Uv`)

**Activation boundary:** prospective from the merge that activates this procedure.

## 1. Purpose

Prevent the same competitions from repeatedly consuming board capacity when they repeatedly fail operationally near kickoff.

This memory may use only execution-observability evidence:

- usable confirmed/reliable XI availability;
- executable Asian-total market availability;
- usable team-news availability;
- fixture identity/time integrity;
- whether required Step 2 could actually be completed.

It must **never** use:

- FT score;
- total goals;
- Over/Under settlement;
- C/C2 prediction result;
- betting P/L;
- whether a skipped match would have won.

Competition reliability is therefore separate from `FOOTBALL_LEAGUE_ENVIRONMENT_REGISTRY.md`.

## 2. Activation / no-backfill boundary

Do not manufacture historical reliability events from older boards that did not persist the required operational channels consistently.

Older notes may explain why this system was added, but they do not count toward the rolling classifier unless the exact XI/market/team-news/identity/Step-2 operational state was prospectively frozen under this contract.

Therefore a competition with no compliant post-activation events starts `UNPROVEN`.

This prevents outcome-aware or incomplete retrospective backfill.

## 3. Append-only reliability events

Post-slate audit owns the canonical event write.

Create at most one canonical reliability event per board fixture/operational epoch using a stable `Event ID`.

Countable observations are:

- `STEP2_OBSERVED`;
- `SCHEDULE_INTEGRITY`.

`PREFLIGHT_OBSERVED` may be stored for diagnosis but does not by itself improve or degrade the rolling reliability state.

Outcome fields:

- XI: `USABLE / LATE / MISSING / NOT_CHECKED`;
- market: `USABLE / THIN / STALE_OR_VANISHED / UNAVAILABLE / NOT_CHECKED`;
- team news: `USABLE / LIMITED / UNAVAILABLE / NOT_CHECKED`;
- identity/time: `CLEAN / FAULT / NOT_CHECKED`;
- Step 2: `COMPLETED / BLOCKED_XI / BLOCKED_MARKET / PROCESS_MISSING / NOT_SELECTED / NOT_APPLICABLE`.

Critical failures are:

- XI = MISSING;
- market = STALE_OR_VANISHED or UNAVAILABLE;
- identity/time = FAULT;
- Step 2 = PROCESS_MISSING.

Do not mark a fixture critical merely because it was C-PASS, lost, finished low-scoring, or had unattractive odds.

## 4. Rolling memory

Evaluate the **latest 10 countable observations** for a normalized competition key.

Metric denominators ignore `NOT_CHECKED` / `NOT_APPLICABLE`.

- XI usable rate = USABLE / (USABLE + LATE + MISSING).
- Market usable rate = USABLE / (USABLE + THIN + STALE_OR_VANISHED + UNAVAILABLE).
- Team-news usable rate = USABLE / (USABLE + LIMITED + UNAVAILABLE).
- Step-2 completion rate = COMPLETED / (COMPLETED + BLOCKED_XI + BLOCKED_MARKET + PROCESS_MISSING).
- Identity/time faults = FAULT count in the rolling sample.
- Consecutive critical failures = critical events from the newest observation backward until the first clean event.

Use `models/football/engine/competition_reliability.py` as the deterministic classifier.

## 5. Reliability states

### UNPROVEN

Fewer than 3 countable observations.

No historical promotion or demotion. Current fixture evidence decides the A/B/C/D grade.

### TRUSTED

Requires at least 5 countable observations and enough checked channels.

All of the following must hold:

- XI usable >= 85%;
- market usable >= 85%;
- team-news usable >= 70%;
- Step-2 completion >= 85%;
- zero identity/time faults;
- zero current consecutive critical failures.

TRUSTED does **not** promote a weak current fixture. It only means history imposes no cap.

### NEUTRAL

No trust qualification and no caution/demotion trigger.

Current fixture evidence decides normally.

### CAUTION

With at least 3 countable observations, trigger CAUTION when a sufficiently observed channel shows:

- XI usable < 75%; or
- market usable < 75%; or
- team-news usable < 60%; or
- Step-2 completion < 75%; or
- at least one identity/time fault; or
- at least two consecutive critical failures.

A rate trigger requires at least 3 checked observations in that channel.

CAUTION caps a current A fixture to **B**. It never promotes anything.

### DEMOTED

With at least 4 countable observations, trigger DEMOTED when:

- XI usable < 50%; or
- market usable < 50%; or
- Step-2 completion < 50%; or
- at least two identity/time faults; or
- at least three consecutive critical failures.

A rate trigger requires at least 3 checked observations in that channel.

Normal DEMOTED treatment is **C / operational exclusion**.

## 6. Recovery / probation

DEMOTED is not a permanent blacklist.

A DEMOTED competition may receive **one B-grade probation fixture per sweep** only when the current fixture independently satisfies the full raw A-grade operational preflight:

- XI expected = YES;
- market observability = HIGH;
- team-news observability = HIGH or MEDIUM;
- identity/time clean;
- researchability clears.

The historical state prevents routine FOLLOW, so probation remains max B/RESERVE.

The post-slate event from that probation fixture then enters the rolling sample. Repeated clean observations can move the competition back to CAUTION/NEUTRAL/TRUSTED naturally.

A user-declared exception may also reopen a fixture, but does not waive any other integrity gate.

## 7. Step-0 application order

For each discovered senior fixture:

1. normalize the competition key;
2. retrieve the current Airtable `Competition Reliability` row;
3. calculate raw current A/B/C/D viability from current evidence;
4. apply the persistent reliability cap;
5. persist the reliability-state snapshot and reason into Daily Coverage Ledger;
6. continue researchability and 15-fixture capacity gating.

History may only **cap/demote** the current raw grade. It may never promote C->B, B->A, or replace current evidence.

Manual Override in Airtable applies only when it reflects an explicit user/maintainer decision. `NONE` is the normal state.

## 8. Audit update

After the slate:

1. append/upsert canonical operational events without FT/predictive data;
2. load the latest 10 countable events per observed competition;
3. run the deterministic classifier;
4. upsert the summary row:
   - Reliability State;
   - Rolling Sample;
   - XI Usable %;
   - Market Usable %;
   - Team News Usable %;
   - Step2 Completion %;
   - Identity Time Faults;
   - Consecutive Critical Failures;
   - Last Observed At;
   - State Reason;
   - Updated At;
5. preserve Manual Override unless explicitly changed by the user.

No retroactive mutation of historical board states.

## 9. Invariant

The operational-memory question is:

> Can we reliably observe and execute this competition?

It is never:

> Does this competition produce enough goals to bet Overs?
