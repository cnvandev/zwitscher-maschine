import sys
sys.path.append("../dynamo")
from dynamo import *
from common import extract_attributes

# Convenience methods for generating Twitter Bootstrap alert elements.
# http://twitter.github.com/bootstrap/components.html#alerts

ALERT_CLASS = "alert"
ALERT_BLOCK_CLASS = ALERT_CLASS + "-block"
CLOSE_CLASS = "close"
BUTTON_CLASS = "button"

ALERT_ERROR_CLASS = ALERT_CLASS + "-error"
ALERT_SUCCESS_CLASS = ALERT_CLASS + "-success"
ALERT_INFO_CLASS = ALERT_CLASS + "-info"

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

    # We need to add two children to the top of the content list. However, we
    # don't know whether there is an extra attributes hash in the first slot of
    # the content list. But, we do know that there will such a hash *after* the
    # attributes are merged (because that's why we're merging, we're adding
    # attributes), so we'll add the children after the hash has been merged
    # into offsets 1 and 2.
    # I would love a cleaner way to do this.
    merged_content = list(extract_attributes({"class": ALERT_CLASS}, *content))
    merged_content.insert(1, 
        button(
            {
                "type": BUTTON_CLASS,
                "class": CLOSE_CLASS,
                "data-dismiss": ALERT_CLASS
            },
            "x"
        )
    )
    merged_content.insert(2, strong(title) if is_long else h4(title))

    return div(
        *merged_content
    )


def success_alert(title, *content):
    ''' Returns the HTML code for a small, green success message. '''

    return alert(
        title,
        *extract_attributes({"class": ALERT_SUCCESS_CLASS}, *content)
    )


def long_success_alert(title, *content):
    ''' Returns the HTML code for a long, green success message. '''

    return long_alert(
        title,
        *extract_attributes({"class": ALERT_SUCCESS_CLASS}, *content)
    )


def error_alert(title, *content):
    ''' Returns the HTML code for a small, red error message. '''

    return alert(
        title,
        *extract_attributes({"class": ALERT_ERROR_CLASS}, *content)
    )


def long_error_alert(title, *content):
    ''' Returns the HTML code for a long, red error message. '''

    return long_alert(
        title,
        *extract_attributes({"class": ALERT_ERROR_CLASS}, *content)
    )


def info_alert(title, *content):
    ''' Returns the HTML code for a small, light-blue info message. '''

    return alert(
        title,
        extract_attributes({"class": ALERT_INFO_CLASS}, *content)
    )


def long_info_alert(title, *content):
    ''' Returns the HTML code for a long, light-blue info message. '''

    return long_alert(
        title,
        extract_attributes({"class": ALERT_INFO_CLASS}, *content)
    )