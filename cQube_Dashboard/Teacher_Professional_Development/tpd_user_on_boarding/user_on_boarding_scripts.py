import os
import time
import pandas as pd
from Locators.parameters import Data
from files import Files
from get_dir import pwd
from reuse_func import GetData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class user_on_boarding_report():
    def __init__(self,driver):
        self.driver = driver
        self.data = GetData()
        self.p = pwd()
        self.fname = Files()

    def check_navigation_to_user_on_boarding_report(self):
        count = 0
        self.data.click_on_state(self.driver)
        self.driver.find_element(By.ID, Data.cQube_logo).click()
        time.sleep(1)
        self.data.navigate_to_tpd_user_on_boarding_report()
        if 'enrollment-progress' not in self.driver.current_url:
            print(' User On Boarding Report is not displayed')
            count = count + 1
        else:
            print("User On Boarding Report Report is displayed")
        return count


    def check_hyperlink_functionality(self):
        count = 0
        self.driver.find_element(By.XPATH, Data.hyper_link).click()
        time.sleep(3)
        districts = Select(self.driver.find_element(By.ID, Data.dist_dropdown))
        districts.select_by_index(2)
        print(districts.options[2].text, 'is selected')
        time.sleep(1)
        self.driver.find_element(By.XPATH, Data.hyper_link).click()
        if districts.first_selected_option.text == districts.options[2].text:
            print("Hyperlink is not working ")
            count = count + 1
        else:
            print("Hyper link is working as expected ")
        return count



    def check_selection_of_program_dropdown(self):
        count = 0
        self.driver.find_element(By.XPATH, Data.hyper_link).click()
        time.sleep(3)
        program = Select(self.driver.find_element(By.ID, Data.program_dropdown))
        spents = len(program.options) - 1
        if spents == 0 or spents < 1:
            print('Program dropdown are not having options ')
            count = count + 1
        else:
            for i in range(1, spents):
                program.select_by_index(i)
                time.sleep(2)
                print(program.options[i].text, 'is selected and chart also displayed...')
        return count

    def check_selection_of_course_dropdown(self):
        count = 0
        self.driver.find_element(By.XPATH, Data.hyper_link).click()
        time.sleep(3)
        course = Select(self.driver.find_element(By.ID, Data.course_dropdown))
        spents = len(course.options) - 1
        if spents == 0 or spents < 1 :
            print('Course dropdown are not having options ')
            count = count + 1
        else:
            for i in range(1, spents):
                course.select_by_index(i)
                time.sleep(2)
                print(course.options[i].text, 'is selected and chart also displayed...')
        return count

    def check_download_button_on_selection_of_programs(self):
        count = 0
        self.driver.find_element(By.XPATH, Data.hyper_link).click()
        time.sleep(3)
        program = Select(self.driver.find_element(By.ID, Data.program_dropdown))
        spents = len(program.options) - 1
        if spents == 0 or spents < 1:
            print('Program dropdown are not having options ')
            count = count + 1
        else:
            for i in range(1, spents):
                program.select_by_index(i)
                program_name = program.options[i].text
                time.sleep(2)
                print(program_name, 'is selected and chart also displayed...')
                self.driver.find_element(By.ID,Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + '/' + self.fname.onboarding_program
                if os.path.isfile(self.filename) != True:
                    print(program_name, 'file is not downloaded')
                    count = count + 1
                else:
                    df = pd.read_csv(self.filename)
                    size = len(df)
                    total_enrolled = df['Expected Enrollment'].sum()
                    avg_time = df['Net Enrollment'].sum()
                    if program_name not in df.values :
                        print(program_name,'program is not having details in downloaded csv file')
                        count = count + 1
                    if int(total_enrolled) > 0 and int(avg_time) > 0:
                        print(total_enrolled,avg_time,'values are showing wrong!...')
                        count = count + 1
        return count

    def check_download_button_on_selection_of_courses(self):
        count = 0
        self.driver.find_element(By.XPATH, Data.hyper_link).click()
        time.sleep(3)
        courses = Select(self.driver.find_element(By.ID, Data.course_dropdown))
        spents = len(courses.options) - 1
        if spents == 0 or spents < 1:
            print('Program dropdown are not having options ')
            count = count + 1
        else:
            for i in range(1, spents):
                courses.select_by_index(i)
                course_name = courses.options[i].text
                time.sleep(2)
                print(course_name, 'is selected and chart also displayed...')
                self.driver.find_element(By.ID,Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + '/' + self.fname.onboarding_course
                if os.path.isfile(self.filename) != True:
                    print(course_name, 'file is not downloaded')
                    count = count + 1
                else:
                    df = pd.read_csv(self.filename)
                    size = len(df)
                    total_enrolled = df['Expected Enrollment'].sum()
                    avg_time = df['Net Enrollment'].sum()
                    if course_name not in df.values :
                        print(course_name,'course is not having details in downloaded csv file')
                        count = count + 1
                    if int(total_enrolled) > 0 and int(avg_time) > 0:
                        print(total_enrolled,avg_time,'values are showing wrong!...')
                        count = count + 1
        return count

    def check_download_button_on_selection_of_courses_and_districts(self):
        count = 0
        self.driver.find_element(By.XPATH, Data.hyper_link).click()
        time.sleep(3)
        courses = Select(self.driver.find_element(By.ID, Data.course_dropdown))
        districts = Select(self.driver.find_element(By.ID,Data.dist_dropdown))
        spents = len(courses.options) - 1
        if spents == 0 or spents < 1:
            print('Program dropdown are not having options ')
            count = count + 1
        else:
            for i in range(1, spents):
                courses.select_by_index(i)
                course_name = courses.options[i].text
                time.sleep(2)
                print(course_name, 'is selected and chart also displayed...')
                for j in range(1,len(districts.options-1)):
                    districts.select_by_index(j)
                    time.sleep(2)
                    self.driver.find_element(By.ID,Data.Download).click()
                    time.sleep(3)
                    self.filename = self.p.get_download_dir() + '/' + self.fname.onboarding_course
                    if os.path.isfile(self.filename) != True:
                        print(course_name,districts.options[j].text, 'file is not downloaded')
                        count = count + 1
                    else:
                        df = pd.read_csv(self.filename)
                        size = len(df)
                        total_enrolled = df['Expected Enrollment'].sum()
                        avg_time = df['Net Enrollment'].sum()
                        if course_name not in df.values and districts.options[j].text not in df.values :
                            print(course_name,districts.options[j].text,'course and district wise is not having details in downloaded csv file')
                            count = count + 1
                        if int(total_enrolled) > 0 and int(avg_time) > 0:
                            print(total_enrolled,avg_time,'values are showing wrong!...')
                            count = count + 1
        return count


    def check_download_button_on_selection_of_program_courses_and_districts(self):
        count = 0
        self.driver.find_element(By.XPATH, Data.hyper_link).click()
        time.sleep(3)
        programs = Select(self.driver.find_element(By.ID,Data.program_dropdown))
        courses = Select(self.driver.find_element(By.ID, Data.course_dropdown))
        districts = Select(self.driver.find_element(By.ID,Data.dist_dropdown))
        spents = len(courses.options) - 1
        if len(programs.options-1) == 0:
            print('Program dropdown are not having options ')
            count = count + 1
        else:
            for i in range(1, len(programs.options-1)):
                programs.select_by_index(i)
                program_name = programs.options[i].text
                time.sleep(2)
                for j in range(1,len(courses.options-1)):
                    courses.select_by_index(j)
                    course_name = courses.options[j].text
                    time.sleep(2)
                    print(program_name,course_name, 'is selected and chart also displayed...')
                    for z in range(1,len(districts.options-1)):
                        districts.select_by_index(z)
                        time.sleep(2)
                        district_name = districts.options[z].text
                        self.driver.find_element(By.ID,Data.Download).click()
                        time.sleep(3)
                        self.filename = self.p.get_download_dir() + '/' + self.fname.onboarding_course
                        if os.path.isfile(self.filename) != True:
                            print(program_name,district_name, 'file is not downloaded')
                            count = count + 1
                        else:
                            df = pd.read_csv(self.filename)
                            size = len(df)
                            total_enrolled = df['Expected Enrollment'].sum()
                            avg_time = df['Net Enrollment'].sum()

                            if program_name not in df.values or course_name not in df.values and district_name not in df.values :
                                print(program_name,course_name,district_name.text,'Program , Course and district wise is not having details in downloaded csv file')
                                count = count + 1
                            if int(total_enrolled) > 0 and int(avg_time) > 0:
                                print(total_enrolled,avg_time,'values are showing wrong!...')
                                count = count + 1
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
            if 'enrollment-progress' in self.driver.current_url:
                print(" User OnBoarding report home page is displayed ")
            else:
                print("Navigation to User OnBoarding Report is failed !")
                count = count + 1
        return count

    def check_download_button_on_statewise(self):
        count = 0
        self.driver.find_element(By.XPATH, Data.hyper_link).click()
        time.sleep(3)
        program = Select(self.driver.find_element(By.ID, Data.program_dropdown))
        spents = len(program.options) - 1
        self.driver.find_element(By.ID, Data.Download).click()
        time.sleep(3)
        self.filename = self.p.get_download_dir() + '/' + self.fname.onboarding_statewise
        if os.path.isfile(self.filename) != True:
            print(self.filename, 'Statewise file is not downloaded')
            count = count + 1
        else:
            df = pd.read_csv(self.filename)
            size = len(df)
            total_enrolled = df['Expected Enrollment'].sum()
            avg_time = df['Net Enrollment'].sum()
            n = len(pd.unique(df['Program Name']))
            if int(n) != int(spents):
                print('all programs information is not having in downloaded csv file state wise file')
                count = count + 1
            if int(total_enrolled) > 0 and int(avg_time) > 0:
                print(total_enrolled, avg_time, 'values are showing wrong!...')
                count = count + 1

        return count
