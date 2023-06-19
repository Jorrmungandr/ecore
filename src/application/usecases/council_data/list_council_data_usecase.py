from src.infrastructure.in_file_storage.repositories.council_data_repository import CouncilDataRepository

class ListCouncilDataUsecase:
    def __init__(self):
        self.repository = CouncilDataRepository()

    def execute(self):
        return self.repository.list_data()
