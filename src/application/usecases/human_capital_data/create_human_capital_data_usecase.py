from src.infrastructure.in_file_storage.repositories.human_capital_data_repository import HumanCapitalDataRepository

from src.domain.entities.human_capital_data_entity import HumanCapitalDataEntity

from src.application.exceptions.data.data_already_exists_exception import DataAlreadyExistsException

class CreateHumanCapitalDataUsecase:
    def __init__(self):
        self.repository = HumanCapitalDataRepository()

    def execute(self, human_capital_data_dto):
        human_capital_data_already_exists = self.repository.get_data_by_month(human_capital_data_dto['month'])

        if human_capital_data_already_exists is not None:
            raise DataAlreadyExistsException("Já existe um dado para esse mês")

        human_capital_data_count = self.repository.count()

        human_capital_data_to_create = HumanCapitalDataEntity({
            'id': human_capital_data_count + 1,
            **human_capital_data_dto,
        })

        human_capital_data_to_create.validate()

        created_data = self.repository.create_data(human_capital_data_to_create)

        return created_data
