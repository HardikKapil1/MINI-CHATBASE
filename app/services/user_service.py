from sqlalchemy.orm import Session
from app.exceptions.user import UserAlreadyExistsError
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.exceptions.user import UserNotFoundError


class UserService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def get_user(self, user_id: int):

        user = self.user_repository.get_by_id(user_id)

        if not user:
            raise UserNotFoundError()

        return user

    def create_user(self, user_data: UserCreate) -> User:

        existing_user = self.user_repository.get_by_email(user_data.email)

        if existing_user:
            raise UserAlreadyExistsError()

        user = User(
            email=user_data.email,
            full_name=user_data.full_name,
            password_hash=user_data.password,  # Temporary
        )

        return self.user_repository.create(user)
