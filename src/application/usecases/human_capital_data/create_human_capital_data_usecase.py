from src.infrastructure.in_file_storage.repositories.human_capital_data_repository import HumanCapitalDataRepository

from src.domain.entities.human_capital_data_entity import HumanCapitalDataEntity

class CreateHumanCapitalDataUsecase:
    def __init__(self):
        self.repository = HumanCapitalDataRepository()

    def execute(self, human_capital_data_dto):
        human_capital_data_count = self.repository.count()

        human_capital_data_to_create = HumanCapitalDataEntity({
            'id': human_capital_data_count + 1,
            **human_capital_data_dto,
        })

        human_capital_data_to_create.validate()

        created_data = self.repository.create_data(human_capital_data_to_create)

        return created_data
