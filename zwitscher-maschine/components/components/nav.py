import sys
sys.path.append("../dynamo")
from dynamo import *
from common import extract_attributes, classed_ul, classed_div, classes, combine, active, disabled, ID

# Convenience methods for generating Twitter Bootstrap navigation elements
# HTML code - http://twitter.github.com/bootstrap/components.html#navs.

NAV_CLASS = "nav"
NAV_TABS_CLASS = combine(NAV_CLASS, "tabs")
NAV_PILLS_CLASS = combine(NAV_CLASS, "pills")
NAV_STACKED_CLASS = combine(NAV_CLASS, "stacked")

TABBABLE_CLASS = "tabbable"
TAB_CLASS = "tab"
TAB_LEFT_CLASS = combine(TAB_CLASS, "left")
TAB_RIGHT_CLASS = combine(TAB_CLASS, "right")
TAB_BELOW_CLASS = combine(TAB_CLASS, "below")
TAB_CONTENT_CLASS = combine(TAB_CLASS, "content")
TAB_PANE_CLASS = combine(TAB_CLASS, "pane")

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
    
    return classed_div(TAB_PANE_CLASS, ID(tab_id), *content))


def stacked():
    return classes(NAV_STACKED_CLASS)