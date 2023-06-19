from src.infrastructure.in_file_storage.repositories.controlling_data_repository import ControllingDataRepository

from src.domain.entities.controlling_data_entity import ControllingDataEntity

class CreateControllingDataUsecase:
    def __init__(self):
        self.repository = ControllingDataRepository()

    def execute(self, controlling_data_dto):
        controlling_data_count = self.repository.count()

        controlling_data_to_create = ControllingDataEntity({
            'id': controlling_data_count + 1,
            **controlling_data_dto,
        })

        controlling_data_to_create.validate()

        created_data = self.repository.create_data(controlling_data_to_create)

        return created_data
