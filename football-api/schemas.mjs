const str = {type:'string'}, num = {type:'number'}, bool = {type:'boolean'};
const nullableNum = {type:['number','null']};
const list = items => ({type:'array',items});
const object = properties => ({type:'object',properties,required:Object.keys(properties),additionalProperties:false});
export const oddsSchema = object({home:str, away:str, competition:str, bookmaker:str, period:{type:'string',enum:['full_match_90','first_half','second_half','extra_time','unknown']}, oddsFormat:{type:'string',enum:['decimal','other','unknown']}, capturedAtVisible:str, warnings:list(str), offers:list(object({line:nullableNum,odds:nullableNum,visibleLabel:str}))});
export const verdictSchema = object({
  verdict:{type:'string',enum:['OFFICIAL LOCK','NO BET — HOLD','PASS']}, postXIGrade:{type:'string',enum:['A1','A2','B+','B','PASS']},
  selectedLine:nullableNum,selectedOdds:nullableNum,summary:str,primaryRoute:str,profileAssessment:str,chanceQualityAssessment:str,lineupAssessment:str,
  failureModes:list(str),missingEvidence:list(str),lineComparisons:list(str),
  gates:object({competitionEligible:bool,profileSufficient:bool,chanceSupportSufficient:bool,lineupSufficient:bool,burdenJustified:bool,failureModesAcceptable:bool,scorelineDriven:bool,roleChangeRemovesFailure:bool})
});
