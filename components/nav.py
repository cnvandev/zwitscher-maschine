import sys
sys.path.append("../dynamo")
from dynamo import *

# Convenience methods for generating Twitter Bootstrap navigation elements
# HTML code - http://twitter.github.com/bootstrap/components.html#navs.

NAV_CLASS = "nav"
NAV_TABS_CLASS = NAV_CLASS + "-tabs"
NAV_PILLS_CLASS = NAV_CLASS + "-pills"
NAV_STACKED_CLASS = NAV_CLASS + "-stacked"

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


def tab(text, url):
    ''' A single tab item for a tab or pill navigation system. '''

    return li(
        a(
            text,
            **{"href": url, "data-toggle": "tab"}
        )
    )


def active_tab(text, url):
    ''' An "active" single tab item for a tab or pill navigation system. '''

    return li(
        a(text, href=url),
        **{"class": "active"}
    )

def disabled_tab(text, url):
    ''' A disabled (yet still clickable) tab item for a tab or pill navigation
    system. '''

    return li(
        a(text, href=url),
        **{"class": "disabled"}
    )

def disabled_unclickable_tab(text):
    ''' A disabled and unclickable tab item for a tab or pill nagivation
    system. '''

    return li(
        a(text),
        **{"class": "disabled"}
    )


def tab_navigation(tab_nav, tab_container):
    ''' Returns the HTML code for a tab navigation container using the supplied
    tabs and container (see tabs() and tab_container()). '''
    
    return div(
        tab_nav,
        tab_container,
        **{"class": "tabbable"}
    )


def tab_navigation_left(tab_nav, tab_container):
    ''' Returns the HTML code for a tab navigation container with the tabs on
    the left, using the supplied tabs and container. '''
    
    return div(
        tab_nav,
        tab_container,
        **{"class": "tabbable tabs-left"}
    )


def tab_navigation_right(tab_nav, tab_container):
    ''' Returns the HTML code for a tab navigation container with the tabs on
    the right, using the supplied tabs and container. '''
    
    return div(
        tab_nav,
        tab_container,
        **{"class": "tabbable tabs-right"}
    )


def tab_navigation_below(tab_nav, tab_container):
    ''' Returns the HTML code for a tab navigation container with the tabs below
    the content, using the supplied tabs and container. '''
    
    return div(
        tab_nav,
        tab_container,
        **{"class": "tabbable tabs-below"}
    )


def tab_container(*panes):
    ''' Returns a container for tab-pane elements. '''

    return div(
        *panes,
        **{"class": "tab-content"}
    )


def tab_pane(tab_id, *content):
    ''' Returns a single content pane for tab navigation. '''
    
    return div(
        *content,
        **{"class": "tab-pane", "id": tab_id}
    )


def active_tab_pane(id, *content):
    ''' Returns an active tab content pane for tab navigation. '''

    return div(
        *content,
        **{"class": "tab-pane active", "id": tab_id}
    )
