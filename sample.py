from zwitscher_maschine import *
sys.path.append("components")
from dropdowns import dropdown_menu, menu_item, divider, dropdown_submenu

print basic_template(
    dropdown_menu(
        menu_item("Thing 1", "#"),
        menu_item("Thing 2", "#"),
        menu_item("Thing 3", "#"),
        divider(),
        menu_item("Thing 4", "#"),
        dropdown_submenu("My Submenu", "#", 
            menu_item("Thing 5", "#"),
            menu_item("Thing 6", "#")
        )
    )
)