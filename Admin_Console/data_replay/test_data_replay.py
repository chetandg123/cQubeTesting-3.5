import time
import unittest
from get_dir import pwd
from reuse_func import GetData


class DataReplay(unittest.TestCase):
    driver = None
    data = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.p = pwd()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.data.open_cqube_appln(self.driver)
        self.data.login_to_adminconsole(self.driver)
        time.sleep(2)

    def test_data_replay_icon(self):
        self.data.click_data_replay(self.driver)
        # self.assertIn("report",self.driver.current_url,"Locators-replay icon is not working")

    def test_data_replay_infrastructure(self):
        self.data.select_data_replay_data_source(self.driver, "Infrastructure")
        time.sleep(2)
        self.data.select_data_replay_year(self.driver, " Delete all data")
        time.sleep(2)

    def test_data_replay_static(self):
        self.data.select_data_replay_data_source(self.driver, "Static")
        time.sleep(2)
        self.data.select_data_replay_year(self.driver, " Delete all data")
        time.sleep(2)

    def test_data_replay_udise(self):
        self.data.select_data_replay_data_source(self.driver, "UDISE")
        time.sleep(2)
        self.data.select_data_replay_year(self.driver, " Delete all data")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
