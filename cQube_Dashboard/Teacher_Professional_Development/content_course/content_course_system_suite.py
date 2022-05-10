import unittest

from cQube_Dashboard.Teacher_Professional_Development.content_course.diksha_content_course import Content_Course_Report
from reuse_func import GetData

'''Script developed to test the each functionalities of web element like buttons , charts , dropdowns , search box 
etc '''


class cQube_content_course_system_suite(unittest.TestCase):
    driver = None
    data = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_diksha_content_course()
        self.data.page_loading(self.driver)

    def test_diksha_page(self):
        b = Content_Course_Report(self.driver)
        res = b.test_navigation()
        self.assertEqual(res, 0, msg='content course page is present but url is not matching to report')
        self.data.page_loading(self.driver)

    def test_course_districtwise_records(self):
        b = Content_Course_Report(self.driver)
        res = b.test_alldata_districts()
        self.assertEqual(0, res, msg='Records are not present on table ')
        self.data.page_loading(self.driver)

    def test_Districtwise_lastday_records(self):
        b = Content_Course_Report(self.driver)
        res = b.test_districts()
        self.assertEqual(res, 0, msg='Some districts does not have table records')
        self.data.page_loading(self.driver)

    def test_Districtwise_lastweek_records(self):
        b = Content_Course_Report(self.driver)
        res = b.test_districts()
        self.assertEqual(res, 0, msg='Some districts does not have table records')
        self.data.page_loading(self.driver)

    def test_Districtwise_monthwise_records(self):
        b = Content_Course_Report(self.driver)
        res = b.test_districts()
        self.assertEqual(res, 0, msg='Some districts does not have table records')
        self.data.page_loading(self.driver)

    def test_Table_orderwise(self):
        b = Content_Course_Report(self.driver)
        res = b.test_tablevalue()
        print("checking order of the table and working as per requirement ")
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
