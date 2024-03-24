from pydantic import BaseModel

class CandidateAndJobDocPayload(BaseModel):
    candidate_descriptions : list[str]
    job_description : str

class CandidateRanking(BaseModel):
    rank :int
    candidate_idx:int
    score : float