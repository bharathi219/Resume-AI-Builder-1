import streamlit as st
import pdfplumber
import spacy
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import io

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = ['python', 'java', 'sql', 'machine learning', 'deep learning', 'nlp', 'pandas',
             'numpy', 'django', 'flask', 'html', 'css', 'javascript', 'power bi', 'aws', 'time series forecasting']

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def classify_resume(text):
    text_lower = text.lower()
    if 'machine learning' in text_lower or 'data science' in text_lower:
        return 'Data Scientist'
    elif 'python' in text_lower and 'django' in text_lower:
        return 'Backend Developer'
    elif 'html' in text_lower and 'css' in text_lower:
        return 'Frontend Developer'
    elif 'sql' in text_lower and 'excel' in text_lower:
        return 'Data Analyst'
    else:
        return 'General IT Role'

def extract_skills(text):
    tokens = [token.text.lower() for token in nlp(text)]
    return list(set([skill for skill in SKILLS_DB if skill in tokens]))

def extract_skills_from_jd(jd_text):
    tokens = [token.text.lower() for token in nlp(jd_text)]
    return list(set([skill for skill in SKILLS_DB if skill in tokens]))

def extract_education(text):
    education = []
    edu_keywords = ['btech', 'mtech', 'b.sc', 'm.sc', 'bachelor', 'master', 'phd']
    for line in text.split('\n'):
        if any(word in line.lower() for word in edu_keywords):
            education.append(line.strip())
    return education

def extract_experience(text):
    experience = []
    exp_keywords = ['intern', 'developer', 'engineer', 'analyst', 'consultant']
    for line in text.split('\n'):
        if any(keyword in line.lower() for keyword in exp_keywords):
            experience.append(line.strip())
    return experience

def extract_projects(text):
    projects = []
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if 'project' in line.lower():
            project = ' '.join(lines[i:i+3])
            projects.append(project.strip())
    return projects

def calculate_similarity(resume_skills, jd_skills):
    resume_vector = [' '.join(resume_skills)]
    jd_vector = [' '.join(jd_skills)]
    vectorizer = CountVectorizer().fit_transform(jd_vector + resume_vector)
    vectors = vectorizer.toarray()
    score = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
    return round(score, 2)

def generate_feedback(score, resume_skills, jd_skills):
    missing_skills = list(set(jd_skills) - set(resume_skills))
    top_missing = ", ".join(missing_skills[:3])
    if score >= 0.8:
        return f"🔥 Excellent match! Apply right away."
    elif score >= 0.6:
        return f"✅ Good match. A few skill enhancements will strengthen your fit."
    elif score >= 0.4:
        return f"⚠️ Moderate match. Consider learning or emphasizing: {top_missing}. These are key in this JD and missing from your resume."
    else:
        return f"❌ Low match. You're missing key skills: {top_missing}. Consider updating your resume or exploring other roles."

# Streamlit UI
st.title("AI Resume Analyzer")

resume_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])
jd_files = st.file_uploader("Upload One or More Job Descriptions (TXT only)", type=["txt"], accept_multiple_files=True)

if resume_file and jd_files:
    resume_text = extract_text_from_pdf(resume_file)
    skills = extract_skills(resume_text)
    education = extract_education(resume_text)
    experience = extract_experience(resume_text)
    projects = extract_projects(resume_text)
    role = classify_resume(resume_text)

    st.subheader("🎯 Predicted Role:")
    st.write(role)

    st.subheader("✅ Skills from Resume:")
    st.write(skills)

    st.subheader("🎓 Education:")
    st.write(education)

    st.subheader("💼 Experience:")
    st.write(experience)

    st.subheader("🛠 Projects:")
    st.write(projects)

    best_score = 0
    best_jd = ""

    st.subheader("📊 JD Match Scores:")
    for jd_file in jd_files:
        jd_text = jd_file.read().decode("utf-8")
        jd_skills = extract_skills_from_jd(jd_text)
        match_score = calculate_similarity(skills, jd_skills)
        feedback = generate_feedback(match_score, skills, jd_skills)
        st.markdown(f"**{jd_file.name}** - Match Score: `{match_score * 100:.2f}%`")
        st.info(feedback)
        if match_score > best_score:
            best_score = match_score
            best_jd = jd_file.name

    if best_jd:
        st.success(f"🏆 Best Match: **{best_jd}** — Apply to this one first!")
