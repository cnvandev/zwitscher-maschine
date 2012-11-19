import sys
sys.path.append("../dynamo")
from dynamo import *

# Convenience methods for generating Twitter Bootstrap navigation bars.
# http://twitter.github.com/bootstrap/components.html#navbar

NAVBAR_CLASS = "navbar"
NAVBAR_INNER_CLASS = NAVBAR_CLASS + "-inner"
BRAND_CLASS = "brand"

PULL_LEFT_CLASS = "pull-left"
PULL_RIGHT_CLASS = "pull-right"

NAVBAR_FORM_CLASS = NAVBAR_CLASS + "-form"
NAVBAR_SEARCH_CLASS = NAVBAR_CLASS + "-search"
SEARCH_INPUT_CLASS = "search-query"

NAV_CLASS = "nav"
DIVIDER_CLASS = "divider-vertical"



def navbar(*elements):
    ''' A navigation bar element that spans the available width. Use by filling
    with either a nav element (see nav.py ) '''

    return div(
        div(
            *elements,
            **{"class": NAVBAR_INNER_CLASS}
        ),
        **{"class": NAVBAR_CLASS}
    )


def brand(content, url):
    ''' A "brand" element in a navbar, essentially the title or logo. '''

    return a(
        content,
        **{
            "class": BRAND_CLASS,
            "href": url
        }
    )


def nav_group(*elements):
    ''' A group of navigation elements for use in a navbar. Children should be
    element()s (see nav.py's element() function.) '''

    return ul(
        **{"class": NAV_CLASS}
    )


def nav_divider():
    ''' A vertical divider for navigation bars. '''

    return li(
        **{"class": DIVIDER_CLASS}
    )


def form_left(*elements):
    ''' A wrapper for form elements (like login, search, etc.) for use in
    navigation bars, aligned to the left side of the bar. '''

    return form(
        *elements,
        **{"class": " ".join([NAVBAR_FORM_CLASS, PULL_LEFT_CLASS])}
    )


def form_right(*elements):
    ''' A wrapper for form elements (like login, search, etc.) for use in
    navigation bars, aligned to the right side of the bar. '''

    return form(
        *elements,
        **{"class": " ".join([NAVBAR_FORM_CLASS, PULL_RIGHT_CLASS])}
    )


def search_input(hint_text):
    ''' A search input type for use in navigation bars. '''

    return Input(**{
        "type": "text",
        "class": SEARCH_INPUT_CLASS,
        "placeholder": hint_text
    })


def search_form_left(*elements):
    ''' A left-aligned wrapper around search input elements. '''

    return form(
        *elements,
        **{"class": " ".join([NAVBAR_FORM_CLASS, PULL_LEFT_CLASS])}
    )


def search_form_right(*elements):
    ''' A right-aligned wrapper around search input elements. '''

    return form(
        *elements,
        **{"class": " ".join([NAVBAR_FORM_CLASS, PULL_RIGHT_CLASS])}
    )


def navbar_text(text):
    ''' A wrapper for text elements in navigation bars. '''

    return p(
        text,
        **{"class": NAVBAR_FORM_CLASS + "-text"}
    )