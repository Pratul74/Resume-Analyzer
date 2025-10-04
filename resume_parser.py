import PyPDF2
import docx2txt
import os

def extract_text_from_pdf(file_path):
    text=""
    with open(file_path, "rb") as f:
        reader=PyPDF2.PdfReader(f)
        for page in reader.pages:
            text+=page.extract_text() or ""
    return text