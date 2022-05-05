import unittest

from cQube_Dashboard.Energise_Textbook_Usage.etb_usage_per_capita.usage_per_capita_report import usage_per_capita_map
from reuse_func import GetData


class user_capita_regression(unittest.TestCase):
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
        self.data.navigate_to_etb_usage_per_capita_report()
        self.data.page_loading(self.driver)

    def test_navigation_to_report(self):
        fun = usage_per_capita_map(self.driver)
        method = fun.check_navigation_from_dashboard()
        self.assertEqual(0, method, msg='Usage per capita report icon is not working')

    def test_cQube_logo_to_capita_report(self):
        fun = usage_per_capita_map(self.driver)
        method1, method2 = fun.check_report_home_page()
        self.assertEqual(0, method1, msg='cQube logo is not working ')
        self.assertNotEqual(method2, 0, msg="markers are not present")

    # def test_the_dropdown_options(self):
    #     fun = usage_per_capita_map(self.driver)
    #     method = fun.check_choose_type_dropdown()
    #     self.assertNotEqual(0,method, msg='Dropdown is not having options')

    # def test_the_select_each_options(self):
    #     fun = usage_per_capita_map(self.driver)
    #     method = fun.check_selection_of_options()
    #     self.assertNotEqual(0,method, msg='Dropdown is not having options')

    def test_the_hyperlink_functionality(self):
        fun = usage_per_capita_map(self.driver)
        method = fun.check_hyperlink_functionality()

    def test_legend_card_functionality(self):
        fun = usage_per_capita_map(self.driver)
        method = fun.check_legend_card_functionality()
        self.assertEqual(0, method, msg='legend button is not working')

    def test_logout_button_functionality(self):
        fun = usage_per_capita_map(self.driver)
        method = fun.check_logout_from_the_report()
        self.assertEqual(0, method, msg='Logout button is not working')

    def test_click_on_upper_quartile(self):
        fun = usage_per_capita_map(self.driver)
        method = fun.check_with_upper_quartile_functionality()
        self.assertEqual(0, method, msg='upper quartile button and markers color is not matched')

    def test_click_on_inter_quartile(self):
        fun = usage_per_capita_map(self.driver)
        method = fun.check_with_inter_quartile_functionality()
        self.assertEqual(0, method, msg='Inter quartile button and markers color is not matched')

    def test_click_on_bottom_quartile(self):
        fun = usage_per_capita_map(self.driver)
        method = fun.check_with_bottom_quartile_functionality()
        self.assertEqual(0, method, msg='Bottom quartile button and markers color is not matched')

    def test_click_on_upper_quartile_download_csv(self):
        fun = usage_per_capita_map(self.driver)
        method = fun.check_download_functionality_with_upper_quartile()
        self.assertEqual(0, method, msg='upper quartile button and download button is not working')

    def test_click_on_inter_quartile_download_csv(self):
        fun = usage_per_capita_map(self.driver)
        method = fun.check_download_functionality_with_inter_quartile()
        self.assertEqual(0, method, msg='Inter quartile button and download button is not working')

    def test_click_on_bottom_quartile_download_csv(self):
        fun = usage_per_capita_map(self.driver)
        method = fun.check_download_functionality_with_bottom_quartile()
        self.assertEqual(0, method, msg='Bottom quartile button and download button is not working')

    def test_overall_per_capita_download(self):
        fun = usage_per_capita_map(self.driver)
        method = fun.check_download_functionality_per_capita_over_quartile()
        self.assertEqual(0, method, msg='Download button is not working ')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
