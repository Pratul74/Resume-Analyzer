#for interacting and working with PDF files
import PyPDF2

#for interacting and working with DOCX files
import docx2txt

#for interacting with Operating System
import os


#Function to extract the text from PDF using PyPDF2 Library
def extract_text_from_pdf(file_path):
    text=""
    with open(file_path, "rb") as f:
        reader=PyPDF2.PdfReader(f)
        for page in reader.pages:
            text+=page.extract_text() or ""
    return text

#Function to extract the text from DOCX file using docx2txt library
def extracted_text_from_docx(file_path):
    text=docx2txt.process(file_path)
    return text


def extract_resume_text(uploaded_file):
    temp_path=f"temp_{uploaded_file.name}"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if uploaded_file.name.endswith(".pdf"):
        text=extract_text_from_pdf(temp_path)

    elif uploaded_file.name.endswith(".docx"):
        text=extracted_text_from_docx(temp_path)
    
    else:
        text="Unsupported file format. Please upload a PDF or DOCX file."

    os.remove(temp_path)

    return text

