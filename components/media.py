import sys
sys.path.append("../dynamo")
from dynamo import *
from common import extract_attributes, classes, classed_div, classed_ul, classed_li, combine

# Convenience methods for generating Twitter Bootstrap media elements.
# http://twitter.github.com/bootstrap/components.html#media


MEDIA_CLASS = "media"
MEDIA_LIST_CLASS = combine(MEDIA_CLASS, "list")
MEDIA_BODY_CLASS = combine(MEDIA_CLASS, "body")
MEDIA_OBJECT_CLASS = combine(MEDIA_CLASS, "object")
MEDIA_HEADING_CLASS = combine(MEDIA_CLASS, "heading")

PULL_LEFT = "pull-left"


def media(img_url, title, link_url, *content):
    ''' Returns the HTML for a basic formatter for a "media object" like a video
    or something. It kind of looks like a Facebook post. '''

    return classed_div(MEDIA_CLASS,
        *media_content(img_url, title, link_url, *content
    )


def media_list(*content):
    ''' A list that handles media items (even nested!) gracefully. Use
    media_list_item to generate them. '''

    return classed_ul(MEDIA_LIST_CLASS, *content)


def media_list_item(img_url, title, link_url, *content):
    ''' A single list item in a media list (see media_list() for something that
    is designed to gracefully hold them). '''

    return classed_li(MEDIA_CLASS,
        *media_content(img_url, title, link_url, *content)
    )


def media_content(img_url, title, link_url, *content):
    ''' Returns the content to a media block. Should only be used internally,
    use media() or media_list() + media_list_item(). '''

    return [
        a({"class": PULL_LEFT, "href": link_url},
            img({"src": img_url, "class": MEDIA_OBJECT_CLASS})
        ),
        classed_div(MEDIA_BODY_CLASS,
            h4(classes(MEDIA_HEADING_CLASS), title),
            *content
        )
    ]