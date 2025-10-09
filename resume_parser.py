import os
import re
import nltk
from PyPDF2 import PdfReader
from docx import Document
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def clean_text(text):
    # Lowercase
    text = text.lower()
    # Remove non-alpha characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Tokenize
    words = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    filtered = [w for w in words if w not in stop_words]
    return ' '.join(filtered)

def read_pdf(file_path):
    text = ''
    reader = PdfReader(file_path)
    for page in reader.pages:
        text += page.extract_text()
    return text

def read_docx(file_path):
    text = ''
    doc = Document(file_path)
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def parse_resume(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        return read_pdf(file_path)
    elif ext == '.docx':
        return read_docx(file_path)
    elif ext == '.txt':
        return read_txt(file_path)
    else:
        raise ValueError("Unsupported file format")

# Example usage
if __name__ == "__main__":
    resume_text = parse_resume("example_resume.pdf")
    cleaned_resume = clean_text(resume_text)
    print(cleaned_resume)
