import sys
sys.path.append("../dynamo")
from dynamo import *

# Convenience methods for generating Twitter Bootstrap button group HTML code.
# http://twitter.github.com/bootstrap/components.html#buttonGroup for examples.

BUTTON_CLASS = "btn"
BUTTON_GROUP_CLASS = BUTTON_CLASS + "-group"
BUTTON_TOOLBAR_CLASS = BUTTON_CLASS + "-toolbar"
BUTTON_GROUP_VERTICAL_CLASS = BUTTON_GROUP_CLASS + "-vertical"

# *sigh* button() is already taken by straight HTML buttons. Jerks.
def zm_button(text):
    ''' Returns the HTML code for a Twitter Bootstrap-ready button. '''

    return button(
        text,
        **{"class": BUTTON_CLASS}
    )

def button_group(*buttons):
    ''' Returns the HTML code for a button group that contains the given
    buttons. '''

    return div(
        *buttons,
        **{"class": BUTTON_GROUP_CLASS}
    )

def button_toolbar(*buttons):
    ''' Returns the HTML code for a toolbar that contains the given buttons. '''

    return div(
        *buttons,
        **{"class": BUTTON_TOOLBAR_CLASS}
    )

def button_group_vertical(*buttons):
    ''' Returns the HTML code for a vertical button group that contains the
    given buttons. '''

    return div(
        *buttons,
        **{"class": BUTTON_GROUP_CLASS + " " + BUTTON_GROUP_VERTICAL_CLASS}
    )