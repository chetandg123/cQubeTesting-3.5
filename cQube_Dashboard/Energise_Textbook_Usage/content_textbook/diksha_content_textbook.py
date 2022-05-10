import csv
import os
import time

from selenium.webdriver.support.select import Select

from Locators.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData

'''Script developed to test the each functionalities of web element like buttons , charts , dropdowns , chart 
etc '''


class Diksha_Content_Textbook_Report():

    def __init__(self, driver):
        self.p = None
        self.data = None
        self.driver = driver

    def test_navigation(self):
        self.data = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.data.page_loading(self.driver)
        self.data.navigate_to_diksha_content_textbook()
        self.data.page_loading(self.driver)
        if "usage-by-textbook-content" in self.driver.current_url:
            print("Diksha usage-by-textbook-content page is Displayed")
        else:
            print("Diksha usage-by-textbook-content page is not exist ")
            count = count + 1
        self.data.page_loading(self.driver)
        return count

    def test_hyperlink(self):
        self.data = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        time.sleep(5)
        district = Select(self.driver.find_element_by_id('choose_dist'))
        district.select_by_index(5)
        self.data.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)

    def test_alldata_districts(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        self.filename = self.p.get_download_dir() + "/" + 'usage_by_textbook_content_all_' + self.data.get_current_date() + '.csv'
        print(self.filename)
        file = os.path.isfile(self.filename)
        self.data.page_loading(self.driver)
        with open(self.filename) as fin:
            csv_reader = csv.reader(fin, delimiter=',')
            header = next(csv_reader)
            data = list(csv_reader)
            row_count = len(data)
        os.remove(self.filename)
        tablecount = self.driver.find_elements_by_tag_name('tr')
        int(len(tablecount)) - 2
        time.sleep(2)
        # if row_count != records:
        #     print("records count mismatch in downloaded file and table records")
        #     count = count + 1
        return count

    def test_each_districts(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        times = Select(self.driver.find_element_by_name('timePeriod'))
        times.select_by_index('3')
        self.data.page_loading(self.driver)
        if self.msg.no_data_found() in self.driver.page_source:
            print("Last 7 days showing no records")
        else:
            districts = Select(self.driver.find_element_by_id('choose_dist'))
            i = 0
            for x in range(len(districts.options) - 2, len(districts.options)):
                time.sleep(1)
                districts.select_by_index(x)
                name = districts.options[x].text
                time.sleep(2)
                names = name.strip()
                self.data.page_loading(self.driver)
                if self.msg.no_data_found() in self.driver.page_source:
                    print(districts.options[x].text, " does not last 7 days records")
                else:
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(3)
                    self.filename = self.p.get_download_dir() + "/" + 'usage_by_textbook_content_last_7_days_' + self.data.get_current_date() + ".csv"
                    print(self.filename)
                    file = os.path.isfile(self.filename)
                    self.data.page_loading(self.driver)
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        data = list(csv_reader)
                        row_count = len(data)
                    os.remove(self.filename)
                    tablecount = self.driver.find_elements_by_tag_name('tr')
                    records = int(len(tablecount)) - 2
                    time.sleep(2)
                    # if row_count != records:
                    #     print(districts.options[x].text, "records count mismatch in downloaded file and table records")
                    #     count = count + 1
                    # i = i + 1
        return count

    def test_each_districts(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        times = Select(self.driver.find_element_by_name('timePeriod'))
        # times.select_by_visible_text(' Last Day ')
        times.select_by_index(4)
        self.data.page_loading(self.driver)
        print(times.first_selected_option)
        if self.msg.no_data_found() in self.driver.page_source:
            print("Last days showing no records")
        else:
            districts = Select(self.driver.find_element_by_id('choose_dist'))
            i = 0
            for x in range(len(districts.options) - 2, len(districts.options)):
                time.sleep(1)
                districts.select_by_index(x)
                name = districts.options[x].text
                names = name.strip()
                self.data.page_loading(self.driver)
                time.sleep(2)
                if self.msg.no_data_found() in self.driver.page_source:
                    print(districts.options[x].text, " does not last day records")
                else:
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(3)
                    self.filename = self.p.get_download_dir() + "/" + 'usage_by_textbook_content_last_day_' + self.data.get_current_date() + ".csv"
                    print(self.filename)
                    file = os.path.isfile(self.filename)
                    self.data.page_loading(self.driver)
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        data = list(csv_reader)
                        row_count = len(data)
                    os.remove(self.filename)
                    tablecount = self.driver.find_elements_by_tag_name('tr')
                    records = int(len(tablecount)) - 2
                    time.sleep(2)
                    # if row_count!= records:
                    #     print(districts.options[x].text ,"records count mismatch in downloaded file and table records")
                    #     count = count + 1
                    # i = i + 1
        return count

    def test_each_districts(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        times = Select(self.driver.find_element_by_name('timePeriod'))
        # times.select_by_visible_text(" Last 30 Days ")
        times.select_by_index(2)
        self.data.page_loading(self.driver)
        if self.msg.no_data_found() in self.driver.page_source:
            print("Last 30 day showing no records")
        else:
            districts = Select(self.driver.find_element_by_id('choose_dist'))
            i = 0
            for x in range(len(districts.options) - 10, len(districts.options)):
                time.sleep(1)
                districts.select_by_index(x)
                name = districts.options[x].text
                names = name.strip()
                self.data.page_loading(self.driver)
                if self.msg.no_data_found() in self.driver.page_source:
                    print(districts.options[x].text, " does not last 30 days records")
                else:
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(3)
                    self.filename = self.p.get_download_dir() + "/" + 'usage_by_textbook_content_last_30_days_' + self.data.get_current_date() + ".csv"
                    print(self.driver)
                    file = os.path.isfile(self.filename)
                    self.data.page_loading(self.driver)
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        data = list(csv_reader)
                        row_count = len(data)
                    os.remove(self.filename)
                    tablecount = self.driver.find_elements_by_tag_name('tr')
                    records = int(len(tablecount)) - 2
                    time.sleep(2)
                    # if int(row_count) != records:
                    #     print(districts.options[x].text, "records count mismatch in downloaded file and table records")
                    #     count = count + 1
                    # i = i + 1
        return count

    def test_districts(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        times = Select(self.driver.find_element_by_name('timePeriod'))
        # times.select_by_visible_text(' Last Day ')
        times.select_by_index(3)
        print(times.first_selected_option)
        self.data.page_loading(self.driver)
        if self.msg.no_data_found() in self.driver.page_source:
            print("Last days records")
        else:
            districts = Select(self.driver.find_element_by_id('choose_dist'))
            for x in range(len(districts.options) - 3, len(districts.options)):
                time.sleep(1)
                districts.select_by_index(x)
                self.data.page_loading(self.driver)
                if self.msg.no_data_found() in self.driver.page_source:
                    print(districts.options[x].text, " does not last day records")
                    count = count + 1
        return count

    def test_districts(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        times = Select(self.driver.find_element_by_name('timePeriod'))
        # times.select_by_visible_text(' Last 7 Days ')
        times.select_by_index(3)
        time.sleep(2)
        if self.msg.no_data_found() in self.driver.page_source:
            print("Last 7 days records")
        else:
            districts = Select(self.driver.find_element_by_id('choose_dist'))
            for x in range(len(districts.options) - 3, len(districts.options)):
                time.sleep(1)
                districts.select_by_index(x)
                self.data.page_loading(self.driver)
                if self.msg.no_data_found() in self.driver.page_source:
                    print(districts.options[x].text, " does not last week records")
                    count = count + 1
        return count

    def test_districts(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        times = Select(self.driver.find_element_by_name('timePeriod'))
        # times.select_by_visible_text(' Last 30 Days ')
        times.select_by_index(2)
        self.data.page_loading(self.driver)
        if self.msg.no_data_found() in self.driver.page_source:
            print("Last 30 days records")
        else:
            districts = Select(self.driver.find_element_by_id('choose_dist'))
            for x in range(len(districts.options) - 3, len(districts.options)):
                time.sleep(1)
                districts.select_by_index(x)
                self.data.page_loading(self.driver)
                if self.msg.no_data_found() in self.driver.page_source:
                    print(districts.options[x].text, " does not last month records")
                    count = count + 1
            self.data.page_loading(self.driver)
        return count

    def test_homeicon(self):
        self.data = GetData()
        count = 0
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        district = Select(self.driver.find_element_by_id('choose_dist'))
        district.select_by_index(4)
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.homeicon).click()
        self.data.page_loading(self.driver)

    def test_homebutton(self):
        self.data = GetData()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.data.page_loading(self.driver)
        self.data.navigate_to_diksha_content_textbook()
        self.data.page_loading(self.driver)

    def test_searchbox(self):
        count = 0
        self.data = GetData()
        self.data.page_loading(self.driver)
        search = self.driver.find_element_by_xpath("//*[@id='table_filter']/label/input")
        search.send_keys('Mathematics')
        self.data.page_loading(self.driver)
        if 'Mathematics' in self.driver.page_source:
            print("Search box is working ")
        else:
            print('Search box is not working')
            count = count + 1
        return count

    def test_tablevalue(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='table_wrapper']/div/div[1]/div/table/thead/tr/th[1]").click()
        self.p.page_loading(self.driver)
        values = self.driver.find_elements_by_xpath("//th[2]")
        for i in values:
            print(i.get_attribute("aria-sort"))

        self.p.page_loading(self.driver)
        self.driver.find_element_by_xpath("//*[@id='table_wrapper']/div/div[1]/div/table/thead/tr/th[1]").click()
        self.p.page_loading(self.driver)
        value = self.driver.find_elements_by_xpath("//th[2]")
        for i in value:
            print(i.get_attribute("aria-sort"))
        self.p.page_loading(self.driver)

    def test_logout(self):
        self.data = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.logout).click()
        time.sleep(2)
        loginpage = self.driver.title
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)
        self.data.navigate_to_diksha_content_textbook()
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
