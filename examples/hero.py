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
            brand(href("#"), "Project Name"),
            li(active(), a("Home", href="#")),
            li(a("About", href="#about")),
            li(a("Contact", href="#contact")),

            nav_dropdown("Dropdown"
                dropdown_menu(
                    li(a("Action", href="#")),
                    li(a("Anotion action", href="#")),
                    li(a("Something else here", href="#")),
                    divider(),
                    nav_header("Nav header"),
                    li(a("Separated link", href="#")),
                    li(a("Something else here", href="#")),
                )
            ),
            nav_form(classes("pull-right"),
                Input({"class": "span2", "type": "text", "placeholder": "Email")),
                Input({"class": "span2", "type": "text", "placeholder": "Password")),
                zm_button({"type": "submit"}, "Sign in")
            )
        )

        container(
            comment("Example row of columns")
            *[
                grid_row(
                    column_span(4,
                        h2("Heading"),
                        p("Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui."),
                        p(link_button("View details &raquo;", href="#"))
                    )
                ) for number in [1, 2, 3]
            ],
            hr(),
            footer(p("&copy; Company 2012"))
        ) + comment("/.container"),

        bootstrap_scripts("../assets/js/", "transition", "alert", "modal", "dropdown", "scrollspy", "tab", "tooltip", "popover", "button", "collapse", "carousel", "typeahead")
    )
)