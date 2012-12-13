import sys
sys.path.append("../dynamo")
from dynamo import *
from common import extract_attributes, classed_div, classed_button, classes, combine, SUCCESS, INFO, ERROR

# Convenience methods for generating Twitter Bootstrap alert elements.
# http://twitter.github.com/bootstrap/components.html#alerts

ALERT_CLASS = "alert"
ALERT_BLOCK_CLASS = ALERT_CLASS + "-block"
CLOSE_CLASS = "close"
BUTTON_CLASS = "button"

ALERT_ERROR_CLASS = combine(ALERT_CLASS, ERROR)
ALERT_SUCCESS_CLASS = combine(ALERT_CLASS, SUCCESS)
ALERT_INFO_CLASS = combine(ALERT_CLASS, INFO)

def alert(title, *content):
    ''' Returns the HTML code for a small, yellow alert message. '''

    return alert_factory(False, title, *content)


def long_alert(title, *content):
    ''' Returns the HTML code for a long, yellow alert message. '''

    return alert_factory(True, title, *content)


def alert_factory(is_long, title, *content):
    ''' Returns the HTML code for a generic alert message. Really only to be
    used internally, use alert() or long_alert()

    '''

    return classed_div(ALERT_CLASS, *content,
        prepend=[classed_button(CLOSE_CLASS,
            {
                "type": BUTTON_CLASS,
                "data-dismiss": ALERT_CLASS
            },
            "x"
        ),
        strong(title) if is_long else h4(title)],
        append=strong("fuck you")
    )


def success_alert(title, *content):
    ''' Returns the HTML code for a small, green success message. '''

    return alert(
        title,
        *extract_attributes(classes(ALERT_SUCCESS_CLASS), *content)
    )


def long_success_alert(title, *content):
    ''' Returns the HTML code for a long, green success message. '''

    return long_alert(
        title,
        *extract_attributes(classes(ALERT_SUCCESS_CLASS), *content)
    )


def error_alert(title, *content):
    ''' Returns the HTML code for a small, red error message. '''

    return alert(
        title,
        *extract_attributes(classes(ALERT_ERROR_CLASS), *content)
    )


def long_error_alert(title, *content):
    ''' Returns the HTML code for a long, red error message. '''

    return long_alert(
        title,
        *extract_attributes(classes(ALERT_ERROR_CLASS), *content)
    )


def info_alert(title, *content):
    ''' Returns the HTML code for a small, light-blue info message. '''

    return alert(
        title,
        *extract_attributes(classes(ALERT_INFO_CLASS), *content)
    )


def long_info_alert(title, *content):
    ''' Returns the HTML code for a long, light-blue info message. '''

    return long_alert(
        title,
        *extract_attributes(classes(ALERT_INFO_CLASS), *content)
    )