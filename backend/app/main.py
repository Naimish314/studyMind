from fastapi import FastAPI

from app.api.v1.routes.health import router as health_router
from app.core.config import APP_NAME, ENVIRONMENT
from app.api.v1.routes.documents import router as documents_router

app = FastAPI(title=APP_NAME)


@app.get("/")
def home():
    return {
        "message": "StudyMind backend is running!",
        "environment": ENVIRONMENT
    }


app.include_router(health_router, prefix="/api/v1")
app.include_router(
    documents_router,
    prefix="/api/v1",
)