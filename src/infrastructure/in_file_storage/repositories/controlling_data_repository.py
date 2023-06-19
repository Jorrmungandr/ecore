from src.domain.entities.controlling_data_entity import ControllingDataEntity

class ControllingDataRepository:
    file_path = './db/controlling_data.csv'

    def count(self) -> int:
        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            count = len(csv_file.readlines()) - 1

            csv_file.close()

            return count

    def get_data_by_month(self, month: str) -> ControllingDataEntity | None:
        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            for data_line in csv_file.readlines()[1:]:
                data_fields = data_line.strip().split(',')

                if data_fields[1] != month:
                    continue

                controlling_data_entity = ControllingDataEntity({
                    'id': float(data_fields[0]),
                    'month': data_fields[1],
                    'ebitda': float(data_fields[2]),
                    'faturamento': float(data_fields[3]),
                })

                return controlling_data_entity

            csv_file.close()

            return None

    def get_data_by_id(self, data_id: float) -> ControllingDataEntity | None:
        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            for data_line in csv_file.readlines()[1:]:
                data_fields = data_line.strip().split(',')

                if float(data_fields[0]) != data_id:
                    continue

                controlling_data_entity = ControllingDataEntity({
                    'id': float(data_fields[0]),
                    'month': data_fields[1],
                    'ebitda': float(data_fields[2]),
                    'faturamento': float(data_fields[3]),
                })

                return controlling_data_entity

            csv_file.close()

            return None

    def create_data(self, controlling_data_entity: ControllingDataEntity) -> ControllingDataEntity:
        with open(self.file_path, 'a', encoding='utf8') as csv_file:
            controlling_values = controlling_data_entity.values()

            converted_values = map(str, controlling_values)

            line = ','.join(converted_values)

            data_line = f"\n{line}"

            csv_file.write(data_line)

            csv_file.close()

            return controlling_data_entity

    def list_data(self) -> list[ControllingDataEntity]:
        data_list = []

        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            for data_line in csv_file.readlines()[1:]:
                data_fields = data_line.strip().split(',')

                controlling_data_entity = ControllingDataEntity({
                    'id': float(data_fields[0]),
                    'month': data_fields[1],
                    'ebitda': float(data_fields[2]),
                    'faturamento': float(data_fields[3]),
                })

                data_list.append(controlling_data_entity)

            csv_file.close()

        return data_list
