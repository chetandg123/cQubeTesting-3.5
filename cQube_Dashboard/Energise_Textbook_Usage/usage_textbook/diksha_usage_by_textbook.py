import csv
import os
import re
import time

from selenium.webdriver.support.select import Select

from Locators.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class diksha_usage_textbook_report():
    def __init__(self, driver):
        self.msg = None
        self.data = None
        self.driver = driver

    def test_hyperlink(self):
        self.data = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        district = Select(self.driver.find_element_by_name('timePeriod'))
        district.select_by_index(2)
        self.data.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)

    def download_csv_file(self):
        self.data = GetData()
        count = 0
        p = pwd()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        fname = file_extention()
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        self.filename = p.get_download_dir() + '/' + fname.location_textbook() + self.data.get_current_date() + '.csv'
        print(self.filename)
        self.data.page_loading(self.driver)
        if os.path.isfile(self.filename) == False:
            print('Diksha usage by course chart csv file is not downloded ')
            count = count + 1
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                contents = 0
                for row in csv.reader(fin):
                    contents += int(row[0])
                total = self.driver.find_element_by_id("totalCount").text
                usage = re.sub('\D', "", total).replace(',', '')
                if int(contents) != int(usage):
                    print('Total content usage mis match found')
                    count = count + 1
            os.remove(self.filename)
        return count

    def test_last30_days(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        timeperiod = Select(self.driver.find_element_by_name('timePeriod'))
        # timeperiod.select_by_visible_text(' Last 30 Days ')
        timeperiod.select_by_index(2)
        self.data.page_loading(self.driver)
        if self.msg.no_data_available() or "No data found" in self.driver.page_source:
            print("Last 30 days does not having data")
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + "/" + 'usage_by_textbook_all_' + self.data.get_current_date() + ".csv"
            print(self.filename)
            if not os.path.isfile(self.filename):
                print("Diksha course type of  last 30 days data csv file not downloaded")
            else:
                with open(self.filename) as fin:
                    csv_reader = csv.reader(fin, delimiter=',')
                    header = next(csv_reader)
                    contentplays = 0
                    for row in csv.reader(fin):
                        contentplays += int(row[0])
                    play_count = self.driver.find_element_by_id('totalCount').text
                    pc = re.sub('\D', "", play_count)
                    if int(pc) != int(contentplays):
                        print("Course type of last 30 days has difference between screen count value and csv file "
                              "count ")
                        count = count + 1
                    self.data.page_loading(self.driver)
                os.remove(self.filename)
        return count

    def test_last7_days(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        timeperiod = Select(self.driver.find_element_by_name('timePeriod'))
        # timeperiod.select_by_visible_text(' Last 30 Days ')
        timeperiod.select_by_index(3)
        self.data.page_loading(self.driver)
        if self.msg.no_data_available() or "No data found" in self.driver.page_source:
            print("Last 7 days does not having data")
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + "/" + 'usage_by_textbook_all_' + self.data.get_current_date() + ".csv"
            print(self.filename)
            if not os.path.isfile(self.filename):
                print("Diksha course type of  last 30 days data csv file not downloaded")
            else:
                with open(self.filename) as fin:
                    csv_reader = csv.reader(fin, delimiter=',')
                    header = next(csv_reader)
                    contentplays = 0
                    for row in csv.reader(fin):
                        contentplays += int(row[0])
                    play_count = self.driver.find_element_by_id('totalCount').text
                    pc = re.sub('\D', "", play_count)
                    if int(pc) != int(contentplays):
                        print(
                            "Course type of last 30 days has difference between screen count value and csv file count ")
                        count = count + 1
                    self.data.page_loading(self.driver)
                os.remove(self.filename)
        return count

    def test_last_day(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        timeperiod = Select(self.driver.find_element_by_name('timePeriod'))
        # timeperiod.select_by_visible_text(' Last 30 Days ')
        timeperiod.select_by_index(3)
        self.data.page_loading(self.driver)
        if self.msg.no_data_available() or "No data found" in self.driver.page_source:
            print("Last day does not having data")
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + "/" + 'usage_by_textbook_all_' + self.data.get_current_date() + ".csv"
            print(self.filename)
            if not os.path.isfile(self.filename):
                print("Diksha course type of  last 30 days data csv file not downloaded")
            else:
                with open(self.filename) as fin:
                    csv_reader = csv.reader(fin, delimiter=',')
                    header = next(csv_reader)
                    contentplays = 0
                    for row in csv.reader(fin):
                        contentplays += int(row[0])
                    play_count = self.driver.find_element_by_id('totalCount').text
                    pc = re.sub('\D', "", play_count)
                    if int(pc) != int(contentplays):
                        print(
                            "Course type of last 30 days has difference between screen count value and csv file count ")
                        count = count + 1
                    self.data.page_loading(self.driver)
                os.remove(self.filename)
        return count

    def test_homeicon(self):
        self.data = GetData()
        count = 0
        self.data.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        choose = Select(self.driver.find_element_by_name('timePeriod'))
        choose.select_by_index(2)
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.data.page_loading(self.driver)
        self.data.navigate_to_column_textbook()
        time.sleep(2)

    def test_homebutton(self):
        count = 0
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.data.page_loading(self.driver)
        # self.data.navigate_to_column_course()
        self.driver.find_element_by_id('dcc').click()
        self.data.page_loading(self.driver)
        if 'usage-by-course' in self.driver.current_url:
            print('Home button is working')
        else:
            print("Home button is not working ")
            count = count + 1
        return count

    def test_logout(self):
        self.data = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.logout).click()
        loginpage = self.driver.title
        self.data.login_cqube(self.driver)
        print("Logout button is working as expected.. now relogging to cQube ")
        self.data.page_loading(self.driver)
        self.data.navigate_to_column_textbook()
        self.data.page_loading(self.driver)
        return loginpage

    def test_overall_rawfile_download(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        times = Select(self.driver.find_element_by_name('timePeriod'))
        times.select_by_index(1)
        if " No Data Available " or "No data found" in self.driver.page_source:
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
        if " No Data Available " or "No data found" in self.driver.page_source:
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
        if " No Data Available " or "No data found" in self.driver.page_source:
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
        if " No Data Available " or "No data found" in self.driver.page_source:
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
