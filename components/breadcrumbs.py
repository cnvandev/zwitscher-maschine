import sys
sys.path.append("../dynamo")
from dynamo import *
from common import extract_attributes

# Convenience methods for generating Twitter Bootstrap navigation bars.
# http://twitter.github.com/bootstrap/components.html#navbar
#
# Official docs alternate crumbs and dividers - I'll add convenience methods in
# a later release, but proper usage is breadcrumbs(crumb(a({"href": "url"},
# "title")), divider(), crumb(a({"href": "url"}, "title")), divider(), ...)

BREADCRUMBS_CLASS = "breadcrumb"
DIVIDER_CLASS = "divider"

def breadcrumbs(*crumbs):
    ''' Returns the HTML code for a breadcrumb listing. Fill with crumb() and
    divider() elements (see below in this class.) '''

    return ul(
        *extract_attributes({"class": BREADCRUMBS_CLASS}, *crumbs)
    )


def divider(*content):
    ''' Returns a divider class for use to split breadcrumbs. It's a slash. '''

    return "&nbsp;" + span(*extract_attributes({"class": DIVIDER_CLASS}, *(content + ("/",))))

def crumb(*content):
    ''' Returns a single "crumb" in a breadcrumb group. Common usage is to give
    it a link to the page, but can also take raw text. '''

    return li(
        *content
    )