import unittest

from cQube_Dashboard.Energise_Textbook_Usage.etb_heartbeat_nation.heart_beat_nation_learning import \
    Etb_Nation_Learning_Report
from reuse_func import GetData

'''Script developed to test the each functionalities of web element like buttons , charts , dropdowns , chart 
etc '''


class Etb_Nation_Learning_Regression(unittest.TestCase):
    driver = None
    data = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)
        self.data.navigate_to_etb_nation_learning_report()
        self.data.page_loading(self.driver)

    def test_navigation_to_nation_learning_report(self):
        fun = Etb_Nation_Learning_Report(self.driver)
        method = fun.check_navigation_to_nation_learning_report()
        self.assertEqual(0, method, msg='Navigation to Report is failed')

    def test_hyperlink_functionality(self):
        fun = Etb_Nation_Learning_Report(self.driver)
        method = fun.check_hyperlink_functionality()
        self.assertEqual(0, method, msg='Hyperlink is not working ')

    def test_dropdown_options_presence(self):
        fun = Etb_Nation_Learning_Report(self.driver)
        method = fun.check_dropdown_options()
        self.assertNotEqual(0, method, msg='Dropdown is not having options ')

    def test_dropdown_options_selection(self):
        fun = Etb_Nation_Learning_Report(self.driver)
        method = fun.check_selection_of_options()
        self.assertNotEqual(0, method, msg='Dropdown is not having options ')

    def test_dowload_button_on_each_districtwise_selection(self):
        fun = Etb_Nation_Learning_Report(self.driver)
        method = fun.check_download_functionality_each_districtwise()
        self.assertEqual(0, method, msg='Some District wise csv file is not downloaded')

    def test_dowload_button_on_state_level(self):
        fun = Etb_Nation_Learning_Report(self.driver)
        method = fun.check_download_functionality_statewise()
        self.assertEqual(0, method, msg='State level csv file is not downloaded')

    def test_check_logout_from_report(self):
        fun = Etb_Nation_Learning_Report(self.driver)
        method = fun.check_logout_from_report()
        self.assertEqual(0, method, msg='Logout is not working ')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
