from src.application.exceptions.auth.user_not_found_exception import UserNotFoundException

from src.application.usecases.user.delete_user_usecase import DeleteUserUsecase
from src.domain.controllers.cli_controller import CLIController
from src.infrastructure.helpers.authorize import authorize

@authorize('admin')
class DeleteUserCLIController(CLIController):
    def __init__(self):
        self.usecase = DeleteUserUsecase()

    def execute(self):
        try:
            _id = int(input("Digite o id do usuário: "))

            self.usecase.execute(_id)

            print("\nUsuário excluído com sucesso")
        except UserNotFoundException:
            print("Usuário não encontrado")
        except ValueError:
            print("Valor do id inválido")
