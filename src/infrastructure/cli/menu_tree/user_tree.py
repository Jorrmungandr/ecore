from src.interface.cli.controllers.user.create_user_cli_controller import CreateUserCLIController
from src.interface.cli.controllers.user.update_user_cli_controller import UpdateUserCLIController
from src.interface.cli.controllers.user.detail_user_cli_controller import DetailUserCLIController
from src.interface.cli.controllers.user.list_users_cli_controller import ListUsersCLIController

user_tree = {
    'create': CreateUserCLIController(),
    'read': ListUsersCLIController(),
    'detail': DetailUserCLIController(),
    'update': UpdateUserCLIController(),
}
