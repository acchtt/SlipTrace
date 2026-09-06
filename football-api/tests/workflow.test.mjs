import test from 'node:test';
import assert from 'node:assert/strict';
import {DatabaseSync} from 'node:sqlite';
import {readFileSync} from 'node:fs';
import worker from '../worker.mjs';
import {parseBoard,validateMatches,settlement,competitionExclusion,profileFromEvents,confirmedXI} from '../../football/core.mjs';

const kickoff=()=>new Date(Date.now()+2*3600000).toISOString();
const match=()=>({rank:1,home:'Home FC',away:'Away FC',kickoff:kickoff(),grade:'A2',competition:'Premier League',structuralType:'Two-Sided',evidence:'Test evidence'});
const envToken='test-only-workspace-key-not-a-real-secret-12345';
function database(){
  const db=new DatabaseSync(':memory:');db.exec(readFileSync(new URL('../migrations/0001.sql',import.meta.url),'utf8'));
  const wrap=(sql,args=[])=>({bind:(...a)=>wrap(sql,a),first:async()=>db.prepare(sql).get(...args) || null,all:async()=>({results:db.prepare(sql).all(...args)}),run:async()=>db.prepare(sql).run(...args)});
  return {prepare:sql=>wrap(sql),batch:async statements=>{db.exec('BEGIN');try{const r=[];for(const s of statements)r.push(await s.run());db.exec('COMMIT');return r;}catch(e){db.exec('ROLLBACK');throw e;}},close:()=>db.close()};
}
function fixture(){return {id:101,home_team:'Home FC',away_team:'Away FC',home_team_id:11,away_team_id:22,event_date:kickoff(),league_id:1,season_id:2,status:'notstarted'};}
function lineup(status='confirmed') {return {event_id:101,lineup_status:status,lineups:Object.fromEntries(['home','away'].map((side,i)=>[side,{team_id:i===0?11:22,team_name:i===0?'Home FC':'Away FC',formation:'4-3-3',players:Array.from({length:11},(_,j)=>({id:i*20+j,name:`Player ${i}-${j}`,jersey_number:j+1})),substitutes:[]}]))};}
function setup(t,options={}){
  const DB=database(),env={DB,APP_TOKEN:envToken,BSD_API_KEY:'test-bsd',OPENAI_API_KEY:'test-ai',OPENAI_MODEL:'test-model',ALLOWED_ORIGIN:'https://acchtt.github.io',...(options.audit?{AIRTABLE_TOKEN:'test-airtable'}:{})};
  const nativeFetch=globalThis.fetch;let aiCalls=0,auditCalls=0;
  globalThis.fetch=async(url,init)=>{
    const u=new URL(url);let data;
    if(u.hostname==='sports.bzzoiro.com'){
      assert.equal(init.headers.Authorization,'Token test-bsd');
      if(u.pathname.endsWith('/lineups/'))data=lineup(options.predicted?'predicted':'confirmed');
      else if(u.pathname.endsWith('/stats/'))data={stats:{home:{big_chances:3},away:{big_chances:2}}};
      else if(u.pathname.includes('/leagues/'))data={id:1,name:options.league || 'Premier League',country:'England'};
      else if(/\/events\/\d+\/$/.test(u.pathname))data=fixture();
      else if(u.pathname==='/api/v2/events/')data=u.searchParams.has('team_name')?[fixture()]:Array.from({length:4},(_,i)=>({id:200+i,home_team_id:11,away_team_id:22,status:'finished',event_date:new Date(Date.now()-(i+1)*86400000).toISOString(),home_score:2,away_score:2}));
      else throw new Error(`Unmocked BSD URL: ${u}`);
    }else if(u.hostname==='api.openai.com'){
      aiCalls++;const body=JSON.parse(init.body);assert.equal(body.store,false);assert.equal(body.text.format.type,'json_schema');
      const output=body.text.format.name==='football_odds'?{home:'Home FC',away:'Away FC',competition:'Premier League',bookmaker:'Test book',period:options.period || 'full_match_90',oddsFormat:'decimal',capturedAtVisible:'',warnings:[],offers:[{line:2.75,odds:1.9,visibleLabel:'Over 2.75'}]}:{verdict:'OFFICIAL LOCK',postXIGrade:options.promote?'A1':'A2',selectedLine:options.wrongOffer?3.75:2.75,selectedOdds:1.9,summary:'Test-only supported route.',primaryRoute:'Both sides',profileAssessment:'Provided data',chanceQualityAssessment:'Provided data',lineupAssessment:'Confirmed',failureModes:['Early game management'],missingEvidence:[],lineComparisons:['O2.75 protection'],gates:{competitionEligible:true,profileSufficient:true,chanceSupportSufficient:!options.weakChance,lineupSufficient:true,burdenJustified:true,failureModesAcceptable:true,scorelineDriven:!!options.weakChance,roleChangeRemovesFailure:false}};
      data={status:'completed',output:[{type:'message',content:[{type:'output_text',text:JSON.stringify(output)}]}]};
    }else if(u.hostname==='api.airtable.com'){
      auditCalls++;if(options.auditFailure)return new Response('{}',{status:503});
      const body=JSON.parse(init.body);assert.deepEqual(body.performUpsert.fieldsToMergeOn,['Assessment ID']);data={records:[{id:'rec-test-'+auditCalls}]};
    }else throw new Error(`Unexpected egress: ${u}`);
    return new Response(JSON.stringify(data),{headers:{'content-type':'application/json'}});
  };
  t.after(()=>{globalThis.fetch=nativeFetch;DB.close();});
  async function request(path,body,overrides={}){const r=await worker.fetch(new Request('https://test-worker.invalid'+path,{method:body===undefined?'GET':'POST',headers:{Authorization:`Bearer ${envToken}`,...(body===undefined?{}:{'Content-Type':'application/json'}),...overrides},...(body===undefined?{}:{body:JSON.stringify(body)})}),env);return {status:r.status,data:await r.json(),headers:r.headers};}
  return {env,request,counts:()=>({aiCalls,auditCalls})};
}
async function prepare(request,grade='A2'){
  const board=await request('/boards',{matches:[{...match(),grade}],context:'Test profile and expected XI context'});assert.equal(board.status,201,JSON.stringify(board.data));
  const m=board.data.matches[0],path='/matches/'+m.id;
  assert.equal((await request(path+'/fixture-preview',{eventId:101})).status,200);
  assert.equal((await request(path+'/bind',{eventId:101,identityConfirmed:true})).status,200);
  const evidence=await request(path+'/lineups',{});assert.equal(evidence.status,200);
  const odds=await request(path+'/odds',{images:['data:image/png;base64,aGVsbG8=']});assert.equal(odds.status,200);
  return {board,path,odds,body:{oddsEvidenceId:odds.data.id,offers:[{line:2.75,odds:1.9}],capturedAt:new Date().toISOString(),identityConfirmed:true}};
}

