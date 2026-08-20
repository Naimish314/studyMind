import os

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "StudyMind backend is running!",
        "environment": os.getenv("ENVIRONMENT")
    }