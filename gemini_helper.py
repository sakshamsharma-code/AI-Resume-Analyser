import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

# ---------- Initialize Gemini ----------
def init_gemini(api_key):
    genai.configure(api_key=api_key)

# ---------- Extract Skills from Job Description ----------
def extract_skills_from_jd(jd_text):
    prompt = f"""
    From the following job description, extract the top 10 required technical skills.
    Return only a comma-separated list of skills. No explanation.

    Job Description:
    \"\"\"{jd_text}\"\"\"
    """
    model = genai.GenerativeModel(model_name="gemini-2.5-pro")

    try:
        response = model.generate_content(prompt)
        return [s.strip().lower() for s in response.text.split(",") if s.strip()]
    except ResourceExhausted:
        print("Gemini quota exceeded during skill extraction.")
        return None
    except Exception as e:
        print(f"Gemini error (skills): {e}")
        return None

# ---------- Get AI Suggestions for Resume Improvement ----------
def get_skill_suggestions(resume_text, job_description):
    prompt = f"""
    You are an AI hiring assistant. A candidate is applying for a role based on the job description below.

    Job Description:
    \"\"\"{job_description}\"\"\"

    Resume:
    \"\"\"{resume_text}\"\"\"

    Provide:
    1. Missing important skills
    2. Suggestions to improve their fit for the role
    Return your response in a clear bullet-point format.
    """
    model = genai.GenerativeModel(model_name="gemini-2.5-pro")
    try:
        response = model.generate_content(prompt)
        return response.text
    except ResourceExhausted:
        print("Gemini quota exceeded during suggestion generation.")
        return None
    except Exception as e:
        print(f"Gemini error (suggestions): {e}")
        return None

def calculate_ats_score_ai(resume_text, job_description):
    prompt = f"""
    You are acting as a modern ATS (Applicant Tracking System).

    Given the resume and job description below, evaluate the following aspects and assign a score (out of 100) based on typical ATS criteria:

    1. Hard skill match (40%)
    2. Relevant job titles (15%)
    3. Years of experience (15%)
    4. Education level match (10%)
    5. Relevant certifications (10%)
    6. Soft skills & formatting (10%)

    Return a single final ATS score, followed by a brief explanation (3-5 lines).

    Resume:
    \"\"\"{resume_text}\"\"\"

    Job Description:
    \"\"\"{job_description}\"\"\"  
    """
    try:
        model = genai.GenerativeModel(model_name="gemini-2.5-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("Gemini ATS Error:", e)
        return None
