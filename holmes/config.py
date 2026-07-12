import os

from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = "gemini-2.5-pro"
MAX_STEPS = 25
API_KEY = os.getenv("GEMINI_API_KEY")
