# AI Resume Analyzer & Skill Extractor

This project analyzes resumes (PDFs), extracts key information like skills, education, experience, and projects, classifies the job role, and computes how well it matches a job description using NLP and machine learning techniques. Built with spaCy, scikit-learn, and Streamlit.

---

## 🚀 Setup Instructions

###  1. Clone the Repository
```bash
git clone https://github.com/yourusername/resume-ai-builder.git
cd resume-ai-builder
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Run the Streamlit App
```bash
streamlit run app.py
```

---

## 🧠 Logic Used

### 1. **Resume Parsing & Text Extraction**
- PDF files are parsed using **PyMuPDF (fitz)**.

### 2. **Information Extraction**
- spaCy’s `en_core_web_sm` model helps identify entities and patterns.
- Rule-based matching for extracting:
  - **Skills**
  - **Education** (degree, university)
  - **Experience** (roles, companies)
  - **Projects** (based on keywords like 'developed', 'built', etc.)

### 3. **Job Role Classification**
- A classification model trained on labeled resume text using **TF-IDF** + **scikit-learn classifiers** (e.g., Logistic Regression).

### 4. **Similarity Score Calculation**
- Cosine similarity between job description and resume content using TF-IDF vectors.
- Outputs a percentage match score.

---

## ⏱️ Time Taken to Complete

| Task                               | Time Spent |
|------------------------------------|------------|
| Resume parsing & extraction logic | ~6 hours   |
| Skill/education/experience parsing | ~5 hours   |
| Classification model & scoring     | ~4 hours   |
| Streamlit UI setup                 | ~3 hours   |
| Testing, debugging, and polishing  | ~2 hours   |
| Video demo prep                    | ~2 hours   |
| **Total**                          | **~22 hours** |

---

## 📁 Upload Directory

Uploaded resumes are saved in the `uploads/` folder:

```python
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
```

When a file is uploaded via the UI:
```python
uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])
if uploaded_file:
    with open(os.path.join(UPLOAD_FOLDER, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
```

---

## 👤 About Me
I'm Bharathi Mekala, a passionate and curious Data Science enthusiast with a strong foundation in machine learning, algorithms, and data analysis. With a background in Computer Science and hands-on experience as a Data Analyst Intern, I thrive on turning raw data into meaningful insights that drive smarter decisions.

🎓 Education:

--**📍 Pursuing MCA at KMM University**

--**🎓 BSc Computer Science, Sri Vaishnavi Degree College, Class of 2024**

💼 Internship:

-- Data Analyst Intern at Social Tek AI and Business Solutions, where I contributed to building smarter chatbots using NLP and supported optimization of conversational flows based on user interaction data.

🛠️ Skills:

Languages: Python, SQL, Java

Data Tools: Power BI, Tableau, Pandas, NumPy

ML/AI: Scikit-learn, TensorFlow, NLP, Computer Vision

Others: Git, Jupyter, Excel (Advanced)

📊 Projects:

OCR Application Form Reader using TensorFlow + Tesseract

Order Priority Prediction using classification models and Tableau dashboards

Crop Yield Estimation using regression models and agri data visualization

📜 Certifications:

Data Science with AI

Data Analysis with Python

🚀 I'm looking for an entry-level role in data analytics or machine learning where I can grow and make a real impact through data-driven solutions.

