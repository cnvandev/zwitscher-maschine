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
        a(text, href=url)
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