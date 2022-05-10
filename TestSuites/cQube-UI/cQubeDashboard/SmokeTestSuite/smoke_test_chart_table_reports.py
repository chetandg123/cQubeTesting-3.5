import unittest

from cQube_Dashboard.CRC_Visit import crc_report_smoke_testing
from cQube_Dashboard.Composite_Report_across_metrics import composite_smoke_testing
from cQube_Dashboard.Energise_Textbook_Usage.content_textbook import content_textbook_smoke_suite
from cQube_Dashboard.Energise_Textbook_Usage.etb_heartbeat_nation import etb_nation_learning_smoke
from cQube_Dashboard.Energise_Textbook_Usage.etb_usage_per_capita import user_per_capita_smoke
from cQube_Dashboard.Energise_Textbook_Usage.gps_of_learning_etb import etb_gps_learning_smoke
from cQube_Dashboard.Energise_Textbook_Usage.usage_textbook import usage_by_textbook_smoke_suite
from cQube_Dashboard.School_Infrastructure.composite_report import School_report_smoke_testing
from cQube_Dashboard.Student_Performance.pat_heatchart import patheatchart_smoke_test
from cQube_Dashboard.Student_Performance.pat_lotable import PAT_LO_Table_smoke_suite
from cQube_Dashboard.Teacher_Professional_Development.content_course import content_course_smoke_testing
from cQube_Dashboard.Teacher_Professional_Development.gps_of_learning_tpd import tpd_gps_learning_smoke
from cQube_Dashboard.Teacher_Professional_Development.tpd_completion import completion_smoke_test
from cQube_Dashboard.Teacher_Professional_Development.tpd_content_preference import content_preference_smoke_suite
from cQube_Dashboard.Teacher_Professional_Development.tpd_course_progress import tpd_course_smoke_test
from cQube_Dashboard.Teacher_Professional_Development.tpd_user_engagement import user_engagement_report_smoke
from cQube_Dashboard.Teacher_Professional_Development.tpd_user_on_boarding import user_on_boarding_line_smoke
from cQube_Dashboard.Teacher_Professional_Development.tpd_teacher_percentage import lpd_percentage_smoke_test
from cQube_Dashboard.Teacher_Professional_Development.usage_course import usage_by_course_smoke_testing
from get_dir import pwd
from reuse_func import GetData
from HTMLTestRunner import HTMLTestRunner


