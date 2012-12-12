import collections
import sys
sys.path.append("../dynamo")
from dynamo import *

def extract_attributes(attributes, *content, **kwargs):
    # If there's nothing to add, pass the attributes through.
    initial_offset = 0
    if len(content) is 0 or not isinstance(content[0], dict):
        if attributes:
            content = list(content)
            content.insert(0, attributes)
    else:
        for (key, value) in attributes.iteritems():
            if key in content[0]:
                # If either values aren't lists, make them so!
                value = ensure_list(value)
                content[0][key] = ensure_list(content[0][key])

                # Join the two lists in holy matrimony.
                content[0][key].extend(value)
            else:
                content[0][key] = value

    # If we have anything to prepend or append
    if kwargs.has_key("prepend"):
        prepends = ensure_list(kwargs["prepend"])
        for index, prepend in enumerate(prepends):
            if len(content) is 0 or not isinstance(content[0], dict):
                merged_content.insert(index + 1, prepend)
            else:
                merged_content.insert(index, prepend)
    else if kwargs.has_key("append"):
        appends = ensure_list(kwargs["append"])
        for index, append in enumerate(appends):
            merged_content.append(append)

    return content


def ensure_list(potential_list):
    if not isinstance(potential_list, collections.Iterable) and not isinstance(potential_list, basestring):
            return list(potential_list)
        else:
            return potential_list


# We cheat a bit here - Dynamo uses tag_with_child internally to construct tags,
# all of the tag methods just pass through to it. We use this to abstract
# classed tag generation up a level so we have to write extract_attributes only
# once.
def classed_open_tag(tag, dem_classes, *content, **kwargs):
    return tag_with_child(tag, *extract_attributes(classes(dem_classes), *content, **kwargs))


def classed_closed_tag(tag, dem_classes, *content, **kwargs):
    return tag_with_child(tag, *extract_attributes(classes(dem_classes), *content, **kwargs))


##### Classed-tag convenience functions

def classed_div(dem_classes, *content, **kwargs):
    return classed_open_tag("div", dem_classes, *content, **kwargs)


def classed_ul(dem_classes, *content, **kwargs):
    return classed_open_tag("ul", dem_classes, *content, **kwargs)


def classed_li(dem_classes, *content, **kwargs):
    return classed_open_tag("li", dem_classes, *content, **kwargs)


def classed_button(dem_classes, *content, **kwargs):
    return classed_open_tag("button", dem_classes, *content, **kwargs)


def classed_span(dem_classes, *content, **kwargs):
    return classed_open_tag("span", dem_classes, *content, **kwargs)


def classed_form(dem_classes, *content, **kwargs):
    return classed_open_tag("form", dem_classes, *content, **kwargs)


def classed_input(dem_classes, *content, **kwargs):
    return classed_open_tag("input", dem_classes, *content, **kwargs)


def classed_a(dem_classes, *content, **kwargs):
    return classed_open_tag("a", dem_classes, *content, **kwargs)


def classed_p(dem_classes, *content, **kwargs):
    return classed_open_tag("p", dem_classes, *content, **kwargs)


##### Attribute convenience functions

def classes(dem_classes):
    return {"class": dem_classes}


def untabbable():
    return {"tabindex": "-1"}