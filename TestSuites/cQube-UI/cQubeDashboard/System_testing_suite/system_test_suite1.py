import unittest
from HTMLTestRunner import HTMLTestRunner

from Login import login_page
from cQube_Dashboard.Attendance.student_attendance import student_attendance_system_testing
from cQube_Dashboard.CRC_Visit import crc_report_system_testing
from cQube_Dashboard.Exception_List.sat_exception import exception_system_testing
from cQube_Dashboard.School_Infrastructure.Infrastructure_map import school_map_system_testing
from cQube_Dashboard.School_Infrastructure.composite_report import school_report_system_testing
from cQube_Dashboard.School_Infrastructure.udise_report import udise_system_testing
from cQube_Dashboard.Student_Performance.pat_map import periodic_system_suite
from cQube_Dashboard.Student_Performance.sat_map import semester_report_system_testing
from cQube_Dashboard.Telemetry import telemetry_system_testing
from get_dir import pwd
from reuse_func import GetData


class MyTestSuite(unittest.TestCase):

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
        system_test = unittest.TestSuite()
        system_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(login_page.login),
        ])
        p = pwd()
        outfile = open(p.get_system_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='login to cQube system Test  Report',
            verbosity=1,
        )
        runner1.run(system_test)
        outfile.close()

    def test_issue03(self):
            self.data.page_loading(self.driver)
            status = self.data.get_student_status("student")
            if status == str(True):
                self.data.page_loading(self.driver)
                self.data.navigate_to_student_report()
                if 'No data found' in self.driver.page_source:
                    print('Student Attendance Report is showing no data found!..')
                    self.driver.close()
                else:
                    system_test = unittest.TestSuite()
                    system_test.addTests([
                        # file name .class name
                        unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_system_testing.cQube_Student_Attendance),
                    ])
                    p = pwd()
                    outfile = open(p.get_system_report_path(), "a")

                    runner1 = HTMLTestRunner.HTMLTestRunner(
                        stream=outfile,
                        title='Student Attendance System Test  Report',
                        verbosity=1,
                    )
                    runner1.run(system_test)
                    outfile.close()
            else:
                print(status,"is selected due to this unable to run suite")

    def test_issue04(self):
            self.data.page_loading(self.driver)
            status = self.data.get_student_status("crc")
            if status == str(True):
                self.data.page_loading(self.driver)
                self.data.navigate_to_crc_report()
                if 'No data found' in self.driver.page_source:
                    print('CRC Report is showing no data found!..')
                    self.driver.close()
                else:
                    system_test = unittest.TestSuite()
                    system_test.addTests([
                        # file name .class name
                        unittest.defaultTestLoader.loadTestsFromTestCase(crc_report_system_testing.crc_System_Testing),
                    ])
                    p = pwd()
                    outfile = open(p.get_system_report_path(), "a")
                    runner1 = HTMLTestRunner.HTMLTestRunner(
                        stream=outfile,
                        title='CRC System Test  Report',
                        verbosity=1,
                    )
                    runner1.run(system_test)
                    outfile.close()
            else:
                 print(status,"is selected due to this unable to run suite")

    def test_issue05(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("sat")
        if status == str(True):
             self.data.page_loading(self.driver)
             self.data.navigate_to_semester_report()
             if 'No data found' in self.driver.page_source:
                print('Semester Report is showing no data found!..')
                self.driver.close()
             else:
                system_test = unittest.TestSuite()
                system_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(semester_report_system_testing.cQube_Semester_Report),
                ])
                p = pwd()
                outfile = open(p.get_system_report_path(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Semester System Test  Report',
                    verbosity=1,
                )
                runner1.run(system_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue06(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("infrastructure")
        if status == str(True):
            system_test = unittest.TestSuite()
            system_test.addTests([
                # file name .class name
                unittest.defaultTestLoader.loadTestsFromTestCase(school_map_system_testing.cQube_SI_Map_Report),
            ])
            p = pwd()
            outfile = open(p.get_system_report_path(), "a")
            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='School Infrastructure Map system Test  Report',
                verbosity=1,
            )
            runner1.run(system_test)
            outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue07(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("infrastructure")
        if status == str(True):
             self.data.page_loading(self.driver)
             self.data.navigate_to_composite_infrastructure()
             if 'No data found' in self.driver.page_source:
                print('School infrastructure Report is showing no data found!..')
                self.driver.close()
             else:
                system_test = unittest.TestSuite()
                system_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(school_report_system_testing.cQube_SI_Report)
                ])
                p = pwd()
                outfile = open(p.get_system_report_path(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='School Infrastructre scattor plot system  Report',
                    verbosity=1,
                )
                runner1.run(system_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue11(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("sat")
        if status == str(True):
            system_test = unittest.TestSuite()
            system_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    exception_system_testing.cQube_Semester_Exception_Report)
            ])
            p = pwd()
            outfile = open(p.get_system_report_path(), "a")
            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Semester Exception system Test  Report',
                verbosity=1,)
            runner1.run(system_test)
            outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue12(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("telemetry")
        if status == str(True):
          self.data.page_loading(self.driver)
          self.data.navigate_to_telemetry()
          if 'No data found' in self.driver.page_source:
            print('Telemetry Report is showing no data found!..')
            self.driver.close()
          else:
            system_test = unittest.TestSuite()
            system_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    telemetry_system_testing.Test_Telemetry)
            ])
            p = pwd()
            outfile = open(p.get_system_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Telemetry system Test  Report',
                verbosity=1,
            )
            runner1.run(system_test)
            outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue13(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("udise")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_udise_report()
            if 'No data found' in self.driver.page_source:
                print('UIDSE Map Report is showing no data found!..')
                self.driver.close()
            else:
                system_test = unittest.TestSuite()
                system_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        udise_system_testing.cQube_UdiseReport)
                ])
                p = pwd()
                outfile = open(p.get_system_report_path(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Udise System Test  Report',
                    verbosity=1,
                )
                runner1.run(system_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")


    def test_issue15(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("pat")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_periodic_report()
            if 'No data found' in self.driver.page_source:
                print('Periodic Map Report is showing no data found!..')
                self.driver.close()
            else:
                system_test = unittest.TestSuite()
                system_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        periodic_system_suite.Periodic_System_Testing)
                ])
                p = pwd()
                outfile = open(p.get_system_report_path(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Periodic  Report System Test  Report',
                    verbosity=1,)
                runner1.run(system_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")


    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
