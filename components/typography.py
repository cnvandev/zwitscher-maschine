import sys
sys.path.append("../dynamo")
from dynamo import *
from common import extract_attributes

# Convenience methods for generating Twitter Bootstrap typographic elements.
# http://twitter.github.com/bootstrap/components.html#typography

HERO_UNIT_CLASS = "hero-unit"
PAGE_HEADER_CLASS = "page-header"


def hero_unit(*content):
    ''' Returns the HTML code for a 'Hero Unit', like a big marketing banner on
    a front page. '''

    return div(*extract_attributes({"class": HERO_UNIT_CLASS}, *elements))


def page_header(title, subtitle):
    ''' Returns the HTML for a page header or title, with a subtitle. '''
    
    return div(
        *extract_attributes({"class": PAGE_HEADER_CLASS},
            h1(title, small(subtitle)
        )
    )