from getpass import getpass

from src.application.exceptions.auth.user_not_found_exception import UserNotFoundException
from src.application.exceptions.auth.invalid_credentials_exception import InvalidCredentialsException

from src.application.usecases.auth.login_usecase import LoginUsecase

from src.infrastructure.cli.helpers.clear_console import clear_console

class LoginCLIController:
    def __init__(self):
        self.usecase = LoginUsecase()

    def execute(self):
        try:
            clear_console()
            print('Login\n')

            email = input('Digite o seu email: ')
            password = getpass('Digite a sua senha: ')

            result = self.usecase.execute(email, password)

            print(result)

            return result
        except UserNotFoundException:
            print('Credenciais Inválidas')
        except InvalidCredentialsException:
            print('Credenciais Inválidas')
