import sys
sys.path.append("../dynamo")
from dynamo import *
from common import extract_attributes, classed_div, classed_button, classes, combine

# Convenience methods for generating Twitter Bootstrap button group HTML code.
# http://twitter.github.com/bootstrap/components.html#buttonGroup for examples.

BUTTON_CLASS = "btn"
BUTTON_GROUP_CLASS = combine(BUTTON_CLASS, "group")
BUTTON_TOOLBAR_CLASS = combine(BUTTON_CLASS, "toolbar")
BUTTON_GROUP_VERTICAL_CLASS = combine(BUTTON_GROUP_CLASS, "vertical")

# *sigh* button() is already taken by straight HTML buttons. Jerks.
def zm_button(text):
    ''' Returns the HTML code for a Twitter Bootstrap-ready button. '''

    return classed_button(BUTTON_CLASS, *content)

def button_group(*content):
    ''' Returns the HTML code for a button group that contains the given
    buttons. '''

    return classed_div(BUTTON_GROUP_CLASS, *content)

def button_toolbar(*content):
    ''' Returns the HTML code for a toolbar that contains the given buttons. '''

    return classed_div(BUTTON_TOOLBAR_CLASS, *content)

def vertical_button_group(*content):
    ''' Returns the HTML code for a vertical button group that contains the
    given buttons. '''

    return button_group(classes(BUTTON_GROUP_CLASS), *content)