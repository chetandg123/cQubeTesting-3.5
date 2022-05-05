import time
import unittest

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators.parameters import Data

from cQube_Dashboard.Attendance.student_attendance.student_attendance_report import student_attendance_report
from reuse_func import GetData


class cQube_Student_Attendance(unittest.TestCase):
    driver = None
    data = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)
        self.data.navigate_to_student_report()
        year = Select(self.driver.find_element_by_id(Data.sar_year))
        month = Select(self.driver.find_element_by_id(Data.sar_month))
        self.year = year.first_selected_option.text
        self.month = month.first_selected_option.text

    def test_click_on_student_attendence_report(self):
        sar = student_attendance_report(self.driver, self.year, self.month)
        result = sar.click_on_sar()
        if "student-attendance" in result:
            print("Student Attendance Infra_Table_Report is Working")
        else:
            raise self.failureException("Student Attendance Infra_Table_Report Is Not Working")

    def test_click_on_blocks(self):
        state = GetData()
        state.click_on_state(self.driver)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, Data.SAR_Blocks_btn))
        )
        try:
            element.click()
            time.sleep(5)
            print("Blocks Button is working")
        except WebDriverException:
            raise self.failureException("Blocks Button is not clickable")

    def test_click_on_clusters(self):
        state = GetData()
        state.click_on_state(self.driver)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, Data.SAR_Clusters_btn))
        )
        try:
            element.click()
            self.data.page_loading(self.driver)
            print("Cluster Button is working")
        except WebDriverException:
            raise self.failureException("Cluster Button is not working")

    def test_click_on_schools(self):
        state = GetData()
        state.click_on_state(self.driver)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, Data.SAR_Schools_btn))
        )
        try:
            element.click()
            self.data.page_loading(self.driver)
            print("Schools Button is working")
        except WebDriverException:
            raise self.failureException("Schools Button is not working")

    def test_logout(self):
        self.data.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.logout).click()
        self.assertEqual("Log in to cQube", self.driver.title, msg="Logout is not worked")
        time.sleep(2)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_student_report()
        print("Logout functionality is working fine...")
        self.data.page_loading(self.driver)

    def test_choose_district(self):
        state = GetData()
        state.click_on_state(self.driver)
        choose_district = Select(self.driver.find_element_by_id(Data.sar_district))
        try:
            for x in range(1, len(choose_district.options)):
                choose_district.select_by_index(x)
                self.data.page_loading(self.driver)
            print("Choose District is working")
        except WebDriverException:
            raise self.failureException("Choose District is not working")

    def test_choose_block(self):
        self.data.click_on_state(self.driver)
        choose_district = Select(self.driver.find_element_by_id(Data.sar_district))
        choose_block = Select(self.driver.find_element_by_id(Data.sar_block))

        try:
            for x in range(len(choose_district.options) - 1, len(choose_district.options)):
                choose_district.select_by_index(x)
                self.data.page_loading(self.driver)
                for y in range(len(choose_block.options) - 1, len(choose_block.options)):
                    choose_block.select_by_index(y)
                    self.data.page_loading(self.driver)
            print("Choose District and Block is working")
        except WebDriverException:
            raise self.failureException("Choose District and Block is not working")

    def test_choose_cluster(self):
        self.data.click_on_state(self.driver)
        choose_district = Select(self.driver.find_element_by_id(Data.sar_district))
        choose_block = Select(self.driver.find_element_by_id(Data.sar_block))
        choose_cluster = Select(self.driver.find_element_by_id(Data.sar_cluster))

        try:
            for x in range(len(choose_district.options) - 1, len(choose_district.options)):
                choose_district.select_by_index(x)
                self.data.page_loading(self.driver)
                for y in range(len(choose_block.options) - 1, len(choose_block.options)):
                    choose_block.select_by_index(y)
                    self.data.page_loading(self.driver)
                    for z in range(1, len(choose_cluster.options)):
                        choose_cluster.select_by_index(z)
                        self.data.page_loading(self.driver)
            print("Choose District,Block and Cluster is working")
        except WebDriverException:
            raise self.failureException("Choose District,Block and Cluster is not working")

    def test_home_icon(self):
        home = student_attendance_report(self.driver, self.year, self.month)
        home.click_on_blocks_click_on_home_icon()
        result = home.click_HomeButton()
        if "student-attendance" in result:
            print("Home Icon is Working")
        else:
            raise self.failureException('Home Icon is not working')

    def test_districtwise_csv_download(self):
        csv = student_attendance_report(self.driver, self.year, self.month)
        result = csv.click_download_icon_of_district()
        self.assertEqual(0, result, msg='Mis match found at footer information')
        print('Districtwise csv file is downloaded')
        self.data.page_loading(self.driver)

    def test_markers_on_map(self):
        state = GetData()
        state.click_on_state(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        if int(len(dots) - 1) != 0:
            print('Markers are present on the map')
        else:
            raise self.failureException("Markers are not present on the map")

    def test_no_of_schools_is_equals_at_districts_blocks_clusters_schools(self):
        tc = student_attendance_report(self.driver, self.year, self.month)
        schools, Bschools = tc.block_no_of_schools()
        self.assertEqual(int(schools), int(Bschools), msg="Block level no of schools are not equal to no of schools ")
        schools, Cschools = tc.cluster_no_of_schools()
        self.assertEqual(int(schools), int(Cschools), msg="Cluster level no of schools are not equal to no of schools ")
        schools, Sschools = tc.schools_no_of_schools()
        self.assertEqual(int(schools), int(Sschools), msg="Cluster level no of schools are not equal to no of schools ")

    def test_total_no_of_students_is_equals_at_districts_blocks_clusters_schools(self):
        tc = student_attendance_report(self.driver, self.year, self.month)
        student_count, Bstudents = tc.block_total_no_of_students()
        self.assertEqual(int(student_count), int(Bstudents), msg="Block level no of students are not equal")
        student_count, Cstudents = tc.cluster_total_no_of_students()
        self.assertEqual(int(student_count), int(Cstudents), msg="Cluster level no of students are not equal")
        student_count, Sstudents = tc.schools_total_no_of_students()
        self.assertEqual(int(student_count), int(Sstudents), msg="Cluster level no of students are not equal")

    #
    # def test_date_range(self):
    #     daterange = DateRange(self.driver)
    #     result = daterange.check_date_range()
    #     self.driver.find_element_by_id(Locators.menu_icon).click()
    #     time.sleep(2)
    #     self.data.navigate_to_student_report()
    #     self.data.page_loading(self.driver)

    def test_total_no_of_students_and_total_no_of_schools_is_equals_at_blocks_clusters_schools(self):
        tc = student_attendance_report(self.driver, self.year, self.month)
        student_count, Bstudents, school_count, Bschools = tc.check_blocklevel_total_no_of_students()
        self.assertEqual(int(student_count), int(Bstudents), msg="Block level no of students are not equal")
        self.assertEqual(int(school_count), int(Bschools),
                         msg="Block level no of schools are not equal to no of schools ")

        student_count, Cstudents, school_count, Cschool = tc.check_clusterlevel_total_no_of_students()
        self.assertEqual(int(student_count), int(Cstudents), msg="Cluster level no of students are not equal")
        self.assertEqual(int(school_count), int(Cschool),
                         msg="Cluster level no of schools are not equal to no of schools ")

        student_count, Sstudents, school_count, Sschool = tc.check_schoollevel_total_no_of_students()
        self.assertEqual(int(student_count), int(Sstudents), msg="Cluster level no of students are not equal")
        self.assertEqual(int(school_count), int(Sschool),
                         msg="Cluster level no of schools are not equal to no of schools ")
        print("Total number of students and school equals on clicking of blocks,clusters,schools")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
