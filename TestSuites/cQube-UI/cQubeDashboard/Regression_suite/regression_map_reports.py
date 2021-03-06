from Login import login_page
from cQube_Dashboard.Attendance.student_attendance import student_attendance_regression_testing
from cQube_Dashboard.Attendance.teacher_attendance import teacher_attendance_regression_testing
from cQube_Dashboard.Dashboard_Icons import cQube_landing_page
from cQube_Dashboard.School_Infrastructure.Infrastructure_map import School_Map_regression_testing
from cQube_Dashboard.School_Infrastructure.udise_report import udise_regression_testing
from cQube_Dashboard.Student_Performance.pat_map import periodic_regression_testing
from cQube_Dashboard.Student_Performance.sat_map import semester_report_regression_testing
from cQube_Dashboard.Telemetry import telemetry_regression_testing
from get_dir import pwd
import unittest
from HTMLTestRunner import HTMLTestRunner
from reuse_func import GetData


class MyTestSuite_cQube_Map_Reports(unittest.TestCase):
    driver = None
    data = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()  # resue_fun.py
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)

    def test_issue01(self):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(login_page.login),
        ])
        p = pwd()
        outfile = open(p.get_regression_map_reports(), "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='login to cQube regression Test Report',
            verbosity=1,

        )
        runner1.run(regression_test)
        outfile.close()

    def test_issue02(self):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(cQube_landing_page.cQube_Home),
        ])
        p = pwd()
        outfile = open(p.get_regression_map_reports(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='cQube landing page regression Report',
            verbosity=1,

        )
        runner1.run(regression_test)
        outfile.close()

    def test_issue03(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("student")
        if status == str(True):
            self.data.navigate_to_student_report()
            if 'No data found' in self.driver.page_source:
                print('Student Attendance Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    # file name .class name
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        student_attendance_regression_testing.cQube_Student_Attendance_Regression),

                ])
                p = pwd()
                outfile = open(p.get_regression_map_reports(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Student Attendance regression Test Report',
                    verbosity=1, )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue04(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("sat")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_semester_report()
            if 'No data found' in self.driver.page_source:
                print('Semester Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        semester_report_regression_testing.cQube_Semester_Regression_Report),
                ])
                p = pwd()
                outfile = open(p.get_regression_map_reports(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Semester regression Test Report',
                    verbosity=1, )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue05(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("infrastructure")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_school_infrastructure_map()
            if 'No data found' in self.driver.page_source:
                print('School infrastructure Map Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    # file name .class name
                    unittest.defaultTestLoader.loadTestsFromTestCase(School_Map_regression_testing.cQube_SI_Map_Report),

                ])
                p = pwd()
                outfile = open(p.get_regression_map_reports(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='School Infrastructure Map regression Test Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue07(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("telemetry")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_telemetry()
            if 'No data found' in self.driver.page_source:
                print('Telemetry Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(telemetry_regression_testing.Test_Telemetry)
                ])
                p = pwd()
                outfile = open(p.get_regression_map_reports(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Telemetry Regression Test Report',
                    verbosity=1, )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue08(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("udise")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_udise_report()
            if 'No data found' in self.driver.page_source:
                print('UIDSE Map Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(udise_regression_testing.cQube_UdiseReport)
                ])
                p = pwd()
                outfile = open(p.get_regression_map_reports(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Udise Regression Test Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue09(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("pat")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_periodic_report()
            if 'No data found' in self.driver.page_source:
                print('Periodic Map Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        periodic_regression_testing.Periodic_Regression)
                ])
                p = pwd()
                outfile = open(p.get_regression_map_reports(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Periodic Report Regression Test Report',
                    verbosity=1, )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue10(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("teacher")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_teacher_attendance_report()
            if 'No data found' in self.driver.page_source:
                print('Teacher Attendance Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        teacher_attendance_regression_testing.cQube_Teacher_Attendance_Regression
                    )
                ])
                p = pwd()
                outfile = open(p.get_regression_map_reports(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Teacher Attendance Regression Test Report',
                    verbosity=1, )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
