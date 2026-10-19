# Football C G4 evidence disposition

This prospective contract changes evidence completeness and explanations, not
the predictive predicates in `engine/core.py`. Historical receipts are immutable.

An explicit completed G4 declaration must carry:

- Upper-tail transferability and comparable-context signal, each with its basis.
- `g4_path_evidence`, keyed by `g4_carrier_path`, `g4_distributed_path`,
  `g4_reply_path`. Each record has a nonempty `basis` and `evidence_refs`.
- Every FAILED path references `mechanism_ids` in `failure_mechanisms`. Each
  mechanism has basis, evidence references, kind and `affected_paths`.
  `OPPONENT_REPLY_ONLY` cannot alone establish carrier failure.
- `grade_evidence` for route reliability, continuation quality, burden stall
  risk, failure resistance and independent upper tail. HIGH stall risk must
  reference an identified mechanism. Reuse a causal ID when the same mechanism
  affects several grades; do not narrate these as independent observations.
- If a path is SUPPORTED but G4 is rejected, `g4_global_blockers` must contain
  evidence records with a `condition` emitted by `certificate_diagnostics`.

UNAVAILABLE is not FAILED. Missing proof becomes G4_RESEARCH_INCOMPLETE;
documented unavailable paths become G4_RESEARCH_EVIDENCE_LIMITED. Resolved but
mixed evidence uses G4_RESEARCH_COMPLETE_MIXED, distinct from a supported
negative conclusion. Pending rows remain resumable and cannot silently finalize
a G3-only FOCUS board row. Complete mixed evidence may retain G3 support but
must receive the same material-disagreement recheck as complete rejection.

The existing inferred-funded legacy path stays readable. New research should
use explicit status and provenance. No status, rate, market quote or evidence
reference itself creates G4: the unchanged compiler remains authoritative.
Evidence references must resolve to the actual prospective source snapshot;
the runtime validates their structure, not the truth of the research narrative.

XI must consume the native result. It cannot replace missing research with a
manual ACT/WAIT/PASS. Complete claims with evidence gaps cannot issue a priced
decision. Source-backed VERIFIED_PRIOR_CERTIFICATE_MISCLASSIFICATION remains
available; market disagreement alone cannot create a certificate.

Production scope is checked against the V4 league registry at board and XI
price boundaries. Country, competition and competition kind are required and
rank binds them to the original frozen source. Non-Japan domestic women remain
excluded; the Japan women's exception remains. Explicit user exceptions are
labeled out-of-scope analysis and do not silently enter production ranking or
execution. Quote-free football analysis can still complete with that label.

Compiler diagnostics expose actual funding, robustness, branch requirements,
and shared failure mechanisms. They explain the current rule; they do not
reweight risk, change rank sorting, or certify that structural calibration is
statistically solved.
