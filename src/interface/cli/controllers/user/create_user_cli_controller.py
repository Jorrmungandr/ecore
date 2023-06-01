from getpass import getpass

from src.application.exceptions.user.invalid_params_exception import InvalidParamsException
from src.application.exceptions.user.invalid_confirm_password_exception import InvalidConfirmPasswordException

from src.application.usecases.user.create_user_usecase import CreateUserUsecase

from src.infrastructure.cli.helpers.clear_console import clear_console

class CreateUserCLIController:
    def __init__(self):
        self.usecase = CreateUserUsecase()

    def execute(self):
        try:
            name = input('Digite o nome: ')
            email = input('Digite o email: ')
            role = input('Digite o tipo de usuário: ')
            password = getpass('Digite a senha: ')
            confirm_password = getpass('Confirme a senha: ')

            result = self.usecase.execute(name, role, email, password, confirm_password)

            clear_console()
            print('Usuário criado com sucesso:')
            print(f'{result}\n')

            return result
        except InvalidParamsException as error:
            print(f'Erro de validação de parâmetro: {error.message}')
        except InvalidConfirmPasswordException:
            print('A confirmação de senha está diferente da senha')
