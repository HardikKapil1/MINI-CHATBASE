from sqlalchemy.orm import Session
from app.exceptions.auth import InvalidCredentialsError
from app.repositories.user_repository import UserRepository
from app.core.security import (
    verify_password,
    create_access_token,
)
from fastapi.security import OAuth2PasswordRequestForm


class AuthService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def login(
        self,
        form_data: OAuth2PasswordRequestForm,
    ):
        user = self.user_repository.get_by_email(form_data.username)

        if not user:
            raise InvalidCredentialsError()

        if not verify_password(
            form_data.password,
            user.password_hash,
        ):
            raise InvalidCredentialsError()

        token = create_access_token(
            {
                "sub": str(user.id),
            }
        )

        return token
