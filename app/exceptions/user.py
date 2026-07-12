from fastapi import status

from app.exceptions.base import AppException


class UserAlreadyExistsError(AppException):
    def __init__(self):

        super().__init__(
            message="Email already registered",
            status_code=status.HTTP_409_CONFLICT,
        )


class UserNotFoundError(AppException):
    def __init__(self):

        super().__init__(
            message="User not found",
            status_code=status.HTTP_404_NOT_FOUND,
        )
