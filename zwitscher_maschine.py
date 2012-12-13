import sys
sys.path.append("dynamo")
from dynamo import *
from misc import container

def basic_template(*content):
    return doctype("html") + "\n" + html(
        head(
            title("Bootstrap 101 Template"),
            comment("Bootstrap"),
            link(href="https://netdna.bootstrapcdn.com/twitter-bootstrap/2.2.1/css/bootstrap.min.css", rel="stylesheet", media="screen"),
        ),
        body(
            container(
                *content,
                append=(
                    script("", src="https://code.jquery.com/jquery-latest.js"),
                    script("", src="https://netdna.bootstrapcdn.com/twitter-bootstrap/2.2.1/js/bootstrap.min.js")
            ),
        )
    )

