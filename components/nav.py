import sys
sys.path.append("../dynamo")
from dynamo import *
from common import extract_attributes

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

def generic_nav(*content):
    ''' Returns the HTML code for a set of tab navigaiton elements using the set
    of given tabs. '''

    return classed_ul([NAV_CLASS, NAV_TABS_CLASS], *content)


def pills(*content):
    ''' Returns the HTML code for a set of "pill" navigaiton elements using the
    set of given tabs. '''

    return generic_nav(classes(NAV_PILLS_CLASS), *content)


def element(*content):
    ''' A single navigational element for a tab, pill, or navbar navigation
    system. Pass it a link to make this work properly.

    '''

    return li(*extract_attributes(*content))


def tab_navigation(*content):
    ''' Returns the HTML code for a tab navigation container using the supplied
    tabs and container (see tabs() and tab_container()). '''
    
    return classed_div(TABBABLE_CLASS, *content)


def tab_container(*content):
    ''' Returns a container for tab-pane elements. '''

    return classed_div(TAB_CONTENT_CLASS, *content)


def tab_pane(tab_id, *content):
    ''' Returns a single content pane for tab navigation. '''
    
    return div(
        *extract_attributes(
            {"class": TAB_PANE_CLASS, "id": tab_id},
            *content
        )
    )


def stacked():
    return classes(NAV_STACKED_CLASS)


def active():
    return classes(ACTIVE_CLASS)


def disabled():
    return classes(DISABLED_CLASS)