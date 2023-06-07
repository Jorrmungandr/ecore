from src.application.exceptions.auth.user_not_found_exception import UserNotFoundException

from src.application.usecases.user.detail_user_usecase import DetailUserUsecase
from src.domain.controllers.cli_controller import CLIController
from src.infrastructure.helpers.authorize import authorize

@authorize('admin')
class DetailUserCLIController(CLIController):
    def __init__(self):
        self.usecase = DetailUserUsecase()

    def execute(self):
        try:
            _id = int(input("Digite o id do usuário: "))

            result = self.usecase.execute(_id)

            print(result)

            return result
        except UserNotFoundException:
            print("Usuário não encontrado")
        except ValueError:
            print("Valor do id inválido")
