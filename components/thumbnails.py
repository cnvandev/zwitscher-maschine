import sys
sys.path.append("../dynamo")
from dynamo import *

# Convenience methods for generating Twitter Bootstrap thumbnails.
# http://twitter.github.com/bootstrap/components.html#thumbnails

SPAN_CLASS = "span"
THUMBNAIL_CLASS = "thumbnail"
THUMBNAILS_CLASS = THUMBNAIL_CLASS + "s"

def thumbnails(*thumbnails):
    ''' Returns the HTML code for a container for thumbnail elements. '''

    return ul(
        *thumbnails,
        **{"class": THUMBNAILS_CLASS}
    )


def thumbnail(span, *elements):
    ''' Returns the HTML code for a single thumbnail element that can contain
    any HTML. Can contain one or multiple elements if needed. '''

    inner_elements = ""
    if len(elements) > 1:
        inner_elements = div(
            *elements,
            **{"class": THUMBNAIL_CLASS}
        )
    else :
        inner_elements = elements

    return li(
        *inner_elements,
        **{"class": SPAN_CLASS + span}
    )