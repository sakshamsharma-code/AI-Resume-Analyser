# 📄 AI Resume Analyzer with Gemini

This is a powerful AI-based Resume Analyzer built using **Google Gemini**, designed to extract skills, simulate ATS scores, and give intelligent suggestions to job seekers based on their resume and job descriptions.

---

## 🚀 Features

- 🧠 **Gemini-Powered Feedback**: Get improvement suggestions and missing skills.
- 📄 **PDF Resume Parsing**: Extracts content using `PyMuPDF`.
- 🧪 **Simulated ATS Score**: Mimics how applicant tracking systems evaluate resumes.
- 📊 **Skill Match Score**: Compares resume against job requirements.
- ⚙️ **Streamlit Web Interface**: Easy-to-use, interactive frontend.

---

## 🛠️ Technologies Used

- **Frontend**: [Streamlit](https://streamlit.io/)
- **AI Engine**: Google Gemini 2.5 Pro (via `google.generativeai`)
- **PDF Parsing**: `PyMuPDF`
- **Environment Config**: `python-dotenv`

---

## 📁 File Structure
```
├── app.py # Main Streamlit app
├── gemini_helper.py # Gemini-based skill extraction and analysis
├── job_matcher.py # Logic for skill match scoring
├── resume_parser.py # PDF text extractor using PyMuPDF
├── .env # API keys 
```
---

## 🧪 Demo Workflow

1. Upload your **resume** (PDF only).
2. Paste the **job description**.
3. Click **Analyze Resume** to:
   - Extract required skills from JD.
   - Get Gemini-powered suggestions.
   - View ATS score (simulated).
   - See matched vs. missing skills.

---

## 📦 Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/sakshamsharma-code/AI-Resume-Analyser.git
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Create a .env File
```env
GEMINI_API_KEY=your_gemini_api_key
```
You can get a key from: Google AI Studio

## 🏃 Run the Application
```bash
streamlit run app.py
```
Open http://localhost:"your_port" in your browser.

---

## 📋 Requirements File
If you don't already have it, here are the essential packages:

```txt
streamlit
google-generativeai
python-dotenv
PyMuPDF
```

### Create it with:
```bash
pip freeze > requirements.txt
```

---

## License
Licensed under the MIT License.

---

## Author
Developed By Saksham Sharma
