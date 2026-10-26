import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Medical Assistant App", layout="centered")
st.title("Ahmad Medical Assistant App")

# স্ট্রিমলিটের ইন্টারনাল সিকিউরিটি থেকে এপিআই কি রিড করবে
if "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    API_KEY = "কোডে কিছু দেওয়া লাগবে না"

user_input = st.text_area("Chief Complaints (Bangla-te):", placeholder="এখানে বাংলায় রোগের লক্ষণ লিখুন...")

if st.button("Generate Medical Terms & Tests", type="primary"):
    if not user_input.strip():
        st.warning("Anugroho kore complaints likhun!")
    else:
        with st.spinner("AI Processing... Please wait"):
            try:
                genai.configure(api_key=API_KEY)
                model = genai.GenerativeModel("gemini-3.8-flash")
                
                prompt = f"""
                You are a highly professional clinical medical assistant. 
                Analyze the patient complaints provided in Bangla and output exactly two distinct sections:
                1. Clinical English Terms (C/C): Standard clinical terms for prescription.
                2. Suggestive Diagnostic Tests: Relevant diagnostic or imaging tests (e.g., CBC, USG) as a checklist.
                
                Patient Complaint: "{user_input}"
                """
                
                response = model.generate_content(prompt)
                st.subheader("📋 Output:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error occurred: {e}")
