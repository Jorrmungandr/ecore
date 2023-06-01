import os
import sys

from src.interface.cli.controllers.auth.login_cli_controller import LoginCLIController

from src.infrastructure.cli.menu_paths import menu_paths
from src.infrastructure.cli.helpers.translate_paths import path_translation
from src.infrastructure.cli.helpers.clear_console import clear_console

try:
    # Login Cycle
    login_controller = LoginCLIController()

    auth_user = None

    while not auth_user:
        auth_user = login_controller.execute()

    def render_menu(render_path):
        clear_console()

        is_main_menu = len(render_path) == 0

        if is_main_menu:
            print('Menu principal\n')
        else:
            print(f'Menu {path_translation[".".join(render_path)]}\n')

        current_menu = menu_paths

        for key in render_path:
            current_menu = current_menu[key]

        current_keys = list(current_menu.keys())

        for index, key in enumerate(current_keys):
            print(f'{index + 1} - {path_translation[".".join([*render_path, key])]}\n')

        if is_main_menu:
            print('0 - Sair\n')
        else:
            print('0 - Voltar\n')

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
                    render_menu(render_path[:-1])

            selected_key = current_keys[selected_index - 1]

            selection = current_menu[current_keys[selected_index - 1]]

            if isinstance(selection, dict):
                render_menu([*render_path, selected_key])
            else:
                os.system('cls||clear')
                print(f'{path_translation[".".join([*render_path, key])]}\n')

                selection.execute()

                input('\nPressione Enter para voltar para o menu principal')

                render_menu([])

    render_menu([])
except KeyboardInterrupt:
    print('\n\nPrograma interrompido pelo usuário')
    sys.exit(0)
