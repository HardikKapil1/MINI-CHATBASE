from fastapi import FastAPI

from app.api.v1.health import router as health_router
from app.core.config import settings
from app.api.v1.users import router as users_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="A Chatbase-like backend built with FastAPI",
)

app.include_router(health_router)
app.include_router(users_router)