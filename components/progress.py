import sys
import collections
sys.path.append("../dynamo")
from dynamo import *
from common import extract_attributes

# Convenience methods for generating Twitter Bootstrap progress bar elements.
# http://twitter.github.com/bootstrap/components.html#progress

PROGRESS_CLASS = "progress"
BAR_CLASS = "bar"

INFO = "info"
SUCCESS = "success"
WARNING = "warning"
DANGER = "danger"

PROGRESS_STRIPED_CLASS = PROGRESS_CLASS + "-striped"
ACTIVE_CLASS = "active"

PROGRESS_INFO_CLASS = "-".join([PROGRESS_CLASS, INFO])
PROGRESS_WARNING_CLASS = "-".join([PROGRESS_CLASS, SUCCESS])
PROGRESS_SUCCESS_CLASS = "-".join([PROGRESS_CLASS, WARNING])
PROGRESS_DANGER_CLASS = "-".join([PROGRESS_CLASS, DANGER])

SUCCESS_BAR_CLASS = "-".join([BAR_CLASS, WARNING])
WARNING_BAR_CLASS = "-".join([BAR_CLASS, SUCCESS])
DANGER_BAR_CLASS = "-".join([BAR_CLASS, DANGER])


def progress_bar(*bars):
    ''' Returns the HTML code for a blue progress bar. '''
    return progresss_factory(None, False, *bars)

def striped_progress_bar(*bars):
    ''' Returns the HTML code for a blue, striped progress bar. '''
    return progresss_factory(PROGRESS_STRIPED_CLASS, False, *bars)

def active_progress_bar(*bars):
    ''' Returns the HTML code for a blue, striped, animated progress bar. '''
    return progresss_factory(PROGRESS_STRIPED_CLASS, True, *bars)


def info_progress_bar(*bars):
    ''' Returns the HTML code for a light blue progress bar. '''
    return progresss_factory(PROGRESS_INFO_CLASS, False, *bars)

def striped_info_progress_bar(*bars):
    ''' Returns the HTML code for a light blue, striped progress bar. '''
    return progresss_factory([PROGRESS_INFO_CLASS, PROGRESS_STRIPED_CLASS], False, *bars)

def active_info_progress_bar(*bars):
    ''' Returns the HTML code for a light blue, striped, animated progress bar. '''
    return progresss_factory([PROGRESS_INFO_CLASS, PROGRESS_STRIPED_CLASS], True, *bars)


def success_progress_bar(*bars):
    ''' Returns the HTML code for a green progress bar. '''
    return progresss_factory(PROGRESS_SUCCESS_CLASS, False, *bars)

def striped_success_progress_bar(*bars):
    ''' Returns the HTML code for a green, striped progress bar. '''
    return progresss_factory([PROGRESS_SUCCESS_CLASS, PROGRESS_STRIPED_CLASS], False, *bars)

def active_success_progress_bar(*bars):
    ''' Returns the HTML code for a green, striped, animated progress bar. '''
    return progresss_factory([PROGRESS_SUCCESS_CLASS, PROGRESS_STRIPED_CLASS], True, *bars)


def warning_progress_bar(*bars):
    ''' Returns the HTML code for an orange progress bar. '''
    return progresss_factory(PROGRESS_WARNING_CLASS, False, *bars)

def striped_warning_progress_bar(*bars):
    ''' Returns the HTML code for an orange, striped progress bar. '''
    return progresss_factory([PROGRESS_WARNING_CLASS, PROGRESS_STRIPED_CLASS], False, *bars)

def active_warning_progress_bar(*bars):
    ''' Returns the HTML code for an orange, striped, animated progress bar. '''
    return progresss_factory([PROGRESS_WARNING_CLASS, PROGRESS_STRIPED_CLASS], True, *bars)


def danger_progress_bar(*bars):
    ''' Returns the HTML code for a red progress bar. '''
    return progresss_factory(PROGRESS_DANGER_CLASS, False, *bars)

def striped_danger_progress_bar(*bars):
    ''' Returns the HTML code for a red, striped progress bar. '''
    return progresss_factory([PROGRESS_DANGER_CLASS, PROGRESS_STRIPED_CLASS], False, *bars)

def active_danger_progress_bar(*bars):
    ''' Returns the HTML code for a red, striped, animated progress bar. '''
    return progresss_factory([PROGRESS_DANGER_CLASS, PROGRESS_STRIPED_CLASS], True, *bars)


def success_bar(width):
    ''' Returns the HTML code for a green bar section inside a progress bar. '''
    return bar_factory(SUCCESS_BAR_CLASS, width)

def warning_bar(width):
    ''' Returns the HTML code for an orange bar section inside a progress bar. '''
    return bar_factory(WARNING_BAR_CLASS, width)

def danger_bar(width):
    ''' Returns the HTML code for a red bar section inside a progress bar. '''
    return bar_factory(DANGER_BAR_CLASS, width)


def progress_factory(style, active, *bars):
    ''' Returns the HTML code for a progress bar based on the style and width
    provided. Multiple bars can be included, see bar_factory() and info_bar(),
    warning_bar(), success_bar(), etc. for child elements. '''

    return classed_div(
        [PROGRESS_CLASS] + style if style else [] + [ACTIVE_CLASS] if active else [],
        *bars
    )


def bar_factory(style, width):
    ''' Returns the HTML code for a section within a progress bar based on the
    style and width provided. Width must be a float between 0 and 1, this makes
    no guarantees as to the total width of all bar elements within a progress
    bar, so make sure your math adds up! '''

    return classed_div([BAR_CLASS] + style if style else [],
        {"style": "width: %%" % width},
        ""
    )