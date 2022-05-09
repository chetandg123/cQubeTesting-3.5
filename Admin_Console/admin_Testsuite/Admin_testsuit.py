from Admin_Console import create_user, user_list
from Admin_Console.admin_dashboard import check_admin_landing_page
from Admin_Console.logs import Logs_scripts
from Admin_Console.changepassword import change_password
from get_dir import pwd

import unittest
from HTMLTestRunner import HTMLTestRunner

'''Test suite for run the script to perform the checking the working condition of the admin dashboard side 
note- while running admin console script make sure need to connect to vpn '''

class MyTestSuite(unittest.TestCase):

    def test_Issue01(self):
        functional_test = unittest.TestSuite()
        functional_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(check_admin_landing_page.Test_admin_landing_page),
        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Admin console Functional Test Infra_Table_Report',
            verbosity=1,
            description="Admin Console Test Result "
        )

        runner1.run(functional_test)
        outfile.close()

    def test_Issue02(self):
        functional_test = unittest.TestSuite()
        functional_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(change_password.change_password),

        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Change password Functional Test Infra_Table_Report',
            verbosity=1,
            description="Admin Console Test Result "
        )

        runner1.run(functional_test)
        outfile.close()

    def test_Issue03(self):
        functional_test = unittest.TestSuite()
        functional_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Logs_scripts.Test_logs)

        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Logs Functional Test Infra_Table_Report',
            verbosity=1,
            description="Admin Console Test Result "
        )

        runner1.run(functional_test)
        outfile.close()


if __name__ == '__main__':
    unittest.main()
