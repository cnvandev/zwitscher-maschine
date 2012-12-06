import sys
sys.path.append("dynamo")
from dynamo import *

def basic_template(*content):
    return doctype("html") + "\n" + html(
        head(
            title("Bootstrap 101 Template"),
            comment("Bootstrap"),
            link(href="https://netdna.bootstrapcdn.com/twitter-bootstrap/2.2.1/css/bootstrap.min.css", rel="stylesheet", media="screen"),
        ),
        body(
            div(
                *content +
                (
                    script("", src="https://code.jquery.com/jquery-latest.js"),
                    script("", src="https://netdna.bootstrapcdn.com/twitter-bootstrap/2.2.1/js/bootstrap.min.js")
                ),
                **{"class": "container"}
            )
        )
    )

