from zwitscher_maschine import *
sys.path.append("components")
from alerts import *

print basic_template(
    long_success_alert("Dude!", {"class": "your_mom"}, "Watch out, man, you're gonna be in trouble."),
)