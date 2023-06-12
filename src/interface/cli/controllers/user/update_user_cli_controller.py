from schematics.exceptions import DataError

from src.application.exceptions.auth.user_not_found_exception import UserNotFoundException

from src.application.usecases.user.update_user_usecase import UpdateUserUsecase

from src.domain.controllers.cli_controller import CLIController
from src.infrastructure.helpers.authorize import authorize

@authorize('admin')
class UpdateUserCLIController(CLIController):
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
        except DataError as error:
            print(f'\nErro de validação de parâmetro: {", ".join(error.to_primitive().keys())}')
        except UserNotFoundException:
            print('Usuário não encontrado.')
