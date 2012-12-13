from zwitscher_maschine import *
sys.path.append("components")
from alerts import *

print basic_template(
    success_alert("Wat", "Nowai")
)