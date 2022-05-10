import unittest

from Locators.parameters import Data
from cQube_Dashboard.Energise_Textbook_Usage.usage_textbook.diksha_usage_by_textbook import Diksha_Usage_Textbook_Report
from reuse_func import GetData

'''Script developed to test the each functionalities of web element like buttons , charts , dropdowns , chart 
etc '''


class cQube_Usage_Textbook_Functional_Report(unittest.TestCase):
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

    def test_hyperlink(self):
        b = Diksha_Usage_Textbook_Report(self.driver)
        b.test_hyperlink()
        print('checked with hyper link is working')
        self.data.page_loading(self.driver)

    def test_overalldownload(self):
        b = Diksha_Usage_Textbook_Report(self.driver)
        res = b.download_csv_file()
        self.assertEqual(0, res, msg='Failed due to mismatch found on content plays')
        self.data.page_loading(self.driver)

    def test_test_textbook_based_on_last30days(self):
        b = Diksha_Usage_Textbook_Report(self.driver)
        res = b.test_last30_days()
        self.assertEqual(0, res, msg='mis match found at content usage ')
        self.data.page_loading(self.driver)

    def test_test_textbook_based_on_last7days(self):
        b = Diksha_Usage_Textbook_Report(self.driver)
        res = b.test_last7_days()
        self.assertEqual(0, res, msg='mis match found at content usage ')
        self.data.page_loading(self.driver)

    def test_test_course_based_on_lastday(self):
        b = Diksha_Usage_Textbook_Report(self.driver)
        res = b.test_last_day()
        self.assertEqual(0, res, msg='mis match found at content usage ')
        self.data.page_loading(self.driver)

    def test_Diksha_homeicon(self):
        b = Diksha_Usage_Textbook_Report(self.driver)
        res = b.test_homeicon()
        print("Home icon is working")
        self.data.page_loading(self.driver)

    def test_Diksha_logout(self):
        b = Diksha_Usage_Textbook_Report(self.driver)
        res = b.test_logout()
        self.assertEqual(res, 'Log in to cQube', msg="Logout is not working")
        self.data.page_loading(self.driver)

    def test_download_raw_files_overall_period(self):
        b = Diksha_Usage_Textbook_Report(self.driver)
        res = b.test_overall_rawfile_download()
        self.assertEqual(0, res, msg='Raw file is not downloaded')

    def test_download_raw_files_last_30days_period(self):
        b = Diksha_Usage_Textbook_Report(self.driver)
        res = b.test_last_30_days_rawfile_download()
        self.assertEqual(0, res, msg='Raw file is not downloaded')

    def test_download_raw_files_last_7_day_period(self):
        b = Diksha_Usage_Textbook_Report(self.driver)
        res = b.test_last_7_days_rawfile_download()
        self.assertEqual(0, res, msg='Raw file is not downloaded')

    def test_download_raw_files_lastday_period(self):
        b = Diksha_Usage_Textbook_Report(self.driver)
        res = b.test_last_day_rawfile_download()
        self.assertEqual(0, res, msg='Raw file is not downloaded')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
