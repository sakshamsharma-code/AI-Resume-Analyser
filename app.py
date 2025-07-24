import streamlit as st
from resume_parser import extract_text_from_pdf
from gemini_helper import (
    init_gemini,
    get_skill_suggestions,
    extract_skills_from_jd,
    calculate_ats_score_ai
)
from job_matcher import calculate_match_score
from dotenv import load_dotenv
import os

# ---------- ENV + GEMINI ----------
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
init_gemini(GEMINI_API_KEY)

# ---------- UI CONFIG ----------
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
st.markdown("<h1 style='text-align:center;'>AI Resume Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Upload your resume and paste a job description to evaluate your fit, and get AI suggestions.</p>", unsafe_allow_html=True)

# ---------- RESUME UPLOAD ----------
uploaded_file = st.file_uploader("Upload your Resume (PDF format only)", type="pdf")

if uploaded_file:
    with st.spinner("Extracting resume text..."):
        resume_text = extract_text_from_pdf(uploaded_file)
        if not resume_text:
            st.error("Unable to extract text. Please try another file.")
            st.stop()
        st.success("Resume text successfully extracted.")

    with st.expander("View Extracted Resume Text"):
        st.text_area("Resume Content", resume_text, height=300)

    # ---------- JOB DESCRIPTION INPUT ----------
    st.markdown("### Job Description")
    job_description = st.text_area("Paste the job description here", height=200)

    if st.button("Analyze Resume"):
        if not job_description:
            st.warning("Please paste a job description before analyzing.")
        else:
            # ---------- SKILL EXTRACTION ----------
            with st.spinner("Extracting required skills from job description..."):
                required_skills = extract_skills_from_jd(job_description)

            if required_skills is None:
                st.error("Gemini quota exhausted or unavailable.")
                st.stop()

            # ---------- AI ANALYSIS ----------
            with st.spinner("Analyzing your resume with Gemini..."):
                ai_feedback = get_skill_suggestions(resume_text, job_description)

            st.subheader("Gemini Feedback")
            st.write(ai_feedback or "No suggestions available due to quota limits.")



            # ---------- SIMULATED ATS SCORE ----------
            with st.spinner("Calculating simulated ATS score..."):
                ats_result = calculate_ats_score_ai(resume_text, job_description)

            if ats_result:
                st.markdown("### Simulated ATS Score")
                st.success(ats_result)
            else:
                st.warning("Unable to fetch ATS score (Gemini quota may be exhausted).")

            # ---------- MATCH SCORE ----------
            match_score, matched, missing = calculate_match_score(resume_text, required_skills)

            st.markdown("### Resume Match Score")
            st.progress(match_score)
            st.success(f"Match Score: {match_score}%")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**Matched Skills**")
                st.write(", ".join(matched) if matched else "No skills matched.")

            with col2:
                st.markdown("**Missing Skills**")
                st.write(", ".join(missing) if missing else "None")

            # ---------- SUMMARY ----------
            st.markdown("---")
            st.markdown("### Summary")
            st.markdown(f"""
                **Match Score:** {match_score}%  
                **Matched Skills:** {len(matched)}  
                **Missing Skills:** {len(missing)}  
            """)
