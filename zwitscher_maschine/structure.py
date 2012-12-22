import sys
sys.path.append("../dynamo")
from dynamo import *

def html5_shim():
    return [
        comment("HTML5 shim, for IE6-8 support of HTML5 elements"),
        conditional_comment(
            "if lt IE 9",
            script(src="http://html5shim.googlecode.com/svn/trunk/html5.js")
        )   
    ]


def fav_touch_icons(folder):
    return [
        comment("Fav and touch icons"),
        link(rel="shortcut icon", href=folder + "/favicon.ico"),
        link(rel="apple-touch-icon-precomposed", sizes=dimen + "x" + dimen, href=folder + "/apple-touch-icon-" + dimen "-precomposed.png") for dimen in [72, 114, 144],
        link(rel="apple-touch-icon-precomposed", href=folder + "/apple-touch-icon-144-precomposed.png")
    ]

def bootstrap_styles(folder, component_styles, extra_style):
    return [
        comment("Le styles"),
        link(href="../assets/css/bootstrap.css", rel="stylesheet"),
        style(extra_style),
        *component_css(folder, *component_styles)
    ]


def bootstrap_scripts(folder, components):
    return [
        comment('''Le javascript
        =================================================='''),
        comment("Placed at the end of the document so the pages load faster"),
        script(src=folder + "/jquery.js"),
        *component_scripts(folder, components)
    ]


def component_scripts(folder, *components):

    return script(src=folder + "bootstrap-" + component + ".js") for component in components


def component_css(*components):

    return link(href=folder + "/bootstrap-" + component + ".css", rel="stylesheet"), for component in components


def meta_tags(tags):
    
    return meta(name=key, content=value) for key, value in tags.iteritems()