from src.domain.entities.council_data_entity import CouncilDataEntity

class CouncilDataRepository:
    file_path = './db/council_data.csv'

    def count(self) -> int:
        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            count = len(csv_file.readlines()) - 1

            csv_file.close()

            return count

    def get_data_by_month(self, month: str) -> CouncilDataEntity | None:
        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            for data_line in csv_file.readlines()[1:]:
                data_fields = data_line.strip().split(',')

                if data_fields[1] != month:
                    continue

                council_data_entity = CouncilDataEntity({
                    'id': float(data_fields[0]),
                    'month': data_fields[1],
                    'governanca_estrutura_composicao': data_fields[2],
                    'presidente_conselho': data_fields[3],
                    'papel_presidente_conselho_gestao_impacto': data_fields[4],
                    'delegacao_responsabilidade_gestao_impacto': data_fields[5],
                })

                return council_data_entity

            csv_file.close()

            return None

    def get_data_by_id(self, data_id: float) -> CouncilDataEntity | None:
        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            for data_line in csv_file.readlines()[1:]:
                data_fields = data_line.strip().split(',')

                if float(data_fields[0]) != data_id:
                    continue

                council_data_entity = CouncilDataEntity({
                    'id': float(data_fields[0]),
                    'month': data_fields[1],
                    'governanca_estrutura_composicao': data_fields[2],
                    'presidente_conselho': data_fields[3],
                    'papel_presidente_conselho_gestao_impacto': data_fields[4],
                    'delegacao_responsabilidade_gestao_impacto': data_fields[5],
                })

                return council_data_entity

            csv_file.close()

            return None

    def create_data(self, council_data_entity: CouncilDataEntity) -> CouncilDataEntity:
        with open(self.file_path, 'a', encoding='utf8') as csv_file:
            council_values = council_data_entity.values()

            converted_values = map(str, council_values)

            line = ','.join(converted_values)

            data_line = f"\n{line}"

            csv_file.write(data_line)

            csv_file.close()

            return council_data_entity

    def list_data(self) -> list[CouncilDataEntity]:
        data_list = []

        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            for data_line in csv_file.readlines()[1:]:
                data_fields = data_line.strip().split(',')

                council_data_entity = CouncilDataEntity({
                    'id': float(data_fields[0]),
                    'month': data_fields[1],
                    'governanca_estrutura_composicao': data_fields[2],
                    'presidente_conselho': data_fields[3],
                    'papel_presidente_conselho_gestao_impacto': data_fields[4],
                    'delegacao_responsabilidade_gestao_impacto': data_fields[5],
                })

                data_list.append(council_data_entity)

            csv_file.close()

        return data_list
