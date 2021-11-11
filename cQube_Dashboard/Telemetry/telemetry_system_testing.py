import time
import unittest
from Locators.parameters import Data
from cQube_Dashboard.Telemetry.telemetry_details_report import telemetry_map_report

from get_dir import pwd
from reuse_func import GetData


class Test_Telemetry(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.p = pwd()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.page_loading(self.driver)
        self.data.login_cqube(self.driver)
        time.sleep(2)
        self.data.navigate_to_telemetry()
        time.sleep(3)

    def test_navigate_by_dashboard(self):
        count = 0
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        if '' in self.driver.current_url:
            print("Telemetry page is present ")
        else:
            print("Telemetry page is not present ")
            count = count + 1
        self.assertEqual(0,count,msg='Telemetry page is not displayed')
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        self.data.page_loading(self.driver)

    def test_click_on_blocks(self):
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.block_btn).click()
        self.data.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        count = len(dots) - 1
        self.assertNotEqual(0, count  , msg="Markers not present on block level ")
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        self.data.page_loading(self.driver)


    def test_click_on_cluster(self):
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cluster_btn).click()
        self.data.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        count = len(dots) - 1
        self.assertNotEqual(0, count  , msg="Markers not present on cluster level ")
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        self.data.page_loading(self.driver)

    def test_click_on_school(self):
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.schoolbtn).click()
        self.data.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        count = len(dots) - 1
        self.assertNotEqual(0, count, msg="Markers not present on cluster level ")
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        self.data.page_loading(self.driver)

    def test_last7day_download(self):
        b = telemetry_map_report(self.driver)
        res = b.test_overall_records()
        self.assertTrue(res, msg="last7day's csv file is not downloaded")
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        self.data.page_loading(self.driver)

    def test_lastday_download(self):
        b = telemetry_map_report(self.driver)
        res = b.test_lastday_records()
        self.assertTrue(res, msg="last7day's csv file is not downloaded")
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        self.data.page_loading(self.driver)

    def test_overall_download(self):
        b = telemetry_map_report(self.driver)
        res = b.test_overall_records()
        self.assertTrue(res, msg="last7day's csv file is not downloaded")
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        self.data.page_loading(self.driver)

    def test_lastmonth_download(self):
        b = telemetry_map_report(self.driver)
        res = b.test_lastmonth_records()
        self.assertTrue(res, msg="last7day's csv file is not downloaded")
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('telemData').click()
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()