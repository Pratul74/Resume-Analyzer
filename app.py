import streamlit as st
from resume_parser import extract_resume_text

st.set_page_config(page_title="AI Resume Analyzer", page_icon="🧠", layout="wide")

st.title("🧠 AI Resume Analyzer")
st.markdown("### Step 1: Upload your resume to extract and view text")

uploaded_file=st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf","docx"])

if uploaded_file is not None:
    with st.spinner("Extracting text...."):
        resume_text=extract_resume_text(uploaded_file)
    st.success("✅ Resume text extracted successfully!")
    st.subheader("📄 Extracted Text: ")
    st.text_area("Resume Content", resume_text, height=400)
else:
    st.info("Please upload your resume to begin.")