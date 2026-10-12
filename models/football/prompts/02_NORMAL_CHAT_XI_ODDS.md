# 02 — /xi one-match, one-command C + C2 procedure (V4)

**Current authority (2026-10-12):** `FOOTBALL_SIMPLE_ASSESS_AND_BET.md`,
`FOOTBALL_C_C2_ACTIVE_PAIR.md`, `CURRENT_MODEL.md`, C production
and C2 shadow model rules. Do **not** invoke retired V1–V3 packaged
Step0/Step1, Work ZIP or the historical Football A execution compiler.
The previous 574-line technical coordinator is preserved only for audit
in `FOOTBALL_XI_PRE_20261012_COORDINATOR_ARCHIVE.md`.

**ACTIVE MODEL AIRTABLE ROUTING:** Use only
`appbzxqXYf0lKfD4P`; resolve active fields/IDs through
`models/football/airtable/ACTIVE_MODEL_ROUTING.md` and JSON.
Football C official, C2 shadow, C3/C4 retired.
`FOOTBALL_SIMPLE_ASSESS_AND_BET.md` remains the single-command
user contract. Never require a separate /bet, /live or another screenshot
to complete a quote-free football assessment.

## Fast mandatory flow

1. **Resolve match/clock/authority:** identify exact real fixture, canonical
   provider match ID, verified kickoff and assessment epoch, and current
   prematch/started/HT/FT state. Read user-supplied XI/score/event context.
   Use current V4 C/C2 board and its actual frozen separate supported
   burdens if available; if /rank was not completed, an explicit
   `/xi exception` authorizes an independently sourced **EXCEPTION_ONLY**
   assessment, not a fake frozen FOLLOW or retroactive board.
   Routine V4 queue uses `step2_queue_guard.py` mode `V4_ROUTINE`
   with ORIGINAL integrity-checked `v4_sweep_receipt`,
   `v4_rank_receipt` and `v4_persistence_receipt`, plus a complete
   matching C/C2 ranked board. Its `V4_RANK_PERSISTENCE_VERIFIED`
   receipt must originate from independently refetched Airtable.
   Old `work_ready/packaging_complete` are **not V4 authority**.
   STOP/rejected routine cases still require explicit user exception.
2. **Football before market:** one bounded fixture-specific search for
   actual tactical/goal routes, projected or confirmed XI positions,
   injuries and rotation, opponent leakage, finishing and chance quality,
   early goal / third-goal continuation, fourth-goal upper tail, 0–0/1–1
   trap, carrier self-funding, and burden-completion/stall.
   Current cup/knockout/incentive format, table points, draw utility,
   aggregate state and GD margin must be verified when relevant.
   Missing XI or live stats is a stated football limitation, not a
   mandatory bookmaker quotation. Never infer supported burden from
   current market lines. Confirm original frozen supported line separately
   for C and C2; no C2 cloning, no C3/C4.
3. **Use the fast actual portable runtime:** fetch exact-current
   `models/football/engine/xi_portable.py`, run `self-check` once for
   source revision and execute independently frozen C/C2
   `stage=football_assessment` JSON with same match/epoch. Quote
   fields MUST be omitted from this assessment mode. If startup
   requires GitHub source transport, follow the verified artifact
   fast path in `FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md`;
   do not retry broken container DNS or an unnecessary full-repo clone.
   Without genuine C2 evidence or completed deterministic execution,
   report precisely `C+C2 ASSESSMENT INCOMPLETE` instead of guessing.
4. **Only when a real offered price already exists:** freeze separate
   C/C2 `stage=decision` price payloads, using the SAME verified
   football evidence epoch and match. For PREMATCH use the strict
   C/C2 price/market-history (attempt), confirmation and tournament
   recheck; enforce exact quote timestamp, XI authorization,
   supported burden and reachable WAIT. Run the optional
   `--price-c / --price-c2` subdecision in that SAME user /xi turn.
   For STARTED or HT, the prematch priced engine is **forbidden**:
   execute/keep the quote-free live football result and only use a
   truly current separate live-bet authorization where supported.
   A pre-KO screenshot is never executable after kickoff.
