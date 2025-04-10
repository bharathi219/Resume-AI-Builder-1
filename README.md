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
## 2.Create and Active a Virtual Environment

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

pip install -r requirements.txt
python -m spacy download en_core_web_sm
