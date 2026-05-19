import os
import sys
from dotenv import load_dotenv

# Load local environment variables if testing locally
load_dotenv()

# --- CONFIGURATION & SECURITY GATEKEEPER ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash"
DB_NAME = "review_history.db"

if GEMINI_API_KEY == None:
    sys.exit(1)