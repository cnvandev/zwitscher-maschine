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