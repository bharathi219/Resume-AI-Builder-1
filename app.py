import streamlit as st
import pdfplumber
import spacy
import json
import spacy
import subprocess
import importlib.util

def load_model():
    if not importlib.util.find_spec("en_core_web_sm"):
        subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    return spacy.load("en_core_web_sm")

nlp = load_model()

# # Load spaCy model with caching to avoid reloading every time
# @st.cache_resource
# def load_model():
#     return spacy.load("en_core_web_sm")

# nlp = load_model()

st.title("📄 AI Resume Analyzer")

resume_text = st.text_area("Paste your resume here:")

if resume_text:
    doc = nlp(resume_text)
    st.subheader("Named Entities")
    for ent in doc.ents:
        st.write(f"• **{ent.text}** → `{ent.label_}`")


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = ['python', 'java', 'sql', 'machine learning', 'deep learning', 'nlp', 'pandas',
             'numpy', 'django', 'flask', 'html', 'css', 'javascript']

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

# Streamlit UI
st.title("Upload Resume Files")

resume_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])
jd_file = st.file_uploader("Upload Job Description (TXT only)", type=["txt"])

if resume_file and jd_file:
    resume_text = extract_text_from_pdf(resume_file)
    jd_text = jd_file.read().decode("utf-8")

    skills = extract_skills(resume_text)
    jd_skills = extract_skills_from_jd(jd_text)
    education = extract_education(resume_text)
    experience = extract_experience(resume_text)
    projects = extract_projects(resume_text)
    role = classify_resume(resume_text)
    match_score = calculate_similarity(skills, jd_skills)

    st.subheader("🎯 Predicted Role:")
    st.write(role)

    st.subheader("✅ Skills from Resume:")
    st.write(skills)

    st.subheader("📌 Skills from JD:")
    st.write(jd_skills)

    st.subheader("🎓 Education:")
    st.write(education)

    st.subheader("💼 Experience:")
    st.write(experience)

    st.subheader("🛠 Projects:")
    st.write(projects)

    st.subheader("📊 Match Score:")
    st.success(f"{match_score * 100:.2f}%")
