from tabulate import tabulate
from schematics.exceptions import DataError

from src.application.usecases.council_data.list_council_data_usecase import ListCouncilDataUsecase

from src.domain.controllers.cli_controller import CLIController
from src.domain.entities.council_data_entity import CouncilDataEntity

from src.infrastructure.cli.helpers.clear_console import clear_console
from src.infrastructure.helpers.authorize import authorize


@authorize('admin', 'conselho')
class ListCouncilDataCLIController(CLIController):
    def __init__(self):
        self.usecase = ListCouncilDataUsecase()

    def execute(self):
        try:
            result: list[CouncilDataEntity] = self.usecase.execute()

            raw_data = list(map(lambda entity: entity.values(), result))

            clear_console()

            print('Dados do Conselho\n')

            print(tabulate(raw_data, tablefmt='github', headers=[
                'ID',
                'mês',
                'governanca_estrutura_composicao',
                'presidente_conselho',
                'papel_presidente_conselho_gestao_impacto',
                'delegacao_responsabilidade_gestao_impacto',
            ]))

            return result
        except DataError as error:
            print(
                f'\nErro de validação de parâmetro: {", ".join(error.to_primitive().keys())}')
        except ValueError:
            print('\nValor inválido inserido')
