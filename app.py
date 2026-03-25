"""
Elimu AI - Hugging Face Spaces Entry Point
This file launches the FastAPI app on Hugging Face Spaces (free hosting).
The Space will be publicly accessible and always online.
"""
import uvicorn
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from api.main import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
