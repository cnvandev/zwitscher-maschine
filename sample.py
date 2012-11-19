from zwitscher_maschine import *
sys.path.append("components")
from dropdowns import dropdown_menu, menu_item, divider, dropdown_submenu
from button_groups import zm_button, button_group, button_toolbar, button_group_vertical
from button_dropdowns import button_dropdown, button_dropup, split_button_dropdown, split_button_dropup

print basic_template(
    button_toolbar(
        split_button_dropup("Drop Me!",
            menu_item("One!", "#"),
            menu_item("Two!", "#"),
            menu_item("Three!", "#")
        )
    )
)