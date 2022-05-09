import unittest

from Login.login_to_cQube import cQube_Login
from reuse_func import GetData

'''Script performing the login to the cQube application - navigation to application and automatically providing user 
name and password then clicking on login button '''

class login(unittest.TestCase):
    driver = None
    data = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.page_loading(self.driver)

    def test_login_page(self):
        function = cQube_Login(self.driver)
        result = function.test_login_to_cQube()
        self.assertEqual(0, result, msg='Login is failed!')
        self.data.page_loading(self.driver)
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
