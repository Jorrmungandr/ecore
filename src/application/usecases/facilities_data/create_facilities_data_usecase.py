from src.infrastructure.in_file_storage.repositories.facilities_data_repository import FacilitiesDataRepository

from src.domain.entities.facilities_data_entity import FacilitiesDataEntity

from src.application.exceptions.data.data_already_exists_exception import DataAlreadyExistsException

class CreateFacilitiesDataUsecase:
    def __init__(self):
        self.repository = FacilitiesDataRepository()

    def execute(self, facilities_data_dto):
        facilities_data_already_exists = self.repository.get_data_by_month(facilities_data_dto['month'])

        if facilities_data_already_exists is not None:
            raise DataAlreadyExistsException("Já existe um dado para esse mês")

        facilities_data_count = self.repository.count()

        facilities_data_to_create = FacilitiesDataEntity({
            'id': facilities_data_count + 1,
            **facilities_data_dto,
        })

        facilities_data_to_create.validate()

        created_data = self.repository.create_data(facilities_data_to_create)

        return created_data
