import streamlit as st
import os
from resume_parser import parse_resume, clean_text
import matplotlib.pyplot as plt

SKILLS = ['python', 'java', 'sql', 'excel', 'machine learning', 'data analysis', 'flask', 'react', 'docker']
DEGREES = ['bachelor', 'master', 'phd', 'b.tech', 'b.sc', 'm.tech', 'mca']
EXPERIENCE_REGEX = r'(\d+)\s+years?'

def extract_skills(text):
    return [skill for skill in SKILLS if skill in text]

def extract_degrees(text):
    return [degree for degree in DEGREES if degree in text]

def extract_experience(text):
    import re
    return re.findall(EXPERIENCE_REGEX, text)

st.set_page_config(page_title="Smart Resume Screening", layout="centered")

st.title("🤖 Smart Resume Screening Dashboard")
st.markdown("Upload resumes and match against the job requirements below:")

with st.expander("🔧 Set Job Requirements", expanded=True):
    job_skills = st.multiselect("Required skills", SKILLS, default=["python", "react", "machine learning"])
    job_degree = st.selectbox("Required degree", DEGREES, index=0)
    min_experience = st.slider("Minimum experience (years)", 0, 10, 2)

st.markdown("### 📝 Upload Resumes")
uploaded_files = st.file_uploader(
    "Choose multiple resumes (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"], accept_multiple_files=True
)

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

if uploaded_files:
    candidates = []
    for uploaded_file in uploaded_files:
        # Save to disk for resume_parser compatibility
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
        text = parse_resume(uploaded_file.name)
        cleaned = clean_text(text)
        skills = extract_skills(cleaned)
        degrees = extract_degrees(cleaned)
        experience_years = extract_experience(cleaned)
        score, matched_skills, exp_years = match_score(skills, degrees, experience_years)
        candidates.append({
            "filename": uploaded_file.name,
            "score": score,
            "skills": list(matched_skills),
            "degrees": degrees,
            "experience": exp_years
        })
    candidates = sorted(candidates, key=lambda x: x['score'], reverse=True)

    # Leaderboard
    st.markdown("## 🎖️ Leaderboard")
    for rank, candidate in enumerate(candidates, 1):
        col0, col1, col2, col3, col4 = st.columns([1, 3, 1, 3, 1])
        with col1:
            st.markdown(f"**{rank}. {candidate['filename']}**")
        with col2:
            st.markdown(f"**Score:** `{candidate['score']}`")
        with col3:
            st.markdown(f"**Matched Skills:** `{', '.join(candidate['skills'])}`")
        with col4:
            st.markdown(f"**Yrs Exp:** `{candidate['experience']}`")

    st.markdown("---")
    st.markdown("## 📊 Candidate Scores Chart")
    names = [c['filename'] for c in candidates]
    scores = [c['score'] for c in candidates]
    fig, ax = plt.subplots(figsize=(4 + len(names), 3))
    bars = ax.bar(names, scores, width=0.4, color='mediumseagreen')
    ax.set_xlabel('Resume')
    ax.set_ylabel('Match Score')
    ax.set_title('Resume Match Scores')
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    if len(names) == 1:
        ax.set_xlim(-0.5, 0.5)
    for bar, score in zip(bars, scores):
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.2, int(yval),
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    st.pyplot(fig)
