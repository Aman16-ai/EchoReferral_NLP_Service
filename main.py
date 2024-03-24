from fastapi import FastAPI
from candidateRanking.schemas.Ranking import CandidateAndJobDocPayload,CandidateRanking
from candidateRanking.main import findRank
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def index():
    return {"Message":"Welcome to EchoReferral NLP service"}

@app.post("/calculateRank")
def calculateCandidatesRank(payload : CandidateAndJobDocPayload):
    result : list[CandidateRanking] = findRank(payload.candidate_descriptions,payload.job_description)
    return {"Response":result}

