from src.domain.entities.facilities_data_entity import FacilitiesDataEntity

class FacilitiesDataRepository:
    file_path = './db/facilities_data.csv'

    def count(self):
        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            count = len(csv_file.readlines()) - 1

            csv_file.close()

            return count

    def get_data_by_id(self, data_id: float):
        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            for data_line in csv_file.readlines()[1:]:
                data_fields = data_line.strip().split(',')

                if float(data_fields[0]) != data_id:
                    continue

                facilities_data_entity = FacilitiesDataEntity({
                    'id': float(data_fields[0]),
                    'month': data_fields[1],
                    'consumo_mensal_de_energia_eletrica': float(data_fields[2]),
                    'prop_energia_mercado_livre': float(data_fields[3]),
                    'prop_energia_mercado_cativo': float(data_fields[4]),
                    'peso_residuos_solidos': float(data_fields[5]),
                    'gravimetria_residuo_organico': float(data_fields[6]),
                    'gravimetria_residuo_papel': float(data_fields[7]),
                    'gravimetria_residuo_plastico': float(data_fields[8]),
                    'gravimetria_residuo_metais': float(data_fields[9]),
                    'gravimetria_residuo_eletronicos': float(data_fields[10]),
                    'gravimetria_residuo_pilhas': float(data_fields[11]),
                    'prop_residuos_aterrados': float(data_fields[12]),
                    'prop_residuos_reciclados': float(data_fields[13]),
                    'consumo_agua_mes': float(data_fields[14]),
                    'prop_agua_tratada_consumida': float(data_fields[15]),
                    'consumo_combustivel_mes': float(data_fields[16]),
                    'qualidade_ar_trabalho': float(data_fields[17]),
                    'residuos_eletronicos': float(data_fields[18]),
                    'pilhas': int(data_fields[19]),
                })

                return facilities_data_entity

            csv_file.close()

            return None

    def create_data(self, facilities_data_entity: FacilitiesDataEntity):
        with open(self.file_path, 'a', encoding='utf8') as csv_file:
            facilities_values = facilities_data_entity.values()

            converted_values = map(str, facilities_values)

            line = ','.join(converted_values)

            data_line = f"\n{line}"

            csv_file.write(data_line)

            csv_file.close()

            return facilities_data_entity

    def list_data(self):
        data_list = []

        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            for data_line in csv_file.readlines()[1:]:
                data_fields = data_line.strip().split(',')

                data_entity = FacilitiesDataEntity({
                    'id': float(data_fields[0]),
                    'month': data_fields[1],
                    'consumo_mensal_de_energia_eletrica': float(data_fields[2]),
                    'prop_energia_mercado_livre': float(data_fields[3]),
                    'prop_energia_mercado_cativo': float(data_fields[4]),
                    'peso_residuos_solidos': float(data_fields[5]),
                    'gravimetria_residuo_organico': float(data_fields[6]),
                    'gravimetria_residuo_papel': float(data_fields[7]),
                    'gravimetria_residuo_plastico': float(data_fields[8]),
                    'gravimetria_residuo_metais': float(data_fields[9]),
                    'gravimetria_residuo_eletronicos': float(data_fields[10]),
                    'gravimetria_residuo_pilhas': float(data_fields[11]),
                    'prop_residuos_aterrados': float(data_fields[12]),
                    'prop_residuos_reciclados': float(data_fields[13]),
                    'consumo_agua_mes': float(data_fields[14]),
                    'prop_agua_tratada_consumida': float(data_fields[15]),
                    'consumo_combustivel_mes': float(data_fields[16]),
                    'qualidade_ar_trabalho': float(data_fields[17]),
                    'residuos_eletronicos': float(data_fields[18]),
                    'pilhas': int(data_fields[19]),
                })

                data_list.append(data_entity)

            csv_file.close()

        return data_list
