from src.infrastructure.in_file_storage.repositories.user_repository import UserRepository

class ListUsersUsecase:
    def __init__(self):
        self.repository = UserRepository()

    def execute(self):
        users = self.repository.get_users()

        return users
