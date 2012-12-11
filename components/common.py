import collections
import sys
sys.path.append("../dynamo")
from dynamo import *

def extract_attributes(attributes, *content):
    # If there's nothing to add, pass the attributes through.
    if len(content) is 0 or not isinstance(content[0], dict):
        if attributes:
            content = list(content)
            content.insert(0, attributes)
    else:
        for (key, value) in attributes.iteritems():
            if key in content[0]:
                # If the new value's not a list, make it so!
                if not isinstance(value, collections.Iterable) or isinstance(value, basestring):
                    value = [value]

                # If the old value's not a list, make it so!
                if not isinstance(content[0][key], collections.Iterable) or isinstance(content[0][key], basestring):
                    content[0][key] = [content[0][key]]

                # Join the two lists in holy matrimony.
                content[0][key].extend(value)
            else:
                content[0][key] = value

    return content


# We cheat a bit here - Dynamo uses tag_with_child internally to construct tags,
# all of the tag methods just pass through to it. We use this to abstract
# classed tag generation up a level so we have to write extract_attributes only
# once.
def classed_open_tag(tag, dem_classes, *content):
    return tag_with_child(tag, *extract_attributes(classes(dem_classes), *content))


def classed_closed_tag(tag, dem_classes, *content):
    return tag_with_child(tag, *extract_attributes(classes(dem_classes), *content))


##### Classed-tag convenience functions

def classed_div(dem_classes, *content):
    return classed_open_tag("div", dem_classes, *content)


def classed_ul(dem_classes, *content):
    return classed_open_tag("ul", dem_classes, *content)


def classed_li(dem_classes, *content):
    return classed_open_tag("li", dem_classes, *content)


def classed_button(dem_classes, *content):
    return classed_open_tag("button", dem_classes, *content)


def classed_span(dem_classes, *content):
    return classed_open_tag("span", dem_classes, *content)


def classed_form(dem_classes, *content):
    return classed_open_tag("form", dem_classes, *content)


def classed_input(dem_classes, *content):
    return classed_open_tag("input", dem_classes, *content)


def classed_a(dem_classes, *content):
    return classed_open_tag("a", dem_classes, *content)


def classed_p(dem_classes, *content):
    return classed_open_tag("p", dem_classes, *content)


##### Attribute convenience functions

def classes(dem_classes):
    return {"class": dem_classes}


def untabbable():
    return {"tabindex": "-1"}