import sys
sys.path.append("../dynamo")
from dynamo import *
from button_groups import zm_button, button_group
from dropdowns import dropdown_menu, DROPDOWN_CLASS, 
from common import extract_attributes, classed_span, classed_button, combine

# Convenience methods for generating Twitter Bootstrap button dropdown HTML
# code. See http://twitter.github.com/bootstrap/components.html#buttonDropdowns
# for examples.

BUTTON_CLASS = "btn"
BUTTON_GROUP_CLASS = combine(BUTTON_CLASS, "group")

DROPDOWN_TOGGLE_CLASS = combine(DROPDOWN_CLASS,"toggle")

def button_dropdown(text, *menu_items):
    ''' Returns the HTML code for a button with a caret and a dropdown menu
    containing the given menu items. '''

    return button_group(
        zm_button(text),
        caret_button(),
        dropdown_menu(*menu_items),
    )


def button_dropup(text, *menu_items):
    ''' Returns the HTML code for a button with a caret and a drop-up menu
    containing the given menu items. '''

    return button_dropup_group(
        zm_button(text),
        caret_button(),
        dropdown_menu(*menu_items),
    )


def split_button_dropdown(text, *menu_items):
    ''' Returns the HTML code for a two-button group, one with a caret and a
    dropdown menu containing the given menu items. '''

    return button_group(
        zm_button(text),
        caret_button(),
        dropdown_menu(*menu_items)
    )


def split_button_dropup(text, *menu_items):
    ''' Returns the HTML code for a two-button group, one with a caret and a
    drop-up menu containing the given menu items. '''

    return button_dropup_group(
        zm_button(text),
        caret_button(),
        dropdown_menu(*menu_items)
    )


def caret_button():
    ''' Returns the HTML code for a caret indicating a dropdown/dropup menu. '''

    return classed_button([BUTTON_CLASS, DROPDOWN_TOGGLE_CLASS],
        toggle(DROPDOWN_CLASS),
        classed_span("caret")
    )
