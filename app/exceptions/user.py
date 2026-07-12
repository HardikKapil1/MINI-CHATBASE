from app.exceptions.base import AppException


class UserAlreadyExistsError(AppException):
    def __init__(self):
        super().__init__("Email already registered")


class UserNotFoundError(AppException):
    def __init__(self):
        super().__init__("User not found")
