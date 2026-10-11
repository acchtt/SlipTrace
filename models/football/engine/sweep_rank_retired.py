"""Current Football-v2 Step0/Step1 production workflow retirement.

The user retired BOTH /sweep and /rank on 2026-10-11. This policy is
intentionally independent of previous run dates or old model/market data.
Historical pure validators remain importable for audits; none of them
authorizes new production discovery, packaging or board publication.

Only an explicit subsequent user-approved replacement may reactivate these
stages through a reviewed change to the current main branch.
"""
from __future__ import annotations

import json
import sys

RETIRED_STATUS = "SWEEP_RANK_RETIRED"
ACTIVE_SWEEP_RANK_ENABLED = False
RETIRED_COMMANDS = frozenset({
    "/sweep", "/sweep resume", "/sweep repair", "/rank", "/rank reassess"
})
REASON = (
    "The user retired production /sweep and /rank. No new Step0 runs, "
    "resumes, final source ZIPs, C/C2 Step1 boards, or publication are authorized. "
    "Historical evidence and independent /xi and /live remain available."
)


def retirement_receipt(stage: str) -> dict[str, object]:
    if not isinstance(stage, str) or not stage.strip():
        raise ValueError("retired stage name missing")
    return {
        "status": RETIRED_STATUS,
        "stage": stage,
        "production_enabled": False,
        "may_resume_old_run": False,
        "may_issue_official_zip": False,
        "may_publish_rank": False,
        "retirement_reason": REASON,
        "reinstatement": "REQUIRES_NEW_USER_APPROVED_WORKFLOW",
    }


def stop_retired_cli(stage: str) -> int:
    print(json.dumps(retirement_receipt(stage), indent=2, sort_keys=True),
          file=sys.stderr)
    return 2
