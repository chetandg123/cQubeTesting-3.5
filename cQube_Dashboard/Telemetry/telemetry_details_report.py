import os
import time

from selenium.webdriver.support.select import Select

from Locators.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class telemetry_map_report():
    def __init__(self,driver):
        self.driver = driver

    def test_last7day_records(self):
        self.data = GetData()
        self.data.page_loading(self.driver)
        period = Select(self.driver.find_element_by_id('period'))
        # period.select_by_visible_text(' Last 7 Days ')
        period.select_by_index(3)
        self.data.page_loading(self.driver)
        if 'No data found' in self.driver.page_source:
            print('Selected catagory  has no records')
        else:
            self.driver.find_element_by_id('blockbtn').click()
            markers = self.driver.find_elements_by_class_name(Data.dots)
            bcount = len(markers)
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id('clusterbtn').click()
            markers = self.driver.find_elements_by_class_name(Data.dots)
            ccount = len(markers)
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id('schoolbtn').click()
            markers = self.driver.find_elements_by_class_name(Data.dots)
            scount = len(markers)
            self.data.page_loading(self.driver)
            return bcount, ccount, scount

    def test_lastday_records(self):
        self.data = GetData()
        self.data.page_loading(self.driver)
        period = Select(self.driver.find_element_by_id('period'))
        # period.select_by_visible_text(' Last Day ')
        period.select_by_index(3)
        self.data.page_loading(self.driver)
        if 'No data found' in self.driver.page_source:
            print('Selected catagory  has no records')
        else:
            self.driver.find_element_by_id('blockbtn').click()
            markers = self.driver.find_elements_by_class_name(Data.dots)
            bcount = len(markers)
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id('clusterbtn').click()
            markers = self.driver.find_elements_by_class_name(Data.dots)
            ccount = len(markers)
            self.data.page_loading(self.driver)
            scount=0
            self.driver.find_element_by_id('schoolbtn').click()
            if 'no data found' in self.driver.page_source:
                print("School wise telemetry data is not exist!")
            else:
                markers = self.driver.find_elements_by_class_name(Data.dots)
                scount = len(markers)
                self.data.page_loading(self.driver)
            return bcount, ccount, scount

    def test_lastmonth_records(self):
        self.data = GetData()
        self.data.page_loading(self.driver)
        period = Select(self.driver.find_element_by_id('period'))
        # period.select_by_visible_text(' Last 30 Days ')
        period.select_by_index(2)
        self.data.page_loading(self.driver)
        if 'No data found' in self.driver.page_source:
            print('Selected catagory  has no records')
        else:
            self.driver.find_element_by_id('blockbtn').click()
            markers = self.driver.find_elements_by_class_name(Data.dots)
            bcount = len(markers)
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id('clusterbtn').click()
            markers = self.driver.find_elements_by_class_name(Data.dots)
            ccount = len(markers)
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id('schoolbtn').click()
            markers = self.driver.find_elements_by_class_name(Data.dots)
            scount = len(markers)
            self.data.page_loading(self.driver)
            return bcount, ccount, scount
    def test_overall_records(self):
        self.data = GetData()
        self.data.page_loading(self.driver)
        period = Select(self.driver.find_element_by_id('period'))
        # period.select_by_visible_text(' Over All ')
        period.select_by_index(1)
        self.data.page_loading(self.driver)
        if 'No data found' in self.driver.page_source:
            print('Selected catagory  has no records')
        else:
            self.driver.find_element_by_id('blockbtn').click()
            self.data.page_loading(self.driver)
            markers = self.driver.find_elements_by_class_name(Data.dots)
            bcount = len(markers)
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id('clusterbtn').click()
            self.data.page_loading(self.driver)
            markers = self.driver.find_elements_by_class_name(Data.dots)
            ccount = len(markers) - 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id('schoolbtn').click()
            self.data.page_loading(self.driver)
            markers = self.driver.find_elements_by_class_name(Data.dots)
            scount = len(markers)
            self.data.page_loading(self.driver)
            return bcount,ccount,scount

    def test_last_7_records(self):
        self.data = GetData()
        self.p = pwd()
        self.fname = file_extention()
        self.data.page_loading(self.driver)
        period = Select(self.driver.find_element_by_id('period'))
        # period.select_by_visible_text(' Last 7 Days ')
        period.select_by_index(3)
        self.data.page_loading(self.driver)
        markers = self.driver.find_elements_by_class_name(Data.dots)
        count = len(markers)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(4)
        self.filename = self.p.get_download_dir() + '/' + self.fname.telemetry_last7days()+self.data.get_current_date()+'.csv'
        print(self.filename)
        file = os.path.isfile(self.filename)
        self.data.page_loading(self.driver)
        os.remove(self.filename)
        return file





