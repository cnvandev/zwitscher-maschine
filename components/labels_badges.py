import sys
sys.path.append("../dynamo")
from dynamo import *

# Convenience methods for generating Twitter Bootstrap labels and badges.
# http://twitter.github.com/bootstrap/components.html#labels-badges

LABEL_CLASS = "label"
BADGE_CLASS = "badge"

SUCCESS = "success"
WARNING = "warning"
IMPORTANT = "important"
INFO = "info"
INVERSE = "inverse"

LABEL_SUCCESS_CLASS = "-".join([LABEL_CLASS, SUCCESS])
LABEL_WARNING_CLASS = "-".join([LABEL_CLASS, WARNING])
LABEL_IMPORTANT_CLASS = "-".join([LABEL_CLASS, IMPORTANT])
LABEL_INFO_CLASS = "-".join([LABEL_CLASS, INFO])
LABEL_INVERSE_CLASS = "-".join([LABEL_CLASS, INVERSE])

BADGE_SUCCESS_CLASS = "-".join([BADGE_CLASS, SUCCESS])
BADGE_WARNING_CLASS = "-".join([BADGE_CLASS, WARNING])
BADGE_IMPORTANT_CLASS = "-".join([BADGE_CLASS, IMPORTANT])
BADGE_INFO_CLASS = "-".join([BADGE_CLASS, INFO])
BADGE_INVERSE_CLASS = "-".join([BADGE_CLASS, INVERSE])

def default_label(text):
    ''' Returns the HTML code for a grey-coloured label. ''' 

    return span(text, **{"class": LABEL_CLASS})


def success_label(text):
    ''' Returns the HTML code for a successfully-green coloured label. '''

    return span(text, **{"class": " ".join([LABEL_CLASS, LABEL_SUCCESS_CLASS])})


def warning_label(text):
    ''' Returns the HTML code for an orange warning label. '''

    return span(text, **{"class": " ".join([LABEL_CLASS, LABEL_WARNING_CLASS])})


def important_label(text):
    ''' Returns the HTML code for a red AHHHHHHHHH! label. '''

    return span(text, **{"class": " ".join([LABEL_CLASS, LABEL_IMPORTANT_CLASS])})


def info_label(text):
    ''' Returns the HTML code for a light blue info label. '''

    return span(text, **{"class": " ".join([LABEL_CLASS, LABEL_INFO_CLASS])})


def inverse_label(text):
    ''' Returns the HTML code for a black label with white text. '''

    return span(text, **{"class": " ".join([LABEL_CLASS, LABEL_INVERSE_CLASS])})


def default_badge(number):
    ''' Returns the HTML code for a grey-coloured badge. ''' 

    return span(number, **{"class": BADGE_CLASS})


def success_badge(number):
    ''' Returns the HTML code for a successfully-green coloured badge. '''

    return span(number, **{"class": " ".join([BADGE_CLASS, BADGE_SUCCESS_CLASS])})


def warning_badge(number):
    ''' Returns the HTML code for an orange warning badge. '''

    return span(number, **{"class": " ".join([BADGE_CLASS, BADGE_WARNING_CLASS])})


def important_badge(number):
    ''' Returns the HTML code for a red AHHHHHHHHH! badge. '''

    return span(number, **{"class": " ".join([BADGE_CLASS, BADGE_IMPORTANT_CLASS])})


def info_badge(number):
    ''' Returns the HTML code for a light blue info badge. '''

    return span(number, **{"class": " ".join([BADGE_CLASS, BADGE_INFO_CLASS])})


def inverse_badge(number):
    ''' Returns the HTML code for a black badge with a white number. '''

    return span(number, **{"class": " ".join([BADGE_CLASS, BADGE_INVERSE_CLASS])})