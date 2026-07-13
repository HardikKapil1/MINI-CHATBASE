from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.database import get_db
from app.core.security import decode_access_token
from app.repositories.user_repository import UserRepository
from app.exceptions.auth import InvalidTokenError

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{settings.api_v1_str}/auth/login",
)

TokenDep = Annotated[
    str,
    Depends(oauth2_scheme),
]

DBSession = Annotated[
    Session,
    Depends(get_db),
]


def get_current_user(
    db: DBSession,
    token: TokenDep,
):
    payload = decode_access_token(token)

    user_id = int(payload["sub"])

    user = UserRepository(db).get_by_id(user_id)

    if not user:
        raise InvalidTokenError()

    return user
