import os
import time
import unittest

from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.by import By

from Locators.parameters import Data
from cQube_Dashboard.Telemetry.telemetry_details_report import telemetry_map_report

from filenames import file_extention

from get_dir import pwd
from reuse_func import GetData


class Test_Telemetry(unittest.TestCase):
    driver = None
    data = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.p = pwd()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.data.open_cqube_appln(self.driver)
        self.data.page_loading(self.driver)
        self.data.login_cqube(self.driver)
        time.sleep(2)
        self.data.navigate_to_telemetry()
        time.sleep(3)

    def test_navigate_by_dashboard(self):
        count = 0
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.data.page_loading(self.driver)
        self.driver.find_element(By.ID, 'telemetry').click()
        time.sleep(1)
        self.driver.find_element_by_id('telemData').click()
        if 'telemetry' in self.driver.current_url:
            print("Telemetry page is present ")
        else:
            print("Telemetry page is not present ")
            count = count + 1
        self.assertEqual(0, count, msg='Telemetry page is not displayed')
        self.data.navigate_to_telemetry()

    def test_click_on_blocks_cluster_school(self):
        self.data.page_loading(self.driver)
        p = pwd()
        count = 0
        files = file_extention()
        self.driver.find_element_by_id(Data.block_btn).click()
        self.data.page_loading(self.driver)
        time.sleep(5)
        if 'No data found' in self.driver.page_source:
            print('Block level temetry data is not found ')
        else:
            dots = self.driver.find_elements_by_class_name(Data.dots)
            markers = len(dots) - 1
            self.assertNotEqual(0, markers, msg="Markers not present on block level ")
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            self.filename = p.get_download_dir() + '/' + files.telemtry_block() + self.data.get_current_date() + '.csv'
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print('Block wise csv file is not download')
                count = count + 1
            else:
                print(files.telemtry_block() + ' csv file downloaded')
            os.remove(self.filename)
        self.assertEqual(count, 0, msg='Block level csv file not downloaded ')
        self.driver.find_element_by_id('home').click()

        # cluster function

        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cluster_btn).click()
        self.data.page_loading(self.driver)
        time.sleep(5)
        if 'No data found' in self.driver.page_source:
            print('Cluster level temetry data is not found ')
        else:
            dots = self.driver.find_elements_by_class_name(Data.dots)
            markers = len(dots) - 1
            self.assertNotEqual(0, markers, msg="Markers not present on cluster level ")
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            self.filename = p.get_download_dir() + '/' + files.telemetry_cluster() + self.data.get_current_date() + '.csv'
            if os.path.isfile(self.filename) != True:
                print('Cluster wise csv file is not download')
                count = count + 1
            else:
                print(files.telemetry_cluster() + '  csv file downloaded ')
            os.remove(self.filename)
        self.assertEqual(count, 0, msg='Cluster level csv file not downloaded ')
        self.driver.find_element_by_id('home').click()

        # School Function

        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.schoolbtn).click()
        self.data.page_loading(self.driver)
        time.sleep(5)
        if 'No data found' in self.driver.page_source:
            print('School level temetry data is not found ')
        else:
            dots = self.driver.find_elements_by_class_name(Data.dots)
            markers = len(dots) - 1
            self.assertNotEqual(0, markers, msg="Markers not present on School level ")
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            self.filename = p.get_download_dir() + '/' + files.telemetry_school() + self.data.get_current_date() + '.csv'
            if not os.path.isfile(self.filename):
                print('School wise csv file is not download')
                count = count + 1
            else:
                print(files.telemetry_school() + 'is downloaded csv file')
            os.remove(self.filename)
        self.assertEqual(0, count, msg='File is not downloaded')
        self.driver.find_element_by_id('home').click()

    def test_check_with_lastday(self):
        b = telemetry_map_report(self.driver)
        res1, res2, res3 = b.test_lastday_records()
        self.assertNotEqual(0, res1, msg='Block level markers are not present')
        self.assertNotEqual(0, res2, msg='Cluster level markers are not present')
        self.assertNotEqual(0, res3, msg='School level markers are not present')
        print('Last 7 days checked for block , cluster and school levels ')
        self.data.navigate_to_telemetry()

    def test_last7day_timeperiod(self):
        b = telemetry_map_report(self.driver)
        res1, res2, res3 = b.test_last7day_records()
        self.assertNotEqual(0, res1, msg='Block level markers are not present')
        self.assertNotEqual(0, res2, msg='Cluster level markers are not present')
        self.assertNotEqual(0, res3, msg='School level markers are not present')
        self.data.navigate_to_telemetry()

    def test_lastmonth_timeperiod(self):
        b = telemetry_map_report(self.driver)
        res1, res2, res3 = b.test_lastmonth_records()
        self.assertNotEqual(0, res1, msg='Block level markers are not present')
        self.assertNotEqual(0, res2, msg='Cluster level markers are not present')
        self.assertNotEqual(0, res3, msg='School level markers are not present')
        self.data.navigate_to_telemetry()

    def test_overall_period(self):
        b = telemetry_map_report(self.driver)
        res1, res2, res3 = b.test_overall_records()
        self.assertNotEqual(0, res1, msg='Block level markers are not present')
        self.assertNotEqual(0, res2, msg='Cluster level markers are not present')
        self.assertNotEqual(0, res3, msg='School level markers are not present')
        self.data.navigate_to_telemetry()

    def test_last7day_download(self):
        b = telemetry_map_report(self.driver)
        res = b.test_last_7_records()
        self.assertTrue(res, msg="last 7day's csv file is not downloaded")
        self.data.navigate_to_telemetry()

    def test_lastday_download(self):
        b = telemetry_map_report(self.driver)
        res = b.test_lastday_records()
        self.assertTrue(res, msg="last7day's csv file is not downloaded")
        self.data.navigate_to_telemetry()

    def test_overall_download(self):
        b = telemetry_map_report(self.driver)
        res = b.test_overall_records()
        self.assertTrue(res, msg="last7day's csv file is not downloaded")
        self.data.navigate_to_telemetry()

    def test_lastmonth_download(self):
        b = telemetry_map_report(self.driver)
        res = b.test_lastmonth_records()
        self.assertTrue(res, msg="last7day's csv file is not downloaded")
        self.data.navigate_to_telemetry()

    def test_homeicon(self):
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.block_btn).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cluster_btn).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.schoolbtn).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('home').click()
        self.data.navigate_to_telemetry()

    def test_clickon_homebtn(self):
        count = 0
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.data.page_loading(self.driver)
        # self.driver.find_element_by_id('telemData').click()
        self.data.navigate_to_telemetry()
        if 'telemetry' in self.driver.current_url:
            print("Telemetry page is present ")
        else:
            print("Telemetry page is not present ")
            count = count + 1
        self.assertEqual(0, count, msg='Telemetry page is not displayed')
        self.data.page_loading(self.driver)
        self.data.navigate_to_telemetry()

    def test_logout(self):
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(2)
        self.driver.find_element_by_id(Data.logout).click()
        time.sleep(3)
        self.assertEqual('Log in to cQube', self.driver.title, msg="logout is not working ")
        self.data.login_cqube(self.driver)
        time.sleep(2)
        self.data.navigate_to_telemetry()
        time.sleep(5)
        count = 0
        if 'telemetry' in self.driver.current_url:
            print("Telemetry page is displayed")
        else:
            print('Failed to navigate to telemetry report page ')
            count = count + 1
        self.assertEqual(0, count, msg='Navigation is failed ')
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
