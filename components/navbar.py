import sys
sys.path.append("../dynamo")
from dynamo import *
from common import merge_attributes

# Convenience methods for generating Twitter Bootstrap navigation bars.
# http://twitter.github.com/bootstrap/components.html#navbar

NAVBAR_CLASS = "navbar"
NAVBAR_INNER_CLASS = NAVBAR_CLASS + "-inner"
NAVBAR_INVERSE_CLASS = NAVBAR_CLASS + "-inverse"
BRAND_CLASS = "brand"

PULL_LEFT_CLASS = "pull-left"
PULL_RIGHT_CLASS = "pull-right"

NAVBAR_FORM_CLASS = NAVBAR_CLASS + "-form"
NAVBAR_SEARCH_CLASS = NAVBAR_CLASS + "-search"
SEARCH_INPUT_CLASS = "search-query"

NAV_CLASS = "nav"
DIVIDER_CLASS = "divider-vertical"



def navbar(*children):
    ''' A navigation bar element that spans the available width. Use by filling
    with either a nav element (see nav.py) or (something else I forgot while
    writing this comment).

    '''

    return div(
        merge_attributes({"class": NAVBAR_CLASS}, *children),
        div(
            {"class": NAVBAR_INNER_CLASS},
            *children[1:]
        )
    )


def brand(*children):
    ''' A "brand" element in a navbar, essentially the title or logo. To make
    it a link, pass it a {"href": "http://my.link.here"} attribute dict.

    '''

    return a(
        merge_attributes({"class": NAVBAR_CLASS}, *children),
        *children[1:]
    )


def nav_group(*children):
    ''' A group of navigation elements for use in a navbar. Children should be
    element()s (see nav.py's element() function.)

    '''

    return ul(
        merge_attributes({"class": NAV_CLASS}, *children),
        *children[1:]
    )


def nav_divider():
    ''' A vertical divider for navigation bars.

    '''

    return li(
        merge_attributes({"class": DIVIDER_CLASS}, *children),
        *children[1:]
    )


def form_left(*children):
    ''' A wrapper for form elements (like login, search, etc.) for use in
    navigation bars, aligned to the left side of the bar.

    '''

    return form(
        merge_attributes(
            {"class": [NAVBAR_FORM_CLASS, PULL_LEFT_CLASS]},
            *children[1:]
        ),
        *children[2:]
    )


def form_right(*elements):
    ''' A wrapper for form elements (like login, search, etc.) for use in
    navigation bars, aligned to the right side of the bar.

    '''

    return form(
        merge_attributes(
            {"class": [NAVBAR_FORM_CLASS, PULL_RIGHT_CLASS]},
            *children[1:]
        ),
        *children[2:]
    )


def search_input(*children):
    ''' A search input type for use in navigation bars. To give hint text,
    supply a {"placeholder": "Search..."} extra attributes dict as the first
    argument.

    '''

    return Input(
        merge_attributes(
            {"type": "text", "class": SEARCH_INPUT_CLASS},
            *children[1:]
        ),
        *children[2:]
    )


def search_form_left(*children):
    ''' A left-aligned wrapper around search input elements.

    '''

    return form(
        merge_attributes(
            {"class": [NAVBAR_FORM_CLASS, PULL_LEFT_CLASS]},
            *children[1:]
        ),
        *children[2:]
    )


def search_form_right(*children):
    ''' A right-aligned wrapper around search input elements.

    '''

    return form(
        merge_attributes(
            {"class": [NAVBAR_FORM_CLASS, PULL_RIGHT_CLASS]},
            *children[1:]
        ),
        *children[2:]
    )


def navbar_text(*children):
    ''' A wrapper for text elements in navigation bars.

    '''

    return p(
        merge_attributes(
            {"class": NAVBAR_FORM_CLASS + "-text"},
            *children[1:]
        ),
        *children[2:]
    )