import sys
sys.path.append("../dynamo")
from dynamo import *

MENU_CLASS = "dropdown-menu"
SUBMENU_CLASS = "dropdown-submenu"

def dropdown_menu(*items):
    return ul(
        *items,
        **{
            "class": MENU_CLASS,
            "role": "menu",
            "aria-labelledBy": "dropdownMenu",
        }
    )


def menu_item(text, url):
    return li(a(text, href=url, tabindex="-1"))


def divider():
    return li("", Class="divider")

def dropdown_submenu(text, url, *items):
    return li(
        a(text, tabindex="-1", href=url),
        dropdown_menu(*items),
        **{
            "class": SUBMENU_CLASS,
        })