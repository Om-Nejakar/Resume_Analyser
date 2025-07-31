
import streamlit as st # for web page
import fitz # This is PyMuPDF (import it like this)
import re # regular expression (extract mail,date,pass, phone no.)
from io import BytesIO #taking the values direclty from the memory with stroing in the disk 
from openai import OpenAI # for conversation
from fpdf import FPDF # to convert text to pdf
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key= api_key,
)

st.title("AI Resume Analyser")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf") #uploading option

if uploaded_file:
    st.success(f"You uploaded: {uploaded_file.name}") # on success message 

    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf") #stream= its neccessary because file is not opened by the disk from local hence it reads directly from the stream byte
    full_text = ""

    for page in doc:
        full_text += page.get_text()

    # emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b',full_text)
    # phone = re.findall(r'\d{10}', full_text)
    # st.write(emails[0])
    # st.write(phone[0])

    st.subheader("📑 Extracted Resume Text (Preview)")
    st.text_area("Contents", full_text, height=300)

    user_prompt = st.text_input("Enter your question or instruction for the resume") #enter the prompt 

    if st.button("Ask AI") and user_prompt:
        with st.spinner("Thinking"):
            response = client.chat.completions.create(
            model="google/gemma-3n-e4b-it:free",  # ai modal used 
            messages=[
                {
                    "role": "user", 
                    "content": f'''{user_prompt}\n\nHere is the resume:\n{full_text} 
                                also Rate my resume out of 10 and explain the rating briefly'''},
                
            ]
        )
        st.success("Response received!")
        content = response.choices[0].message.content
        st.write(content)

        
        def create_pdf_from_text(content):
            pdf = FPDF() #creating the instance of the fpdf
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            content = content.replace('\u2013', '-') #pfdf does not support the unicode hence replace them with other symbol
            content = content.encode('latin-1', 'replace').decode('latin-1')

            lines = content.split('\n')
            for line in lines:
                pdf.multi_cell(0, 10, txt=line)

            # Save to a BytesIO buffer instead of a file
            buffer = BytesIO()
            buffer.write(pdf.output(dest='S').encode('latin1')) 
            buffer.seek(0) # file pointer to the beginning 
            return buffer

        pdf_file = create_pdf_from_text(content)
        st.download_button("📄 Download Suggestions as PDF", pdf_file, file_name="ai_resume_feedback.pdf")
