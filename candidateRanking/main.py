from .NLP_PIPE import NLP_SERVICE
from .Rank import calculate_candidates_rank


def findRank(candidate_descriptions:list[str],job_description:str):
    candidate_doc = []
    job_doc = NLP_SERVICE(doc=job_description)\
    .clean_text()\
    .transform_text()\
    .get_doc()

    for candidate in candidate_descriptions:
        nlp_serive = NLP_SERVICE(doc = candidate)
        doc = nlp_serive\
        .clean_text()\
        .transform_text()\
        .get_doc()
        candidate_doc.append(doc)
    
    print(candidate_doc)
    print(job_doc)
    return calculate_candidates_rank(candidate_doc,job_doc)

# job_description = "Looking for experience data analysis and machine learning engineer."

# candidate_descriptions = [
#     "Candidate 1 is experienced in machine learning and data analysis.",
#     "Candidate 2 has a background in software engineering and project management.",
#     "Candidate 3 specializes in data visualization, analysis and communication skills.",
# ]
# findRank(candidate_descriptions=candidate_descriptions,job_description=job_description)