import unittest

from cQube_Dashboard.Dashboard_Icons.cQube_icons import cQubeLandingPage
from reuse_func import GetData

'''Script to validate the cQube Dashboard icon functionalities and check whether each icon navigating to their 
respective reports or not '''


class cQube_Home(unittest.TestCase):
    driver = None
    data = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(30)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)

    def test_sar_icon(self):
        b = cQubeLandingPage(self.driver)
        result = b.test_SAR()
        self.data.page_loading(self.driver)

    def test_crc_icon(self):
        b = cQubeLandingPage(self.driver)
        result = b.test_crc_visit_report()
        self.assertEqual(0, result, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_semester_icon(self):
        b = cQubeLandingPage(self.driver)
        result = b.test_Semester_map()
        self.assertEqual(0, result, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_semester_heatchart_icon(self):
        b = cQubeLandingPage(self.driver)
        result = b.test_Semester_heatchart()
        self.assertEqual(0, result, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_tar_icon(self):
        b = cQubeLandingPage(self.driver)
        result = b.test_TAR()
        self.assertEqual(0, result, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_school_map_icon(self):
        b = cQubeLandingPage(self.driver)
        result = b.test_school_infrastructure_map()
        self.data.page_loading(self.driver)

    #
    def test_school_chart_icon(self):
        b = cQubeLandingPage(self.driver)
        result = b.test_composite_chart_map()
        self.assertEqual(0, result, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_sem_exception(self):
        b = cQubeLandingPage(self.driver)
        res = b.check_semester_Exception_report_icon()
        self.assertEqual(0, res, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_telemetry_icon(self):
        b = cQubeLandingPage(self.driver)
        result = b.check_telemetry_icon()
        self.assertEqual(0, result, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_completionerror(self):
        b = cQubeLandingPage(self.driver)
        res = b.check_isdata_exception_list()
        self.assertEqual(0, res, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_composite_metrics_Report(self):
        b = cQubeLandingPage(self.driver)
        res = b.check_composite_metrics()
        self.assertEqual(0, res, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_patreport(self):
        b = cQubeLandingPage(self.driver)
        res = b.test_periodic_map_report()
        self.assertEqual(0, res, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_pat_heatchart_report(self):
        b = cQubeLandingPage(self.driver)
        res = b.test_periodic_heatchart_report()
        self.assertEqual(0, res, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_pat_lo_report(self):
        b = cQubeLandingPage(self.driver)
        res = b.test_periodic_lo_report()
        self.assertEqual(0, res, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_udisereport(self):
        b = cQubeLandingPage(self.driver)
        res = b.test_udise_report()
        self.assertEqual(0, res, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_diksha_usage_by_course(self):
        b = cQubeLandingPage(self.driver)
        res = b.check_usage_by_course()
        self.assertEqual(0, res, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_diksha_usage_by_course_content(self):
        b = cQubeLandingPage(self.driver)
        res = b.check_usage_by_content_course()
        self.assertEqual(0, res, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_etb_usage_by_textbook(self):
        b = cQubeLandingPage(self.driver)
        res = b.check_usage_by_textbook()
        self.assertEqual(0, res, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_etb_usage_by_textbook_content(self):
        b = cQubeLandingPage(self.driver)
        res = b.check_usage_by_content_textbook()
        self.assertEqual(0, res, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_diksha_enrollment(self):
        b = cQubeLandingPage(self.driver)
        res = b.check_enrollment_report()
        self.assertEqual(0, res, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    # def test_diksha_completion(self):
    #     b = cQubeLandingPage(self.driver)
    #     res = b.check_tpd_completion_report()
    #     self.assertEqual(0, res, msg='Report page is not exist')
    #     self.data.page_loading(self.driver)

    def test_diksha_course_progress(self):
        b = cQubeLandingPage(self.driver)
        res = b.check_course_progress()
        self.assertEqual(0, res, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
