from tabulate import tabulate

from src.application.usecases.user.list_users_usecase import ListUsersUsecase

from src.domain.controllers.cli_controller import CLIController

from src.infrastructure.cli.helpers.clear_console import clear_console
from src.infrastructure.helpers.authorize import authorize

@authorize('admin')
class ListUsersCLIController(CLIController):
    def __init__(self):
        self.usecase = ListUsersUsecase()

    def execute(self):
        result = self.usecase.execute()

        users_without_password = list(map(lambda entity: entity.values()[:-1], result))

        clear_console()

        print('Usuários\n')

        print(tabulate(users_without_password, tablefmt='github', headers=[
            'ID',
            'nome',
            'tipo',
            'email',
        ]))

        return result
