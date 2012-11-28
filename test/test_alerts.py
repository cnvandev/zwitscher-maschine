import sys
sys.path.append("../components")
from alerts import alert, success_alert, error_alert, info_alert, long_alert, long_success_alert, long_error_alert, long_info_alert
import unittest

class TestAlerts(unittest.TestCase):

    def setUp(self):
        self.title = "This is a Random Title"
        self.message = "This is a random message for you to read. Aren't you happy?"

        self.alert = '''<div class="alert">\n\t<button data-dismiss="alert" type="button" class="close">x</button>\n\t<h4>%s</h4>\n\t%s\n</div>''' % (self.title, self.message)
        self.long_alert = '''<div class="alert">\n\t<button data-dismiss="alert" type="button" class="close">x</button>\n\t<strong>%s</strong>\n\t%s\n</div>''' % (self.title, self.message)

        self.success_alert = '''<div class="alert alert-success">\n\t<button data-dismiss="alert alert-success" type="button" class="close">x</button>\n\t<h4>%s</h4>\n\t%s\n</div>''' % (self.title, self.message)
        self.long_success_alert = '''<div class="alert alert-success">\n\t<button data-dismiss="alert alert-success" type="button" class="close">x</button>\n\t<strong>%s</strong>\n\t%s\n</div>''' % (self.title, self.message)

        self.error_alert = '''<div class="alert alert-error">\n\t<button data-dismiss="alert alert-error" type="button" class="close">x</button>\n\t<h4>%s</h4>\n\t%s\n</div>''' % (self.title, self.message)
        self.long_error_alert = '''<div class="alert alert-error">\n\t<button data-dismiss="alert alert-error" type="button" class="close">x</button>\n\t<strong>%s</strong>\n\t%s\n</div>''' % (self.title, self.message)

        self.info_alert = '''<div class="alert alert-info">\n\t<button data-dismiss="alert alert-info" type="button" class="close">x</button>\n\t<h4>%s</h4>\n\t%s\n</div>''' % (self.title, self.message)
        self.long_info_alert = '''<div class="alert alert-info">\n\t<button data-dismiss="alert alert-info" type="button" class="close">x</button>\n\t<strong>%s</strong>\n\t%s\n</div>''' % (self.title, self.message)

    def test_alerts(self):
        self.assertEqual(alert(self.title, self.message), self.alert)
        self.assertEqual(success_alert(self.title, self.message), self.success_alert)
        self.assertEqual(error_alert(self.title, self.message), self.error_alert)
        self.assertEqual(info_alert(self.title, self.message), self.info_alert)

    def test_long_alerts(self):
        self.assertEqual(long_alert(self.title, self.message), self.long_alert)
        self.assertEqual(long_success_alert(self.title, self.message), self.long_success_alert)
        self.assertEqual(long_error_alert(self.title, self.message), self.long_error_alert)
        self.assertEqual(long_info_alert(self.title, self.message), self.long_info_alert)

if __name__ == '__main__':
    unittest.main()