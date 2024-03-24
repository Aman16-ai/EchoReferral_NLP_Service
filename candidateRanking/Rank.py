from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .schemas.Ranking import CandidateRanking

def calculate_candidates_rank(candidates_doc,job_doc) -> list[CandidateRanking]:
    vectorizer = TfidfVectorizer()
    job_vector = vectorizer.fit_transform([job_doc])
    candidates_vector = vectorizer.transform(candidates_doc)

    cosine_similarities = cosine_similarity(candidates_vector,job_vector)
    print(cosine_similarities)
    candidate_ranking = sorted(
        zip(range(len(cosine_similarities)), cosine_similarities),
        key=lambda x: x[1],
        reverse=True,
    )
    print(candidate_ranking)
    result : list[CandidateRanking] = []
    for rank, (candidate_idx, similarity_score) in enumerate(candidate_ranking, start=1):
        print(f"Rank {rank}: Candidate {candidate_idx + 1} - Similarity Score: {similarity_score[0]}")
        candidateRank = CandidateRanking(rank=rank,candidate_idx=candidate_idx,score=similarity_score[0])
        result.append(candidateRank)
    
    return result
