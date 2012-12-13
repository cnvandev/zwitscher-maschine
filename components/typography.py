import sys
sys.path.append("../dynamo")
from dynamo import *
from common import extract_attributes, classed_div, combine

# Convenience methods for generating Twitter Bootstrap typographic elements.
# http://twitter.github.com/bootstrap/components.html#typography

HERO_UNIT_CLASS = combine("hero", "unit")
PAGE_HEADER_CLASS = combine("page", "header")


def hero_unit(*content):
    ''' Returns the HTML code for a 'Hero Unit', like a big marketing banner on
    a front page. '''

    return classed_div(HERO_UNIT_CLASS, *elements)


def page_header(title, subtitle):
    ''' Returns the HTML for a page header or title, with a subtitle. '''
    
    return classed_div(PAGE_HEADER_CLASS,
        h1(title, small(subtitle)
    )