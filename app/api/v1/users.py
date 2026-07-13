from fastapi import APIRouter, Depends
from app.api.deps import DBSession, get_current_user
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.models.user import User

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(
    "/me",
    response_model=UserResponse,
)
def me(
    current_user: User = Depends(get_current_user),
):
    return current_user


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
