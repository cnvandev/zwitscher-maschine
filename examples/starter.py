from ..dynamo import *
from components.misc import *
from navbar import NAVBAR_INVERSE_CLASS, NAVBAR_FIXED_TOP_CLASS, navbar
from structure import *

print doctype("html")
print html({"lang": "en"},
    head(
        meta(charset="utf-8"),
        title("Bootstrap, from Twitter"),
        meta_tags({
            "viewport": "view=device-width, initial-scale=1.0",
            "description": "",
            "author": ""
        })

        styles("../assets/css",
        '''
            body {
                padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
            }
        ''',
        "responsive")
        html5_shim()
        fav_touch_icons("../assets/ico")
    ),
    body(
        responsive_navigation(
            [NAVBAR_INVERSE_CLASS, NAVBAR_FIXED_TOP_CLASS],
            brand(href("#"), "Project Name")
            li(active(), a("Home", href="#")),
            li(a("About", href="#about")),
            li(a("Contact", href="#contact"))
        )

        container(,
            h1("Boostrap starter template"),
            p("Use this document as a way to quick start any new project." + br() + "All you get is this message and a barebones HTML document.")
        ) + comment("/.container"),

        bootstrap_scripts("../assets/js/", "transition", "alert", "modal", "dropdown", "scrollspy", "tab", "tooltip", "popover", "button", "collapse", "carousel", "typeahead")
    )
)