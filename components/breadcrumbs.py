import sys
sys.path.append("../dynamo")
from dynamo import *

# Convenience methods for generating Twitter Bootstrap navigation bars.
# http://twitter.github.com/bootstrap/components.html#navbar
#
# Official docs alternate crumbs and dividers - I'll add convenience methods in
# a later release, but proper usage is breadcrumbs(crumb("url", "title"),
# divider(), crumb("url", "title"), divider(), ...)

BREADCRUMBS_CLASS = "breadcrumb"
DIVIDER_CLASS = "divider"

def breadcrumbs(*elements):
    ''' Returns the HTML code for a breadcrumb listing. Fill with crumb() and
    divider() elements (see below in this class.) '''

    return ul(
        *elements,
        **{"class": BREADCRUMBS_CLASS}
    )


def divider():
    ''' Returns a divider class for use to split breadcrumbs. It's a slash. '''

    return "&nbsp;" + span("/", **{"class": DIVIDER_CLASS})

def crumb(text, url):
    ''' Returns a single "crumb" in a breadcrumb group, taking text and a URL to
    point it all to. '''

    return li(a(text, href=url))