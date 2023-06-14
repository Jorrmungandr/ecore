from tabulate import tabulate
from schematics.exceptions import DataError

from src.application.usecases.facilities_data.list_facilities_data_usecase import ListFacilitiesDataUsecase

from src.domain.controllers.cli_controller import CLIController
from src.domain.entities.facilities_data_entity import FacilitiesDataEntity

from src.infrastructure.cli.helpers.clear_console import clear_console
from src.infrastructure.helpers.authorize import authorize


@authorize('admin', 'facilities')
class ListFacilitiesDataCLIController(CLIController):
    def __init__(self):
        self.usecase = ListFacilitiesDataUsecase()

    def execute(self):
        try:
            result: list[FacilitiesDataEntity] = self.usecase.execute()

            raw_data = list(map(lambda entity: entity.values(), result))

            clear_console()

            print('Dados de Facilities\n')

            print(tabulate(raw_data, tablefmt='github', headers=[
                'ID',
                'mês',
                'cmee',
                'peml',
                'pemc',
                'prs',
                'gro',
                'grp',
                'gpl',
                'gm',
                'gre',
                'grpi',
                'pra',
                'prr',
                'cam',
                'patc',
                'ccm',
                'qat',
                're',
                'p',
            ]))

            return result
        except DataError as error:
            print(
                f'\nErro de validação de parâmetro: {", ".join(error.to_primitive().keys())}')
        except ValueError:
            print('\nValor inválido inserido')
