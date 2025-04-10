## AI Resume Analyzer & Skill Extractor

This project is a smart resume analyzer built using NLP techniques that extracts text from resumes (PDF format), identifies skills, education, work experience, and projects. It also classifies the job role and calculates the similarity between the resume content and a provided job description.

## Features

- PDF resume parsing and text extraction
- Skill, education, and experience extraction using spaCy
- Job role classification using a scikit-learn model
- Resume-to-job-description similarity scoring
- Streamlit-based interactive web UI

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/resume-ai-builder.git
cd resume-ai-builder




Logic Used
1. Text Extraction
PyMuPDF (fitz) is used to extract text from uploaded PDF resumes.

2. Information Extraction
Uses spaCy’s en_core_web_sm model to identify named entities and key patterns.

Custom rule-based NLP patterns are used to extract:

Skills

Education (degrees, universities)

Work Experience (roles, companies, years)

Projects (using project-related keywords)

3. Job Role Classification
A text classification model trained using scikit-learn (e.g., Logistic Regression or Naive Bayes).

The model uses TF-IDF features extracted from resume texts to predict job roles like Data Scientist, Web Developer, etc.

4. Similarity Score Calculation
Compares the extracted resume text and job description using cosine similarity over TF-IDF vectors.

Outputs a percentage score indicating the relevance of the resume for the given job description.


Time Taken
Task	Time Spent
Data Collection & Preprocessing	~6 hours
NLP Pipelines & Skill Extraction	~5 hours
Model Training & Classification Logic	~4 hours
Streamlit UI Development	~3 hours
Testing & Debugging	~2 hours
Video Demo Preparation	~2 hours
Total Time	~22 hours


