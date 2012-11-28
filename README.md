Zwitscher-Maschine
==================

A Twitter Bootstrap HTML generator. Using the functional style I use for Dynamo
(https://www.github.com/cnvandev/dynamo), you can quickly generate sites that
use Twitter Bootstrap elements. Right now it's fairly bare-bones, I'm not sure
what the API should really look like, and it's really simple as it is right now.

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
whatever you want.

*What's with the weird name? It's the name of one of my favourite paintings, a
piece by Paul Klee called "Die Zwitscher-Machine," a cute-but-eerie-looking
watercolour depiction of a machine made up of a crank attached to a set of
mechanical birds. You can almost imagine the mechanical tweeting and the jerky,
automaton-ish movement that would happen if you could reach in and start turning
the crank, like a Tim Burton music box. Since every software library needs to be
named by a pun of some kind, and since it's based on both Twitter Bootstrap and
Dynamo (a fancy word for "generator"), Zwitscher-Maschine ("Twittering Machine")
is a decent fit.*