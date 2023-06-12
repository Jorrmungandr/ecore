from src.interface.cli.controllers.marketing_data.create_marketing_data_cli_controller import CreateMarketingDataCLIController
from src.interface.cli.controllers.marketing_data.list_marketing_data_cli_controller import ListMarketingDataCLIController

marketing_data_tree = {
    'create': CreateMarketingDataCLIController(),
    'read': ListMarketingDataCLIController(),
}
