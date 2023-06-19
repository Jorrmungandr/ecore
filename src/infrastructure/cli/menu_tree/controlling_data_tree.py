from src.interface.cli.controllers.controlling_data.create_controlling_data_cli_controller import CreateControllingDataCLIController
from src.interface.cli.controllers.controlling_data.list_controlling_data_cli_controller import ListControllingDataCLIController

controlling_data_tree = {
    'create': CreateControllingDataCLIController(),
    'read': ListControllingDataCLIController(),
}
