Zwitscher-Maschine
==================

A Twitter Bootstrap HTML generator. Using the functional style I use for Dynamo
(https://www.github.com/cnvandev/dynamo), you can quickly generate sites that
use Twitter Bootstrap elements. Right now it's fairly bare-bones, I'm not sure
what the API should really look like, and it's really simple as it is right now.

The ultimate goal for this library is to have one line of code (or less!) for
every visible object in the final Twitter Bootstrap page. Knowing the function
names, it should come easily how to write Twitter Bootstrap HTML and it the
output should make sense, as much as possible.

Usage
-----
In any case, you can quickly output HTML code for Twitter Bootstrap-based sites
using this library. Behold!

    alert("This is a Random Title", "This is a random message for you to read. Aren't you happy?")

will output:

    <div class="alert">
        <button data-dismiss="alert" type="button" class="close">x</button>
        <h4>This is a Random Title</h4>
        This is a random message for you to read. Aren't you happy?
    </div>

as a convenient use of the "Alerts" component (see
http://twitter.github.com/bootstrap/components.html#alerts for working examples)
which is one of many you have available. They all return strings, so they can be
combined with other strings or other Dynamo HTML functions or, I don't know,
whatever you want. Combining more complex things:

    basic_template(
        tab_navigation_below(
            tabs(
                active_element("Home", "#tab1"),
                element("About", "#tab2"),
                element("Stuff", "#tab3"),
            ),
            tab_container(
                tab_pane("#tab1", p("Home!")),
                tab_pane("#tab2", p("About!")),
                tab_pane("#tab3", p("Stuff!"))
            )
        )
    )

you end up with:

    <!DOCTYPE html>
    <html>
        <head>
            <title>Bootstrap 101 Template</title>
            <!--Bootstrap-->
            <link media="screen" href="https://netdna.bootstrapcdn.com/twitter-bootstrap/2.2.1/css/bootstrap.min.css" rel="stylesheet" />
        </head>
        <body>
            <div class="container">
                <div class="tabbable tab-below">
                    <ul class="nav nav-tabs">
                        <li class="active">
                            <a href="#tab1">Home</a>
                        </li>
                        <li>
                            <a href="#tab2">About</a>
                        </li>
                        <li>
                            <a href="#tab3">Stuff</a>
                        </li>
                    </ul>
                    <div class="tab-content">
                        <div class="tab-pane" id="#tab1">
                            <p>Home!</p>
                        </div>
                        <div class="tab-pane" id="#tab2">
                            <p>About!</p>
                        </div>
                        <div class="tab-pane" id="#tab3">
                            <p>Stuff!</p>
                        </div>
                    </div>
                </div>
                <script src="https://code.jquery.com/jquery-latest.js"></script>
                <script src="https://netdna.bootstrapcdn.com/twitter-bootstrap/2.2.1/js/bootstrap.min.js"></script>
            </div>
        </body>
    </html>

It needs a lot of work, all additions are appreciated.

Name
----
*What's with the weird name? It's the name of one of my favourite paintings, a
piece by Paul Klee called "Die Zwitscher-Machine"
(http://www.moma.org/collection/object.php?object_id=37347). It's a
cute-but-eerie-looking watercolour depiction of a machine made up of a crank
attached to a set of mechanical birds. You can almost imagine the mechanical
tweeting and the jerky, automaton-ish movement that would happen if you could
reach in and start turning the crank, like a Tim Burton music box. Since every
software library needs to be named by a pun of some kind, and since it's based
on both Twitter Bootstrap and Dynamo (a fancy word for "generator"),
Zwitscher-Maschine ("Twittering Machine") is a decent fit.*