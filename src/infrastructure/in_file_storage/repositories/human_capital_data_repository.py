from src.domain.entities.human_capital_data_entity import HumanCapitalDataEntity

class HumanCapitalDataRepository:
    file_path = './db/human_capital_data.csv'

    def count(self):
        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            count = len(csv_file.readlines()) - 1

            csv_file.close()

            return count

    def get_data_by_id(self, data_id: int):
        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            for data_line in csv_file.readlines()[1:]:
                data_fields = data_line.strip().split(',')

                if int(data_fields[0]) != data_id:
                    continue

                human_data_entity = HumanCapitalDataEntity({
                    'id': int(data_fields[0]),
                    'month': data_fields[1],
                    'colaboradores_lgbtqia': int(data_fields[2]),
                    'colaboradores_negros': int(data_fields[3]),
                    'colaboradoras_mulheres': int(data_fields[4]),
                    'idade_media_colaboradores': int(data_fields[5]),
                    'colaboradores_pcd': int(data_fields[6]),
                    'colaboradores_minorizados': int(data_fields[7]),
                    'mulheres_lideranca_tecnica': int(data_fields[8]),
                    'mulheres_media_lideranca': int(data_fields[9]),
                    'mulheres_alta_lideranca': int(data_fields[10]),
                    'pessoas_negras_lideranca_tecnica': int(data_fields[11]),
                    'pessoas_negras_media_lideranca': int(data_fields[12]),
                    'pessoas_negras_alta_lideranca': int(data_fields[13]),
                    'total_colaboradores': int(data_fields[14]),
                    'total_estagiarios': int(data_fields[15]),
                    'pcds': int(data_fields[16]),
                    'pessoas_pardas': int(data_fields[17]),
                    'pessoas_pretas': int(data_fields[18]),
                    'mulheres': int(data_fields[19]),
                    'cinquenta_mais': int(data_fields[20]),
                    'e_nps': float(data_fields[21]),
                    'turnover_ate_julho_2022': float(data_fields[22]),
                    'indice_recrutamento_interno': float(data_fields[23]),
                    'vagas_recrutamento_interno': float(data_fields[24]),
                    'detalhes_organizacionais': float(data_fields[25]),
                    'periodo_frequencia_relatorio': float(data_fields[26]),
                })

                return human_data_entity

            csv_file.close()

            return None

    def create_data(self, human_capital_data_entity: HumanCapitalDataEntity):
        with open(self.file_path, 'a', encoding='utf8') as csv_file:
            human_capital_values = human_capital_data_entity.values()

            converted_values = map(str, human_capital_values)

            line = ','.join(converted_values)

            data_line = f"\n{line}"

            csv_file.write(data_line)

            csv_file.close()

            return human_capital_data_entity

    def list_data(self):
        data_list = []

        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            for data_line in csv_file.readlines()[1:]:
                data_fields = data_line.strip().split(',')

                data_entity = HumanCapitalDataEntity({
                    'id': int(data_fields[0]),
                    'month': data_fields[1],
                    'colaboradores_lgbtqia': int(data_fields[2]),
                    'colaboradores_negros': int(data_fields[3]),
                    'colaboradoras_mulheres': int(data_fields[4]),
                    'idade_media_colaboradores': int(data_fields[5]),
                    'colaboradores_pcd': int(data_fields[6]),
                    'colaboradores_minorizados': int(data_fields[7]),
                    'mulheres_lideranca_tecnica': int(data_fields[8]),
                    'mulheres_media_lideranca': int(data_fields[9]),
                    'mulheres_alta_lideranca': int(data_fields[10]),
                    'pessoas_negras_lideranca_tecnica': int(data_fields[11]),
                    'pessoas_negras_media_lideranca': int(data_fields[12]),
                    'pessoas_negras_alta_lideranca': int(data_fields[13]),
                    'total_colaboradores': int(data_fields[14]),
                    'total_estagiarios': int(data_fields[15]),
                    'pcds': int(data_fields[16]),
                    'pessoas_pardas': int(data_fields[17]),
                    'pessoas_pretas': int(data_fields[18]),
                    'mulheres': int(data_fields[19]),
                    'cinquenta_mais': int(data_fields[20]),
                    'e_nps': float(data_fields[21]),
                    'turnover_ate_julho_2022': float(data_fields[22]),
                    'indice_recrutamento_interno': float(data_fields[23]),
                    'vagas_recrutamento_interno': float(data_fields[24]),
                    'detalhes_organizacionais': float(data_fields[25]),
                    'periodo_frequencia_relatorio': float(data_fields[26]),
                })

                data_list.append(data_entity)

            csv_file.close()

        return data_list
