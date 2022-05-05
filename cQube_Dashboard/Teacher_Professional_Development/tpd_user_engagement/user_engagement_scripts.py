import os
import time
import pandas as pd
from Locators.parameters import Data
from files import Files
from get_dir import pwd
from reuse_func import GetData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class user_engagement_automation_scripts:

    def __init__(self, driver):
        self.driver = driver
        self.data = GetData()
        self.p = pwd()
        self.fname = Files()

    def check_navigation_to_user_engagement_report(self):
        count = 0
        self.data.click_on_state(self.driver)
        self.driver.find_element(By.ID, Data.cQube_logo).click()
        time.sleep(1)
        self.data.navigate_to_tpd_user_engagement_report()
        if 'average-time-spend' not in self.driver.current_url:
            print(' User Engagement Report is not displayed')
            count = count + 1
        else:
            print("User Engagement Report Report is displayed")
        return count

    def check_hyperlink_functionality(self):
        count = 0
        self.driver.find_element(By.XPATH, Data.hyper_link).click()
        time.sleep(3)
        districts = Select(self.driver.find_element(By.ID, Data.dist_dropdown))
        districts.select_by_index(2)
        print(districts.options[2].text, 'is selected')
        time.sleep(3)
        self.driver.find_element(By.XPATH, Data.hyper_link).click()
        if districts.first_selected_option.text == districts.options[2].text:
            print("Hyperlink is not working ")
            count = count + 1
        else:
            print("Hyper link is working as expected ")
        return count

    def check_dropdown_options(self):
        self.data.click_on_state(self.driver)
        districts = Select(self.driver.find_element(By.ID, Data.dist_dropdown))
        options = len(districts.options) - 1
        return options

    def check_selection_of_options(self):
        self.driver.find_element(By.XPATH, Data.hyper_link).click()
        time.sleep(3)
        district = Select(self.driver.find_element(By.ID, Data.dist_dropdown))
        spents = len(district.options) - 1
        for i in range(1, spents):
            district.select_by_index(i)
            time.sleep(2)
            print(district.options[i].text, 'is selected and chart also displayed...')
        return spents

    def check_download_functionality_each_districtwise(self):
        count = 0
        self.driver.find_element(By.XPATH, Data.hyper_link).click()
        time.sleep(3)
        district = Select(self.driver.find_element(By.ID, Data.dist_dropdown))
        spents = len(district.options) - 1
        for i in range(1, spents):
            district.select_by_index(i)
            dist_name = district.options[i].text
            time.sleep(2)
            if ' No Data Available ' in self.driver.page_source:
                print(dist_name, 'is not having ')
            else:
                courses = self.driver.find_elements(By.CSS_SELECTOR, Data.course_list)
                count_of_course = len(courses)
                print(dist_name, 'is selected and chart also displayed...')
                self.driver.find_element(By.ID, Data.Download).click()
                time.sleep(3)

                self.filename = self.p.get_download_dir() + '/' + self.fname.user_engagement_districtwise + '' + dist_name + '.csv'
                if os.path.isfile(self.filename) != True:
                    print(self.filename, 'is not downlaoded so download button is not working')
                    count = count + 1
                else:
                    print(self.filename, 'file is downlaoded')
                    df = pd.read_csv(self.filename)
                    size = len(df)
                    total_enrolled = df['Total Enrolled'].sum()
                    avg_time = df['Avg Time Spent'].sum()

                    if int(size) == 0:
                        print('Course Result in UI and Downloaded files are not same  so no of courses ', size)
                        count = count + 1
                    if total_enrolled == 0 and avg_time == 0:
                        print('Total enrolled and avg time  both are not correct ')
                        count = count + 1
                os.remove(self.filename)
        return count

    def check_download_functionality_statewise(self):
        count = 0
        self.driver.find_element(By.XPATH, Data.hyper_link).click()
        time.sleep(3)
        courses = self.driver.find_elements(By.CSS_SELECTOR, Data.course_list)
        count_of_course = len(courses)
        self.driver.find_element(By.ID, Data.Download).click()
        time.sleep(3)
        state_name = self.driver.find_element(By.XPATH, '//p/span').text
        self.filename = self.p.get_download_dir() + '/' + self.fname.user_engagement_statewise + state_name + '.csv'
        if os.path.isfile(self.filename) != True:
            print(self.filename, 'is not downlaoded so download button is not working')
            count = count + 1
        else:
            print(self.filename, 'file is downlaoded')
            df = pd.read_csv(self.filename)
            size = len(df)
            total_enrolled = df['Total Enrolled'].sum()
            avg_time = df['Avg Time Spent'].sum()
            if count_of_course == int(size):
                print('Course Result in UI and Downloaded files are not same  so no of courses ', count_of_course, size)
                count = count + 1
            if total_enrolled == 0 and avg_time == 0:
                print('Total enrolled and avg time  both are not correct ')
                count = count + 1
            os.remove(self.filename)
        return count

    def check_logout_from_report(self):
        count = 0
        self.data.click_on_state(self.driver)
        self.driver.find_element(By.ID, Data.cQube_logo).click()
        time.sleep(1)
        self.driver.find_element(By.ID, Data.logout).click()
        time.sleep(3)
        if 'cQube' not in self.driver.page_source:
            print("Logout button is not working ")
            count = count + 1
        else:
            print("Logout button is working as expected ")
            self.data.login_cqube(self.driver)
            self.data.navigate_to_tpd_user_engagement_report()
            if 'average-time-spend' in self.driver.current_url:
                print(" User Engagement report home page is displayed ")
            else:
                print("Navigation to User Engagement Report is failed !")
                count = count + 1
        return count
