import streamlit as st
import google.generativeai as genai

# -- API Key Setup --
# আপনার আগের সেই সচল API Key-টি নিচের কোটেশনের ভেতর বসিয়ে দিন
# API_KEY line-ti ekeebare faka kore din erokom:
API_KEY = ""

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-3.8-flash") # ২০২৬ সালের সবচেয়ে স্টেবল ও ফাস্ট মডেল

st.set_page_config(page_title="Medical Assistant App", layout="centered")
st.title("Ahmad Medical Assistant App")

user_input = st.text_area("Chief Complaints (Bangla-te):", placeholder="এখানে বাংলায় রোগের লক্ষণ লিখুন...")

if st.button("Generate Medical Terms & Tests", type="primary"):
    if not user_input.strip():
        st.warning("Anugroho kore kichu likhun!")
    else:
        prompt = f"""
        You are a highly professional clinical medical assistant. 
        Analyze the patient complaints provided in Bangla and output exactly two distinct sections:
        1. Clinical English Terms (C/C): Standard clinical terms for prescription.
        2. Suggestive Diagnostic Tests: Relevant diagnostic or imaging tests (e.g., CBC, USG) as a checklist.
        
        Patient Complaint: "{user_input}"
        """
        
        # ফোনে যেন লোডিং বুঝতে সুবিধা হয়, তাই স্পিনার যুক্ত করা হলো
        with st.spinner("AI Processing... Please wait"):
            try:
                response = model.generate_content(prompt)
                st.subheader("📋 Output:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
