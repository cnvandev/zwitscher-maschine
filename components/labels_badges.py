import sys
sys.path.append("../dynamo")
from dynamo import *
from common import classed_span, classes

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

def default_label(*content):
    ''' Returns the HTML code for a grey-coloured label. ''' 

    return classed_span(LABEL_CLASS, *content)


def success_label(*content):
    ''' Returns the HTML code for a successfully-green coloured label. '''

    return default_label(classes(LABEL_SUCCESS_CLASS), *content)


def warning_label(*content):
    ''' Returns the HTML code for an orange warning label. '''

    return default_label(classes(LABEL_WARNING_CLASS), *content)


def important_label(*content):
    ''' Returns the HTML code for a red AHHHHHHHHH! label. '''

    return default_label(classes(LABEL_IMPORTANT_CLASS), *content)


def info_label(*content):
    ''' Returns the HTML code for a light blue info label. '''

    return default_label(classes(LABEL_INFO_CLASS), *content)


def inverse_label(*content):
    ''' Returns the HTML code for a black label with white text. '''

    return default_label(classes(LABEL_INVERSE_CLASS), *content)


def default_badge(*content):
    ''' Returns the HTML code for a grey-coloured badge. ''' 

    return classed_span(BADGE_CLASS, *content)


def success_badge(*content):
    ''' Returns the HTML code for a successfully-green coloured badge. '''

    return default_badge(classes(BADGE_SUCCESS_CLASS), *content)


def warning_badge(*content):
    ''' Returns the HTML code for an orange warning badge. '''

    return default_badge(classes(BADGE_WARNING_CLASS), *content)


def important_badge(*content):
    ''' Returns the HTML code for a red AHHHHHHHHH! badge. '''

    return default_badge(classes(BADGE_IMPORTANT_CLASS), *content)


def info_badge(*content):
    ''' Returns the HTML code for a light blue info badge. '''

    return default_badge(classes(BADGE_INFO_CLASS), *content)


def inverse_badge(*content):
    ''' Returns the HTML code for a black badge with a white number. '''

    return default_badge(classes(BADGE_INVERSE_CLASS), *content)