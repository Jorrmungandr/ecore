from src.application.exceptions.user.invalid_params_exception import InvalidParamsException
from src.application.exceptions.user.invalid_confirm_password_exception import InvalidConfirmPasswordException
from src.application.exceptions.auth.user_not_found_exception import UserNotFoundException

from src.infrastructure.in_file_storage.repositories.user_repository import UserRepository

class UpdateUserUsecase:
    def __init__(self):
        self.repository = UserRepository()

    def execute(self, _id, name, email):
        if ',' in name:
            raise InvalidParamsException('Nome inválido')
        if ',' in email:
            raise InvalidParamsException('Email inválido')

        user_exists = self.repository.get_user_by_id(_id)

        if user_exists == None:
            raise UserNotFoundException('Usuário não encontrado')

        if name == '':
            name = user_exists.name
        
        if email == '':
            email = user_exists.email

        update_user = self.repository.update_user_by_id(_id, name, email)

        return update_user
