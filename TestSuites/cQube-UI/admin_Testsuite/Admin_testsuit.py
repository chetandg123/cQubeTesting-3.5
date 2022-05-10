from Admin_Console.admin_dashboard import check_admin_landing_page
from Admin_Console.logs import Logs_scripts
from Admin_Console.changepassword import change_password
from get_dir import pwd

import unittest
from HTMLTestRunner import HTMLTestRunner

'''Test suite for run the script to perform the checking the working condition of the admin dashboard side 
note- while running admin console script make sure need to connect to vpn '''


class MyTestSuite(unittest.TestCase):

    @staticmethod
    def test_Issue01():
        functional_test = unittest.TestSuite()
        functional_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(check_admin_landing_page.TestAdminLandingPage),
        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Admin console Functional Test Report',
            verbosity=1,
            description="Admin Console Test Result "
        )

        runner1.run(functional_test)
        outfile.close()

    @staticmethod
    def test_Issue02():
        functional_test = unittest.TestSuite()
        functional_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(change_password.ChangePassword),

        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Change password Functional Test Report',
            verbosity=1,
            description="Admin Console Test Result "
        )

        runner1.run(functional_test)
        outfile.close()

    @staticmethod
    def test_Issue03():
        functional_test = unittest.TestSuite()
        functional_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Logs_scripts.TestLogs)

        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Logs Functional Test Report',
            verbosity=1,
            description="Admin Console Test Result "
        )

        runner1.run(functional_test)
        outfile.close()


if __name__ == '__main__':
    unittest.main()
