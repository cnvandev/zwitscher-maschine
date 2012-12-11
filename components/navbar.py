import sys
sys.path.append("../dynamo")
from dynamo import *
from common import extract_attributes

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



def navbar(*content):
    ''' A navigation bar element that spans the available width. Use by filling
    with either a nav element (see nav.py) or (something else I forgot while
    writing this comment).

    '''

    # Gross little hack - we have to wrap the content (regardless of an
    # attributes hash) with a div(). We can do this because we know
    # extract_attributes() will return a hash first, since we're giving it one.
    merged_content = extract_attributes({"class": NAVBAR_CLASS}, *content)
    attributes = merged_content[0:1]
    merged_content = div({"class": NAVBAR_INNER_CLASS}, *merged_content[1:])
    return div(*merged_content)


def brand(*content):
    ''' A "brand" element in a navbar, essentially the title or logo. To make
    it a link, pass it a {"href": "http://my.link.here"} attribute dict.

    '''

    return a(
        *extract_attributes({"class": NAVBAR_CLASS}, *content)
    )


def nav_group(*content):
    ''' A group of navigation elements for use in a navbar. Children should be
    element()s (see nav.py's element() function.)

    '''

    return ul(
        *extract_attributes({"class": NAV_CLASS}, *content)
    )


def nav_divider():
    ''' A vertical divider for navigation bars. '''

    return li(
        *extract_attributes({"class": DIVIDER_CLASS}, *content)
    )


def form_left(*content):
    ''' A wrapper for form elements (like login, search, etc.) for use in
    navigation bars.

    '''

    return form(
        extract_attributes({"class": NAVBAR_FORM_CLASS}, *content)
    )


def search_input(*content):
    ''' A search input type for use in navigation bars. To give hint text,
    supply a {"placeholder": "Search..."} extra attributes dict as the first
    argument.

    '''

    return Input(
        extract_attributes(
            {"type": "text", "class": SEARCH_INPUT_CLASS},
            *content
        )
    )


def search_form(*content):
    ''' A wrapper around search input elements.

    '''

    return form(
        extract_attributes(
            {"class": NAVBAR_FORM_CLASS},
            *content
        )
    )


def navbar_text(*content):
    ''' A wrapper for text elements in navigation bars.

    '''

    return p(
        extract_attributes(
            {"class": NAVBAR_FORM_CLASS + "-text"},
            *content
        )
    )