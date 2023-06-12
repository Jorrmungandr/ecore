from src.interface.cli.controllers.user.create_user_cli_controller import CreateUserCLIController
from src.interface.cli.controllers.user.update_user_cli_controller import UpdateUserCLIController
from src.interface.cli.controllers.user.detail_user_cli_controller import DetailUserCLIController

user_tree = {
    'create': CreateUserCLIController(),
    'update': UpdateUserCLIController(),
    'detail': DetailUserCLIController(),
}
