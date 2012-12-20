import sys
sys.path.append("../dynamo")
from dynamo import *
from common import extract_attributes, classed_li, classed_ul, untabbable, classes, combine, untabbable

# Convenience methods for generating Twitter Bootstrap dropdown menu HTML code.
# http://twitter.github.com/bootstrap/components.html#dropdowns for examples.

DROPDOWN_CLASS = "dropdown"
DROPUP_CLASS = "dropup"

MENU_CLASS = combine(DROPDOWN_CLASS, "menu")
SUBMENU_CLASS = combine(DROPDOWN_CLASS, "submenu")

DIVIDER_CLASS = "divider"

def dropdown_menu(*items):
    ''' Returns the HTML code for a dropdown menu containing the given
    menu items. '''

    return classed_ul(MENU_CLASS,
        {
            "role": "menu",
            "aria-labelledBy": "dropdownMenu",
        },
        *items
    )


def menu_item(*content):
    ''' Returns the HTML code for a menu item in a dropdown menu. '''

    return classed_li(*content)


def divider(*content):
    ''' Returns the HTML code for divider in a dropdown menu. '''

    return classed_li(DIVIDER_CLASS, *content)


def nav_header(*content):
    ''' A header in a navigation list. '''

    return classed_li(NAV_HEADER_CLASS, *content)


def submenu(text, url, *items):
    ''' Returns the HTML code for a submenu in a dropdown menu. The submenu
    can contain its own items just like a regular menu. '''

    return classed_li(
        SUBMENU_CLASS, items,
        prepend=[a(untabbable(), text, href=url), dropdown_menu(*items)]
    )