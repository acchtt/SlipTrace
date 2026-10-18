import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from models.football.stages_v4.tools import normal_source
from models.football.stages_v4.test_source_completeness import source, NOW


class NormalSourceTests(unittest.TestCase):
    def test_source_only_persists_before_research(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            src=source()
            request={
                "run_id":src["run_id"],
                "window_start_ict":src["window_start_utc"],
                "window_end_ict":src["window_end_utc"],
            }
            (root/"request.json").write_text(json.dumps(request))
            with patch.object(normal_source.work_sweep,"utcnow",return_value=NOW), \
                 patch.object(normal_source.work_sweep,"acquire",return_value=src):
                self.assertEqual(normal_source.run(root/"request.json",root/"out"),0)
            cp=json.loads((root/"out/checkpoint.json").read_text())
            self.assertEqual(cp["status"],"SOURCE_READY_FOR_RESEARCH")
            self.assertFalse(cp["native_v4_sweep_ready"])
            self.assertFalse(cp["rank_handoff_ready"])
            self.assertTrue((root/"out/original-source.json").exists())
            self.assertTrue((root/"out/source.json").exists())
            self.assertTrue((root/"out/listing-receipt.json").exists())
            self.assertEqual(
                cp["research_order"],
                json.loads((root/"out/listing-receipt.json").read_text()).get("priority_research_order", []),
            )
            self.assertEqual(
                cp["pending_research_count"],
                len(cp["research_order"]),
            )
            self.assertGreaterEqual(cp["deferred_research_backlog_count"], 0)
            self.assertEqual(cp["candidate_promotion_limit"], 30)


if __name__=="__main__":
    unittest.main()
