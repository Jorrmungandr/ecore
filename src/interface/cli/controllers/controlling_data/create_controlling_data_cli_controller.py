from schematics.exceptions import DataError

from src.application.usecases.controlling_data.create_controlling_data_usecase import CreateControllingDataUsecase

from src.domain.controllers.cli_controller import CLIController

from src.infrastructure.cli.helpers.clear_console import clear_console
from src.infrastructure.helpers.authorize import authorize

@authorize('admin', 'controladoria')
class CreateControllingDataCLIController(CLIController):
    def __init__(self):
        self.usecase = CreateControllingDataUsecase()

    def execute(self):
        try:
            controlling_data_dto = {}

            controlling_data_dto['month'] = input('Digite o mês ao qual os dados correspondem (MM/AAAA): ')
            controlling_data_dto['ebitda'] = float(input('Digite o EBITDA: '))
            controlling_data_dto['faturamento'] = float(input('Digite o faturamento: '))

            result = self.usecase.execute(controlling_data_dto)

            clear_console()
            print('Dados da Controladoria cadastrados com sucesso:\n')

            return result
        except DataError as error:
            print(f'\nErro de validação de parâmetro: {", ".join(error.to_primitive().keys())}')
        except ValueError:
            print('\nValor inválido inserido')
