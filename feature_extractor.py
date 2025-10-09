import re
import os
import matplotlib.pyplot as plt
from resume_parser import parse_resume, clean_text

RESUME_FOLDER = "resumes"

SKILLS = ['python', 'java', 'sql', 'excel', 'machine learning', 'data analysis', 'flask', 'react', 'docker']
DEGREES = ['bachelor', 'master', 'phd', 'b.tech', 'b.sc', 'm.tech', 'mca']
EXPERIENCE_REGEX = r'(\d+)\s+years?'

def extract_skills(text):
    found = []
    for skill in SKILLS:
        if skill in text:
            found.append(skill)
    return found

def extract_degrees(text):
    found = []
    for degree in DEGREES:
        if degree in text:
            found.append(degree)
    return found

def extract_experience(text):
    matches = re.findall(EXPERIENCE_REGEX, text)
    return matches

job_skills = ['python', 'react', 'machine learning']
job_degree = 'bachelor'
min_experience = 2  # years

def match_score(skills, degrees, experience):
    score = 0
    matched_skills = set(job_skills) & set(skills)
    score += len(matched_skills) * 2
    if job_degree in degrees:
        score += 2
    exp_years = int(experience[0]) if experience else 0
    if exp_years >= min_experience:
        score += 2
    return score, matched_skills, exp_years

if __name__ == "__main__":
    candidates = []
    for fname in os.listdir(RESUME_FOLDER):
        if fname.endswith(('.pdf', '.docx', '.txt')):
            fpath = os.path.join(RESUME_FOLDER, fname)
            text = parse_resume(fpath)
            cleaned = clean_text(text)
            skills = extract_skills(cleaned)
            degrees = extract_degrees(cleaned)
            experience_years = extract_experience(cleaned)
            score, matched_skills, exp_years = match_score(skills, degrees, experience_years)
            candidates.append({
                "filename": fname,
                "score": score,
                "skills": matched_skills,
                "degrees": degrees,
                "experience": exp_years
            })
    candidates = sorted(candidates, key=lambda x: x["score"], reverse=True)
    for rank, candidate in enumerate(candidates, 1):
        print(f"Rank {rank}: {candidate['filename']}")
        print(f"  Score: {candidate['score']}")
        print(f"  Matched Skills: {candidate['skills']}")
        print(f"  Degrees: {candidate['degrees']}")
        print(f"  Experience: {candidate['experience']} years")
        print("---")


names = [c['filename'] for c in candidates]
scores = [c['score'] for c in candidates]

plt.figure(figsize=(10, 6))
plt.bar(names, scores, color='skyblue')
plt.xlabel('Candidate')
plt.ylabel('Match Score')
plt.title('Resume Match Score Leaderboard')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()