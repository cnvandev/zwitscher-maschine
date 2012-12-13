import sys
sys.path.append("../dynamo")
from dynamo import *
from common import extract_attributes, classed_div, classed_a, combine, href

# Convenience methods for generating miscellaneous Twitter Bootstrap elements.
# http://twitter.github.com/bootstrap/components.html#misc

WELL_CLASS = "well"
LARGE_WELL_CLASS = combine(WELL_CLASS, "large")
SMALL_WELL_CLASS = combine(WELL_CLASS, "small")

CONTAINER_CLASS = "container"

CLOSE_CLASS = "close"

def well(*content):
    ''' Returns the HTML code for a well. Like a grey-background blockquote. '''

    return classed_div(WELL_CLASS, *content)


def large_well(*content):
    ''' Returns the HTML code for a large well. Like a grey-background
    blockquote. '''

    return classed_div([WELL_CLASS, LARGE_WELL_CLASS], *content)


def small_well(*content):
    ''' Returns the HTML code for a small well. Like a grey-background
    blockquote. '''

    return classed_div([WELL_CLASS, SMALL_WELL_CLASS], *content)


def close():
    ''' Returns the HTML code for an X that indicates an element can be closed
    (like a window.) '''

    return classed_a(CLOSE_CLASS, href("#"), "&times;"))


def container(*content):
    ''' Returns the HTML code for a basic div container. '''

    return classed_div(CONTAINER_CLASS, *content)


def component_scripts(scripts):

    return *[script(src="../assets/js/bootstrap-" + component_script + ".js") for component_script in scripts]