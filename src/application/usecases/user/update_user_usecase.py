
from src.application.exceptions.auth.user_not_found_exception import UserNotFoundException

from src.infrastructure.in_file_storage.repositories.user_repository import UserRepository

from src.domain.entities.user_entity import UserEntity

class UpdateUserUsecase:
    def __init__(self):
        self.repository = UserRepository()

    def execute(self, _id, name, email):
        user_exists = self.repository.get_user_by_id(_id)

        if user_exists is None:
            raise UserNotFoundException('Usuário não encontrado')

        user_to_update = UserEntity({
            'id': _id,
            'name': name or user_exists.name,
            'role': user_exists.role,
            'email': email or user_exists.email,
            'password': user_exists.password
        })

        user_to_update.validate()

        if name == '':
            name = user_exists.name

        if email == '':
            email = user_exists.email

        update_user = self.repository.update_user_by_id(_id, name, email)

        return update_user
