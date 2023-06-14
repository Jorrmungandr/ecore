from schematics.exceptions import DataError

from src.application.usecases.marketing_data.create_marketing_data_usecase import CreateMarketingDataUsecase

from src.domain.controllers.cli_controller import CLIController

from src.infrastructure.cli.helpers.clear_console import clear_console
from src.infrastructure.helpers.authorize import authorize

@authorize('admin', 'marketing')
class CreateMarketingDataCLIController(CLIController):
    def __init__(self):
        self.usecase = CreateMarketingDataUsecase()

    def execute(self):
        try:
            marketing_data_dto = {}

            marketing_data_dto['month'] = input('Digite o mês ao qual os dados correspondem (MM/AAAA): ')
            marketing_data_dto['quantidade_empresas'] = int(input('Digite a quantidade de empresas do porto digital: '))
            marketing_data_dto['projetos_executados_por_ano'] = int(input('Digite o número de projetos executados por ano: '))
            marketing_data_dto['nota_glassdoor'] = float(input('Digite a nota do Glassdoor: '))
            marketing_data_dto['recomendam_cesar_amigo'] = float(input('Digite a persentagem de funcionários que recomendam o Cesar como amigo: '))
            marketing_data_dto['perspectiva_positiva_cesar'] = float(input('Digite a perspectiva positiva sobre o Cesar: '))
            marketing_data_dto['indice_sistema_b'] = float(input('Digite o índice Sistema B: '))
            marketing_data_dto['comunicacao_questoes_chave'] = input('Digite a comunicação de questões-chave: ')
            marketing_data_dto['atividades'] = input('Digite as atividades: ')

            result = self.usecase.execute(marketing_data_dto)

            clear_console()
            print('Dados de Marketing cadastrados com sucesso:\n')

            return result
        except DataError as error:
            print(f'\nErro de validação de parâmetro: {", ".join(error.to_primitive().keys())}')
        except ValueError:
            print('\nValor inválido inserido')
