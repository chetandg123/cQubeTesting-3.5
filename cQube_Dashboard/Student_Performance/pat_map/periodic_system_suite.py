import time

from cQube_Dashboard.Student_Performance.pat_map.Periodic_Assessment_Test import Periodic_Assessment_Test
from reuse_func import GetData
import unittest

'''Script perform the test the blocks , cluster and school level buttons and dropdowns , map records , 
footer information's '''


class periodic_system_testing(unittest.TestCase):
    driver = None
    data = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_periodic_report()
        self.data.page_loading(self.driver)

    def test_Pat_Report_icon(self):
        cls = Periodic_Assessment_Test(self.driver)
        fnc = cls.check_landing_page()
        self.assertEqual(0, fnc, msg='Pat icon is not working ')
        print('Checked with pat icon is working fine ')
        self.data.page_loading(self.driver)

    def test_grades_selection(self):
        b = Periodic_Assessment_Test(self.driver)
        b.click_each_grades()
        print("selected each grade options ")
        self.data.page_loading(self.driver)
        time.sleep(4)

    def test_select_each_subjects(self):
        b = Periodic_Assessment_Test(self.driver)
        b.select_subjects_dropdown()
        print("selected each grade with all the subjects")
        self.data.page_loading(self.driver)

    def test_DistrictwiseCsv(self):
        cls = Periodic_Assessment_Test(self.driver)
        func = cls.click_download_icon()
        self.assertEqual(0, func, msg='Mismatch found at Districtwise footer values')
        print('Downloading district level csv file is working')
        self.data.page_loading(self.driver)

    def test_blockbutton_records(self):
        b = Periodic_Assessment_Test(self.driver)
        res1 = b.click_download_icon_of_blocks()
        self.assertNotEqual(0, res1, msg='markers are not present on block levels')
        print('Block level records are working fine')
        self.data.page_loading(self.driver)

    def test_clusterbutton_records(self):
        b = Periodic_Assessment_Test(self.driver)
        res1 = b.click_download_icon_of_clusters()
        self.assertNotEqual(0, res1, msg='markers are not present on block levels')
        print('cluster level records are working fine')
        self.data.page_loading(self.driver)

    def test_schoolbutton_records(self):
        b = Periodic_Assessment_Test(self.driver)
        res1 = b.click_download_icon_of_schools()
        self.assertNotEqual(0, res1, msg='markers are not present on block levels')
        print('School level records are working fine')
        self.data.page_loading(self.driver)

    def test_DotsOnDistricts(self):
        b = Periodic_Assessment_Test(self.driver)
        res = b.check_dots_on_each_districts()
        self.assertEqual(0, res, msg='Some districts dont have markers ')
        print('Checked with markers on each district wise')
        self.data.page_loading(self.driver)

    def test_district_block_clusterwise(self):
        b = Periodic_Assessment_Test(self.driver)
        res = b.check_district_block_cluster()
        self.assertEqual(0, res, msg='Some mis match found at school level records')
        print('School level records are working fine')
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
