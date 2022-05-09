import unittest

from cQube_Dashboard.Exception_List.download_exception.Download_Missing_Data import exception_download
from reuse_func import GetData

'''Script validation of downloading the exception information '''


class cQube_regression_download_exceptions(unittest.TestCase):
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

    def test_checking_all_the_management_files(self):
        function = exception_download(self.driver)
        res = function.get_exceptions()
        self.assertEqual(0, res, msg="Files are not downloaded")
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
