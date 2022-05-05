import csv
import os
import re
import time

from selenium.webdriver.support.select import Select

from Locators.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class tpd_enrollment_completion_reports():
    def __init__(self, driver):
        self.msg = None
        self.data = None
        self.driver = driver

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
        # course_type = Select(self.driver.find_element_by_id(Data.coursetype))
        # course_type.select_by_visible_text(' Enrollment ')
        # course_type.select_by_index(1)
        self.data.page_loading(self.driver)
        # ctype = (self.driver.find_element_by_id(Data.coursetype).text).strip()
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        # timeseries.select_by_visible_text(' Overall ')
        timeseries.select_by_index(1)
        self.data.page_loading(self.driver)
        times = (self.driver.find_element_by_name(Data.timeperiods).text).strip()
        if self.msg.no_data_available() in self.driver.page_source:
            print('No Data Available for overall')
            count = 0
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + '/' + 'enrollment_completion_enrollment_all_district_overall_' + self.data.get_current_date() + '.csv'
            print(self.filename)
            self.data.page_loading(self.driver)
            collnames = Select(self.driver.find_element_by_id(Data.coll_names))
            counter = len(collnames.options) - 1
            for i in range(len(collnames.options), len(collnames.options) - 5):
                collnames.select_by_index(i)
                self.data.page_loading(self.driver)
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
        # course_type = Select(self.driver.find_element_by_id(Data.coursetype))
        # # course_type.select_by_visible_text(' Enrollment ')
        # course_type.select_by_index(1)
        self.data.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        # timeseries.select_by_visible_text(' Last Day ')
        timeseries.select_by_index(4)
        self.data.page_loading(self.driver)
        counter = 0
        if self.msg.no_data_available() in self.driver.page_source:
            print('No Data Available for last day')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            times = (self.driver.find_element_by_name(Data.timeperiods).text).strip()
            # ctype = (self.driver.find_element_by_id(Data.coursetype).text).strip()
            self.filename = self.p.get_download_dir() + '/' + 'tpd_enrollment_all_district_last_day_' + self.data.get_current_date() + '.csv'
            self.data.page_loading(self.driver)
            collnames = Select(self.driver.find_element_by_id(Data.coll_names))
            counter = len(collnames.options) - 1
            for i in range(len(collnames.options) - 5, len(collnames.options) - 1):
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
        # course_type = Select(self.driver.find_element_by_id(Data.coursetype))
        # # course_type.select_by_visible_text(' Enrollment ')
        # course_type.select_by_index(1)
        self.data.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        # timeseries.select_by_visible_text(' Last 7 Days ')
        timeseries.select_by_index(3)
        self.data.page_loading(self.driver)
        if self.msg.no_data_available() in self.driver.page_source:
            print('No Data Available for last 7 days')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            times = (self.driver.find_element_by_name(Data.timeperiods).text).strip()
            # ctype = (self.driver.find_element_by_id(Data.coursetype).text).strip()
            self.filename = self.p.get_download_dir() + '/' + 'tpd_enrollment_all_district_last_7_days_' + self.data.get_current_date() + '.csv'
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
        # course_type = Select(self.driver.find_element_by_id(Data.coursetype))
        # # course_type.select_by_visible_text(' Enrollment ')
        # course_type.select_by_index(1)
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        # timeseries.select_by_visible_text(' Last 30 Days ')
        timeseries.select_by_index(2)
        self.data.page_loading(self.driver)
        if self.msg.no_data_available() in self.driver.page_source:
            print('No Data Available for last 30 days')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            times = (self.driver.find_element_by_name(Data.timeperiods).text).strip()
            # ctype = (self.driver.find_element_by_id(Data.coursetype).text).strip()
            self.filename = self.p.get_download_dir() + '/' + 'enrollment_completion_enrollment_all_district_last_30_days_' + self.data.get_current_date() + '.csv'
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
            # return counter, count

    def test_completion_overall(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        # course_type = Select(self.driver.find_element_by_id(Data.coursetype))
        # course_type.select_by_visible_text(' Completion ')
        # course_type.select_by_index(2)
        self.data.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        # timeseries.select_by_visible_text(' Overall ')
        timeseries.select_by_index(1)
        self.data.page_loading(self.driver)
        if self.msg.no_data_available() in self.driver.page_source:
            print('No Data Available for Over All')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(5)
            times = (self.driver.find_element_by_name(Data.timeperiods).text).strip()
            self.filename = self.p.get_download_dir() + '/' + 'enrollment_completion_completion_all_district_overall_' + self.data.get_current_date() + '.csv'
            print(self.filename)
            self.data.page_loading(self.driver)
            collnames = Select(self.driver.find_element_by_id(Data.coll_names))
            counter = len(collnames.options) - 1
            for i in range(1, len(collnames.options) - 1):
                collnames.select_by_index(i)
                self.data.page_loading(self.driver)
            if os.path.isfile(self.filename) != True:
                print('Completion Over all csv file is not downloaded ')
                count = count + 1
            self.data.page_loading(self.driver)
            os.remove(self.filename)
            return counter, count

    def test_completion_last_day(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        course_type = Select(self.driver.find_element_by_id(Data.coursetype))
        # course_type.select_by_visible_text(' Completion ')
        course_type.select_by_index(2)
        self.data.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        # timeseries.select_by_visible_text(' Last Day ')
        timeseries.select_by_index(1)
        self.data.page_loading(self.driver)
        if self.msg.no_data_available() in self.driver.page_source:
            print('No Data Available for last day')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            times = (self.driver.find_element_by_name(Data.timeperiods).text).strip()
            ctype = (self.driver.find_element_by_id(Data.coursetype).text).strip()
            self.filename = self.p.get_download_dir() + '/' + 'tpd_' + ctype + '_all_district_last_day' + '_' + self.data.get_current_date() + '.csv'
            print(self.filename)
            self.data.page_loading(self.driver)
            collnames = Select(self.driver.find_element_by_id(Data.coll_names))
            counter = len(collnames.options) - 1
            for i in range(1, len(collnames.options) - 1):
                collnames.select_by_index(i)
                self.data.page_loading(self.driver)
            if os.path.isfile(self.filename) != True:
                print('Completion last day csv file is not downloaded ')
                count = count + 1
            self.data.page_loading(self.driver)
            os.remove(self.filename)
            # return counter,count

    def test_completion_last7_days(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        course_type = Select(self.driver.find_element_by_id(Data.coursetype))
        # course_type.select_by_visible_text(' Completion ')
        course_type.select_by_index(2)
        self.data.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        # timeseries.select_by_visible_text(' Last 7 Days ')
        timeseries.select_by_index(2)
        self.data.page_loading(self.driver)
        if self.msg.no_data_available() in self.driver.page_source:
            print('No Data Available for last 7 days')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(4)
            times = (self.driver.find_element_by_name(Data.timeperiods).text).strip()
            ctype = (self.driver.find_element_by_id(Data.coursetype).text).strip()
            self.filename = self.p.get_download_dir() + '/' + 'tpd_' + ctype + '_all_district_last_7_days' + '_' + self.data.get_current_date() + '.csv'
            print(self.filename)
            self.data.page_loading(self.driver)
            collnames = Select(self.driver.find_element_by_id(Data.coll_names))
            counter = len(collnames.options) - 1
            for i in range(1, len(collnames.options) - 1):
                collnames.select_by_index(i)
                self.data.page_loading(self.driver)
            if os.path.isfile(self.filename) != True:
                print('Completion last 7 days csv file is not downloaded ')
                count = count + 1
            self.data.page_loading(self.driver)
            os.remove(self.filename)
            # return counter, count

    def test_completion_last30_days(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        course_type = Select(self.driver.find_element_by_id(Data.coursetype))
        # course_type.select_by_visible_text(' Completion ')
        course_type.select_by_index(2)
        self.data.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        # timeseries.select_by_visible_text(' Last 30 Days ')
        timeseries.select_by_index(3)
        self.data.page_loading(self.driver)
        if self.msg.no_data_available() in self.driver.page_source:
            print('No Data Available for last 30 days')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            times = (self.driver.find_element_by_name(Data.timeperiods).text).strip()
            ctype = course_type.first_selected_option
            self.filename = self.p.get_download_dir() + '/' + 'enrollment_completion_completion_all_district_last_30_days_' + self.data.get_current_date() + '.csv'
            print(self.filename)
            self.data.page_loading(self.driver)
            collnames = Select(self.driver.find_element_by_id(Data.coll_names))
            counter = len(collnames.options) - 1
            for i in range(1, len(collnames.options) - 1):
                collnames.select_by_index(i)
                self.data.page_loading(self.driver)
            if os.path.isfile(self.filename) != True:
                print('Completion last 30 days csv file is not downloaded ')
                count = count + 1
            self.data.page_loading(self.driver)
            os.remove(self.filename)
        return count

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
        self.driver.find_element_by_id(Data.homeicon).click()
        print('checked with homeicon function is working ')
        self.data.page_loading(self.driver)
        # return  present

    def test_homebtn_funtion(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.data.page_loading(self.driver)
        if 'dashboard' in self.driver.current_url:
            print('Home button is working ')
        else:
            print('Homebtn is not working ')
            count = count + 1
        self.data.page_loading(self.driver)
        self.data.navigate_to_tpd_enrollment_report()
        self.data.page_loading(self.driver)
        return count

    def test_hyperlink_function(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        # timeseries.select_by_visible_text(' Last 7 Days ')
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
        self.filename = self.p.get_download_dir() + '/' + "enrollment_completion_enrollment_all_district_overall_" + self.data.get_current_date() + '.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            print('Districtwise csv file is not downloaded')
            count = count + 1
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                enrolls = 0
                for row in csv.reader(fin):
                    enrolls += int(row[6].replace(',', ''))
                totalenrollment = self.driver.find_element_by_id("totalCount").text
                enrol = re.sub('\D', "", totalenrollment)
                if int(enrol) != int(enrolls):
                    print(int(enrol) != int(enrolls), 'mis match found at enrollment count')
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
            for j in range(len(Districts.options) - 5, len(Districts.options)):
                Districts.select_by_index(j)
                self.data.page_loading(self.driver)
                self.driver.find_element_by_id(Data.Download).click()
                self.data.page_loading(self.driver)
                dname = self.driver.find_element_by_id(Data.sar_district).get_attribute('value')
                value = dname[4:] + '_'

                self.filename = self.p.get_download_dir() + "/" + "enrollment_completion_" + course.lower() + '_overall' + '_' + value.strip() + self.data.get_current_date() + ".csv"
                print(self.filename)
                if os.path.isfile(self.filename) != True:
                    print(course_type.options[i].text, Districts.options[j].text, 'csv file not downloaded')
                    count = count + 1
                    self.data.page_loading(self.driver)
                else:
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        enrolls = 0
                        for row in csv.reader(fin):
                            enrolls += int(row[8].replace(',', ''))
                        totalenrollment = self.driver.find_element_by_id("totalCount").text
                        enrol = re.sub('\D', "", totalenrollment)
                        if int(enrol) != int(enrolls):
                            print(int(enrol) != int(enrolls), 'mis match found at enrollment count')
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
            for j in range(len(Districts.options) - 1, len(Districts.options)):
                Districts.select_by_index(j)
                self.data.page_loading(self.driver)
                for k in range(1, len(Blocks.options)):
                    Blocks.select_by_index(k)
                    name = Blocks.options[k].text
                    bname = name.strip()
                    self.data.page_loading(self.driver)
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(4)
                    dname = self.driver.find_element_by_id(Data.sar_block).get_attribute('value')
                    value = dname[3:] + '_'
                    # times = (self.driver.find_element_by_id('time_range').text).strip()

                    self.filename = self.p.get_download_dir() + "/" + "enrollment_completion_" + course.lower() + "_" + "overall_" + value.strip() + self.data.get_current_date() + ".csv "
                    print(self.filename)
                    if os.path.isfile(self.filename) != True:
                        print(course_type.options[i].text, Districts.options[j].text, Blocks.options[k].text,
                              'csv file not downloaded')
                        count = count + 1
                        self.data.page_loading(self.driver)
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            next(csv_reader)
                            enrolls = 0
                            for row in csv.reader(fin):
                                enrolls += int(row[10].replace(',', ''))
                            totalenrollment = self.driver.find_element_by_id("totalCount").text
                            enrol = re.sub('\D', "", totalenrollment)
                            if int(enrol) != int(enrolls):
                                print(int(enrol) != int(enrolls), 'mis match found at enrollment count')
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
        # for i in range(1, len(course_type.options)):
        #     course_type.select_by_index(i)
        #     cname = course_type.options[i].text
        #     course = cname.strip()
        #     self.data.page_loading(self.driver)
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
                    # times = (self.driver.find_element_by_id('time_range').text).strip()

                    self.filename = self.p.get_download_dir() + "/" + "enrollment_completion_enrollment" + '_overall_' + value.strip() + self.data.get_current_date() + ".csv"
                    print(self.filename)
                    if os.path.isfile(self.filename) != True:
                        print(Districts.options[j].text, Blocks.options[k].text, Cluster.options[m].text,
                              'csv file not downloaded')
                        count = count + 1
                        self.data.page_loading(self.driver)
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            enrolls = 0
                            for row in csv.reader(fin):
                                enrolls += int(row[12].replace(',', ''))
                            totalenrollment = self.driver.find_element_by_id("totalCount").text
                            enrol = re.sub('\D', "", totalenrollment)
                            if int(enrol) != int(enrolls):
                                print(int(enrol) != int(enrolls), 'mis match found at enrollment count')
                                count = count + 1
                    os.remove(self.filename)
                return count

    def click_on_logout_btn(self):
        self.data = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.logout).click()
        self.data.page_loading(self.driver)
        if 'Log in to cQube' in self.driver.title:
            print('Logout button is working ')
        else:
            print('Logout is not working')
            count = count + 1
        self.data.login_cqube(self.driver)
        time.sleep(2)
        self.data.navigate_to_tpd_enrollment_report()
        self.data.page_loading(self.driver)
        return count

    def test_overall_rawfile_download(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        times = Select(self.driver.find_element_by_name('timePeriod'))
        times.select_by_index(1)
        if " No Data Available " in self.driver.page_source:
            print(times.first_selected_option.text, "is not having data..")
            return count
        else:
            self.driver.find_element_by_id('rawDownload').click()
            time.sleep(35)
            timeperiod = (times.first_selected_option.text).lower()
            self.filename = self.p.get_download_dir() + "/" + timeperiod + ".csv"
            if os.path.isfile(self.filename) != True:
                print(timeperiod, 'raw file is not downloaded')
                count = count + 1
            else:
                print(timeperiod, 'raw file is downloaded..')
                os.remove(self.filename)
            return count

    def test_last_30_days_rawfile_download(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        times = Select(self.driver.find_element_by_name('timePeriod'))
        times.select_by_index(2)
        time.sleep(3)
        if " No Data Available " in self.driver.page_source:
            print(times.first_selected_option.text, "is not having data..")
            return count
        else:
            self.driver.find_element_by_id('rawDownload').click()
            time.sleep(35)
            timeperiod = (times.first_selected_option.text.replace("", "_")).lower()
            self.filename = self.p.get_download_dir() + "/last_30_days" + ".csv"
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print(timeperiod, 'raw file is not downloaded')
                count = count + 1
            else:
                print(timeperiod, 'raw file is downloaded..')
                os.remove(self.filename)
            return count

    def test_last_7_days_rawfile_download(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        times = Select(self.driver.find_element_by_name('timePeriod'))
        times.select_by_index(3)
        time.sleep(3)
        if " No Data Available " in self.driver.page_source:
            print(times.first_selected_option.text, "is not having data..")
            return count
        else:
            self.driver.find_element_by_id('rawDownload').click()
            time.sleep(35)
            timeperiod = (times.first_selected_option.text.replace("", "_")).lower()
            self.filename = self.p.get_download_dir() + "/last_7_days" + ".csv"
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print(timeperiod, 'raw file is not downloaded')
                count = count + 1
            else:
                print(timeperiod, 'raw file is downloaded..')
                os.remove(self.filename)
            return count

    def test_last_day_rawfile_download(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        times = Select(self.driver.find_element_by_name('timePeriod'))
        times.select_by_index(4)
        time.sleep(5)
        if " No Data Available " in self.driver.page_source:
            print(times.first_selected_option.text, "is not having data..")
            return count
        else:
            self.driver.find_element_by_id('rawDownload').click()
            time.sleep(35)
            timeperiod = (times.first_selected_option.text.replace("", "_")).lower()
            self.filename = self.p.get_download_dir() + "/last_day" + ".csv"
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print(timeperiod, 'raw file is not downloaded')
                count = count + 1
            else:
                print(timeperiod, 'raw file is downloaded..')
                os.remove(self.filename)
            return count
