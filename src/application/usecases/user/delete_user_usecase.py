from src.application.exceptions.auth.user_not_found_exception import UserNotFoundException

from src.infrastructure.in_file_storage.repositories.user_repository import UserRepository

class DeleteUserUsecase:
    def __init__(self):
        self.repository = UserRepository()

    def execute(self, _id):
        user = self.repository.get_user_by_id(_id)

        if user is None:
            raise UserNotFoundException("Usuário não encontrado")

        self.repository.delete_user(_id)
