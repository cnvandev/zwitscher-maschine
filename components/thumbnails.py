import sys
sys.path.append("../dynamo")
from dynamo import *
from common import extract_attributes

# Convenience methods for generating Twitter Bootstrap thumbnails.
# http://twitter.github.com/bootstrap/components.html#thumbnails

SPAN_CLASS = "span"
THUMBNAIL_CLASS = "thumbnail"
THUMBNAILS_CLASS = THUMBNAIL_CLASS + "s"

def thumbnails(*content):
    ''' Returns the HTML code for a container for thumbnail elements. '''

    return ul(
        *extract_attributes(
            {"class": THUMBNAILS_CLASS},
            *content
        )
    )


def thumbnail(span, *content):
    ''' Returns the HTML code for a single thumbnail element that can contain
    any HTML. Can contain one or multiple elements if needed. '''

    inner_elements = ""
    if len(elements) > 1:
        inner_elements = div(
            {"class": THUMBNAIL_CLASS},
            *content
        )
    else :
        inner_elements = content

    return li(
        *extract_attributes(
            {"class": SPAN_CLASS + span},
            *inner_elements
        )
    )