from src.application.exceptions.user.invalid_confirm_password_exception import InvalidConfirmPasswordException
from src.application.exceptions.user.user_already_exists_exception import UserAlreadyExistsException

from src.infrastructure.in_file_storage.repositories.user_repository import UserRepository

from src.domain.entities.user_entity import UserEntity

class CreateUserUsecase:
    def __init__(self):
        self.repository = UserRepository()

    def execute(self, name, role, email, password, confirm_password):
        user_count = self.repository.count()

        user_to_create = UserEntity({
            'id': user_count + 1,
            'name': name,
            'role': role,
            'email': email,
            'password': password
        })

        user_to_create.validate()

        if password != confirm_password:
            raise InvalidConfirmPasswordException('As senhas estão diferentes')

        user_already_exists = self.repository.get_user_by_email(email)

        if user_already_exists:
            raise UserAlreadyExistsException('Um usuário com esse email já está cadastrado')

        return self.repository.create_user(user_to_create)