5. **Report result first:** output one compact C official and C2 shadow
   football assessment with evidence epoch, risk and supported burdens.
   If no eligible offered quote: `No bet price checked`.
   If quoted priced pair truly executed: C `ACT` / reachable `WAIT`
   / `PASS` and independent C2 shadow action (no actual user bet
   assumed). If price validation fails: `Football assessed — price
   check blocked: <exact reason>`. A bad quote MUST NOT erase
   a successful C+C2 football assessment.
6. **Persist with appropriate safeguard:** genuine football-only execution
   may complete as `EXECUTED_C_C2_FOOTBALL_ONLY` without price,
   bet accounting, Website Pick or priced publication guard.
   Store current `XI Assessment Execution Status` (Airtable field
   `fldkjs6Sykivp0fag`) and BOTH model result JSON records; independently
   read them back and invoke `xi_assessment_reconcile.py` to verify.
   The legacy `Engine Execution Status` field can remain unset for
   football-only; never mark it failed or retroactively alter history.
   Actual **priced** C/C2 decisions require strict current
   `step2_publication_guard.py`, independently refetched quote/record,
   one-publication-per-epoch, and proper WAIT/accounting. Website Picks
   are model suggestions; only user-confirmed slips enter
   `Actual Bets — Current`.

## Execution syntax (one user command)

```bash
# Always start with actual independent football inputs
python models/football/engine/xi_portable.py xi --c c_football.json --c2 c2_football.json

# Add available exact/current PREMATCH line+odds without a new user command
python models/football/engine/xi_portable.py xi \
  --c c_football.json --c2 c2_football.json \
  --price-c c_priced.json --price-c2 c2_priced.json

# Only after separate actual Airtable write and new independent refetch:
python models/football/engine/xi_assessment_reconcile.py \
  --receipt xi_result.json --readback airtable_refetched.json
```

The new runner **executes football first**. Failure of the separate
price subdecision returns `FOOTBALL_ASSESSED_PRICE_CHECK_BLOCKED`
with both complete football results; it does not silently convert
price failure into C-PASS. Old `stage=decision` under `--c/--c2`
remains available to historical price-only callers but is labelled
`LEGACY_PREMATCH_PRICE_CHECK`, NOT a completed football-first run.

## User-facing labels are presentation, not new model thresholds

- `FOOTBALL_THESIS_CURRENTLY_INTACT`: thesis intact; use `FOCUS`
  only if that **model's own** frozen board was actually FOCUS and
  the supported burden remains funded. Otherwise say `CURRENTLY INTACT`.
- `FOOTBALL_ANALYSIS_WITH_EXPLICIT_RECHECKS`: `CAUTION —
  <specific missing/recheck>`, not unconditional PASS or ACT.
- `FOOTBALL_THESIS_ADVERSE`: `AVOID — <failure>`.
- No genuine independent C or C2 payload: `NOT ENOUGH VERIFIED
  EVIDENCE / ASSESSMENT INCOMPLETE`. Never manufacture C2.
- ACT/WAIT/PASS are **priced C/C2 engine actions only**, not
  mere qualitative goals predictions or evidence that a wager was placed.

## Non-negotiable safety / provenance

Never derive live odds from frozen burden, present stale pricing
as current, backfill a skipped prematch wager after kickoff, claim
that optional diagnostic probability estimates are market value,
or reinterpret C2 shadow as real exposure. Persist the original
frozen epoch and exact current event/quote evidence. Post-XI
source checks are mandatory for a final priced bet; a failed,
genuinely attempted source check is explicitly LIMITED, never FOUND.
Incomplete verified tournament incentive blocks a **priced action**,
not the existence of a football discussion. Technical status and
football PASS must always remain separate. Session due-set accounting
applies to routine scheduled boards, not as an additional global
obstacle to one authorized exception.
