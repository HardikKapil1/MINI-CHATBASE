from fastapi import APIRouter, Depends, status

from app.api.deps import DBSession, get_current_user
from app.models.user import User
from app.schemas.chat import (
    ChatCreate,
    ChatResponse,
)
from app.services.chat_service import ChatService

router = APIRouter(
    prefix="/chats",
    tags=["Chats"],
)


@router.post(
    "",
    response_model=ChatResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_chat(
    chat: ChatCreate,
    db: DBSession,
    current_user: User = Depends(get_current_user),
):
    return ChatService(db).create_chat(
        chat,
        current_user,
    )


@router.get(
    "",
    response_model=list[ChatResponse],
)
def get_my_chats(
    db: DBSession,
    current_user: User = Depends(get_current_user),
):
    return ChatService(db).get_my_chats(
        current_user,
    )


@router.get(
    "/{chat_id}",
    response_model=ChatResponse,
)
def get_chat(
    chat_id: int,
    db: DBSession,
    current_user: User = Depends(get_current_user),
):
    return ChatService(db).get_chat(
        chat_id,
        current_user,
    )


@router.delete(
    "/{chat_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_chat(
    chat_id: int,
    db: DBSession,
    current_user: User = Depends(get_current_user),
):
    ChatService(db).delete_chat(
        chat_id,
        current_user,
    )
