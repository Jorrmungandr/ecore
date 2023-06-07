from src.infrastructure.in_file_storage.repositories.marketing_data_repository import MarketingDataRepository

class ListMarketingDataUsecase:
    def __init__(self):
        self.repository = MarketingDataRepository()

    def execute(self):
        return self.repository.list_data()
