from zwitscher_maschine import *
sys.path.append("components")
from dropdowns import dropdown_menu, menu_item, divider, dropdown_submenu
from button_groups import zm_button, button_group, button_toolbar, button_group_vertical
from button_dropdowns import button_dropdown, button_dropup, split_button_dropdown, split_button_dropup
from nav import tabs, active_element, element, disabled_element, disabled_unclickable_element, pills, stacked_tabs, stacked_pills, tab_navigation, tab_container, tab_pane, tab_navigation_left, tab_navigation_right, tab_navigation_below
from navbar import navbar, brand, nav_group, nav_divider, form_left, form_right, search_input, search_form_left, search_form_right, navbar_text

print basic_template(
    tab_navigation_below(
        tabs(
            active_element("Home", "#tab1"),
            element("About", "#tab2"),
            element("Stuff", "#tab3"),
        ),
        tab_container(
            tab_pane("#tab1", p("Home!")),
            tab_pane("#tab2", p("About!")),
            tab_pane("#tab3", p("Stuff!"))
        )
    )
)