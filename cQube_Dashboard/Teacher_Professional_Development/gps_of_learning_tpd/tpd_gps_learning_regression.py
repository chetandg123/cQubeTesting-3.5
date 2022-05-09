import unittest

from cQube_Dashboard.Teacher_Professional_Development.gps_of_learning_tpd.gps_learning_tpd import \
    tpd_content_plays_map_report
from reuse_func import GetData

'''Script developed to test the each functionalities of web element like buttons , charts , dropdowns , map and markers 
etc '''


class gps_learning_tpd_regression(unittest.TestCase):
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
        self.data.navigate_to_gps_of_learning_tpd()
        self.data.page_loading(self.driver)

    def test_navigation_to_report(self):
        fun = tpd_content_plays_map_report(self.driver)
        method = fun.check_navigation_from_dashboard()
        self.assertEqual(0, method, msg='Navigation to report is failed')

    def test_report_home_page(self):
        fun = tpd_content_plays_map_report(self.driver)
        method1 = fun.check_report_home_page()
        self.assertEqual(0, method1, msg='Navigation to report is failed')

    def test_check_choose_type_dropdown(self):
        fun = tpd_content_plays_map_report(self.driver)
        method = fun.check_choose_type_dropdown()
        self.assertNotEqual(0, method, msg='Dropdown options are not present')

    def test_selection_of_options(self):
        fun = tpd_content_plays_map_report(self.driver)
        method = fun.check_selection_of_options()
        self.assertNotEqual(0, method, msg='Dropdown options are not present')

    def test_check_hyperlink_functionality(self):
        fun = tpd_content_plays_map_report(self.driver)
        method = fun.check_hyperlink_functionality()
        self.assertEqual(0, method, msg='hyperlink is not working')

    def test_check_legend_card_functionality(self):
        fun = tpd_content_plays_map_report(self.driver)
        method = fun.check_legend_card_functionality()
        self.assertEqual(0, method, msg='legend card button are not working')

    def test_total_content_plays_legendcard(self):
        fun = tpd_content_plays_map_report(self.driver)
        method = fun.check_total_content_plays_legendcard()
        self.assertEqual(0, method, msg='total content plays legend card button are not working')

    def test_total_time_spent_legendcard(self):
        fun = tpd_content_plays_map_report(self.driver)
        method = fun.check_total_time_spent_legendcard()
        self.assertEqual(0, method, msg='total time spent legend card button are not working')

    def test_check_average_timespent_legendcard(self):
        fun = tpd_content_plays_map_report(self.driver)
        method = fun.check_averaage_timespent_legendcard()
        self.assertEqual(0, method, msg=' average time spent legend cards button are not working ')

    def test_check_logout_from_the_report(self):
        fun = tpd_content_plays_map_report(self.driver)
        method = fun.check_logout_from_the_report()
        self.assertEqual(0, method, msg='Logout button is not working')

    def test_check_total_content_plays_records(self):
        fun = tpd_content_plays_map_report(self.driver)
        method = fun.check_total_content_plays_records()
        self.assertEqual(0, method, msg='Content plays csv file is not downloaded')

    def test_check_total_timespent_plays_records(self):
        fun = tpd_content_plays_map_report(self.driver)
        method = fun.check_total_timespent_plays_records()
        self.assertEqual(0, method, msg='Total Time spent plays csv file is not downloaded')

    def test_check_average_time_records(self):
        fun = tpd_content_plays_map_report(self.driver)
        method = fun.check_average_time_records()
        self.assertEqual(0, method, msg='Average Time spent plays csv file is not downloaded')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
