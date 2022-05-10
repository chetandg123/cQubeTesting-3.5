import os
import time
import unittest
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.parameters import Data
from cQube_Dashboard.Attendance.teacher_attendance.teacher_attendance_report import Teacher_Attendance_Report
from get_dir import pwd
from reuse_func import GetData

'''Script perform the test the blocks , cluster and school level buttons and dropdowns , map records , 
footer information's '''


class cQube_Teacher_Attendance_SmokeTest(unittest.TestCase):
    driver = None
    data = None

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)
        self.data.navigate_to_teacher_attendance_report()
        year = Select(self.driver.find_element_by_id(Data.sar_year))
        month = Select(self.driver.find_element_by_id(Data.sar_month))
        self.year = year.first_selected_option.text
        self.month = month.first_selected_option.text

    def test_click_on_student_attendence_report(self):
        sar = Teacher_Attendance_Report(self.driver, self.year, self.month)
        result = sar.click_on_tar()
        if "teacher-attendance" in result:
            print("Teacher Attendance Report is Working")
        else:
            raise self.failureException("Teacher Attendance Report Is Not Working")

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
        time.sleep(2)
        self.driver.find_element_by_id(Data.logout).click()
        self.assertEqual("Log in to cQube", self.driver.title, msg="Logout is not worked")
        time.sleep(2)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_teacher_attendance_report()
        print("Logout functionality is working fine...")
        self.data.page_loading(self.driver)

    def test_check_hyperlinks(self):
        hyperlinks = Teacher_Attendance_Report(self.driver, self.year, self.month)
        result1, result2, choose_dist = hyperlinks.click_on_hyperlinks()
        if result1 == False and result2 == False and choose_dist == "Choose a District ":
            print("hyperlinks are working")
        else:
            raise self.failureException("hyperlinks are not working")

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
        home = Teacher_Attendance_Report(self.driver, self.year, self.month)
        home.click_on_blocks_click_on_home_icon()
        result = home.click_HomeButton()
        if "teacher-attendance" in result:
            print("Home Icon is Working")
        else:
            raise self.failureException('Home Icon is not working')

    def test_download(self):
        self.p = pwd()
        state = GetData()
        state.click_on_state(self.driver)
        management = self.driver.find_element_by_id('name').text
        manage = management[16:].lower()
        element = self.driver.find_element_by_id(Data.Download)
        try:
            element.click()
            time.sleep(3)
            print("Download Button is working")
            self.filename = self.p.get_download_dir() + '/teacher_attendance_' + manage.strip() + '_allDistricts_overall_' + self.data.get_current_date() + '.csv'
            if self.filename != True:
                print("District level csv file is not downloaded")
            os.remove(self.filename)
        except WebDriverException:
            raise self.failureException("Download Button is not working")

    def test_markers_on_map(self):
        state = GetData()
        state.click_on_state(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        if int(len(dots) - 1) != 0:
            print('Markers are present on the map')
        else:
            raise self.failureException("Markers are not present on the map")

    def test_no_of_schools_is_equals_at_districts_blocks_clusters_schools(self):
        tc = Teacher_Attendance_Report(self.driver, self.year, self.month)
        self.school_count, Bschools = tc.block_no_of_schools()
        self.assertEqual(int(self.school_count), int(Bschools),
                         msg="Block level no of schools are not equal to no of schools ")

        schools, Cschools = tc.cluster_no_of_schools()
        self.assertEqual(int(schools), int(Cschools), msg="Cluster level no of schools are not equal to no of schools ")

        schools, Sschools = tc.schools_no_of_schools()
        self.assertEqual(int(schools), int(Sschools), msg="Cluster level no of schools are not equal to no of schools ")

    def test_total_no_of_teachers_is_equals_at_districts_blocks_clusters_schools(self):
        tc = Teacher_Attendance_Report(self.driver, self.year, self.month)
        student_count, Bstudents = tc.block_total_no_of_teachers()
        self.assertEqual(int(student_count), int(Bstudents), msg="Block level no of students are not equal")
        student_count, Cstudents = tc.cluster_total_no_of_teachers()
        self.assertEqual(int(student_count), int(Cstudents), msg="Cluster level no of students are not equal")
        student_count, Sstudents = tc.schools_total_no_of_teacher()
        self.assertEqual(int(student_count), int(Sstudents), msg="Cluster level no of students are not equal")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
