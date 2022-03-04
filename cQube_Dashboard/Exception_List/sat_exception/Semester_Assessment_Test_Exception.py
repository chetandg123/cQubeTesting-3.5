import os
import re
import time
from datetime import date

import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Locators.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class Semester_Assessment_Test_Exception():
    def __init__(self,driver):
        self.driver = driver

    def test_icon(self):
        self.data = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.data.page_loading(self.driver)
        self.data.navigate_to_semester_exception()
        self.data.page_loading(self.driver)
        if "sem-exception" in self.driver.current_url:
            print("Semester exception report page is dispayed")
        else:
            print("Semester exception icon is not working")
            count = count + 1
        return count
    def sem_exception_options_test(self):
        self.data = GetData()
        p = pwd()
        count = 0
        fname = file_extention()
        choose = Select(self.driver.find_element_by_id('choose_semester'))
        choose.select_by_index(1)
        if 'no data found' in self.driver.page_source:
            print("Semester 1 has not data")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.data.page_loading(self.driver)
            self.data.navigate_to_semester_exception()
            self.data.page_loading(self.driver)
        return count

    def test_click_on_dashboard(self):
        count = 0
        cal = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        cal.navigate_to_semester_exception()
        cal.page_loading(self.driver)
        if 'sem-exception' in self.driver.current_url:
            print("Semester exception report is present ")
        else:
            print("Semester exception is not exist")
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
        clustcount = self.driver.find_element_by_id('schools').text
        clustercount = re.sub("\D", "", clustcount)
        cal.page_loading(self.driver)

        self.driver.find_element_by_id('schoolbtn').click()
        cal.page_loading(self.driver)
        sccount = self.driver.find_element_by_id('schools').text
        schoolcount = re.sub("\D", "", sccount)
        cal.page_loading(self.driver)

        return  notcount , bcount , clustercount,schoolcount

    def check_markers_on_block_map(self):
        cal = GetData()
        self.fname =file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        self.driver.find_element_by_id('blockbtn').click()
        cal.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        markers = len(dots) - 1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.exception_block()+management+"_overall_allGrades__allBlocks_"+cal.get_current_date()+".csv"
        if os.path.isfile(self.filename) != True:
            os.remove(self.filename)
            return "File Not Downloaded"
        if os.path.isfile(self.filename) == True:
            os.remove(self.filename)
        return markers
    def check_markers_on_clusters_map(self):
        self.driver.find_element(By.XPATH,Data.hyper_link).click()
        time.sleep(2)
        self.driver.find_element_by_id('clusterbtn').click()
        cal = GetData()
        self.fname = file_extention()
        cal.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        markers = len(dots)-1
        cal.page_loading(self.driver)
        management_name = self.driver.find_element(By.ID,"name").text
        print(management_name,'is management')
        management = (management_name[16:].strip()).lower()
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.exception_cluster()+management+"_overall_allGrades__allClusters_"+cal.get_current_date()+'.csv'
        if os.path.isfile(self.filename) != True:
            os.remove(self.filename)
            return "File Not Downloaded"
        if os.path.isfile(self.filename) == True:
            os.remove(self.filename)
        return markers

    def check_markers_on_school_map(self):
        self.driver.find_element_by_id('schoolbtn').click()
        time.sleep(15)
        cal = GetData()
        self.fname = file_extention()
        cal.page_loading(self.driver)
        result= self.driver.find_elements_by_class_name(Data.dots)
        cal.page_loading(self.driver)
        markers = len(result) - 1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.exception_school()+cal.get_current_date()+'.csv'
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        if os.path.isfile(self.filename) == True:
            os.remove(self.filename)
        return markers

    def check_districts_csv_download(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        count = 0
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            value = self.driver.find_element_by_id('choose_dist').get_attribute('value')
            value = value[4:]+'_'
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            p = pwd()
            self.filename = p.get_download_dir() + "/" + self.fname.exception_districtwise()+management+'_overall_allGrades__blockPerDistricts_of_district_'+value.strip()+cal.get_current_date()+'.csv'
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print("District" + select_district.first_selected_option.text + "csv is not downloaded")
                count = count + 1
            else:
                # with open(self.filename) as fin:
                #     csv_reader = csv.reader(fin, delimiter=',')
                #     header = next(csv_reader)
                #     schools = 0
                #     for row in csv.reader(fin):
                #         schools += int(row[6].replace(',', ''))
                data = pd.read_csv(self.filename)
                schools = data['Total Schools With Missing Data'].sum()
                missingdata = self.driver.find_element_by_id('schools').text
                md = re.sub('\D', '', missingdata)
                if int(schools) != int(md):
                    print("District" + select_district.first_selected_option.text, schools, md)
                    count = count + 1
                os.remove(self.filename)
            return count

    def click_download_csv_of_districts(self):
        cal = GetData()
        count = 0
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.exception_district()+management+'_overall_allGrades__allDistricts_'+cal.get_current_date()+'.csv'
        print(self.filename)
        cal.page_loading(self.driver)
        if not os.path.isfile(self.filename):
            print("Districtwise csv is not downloaded")
            count = count + 1
        else:
            # with open(self.filename) as fin:
            #     csv_reader = csv.reader(fin, delimiter=',')
            #     header = next(csv_reader)
            #     schools = 0
            #     for row in csv.reader(fin):
            #         schools += int(row[4])
            data = pd.read_csv(self.filename)
            schools = data["Total Schools With Missing Data"].sum()
            school = self.driver.find_element_by_id("schools").text
            sc = re.sub('\D', "", school)
            if int(sc) != int(schools):
                print("school count mismatched", int(sc), int(schools))
                count = count + 1
        os.remove(self.filename)
        return count

    def click_on_blocks_click_on_home_icon(self):
        self.driver.find_element_by_id('blockbtn').click()
        cal = GetData()
        count = 0
        cal.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal = GetData()
        cal.page_loading(self.driver)
        if 'sem-exception' in self.driver.current_url:
            print("Semester exception report is present ")
        else:
            print("Semester exception is not exist")
            count = count + 1
        return count

    def check_dots_on_each_districts(self):
        cal = GetData()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        count = 0
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            dots = self.driver.find_elements_by_class_name(Data.dots)
            if int(len(dots) - 1) == 0:
                print("District" + select_district.first_selected_option.text + "Markers are not found")
                count = count + 1
        return count

    def check_csv_download(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        select_block = Select(self.driver.find_element_by_id('choose_block'))
        count = 0
        for x in range(len(select_district.options)-1, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            for y in range(1, len(select_block.options)):
                select_block.select_by_index(y)
                cal.page_loading(self.driver)
                value = self.driver.find_element_by_id('choose_block').get_attribute('value')
                value = value.split(":")
                value = value[1].strip() + '_'
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(4)
                p= pwd()
                self.filename = p.get_download_dir() + "/" + self.fname.exception_blockwise()+management+'_overall_allGrades__clusterPerBlocks_of_block_'+value.strip()+date.today().strftime('%d-%m-%Y').strip()+'.csv'
                print(self.filename)
                if os.path.isfile(self.filename) != True:
                    print("District" + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text   + "csv is not downloaded")
                    count = count + 1
                else:
                    # with open(self.filename) as fin:
                    #     csv_reader = csv.reader(fin, delimiter=',')
                    #     header = next(csv_reader)
                    #     schools = 0
                    #     for row in csv.reader(fin):
                    #         schools += int(row[8].replace(',', ''))
                    data = pd.read_csv(self.filename)
                    schools = data["Total Schools With Missing Data"].sum()
                    missingdata = self.driver.find_element_by_id('schools').text
                    md = re.sub('\D', '', missingdata)
                    if int(schools) != int(md):
                        print(
                            'District' + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text,
                            schools, md)
                        count = count + 1
                os.remove(self.filename)
                return count
    def click_on_logout(self):
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.logout).click()
        return self.driver.title

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
        choose_dist= dist.first_selected_option.text
        return result1,result2,choose_dist

