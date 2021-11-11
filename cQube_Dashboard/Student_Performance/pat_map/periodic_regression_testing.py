import time
import unittest

from Locators.parameters import Data
from cQube_Dashboard.Student_Performance.pat_map.Periodic_Assessment_Test import Periodic_Assessment_Test

from reuse_func import GetData


class periodic_regression(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_periodic_report()
        self.data.page_loading(self.driver)


    def test_dashboard_patreport(self):
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.data.page_loading(self.driver)
        self.data.navigate_to_periodic_report()
        time.sleep(3)
        if 'pat-report' in self.driver.current_url:
            print('Navigated to Periodic Assessment report')
        else:
            print('Pat report icon is not working')
            count = count + 1
        self.assertEqual(count,0,msg='Pat report button is not working')
        self.data.page_loading(self.driver)

    def test_DistrictwiseCsv(self):
        cls = Periodic_Assessment_Test(self.driver)
        func = cls.click_download_icon()
        self.assertEqual(0,func,msg='Mismatch found at Districtwise footer values')
        print('Downloading district level csv file is working')
        self.data.page_loading(self.driver)

    def test_blockbutton_footers(self):
        b = Periodic_Assessment_Test(self.driver)
        res1, res2 = b.check_with_footervalues()
        self.assertNotEqual(0, res1, msg='markers are not present on block levels')
        self.assertEqual(0, res2, msg='Footer values mis match found')
        print('Block level records are working fine')
        self.data.page_loading(self.driver)

    def test_clusterbutton_footers(self):
        b = Periodic_Assessment_Test(self.driver)
        res1, res2 = b.check_with_footervalues()
        self.assertNotEqual(0, res1, msg='markers are not present on block levels')
        self.assertEqual(0, res2, msg='Footer values mis match found')
        print('cluster level records are working fine')
        self.data.page_loading(self.driver)

    def test_schoolbutton_footers(self):
        b = Periodic_Assessment_Test(self.driver)
        res1, res2 = b.check_with_footers()
        self.assertNotEqual(0, res1, msg='markers are not present on block levels')
        self.assertEqual(0, res2, msg='Footer values mis match found')
        print('School level records are working fine')
        self.data.page_loading(self.driver)

    def test_TotalStudentsSchools(self):
        b = Periodic_Assessment_Test(self.driver)
        res= b.block_cluster_schools_footer_info()
        self.assertEqual(res,0,msg='Block level footers  are not matched')
        self.data.page_loading(self.driver)


    def test_homebtn(self):
        b = Periodic_Assessment_Test(self.driver)
        res = b.click_HomeButton()
        self.assertEqual(0,res,msg='home button is not worked ')
        print('Home button is working ')
        self.data.navigate_to_periodic_report()
        self.data.page_loading(self.driver)

    def test_check_hyperlinks(self):
        hyperlinks = Periodic_Assessment_Test(self.driver)
        result1, result2, choose_dist = hyperlinks.click_on_hyperlinks()
        if result1 == False and result2 == False and choose_dist == "Choose a District":
            print("hyperlinks are working")
        else:
            raise self.failureException("hyperlinks are not working")
        self.data.page_loading(self.driver)

    def test_Logout(self):
        b = Periodic_Assessment_Test(self.driver)
        res = b.click_on_logout()
        self.assertEqual('Log in to cQube',res ,msg='Logout button is not working')
        self.data.page_loading(self.driver)
        print('Logout button is button and navigated to login page ')
        self.data.login_cqube(self.driver)
        self.data.navigate_to_periodic_report()
        self.data.page_loading(self.driver)


    def test_each_district(self):
        b = Periodic_Assessment_Test(self.driver)
        res = b.check_district()
        self.assertEqual(0, res, msg='Some mis match found at districtwise records')
        print('Districtwise records are working fine')
        self.data.page_loading(self.driver)


    def test_district_block_clusterwise(self):
        b = Periodic_Assessment_Test(self.driver)
        res = b.check_district_block_cluster()
        self.assertEqual(0, res, msg='Some mis match found at school level records')
        print('School level records are working fine')
        self.data.page_loading(self.driver)


    def test_periodic_grades(self):
        b = Periodic_Assessment_Test(self.driver)
        res = b.check_grade_dropdown_options()
        self.assertNotEqual(0,res,msg="Grade options not present")
        print("checking with each grades")
        self.data.page_loading(self.driver)

    def test_grades_subjects(self):
        b = Periodic_Assessment_Test(self.driver)
        res = b.select_subjects_dropdown()
        self.assertEqual(0,res,msg='Files are not downloaded')
        print("checking with each grades with subjects")
        self.data.page_loading(self.driver)


    def test_timeseries(self):
        b = Periodic_Assessment_Test(self.driver)
        res =b.test_options_times()
        self.assertNotEqual(0,res,msg="Time series options are not present ")
        print("checking with time period options ")
        self.data.page_loading(self.driver)

    def test_timeseries_with_downloading(self):
        b = Periodic_Assessment_Test(self.driver)
        res =b.time_over_all()
        self.assertEqual(0,res,msg="Some mismatch found in footer values")
        print("checking with time period options ")
        self.data.page_loading(self.driver)

    def test_click_on_blocks_cluster_schools(self):
        block = Periodic_Assessment_Test(self.driver)
        result = block.check_last_30_days()
        self.assertEqual(0, result, msg='Footer mismatch found')
        self.data.page_loading(self.driver)

        res = block.check_last_7_days()
        self.assertEqual(0, result, msg='Footer mismatch found')
        self.data.page_loading(self.driver)

    def test_last30_districts(self):
        block = Periodic_Assessment_Test(self.driver)
        result = block.check_last_30_days_districts()
        self.assertEqual(0, result, msg='Some footer value mismatch found ')
        self.assertEqual(0, result, msg='Files are not downloaded')

    def test_last7days_districts(self):
        block = Periodic_Assessment_Test(self.driver)
        result = block.check_last_7_days_districts()
        self.assertEqual(0, result, msg='Some footer value mismatch found ')
        self.assertEqual(0, result, msg='Files are not downloaded')

    def test_last30days_district_blockwise_clusterwise(self):
        block = Periodic_Assessment_Test(self.driver)
        result = block.check_last30days_districts_block()
        if result == 0:
            print("Cluster per block csv report download is working")
            print("on selection of each district and block")
        else:
            raise self.failureException("Cluster per block csv report download not is working")
        schools = Periodic_Assessment_Test(self.driver)
        result = schools.check_last30_district_block_cluster()
        if result == 0:
            print("Schools per cluster csv download report is working")
            print("on selection of each district,block and cluster")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            raise self.failureException("Schools per cluster csv report download not is working")

    def test_last7days_district_blockwise_clusterwise(self):
        block = Periodic_Assessment_Test(self.driver)
        result = block.check_last7days_districts_block()
        if result == 0:
            print("Cluster per block csv report download is working")
            print("on selection of each district and block")
        else:
            raise self.failureException("Cluster per block csv report download not is working")
        schools = Periodic_Assessment_Test(self.driver)
        result = schools.check_last7_district_block_cluster()
        if result == 0:
            print("Schools per cluster csv download report is working")
            print("on selection of each district,block and cluster")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            raise self.failureException("Schools per cluster csv report download not is working")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()