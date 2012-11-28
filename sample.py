from zwitscher_maschine import *
sys.path.append("components")
from alerts import *
from breadcrumbs import *
from button_dropdowns import *
from button_groups import *
from dropdowns import *
from labels_badges import *
from media import *
from misc import *
from nav import *
from navbar import *
from pagination import *
from progress import *
from thumbnails import *
from typography import *

print basic_template(
    h1("Testing Alerts"),
    p("I'm testing out an alert system, let's see if it works!"),
    alert("This is a Random Title", "This is a random message."),
    long_alert("This is a Random Title", "This is a random message."),
    success_alert("This is a Random Title", "This is a random message."),
    long_success_alert("This is a Random Title", "This is a random message."),
    error_alert("This is a Random Title", "This is a random message."),
    long_error_alert("This is a Random Title", "This is a random message."),
    info_alert("This is a Random Title", "This is a random message."),
    long_info_alert("This is a Random Title", "This is a random message.")
)