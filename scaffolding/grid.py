from ..dynamo import *
from ..components.common import *

ROW = "row"
SPAN = "span"

def grid_row(*content):
    return classed_div(ROW, *content)

def column_span(cols, *content):
    return classed_div(SPAN + cols, *content)