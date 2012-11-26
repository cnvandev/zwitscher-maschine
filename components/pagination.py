import sys
sys.path.append("../dynamo")
from dynamo import *

# Convenience methods for generating Twitter Bootstrap pagination elements.
# http://twitter.github.com/bootstrap/components.html#pagination

PAGINATION_CLASS = "pagination"
PAGINATION_LARGE_CLASS = PAGINATION_CLASS + "-large"
PAGINATION_LARGE_CLASS = PAGINATION_CLASS + "-small"
PAGINATION_LARGE_CLASS = PAGINATION_CLASS + "-mini"


def large_pagination(*elements):
    ''' Returns the HTML for a huge pagination element. Fill with an unordered
    list to display properly. '''

    return div(
        *elements,
        **{"class": " ".join([PAGINATION_CLASS, PAGINATION_LARGE_CLASS])}
    )


def pagination(*elements):
    ''' Returns the HTML for a pagination element. Fill with an unordered list
    (I know, right? Unordered?) to display properly. '''
    
    return div(
        *elements,
        **{"class": PAGINATION_CLASS}
    )


def small_pagination(*elements):
    ''' Returns the HTML for a small pagination element. Fill with an unordered
    list to display properly. '''

    return div(
        *elements,
        **{"class": " ".join([PAGINATION_CLASS, PAGINATION_SMALL_CLASS])}
    )


def mini_pagination(*elements):
    ''' Returns the HTML for a tiny pagination element. Fill with an unordered
    list to display properly. '''

    return div(
        *elements,
        **{"class": " ".join([PAGINATION_CLASS, PAGINATION_MINI_CLASS])}
    )