from src.interface.cli.controllers.council_data.create_council_data_cli_controller import CreateCouncilDataCLIController
from src.interface.cli.controllers.council_data.list_council_data_cli_controller import ListCouncilDataCLIController

council_data_tree = {
    'create': CreateCouncilDataCLIController(),
    'read': ListCouncilDataCLIController(),
}
