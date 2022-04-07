import csv
import os
import re
import time

import pandas as pd
from selenium.webdriver.support.select import Select

from Locators.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class pat_exception_report():

    def __init__(self,driver):
        self.driver = driver
        self.filename =''


    def test_icon(self):
        self.data = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('patExcpt').click()
        self.data.page_loading(self.driver)
        if "pat-exception" in self.driver.current_url:
            print("PAT exception report page is dispayed")
        else:
            print("PAT exception icon is not working")
            count = count + 1
        return count


    def click_on_logout(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(2)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.logout).click()
        print(self.driver.title)
        return self.driver.title

    def test_click_on_dashboard(self):
        count = 0
        cal = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        cal.navigate_to_pat_exception()
        cal.page_loading(self.driver)
        if 'pat-exception' in self.driver.current_url:
            print("PAT exception report is present ")
        else:
            print("PAT exception is not exist")
            count = count + 1
        return count

    def test_total_not_recieved_data(self):
        cal = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)

        school_not_recived = self.driver.find_element_by_id('schools').text
        notcount = re.sub("\D", "",school_not_recived)

        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.driver.find_element_by_id('blockbtn').click()
        cal.page_loading(self.driver)
        blockcount = self.driver.find_element_by_id('schools').text
        bcount = re.sub("\D", "",blockcount)
        cal.page_loading(self.driver)

        self.driver.find_element_by_id('clusterbtn').click()
        cal.page_loading(self.driver)
        time.sleep(6)
        clustcount = self.driver.find_element_by_id('schools').text
        clustercount = re.sub("\D", "", clustcount)
        cal.page_loading(self.driver)

        self.driver.find_element_by_id('schoolbtn').click()
        cal.page_loading(self.driver)
        time.sleep(8)
        sccount = self.driver.find_element_by_id('schools').text
        schoolcount = re.sub("\D", "", sccount)
        cal.page_loading(self.driver)
        return  notcount , bcount , clustercount,schoolcount

    def check_dots_on_each_districts(self):
        cal = GetData()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        count = 0
        for x in range(1, len(select_district.options)):
            time.sleep(2)
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            dots = self.driver.find_elements_by_class_name(Data.dots)
            if int(len(dots) - 1) == 0:
                print("District" + select_district.first_selected_option.text + "Markers are not found")
                count = count + 1
        return count

    def check_districts_csv_download(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            value = self.driver.find_element_by_id('choose_dist').get_attribute('value')
            value = value[4:]+'_'
            markers = self.driver.find_elements_by_class_name(Data.dots)
            time.sleep(3)
            if (len(markers) - 1) == 0:
                print("District" + select_district.first_selected_option.text + "no data")
                count = count + 1
            else:
                time.sleep(2)
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(3)
                p = pwd()
                self.filename = p.get_download_dir() + "/" + "periodic_assesment_test_exception_"+management+"_overall_allGrades__blockPerDistricts_of_district_"+value.strip()+cal.get_current_date()+'.csv'
                print(self.filename)
                if not os.path.isfile(self.filename):
                    print("District" + select_district.first_selected_option.text + "csv is not downloaded")
                    count = count + 1
                else:
                    df = pd.read_csv(self.filename)
                    schools = df['Total Schools With Missing Data'].sum()
                    school = self.driver.find_element_by_id("schools").text
                    sc = re.sub('\D', "", school)
                    os.remove(self.filename)
                    if int(sc) != int(schools):
                        print("school count mismatched", int(sc), int(schools))
                        count = count + 1

        return count



    def ClusterPerBlockCsvDownload(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        select_block = Select(self.driver.find_element_by_id('choose_block'))
        count = 0
        for x in range(len(select_district.options) - 1, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            for y in range(1, len(select_block.options)):
                select_block.select_by_index(y)
                cal.page_loading(self.driver)
                value = self.driver.find_element_by_id('choose_block').get_attribute('value')
                value = value[3:]+'_'
                time.sleep(2)
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(4)
                p = pwd()
                self.filename = p.get_download_dir() + "/" +"periodic_assesment_test_exception_"+management+"_overall_allGrades__clusterPerBlocks_of_block_"+value.strip()+cal.get_current_date()+'.csv'
                print(self.filename)
                if os.path.isfile(self.filename) != True:
                    print(
                        "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "csv is not downloaded")
                    count = count + 1
                else:
                    df = pd.read_csv(self.filename)
                    schools = df['Total Schools With Missing Data'].sum()
                    school = self.driver.find_element_by_id("schools").text
                    sc = re.sub('\D', "", school)
                    if int(sc) != int(schools):
                        print("school count mismatched", int(sc), int(schools))
                        count = count + 1
            os.remove(self.filename)
        return count

    def SchoolPerClusterCsvDownload(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        select_block = Select(self.driver.find_element_by_id('choose_block'))
        select_cluster=Select(self.driver.find_element_by_id('choose_cluster'))
        count = 0
        for x in range(len(select_district.options)-1, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            for y in range(1, len(select_block.options)):
                time.sleep(2)
                select_block.select_by_index(y)
                cal.page_loading(self.driver)
                for z in range(1,len(select_cluster.options)):
                    select_cluster.select_by_index(z)
                    cal.page_loading(self.driver)
                    value = self.driver.find_element_by_id('choose_cluster').get_attribute('value')
                    value = value.split(":")
                    value = value[1].strip() +'_'
                    time.sleep(2)
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(4)
                    p = pwd()
                    self.filename = p.get_download_dir() + "/" +"periodic_assesment_test_exception_"+management+"_overall_allGrades__schoolPerClusters_of_cluster_"+value+cal.get_current_date()+'.csv'
                    print(self.filename)
                    if os.path.isfile(self.filename) != True:
                        print(
                            "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text +  "csv is not downloaded")
                        count = count + 1
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            data = list(csv_reader)
                            row_count = len(data)
                            os.remove(self.filename)
                            school = self.driver.find_element_by_id("schools").text
                            sc = re.sub('\D', "", school)
                            if int(sc) != int(row_count):
                                print("school count mismatched", int(sc), int(row_count))
                                count = count + 1
            return count

    def check_markers_on_block_map(self):
        cal = GetData()
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_id('blockbtn').click()
        cal.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        markers = len(dots) - 1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        self.filename = p.get_download_dir() + "/" +"periodic_assessment_test_exception_"+management+"_overall_allGrades__allBlocks_"+cal.get_current_date()+'.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        if os.path.isfile(self.filename) == True:
            os.remove(self.filename)
        return markers

    def check_markers_on_clusters_map(self):
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_id('clusterbtn').click()
        cal = GetData()
        self.fname = file_extention()
        cal.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        markers = len(dots) - 1
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + "periodic_assessment_test_exception_"+management+"_overall_allGrades__allClusters_" + cal.get_current_date() + '.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        if os.path.isfile(self.filename) == True:
            os.remove(self.filename)
        return markers

    def check_markers_on_school_map(self):
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_id('schoolbtn').click()
        cal = GetData()
        self.fname = file_extention()
        cal.page_loading(self.driver)
        time.sleep(10)
        result = self.driver.find_elements_by_class_name(Data.dots)
        cal.page_loading(self.driver)
        markers = len(result) - 1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + "periodic_assessment_test_exception_"+management+"_overall_allGrades__allSchools_" + cal.get_current_date() + '.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        if os.path.isfile(self.filename) == True:
            os.remove(self.filename)
        return markers

    def click_on_hyperlinks(self):
        cal = GetData()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        dist = Select(self.driver.find_element_by_id("choose_dist"))
        dist.select_by_index(1)
        cal.page_loading(self.driver)
        block = Select(self.driver.find_element_by_id("choose_block"))
        block.select_by_index(1)
        cal.page_loading(self.driver)
        cluster = Select(self.driver.find_element_by_id("choose_cluster"))
        cluster.select_by_index(1)
        cal.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.sr_school_hyper).click()
        cal.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.sr_cluster_hyper).click()
        cal.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.sr_dist_hyper).click()
        cal.page_loading(self.driver)
        result1 = self.driver.find_element_by_id('choose_block').is_displayed()
        time.sleep(2)
        result2 = self.driver.find_element_by_id('choose_cluster').is_displayed()
        time.sleep(2)
        dist = Select(self.driver.find_element_by_id('choose_dist'))
        choose_dist = dist.first_selected_option.text
        return result1, result2, choose_dist

    def check_time_series_overall(self):
        cal = GetData()
        self.p = pwd()
        count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.file = file_extention()
        cal.click_on_state(self.driver)
        timeperiods = Select(self.driver.find_element_by_id('period'))
        # timeperiods.select_by_visible_text(' Overall ')
        timeperiods.select_by_index(1)
        time.sleep(3)
        cal.page_loading(self.driver)
        if 'No data found' in self.driver.page_source:
            print('Over all is not having data')
        else:
            markers = self.driver.find_elements_by_class_name(Data.dots)
            dots = len(markers) - 1
            if markers == 0:
                print('Markers are not present on screen ')
                count = count + 1
            else:
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + '/' + "periodic_assesment_test_exception_"+management+"_overall_allGrades__allBlocks_"+cal.get_current_date()+'.csv'
                print(self.filename)
                if os.path.isfile(self.filename) != True:
                    print("Over all time series csv file is not downloaded")
                    count = count + 1
                else:
                    df = pd.read_csv(self.filename)
                    schools = df['Total Schools With Missing Data'].sum()
                    school = self.driver.find_element_by_id("schools").text
                    sc = re.sub('\D', "", school)
                    if int(sc) != int(schools):
                        print("school count mismatched", int(sc), int(schools))
                        count = count + 1
            os.remove(self.filename)
        return count

    def check_time_series_last_7_days(self):
        cal = GetData()
        self.p = pwd()
        count = 0
        cal.click_on_state(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.file = file_extention()
        timeperiods = Select(self.driver.find_element_by_id('period'))
        # timeperiods.select_by_visible_text(' Last 7 Days ')
        timeperiods.select_by_index(3)
        timepd = (timeperiods.first_selected_option.text).lower()
        cal.page_loading(self.driver)
        if 'No data found' in self.driver.page_source:
            print('Last 7 Days is not having data')
        else:
            markers = self.driver.find_elements_by_class_name(Data.dots)
            dots = len(markers)-1
            if markers == 0:
                print('Markers are not present on screen ')
                count = count + 1
            else:
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + '/' +"periodic_assesment_test_exception_"+management+'_'+timepd.replace(' ','_')+'_allGrades__allBlocks_'+cal.get_current_date()+'.csv'
                print(self.filename)
                if os.path.isfile(self.filename) != True:
                    print(" Last 7 Days time series csv file is not downloaded")
                else:
                    df = pd.read_csv(self.filename)
                    total_mis = df['Total Schools With Missing Data'].sum()
                    school = self.driver.find_element_by_id("schools").text
                    sc = re.sub('\D', "", school)
                    if int(sc) != int(total_mis):
                        print("school count mismatched", int(sc), int(total_mis))
                        count = count + 1
                os.remove(self.filename)
        return count

    def check_time_series_last_30_days(self):
        cal = GetData()
        self.p = pwd()
        count = 0
        self.file = file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        cal.click_on_state(self.driver)
        timeperiods = Select(self.driver.find_element_by_id('period'))
        # timeperiods.select_by_visible_text(' Last 30 Days ')
        timeperiods.select_by_index(2)
        timepd = (timeperiods.first_selected_option.text).lower()
        cal.page_loading(self.driver)
        if 'No data found' in self.driver.page_source:
            print('Last 30 Days is not having data')
        else:
            markers = self.driver.find_elements_by_class_name(Data.dots)
            dots = len(markers) - 1
            if markers == 0:
                print('Markers are not present on screen ')
                count = count + 1
            else:
                cal.page_loading(self.driver)
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(5)
                self.filename = self.p.get_download_dir() + '/' +"periodic_assesment_test_exception_"+management+'_'+timepd.replace(' ','_')+'_allGrades__allBlocks_'+cal.get_current_date()+'.csv'
                print(self.filename)
                if os.path.isfile(self.filename) != True:
                    print(" Last 30 Days time series csv file is not downloaded")
                else:
                    df = pd.read_csv(self.filename)
                    total_mis = df['Total Schools With Missing Data'].sum()
                    school = self.driver.find_element_by_id("schools").text
                    sc = re.sub('\D', "", school)
                    if int(sc) != int(total_mis):
                        print("school count mismatched", int(sc), int(total_mis))
                        count = count + 1
                os.remove(self.filename)
        return count