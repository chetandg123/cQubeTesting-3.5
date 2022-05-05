import unittest

from Locators.parameters import Data
from cQube_Dashboard.Energise_Textbook_Usage.usage_textbook.diksha_usage_by_textbook import diksha_usage_textbook_report
from reuse_func import GetData


class cQube_usage_textbook_system_report(unittest.TestCase):
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
        self.data.navigate_to_column_textbook()
        self.data.page_loading(self.driver)

    def test_navigation_from_hamburger(self):
        count = 0
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.data.page_loading(self.driver)
        self.data.page_loading(self.driver)
        self.data.navigate_to_column_textbook()
        self.data.page_loading(self.driver)
        if 'usage-by-textbook' in self.driver.current_url:
            print('Home button is working')
        else:
            print("Home button is not working ")
            count = count + 1
        self.assertEqual(0, count, msg="Navigatation to diksha couse report is failed ")
        self.data.page_loading(self.driver)

    def test_overalldownload(self):
        b = diksha_usage_textbook_report(self.driver)
        res = b.download_csv_file()
        self.assertEqual(0, res, msg='Failed due to mismatch found on content plays')
        self.data.page_loading(self.driver)

    def test_test_course_based_on_last30days(self):
        b = diksha_usage_textbook_report(self.driver)
        res = b.test_last30_days()
        self.assertEqual(0, res, msg='mis match found at content usage ')
        self.data.page_loading(self.driver)

    def test_test_course_based_on_last7days(self):
        b = diksha_usage_textbook_report(self.driver)
        res = b.test_last7_days()
        self.assertEqual(0, res, msg='mis match found at content usage ')
        self.data.page_loading(self.driver)

    def test_test_course_based_on_lastday(self):
        b = diksha_usage_textbook_report(self.driver)
        res = b.test_last_day()
        self.assertEqual(0, res, msg='mis match found at content usage ')
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
