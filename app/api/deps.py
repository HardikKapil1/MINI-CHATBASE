from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from fastapi import Depends
from app.core.security import decode_access_token
from app.core.database import get_db
from app.repositories.user_repository import UserRepository

DBSession = Annotated[Session, Depends(get_db)]
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    user_id = decode_access_token(token)
    return UserRepository(db).get_by_id(user_id)
