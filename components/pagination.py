import sys
sys.path.append("../dynamo")
from dynamo import *
from common import extract_attributes

# Convenience methods for generating Twitter Bootstrap pagination elements.
# http://twitter.github.com/bootstrap/components.html#pagination

PAGINATION_CLASS = "pagination"
PAGINATION_LARGE_CLASS = PAGINATION_CLASS + "-large"
PAGINATION_LARGE_CLASS = PAGINATION_CLASS + "-small"
PAGINATION_LARGE_CLASS = PAGINATION_CLASS + "-mini"


def pagination(*content):
    ''' Returns the HTML for a pagination element. Fill with an unordered list
    (I know, right? Unordered?) to display properly. '''
    
    return classed_div(PAGINATION_CLASS, *content)


def large_pagination(*content):
    ''' Returns the HTML for a huge pagination element. Fill with an unordered
    list to display properly. '''

    return pagination(classes(PAGINATION_LARGE_CLASS), *content)


def small_pagination(*content):
    ''' Returns the HTML for a small pagination element. Fill with an unordered
    list to display properly. '''

    return pagination(classes(PAGINATION_SMALL_CLASS), *content)


def mini_pagination(*content):
    ''' Returns the HTML for a tiny pagination element. Fill with an unordered
    list to display properly. '''

    return pagination(classes(PAGINATION_MINI_CLASS), *content)