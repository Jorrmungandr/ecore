from schematics.exceptions import DataError

from src.application.usecases.human_capital_data.create_human_capital_data_usecase import CreateHumanCapitalDataUsecase

from src.application.exceptions.data.data_already_exists_exception import DataAlreadyExistsException

from src.domain.controllers.cli_controller import CLIController

from src.infrastructure.cli.helpers.clear_console import clear_console
from src.infrastructure.helpers.authorize import authorize

@authorize('admin', 'capital_humano')
class CreateHumanCapitalDataCLIController(CLIController):
    def __init__(self):
        self.usecase = CreateHumanCapitalDataUsecase()

    def execute(self):
        try:
            human_capital_data_dto = {}

            human_capital_data_dto['month'] = input('Digite o mês ao qual os dados correspondem (MM/AAAA): ')
            human_capital_data_dto['colaboradores_lgbtqia'] = int(input('Digite o número de colaboradores LGBTQIA+: '))
            human_capital_data_dto['colaboradores_negros'] = int(input('Digite o número de colaboradores negros: '))
            human_capital_data_dto['colaboradoras_mulheres'] = int(input('Digite o número de colaboradoras mulheres: '))
            human_capital_data_dto['idade_media_colaboradores'] = int(input('Digite a idade média dos colaboradores: '))
            human_capital_data_dto['colaboradores_pcd'] = int(input('Digite o número de colaboradores PCD: '))
            human_capital_data_dto['colaboradores_minorizados'] = int(input('Digite o número de colaboradores minorizados: '))
            human_capital_data_dto['mulheres_lideranca_tecnica'] = int(input('Digite o número de mulheres na liderança técnica: '))
            human_capital_data_dto['mulheres_media_lideranca'] = int(input('Digite o número de mulheres na média liderança: '))
            human_capital_data_dto['mulheres_alta_lideranca'] = int(input('Digite o número de mulheres na alta liderança: '))
            human_capital_data_dto['pessoas_negras_lideranca_tecnica'] = int(input('Digite o número de pessoas negras na liderança técnica: '))
            human_capital_data_dto['pessoas_negras_media_lideranca'] = int(input('Digite o número de pessoas negras na média liderança: '))
            human_capital_data_dto['pessoas_negras_alta_lideranca'] = int(input('Digite o número de pessoas negras na alta liderança: '))
            human_capital_data_dto['total_colaboradores'] = int(input('Digite o total de colaboradores: '))
            human_capital_data_dto['total_estagiarios'] = int(input('Digite o total de estagiários: '))
            human_capital_data_dto['pcds'] = int(input('Digite o total de PCDs: '))
            human_capital_data_dto['pessoas_pardas'] = int(input('Digite o total de pessoas pardas: '))
            human_capital_data_dto['pessoas_pretas'] = int(input('Digite o total de pessoas pretas: '))
            human_capital_data_dto['mulheres'] = int(input('Digite o total de mulheres: '))
            human_capital_data_dto['cinquenta_mais'] = int(input('Digite o total de colaboradores com 50 anos ou mais: '))
            human_capital_data_dto['e_nps'] = float(input('Digite o valor do e-NPS: '))
            human_capital_data_dto['turnover_ate_julho_2022'] = float(input('Digite o valor do turnover até julho de 2022: '))
            human_capital_data_dto['indice_recrutamento_interno'] = float(input('Digite o valor do índice de recrutamento interno: '))
            human_capital_data_dto['vagas_recrutamento_interno'] = float(input('Digite o valor das vagas de recrutamento interno: '))
            human_capital_data_dto['detalhes_organizacionais'] = float(input('Digite o valor dos detalhes organizacionais: '))
            human_capital_data_dto['periodo_frequencia_relatorio'] = float(input('Digite o valor do período de frequência do relatório: '))

            result = self.usecase.execute(human_capital_data_dto)

            clear_console()
            print('Dados de Capital Humano cadastrados com sucesso:\n')

            return result
        except DataError as error:
            print(f'\nErro de validação de parâmetro: {", ".join(error.to_primitive().keys())}')
        except ValueError:
            print('\nValor inválido inserido')
        except DataAlreadyExistsException:
            print('\n Já existe um dado cadastrado para esse mês')