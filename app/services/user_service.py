class UserService:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_user_info(self):
        return f"User Name: {self.name}, Email: {self.email}"
