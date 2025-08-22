# app/services/gemini_service.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL = "gemini-1.5-flash"  # ← updated model

def generate_response(user_message, wa_id=None, name=None):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={GOOGLE_API_KEY}"
    data = {
        "contents": [{"parts": [{"text": f"{user_message}"}]}]
    }
    response = requests.post(url, json=data)
    result = response.json()
    try:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return f"⚠ Error from Gemini API: {result}"
