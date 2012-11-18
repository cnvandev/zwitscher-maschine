import sys
sys.path.append("dynamo")
from dynamo import *

def basic_template(content):
    return doctype("html") + "\n" + html(
        head(
            title("Bootstrap 101 Template"),
            comment("Bootstrap"),
            link(href="css/boostrap.min.css", rel="stylesheet", media="screen")
        ),
        body(
            content,
            script("", src="http://code.jquery.com/jquery-latest.js"),
            script("", src="js/bootstrap.min.js")
        )
    )