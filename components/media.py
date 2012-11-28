import sys
sys.path.append("../dynamo")
from dynamo import *

# Convenience methods for generating Twitter Bootstrap media elements.
# http://twitter.github.com/bootstrap/components.html#media


MEDIA_CLASS = "media"
MEDIA_LIST_CLASS = MEDIA_CLASS + "-list"
MEDIA_BODY_CLASS = MEDIA_CLASS + "-body"
MEDIA_OBJECT_CLASS = MEDIA_CLASS + "-object"
MEDIA_HEADING_CLASS = MEDIA_CLASS + "-heading"

PULL_LEFT = "pull-left"


def media(img_url, title, link_url, *content):
    ''' Returns the HTML for a basic formatter for a "media object" like a video
    or something. It kind of looks like a Facebook post. '''

    return div(
        *media_content(img_url, title, link_url, *content)
        **{"class", MEDIA_CLASS}
    )


def media_list(*media_items):
    ''' A list that handles media items (even nested!) gracefully. Use
    media_item to generate them. '''

    return ul(
        *media_items
        **{"class": MEDIA_LIST_CLASS}
    )


def media_list_item(img_url, title, link_url, *content):
    ''' A single list item in a media list (see media_list() for something that
    is designed to gracefully hold them). '''

    return li(
        *media_content(img_url, title, link_url, *content),
        **{"class": MEDIA_CLASS}
    )


def media_content(img_url, title, link_url, *content):
    ''' Returns the content to a media block. Should only be used internally,
    use media() or media_list() + media_list_item(). '''

    return [
        a(
            img(**{"src": img_url, "class": MEDIA_OBJECT_CLASS}),
            **{"class": PULL_LEFT, "href": link_url}
        ),
        div(
            h4(title, **{"class": MEDIA_HEADING_CLASS}),
            *content,
            **{"class": MEDIA_BODY_CLASS}
        )
    ]