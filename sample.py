from zwitscher_maschine import *
sys.path.append("components")
from breadcrumbs import *

print basic_template(
    breadcrumbs(crumb(a({"href": "#"}, "One")), divider(), crumb(a({"href": "#"}, "Two")), divider(), crumb(a({"href": "#"}, "Three")))
)