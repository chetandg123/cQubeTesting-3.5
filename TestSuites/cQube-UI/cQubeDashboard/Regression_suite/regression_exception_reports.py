import unittest

from HTMLTestRunner import HTMLTestRunner

from cQube_Dashboard.Exception_List.pat_exception import regression_pat_exception
from cQube_Dashboard.Exception_List.sat_exception import exception_regression_testing
from cQube_Dashboard.Exception_List.student_exception import regression_student_exception
from cQube_Dashboard.Exception_List.teacher_exception import regression_teacher_exception
from get_dir import pwd
from reuse_func import GetData


class MyTestSuite_Exception(unittest.TestCase):
    driver = None
    data = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(200)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)

    def test_issue01(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("sat")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_semester_exception()
            if 'No data found' in self.driver.page_source:
                print('Semester Exception Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        exception_regression_testing.cQube_Semester_Exception_Report)
                ])
                p = pwd()
                outfile = open(p.get_regression_map_reports(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Semester Exception Regression Test Report',
                    verbosity=1, )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue02(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("student")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_student_exception()
            if 'No data found' in self.driver.page_source:
                print('Student Exception Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        regression_student_exception.cQube_Regression_Student_Exception)
                ])
                p = pwd()
                outfile = open(p.get_regression_map_reports(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Student Exception Regression Test Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue03(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("teacher")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_teacher_exception()
            if 'No data found' in self.driver.page_source:
                print('Teacher Exception Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        regression_teacher_exception.cQube_Teacher_Exception_Regression_Report)
                ])
                p = pwd()
                outfile = open(p.get_regression_map_reports(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Teacher Exception Regression Test Report',
                    verbosity=1,

                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status, "is selected due to this unable to run suite")

    def test_issue04(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("pat")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_pat_exception()
            if 'No data found' in self.driver.page_source:
                print('PAT Exception Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        regression_pat_exception.cQube_Pat_Exception_Regression_Report)
                ])
                p = pwd()
                outfile = open(p.get_regression_map_reports(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='PAT Exception Regression Test Report',
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
