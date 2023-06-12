from src.infrastructure.in_file_storage.repositories.facilities_data_repository import FacilitiesDataRepository

class ListFacilitiesDataUsecase:
    def __init__(self):
        self.repository = FacilitiesDataRepository()

    def execute(self):
        return self.repository.list_data()
