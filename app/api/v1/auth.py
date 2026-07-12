from fastapi import APIRouter

from app.api.deps import DBSession
from app.exceptions.auth import InvalidCredentialsError
from app.schemas.auth import (
    LoginRequest,
    TokenResponse,
)
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    login_data: LoginRequest,
    db: DBSession,
):

    token = AuthService(db).login(login_data)

    return TokenResponse(
        access_token=token,
    )
