from src.infrastructure.cli.menu_tree.user_tree import user_tree
from src.infrastructure.cli.menu_tree.human_capital_data_tree import human_capital_data_tree
from src.infrastructure.cli.menu_tree.facilities_data_tree import facilities_data_tree
from src.infrastructure.cli.menu_tree.marketing_data_tree import marketing_data_tree

menu_tree = {
    'users': user_tree,
    'human_capital_data': human_capital_data_tree,
    'facilities_data': facilities_data_tree,
    'marketing_data': marketing_data_tree,
}