class MyTestSuite_smoke_chart_tables(unittest.TestCase):
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
        self.data.navigate_to_heatchart_report()
        if 'No data found' in self.driver.page_source:
            print(' PAT Heat chart Report is showing no data found!..')
            self.driver.close()
        else:
            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    patheatchart_smoke_test.cQube_heatchart_Smoke_test
                )
            ])
            p = pwd()
            outfile = open(p.get_smoke_chart_tables_report(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=' PAT Heat chart  Report Smoke Test  Report',
                verbosity=1,

            )
            runner1.run(smoke_test)
            outfile.close()

    def test_issue02(self):
        self.data.page_loading(self.driver)
        self.data.navigate_to_lo_table_report()
        if 'No data found' in self.driver.page_source:
            print(' PAT LO Table Report is showing no data found!..')
            self.driver.close()
        else:
            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    PAT_LO_Table_smoke_suite.cQube_Pat_LoTable_Smoke_Test
                )
            ])
            p = pwd()
            outfile = open(p.get_smoke_chart_tables_report(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=' PAT LO Table  Report Smoke Test  Report',
                verbosity=1,

            )
            runner1.run(smoke_test)
            outfile.close()

    def test_issue03(self):
        self.data.page_loading(self.driver)
        self.data.navigate_to_diksha_content_course()
        if 'No data found' in self.driver.page_source:
            print('Diksha Content Course Report is showing no data found!..')
            self.driver.close()
        else:
            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    content_course_smoke_testing.cQube_Content_Course_Smoke)
            ])
            p = pwd()
            outfile = open(p.get_smoke_chart_tables_report(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Content BY Course Smoke Test  Report',
                verbosity=1,

            )
            runner1.run(smoke_test)
            outfile.close()

    def test_issue04(self):
        self.data.page_loading(self.driver)
        self.data.navigate_to_diksha_content_textbook()
        if 'No data found' in self.driver.page_source:
            print('Diksha Content Textbook Report is showing no data found!..')
            self.driver.close()
        else:
            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    content_textbook_smoke_suite.cQube_Content_Textbook_Smoke
                )
            ])
            p = pwd()
            outfile = open(p.get_smoke_chart_tables_report(), "a")
            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Content By Textbook report Smoke Test  Report',
                verbosity=1, )
            runner1.run(smoke_test)
            outfile.close()

    def test_issue05(self):
        self.data.page_loading(self.driver)
        self.data.navigate_to_column_course()
        if 'No data found' in self.driver.page_source:
            print('Diksha usage by course Report is showing no data found!..')
            self.driver.close()
        else:
            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    usage_by_course_smoke_testing.cQube_Diskha_Course_Smoke_Test
                )
            ])
            p = pwd()
            outfile = open(p.get_smoke_chart_tables_report(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=' Usage By Course Smoke Test  Report',
                verbosity=1,

            )
            runner1.run(smoke_test)
            outfile.close()

    def test_issue06(self):
        self.data.page_loading(self.driver)
        self.data.navigate_to_column_textbook()
        if 'No data found' in self.driver.page_source:
            print('Diksha usage by textbook Report is showing no data found!..')
            self.driver.close()
        else:
            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    usage_by_textbook_smoke_suite.cQube_Usage_Textbook_Smoke_Report
                )
            ])
            p = pwd()
            outfile = open(p.get_smoke_chart_tables_report(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=' Usage By Textbook  Smoke Test  Report',
                verbosity=1,

            )
            runner1.run(smoke_test)
            outfile.close()

    def test_issue07(self):
        self.data.page_loading(self.driver)
        self.data.navigate_to_tpd_content_progress()
        if 'No data found' in self.driver.page_source:
            print('TPD Course Progress Report is showing no data found!..')
            self.driver.close()
        else:
            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    tpd_course_smoke_test.cQube_TpdContent_Smoke_Test
                )
            ])
            p = pwd()
            outfile = open(p.get_smoke_chart_tables_report(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=' TPD Course Progress  Smoke Test  Report',
                verbosity=1,

            )
            runner1.run(smoke_test)
            outfile.close()

    def test_issue08(self):
        self.data.page_loading(self.driver)
        self.data.navigate_to_tpd_percentage_progress()
        if 'No data found' in self.driver.page_source:
            print('TPD Course Percentage Report is showing no data found!..')
            self.driver.close()
        else:
            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    lpd_percentage_smoke_test.cQube_Tpd_Percentage_Smoke_Test
                )
            ])
            p = pwd()
            outfile = open(p.get_smoke_chart_tables_report(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=' TPD Percentage Progress  Smoke Test  Report',
                verbosity=1,

            )
            runner1.run(smoke_test)
            outfile.close()

    def test_issue10(self):
        p = pwd()
        self.data.page_loading(self.driver)
        self.data.navigate_to_tpd_completion_percentage()
        if 'No data found' in self.driver.page_source:
            print('TPD Completion Report is showing no data found!..')
            self.driver.close()
        else:
            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    completion_smoke_test.cQube_Completion_Percentage_Smoke)])
            outfile = open(p.get_smoke_chart_tables_report(), "a")
            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='TPD Completion Percentage Smoke Test  Report',
                verbosity=1, )
            runner1.run(smoke_test)
            outfile.close()

    def test_issue13(self):
        self.data.page_loading(self.driver)
        self.data.navigate_to_crc_report()
        if 'No data found' in self.driver.page_source:
            print('CRC Report is showing no data found!..')
            self.driver.close()
        else:
            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                # file name .class name
                unittest.defaultTestLoader.loadTestsFromTestCase(crc_report_smoke_testing.cQube_CRC_Report)])
            p = pwd()
            outfile = open(p.get_smoke_chart_tables_report(), "a")
            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Crc Test  Report',
                verbosity=1, )
            runner1.run(smoke_test)
            outfile.close()

    def test_issue14(self):
        self.data.page_loading(self.driver)
        self.data.navigate_to_composite_infrastructure()
        if 'No data found' in self.driver.page_source:
            print('School infrastructure Report is showing no data found!..')
            self.driver.close()
        else:
            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(School_report_smoke_testing.cQube_SI_Report)
            ])
            p = pwd()
            outfile = open(p.get_smoke_chart_tables_report(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='School Infrastructure Smoke Test Report',
                verbosity=1,
            )
            runner1.run(smoke_test)
            outfile.close()

    def test_issue15(self):
        self.data.page_loading(self.driver)
        self.data.navigate_to_composite_report()
        if 'No data found' in self.driver.page_source:
            print('Composite Accross metrics Report is showing no data found!..')
            self.driver.close()
        else:
            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    composite_smoke_testing.composite_smoke_testing)
            ])
            p = pwd()
            outfile = open(p.get_smoke_chart_tables_report(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Composite Report smoke Test  Report',
                verbosity=1,
            )
            runner1.run(smoke_test)
            outfile.close()

    def test_issue_16(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_TPD")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_tpd_content_usage_piechart_report()
            if 'No data found' in self.driver.page_source:
                print('TPD Content Preference Report is showing no data found!..')
            else:
                smoke_test = unittest.TestSuite()
                smoke_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        content_preference_smoke_suite.Preference_Report_Smoke_Suite
                    )])
                p = pwd()
                outfile = open(p.get_smoke_chart_tables_report(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='TPD Content Preference Report Smoke Test Report',
                    verbosity=1,
                )
                runner1.run(smoke_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue_17(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_TPD")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_gps_of_learning_tpd()
            if 'No data found' in self.driver.page_source:
                print('TPD GPS Learning Report is showing no data found!..')
            else:
                smoke_test = unittest.TestSuite()
                smoke_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        tpd_gps_learning_smoke.gps_learning_tpd_smoke_suite
                    )])
                p = pwd()
                outfile = open(p.get_smoke_chart_tables_report(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='TPD GPS Learning Report Smoke Test Report',
                    verbosity=1,
                )
                runner1.run(smoke_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue_18(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_TPD")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_tpd_user_engagement_report()
            if 'No data found' in self.driver.page_source:
                print('TPD user engengement Report is showing no data found!..')
            else:
                smoke_test = unittest.TestSuite()
                smoke_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        user_engagement_report_smoke.User_Engagement_Smoke
                    )])
                p = pwd()
                outfile = open(p.get_smoke_chart_tables_report(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='TPD User Engagement Report Smoke Test Report',
                    verbosity=1,
                )
                runner1.run(smoke_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue_19(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_TPD")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_tpd_user_on_boarding_report()
            if 'No data found' in self.driver.page_source:
                print('TPD user on boarding Report is showing no data found!..')
            else:
                smoke_test = unittest.TestSuite()
                smoke_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        user_on_boarding_line_smoke.User_On_Boarding_Line_Chart_Smoke
                    )])
                p = pwd()
                outfile = open(p.get_smoke_chart_tables_report(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='TPD User on boarding Report Smoke Test Report',
                    verbosity=1,
                )
                runner1.run(smoke_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue_20(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_ETB")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_etb_content_plays_report()
            if 'No data found' in self.driver.page_source:
                print('ETB GPS Learning Report is showing no data found!..')
            else:
                smoke_test = unittest.TestSuite()
                smoke_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        etb_gps_learning_smoke.Etb_Gps_Learning_Smoke_Suite
                    )])
                p = pwd()
                outfile = open(p.get_smoke_chart_tables_report(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='ETB GPS Learning Report Smoke Test Report',
                    verbosity=1,
                )
                runner1.run(smoke_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue_21(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_ETB")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_etb_usage_per_capita_report()
            if 'No data found' in self.driver.page_source:
                print('ETB User Per Capita Report is showing no data found!..')
            else:
                smoke_test = unittest.TestSuite()
                smoke_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        user_per_capita_smoke.User_Capita_Smoke
                    )])
                p = pwd()
                outfile = open(p.get_smoke_chart_tables_report(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='ETB User Per Capita Report Smoke Test Report',
                    verbosity=1,
                )
                runner1.run(smoke_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue_22(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_ETB")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_etb_nation_learning_report()
            if 'No data found' in self.driver.page_source:
                print('ETB Heart Beat Nation Report is showing no data found!..')
            else:
                smoke_test = unittest.TestSuite()
                smoke_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        etb_nation_learning_smoke.Etb_Nation_Learning_Smoke
                    )])
                p = pwd()
                outfile = open(p.get_smoke_chart_tables_report(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='ETB Heart Beat Nation Report Smoke Test Report',
                    verbosity=1,
                )
                runner1.run(smoke_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    @classmethod
    def tearDownClass(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
