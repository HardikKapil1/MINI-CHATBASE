from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
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
    db: DBSession,
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    token = AuthService(db).login(form_data)

    return TokenResponse(
        access_token=token,
    )
