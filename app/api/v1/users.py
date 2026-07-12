from fastapi import APIRouter
from app.exceptions.user import UserNotFoundError
from app.api.deps import DBSession
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(
    "/{user_id}",
    response_model=UserResponse,
)
def get_user(
    user_id: int,
    db: DBSession,
):
    return UserService(db).get_user(user_id)


@router.post(
    "",
    response_model=UserResponse,
    status_code=201,
)
def create_user(
    user: UserCreate,
    db: DBSession,
):
    return UserService(db).create_user(user)
