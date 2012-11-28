import sys
sys.path.append("../dynamo")
from dynamo import *

# Convenience methods for generating Twitter Bootstrap alert elements.
# http://twitter.github.com/bootstrap/components.html#alerts

ALERT_CLASS = "alert"
ALERT_BLOCK_CLASS = ALERT_CLASS + "-block"
CLOSE_CLASS = "close"
BUTTON_CLASS = "button"

ALERT_ERROR_CLASS = ALERT_CLASS + "-error"
ALERT_SUCCESS_CLASS = ALERT_CLASS + "-success"
ALERT_INFO_CLASS = ALERT_CLASS + "-info"

def alert(title, message):
    ''' Returns the HTML code for a small, yellow alert message. '''

    return alert_factory(ALERT_CLASS, False, title, message)


def long_alert(title, message):
    ''' Returns the HTML code for a long, yellow alert message. '''

    return alert_factory(ALERT_CLASS, True, title, message)


def success_alert(title, message):
    ''' Returns the HTML code for a small, green success message. '''

    return alert_factory(" ".join([ALERT_CLASS, ALERT_SUCCESS_CLASS]), False, title, message)


def long_success_alert(title, message):
    ''' Returns the HTML code for a long, green success message. '''

    return alert_factory(" ".join([ALERT_CLASS, ALERT_SUCCESS_CLASS]), True, title, message)


def error_alert(title, message):
    ''' Returns the HTML code for a small, red error message. '''

    return alert_factory(" ".join([ALERT_CLASS, ALERT_ERROR_CLASS]), False, title, message)


def long_error_alert(title, message):
    ''' Returns the HTML code for a long, red error message. '''

    return alert_factory(" ".join([ALERT_CLASS, ALERT_ERROR_CLASS]), True, title, message)


def info_alert(title, message):
    ''' Returns the HTML code for a small, light-blue info message. '''

    return alert_factory(" ".join([ALERT_CLASS, ALERT_INFO_CLASS]), False, title, message)


def long_info_alert(title, message):
    ''' Returns the HTML code for a long, light-blue info message. '''

    return alert_factory(" ".join([ALERT_CLASS, ALERT_INFO_CLASS]), True, title, message)    


def alert_factory(type_class, is_long, title, message):
    ''' Returns the HTML code for a generic alert message. '''

    return div(
        button(
            "x",
            **{
                "type": BUTTON_CLASS,
                "class": CLOSE_CLASS,
                "data-dismiss": type_class
            }
        ),
        strong(title) if is_long else h4(title),
        message,
        **{"class": type_class}
    )