import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

models = genai.list_models()
for m in models:
    print(f"Name: {m.name}, Type: {m.model_type}, Supported Methods: {m.supported_generation_methods}")
