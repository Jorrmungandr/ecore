from tabulate import tabulate
from schematics.exceptions import DataError

from src.application.usecases.human_capital_data.list_human_capital_data_usecase import ListHumanCapitalDataUsecase

from src.domain.controllers.cli_controller import CLIController
from src.domain.entities.human_capital_data_entity import HumanCapitalDataEntity

from src.infrastructure.cli.helpers.clear_console import clear_console
from src.infrastructure.helpers.authorize import authorize


@authorize('admin', 'capital_humano')
class ListHumanCapitalDataCLIController(CLIController):
    def __init__(self):
        self.usecase = ListHumanCapitalDataUsecase()

    def execute(self):
        try:
            result: list[HumanCapitalDataEntity] = self.usecase.execute()

            raw_data = list(map(lambda entity: entity.values(), result))

            clear_console()

            print('Dados de Capital Humano\n')

            print(tabulate(raw_data, tablefmt='orgtbl', headers=[
                'id',
                'cl',
                'cn',
                'cm',
                'imc',
                'cp',
                'cmi',
                'mlt',
                'mml',
                'mal',
                'nlt',
                'nml',
                'nat',
                'tc',
                'te',
                'p',
                'pp',
                'pp',
                'm',
                'cm',
                'e',
                't',
                'i',
                'v',
                'd',
                'p',
            ]))

            return result
        except DataError as error:
            print(
                f'\nErro de validação de parâmetro: {", ".join(error.to_primitive().keys())}')
        except ValueError:
            print('\nValor inválido inserido')
