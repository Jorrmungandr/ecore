from src.application.exceptions.user.invalid_params_exception import InvalidParamsException
from src.application.exceptions.user.invalid_confirm_password_exception import InvalidConfirmPasswordException
from src.application.exceptions.auth.user_not_found_exception import UserNotFoundException

from src.application.usecases.user.update_user_usecase import UpdateUserUsecase

class UpdateUserCLIController:
    def __init__(self):
        self.usecase = UpdateUserUsecase()

    def execute(self):
        try:
            _id = int(input('Digite o id do usuário a ser atualizado: '))
            name = input('Digite o novo nome (para manter o mesmo, deixe esse campo em branco): ')
            email = input('Digite o novo email (para manter o mesmo, deixe esse campo em branco): ')

            result = self.usecase.execute(_id, name, email)

            print('Usuário atualizado com sucesso!')
            print(result)

            return result
        except InvalidParamsException as error:
            print(f'Erro de validação de parâmetro: {error.message}')
        except UserNotFoundException:
            print('Usuário não encontrado.')
