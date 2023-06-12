from src.infrastructure.in_file_storage.repositories.facilities_data_repository import FacilitiesDataRepository

from src.domain.entities.facilities_data_entity import FacilitiesDataEntity

class CreateFacilitiesDataUsecase:
    def __init__(self):
        self.repository = FacilitiesDataRepository()

    def execute(self, facilities_data_dto):
        facilities_data_count = self.repository.count()

        facilities_data_to_create = FacilitiesDataEntity({
            'id': facilities_data_count + 1,
            **facilities_data_dto,
        })

        facilities_data_to_create.validate()

        created_data = self.repository.create_data(facilities_data_to_create)

        return created_data
