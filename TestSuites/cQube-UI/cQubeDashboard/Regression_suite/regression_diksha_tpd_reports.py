import time
import unittest

from cQube_Dashboard.Energise_Textbook_Usage.content_textbook import content_textbook_regression_suite
from cQube_Dashboard.Energise_Textbook_Usage.etb_heartbeat_nation import etb_nation_learning_regression
from cQube_Dashboard.Energise_Textbook_Usage.etb_usage_per_capita import user_per_capita_regression
from cQube_Dashboard.Energise_Textbook_Usage.gps_of_learning_etb import etb_gps_learning_regression
from cQube_Dashboard.Energise_Textbook_Usage.usage_textbook import usage_by_textbook_regression_suite
from cQube_Dashboard.Teacher_Professional_Development.content_course import content_course_regression_suite
from cQube_Dashboard.Teacher_Professional_Development.gps_of_learning_tpd import tpd_gps_learning_regression
from cQube_Dashboard.Teacher_Professional_Development.tpd_completion import completion_regression_test
from cQube_Dashboard.Teacher_Professional_Development.tpd_content_preference import content_preference_regression_suite
from cQube_Dashboard.Teacher_Professional_Development.tpd_course_progress import tpd_course_regression_test
from cQube_Dashboard.Teacher_Professional_Development.tpd_user_engagement import user_engagement_report_regression
from cQube_Dashboard.Teacher_Professional_Development.tpd_user_on_boarding import user_on_boarding_line_regression
from cQube_Dashboard.Teacher_Professional_Development.tpd_user_progress import enrollment_regression_test
from cQube_Dashboard.Teacher_Professional_Development.usage_course import usage_by_course_regression_suite
from get_dir import pwd

from reuse_func import GetData
from HTMLTestRunner import HTMLTestRunner


class MyTestSuite_Diksha_tpds(unittest.TestCase):
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

    def test_issue01(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_ETB")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_diksha_content_course()
            if 'No data found' in self.driver.page_source:
                print('Diksha Content Course Report is showing no data found!..')
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        content_course_regression_suite.cQube_Content_Course_Regression)
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "w")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Content BY Course Regression Test Report',
                    verbosity=1, )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue02(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_ETB")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_diksha_content_textbook()
            if 'No data found' in self.driver.page_source:
                print('Diksha Content Textbook Report is showing no data found!..')
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        content_textbook_regression_suite.cQube_Content_Textbook_Regression
                    )
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Content By Textbook report Regression Test Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue03(self):
        self.data = GetData()
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_ETB")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_column_course()
            time.sleep(3)
            if 'No data found' in self.driver.page_source:
                print('Diksha usage by course Report is showing no data found!..')
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        usage_by_course_regression_suite.cQube_Diskha_Course_Regression_Report
                    )
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title=' Usage By Course Report Regression Test Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue04(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_ETB")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_column_textbook()
            if 'No data found' in self.driver.page_source:
                print('Diksha usage by textbook Report is showing no data found!..')
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        usage_by_textbook_regression_suite.cQube_Usage_Textbook_Regression_Report
                    )
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title=' Usage By Textbook Report Regression Test Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue05(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_TPD")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_tpd_content_progress()
            if 'No data found' in self.driver.page_source:
                print('TPD Course Progress Report is showing no data found!..')
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        tpd_course_regression_test.cQube_Tpd_Content_Regression_Test
                    )
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='TPD course Progress Regression Test Report',
                    verbosity=1, )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue07(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_TPD")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_tpd_enrollment_report()
            if 'No data found' in self.driver.page_source:
                print('TPD User Progres Report is showing no data found!..')
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        enrollment_regression_test.cQube_Enrollment_Regression
                    )])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='TPD Enrollment Regression Test Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue08(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_TPD")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_tpd_completion_percentage()
            if 'No data found' in self.driver.page_source:
                print('TPD Completion Report is showing no data found!..')
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        completion_regression_test.cQube_Completion_Percentage_Regression
                    )])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='TPD Completion percentage Regression Test Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    # New Reports

    def test_issue_09(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_TPD")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_tpd_content_usage_piechart_report()
            if 'No data found' in self.driver.page_source:
                print('TPD Content Preference Report is showing no data found!..')
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        content_preference_regression_suite.Preference_Report_Regression_Suite
                    )])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='TPD Content Preference Report Regression Test Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue_10(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_TPD")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_tpd_enrollment_report()
            if 'No data found' in self.driver.page_source:
                print('TPD GPS Learning Report is showing no data found!..')
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        tpd_gps_learning_regression.gps_learning_tpd_regression
                    )])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='TPD GPS Learning  Report Regression Test Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue_11(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_TPD")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_tpd_user_engagement_report()
            if 'No data found' in self.driver.page_source:
                print('TPD User Engagement Report is showing no data found!..')
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        user_engagement_report_regression.User_Engagement_Regression
                    )])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='TPD User Engagement Report Regression Test Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue_12(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_TPD")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_tpd_user_on_boarding_report()
            if 'No data found' in self.driver.page_source:
                print('TPD User on boarding Report is showing no data found!..')
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        user_on_boarding_line_regression.User_On_Boarding_Line_Chart_Regression
                    )])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='TPD on boarding Report Regression Test Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue_13(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_ETB")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_etb_content_plays_report()
            if 'No data found' in self.driver.page_source:
                print('ETB GPS Learning Report is showing no data found!..')
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        etb_gps_learning_regression.Etb_Gps_Learning_Regression
                    )])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='ETB GPS Learning Report Regression Test Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue_14(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_ETB")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_etb_content_plays_report()
            if 'No data found' in self.driver.page_source:
                print('ETB GPS Learning Report is showing no data found!..')
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        etb_gps_learning_regression.Etb_Gps_Learning_Regression
                    )])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='ETB GPS Learning Report Regression Test Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue_15(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_ETB")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_etb_usage_per_capita_report()
            if 'No data found' in self.driver.page_source:
                print('ETB User Per Capita Report is showing no data found!..')
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        user_per_capita_regression.User_Capita_Regression
                    )])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='ETB User Per Capita Report Regression Test Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue_16(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_ETB")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_etb_nation_learning_report()
            if 'No data found' in self.driver.page_source:
                print('ETB Heart Beat Nation Report is showing no data found!..')
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        etb_nation_learning_regression.Etb_Nation_Learning_Regression
                    )])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='ETB Heart Beat Nation Report Regression Test Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    @classmethod
    def tearDownClass(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
