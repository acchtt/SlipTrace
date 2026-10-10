import pathlib
import sys
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from model_reaudit import audit,ModelReauditError

def example():
    states=[
        ("watch_a","WATCH","STOP",2.0),
        ("watch_b","WATCH","STOP",2.0),
        ("focus_a","FOCUS","FOLLOW",2.75),
        ("focus_b","FOCUS","FOLLOW",3.0)
    ]
    c=[{"rank":i+1,"match_id":m,"board_state":s,"follow_lane":lane,
        "supported_line":line} for i,(m,s,lane,line) in enumerate(states)]
    c2=[
        {"rank":i+1,"match_id":m,"board_state":s,"supported_line":line+0.25}
        for i,(m,s,lane,line) in enumerate(states) if s=="FOCUS"
    ]+[
        {"rank":i+1,"match_id":m,"board_state":s,"supported_line":line+0.25}
        for i,(m,s,lane,line) in enumerate(states) if s=="WATCH"
    ]
    for i,row in enumerate(c2):row["rank"]=i+1
    q=[{"match_id":r["match_id"],"official_c_follow_lane":r["follow_lane"],
        "c":{"board_state":r["board_state"],"supported_line":r["supported_line"],
             "funded_at_own_supported_line":r["board_state"]=="WATCH"},
        "c2":{"board_state":c2_row["board_state"],"supported_line":c2_row["supported_line"],
              "funded_at_own_supported_line":False}}
       for r in c for c2_row in c2 if c2_row["match_id"]==r["match_id"]]
    return {"schema_version":"football-model-reaudit-v1","board_id":"B-test",
            "c_board_result":{"schema_version":"football-engine-v1",
                              "stage":"board_result","model":"c","match_count":4,"matches":c},
            "c2_board_result":{"schema_version":"football-engine-v1",
                               "stage":"board_result","model":"c2","match_count":4,"matches":c2},
            "funding_readiness":{"schema_version":"football-follow-funding-readiness-v1",
                                 "board_id":"B-test","advisory_only":True,
                                 "thresholds_changed":False,"fixtures":q}}


class ModelReauditTests(unittest.TestCase):
    def test_c_watch_outranks_two_focus_and_all_supported_lines_unfunded(self):
        output=audit(example())
        self.assertEqual(output["c"]["cross_state_rank_inversion_pairs"],4)
        self.assertEqual(output["c2"]["cross_state_rank_inversion_pairs"],0)
        self.assertEqual(output["c"]["follow_count"],2)
        self.assertEqual(output["c"]["follow_supported_funded"],0)
        self.assertIn("C_RANK_HAS_WATCH_OR_PASS_AHEAD_OF_FOCUS",output["warnings"])
        self.assertIn("ALL_C_FOLLOW_OWN_SUPPORTED_LINES_UNFUNDED",output["warnings"])
        self.assertTrue(output["no_user_or_model_exposure_created"])

    def test_consistent_funding_and_focus_priority_has_no_warning(self):
        p=example()
        c=p["c_board_result"]["matches"]
        c[:]=c[2:]+c[:2]
        for i,x in enumerate(c):x["rank"]=i+1
        for row in p["funding_readiness"]["fixtures"]:
            row["c"]["funded_at_own_supported_line"]=True
            row["c2"]["funded_at_own_supported_line"]=True
        out=audit(p)
        self.assertEqual(out["warnings"],[])
        self.assertEqual(out["qa_status"],"NO_MODEL_ALIGNMENT_WARNING")

    def test_reject_foreign_unverified_funding_data(self):
        p=example()
        p["funding_readiness"]["fixtures"][0]["c"]["supported_line"]=7.0
        with self.assertRaisesRegex(ModelReauditError,"mismatched"):
            audit(p)

    def test_reject_missing_model_or_duplicate_ids(self):
        p=example()
        p["c2_board_result"]["matches"].pop()
        p["c2_board_result"]["match_count"]=3
        with self.assertRaisesRegex(ModelReauditError,"identical"):
            audit(p)
        p=example()
        p["c_board_result"]["matches"][1]["match_id"]="watch_a"
        with self.assertRaisesRegex(ModelReauditError,"duplicate"):
            audit(p)

    def test_no_unfrozen_action_or_price_synthesis(self):
        out=audit(example())
        self.assertFalse(out["actions_created"])
        self.assertFalse(out["model_policy_changed"])
        self.assertNotIn("BET",str(out["c"]))


if __name__=="__main__":
    unittest.main()
