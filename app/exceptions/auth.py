from fastapi import status

from app.exceptions.base import AppException


class InvalidCredentialsError(AppException):

    def __init__(self):

        super().__init__(
            message="Invalid email or password",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
class TokenExpiredError(AppException):

    def __init__(self):

        super().__init__(
            message="Token has expired",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )        

class InvalidTokenError(AppException):

    def __init__(self):

        super().__init__(
            message="Invalid token",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )