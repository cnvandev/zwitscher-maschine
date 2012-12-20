import sys
sys.path.append("../dynamo")
from dynamo import *
from common import extract_attributes, classed_ul, classed_span

# Convenience methods for generating Twitter Bootstrap navigation bars.
# http://twitter.github.com/bootstrap/components.html#navbar
#
# Official docs alternate crumbs and dividers - I'll add convenience methods in
# a later release, but proper usage is breadcrumbs(crumb(a({"href": "url"},
# "title")), divider(), crumb(a({"href": "url"}, "title")), divider(), ...)

BREADCRUMBS_CLASS = "breadcrumb"
DIVIDER_CLASS = "divider"

def breadcrumbs(*content):
    ''' Returns the HTML code for a breadcrumb listing. Fill with crumb() and
    divider() elements (see below in this class.) '''

    return classed_ul(BREADCRUMBS_CLASS, *content)


def divider(*content):
    ''' Returns a divider class for use to split breadcrumbs. Twitter Bootstrap
    examples all pass in a slash as the only content.

    '''

    return "&nbsp;" + classed_span(DIVIDER_CLASS, *content)

def crumb(*content):
    ''' Returns a single "crumb" in a breadcrumb group. Common usage is to give
    it a link to the page, but can also take raw text. '''

    return li(*content)