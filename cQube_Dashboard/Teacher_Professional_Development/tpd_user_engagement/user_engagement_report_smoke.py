import unittest

from cQube_Dashboard.Teacher_Professional_Development.tpd_user_engagement.user_engagement_scripts import \
    User_Engagement_Automation_Scripts
from reuse_func import GetData

'''Script developed to test the each functionalities of web element like buttons , charts , dropdowns , chart 
etc '''


class User_Engagement_Smoke(unittest.TestCase):
    data = None
    driver = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)
        self.data.navigate_to_tpd_user_engagement_report()
        self.data.page_loading(self.driver)

    def test_navigation_to_user_engagement(self):
        fun = User_Engagement_Automation_Scripts(self.driver)
        method = fun.check_hyperlink_functionality()
        self.assertEqual(0, method, msg="Navigation to user engagement is failed")

    def test_check_hyperlink_functionality(self):
        fun = User_Engagement_Automation_Scripts(self.driver)
        method = fun.check_hyperlink_functionality()
        self.assertEqual(0, method, msg="hyperlink is not working")

    def test_check_dropdown_options(self):
        fun = User_Engagement_Automation_Scripts(self.driver)
        method = fun.check_dropdown_options()
        self.assertNotEqual(0, method, msg="Dropdown options are not present")

    def test_check_selection_of_options(self):
        fun = User_Engagement_Automation_Scripts(self.driver)
        method = fun.check_selection_of_options()
        self.assertNotEqual(0, method, msg="Selection of dropdown options")

    def test_check_download_functionality_each_districtwise(self):
        fun = User_Engagement_Automation_Scripts(self.driver)
        method = fun.check_download_functionality_each_districtwise()
        self.assertEqual(0, method, msg="District wise csv file is not downloaded")

    def test_check_download_functionality_statewise(self):
        fun = User_Engagement_Automation_Scripts(self.driver)
        method = fun.check_download_functionality_statewise()
        self.assertEqual(0, method, msg="State level csv file is not downloaded")

    def test_logout_button_functionality(self):
        fun = User_Engagement_Automation_Scripts(self.driver)
        method = fun.check_logout_from_report()
        self.assertEqual(0, method, msg="logout button is not working ")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
