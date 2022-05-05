# -*- coding: utf-8 -*-
import unittest
import time

from selenium.webdriver.support.select import Select

from Locators.parameters import Data
from cQube_Dashboard.Exception_List.teacher_exception.teacher_exception_scripts import teacher_exception_report
from reuse_func import GetData


class cQube_teacher_exception_regression_report(unittest.TestCase):
    driver = None
    data = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(50)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_teacher_exception()
        self.data.page_loading(self.driver)
        year = Select(self.driver.find_element_by_id(Data.sar_year))
        month = Select(self.driver.find_element_by_id(Data.sar_month))
        self.year = year.first_selected_option.text
        self.month = month.first_selected_option.text

    def test_SchoolPerClusterCsvDownload(self):
        b = teacher_exception_report(self.driver, self.year, self.month)
        time.sleep(2)
        res2 = b.SchoolPerClusterCsvDownload()
        self.assertEqual(0, res2, msg='Some School level files are not downloaded')
        print('Checking each school wise markers and csv file downloading ')
        self.data.page_loading(self.driver)

    def test_DistrictwiseDownload(self):
        b = teacher_exception_report(self.driver, self.year, self.month)
        res2 = b.check_districts_csv_download()
        self.assertEqual(0, res2, msg="Some district level csv file is not downloaded")
        print('Checking each districtwise markers and csv file downloading ')
        time.sleep(2)
        self.data.page_loading(self.driver)

    def test_ClusterPerBlockCsvDownload(self):
        b = teacher_exception_report(self.driver, self.year, self.month)
        time.sleep(2)
        res2 = b.ClusterPerBlockCsvDownload()
        self.assertEqual(0, res2, msg='Some cluster level files are not downloaded')
        print('Checking each cluster markers and csv file downloading ')
        self.data.page_loading(self.driver)

    def test_Data_not_recieved(self):
        b = teacher_exception_report(self.driver, self.year, self.month)
        res, r1, r2, r3 = b.test_total_not_recieved_data()
        self.assertEqual(res, r1, msg='Block level data not recieved count mismatch found')
        self.assertEqual(res, r2, msg='cluster level data not recieved count mismatch found')
        self.assertEqual(res, r3, msg='School level data not recieved count mismatch found')

    def test_teacher_exception_Blocks(self):
        b = teacher_exception_report(self.driver, self.year, self.month)
        res1, res2 = b.check_markers_on_block_map()
        self.assertNotEqual(0, res1, msg="markers are not present on block level map")
        self.assertEqual(0, res2, msg='Footer mis match found at block level')
        print('Checked blockwise markers and csv file downloading ')
        self.data.page_loading(self.driver)

    def test_teacher_clusters(self):
        b = teacher_exception_report(self.driver, self.year, self.month)
        res1, res2 = b.check_markers_on_block_map()
        self.assertNotEqual(0, res1, msg="markers are not present on cluster level map")
        self.assertEqual(0, res2, msg='Footer mis match found at cluster level')
        print('Checked cluster wise markers and csv file downloading ')
        self.data.page_loading(self.driver)

    def test_teacher_school(self):
        b = teacher_exception_report(self.driver, self.year, self.month)
        res1, res2 = b.check_markers_on_block_map()
        self.assertNotEqual(0, res1, msg="markers are not present on school level map")
        self.assertEqual(0, res2, msg='Footer mis match found at school level')
        print('Checked schoolwise markers and csv file downloading ')
        self.data.page_loading(self.driver)

    def test_teacher_exception_icon(self):
        b = teacher_exception_report(self.driver, self.year, self.month)
        res = b.test_icon()
        self.assertEqual(0, res, msg='teacher exception report is not displayed')
        print("Pat exception icon on landing is working ")

    def test_teacher_exception_Logout(self):
        b = teacher_exception_report(self.driver, self.year, self.month)
        res = b.click_on_logout()
        self.assertEqual(res, 'Log in to cQube', msg="logout button is not working")
        self.data.login_cqube(self.driver)
        self.data.navigate_to_teacher_exception()
        print("Logout button is working fine ")
        self.data.page_loading(self.driver)

    def test_cluster_btn_records(self):
        b = teacher_exception_report(self.driver, self.year, self.month)
        res1, res2 = b.check_markers_on_clusters_map()
        self.assertNotEqual(0, res1, msg="Cluster level markers are not present")
        self.assertEqual(0, res2, msg='Cluster csv file is not downloaded')
        print('Checked with Clusterwise map records')
        self.data.page_loading(self.driver)

    def test_block_btn_records(self):
        b = teacher_exception_report(self.driver, self.year, self.month)
        res1, res2 = b.check_markers_on_block_map()
        self.assertNotEqual(0, res1, msg="Block level markers are not present")
        self.assertEqual(0, res2, msg='Blockwise csv file is not downloaded')
        print('Checked with blockwise map records')
        self.data.page_loading(self.driver)

    def test_school_btn_records(self):
        b = teacher_exception_report(self.driver, self.year, self.month)
        res1, res2 = b.check_markers_on_school_map()
        self.assertNotEqual(0, res1, msg="School level markers are not present")
        self.assertEqual(0, res2, msg='Schoolwise csv file is not downloaded')
        print('Checked with schoolwise map records')
        self.data.page_loading(self.driver)

    def test_time_series(self):
        p = teacher_exception_report(self.driver, self.year, self.month)
        res = p.check_time_series_day()
        self.assertEqual(0, res, msg='Time series dropdown having no options ')
        print('checked with Time series drop down ')
        self.data.page_loading(self.driver)

    def test_time_series_dropdown_options(self):
        p = teacher_exception_report(self.driver, self.year, self.month)
        res = p.check_time_series_dropdown_options()
        self.assertNotEqual(0, res, msg='Time series dropdown having no options ')
        print('checked with Time series drop down ')
        self.data.page_loading(self.driver)

    def test_time_last_day_series(self):
        p = teacher_exception_report(self.driver, self.year, self.month)
        res = p.check_time_series_month_and_year()
        self.assertEqual(0, res, msg='last day csv file is not downloaded')
        print('checked with Time series  last day')
        self.data.page_loading(self.driver)

    def test_time_day_series(self):
        p = teacher_exception_report(self.driver, self.year, self.month)
        res = p.check_time_series_day()
        self.assertEqual(0, res, msg='time series day csv file is not downloaded')
        print('checked with Time series  last day')
        self.data.page_loading(self.driver)

    def test_time_last_7day_series(self):
        p = teacher_exception_report(self.driver, self.year, self.month)
        res = p.check_time_series_last_7_days()
        self.assertEqual(0, res, msg='last 7 days csv file is not downloaded')
        print('checked with Time series  last 7 day')
        self.data.page_loading(self.driver)

    def test_time_last_30_day_series(self):
        p = teacher_exception_report(self.driver, self.year, self.month)
        res = p.check_time_series_last_30_days()
        self.assertEqual(0, res, msg='last 30 days csv file is not downloaded')
        print('checked with Time series  last 30 day')
        self.data.page_loading(self.driver)

    def test_timeseries_overall_series(self):
        p = teacher_exception_report(self.driver, self.year, self.month)
        res = p.check_time_overall_series_dropdown()
        self.assertEqual(0, res, msg='overall csv file is not downloaded')
        print('checked with Time series overall')
        self.data.page_loading(self.driver)

    def test_month_and_year(self):
        p = teacher_exception_report(self.driver, self.year, self.month)
        res = p.check_time_series_month_and_year()
        self.assertEqual(0, res, msg='year and month csv file is not downloaded')
        print('checked with Time series year and month')
        self.data.page_loading(self.driver)

    def test_month_and_year_csv_file(self):
        p = teacher_exception_report(self.driver, self.year, self.month)
        res = p.check_year_and_month_dropdowns_csv_download()
        self.assertEqual(0, res, msg='year and month csv file is not downloaded')
        print('checked with Time series year and month')
        self.data.page_loading(self.driver)

    def test_time_series_and_click_on_block_cluster_school_btns(self):
        p = teacher_exception_report(self.driver, self.year, self.month)
        res = p.check_select_time_series_and_click_on_block_cluster_school_btns()
        self.assertEqual(0, res, msg='Footer value mismatch found')
        print("Checking with block ,cluster and school level of time series")
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
