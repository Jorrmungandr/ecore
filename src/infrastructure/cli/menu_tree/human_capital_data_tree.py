from src.interface.cli.controllers.human_capital_data.create_human_capital_data_cli_controller import CreateHumanCapitalDataCLIController
from src.interface.cli.controllers.human_capital_data.list_human_capital_data_cli_controller import ListHumanCapitalDataCLIController

human_capital_data_tree = {
    'create': CreateHumanCapitalDataCLIController(),
    'read': ListHumanCapitalDataCLIController(),
}
