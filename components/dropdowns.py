import sys
sys.path.append("../dynamo")
from dynamo import *

# Convenience methods for generating Twitter Bootstrap dropdown menu HTML code.
# http://twitter.github.com/bootstrap/components.html#dropdowns for examples.

MENU_CLASS = "dropdown-menu"
SUBMENU_CLASS = "dropdown-submenu"

DIVIDER_CLASS = "divider"

def dropdown_menu(*items):
    ''' Returns the HTML code for a dropdown menu containing the given
    menu items. '''

    return ul(
        merge_attributes({
            "class": MENU_CLASS,
            "role": "menu",
            "aria-labelledBy": "dropdownMenu",
        }),
        *items
    )


def menu_item(text, url):
    ''' Returns the HTML code for a menu item in a dropdown menu. '''

    return li(a(text, href=url, tabindex="-1"))


def divider():
    ''' Returns the HTML code for divider in a dropdown menu. '''

    return li({"class": DIVIDER_CLASS}, "")

def submenu(text, url, *items):
    ''' Returns the HTML code for a submenu in a dropdown menu. The submenu
    can contain its own items just like a regular menu. '''

    return li(
        merge_attributes({"class": SUBMENU_CLASS}, *items),
        a(text, tabindex="-1", href=url),
        dropdown_menu(*items[1:])
    )