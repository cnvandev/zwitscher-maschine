import sys
sys.path.append("../dynamo")
from dynamo import *
from common import extract_attributes, classed_a, classed_ul, classed_li, classed_input, classed_form, classed_p, combine, classed_span
from buttons import BUTTON_CLASS
from dropdowns import DROPDOWN_CLASS

# Convenience methods for generating Twitter Bootstrap navigation bars.
# http://twitter.github.com/bootstrap/components.html#navbar

NAVBAR_CLASS = "navbar"
NAVBAR_INNER_CLASS = combine(NAVBAR_CLASS, "inner")
NAVBAR_INVERSE_CLASS = combine(NAVBAR_CLASS, "inverse")
NAVBAR_FIXED_TOP_CLASS = combine(NAVBAR_CLASS, "fixed", "top")
NAVBAR_BUTTON_CLASS = combine(BUTTON_CLASS, NAVBAR_CLASS)

BRAND_CLASS = "brand"

PULL_LEFT_CLASS = combine("pull", "left")
PULL_RIGHT_CLASS = combine("pull", "right")

NAVBAR_FORM_CLASS = combine(NAVBAR_CLASS, "form")
NAVBAR_SEARCH_CLASS = combine(NAVBAR_CLASS, "search")
NAVBAR_TEXT_CLASS = combine(NAVBAR_FORM_CLASS, "text")
SEARCH_INPUT_CLASS = combine("search", "query")

NAV_CLASS = "nav"
NAV_HEADER_CLASS = combine(NAV_CLASS, "header")

DIVIDER_CLASS = combine("divider", "vertical")

ICON_BAR_CLASS = combine("icon", "bar")

COLLAPSE = "collapse"
COLLAPSING_NAV_CLASS = combine(NAV_CLASS, COLLAPSE)


def navbar(*content):
    ''' A navigation bar element that spans the available width. Use by filling
    with either a nav element (see nav.py) or (something else I forgot while
    writing this comment).

    '''

    # Gross little hack - we have to wrap the content (regardless of an
    # attributes hash) with a div(). We can do this because we know
    # extract_attributes() will return a hash first, since we're giving it one.
    merged_content = extract_attributes(classes(NAVBAR_CLASS), *content)
    attributes = merged_content[0:1]
    merged_content = classed_div(NAVBAR_INNER_CLASS, *merged_content[1:])
    return div(*merged_content)


def brand(*content):
    ''' A "brand" element in a navbar, essentially the title or logo. To make
    it a link, pass it a {"href": "http://my.link.here"} attribute dict.

    '''

    return classed_a(NAVBAR_CLASS, *content)


def nav_group(*content):
    ''' A group of navigation elements for use in a navbar. Children should be
    element()s (see nav.py's element() function.)

    '''

    return classed_ul(NAV_CLASS, *content)


def nav_divider():
    ''' A vertical divider for navigation bars. '''

    return classed_li(DIVIDER_CLASS, *content)


def nav_form(*content):
    ''' A wrapper for form elements (like login, search, etc.) for use in
    navigation bars.

    '''

    return classed_form(NAVBAR_FORM_CLASS, *content)


def nav_dropdown(title, *content):
    ''' A button to open a dropdown menu in a navbar. Give it a menu in the
    content for it to actually work.
    WARNING: Unlike other functions, this one can't take extra classes right
    now :(

    '''

    return classed_li(DROPDOWN_CLASS,
        classed_a(
            combine(DROPDOWN_CLASS, "toggle"),
            toggle(DROPDOWN_CLASS),
            title,
            classed_b("caret"),
            *content
        )
    )


def search_input(*content):
    ''' A search input type for use in navigation bars. To give hint text,
    supply a {"placeholder": "Search..."} extra attributes dict as the first
    argument.

    '''

    return classed_input(SEARCH_INPUT_CLASS, Type("text"), *content)


def search_form(*content):
    ''' A wrapper around search input elements. '''

    return classed_form(NAVBAR_SEARCH_CLASS, *content)


def navbar_text(*content):
    ''' A wrapper for text elements in navigation bars. '''

    return classed_p(NAVBAR_TEXT_CLASS, *content)


def navbar_button(*content):
    ''' A button for use in the navigation bar. '''

    return classed_a([BUTTON_CLASS, NAVBAR_BUTTON_CLASS], *content)


def icon_bar():
    ''' A visual "bar" in CSS. '''

    return classed_span(ICON_BAR_CLASS)


def collapsed_nav_button():
    ''' A button that looks nice and touchable that appears when the navigation
    bar is collapsed. '''

    return navbar_button(icon_bar(), icon_bar(), icon_bar())


def collapsing_nav(*content):
    ''' A section in the navigation bar that will collapse if room is no longer
    available. '''

    return classed_div([COLLAPSING_NAV_CLASS, COLLAPSE], *content)


def responsive_nav(dem_classes, dat_brand, *content):
    ''' A shortcut for a semi-standard form of "responsive" navigation. The
    brand element will always stay visible, the rest of the content will
    collapse under a touchable button if the screen size is too small. '''

    return navbar(classes(dem_classes),
            container(
                collapsed_nav_button(),
                dat_brand,
                collapsing_nav(
                    nav_group(
                        *content
                    )
                ) + comment("/.nav-collapse")
            )
        )
