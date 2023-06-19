from src.infrastructure.in_file_storage.repositories.marketing_data_repository import MarketingDataRepository

from src.domain.entities.marketing_data_entity import MarketingDataEntity

from src.application.exceptions.data.data_already_exists_exception import DataAlreadyExistsException

class CreateMarketingDataUsecase:
    def __init__(self):
        self.repository = MarketingDataRepository()

    def execute(self, marketing_data_dto):
        marketing_data_already_exists = self.repository.get_data_by_month(marketing_data_dto['month'])

        if marketing_data_already_exists is not None:
            raise DataAlreadyExistsException("Já existe um dado para esse mês")

        marketing_data_count = self.repository.count()

        marketing_data_to_create = MarketingDataEntity({
            'id': marketing_data_count + 1,
            **marketing_data_dto,
        })

        marketing_data_to_create.validate()

        created_data = self.repository.create_data(marketing_data_to_create)

        return created_data
