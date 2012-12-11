import sys
sys.path.append("../dynamo")
from dynamo import *
from common import extract_attributes

# Convenience methods for generating Twitter Bootstrap dropdown menu HTML code.
# http://twitter.github.com/bootstrap/components.html#dropdowns for examples.

MENU_CLASS = "dropdown-menu"
SUBMENU_CLASS = "dropdown-submenu"

DIVIDER_CLASS = "divider"

def dropdown_menu(*items):
    ''' Returns the HTML code for a dropdown menu containing the given
    menu items. '''

    return ul(
        *extract_attributes({
                "class": MENU_CLASS,
                "role": "menu",
                "aria-labelledBy": "dropdownMenu",
            },
            *items
        )
    )


def menu_item(*content):
    ''' Returns the HTML code for a menu item in a dropdown menu. '''

    return li(
        *extract_attributes(
            {"tabindex": "-1"},
            *content
        )
    )


def divider(*content):
    ''' Returns the HTML code for divider in a dropdown menu. '''

    return li(
        *extract_attributes({"class": DIVIDER_CLASS}, *content)
    )

def submenu(text, url, *items):
    ''' Returns the HTML code for a submenu in a dropdown menu. The submenu
    can contain its own items just like a regular menu. '''

    merged_content = list(extract_attributes({"class": SUBMENU_CLASS}, *items))
    merged_content.insert(1, a(text, tabindex="-1", href=url))
    merged_content.insert(2, dropdown_menu(*items))

    return li(*merged_content)