from sqlalchemy.orm import Session

from app.models.chat import Chat
from app.models.user import User
from app.repositories.chat_repository import ChatRepository
from app.schemas.chat import ChatCreate
from app.exceptions.chat import (
    ChatNotFoundError,
    ChatAccessDeniedError,
)


class ChatService:
    def __init__(self, db: Session):
        self.chat_repository = ChatRepository(db)

    def create_chat(
        self,
        chat_data: ChatCreate,
        current_user: User,
    ) -> Chat:

        chat = Chat(
            name=chat_data.name,
            description=chat_data.description,
            user_id=current_user.id,
        )

        return self.chat_repository.create(chat)

    def get_chat(
        self,
        chat_id: int,
        current_user: User,
    ) -> Chat:

        chat = self.chat_repository.get_by_id(chat_id)

        if not chat:
            raise ChatNotFoundError()

        if chat.user_id != current_user.id:
            raise ChatAccessDeniedError()

        return chat

    def get_my_chats(
        self,
        current_user: User,
    ) -> list[Chat]:

        return self.chat_repository.get_all_by_user(current_user.id)

    def delete_chat(
        self,
        chat_id: int,
        current_user: User,
    ):

        chat = self.get_chat(
            chat_id,
            current_user,
        )

        self.chat_repository.delete(chat)
