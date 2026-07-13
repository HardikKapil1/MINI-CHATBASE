from fastapi import FastAPI
from app.handlers.exception_handler import register_exception_handlers
from app.api.v1.users import router as users_router
from app.core.config import settings
from app.api.v1.auth import router as auth_router
from app.api.v1.chats import router as chats_router
from app.api.v1.documents import router as documents_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

register_exception_handlers(app)

app.include_router(
    users_router,
    prefix=settings.api_v1_str,
)
app.include_router(
    auth_router,
    prefix=settings.api_v1_str,
)
app.include_router(
    chats_router,
    prefix=settings.api_v1_str,
)
app.include_router(
    documents_router,
    prefix=settings.api_v1_str,
)