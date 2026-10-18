"""Normal-chat V4 source-only acquisition.

Acquire and persist one complete canonical source epoch plus the native listing
receipt. Do not perform goal-history research and do not emit a rank handoff.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import work_sweep


def run(request_path: Path, output: Path) -> int:
    if output.exists() and any(output.iterdir()):
        raise ValueError("output must be fresh")
    output.mkdir(parents=True, exist_ok=True)
    request = json.loads(request_path.read_text(encoding="utf-8"))
    start, end, _ = work_sweep.parse_request(request)
    if end <= work_sweep.stamp(work_sweep.utcnow()):
        raise ValueError("REQUEST_WINDOW_EXPIRED")
    evidence = work_sweep.Evidence(output)
    source = work_sweep.acquire(request, evidence)
    work_sweep.save(output / "original-source.json", source)
    work_sweep.save(output / "source.json", source)
    receipt = work_sweep.sweep(source, now=work_sweep.utcnow())
    work_sweep.save(output / "listing-receipt.json", receipt)
    order = list(dict.fromkeys(
        receipt.get("priority_research_order", []) +
        receipt.get("goal_research_order", [])
    ))
    checkpoint = {
        "schema_version": "football-v4-sweep-research-checkpoint-v2",
        "status": "SOURCE_READY_FOR_RESEARCH",
        "run_id": source["run_id"],
        "window_start_utc": source["window_start_utc"],
        "window_end_utc": source["window_end_utc"],
        "original_source_sha256": work_sweep.digest(output / "original-source.json"),
        "source_file_sha256": work_sweep.digest(output / "source.json"),
        "native_listing_receipt_integrity_sha256": receipt["integrity_sha256"],
        "research_order": order,
        "resume_queue": order,
        "fixtures": {},
        "completed_research_count": 0,
        "pending_research_count": len(order),
        "resume_generation": 0,
        "native_v4_sweep_ready": False,
        "rank_handoff_ready": False,
        "next_action": "Normal chat researches only resume_queue and checkpoints every <=4 dispositions.",
    }
    work_sweep.save(output / "checkpoint.json", checkpoint)
    return 0


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--request", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    try:
        return run(args.request, args.output)
    except Exception as exc:
        print(f"NORMAL_SOURCE_ACQUISITION_FAILED: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
