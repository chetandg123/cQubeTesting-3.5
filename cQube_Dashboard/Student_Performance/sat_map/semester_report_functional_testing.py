import time
import unittest

from Locators.parameters import Data
from cQube_Dashboard.Student_Performance.sat_map.semester_assesment_test import sat_map_report
from reuse_func import GetData

'''Script perform the test the blocks , cluster and school level buttons and dropdowns , map records , 
footer information's '''


class cQube_Semester_FunctionalTest(unittest.TestCase):
    driver = None
    data = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_semester_report()
        time.sleep(5)

    def test_click_on_semester_report(self):
        sr = sat_map_report(self.driver)
        result = sr.check_semester_landing_page()
        if "sat-report" in result:
            print("Navigating to semester report is working")
        else:
            raise self.failureException("Semester report Not Found")
        self.data.page_loading(self.driver)

    # def test_sem_options(self):
    #     b =Semester_options(self.driver)
    #     res1,res2 = b.test_semester_option()
    #     self.assertEqual(0,res1,msg="Semester 1 is selected ")
    #     self.assertNotEqual(0,res2,msg="Markers are missing on semeter2 map ")
    #     print('Semester 2 is working ')
    #     self.data.page_loading(self.driver)

    def test_click_on_blocks(self):
        block = sat_map_report(self.driver)
        result = block.check_markers_on_block_map()
        self.assertNotEqual(0, len(result) - 1, msg="Dots are not present on map")
        print("Blocks button is working")
        print("Markers are present on the map")

    def test_click_on_blocks_cluster_schools(self):
        block = sat_map_report(self.driver)
        result = block.check_last_30_days()
        self.assertEqual(0, result, msg='Footer mismatch found')
        self.data.page_loading(self.driver)

        block.check_last_7_days()
        self.assertEqual(0, result, msg='Footer mismatch found')
        self.data.page_loading(self.driver)

    def test_last30_districts(self):
        block = sat_map_report(self.driver)
        result = block.check_last_30_days_districts()
        self.assertEqual(0, result, msg='Some footer value mismatch found ')
        self.assertEqual(0, result, msg='Files are not downloaded')

    def test_last7days_districts(self):
        block = sat_map_report(self.driver)
        result = block.check_last_7_days_districts()
        self.assertEqual(0, result, msg='Some footer value mismatch found ')
        self.assertEqual(0, result, msg='Files are not downloaded')

    def test_last30days_district_blockwise_clusterwise(self):
        block = sat_map_report(self.driver)
        result = block.check_last30days_districts_block()
        if result == 0:
            print("Cluster per block csv report download is working")
            print("on selection of each district and block")
        else:
            raise self.failureException("Cluster per block csv report download not is working")
        schools = sat_map_report(self.driver)
        result = schools.check_last30_district_block_cluster()
        if result == 0:
            print("Schools per cluster csv download report is working")
            print("on selection of each district,block and cluster")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            raise self.failureException("Schools per cluster csv report download not is working")

    def test_last7days_district_blockwise_clusterwise(self):
        block = sat_map_report(self.driver)
        result = block.check_last7days_districts_block()
        self.assertEqual(result, 0, msg="Cluster per block csv report download not is working")

        schools = sat_map_report(self.driver)
        result = schools.check_last7_district_block_cluster()
        if result == 0:
            print("Schools per cluster csv download report is working")
            print("on selection of each district,block and cluster")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            raise self.failureException("Schools per cluster csv report download not is working")

    def test_click_on_clusters(self):
        cluster = sat_map_report(self.driver)
        result = cluster.check_markers_on_clusters_map()
        self.assertNotEqual(0, len(result) - 1, msg="Dots are not present on map")
        print("Clusters button is working")
        print("Markers are present on the map")

    def test_click_on_schools(self):
        school = sat_map_report(self.driver)
        result = school.check_markers_on_clusters_map()
        self.assertNotEqual(0, len(result) - 1, msg="Dots are not present on map")
        print("Schools button is working")
        print("Markers are present on the map")

    def test_logout(self):
        logout = sat_map_report(self.driver)
        result = logout.click_on_logout()
        self.assertEqual("Log in to cQube", result, msg="login page is not exist!..")
        self.data.login_cqube(self.driver)
        self.data.navigate_to_semester_report()
        print("Logout Functionality is working")

    def test_check_hyperlinks(self):
        hyperlinks = sat_map_report(self.driver)
        result1, result2, choose_dist = hyperlinks.click_on_hyperlinks()
        if result1 == False and result2 == False and choose_dist == "Choose a District":
            print("hyperlinks are working")
        else:
            raise self.failureException("hyperlinks are not working")

    def test_districtwise_csv_download(self):
        csv = sat_map_report(self.driver)
        result = csv.click_download_icon_of_district()
        if result == "Mismatch found at footer values":
            raise self.failureException(result)
        else:
            print("District wise csv report download is working")

    def test_blockwise_csv_download(self):
        csv = sat_map_report(self.driver)
        result = csv.click_download_icon_of_blocks()
        if result == "File Not Downloaded":
            raise self.failureException(result)
        else:
            print("Block wise csv report download is working")

    def test_clusterwise_csv_download(self):
        csv = sat_map_report(self.driver)
        result = csv.click_download_icon_of_clusters()
        if result == "File Not Downloaded":
            raise self.failureException(result)
        else:
            print("Cluster wise csv report download is working")

    #
    # def test_schoolwise_csv_download(self):
    #     csv = SchoolwiseCsv(self.driver)
    #     result = csv.click_download_icon_of_schools()
    #     self.assertEqual(result,0,msg="School wise csv report download is working")

    def test_home_button(self):
        self.driver.find_element_by_id(Data.menu_icon).click()
        time.sleep(2)
        self.data.navigate_to_semester_report()
        if "sat-report" in self.driver.current_url:
            print("test_home_button is working")
        else:
            raise self.failureException('test_home_button is not working')

    def test_home_icon(self):
        home = sat_map_report(self.driver)
        home.click_on_blocks_click_on_home_icon()
        result = home.click_HomeButton()
        if "sat-report" in result:
            print("Home Icon is working")
        else:
            raise self.failureException('Home Icon is not working')

    def test_gradewise_csv_downloading(self):
        tc = sat_map_report(self.driver)
        res = tc.check_grade_dropdown_options()
        self.assertNotEqual(0, res, msg="Grade options are not present ")
        print("Checked with grade options in sat map report")
        self.data.page_loading(self.driver)

        fun = sat_map_report(self.driver)
        res1 = fun.click_each_grades()
        self.assertEqual(0, res1, msg="gradewise csv file is not downloaded")

    def test_subjectwise_csv_downloading(self):
        tc = sat_map_report(self.driver)
        res = tc.select_subjects_dropdown()
        self.assertEqual(0, res, msg="Subjectwise csv file is not downloaded")

    def test_choose_district_block_cluster(self):
        dist = sat_map_report(self.driver)
        result = dist.check_district()
        if result == 0:
            print("Block per district csv report download is working")
            print("on selection of each district")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            raise self.failureException("Block per district csv report download is not working")
        block = sat_map_report(self.driver)
        result = block.check_districts_block()
        if result == 0:
            print("Cluster per block csv report download is working")
            print("on selection of each district and block")
        else:
            raise self.failureException("Cluster per block csv report download not is working")
        schools = sat_map_report(self.driver)
        result = schools.check_district_block_cluster()
        self.assertEqual(0, result, msg='School of cluster csv file downloaded')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
