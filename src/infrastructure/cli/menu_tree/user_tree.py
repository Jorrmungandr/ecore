from src.interface.cli.controllers.user.create_user_cli_controller import CreateUserCLIController
from src.interface.cli.controllers.user.update_user_cli_controller import UpdateUserCLIController

user_tree = {
    'create': CreateUserCLIController(),
    'update': UpdateUserCLIController(),
}
