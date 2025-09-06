from langchain_google_genai import ChatGoogleGenerativeAI
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

gemini_llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=GOOGLE_GEMINI_API_KEY)
gemini_chatml = OpenAI(
    api_key=GOOGLE_GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

