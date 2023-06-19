import sys

from src.interface.cli.controllers.auth.login_cli_controller import LoginCLIController

from src.infrastructure.cli.menu_tree import menu_tree
from src.infrastructure.cli.helpers.translate_paths import path_translation
from src.infrastructure.cli.helpers.clear_console import clear_console
from src.infrastructure.cli.helpers.authorized_menu_paths import filter_menu_tree_by_rbac

from src.domain.controllers.cli_controller import CLIController

try:
    # Ciclo de Login
    login_controller = LoginCLIController()

    clear_console()
    print('Login\n')
    auth_user = login_controller.execute()

    while not auth_user:
        clear_console()
        print('Login\n')
        print('Credenciais inválidas, tente novamente\n')

        auth_user = login_controller.execute()

    authorized_menu_tree = filter_menu_tree_by_rbac(menu_tree, auth_user.role)

    # Ciclo de menu (recursão)
    def render_menu(node_path):
        clear_console()

        is_main_menu = len(node_path) == 0

        if is_main_menu:
            print('Menu principal\n')
        else:
            print(f'Menu {path_translation[".".join(node_path)]}\n')

        current_menu = authorized_menu_tree

        for key in node_path:
            current_menu = current_menu[key]

        current_keys = list(current_menu.keys())

        for index, key in enumerate(current_keys):
            print(f'{index + 1} - {path_translation[".".join([*node_path, key])]}')

        if is_main_menu:
            print('0 - Sair\n')
        else:
            print('0 - Voltar\n')

        # Ciclo de selecionar opções
        while True:
            selected_option = input('Opção selecionada: ')

            if not selected_option.isnumeric():
                print('Opção inválida')
                continue

            selected_index = int(selected_option)

            if selected_index < 0 or selected_index > len(current_keys):
                print('Opção inválida')
                continue

            if selected_index == 0:
                if is_main_menu:
                    sys.exit(0)
                else:
                    render_menu(node_path[:-1])

            selected_key = current_keys[selected_index - 1]

            selection = current_menu[current_keys[selected_index - 1]]

            if isinstance(selection, CLIController):
                clear_console()
                print(f'{path_translation[".".join([*node_path, key])]}\n')

                selection.user_requester = auth_user
                selection.execute()

                input('\nPressione qualquer tecla para retornar para o menu principal')

                render_menu([])
            else:
                render_menu([*node_path, selected_key])

    render_menu([])
except KeyboardInterrupt:
    print('\n\nPrograma interrompido pelo usuário')
    sys.exit(0)
