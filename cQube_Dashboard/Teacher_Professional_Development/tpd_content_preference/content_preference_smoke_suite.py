import unittest

from cQube_Dashboard.Teacher_Professional_Development.tpd_content_preference.tpd_content_preference_scripts import \
    tpd_content_usage_piechart
from reuse_func import GetData

'''Script developed to test the each functionalities of web element like buttons , charts , dropdowns , chart 
etc '''


class preference_report_smoke_suite(unittest.TestCase):
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
        self.data.navigate_to_tpd_content_usage_piechart_report()

    def test_navigation_to_content_preference_report(self):
        fun = tpd_content_usage_piechart(self.driver)
        method = fun.check_navigation_to_content_usage_report()
        self.assertEqual(method, 0, msg='Navigation is failed ')

    def test_hyperlink_functionality(self):
        fun = tpd_content_usage_piechart(self.driver)
        method = fun.check_hyperlink_functionality()
        self.assertEqual(0, method, msg='Hyperlink is not working ')

    def test_check_dropdown_options(self):
        fun = tpd_content_usage_piechart(self.driver)
        method = fun.check_dropdown_options()
        self.assertNotEqual(0, method, msg='Dropdown options are not present')

    def test_check_selection_of_options(self):
        fun = tpd_content_usage_piechart(self.driver)
        method = fun.check_selection_of_options()
        self.assertNotEqual(0, method, msg='selection options are not present')

    def test_check_logout_to_report(self):
        fun = tpd_content_usage_piechart(self.driver)
        method = fun.check_logout_to_report()
        self.assertEqual(0, method, msg='Logout is not working ')

    def test_download_statewise_with_contentplays(self):
        fun = tpd_content_usage_piechart(self.driver)
        method = fun.check_download_statewise_with_contentplays()
        self.assertEqual(0, method, msg='State wise pie chart is not correct ')

    def test_check_download_state_with_districts_content_plays(self):
        fun = tpd_content_usage_piechart(self.driver)
        method = fun.check_download_state_with_districts_content_plays()
        self.assertEqual(0, method, msg='State wise pie chart is not correct ')

    # def test_download_state_with_random_district_content_plays(self):
    #     fun = tpd_content_usage_piechart(self.driver)
    #     method = fun.check_download_state_with_random_district_content_plays()
    #     self.assertEqual(0,method,msg='State wise pie chart is not correct ')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
