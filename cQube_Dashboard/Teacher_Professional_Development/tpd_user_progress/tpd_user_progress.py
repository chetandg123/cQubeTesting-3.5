import csv
import os
import re
import time

import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Locators.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class user_progress():

    def __init__(self,driver):
        self.driver = driver

        self.fname= ''

    def test_enrollment_icon(self):
        self.data = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        if 'dashboard' in self.driver.current_url:
            print('cQube landing page is displayed')
        else:
            print('Homebtn is not working ')
            count = count + 1
        self.data.page_loading(self.driver)
        self.data.navigate_to_tpd_enrollment_report()
        if 'tpd-enrollment' in self.driver.current_url:
            print('TPD Enrollment report is displayed ')
        else:
            print('TPD Enrollment icon is not working ')
            count = count + 1
        self.data.page_loading(self.driver)
        return count

    def test_dashboard_enrollment_report(self):
        count = 0
        self.data = GetData()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        if 'dashboard' in self.driver.current_url:
            print('cQube landing page is displayed')
        else:
            print('Homebtn is not working ')
        self.data.page_loading(self.driver)
        self.data.navigate_to_tpd_enrollment_report()
        self.data.page_loading(self.driver)
        if 'tpd-enrollment' in self.driver.current_url:
            print("TPD Enrollment report is displayed")
        else:
            print('TPD Enrollment report is not present ')
            count = count + 1
        self.data.page_loading(self.driver)
        return count

    def test_Enrollment_overall(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        timeseries.select_by_index(1)
        self.data.page_loading(self.driver)
        times=(self.driver.find_element_by_name(Data.timeperiods).text).strip()
        if self.msg.no_data_available() in self.driver.page_source:
            print('No Data Available for overall')
            count = 0
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + '/'+'enrollment_completion_enrollment_all_district_overall_'+self.data.get_current_date()+'.csv'
            print(self.filename)
            self.data.page_loading(self.driver)
            # collnames = Select(self.driver.find_element_by_id(Data.coll_names))
            # counter = len(collnames.options)-1
            # for i in range(len(collnames.options),len(collnames.options)-5):
            #     collnames.select_by_index(i)
            #     self.data.page_loading(self.driver)
            if os.path.isfile(self.filename) != True:
                print('Enrollment Over all csv file is not downloaded ')
                count = count + 1
            self.data.page_loading(self.driver)
            os.remove(self.filename)
        return count

    def test_Enrollment_last_day(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.msg = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        timeseries.select_by_index(5)
        self.data.page_loading(self.driver)
        counter = 0
        if self.msg.no_data_available() or self.msg.no_data_found() in self.driver.page_source:
            print('No Data Available/No Data Found for last day')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            times = (self.driver.find_element_by_name(Data.timeperiods).text).strip()
            self.filename = self.p.get_download_dir() + '/'+'tpd_enrollment_all_district_last_day_'+self.data.get_current_date()+'.csv'
            self.data.page_loading(self.driver)
            collnames = Select(self.driver.find_element_by_id(Data.coll_names))
            counter = len(collnames.options)-1
            for i in range(len(collnames.options)-5,len(collnames.options)-1):
                collnames.select_by_index(i)
                self.data.page_loading(self.driver)
            if os.path.isfile(self.filename) != True:
                print('Enrollment last day csv file is not downloaded ')
                count = count + 1
            self.data.page_loading(self.driver)
            os.remove(self.filename)
        return count

    def test_Enrollment_last7_days(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.msg = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        timeseries.select_by_index(4)
        self.data.page_loading(self.driver)
        if self.msg.no_data_available() in self.driver.page_source:
            print('No Data Available for last 7 days')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            times = (self.driver.find_element_by_name(Data.timeperiods).text).strip()
            self.filename = self.p.get_download_dir() + '/'+'tpd_enrollment_all_district_last_7_days_'+self.data.get_current_date()+'.csv'
            self.data.page_loading(self.driver)
            collnames = Select(self.driver.find_element_by_id(Data.coll_names))
            counter = len(collnames.options) - 1
            for i in range(len(collnames.options) - 5, len(collnames.options) - 1):
                collnames.select_by_index(i)
                self.data.page_loading(self.driver)
            if os.path.isfile(self.filename) != True:
                print('Enrollment last 7 days csv file is not downloaded ')
                count = count + 1
            self.data.page_loading(self.driver)
            os.remove(self.filename)
            # return counter, count

    def test_Enrollment_last30_days(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        timeseries.select_by_index(3)
        self.data.page_loading(self.driver)
        if self.msg.no_data_available() in self.driver.page_source:
            print('No Data Available for last 30 days')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            times = (self.driver.find_element_by_name(Data.timeperiods).text).strip()
            # ctype = (self.driver.find_element_by_id(Data.coursetype).text).strip()
            self.filename = self.p.get_download_dir() + '/'+'enrollment_completion_enrollment_all_district_last_30_days_'+self.data.get_current_date()+'.csv'
            print(self.filename)
            self.data.page_loading(self.driver)
            print(self.filename)
            collnames = Select(self.driver.find_element_by_id(Data.coll_names))
            counter = len(collnames.options) - 1
            for i in range(1, len(collnames.options) - 1):
                collnames.select_by_index(i)
                self.data.page_loading(self.driver)
            if os.path.isfile(self.filename) != True:
                print('Enrollment last 30 days csv file is not downloaded ')
                count = count + 1
            self.data.page_loading(self.driver)
            os.remove(self.filename)

    def test_Enrollment_last90_days(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        timeseries.select_by_index(2)
        self.data.page_loading(self.driver)
        if self.msg.no_data_available() in self.driver.page_source:
            print('No Data Available for last 30 days')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + '/'+'enrollment_completion_enrollment_all_district_last_90_days_'+self.data.get_current_date()+'.csv'
            print(self.filename)
            self.data.page_loading(self.driver)
            print(self.filename)
            collnames = Select(self.driver.find_element_by_id(Data.coll_names))
            counter = len(collnames.options) - 1
            for i in range(1, len(collnames.options) - 1):
                collnames.select_by_index(i)
                self.data.page_loading(self.driver)
            if os.path.isfile(self.filename) != True:
                print('Enrollment last 90 days csv file is not downloaded ')
                count = count + 1
            self.data.page_loading(self.driver)
            os.remove(self.filename)

    def test_homeicon_functionality(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        # timeseries.select_by_visible_text(' Last 30 Days ')
        timeseries.select_by_index(2)
        self.data.page_loading(self.driver)
        # present = self.driver.find_element_by_id(Locators.homeicon).isDisplayed()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        print('checked with homeicon function is working ')
        self.data.page_loading(self.driver)
        # return  present

    def test_hyperlink_function(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        timeseries.select_by_index(3)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        print("Checked with hyper link function")
        time.sleep(3)
        self.data.page_loading(self.driver)

    def test_check_download_icon(self):
        self.data = GetData()
        count = 0
        self.p = pwd()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        self.filename =self.p.get_download_dir() + '/'+"enrollment_completion_enrollment_all_district_overall_"+self.data.get_current_date()+'.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            print('Districtwise csv file is not downloaded')
            count = count + 1
        else:
            df = pd.read_csv(self.filename)
            Total_Completed = df[' Total Completed '].sum()
            Total_Enrolled = df[' Total Enrolled '].sum()
            Certificate_Count = df[' Certificate Count '].sum()

            if Total_Completed == 0:
                print(Total_Completed, 'Total completed value is not correct ')
                count = count + 1
            if Total_Enrolled == 0:
                print(Total_Enrolled, 'Total Enrolled value is not correct ')
                count = count + 1
            if Certificate_Count == 0:
                print(Certificate_Count, 'Certificate count value is not correct ')
                count = count + 1
            os.remove(self.filename)
        return count

    def test_coursetype_with_all_districts(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        Districts = Select(self.driver.find_element_by_id(Data.sar_district))
        course_type = Select(self.driver.find_element_by_id(Data.coursetype))
        time = (self.driver.find_element_by_id('time_range').text).strip()
        for i in range(1, len(course_type.options)):
            course_type.select_by_index(i)
            self.data.page_loading(self.driver)
            cname = course_type.options[i].text
            course = cname.strip()
            for j in range(len(Districts.options)-5,len(Districts.options)):
                Districts.select_by_index(j)
                self.data.page_loading(self.driver)
                self.driver.find_element_by_id(Data.Download).click()
                self.data.page_loading(self.driver)
                dname = self.driver.find_element_by_id(Data.sar_district).get_attribute('value')
                value = dname[4:] + '_'

                self.filename = self.p.get_download_dir()+"/"+"enrollment_completion_"+course.lower()+'_overall'+'_'+value.strip()+self.data.get_current_date()+".csv"
                print(self.filename)
                if os.path.isfile(self.filename) != True:
                    print(course_type.options[i].text, Districts.options[j].text, 'csv file not downloaded')
                    count = count + 1
                    self.data.page_loading(self.driver)
                else:
                    df = pd.read_csv(self.filename)
                    Total_Completed = df['Total Completed'].sum()
                    Total_Enrolled = df['Total Enrolled	'].sum()
                    Certificate_Count = df['Certificate Count'].sum()

                    if Total_Completed == 0:
                        print(Total_Completed,'Total completed value is not correct ')
                        count = count + 1
                    if Total_Enrolled == 0:
                        print(Total_Enrolled,'Total Enrolled value is not correct ')
                        count = count + 1
                    if Certificate_Count == 0:
                        print(Certificate_Count,'Certificate count value is not correct ')
                        count = count + 1
                os.remove(self.filename)
        return count

    def test_coursetype_with_all_blockwise(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        Districts = Select(self.driver.find_element_by_id(Data.sar_district))
        Blocks = Select(self.driver.find_element_by_id(Data.sar_block))
        course_type = Select(self.driver.find_element_by_id(Data.coursetype))
        for i in range(1, len(course_type.options)):
            course_type.select_by_index(i)
            cname = course_type.options[i].text
            course = cname.strip()
            self.data.page_loading(self.driver)
            for j in range(len(Districts.options)-1,len(Districts.options)):
                Districts.select_by_index(j)
                self.data.page_loading(self.driver)
                for k in range(1,len(Blocks.options)):
                    Blocks.select_by_index(k)
                    name = Blocks.options[k].text
                    bname = name.strip()
                    self.data.page_loading(self.driver)
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(4)
                    dname = self.driver.find_element_by_id(Data.sar_block).get_attribute('value')
                    value = dname[3:] + '_'
                    # times = (self.driver.find_element_by_id('time_range').text).strip()

                    self.filename = self.p.get_download_dir() + "/" + "enrollment_completion_"+course.lower()+"_"+"overall_" + value.strip() + self.data.get_current_date() + ".csv"
                    print(self.filename)
                    if os.path.isfile(self.filename) != True:
                        print(course_type.options[i].text,Districts.options[j].text,Blocks.options[k].text,'csv file not downloaded')
                        count = count + 1
                        self.data.page_loading(self.driver)
                    else:
                        df = pd.read_csv(self.filename)
                        Total_Completed = df['Total Completed'].sum()
                        Total_Enrolled = df['Total Enrolled	'].sum()
                        Certificate_Count = df['Certificate Count'].sum()

                        if Total_Completed == 0:
                            print(Total_Completed, 'Total completed value is not correct ')
                            count = count + 1
                        if Total_Enrolled == 0:
                            print(Total_Enrolled, 'Total Enrolled value is not correct ')
                            count = count + 1
                        if Certificate_Count == 0:
                            print(Certificate_Count, 'Certificate count value is not correct ')
                            count = count + 1
                    os.remove(self.filename)
                return count

    def test_coursetype_with_all_clusterwise(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        Districts = Select(self.driver.find_element_by_id(Data.sar_district))
        Blocks = Select(self.driver.find_element_by_id(Data.sar_block))
        Cluster = Select(self.driver.find_element_by_id(Data.sar_cluster))
        course_type = Select(self.driver.find_element_by_id(Data.coursetype))
        for i in range(1, len(course_type.options)):
            course_type.select_by_index(i)
            cname = course_type.options[i].text
            course = cname.strip()
            self.data.page_loading(self.driver)
        for j in range(len(Districts.options) - 1, len(Districts.options)):
            Districts.select_by_index(j)
            self.data.page_loading(self.driver)
            for k in range(len(Blocks.options) - 1, len(Blocks.options)):
                Blocks.select_by_index(k)
                self.data.page_loading(self.driver)
                for m in range(1, len(Cluster.options)):
                    Cluster.select_by_index(m)
                    name = Cluster.options[m].text
                    cname = name.strip()
                    self.data.page_loading(self.driver)
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(3)
                    dname = self.driver.find_element_by_id(Data.sar_cluster).get_attribute('value')
                    value = dname[3:] + '_'
                    self.filename = self.p.get_download_dir() + "/" + "enrollment_completion_enrollment"+ '_overall_' + value.strip() + self.data.get_current_date() + ".csv"
                    print(self.filename)
                    if os.path.isfile(self.filename) != True:
                        print(Districts.options[j].text, Blocks.options[k].text,Cluster.options[m].text, 'csv file not downloaded')
                        count = count + 1
                        self.data.page_loading(self.driver)
                    else:
                        df = pd.read_csv(self.filename)
                        Total_Completed = df['Total Completed'].sum()
                        Total_Enrolled = df['Total Enrolled	'].sum()
                        Certificate_Count = df['Certificate Count'].sum()

                        if Total_Completed == 0:
                            print(Total_Completed, 'Total completed value is not correct ')
                            count = count + 1
                        if Total_Enrolled == 0:
                            print(Total_Enrolled, 'Total Enrolled value is not correct ')
                            count = count + 1
                        if Certificate_Count == 0:
                            print(Certificate_Count, 'Certificate count value is not correct ')
                            count = count + 1
                    os.remove(self.filename)
                return count

    def test_program_with_all_districts(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        Districts = Select(self.driver.find_element_by_id(Data.sar_district))
        program_type = Select(self.driver.find_element_by_name(Data.program))
        time = (self.driver.find_element_by_id('time_range').text).strip()
        for i in range(1, len(program_type.options)):
            program_type.select_by_index(i)
            self.data.page_loading(self.driver)
            cname = program_type.options[i].text
            course = cname.strip()
            for j in range(len(Districts.options)-5,len(Districts.options)):
                Districts.select_by_index(j)
                self.data.page_loading(self.driver)
                self.driver.find_element_by_id(Data.Download).click()
                self.data.page_loading(self.driver)
                dname = self.driver.find_element_by_id(Data.sar_district).get_attribute('value')
                value = dname[4:] + '_'

                self.filename = self.p.get_download_dir()+"/"+"enrollment_completion_"+course.lower()+'_overall'+'_'+value.strip()+self.data.get_current_date()+".csv"
                print(self.filename)
                if os.path.isfile(self.filename) != True:
                    print(program_type.options[i].text, Districts.options[j].text, 'csv file not downloaded')
                    count = count + 1
                    self.data.page_loading(self.driver)
                else:
                    df = pd.read_csv(self.filename)
                    Total_Completed = df['Total Completed'].sum()
                    Total_Enrolled = df['Total Enrolled	'].sum()
                    Certificate_Count = df['Certificate Count'].sum()

                    if Total_Completed == 0:
                        print(Total_Completed,'Total completed value is not correct ')
                        count = count + 1
                    if Total_Enrolled == 0:
                        print(Total_Enrolled,'Total Enrolled value is not correct ')
                        count = count + 1
                    if Certificate_Count == 0:
                        print(Certificate_Count,'Certificate count value is not correct ')
                        count = count + 1
                os.remove(self.filename)
        return count

    def test_program_with_all_blockwise(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        Districts = Select(self.driver.find_element_by_id(Data.sar_district))
        Blocks = Select(self.driver.find_element_by_id(Data.sar_block))
        program_type = Select(self.driver.find_element_by_name(Data.program))
        for i in range(1, len(program_type.options)):
            program_type.select_by_index(i)
            cname = program_type.options[i].text
            course = cname.strip()
            self.data.page_loading(self.driver)
            for j in range(len(Districts.options)-1,len(Districts.options)):
                Districts.select_by_index(j)
                self.data.page_loading(self.driver)
                for k in range(1,len(Blocks.options)):
                    Blocks.select_by_index(k)
                    name = Blocks.options[k].text
                    bname = name.strip()
                    self.data.page_loading(self.driver)
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(4)
                    dname = self.driver.find_element_by_id(Data.sar_block).get_attribute('value')
                    value = dname[3:] + '_'
                    self.filename = self.p.get_download_dir() + "/" + "enrollment_completion_"+course.lower()+"_"+"overall_" + value.strip() + self.data.get_current_date() + ".csv"
                    print(self.filename)
                    if os.path.isfile(self.filename) != True:
                        print(program_type.options[i].text,Districts.options[j].text,Blocks.options[k].text,'csv file not downloaded')
                        count = count + 1
                        self.data.page_loading(self.driver)
                    else:
                        df = pd.read_csv(self.filename)
                        Total_Completed = df['Total Completed'].sum()
                        Total_Enrolled = df['Total Enrolled	'].sum()
                        Certificate_Count = df['Certificate Count'].sum()

                        if Total_Completed == 0:
                            print(Total_Completed, 'Total completed value is not correct ')
                            count = count + 1
                        if Total_Enrolled == 0:
                            print(Total_Enrolled, 'Total Enrolled value is not correct ')
                            count = count + 1
                        if Certificate_Count == 0:
                            print(Certificate_Count, 'Certificate count value is not correct ')
                            count = count + 1
                    os.remove(self.filename)
                return count

    def test_program_with_all_clusterwise(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        Districts = Select(self.driver.find_element_by_id(Data.sar_district))
        Blocks = Select(self.driver.find_element_by_id(Data.sar_block))
        Cluster = Select(self.driver.find_element_by_id(Data.sar_cluster))
        program_type = Select(self.driver.find_element_by(By.NAME,Data.program))
        for i in range(1, len(program_type.options)):
            program_type.select_by_index(i)
            cname = program_type.options[i].text
            course = cname.strip()
            self.data.page_loading(self.driver)
        for j in range(len(Districts.options) - 1, len(Districts.options)):
            Districts.select_by_index(j)
            self.data.page_loading(self.driver)
            for k in range(len(Blocks.options) - 1, len(Blocks.options)):
                Blocks.select_by_index(k)
                self.data.page_loading(self.driver)
                for m in range(1, len(Cluster.options)):
                    Cluster.select_by_index(m)
                    name = Cluster.options[m].text
                    cname = name.strip()
                    self.data.page_loading(self.driver)
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(3)
                    dname = self.driver.find_element_by_id(Data.sar_cluster).get_attribute('value')
                    value = dname[3:] + '_'
                    self.filename = self.p.get_download_dir() + "/" + "enrollment_completion_enrollment"+ '_overall_' + value.strip() + self.data.get_current_date() + ".csv"
                    print(self.filename)
                    if os.path.isfile(self.filename) != True:
                        print(Districts.options[j].text, Blocks.options[k].text,Cluster.options[m].text, 'csv file not downloaded')
                        count = count + 1
                        self.data.page_loading(self.driver)
                    else:
                        df = pd.read_csv(self.filename)
                        Total_Completed = df['Total Completed'].sum()
                        Total_Enrolled = df['Total Enrolled	'].sum()
                        Certificate_Count = df['Certificate Count'].sum()

                        if Total_Completed == 0:
                            print(Total_Completed, 'Total completed value is not correct ')
                            count = count + 1
                        if Total_Enrolled == 0:
                            print(Total_Enrolled, 'Total Enrolled value is not correct ')
                            count = count + 1
                        if Certificate_Count == 0:
                            print(Certificate_Count, 'Certificate count value is not correct ')
                            count = count + 1
                    os.remove(self.filename)
            return count
    #new changes
    def check_selection_of_program_dropdown(self):
        count = 0
        self.driver.find_element(By.XPATH, Data.hyper_link).click()
        time.sleep(3)
        program = Select(self.driver.find_element(By.ID, Data.program_dropdown))
        spents = len(program.options) - 1
        if spents == 0:
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
        if spents == 0:
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
                self.driver.find_element(By.ID, Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + '/'+'enrollment_completion_enrollment_all_district_overall_'+self.data.get_current_date()+'.csv'
                if os.path.isfile(self.filename) != True:
                    print(program_name, 'file is not downloaded')
                    count = count + 1
                else:
                    df = pd.read_csv(self.filename)
                    size = len(df)
                    total_enrolled = df['Expected Enrollment'].sum()
                    avg_time = df['Net Enrollment'].sum()
                    if program_name not in df.values and size != 0:
                        print(program_name, 'program is not having details in downloaded csv file')
                        count = count + 1
                    if int(total_enrolled) == 0 and int(avg_time) == 0:
                        print(total_enrolled, avg_time, 'values are showing wrong!...')
                        count = count + 1
            os.remove(self.filename)
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
                self.driver.find_element(By.ID, Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + '/' + 'enrollment_completion_enrollment_overall_district_' + self.data.get_current_date() + '.csv'
                if os.path.isfile(self.filename) != True:
                    print(course_name, 'file is not downloaded')
                    count = count + 1
                else:
                    df = pd.read_csv(self.filename)
                    size = len(df)
                    total_enrolled = df['Expected Enrollment'].sum()
                    avg_time = df['Net Enrollment'].sum()
                    if course_name not in df.values and size > 0:
                        print(course_name, 'course is not having details in downloaded csv file')
                        count = count + 1
                    if int(total_enrolled) == 0 and int(avg_time) == 0:
                        print(total_enrolled, avg_time, 'values are showing wrong!...')
                        count = count + 1
            os.remove(self.filename)
        return count



    def check_logout_from_report(self):
        count = 0
        self.data= GetData()
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
            self.data.navigate_to_tpd_user_on_boarding_report()
            if 'enrollment-progress' in self.driver.current_url:
                print(" User OnBoarding report home page is displayed ")
            else:
                print("Navigation to User OnBoarding Report is failed !")
                count = count + 1
        return count

