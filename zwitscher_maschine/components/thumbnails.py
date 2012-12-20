import sys
sys.path.append("../dynamo")
from dynamo import *
from common import extract_attributes, classed_ul, classed_li, classed_div

# Convenience methods for generating Twitter Bootstrap thumbnails.
# http://twitter.github.com/bootstrap/components.html#thumbnails

SPAN_CLASS = "span"
THUMBNAIL_CLASS = "thumbnail"
THUMBNAILS_CLASS = THUMBNAIL_CLASS + "s"

def thumbnails(*content):
    ''' Returns the HTML code for a container for thumbnail elements. '''

    return classed_ul(THUMBNAILS_CLASS, *content)


def thumbnail(span, *content):
    ''' Returns the HTML code for a single thumbnail element that can contain
    any HTML. Can contain one or multiple elements if needed. '''

    return classed_li(SPAN_CLASS + span,
        *([classed_div(THUMBNAIL_CLASS, *content)] if len(elements) > 1 else content)
    )