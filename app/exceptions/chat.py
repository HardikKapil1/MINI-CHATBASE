from fastapi import status

from app.exceptions.base import AppException


class ChatNotFoundError(AppException):

    def __init__(self):
        super().__init__(
            message="Chat not found",
            status_code=status.HTTP_404_NOT_FOUND,
        )


class ChatAccessDeniedError(AppException):

    def __init__(self):
        super().__init__(
            message="You do not have access to this chat",
            status_code=status.HTTP_403_FORBIDDEN,
        )