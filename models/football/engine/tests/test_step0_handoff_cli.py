import json, pathlib, subprocess, sys, tempfile, unittest
ENGINE=pathlib.Path(__file__).resolve().parents[1]
CLI=ENGINE/"step0_handoff_cli.py"
def row(mid,rank,disp="ADMITTED_TO_C"):
    return {"match_id":mid,"step0_capacity_queue_rank":rank,"final_step0_disposition":disp,"operational_viability_grade":"A","xi_expected":"YES","market_observability":"HIGH","team_news_observability":"HIGH","operational_viability_reason":"ok","competition_reliability_state":"UNPROVEN","competition_reliability_reason":"sample"}
def payload():
    r=row("m1",1)
    return {"handoff_version":"football-step0-handoff-v2","complete":True,"actionable_complete":True,"work_ready":True,"admitted_to_c_count":1,"capacity_deferred_count":0,"admitted_fixtures":[dict(r)],"capacity_queue":[dict(r)]}
class T(unittest.TestCase):
    def runp(self,p):
        with tempfile.NamedTemporaryFile("w",suffix=".json",delete=False) as f: json.dump(p,f); n=f.name
        return subprocess.run([sys.executable,str(CLI),"--input",n],capture_output=True,text=True)
    def test_pass(self): self.assertEqual(self.runp(payload()).returncode,0)
    def test_missing_queue(self):
        p=payload(); del p["capacity_queue"]; r=self.runp(p); self.assertEqual(r.returncode,2); self.assertIn("CAPACITY QUEUE MISSING",r.stderr)
    def test_missing_id(self):
        p=payload(); del p["capacity_queue"][0]["match_id"]; r=self.runp(p); self.assertEqual(r.returncode,2); self.assertIn("STABLE FIXTURE ID MISSING",r.stderr)
    def test_missing_field(self):
        p=payload(); del p["capacity_queue"][0]["xi_expected"]; r=self.runp(p); self.assertEqual(r.returncode,2); self.assertIn("OPERATIONAL CONTRACT MISSING",r.stderr)
if __name__=="__main__": unittest.main()
