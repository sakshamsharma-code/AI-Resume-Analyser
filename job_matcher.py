import re

def calculate_match_score(resume_text, required_skills):
    resume_text = resume_text.lower()
    matched_skills = []

    for skill in required_skills:
        if re.search(r'\b' + re.escape(skill.lower()) + r'\b', resume_text):
            matched_skills.append(skill)

    match_score = int((len(matched_skills) / len(required_skills)) * 100)
    missing_skills = list(set(required_skills) - set(matched_skills))
    return match_score, matched_skills, missing_skills
