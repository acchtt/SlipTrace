import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from models.football.stages_v4.tools import normal_finalize
from models.football.stages_v4.test_source_completeness import source, NOW


class NormalFinalizeTests(unittest.TestCase):
    def test_finalizer_emits_native_rank_handoff_without_resume(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = source()
            fixture = src["fixtures"][0]
            fixture["provider_team_ids"] = ["1", "2"]
            request = {
                "run_id": src["run_id"],
                "window_start_ict": src["window_start_utc"],
                "window_end_ict": src["window_end_utc"],
            }
            (root / "request.json").write_text(json.dumps(request))
            (root / "targets.json").write_text(
                json.dumps({"run_id": src["run_id"], "targets": [fixture["match_id"]]})
            )

            def event(team, opponent, eid, gf, ga, kickoff):
                home = team == "1"
                return {
                    "Eid": eid, "Eps": "FT", "Esid": 1, "Esd": kickoff,
                    "T1": [{"ID": team if home else opponent, "Nm": "A"}],
                    "T2": [{"ID": opponent if home else team, "Nm": "B"}],
                    "Tr1": str(gf if home else ga), "Tr2": str(ga if home else gf),
                }

            current = {
                "Eid": fixture["match_id"], "Eps": "NS", "Esid": 1,
                "Esd": "20261012190000",
                "T1": [{"ID": "1", "Nm": "AC Oulu"}],
                "T2": [{"ID": "2", "Nm": "HJK Helsinki"}],
            }

            def team_payload(team):
                other = "2" if team == "1" else "1"
                games = []
                for i, (gf, ga) in enumerate(((2,1),(1,2),(3,1),(2,2))):
                    games.append(event(team, other, str(200+i), gf, ga, f"2026100{i+1}180000"))
                return {"ID": team, "Stages": [{"Snm": "Veikkausliiga", "Events": games + [current]}]}

            def get(url, name):
                team = url.split("/team/")[1].split("/")[0]
                return team_payload(team), {
                    "source_url": url,
                    "observed_at_utc": NOW,
                    "file": name + ".json",
                    "sha256": "x",
                }

            with patch.object(normal_finalize.work_sweep, "utcnow", return_value=NOW), \
                 patch.object(normal_finalize.work_sweep, "acquire", return_value=copy.deepcopy(src)), \
                 patch.object(normal_finalize.work_sweep.Evidence, "get", side_effect=get):
                self.assertEqual(
                    normal_finalize.run(root/"request.json", root/"targets.json", root/"out"),
                    0,
                )
            handoff = json.loads((root/"out/rank-handoff.json").read_text())
            checkpoint = json.loads((root/"out/checkpoint.json").read_text())
            self.assertEqual(handoff["status"], "V4_RANK_HANDOFF_READY")
            self.assertTrue(handoff["active_research_complete"])
            self.assertTrue(checkpoint["rank_handoff_ready"])
            self.assertEqual(checkpoint["resume_queue"], [])
            self.assertTrue((root/"out/v4_sweep_ready.json").exists())


if __name__ == "__main__":
    unittest.main()
