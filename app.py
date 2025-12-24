import os
from dotenv import load_dotenv
import streamlit as st
import PyPDF2
from openai import OpenAI
import pdf2image
from PIL import Image
import pytesseract  


load_dotenv()


client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)


def get_groq_response(resume_text, job_description, prompt):
    full_input = f"Resume:\n{resume_text}\n\nJob Description:\n{job_description}\n\nInstructions:\n{prompt}"
    response = client.responses.create(
        input=full_input,
        model="openai/gpt-oss-20b",  # Groq-supported model
    )
    return response.output_text


def extract_pdf_text(uploaded_file):
    """
    Extract text from PDF. If normal text PDF, use PyPDF2.
    If scanned PDF, fallback to OCR using pytesseract.
    """
    try:
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        if text.strip():
            return text
        else:
            
            uploaded_file.seek(0)  # Reset file pointer
            images = pdf2image.convert_from_bytes(uploaded_file.read())
            ocr_text = ""
            for img in images:
                ocr_text += pytesseract.image_to_string(img)
            return ocr_text
    except:
        
        uploaded_file.seek(0)
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        ocr_text = ""
        for img in images:
            ocr_text += pytesseract.image_to_string(img)
        return ocr_text


st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

job_description = st.text_area("Job Description:", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage Match")


input_prompt1 = """
You are an experienced Technical Human Resource Manager.
Review the provided resume against the job description.
Evaluate whether the candidate's profile aligns with the role.
Highlight strengths and weaknesses based on the job requirements.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner.
Evaluate the resume against the job description.
Return:
1. Percentage match
2. Missing keywords
3. Final thoughts
"""


if submit1:
    if uploaded_file is not None:
        resume_text = extract_pdf_text(uploaded_file)
        response = get_groq_response(resume_text, job_description, input_prompt1)
        st.subheader("Analysis")
        st.write(response)
    else:
        st.warning("Please upload a resume PDF")

elif submit3:
    if uploaded_file is not None:
        resume_text = extract_pdf_text(uploaded_file)
        response = get_groq_response(resume_text, job_description, input_prompt3)
        st.subheader("ATS Match Result")
        st.write(response)
    else:
        st.warning("Please upload a resume PDF")
