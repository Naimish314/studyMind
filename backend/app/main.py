from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.core.config import APP_NAME, ENVIRONMENT

app = FastAPI(title=APP_NAME)


@app.get("/")
def home():
    return {
        "message": "StudyMind backend is running!",
        "environment": ENVIRONMENT
    }


app.include_router(health_router)