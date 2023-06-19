from src.domain.controllers.cli_controller import CLIController

def filter_menu_tree_by_rbac(menu_tree, user_requester_role):
    # Aqui eu filtro a árvore até que as únicas folhas (controllers)
    # restantes sejam as que incluem a variável `user_requester_role`
    # na property `CLIController.allowed_roles`

    def search_and_filter(node):
        if isinstance(node, CLIController):
            if user_requester_role in node.allowed_roles:
                return node

            return None
        else:
            filtered_node = {}

            for key, value in node.items():
                filtered_value = search_and_filter(value)

                if filtered_value is not None:
                    filtered_node[key] = filtered_value

            # Se um submenu não tem itens ele não deve aparecer
            if len(filtered_node.items()) == 0:
                return None

            return filtered_node

    return search_and_filter(menu_tree) or {}
