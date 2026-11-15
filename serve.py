"""
FastAPI static files mounting patch for the Aaple Sarkar bot.
Adds static file serving when main.py runs.
"""
from main import app
from fastapi.staticfiles import StaticFiles
import os

# Mount static files
static_path = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")
