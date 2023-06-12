from src.interface.cli.controllers.facilities_data.create_facilities_data_cli_controller import CreateFacilitiesDataCLIController
from src.interface.cli.controllers.facilities_data.list_facilities_data_cli_controller import ListFacilitiesDataCLIController

facilities_data_tree = {
    'create': CreateFacilitiesDataCLIController(),
    'read': ListFacilitiesDataCLIController(),
}
