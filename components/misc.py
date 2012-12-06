import sys
sys.path.append("../dynamo")
from dynamo import *

# Convenience methods for generating miscellaneous Twitter Bootstrap elements.
# http://twitter.github.com/bootstrap/components.html#misc

WELL_CLASS = "well"
LARGE_WELL_CLASS = WELL_CLASS + "-large"
SMALL_WELL_CLASS = WELL_CLASS + "-small"

CONTAINER_CLASS = "container"

CLOSE_CLASS = "close"

def well(*content):
    ''' Returns the HTML code for a well. Like a grey-background blockquote. '''

    return div(
        *content,
        **{"class": WELL_CLASS}
    )


def large_well(*content):
    ''' Returns the HTML code for a large well. Like a grey-background
    blockquote. '''

    return div(
        *content,
        **{"class": " ".join([WELL_CLASS, LARGE_WELL_CLASS])}
    )


def small_well(*content):
    ''' Returns the HTML code for a small well. Like a grey-background
    blockquote. '''

    return div(
        *content,
        **{"class": " ".join([WELL_CLASS, SMALL_WELL_CLASS])}
    )


def close():
    ''' Returns the HTML code for an X that indicates an element can be closed
    (like a window.) '''

    return a(
        "&times;",
        **{"class": CLOSE_CLASS, "href": "#"}
    )


def container(*content):
    ''' Returns the HTML code for a basic div container. '''

    return div(
        *content,
        **{"class": CONTAINER_CLASS}
    )


def component_scripts(scripts):

    return *[script(src="../assets/js/bootstrap-" + component_script + ".js") for component_script in scripts]