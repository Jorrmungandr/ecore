from src.infrastructure.in_file_storage.repositories.controlling_data_repository import ControllingDataRepository

class ListControllingDataUsecase:
    def __init__(self):
        self.repository = ControllingDataRepository()

    def execute(self):
        return self.repository.list_data()
