"""Prospective V4 source recovery; never promote Airtable reconstructions."""
from __future__ import annotations
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
sys.path.insert(0,str(ROOT.parent / "engine" / "tests"))
from replay_unattested import replay
from stage import StageError, _hash, rank

RUN=ROOT/"recovery"/"V4-20261012-003037-0600"

def inputs():
    return json.loads((RUN/"source.json").read_text(encoding="utf-8")),json.loads(
        (RUN/"intake-unattested.json").read_text(encoding="utf-8"))


class ReplayUnattestedV4(unittest.TestCase):
    def test_exact_original_source_replay_creates_genuine_stage_receipt(self):
        source,derived=inputs()
        result=replay(source,derived)
        self.assertEqual(result["status"],"V4_SWEEP_READY")
        self.assertEqual(result["run_id"],"V4-20261012-003037-0600")
        self.assertEqual(result["fixture_count"],12)
        self.assertEqual(result["eligible_count"],5)
        self.assertNotEqual(result["integrity_sha256"],derived["integrity_sha256"])
        self.assertTrue(result["source_ledger_hash"])
        self.assertFalse(result["published"])
        self.assertFalse(result["bet_recorded"])

    def test_altered_original_source_cannot_promote_derived_intake(self):
        source,derived=inputs()
        source["fixtures"][3]["home"]="Different Team"
        with self.assertRaisesRegex(StageError,"does not match actual V4 engine"):
            replay(source,derived)

    def test_altered_derived_state_cannot_promote(self):
        source,derived=inputs()
        derived["eligible_queue"][0]["kickoff_utc"]="2026-10-11T22:30:00+00:00"
        with self.assertRaisesRegex(StageError,"derived intake integrity digest"):
            replay(source,derived)
        source,derived=inputs()
        derived["eligible_queue"][0]["kickoff_utc"]="2026-10-11T22:30:00+00:00"
        derived["integrity_sha256"]=_hash({k:v for k,v in derived.items() if k!="integrity_sha256"})
        with self.assertRaisesRegex(StageError,"does not match actual V4 engine"):
            replay(source,derived)

    def test_unattested_input_blocks_rank_early(self):
        _,derived=inputs()
        with self.assertRaisesRegex(StageError,"V4_ATTESTATION_REQUIRED"):
            rank(derived,{}, {},{},now="2026-10-11T17:40:00Z")

    def test_attested_old_fixture_cannot_be_ranked_retroactively(self):
        source,derived=inputs()
        confirmed=replay(source,derived)
        from test_board_pair import c_row,c2_row,payload
        x=c_row();y=c2_row()
        for row in (x,y):
            row["match_id"]="SPORTSCORE-6ypq3nhv9dn7md7"
            row["kickoff_ict"]="2026-10-12T01:00:00+07:00"
        other={mid:"PREMATCH_WINDOW_CLOSED" for mid in confirmed["research_order"]
               if mid!=x["match_id"]}
        with self.assertRaisesRegex(StageError,"retroactive prematch"):
            rank(confirmed,payload("c",x),payload("c2",y),other,
                 now="2026-10-11T18:20:00Z")


if __name__=="__main__":
    unittest.main()
