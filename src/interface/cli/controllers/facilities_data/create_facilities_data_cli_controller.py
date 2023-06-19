from schematics.exceptions import DataError

from src.application.usecases.facilities_data.create_facilities_data_usecase import CreateFacilitiesDataUsecase

from src.application.exceptions.data.data_already_exists_exception import DataAlreadyExistsException

from src.domain.controllers.cli_controller import CLIController

from src.infrastructure.cli.helpers.clear_console import clear_console
from src.infrastructure.helpers.authorize import authorize

@authorize('admin', 'facilities')
class CreateFacilitiesDataCLIController(CLIController):
    def __init__(self):
        self.usecase = CreateFacilitiesDataUsecase()

    def execute(self):
        try:
            facilities_data_dto = {}

            facilities_data_dto['month'] = input('Digite o mês ao qual os dados correspondem (MM/AAAA): ')
            facilities_data_dto['consumo_mensal_de_energia_eletrica'] = float(input('Digite o consumo mensal de energia elétrica: '))
            facilities_data_dto['prop_energia_mercado_livre'] = float(input('Digite a proporção de energia do mercado livre: '))
            facilities_data_dto['prop_energia_mercado_cativo'] = float(input('Digite a proporção de energia do mercado cativo: '))
            facilities_data_dto['peso_residuos_solidos'] = float(input('Digite o peso de resíduos sólidos: '))
            facilities_data_dto['gravimetria_residuo_organico'] = float(input('Digite a gravimetria de resíduo orgânico: '))
            facilities_data_dto['gravimetria_residuo_papel'] = float(input('Digite a gravimetria de resíduo de papel: '))
            facilities_data_dto['gravimetria_residuo_plastico'] = float(input('Digite a gravimetria de resíduo de plástico: '))
            facilities_data_dto['gravimetria_residuo_metais'] = float(input('Digite a gravimetria de resíduo de metais: '))
            facilities_data_dto['gravimetria_residuo_eletronicos'] = float(input('Digite a gravimetria de resíduo de eletrônicos: '))
            facilities_data_dto['gravimetria_residuo_pilhas'] = float(input('Digite a gravimetria de resíduo de pilhas: '))
            facilities_data_dto['prop_residuos_aterrados'] = float(input('Digite a proporção de resíduos aterrados: '))
            facilities_data_dto['prop_residuos_reciclados'] = float(input('Digite a proporção de resíduos reciclados: '))
            facilities_data_dto['consumo_agua_mes'] = float(input('Digite o consumo de água por mês: '))
            facilities_data_dto['prop_agua_tratada_consumida'] = float(input('Digite a proporção de água tratada consumida: '))
            facilities_data_dto['consumo_combustivel_mes'] = float(input('Digite o consumo de combustível por mês: '))
            facilities_data_dto['qualidade_ar_trabalho'] = float(input('Digite a qualidade do ar de trabalho: '))
            facilities_data_dto['residuos_eletronicos'] = float(input('Digite a quantidade de resíduos eletrônicos: '))
            facilities_data_dto['pilhas'] = int(input('Digite a quantidade de pilhas: '))

            result = self.usecase.execute(facilities_data_dto)

            clear_console()
            print('Dados de Facilities cadastrados com sucesso:\n')

            return result
        except DataError as error:
            print(f'\nErro de validação de parâmetro: {", ".join(error.to_primitive().keys())}')
        except ValueError:
            print('\nValor inválido inserido')
        except DataAlreadyExistsException:
            print('\n Já existe um dado cadastrado para esse mês')
