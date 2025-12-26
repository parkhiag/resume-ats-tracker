# End-to-End Resume ATS Tracker

**End-to-End Resume ATS Tracker** is an interactive web application that evaluates resumes for Applicant Tracking System (ATS) compatibility. It provides automated scoring and feedback on formatting, keywords, and technical skills, helping candidates optimize their resumes.

## Key Features

- Analyze resumes for ATS compatibility using AI (Groq/OpenAI LLM)
- Automated scoring of formatting, keyword usage, and technical skills
- User-friendly interface built with Streamlit
- Quick, actionable recommendations to improve resume quality

## Tech Stack

- **Python**  
- **Streamlit** for the frontend  
- **Groq/OpenAI LLM** for AI-based resume analysis  
- **REST API** for backend AI communication  

## How to Run

1. Clone the repository:  
   ```bash
   git clone https://github.com/parkhiag/resume-ats-tracker.git
2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
3. **Add your API key in a .env file**  
   ```bash
   GROQ_API_KEY=your_api_key_here
4. **Run the app**  
   ```bash
   streamlit run app.py     
