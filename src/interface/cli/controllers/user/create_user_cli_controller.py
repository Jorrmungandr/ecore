from getpass import getpass
from schematics.exceptions import DataError

from src.application.exceptions.user.invalid_confirm_password_exception import InvalidConfirmPasswordException
from src.application.exceptions.user.user_already_exists_exception import UserAlreadyExistsException

from src.application.usecases.user.create_user_usecase import CreateUserUsecase

from src.domain.controllers.cli_controller import CLIController

from src.infrastructure.cli.helpers.clear_console import clear_console
from src.infrastructure.helpers.authorize import authorize

@authorize('admin')
class CreateUserCLIController(CLIController):
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
            print('Usuário criado com sucesso:\n')
            print(result)

            return result
        except DataError as error:
            print(f'\nErro de validação de parâmetro: {", ".join(error.to_primitive().keys())}')
        except InvalidConfirmPasswordException:
            print('\nA confirmação de senha está diferente da senha')
        except UserAlreadyExistsException:
            print('\nUm usuário com esse email já está cadastrado no banco')