test('Markdown, copied cells and JSON preserve rank, grade and ICT midnight',()=>{
  const markdown='| Rank | ICT kickoff | Match | Frozen grade | Structural type |\n|---|---|---|---|---|\n| 2 | 00:30 | Alpha vs Beta | **A2** | Two-Sided |\n| 1 | 20:00 | Gamma — Delta | A1 | Elite Carrier |';
  const parsed=parseBoard(markdown,'2026-09-07');assert.equal(parsed[0].rank,1);assert.equal(parsed[1].kickoff,'2026-09-06T17:30:00.000Z');
  assert.equal(parseBoard('Rank\tKickoff\tHome\tAway\tGrade\n1\t20:00\tHome\tAway\tA2','2026-09-07').length,1);
  assert.equal(parseBoard(JSON.stringify({matches:[match()]}))[0].grade,'A2');
  assert.throws(()=>validateMatches([match(),match()]),/unique positive rank/);
  assert.throws(()=>parseBoard(markdown,''),/slate date/);
});
test('Asian quarter-line settlement is correct across protected boundaries',()=>{
  for(const [line,goals,result] of [[2.75,3,'HALF WIN'],[3,3,'PUSH'],[3.25,3,'HALF LOSS'],[3.5,3,'LOSS'],[3.75,4,'HALF WIN'],[4,4,'PUSH'],[4.25,4,'HALF LOSS'],[3.75,5,'WIN']])assert.equal(settlement(line,goals),result);
});
test('Named cup exceptions survive generic exclusions; no youth caps',()=>{
  for(const [name,country] of [['Leagues Cup',''],['DFB-Pokal','Germany'],['FA Cup','England'],['EFL Cup','England'],['Premier League 2','England']])assert.equal(competitionExclusion({name,country}),null);
  for(const [name,country] of [['K League 1','South Korea'],['League Cup','Scotland'],['UEFA Champions League','Europe'],['FA Cup','Thailand']])assert.ok(competitionExclusion({name,country}));
});
test('Profiles exclude missing scores, future results and unrelated teams',()=>{
  const base={status:'finished',event_date:'2026-01-01T00:00:00Z',home_team_id:11,away_team_id:22,home_score:2,away_score:0};
  const p=profileFromEvents([base,{...base,home_score:null},{...base,event_date:'2030-01-01T00:00:00Z'},{...base,home_team_id:33,away_team_id:44}],11,'2026-09-01T00:00:00Z');assert.equal(p.sample.matches,1);assert.equal(p.sample.gf,2);
  assert.ok(confirmedXI(lineup(),fixture()));assert.equal(confirmedXI(lineup('predicted'),fixture()),false);
  const wrong=lineup();wrong.lineups.home.team_id=99;assert.equal(confirmedXI(wrong,fixture()),false);
});
test('Authentication, origin and historical-freeze boundaries reject unsafe requests',async t=>{
  const {request}=setup(t);assert.equal((await request('/boards',undefined,{Authorization:'Bearer wrong'})).status,401);
  assert.equal((await request('/boards',undefined,{Origin:'https://untrusted.example'})).status,403);
  assert.equal((await request('/boards',{matches:[{...match(),kickoff:'2020-01-01T00:00:00Z'}],context:''})).status,400);
});
test('Complete workflow freezes evidence, logs an official lock and returns the same decision on retry',async t=>{
  const {request,counts}=setup(t,{audit:true});const flow=await prepare(request);
  const result=await request(flow.path+'/verdict',flow.body);assert.equal(result.status,200);assert.equal(result.data.verdict,'OFFICIAL LOCK',JSON.stringify(result.data));assert.equal(result.data.auditStatus,'synced');
  const count=counts().aiCalls;const retry=await request(flow.path+'/verdict',flow.body);assert.equal(retry.data.assessmentId,result.data.assessmentId);assert.equal(counts().aiCalls,count);
  const board=await request('/boards/'+flow.board.data.id);assert.equal(board.data.matches[0].grade,'A2');assert.ok(board.data.matches[0].assessments.length>=3);
});
test('Predicted XI returns HOLD without invoking the verdict model',async t=>{
  const {request,counts}=setup(t,{predicted:true,audit:true});const f=await prepare(request);const calls=counts().aiCalls;const r=await request(f.path+'/verdict',f.body);assert.equal(r.data.verdict,'NO BET — HOLD');assert.match(r.data.summary,/confirmed/);assert.equal(counts().aiCalls,calls);
});
test('Stale screenshots cannot be refreshed by uploading them again',async t=>{
  const {request}=setup(t,{audit:true});const f=await prepare(request);f.body.capturedAt=new Date(Date.now()-3600000).toISOString();const r=await request(f.path+'/verdict',f.body);assert.equal(r.data.verdict,'NO BET — HOLD');assert.match(r.data.summary,/freshness/);
});
test('Unclear market scope and excluded competitions return HOLD',async t=>{
  const {request}=setup(t,{audit:true,period:'first_half',league:'Scottish League Cup'});const f=await prepare(request);const r=await request(f.path+'/verdict',f.body);assert.equal(r.data.verdict,'NO BET — HOLD');assert.match(r.data.summary,/90-minute/);
});
test('An unlisted model-selected price cannot become an official lock',async t=>{
  const {request}=setup(t,{audit:true,wrongOffer:true});const f=await prepare(request);const r=await request(f.path+'/verdict',f.body);assert.equal(r.data.verdict,'NO BET — HOLD');assert.equal(r.data.selectedLine,null);
});
test('Scoreline-driven weak chance support and excessive XI promotion are held',async t=>{
  const {request}=setup(t,{audit:true,weakChance:true,promote:true});const f=await prepare(request,'B+');const r=await request(f.path+'/verdict',f.body);assert.equal(r.data.verdict,'NO BET — HOLD');assert.match(r.data.summary,/chance confirmation/);assert.match(r.data.summary,/promotion/);
});
test('Missing audit configuration prevents an official lock',async t=>{
  const {request}=setup(t);const f=await prepare(request);const r=await request(f.path+'/verdict',f.body);assert.equal(r.data.verdict,'NO BET — HOLD');assert.match(r.data.summary,/Airtable/);
});
test('Cross-match odds references and unreviewed identity are rejected',async t=>{
  const {request}=setup(t,{audit:true});const one=await prepare(request),two=await prepare(request);const cross=await request(two.path+'/verdict',one.body);assert.equal(cross.status,400);const r=await request(one.path+'/verdict',{...one.body,identityConfirmed:false});assert.equal(r.data.verdict,'NO BET — HOLD');
});
test('Pending audit outbox survives transport failure without losing assessments',async t=>{
  const {request}=setup(t,{audit:true,auditFailure:true});const f=await prepare(request);const r=await request(f.path+'/verdict',f.body);assert.equal(r.data.verdict,'NO BET — HOLD');assert.equal(r.data.auditStatus,'pending');const board=await request('/boards/'+f.board.data.id);assert.ok(board.data.matches[0].assessments.every(a=>a.auditStatus==='pending'));
});
