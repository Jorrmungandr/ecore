from src.infrastructure.in_file_storage.repositories.council_data_repository import CouncilDataRepository

from src.domain.entities.council_data_entity import CouncilDataEntity

from src.application.exceptions.data.data_already_exists_exception import DataAlreadyExistsException

class CreateCouncilDataUsecase:
    def __init__(self):
        self.repository = CouncilDataRepository()

    def execute(self, council_data_dto):
        council_data_already_exists = self.repository.get_data_by_month(council_data_dto['month'])

        if council_data_already_exists is not None:
            raise DataAlreadyExistsException("Já existe um dado para esse mês")

        council_data_count = self.repository.count()

        council_data_to_create = CouncilDataEntity({
            'id': council_data_count + 1,
            **council_data_dto,
        })

        council_data_to_create.validate()

        created_data = self.repository.create_data(council_data_to_create)

        return created_data
