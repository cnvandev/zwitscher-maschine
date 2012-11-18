from zwitscher_maschine import *
sys.path.append("components")
from dropdowns import dropdown_menu, menu_item, divider, dropdown_submenu
from button_groups import zm_button, button_group, button_toolbar, button_group_vertical

print basic_template(
    button_toolbar(
        button_group_vertical(
            zm_button("Left"),
            zm_button("Center"),
            zm_button("Right")
        )
    )
)