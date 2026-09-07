export const API='https://sports.bzzoiro.com/api/v2/';
export const SOCKET='wss://sports.bzzoiro.com/live/football/';
export const LIVE=new Set(['live','inprogress','1st_half','2nd_half','halftime','extratime','extra_time','penalties']);
export const DONE=new Set(['finished','aet','FT','ft']);
export function rows(data){const list=Array.isArray(data)?data:data?.events??data?.results??data?.data;if(!Array.isArray(list))throw new Error('BSD returned an unexpected match list.');return list;}
export const number=value=>Number.isFinite(value)&&typeof value==='number'?value:null;
export function normalize(e){
  if(!Number.isSafeInteger(e.id)||e.id<=0)throw new Error('BSD returned an invalid match ID.');
  return {...e,home_team:typeof e.home_team==='string'?e.home_team:'Home team',away_team:typeof e.away_team==='string'?e.away_team:'Away team',home_score:number(e.home_score),away_score:number(e.away_score),current_minute:number(e.current_minute)};
}
export function isLive(e){return LIVE.has(e.status)&&!DONE.has(e.period);}
export function statusText(e){
  if(e.checking)return 'CHECK';
  if(e.status==='penalties'||e.period==='penalties')return 'PEN';
  if(DONE.has(e.status)||DONE.has(e.period))return e.status==='aet'?'AET':'FT';
  if(e.status==='halftime'||e.period==='halftime')return 'HT';
  if(['postponed','cancelled','delayed','unresolved'].includes(e.status))return ({postponed:'POSTP.',cancelled:'CANC.',delayed:'DELAY',unresolved:'TBC'})[e.status];
  if(isLive(e))return e.displayMinute || (e.current_minute===null||e.current_minute===undefined?'LIVE':`${e.current_minute}′`);
  return Number.isFinite(Date.parse(e.event_date))?new Intl.DateTimeFormat('en-GB',{timeZone:'Asia/Ho_Chi_Minh',hour:'2-digit',minute:'2-digit',hour12:false}).format(new Date(e.event_date)):'TBC';
}
export function score(e){
  if(e.streamScore)return e.streamScore;
  return ['home','away'].map(side=>e[`${side}_score`]===null||e[`${side}_score`]===undefined?'—':e[`${side}_score`]+(number(e.extra_time_score?.[side])??0));
}
export function mergeRest(previous,next,requestStarted,time=Date.now()){
  const e=normalize(next);
  if(previous?.pushAt && (previous.pushAt>requestStarted || (time-previous.pushAt<35000 && (!Date.parse(e.last_updated)||Date.parse(e.last_updated)<previous.pushAt)))){
    return {...e,status:previous.status,period:previous.period,current_minute:previous.current_minute,displayMinute:previous.displayMinute,streamScore:previous.streamScore,pushAt:previous.pushAt,actionTs:previous.actionTs,checking:false};
  }
  return {...e,checking:false};
}
export function applyFrame(previous,frame,time=Date.now()){
  const f=frame.type==='subscribed'?frame.event:frame;
  if(!f||!previous||Number(frame.event_id??f.event_id)!==previous.id)return previous;
  if(frame.type==='action'){
    if(!['goal','deleted_event'].includes(frame.action_type)||!Number.isFinite(frame.ts)||frame.ts<(previous.actionTs||0))return previous;
    if(number(frame.score?.home)===null||number(frame.score?.away)===null)return previous;
    return {...previous,streamScore:[frame.score.home,frame.score.away],actionTs:frame.ts,pushAt:time};
  }
  if(!['event','subscribed'].includes(frame.type)||!f.score)return previous;
  const s=[number(f.score.home),number(f.score.away)];if(s.includes(null))return previous;
  const status=f.time?.status;
  return {...previous,streamScore:s,pushAt:time,checking:false,status:status==='live'?'inprogress':status||previous.status,displayMinute:f.time?.display||undefined,current_minute:number(f.time?.minute)??previous.current_minute,period:({1:'1st_half',2:'2nd_half',3:'extra_time',4:'extra_time',5:'penalties'})[f.time?.period]||previous.period};
}
export function ictDate(time=Date.now()){return Number.isFinite(time)?new Date(time+7*3600000).toISOString().slice(0,10):'';}
export function dayWindow(date){
  if(!/^\d{4}-\d{2}-\d{2}$/.test(date))throw new Error('Choose a valid date.');
  const start=new Date(`${date}T00:00:00+07:00`).getTime();if(!Number.isFinite(start))throw new Error('Choose a valid date.');
  return {date_from:new Date(start).toISOString(),date_to:new Date(start+86400000-1).toISOString()};
}
export function visibleEvents(events,{tab='live',query='',pins=new Set(),date=ictDate()}={}){
  const q=query.toLowerCase().trim();
  return events.filter(e=>(tab==='live'?(isLive(e)||e.checking):tab==='pinned'?pins.has(e.id):ictDate(Date.parse(e.event_date))===date&&(tab!=='finished'||DONE.has(e.status)||DONE.has(e.period)))&&(!q||`${e.home_team} ${e.away_team} ${e.league_name||''}`.toLowerCase().includes(q))).sort((a,b)=>Number(pins.has(b.id))-Number(pins.has(a.id))||String(a.league_name||a.league_id||'').localeCompare(String(b.league_name||b.league_id||''))||Date.parse(a.event_date)-Date.parse(b.event_date)||a.id-b.id);
}
export function subscriptions(events,pins,selected){return events.filter(e=>isLive(e)&&e.live_websocket).sort((a,b)=>Number(b.id===selected)-Number(a.id===selected)||Number(pins.has(b.id))-Number(pins.has(a.id))||a.id-b.id).slice(0,10).map(e=>e.id);}
