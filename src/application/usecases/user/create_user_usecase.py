from src.application.exceptions.user.invalid_params_exception import InvalidParamsException
from src.application.exceptions.user.invalid_confirm_password_exception import InvalidConfirmPasswordException
from src.application.exceptions.user.user_already_exists_exception import UserAlreadyExistsException

from src.infrastructure.in_file_storage.repositories.user_repository import UserRepository

from src.domain.entities.user_entity import user_roles

class CreateUserUsecase:
    def __init__(self):
        self.repository = UserRepository()

    def execute(self, name, role, email, password, confirm_password):
        if ',' in name:
            raise InvalidParamsException('Nome inválido')
        if ',' in email:
            raise InvalidParamsException('Email inválido')
        if ',' in password:
            raise InvalidParamsException('Senha inválida')

        if role not in user_roles:
            role_list = "\n".join(list(user_roles))
            raise InvalidParamsException(f'Tipo de usuário inválido, tipos válidos:\n{role_list}')

        if password != confirm_password:
            raise InvalidConfirmPasswordException('As senhas estão diferentes')

        user_already_exists = self.repository.get_user_by_email(email)

        if user_already_exists:
            raise UserAlreadyExistsException('Um usuário com esse email já está cadastrado no banco')

        created_user = self.repository.create_user(name, role, email, password)

        return created_user
