from src.infrastructure.in_file_storage.repositories.human_capital_data_repository import HumanCapitalDataRepository

class ListHumanCapitalDataUsecase:
    def __init__(self):
        self.repository = HumanCapitalDataRepository()

    def execute(self):
        return self.repository.list_data()
