import unittest
from selenium.webdriver.support.select import Select
from Locators.parameters import Data

from cQube_Dashboard.Attendance.student_attendance.student_attendance_report import student_attendance_report
from reuse_func import GetData


class cQube_Student_Attendance(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_student_report()
        year = Select(self.driver.find_element_by_id(Data.sar_year))
        month = Select(self.driver.find_element_by_id(Data.sar_month))
        self.year = year.first_selected_option.text
        self.month = month.first_selected_option.text

    def test_click_on_blocks(self):
        block = student_attendance_report(self.driver)
        result = block.check_markers_on_block_map()
        self.assertNotEqual(0, len(result) - 1, msg="Dots are not present on map")

    def test_click_on_clusters(self):
        cluster = student_attendance_report(self.driver)
        result = cluster.check_markers_on_clusters_map()
        self.assertNotEqual(0, len(result) - 1, msg="Dots are not present on map")

    def test_click_on_schools(self):
        school = student_attendance_report(self.driver)
        result = school.check_markers_on_schools_map()
        self.assertNotEqual(0, int(len(result) - 1), msg="Dots are not present on map")

    def test_districtwise_csv_download(self):
        csv = student_attendance_report(self.driver, self.year, self.month)
        result = csv.click_download_icon_of_district()
        self.assertEqual(0,result,msg='Mis match found at footer informations')
        print('Districtwise csv file is downloaded')
        self.data.page_loading(self.driver)

    def test_choose_district_block_cluster(self):
        dist = student_attendance_report(self.driver, self.year, self.month)
        result = dist.check_districts_csv_download()
        if result == 0:
            print("Block per district csv report download is working")
            print("on selection of each district")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            raise self.failureException("Block per district csv report download is working")
        block = student_attendance_report(self.driver, self.year, self.month)
        result = block.check_csv_download()
        if result == 0:
            print("Cluster per block csv report download is working")
            print("on selection of each district and block")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            raise self.failureException("Cluster per block csv report download is working")
        schools = student_attendance_report(self.driver, self.year, self.month)
        result = schools.check_district_block_cluster()
        if result == 0:
            print("Schools per cluster csv download report is working")
            print("on selection of each district,block and cluster")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            raise self.failureException("Schools per cluster csv report download is working")

    def test_dots_on_each_districts(self):
        dist = student_attendance_report(self.driver)
        result = dist.check_markers_on_block_map()
        if result != 0:
            raise self.failureException('data not found')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
