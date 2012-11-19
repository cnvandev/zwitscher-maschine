from zwitscher_maschine import *
sys.path.append("components")
from dropdowns import dropdown_menu, menu_item, divider, dropdown_submenu
from button_groups import zm_button, button_group, button_toolbar, button_group_vertical
from button_dropdowns import button_dropdown, button_dropup, split_button_dropdown, split_button_dropup
from nav import tabs, active_tab, tab, disabled_tab, disabled_unclickable_tab, pills, stacked_tabs, stacked_pills

print basic_template(
    pills(
        active_tab("Home", "#"),
        tab("About", "#"),
        tab("Stuff", "#"),
        disabled_unclickable_tab("Dude")
    )
)