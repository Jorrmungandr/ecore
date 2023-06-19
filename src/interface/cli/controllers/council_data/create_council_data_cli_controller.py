from schematics.exceptions import DataError

from src.application.usecases.council_data.create_council_data_usecase import CreateCouncilDataUsecase

from src.domain.controllers.cli_controller import CLIController

from src.infrastructure.cli.helpers.clear_console import clear_console
from src.infrastructure.helpers.authorize import authorize

@authorize('admin', 'conselho')
class CreateCouncilDataCLIController(CLIController):
    def __init__(self):
        self.usecase = CreateCouncilDataUsecase()

    def execute(self):
        try:
            council_data_dto = {}

            council_data_dto['month'] = input('Digite o mês ao qual os dados correspondem (MM/AAAA): ')
            council_data_dto['presidente_conselho'] = input('Digite o nome do presidente do conselho: ')
            council_data_dto['governanca_estrutura_composicao'] = input('Digite a composição da estrutura de governança: ')
            council_data_dto['papel_presidente_conselho_gestao_impacto'] = input('Digite o papel do presidente do conselho na gestão de impacto: ')
            council_data_dto['delegacao_responsabilidade_gestao_impacto'] = input('Digite a delegação de responsabilidade na gestão de impacto: ')

            result = self.usecase.execute(council_data_dto)

            clear_console()
            print('Dados do Conselho cadastrados com sucesso:\n')

            return result
        except DataError as error:
            print(f'\nErro de validação de parâmetro: {", ".join(error.to_primitive().keys())}')
        except ValueError:
            print('\nValor inválido inserido')
