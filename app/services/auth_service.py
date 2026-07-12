from sqlalchemy.orm import Session
from app.exceptions.auth import InvalidCredentialsError
from app.schemas.auth import LoginRequest
from app.repositories.user_repository import UserRepository
from app.core.security import (
    verify_password,
    create_access_token,
)


class AuthService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def login(self, login_data: LoginRequest):

        user = self.user_repository.get_by_email(login_data.email)

        if not user:
            raise InvalidCredentialsError()

        if not verify_password(
            login_data.password,
            user.password_hash,
        ):
            raise InvalidCredentialsError()

        token = create_access_token(
            {
                "sub": str(user.id),
            }
        )

        return token
