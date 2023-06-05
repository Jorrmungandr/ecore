from src.domain.controllers.cli_controller import CLIController

def filter_menu_tree_by_rbac(menu_tree, user_requester_role):
    # Filter the menu tree recursively so that the only leafs (controllers)
    # left are the ones that include `user_requester_role` in
    # the `CLIController.allowed_roles` property

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

            # If a menu node has no items it shouldn't show up
            if len(filtered_node.items()) == 0:
                return None

            return filtered_node

    return search_and_filter(menu_tree) or {}
