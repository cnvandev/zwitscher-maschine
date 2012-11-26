import sys
sys.path.append("../dynamo")
from dynamo import *

# Convenience methods for generating Twitter Bootstrap typographic elements.
# http://twitter.github.com/bootstrap/components.html#typography

HERO_UNIT_CLASS = "hero-unit"
PAGE_HEADER_CLASS = "page-header"


def hero_unit(*elements):
    ''' Returns the HTML code for a 'Hero Unit', like a big marketing banner on
    a front page. '''

    return div(
        *elements,
        **{"class": HERO_UNIT_CLASS}
    )


def page_header(title, subtitle):
    ''' Returns the HTML for a page header or title, with a subtitle. '''
    
    return div(
        h1(title, small(subtitle)),
        **{"class": PAGE_HEADER_CLASS}
    )