# 🤖 Smart Resume Screening System

A full-stack AI-powered dashboard for fast, automated resume shortlisting using NLP and Machine Learning—built with Python and Streamlit.

## Features

- **Upload PDF/DOCX/TXT resumes in bulk**
- **Custom job requirements:** Interactive skill, degree, and experience selection
- **Automated parsing & scoring**
- **Leaderboard with candidate ranking**
- **Skill/experience/text extraction**
- **Match score visualization bar chart**
- **Modern, responsive UI; uses centered layout for best fit on any monitor**

## Demo

![<img width="1113" height="730" alt="image" src="https://github.com/user-attachments/assets/06810ebe-546c-4808-afd0-1a5d4c2a1754" />

<img width="1032" height="696" alt="image" src="https://github.com/user-attachments/assets/e18574a8-892b-4be0-8b0e-84c870c52a5a" />

]( your job requirements (skills, degree, minimum years experience)
2. Upload resumes (drag & drop or multiple selection)
3. Instantly see ranked candidates—Leaderboard & Score Chart

## Installation

Clone this repo and install dependencies:
```sh
git clone https://github.com/YOUR-USERNAME/smart-resume-screening.git
cd smart_resume_screening
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
Or manually:
```sh
pip install streamlit matplotlib PyPDF2 python-docx pdfminer.six nltk
```
Download required NLTK data:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## Usage

Start the Streamlit dashboard:
```sh
streamlit run app.py
```
Open the browser link provided by Streamlit.

## Folder Structure

```
├── app.py                  # Streamlit dashboard
├── resume_parser.py        # Resume parsing/cleaning logic
├── README.md
├── requirements.txt
├── resumes/                # Upload directory (optional for batch mode)
```

## How It Works

- **Resume Parsing:** Uses `PyPDF2`, `python-docx`, and `pdfminer.six` to extract text.
- **NLP Feature Extraction:** Matches skills, degrees, experiences from resume against job requirements.
- **Scoring System:** Weighted scoring based on skill overlap, degree match, experience.
- **Dashboard:** User can interactively change filtering criteria; visualize candidate scores.

## Example Job Requirements

- Required skills: `python`, `react`, `machine learning`
- Required degree: `bachelor`
- Minimum experience: `2 years`

## Customization

- Edit skill/degree lists in code for your domain.
- Integrate with advanced models (spaCy, BERT) for deeper extraction.
- Switch to Plotly for fancier charts if desired.

## Contributing

PRs welcome! Open an issue for bugs or features.


password = "test123"

## License

MIT
