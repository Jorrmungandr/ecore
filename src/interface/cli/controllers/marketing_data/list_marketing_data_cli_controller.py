from tabulate import tabulate
from schematics.exceptions import DataError

from src.application.usecases.marketing_data.list_marketing_data_usecase import ListMarketingDataUsecase

from src.domain.controllers.cli_controller import CLIController
from src.domain.entities.marketing_data_entity import MarketingDataEntity

from src.infrastructure.cli.helpers.clear_console import clear_console
from src.infrastructure.helpers.authorize import authorize


@authorize('admin', 'marketing')
class ListMarketingDataCLIController(CLIController):
    def __init__(self):
        self.usecase = ListMarketingDataUsecase()

    def execute(self):
        try:
            result: list[MarketingDataEntity] = self.usecase.execute()

            raw_data = list(map(lambda entity: entity.values(), result))

            clear_console()

            print('Dados de Marketing\n')

            print(tabulate(raw_data, tablefmt='orgtbl', headers=[
                'quantidade_empresas',
                'projetos_executados',
                'nota_glassdoor',
                'recomendam_cesar',
                'perspectiva_positiva',
                'indice_sistema_b',
                'questoes_chave',
                'atividades',
            ]))

            return result
        except DataError as error:
            print(
                f'\nErro de validação de parâmetro: {", ".join(error.to_primitive().keys())}')
        except ValueError:
            print('\nValor inválido inserido')
