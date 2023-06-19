from tabulate import tabulate
from schematics.exceptions import DataError

from src.application.usecases.controlling_data.list_controlling_data_usecase import ListControllingDataUsecase

from src.domain.controllers.cli_controller import CLIController
from src.domain.entities.controlling_data_entity import ControllingDataEntity

from src.infrastructure.cli.helpers.clear_console import clear_console
from src.infrastructure.helpers.authorize import authorize


@authorize('admin', 'controladoria')
class ListControllingDataCLIController(CLIController):
    def __init__(self):
        self.usecase = ListControllingDataUsecase()

    def execute(self):
        try:
            result: list[ControllingDataEntity] = self.usecase.execute()

            raw_data = list(map(lambda entity: entity.values(), result))

            clear_console()

            print('Dados da Controladoria\n')

            print(tabulate(raw_data, tablefmt='github', headers=[
                'ID',
                'mês',
                'ebitda',
                'faturamento',
            ]))

            return result
        except DataError as error:
            print(
                f'\nErro de validação de parâmetro: {", ".join(error.to_primitive().keys())}')
