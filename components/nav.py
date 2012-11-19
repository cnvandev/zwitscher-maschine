import sys
sys.path.append("../dynamo")
from dynamo import *

# Convenience methods for generating Twitter Bootstrap navigation elements
# HTML code - http://twitter.github.com/bootstrap/components.html#navs.

NAV_CLASS = "nav"
NAV_TABS_CLASS = NAV_CLASS + "-tabs"
NAV_PILLS_CLASS = NAV_CLASS + "-pills"
NAV_STACKED_CLASS = NAV_CLASS + "-stacked"

ACTIVE_CLASS = "active"
DISABLED_CLASS = "disabled"

TABBABLE_CLASS = "tabbable"
TAB_CLASS = "tab"
TAB_LEFT_CLASS = TAB_CLASS + "-left"
TAB_RIGHT_CLASS = TAB_CLASS + "-right"
TAB_BELOW_CLASS = TAB_CLASS + "-below"
TAB_CONTENT_CLASS = TAB_CLASS + "-content"
TAB_PANE_CLASS = TAB_CLASS + "-pane"

def tabs(*tabs):
    ''' Returns the HTML code for a set of tab navigaiton elements using the set
    of given tabs. '''

    return ul(
        *tabs,
        **{"class": " ".join([NAV_CLASS, NAV_TABS_CLASS])}
    )


def pills(*tabs):
    ''' Returns the HTML code for a set of "pill" navigaiton elements using the
    set of given tabs. '''

    return ul(
        *tabs,
        **{"class": " ".join([NAV_CLASS, NAV_PILLS_CLASS])}
    )


def stacked_tabs(*tabs):
    ''' Returns the HTML code for a set of tab navigaiton elements using the set
    of given tabs. '''

    return ul(
        *tabs,
        **{"class": " ".join([NAV_CLASS, NAV_TABS_CLASS, NAV_STACKED_CLASS])}
    )


def stacked_pills(*tabs):
    ''' Returns the HTML code for a set of "pill" navigaiton elements using the
    set of given tabs. '''

    return ul(
        *tabs,
        **{"class": " ".join([NAV_CLASS, NAV_PILLS_CLASS, NAV_STACKED_CLASS])}
    )


def element(text, url):
    ''' A single navigational element for a tab, pill, or navbar navigation
    system. '''

    return li(
        a(
            text,
            **{"href": url}
        )
    )


def active_element(text, url):
    ''' An "active" single tab item for a tab or pill navigation system. '''

    return li(
        a(text, href=url),
        **{"class": ACTIVE_CLASS}
    )

def disabled_element(text, url):
    ''' A disabled (yet still clickable) tab item for a tab or pill navigation
    system. '''

    return li(
        a(text, href=url),
        **{"class": DISABLED_CLASS}
    )

def disabled_unclickable_element(text):
    ''' A disabled and unclickable tab item for a tab or pill nagivation
    system. '''

    return li(
        a(text),
        **{"class": DISABLED_CLASS}
    )


def tab_navigation(tab_nav, tab_container):
    ''' Returns the HTML code for a tab navigation container using the supplied
    tabs and container (see tabs() and tab_container()). '''
    
    return div(
        tab_nav,
        tab_container,
        **{"class": TABBABLE_CLASS}
    )


def tab_navigation_left(tab_nav, tab_container):
    ''' Returns the HTML code for a tab navigation container with the tabs on
    the left, using the supplied tabs and container. '''
    
    return div(
        tab_nav,
        tab_container,
        **{"class": " ".join([TABBABLE_CLASS, TAB_LEFT_CLASS])}
    )


def tab_navigation_right(tab_nav, tab_container):
    ''' Returns the HTML code for a tab navigation container with the tabs on
    the right, using the supplied tabs and container. '''
    
    return div(
        tab_nav,
        tab_container,
        **{"class": " ".join([TABBABLE_CLASS, TAB_RIGHT_CLASS])}
    )


def tab_navigation_below(tab_nav, tab_container):
    ''' Returns the HTML code for a tab navigation container with the tabs below
    the content, using the supplied tabs and container. '''
    
    return div(
        tab_nav,
        tab_container,
        **{"class": " ".join([TABBABLE_CLASS, TAB_BELOW_CLASS])}
    )


def tab_container(*panes):
    ''' Returns a container for tab-pane elements. '''

    return div(
        *panes,
        **{"class": TAB_CONTENT_CLASS}
    )


def tab_pane(tab_id, *content):
    ''' Returns a single content pane for tab navigation. '''
    
    return div(
        *content,
        **{"class": TAB_PANE_CLASS, "id": tab_id}
    )


def active_tab_pane(tab_id, *content):
    ''' Returns an active tab content pane for tab navigation. '''

    return div(
        *content,
        **{"class": " ".join([TAB_PANE_CLASS, ACTIVE_CLASS]), "id": tab_id}
    )
