from src.domain.entities.marketing_data_entity import MarketingDataEntity

class MarketingDataRepository:
    file_path = './db/marketing_data.csv'

    def count(self) -> int:
        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            count = len(csv_file.readlines()) - 1

            csv_file.close()

            return count

    def get_data_by_month(self, month: str) -> MarketingDataEntity | None:
        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            for data_line in csv_file.readlines()[1:]:
                data_fields = data_line.strip().split(',')

                if data_fields[1] != month:
                    continue

                marketing_data_entity = MarketingDataEntity({
                    'id': float(data_fields[0]),
                    'month': data_fields[1],
                    'quantidade_empresas': int(data_fields[2]),
                    'projetos_executados_por_ano': int(data_fields[3]),
                    'nota_glassdoor': float(data_fields[4]),
                    'recomendam_cesar_amigo': float(data_fields[5]),
                    'perspectiva_positiva_cesar': float(data_fields[6]),
                    'indice_sistema_b': float(data_fields[7]),
                    'comunicacao_questoes_chave': data_fields[8],
                    'atividades': data_fields[9],
                })

                return marketing_data_entity

            csv_file.close()

            return None

    def get_data_by_id(self, data_id: float) -> MarketingDataEntity | None:
        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            for data_line in csv_file.readlines()[1:]:
                data_fields = data_line.strip().split(',')

                if float(data_fields[0]) != data_id:
                    continue

                marketing_data_entity = MarketingDataEntity({
                    'id': float(data_fields[0]),
                    'month': data_fields[1],
                    'quantidade_empresas': int(data_fields[2]),
                    'projetos_executados_por_ano': int(data_fields[3]),
                    'nota_glassdoor': float(data_fields[4]),
                    'recomendam_cesar_amigo': float(data_fields[5]),
                    'perspectiva_positiva_cesar': float(data_fields[6]),
                    'indice_sistema_b': float(data_fields[7]),
                    'comunicacao_questoes_chave': data_fields[8],
                    'atividades': data_fields[9],
                })

                return marketing_data_entity

            csv_file.close()

            return None

    def create_data(self, marketing_data_entity: MarketingDataEntity) -> MarketingDataEntity:
        with open(self.file_path, 'a', encoding='utf8') as csv_file:
            marketing_values = marketing_data_entity.values()

            converted_values = map(str, marketing_values)

            line = ','.join(converted_values)

            data_line = f"\n{line}"

            csv_file.write(data_line)

            csv_file.close()

            return marketing_data_entity

    def list_data(self) -> list[MarketingDataEntity]:
        data_list = []

        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            for data_line in csv_file.readlines()[1:]:
                data_fields = data_line.strip().split(',')

                marketing_data_entity = MarketingDataEntity({
                    'id': float(data_fields[0]),
                    'month': data_fields[1],
                    'quantidade_empresas': int(data_fields[2]),
                    'projetos_executados_por_ano': int(data_fields[3]),
                    'nota_glassdoor': float(data_fields[4]),
                    'recomendam_cesar_amigo': float(data_fields[5]),
                    'perspectiva_positiva_cesar': float(data_fields[6]),
                    'indice_sistema_b': float(data_fields[7]),
                    'comunicacao_questoes_chave': data_fields[8],
                    'atividades': data_fields[9],
                })

                data_list.append(marketing_data_entity)

            csv_file.close()

        return data_list
