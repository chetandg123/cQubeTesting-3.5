import csv
import os
import re
import time
from selenium.common import exceptions
from selenium.webdriver.support.select import Select
from Locators.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData

'''Script perform the test the blocks , cluster and school level buttons and dropdowns , map records , 
footer information's '''


class Infrastructure_access_by_location():

    def __init__(self, driver):
        self.driver = driver

    def test_link(self):
        self.p = GetData()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.scm_block).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)

    def test_donwload(self):
        self.p = GetData()
        cal = pwd()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        managment_name = self.driver.find_element_by_id('name').text
        name = managment_name[16:].strip().lower()
        time.sleep(2)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        self.filename = cal.get_download_dir() + '/' + self.fname.scmap_district() + name + '_allDistricts_' + self.p.get_current_date() + '.csv'
        self.p.page_loading(self.driver)
        if not os.path.isfile(self.filename):
            print("Districtwise csv is not downloaded")
            count = count + 1
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                schools = 0
                for row in csv.reader(fin):
                    schools += int(row[0])
                school = self.driver.find_element_by_id("schools").text
                sc = re.sub('\D', "", school)
                if int(sc) != int(schools):
                    print("school count mismatched")
                    count = count + 1
            os.remove(self.filename)
        return count

    def check_download_csv1(self):
        p = pwd()
        self.cal = GetData()
        self.fname = file_extention()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.cal.page_loading(self.driver)
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        select_block = Select(self.driver.find_element_by_id('choose_block'))
        select_cluster = Select(self.driver.find_element_by_id('choose_cluster'))
        count = 0
        for x in range(int(len(select_district.options)) - 1, int(len(select_district.options))):
            select_district.select_by_index(x)
            self.cal.page_loading(self.driver)
            for y in range(len(select_block.options) - 1, len(select_block.options)):
                select_block.select_by_index(y)
                self.cal.page_loading(self.driver)
                for z in range(1, len(select_cluster.options)):
                    select_cluster.select_by_index(z)
                    self.cal.page_loading(self.driver)
                    value = self.driver.find_element_by_id('choose_cluster').get_attribute('value')
                    value = value.split(":")
                    nodata = self.driver.find_element_by_id("errMsg").text
                    markers = self.driver.find_elements_by_class_name(Data.dots)
                    if len(markers) - 1 == 0:
                        print(select_cluster.options[z].text, "does not contains markers on map")
                    else:
                        self.driver.find_element_by_id(Data.Download).click()
                        time.sleep(3)
                        self.filename = p.get_download_dir() + "/" + self.fname.scmap_clusterwise() + name + '_schools_of_cluster_' + \
                                        value[1].strip() + '_' + self.cal.get_current_date() + '.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(select_cluster.options[z].text, "csv file is not downloaded!")
                            count = count + 1
                        else:
                            with open(self.filename) as fin:
                                csv_reader = csv.reader(fin)
                                data = list(csv_reader)
                                countrecords = len(data)
                                # header = next(csv_reader)
                                # total = 0
                                # for row in csv.reader(fin):
                                #     total += int(row[2])
                                school = self.driver.find_element_by_id("schools").text
                                sc = re.sub('\D', "", school)
                                if int(sc) != int(countrecords) - 1:
                                    print(select_block.options[y].text, "schools:", int(countrecords) - 1, int(sc),
                                          "mismatch found")
                                    count = count + 1
                            os.remove(self.filename)
        return count

    # All infrastructure score options
    def infra_score(self):
        self.fname = file_extention()
        self.cal = GetData()
        self.driver.find_element_by_css_selector('p >span').click()
        self.cal.page_loading(self.driver)
        management_name = self.cal.get_management_selected_option()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(1)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.scmap_district() + management_name + '_allDistricts_' + self.cal.get_current_date() + '.csv'
        row_count = 0
        with open(self.filename, 'rt') as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Infra score percentage is selected and csv file is downloaded")
        return row_count - 1

    def Boys_toilet_percentage(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(2)
        self.cal.page_loading(self.driver)
        management_name = self.cal.get_management_selected_option()
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        filename = p.get_download_dir() + "/" + self.fname.scmap_district() + management_name + '_allDistricts_' + self.cal.get_current_date() + '.csv'
        row_count = 0
        with open(filename, 'rt') as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Boy's toilet percentage is selected and csv file is downloaded")
        return row_count - 1

    def drinking_water(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(3)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        management_name = self.cal.get_management_selected_option()
        filename = p.get_download_dir() + "/" + self.fname.scmap_district() + management_name + '_allDistricts_' + self.cal.get_current_date() + '.csv'
        row_count = 0
        with open(filename, 'rt') as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Drinking water percentage is selected and csv file is downloaded")
        return row_count - 1

    def Electricity(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(4)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        management_name = self.cal.get_management_selected_option()
        filename = p.get_download_dir() + "/" + self.fname.scmap_district() + management_name + '_allDistricts_' + self.cal.get_current_date() + '.csv'
        row_count = 0
        with open(filename, 'rt') as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Electricity percentage is selected and csv file is downloaded")
        return row_count - 1

    def girls_toilet(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(5)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        management_name = self.cal.get_management_selected_option()
        filename = p.get_download_dir() + "/" + self.fname.scmap_district() + management_name + '_allDistricts_' + self.cal.get_current_date() + '.csv'
        row_count = 0
        with open(filename, 'rt') as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("girls toilet percentage is selected and csv file is downloaded")
        return row_count - 1

    def Handpump(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(6)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        management_name = self.cal.get_management_selected_option()
        filename = p.get_download_dir() + "/" + self.fname.scmap_district() + management_name + '_allDistricts_' + self.cal.get_current_date() + '.csv'
        row_count = 0
        with open(filename, 'rt') as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Hand pump percentage is selected and csv file is downloaded")
        return row_count - 1

    def Handwash(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(7)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        management_name = self.cal.get_management_selected_option()
        filename = p.get_download_dir() + "/" + self.fname.scmap_district() + management_name + '_allDistricts_' + self.cal.get_current_date() + '.csv'
        row_count = 0
        with open(filename, 'rt') as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Handwash percentage is selected and csv file is downloaded")
        return row_count - 1

    def Library(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(8)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        management_name = self.cal.get_management_selected_option()
        filename = p.get_download_dir() + "/" + self.fname.scmap_district() + management_name + '_allDistricts_' + self.cal.get_current_date() + '.csv'
        row_count = 0
        with open(filename, 'rt') as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Library percentage is selected and csv file is downloaded")
        return row_count - 1

    def Solar_panel(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(9)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        management_name = self.cal.get_management_selected_option()
        filename = p.get_download_dir() + "/" + self.fname.scmap_district() + management_name + '_allDistricts_' + self.cal.get_current_date() + '.csv'
        row_count = 0
        with open(filename, 'rt') as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("solar panel percentage is selected and csv file is downloaded")
        return row_count - 1

    def Tapwater(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(10)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        management_name = self.cal.get_management_selected_option()
        filename = p.get_download_dir() + "/" + self.fname.scmap_district() + management_name + '_allDistricts_' + self.cal.get_current_date() + '.csv'
        row_count = 0
        with open(filename, 'rt') as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Tapwater percentage is selected and csv file is downloaded")
        return row_count - 1

    def Toilet(self):
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(11)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(2)
        p = pwd()
        management_name = self.cal.get_management_selected_option()
        filename = p.get_download_dir() + "/" + self.fname.scmap_district() + management_name + '_allDistricts_' + self.cal.get_current_date() + '.csv'
        row_count = 0
        with open(filename, 'rt') as f:
            reader = csv.reader(f)
            data = list(reader)
            row = len(data)
            row_count = row
        print("Toilet percentage is selected and csv file is downloaded")
        return row_count - 1

    def infra_score_dropdown(self):
        self.fname = file_extention()
        self.cal = GetData()
        self.driver.find_element_by_css_selector('p >span').click()
        self.cal.page_loading(self.driver)
        infraoptions = Select(self.driver.find_element_by_id('choose_infra'))
        for i in range(1, len(infraoptions.options)):
            infraoptions.select_by_index(i)
            self.cal.page_loading(self.driver)
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.management_name = self.cal.get_management_selected_option()
            filename = p.get_download_dir() + "/" + self.fname.scmap_district() + self.management_name + '_allDistricts_' + self.cal.get_current_date() + '.csv'
            row_count = 0
            with open(self.filename, 'rt') as f:
                reader = csv.reader(f)
                data = list(reader)
                row = len(data)
                row_count = row
            print(infraoptions.options[i].text, "is selected and csv file is downloaded")
            os.remove(self.filename)
            return row_count - 1

    def remove_csv(self):
        os.remove(self.filename)

    def test_infrascores(self):
        self.p = GetData()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        count = len(chooseinfra.options) - 1
        self.p.page_loading(self.driver)
        for x in range(1, len(chooseinfra.options)):
            chooseinfra.select_by_index(x)
            print(chooseinfra.options[x].text, 'is selected')
            self.p.page_loading(self.driver)
        return count

    def test_blocks_button(self):
        self.p = GetData()
        cal = pwd()
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        management_name = self.p.get_management_selected_option()
        self.driver.find_element_by_id(Data.scm_block).click()
        self.p.page_loading(self.driver)
        time.sleep(10)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        count = len(dots) - 1
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        self.filename = cal.get_download_dir() + "/" + self.fname.scmap_block() + management_name + '_allBlocks_' + self.p.get_current_date() + '.csv'
        print(self.filename)
        self.p.page_loading(self.driver)
        file = os.path.isfile(self.filename)
        self.p.page_loading(self.driver)
        os.remove(self.filename)
        return count, file

    def test_clusterbtn(self):
        self.p = GetData()
        cal = pwd()
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        management_name = self.p.get_management_selected_option()
        self.driver.find_element_by_id(Data.scm_cluster).click()
        self.p.page_loading(self.driver)
        time.sleep(30)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        count = len(dots) - 1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(4)
        self.filename = cal.get_download_dir() + '/' + self.fname.scmap_cluster() + management_name + '_allClusters_' + self.p.get_current_date() + '.csv'
        print(self.filename)
        self.p.page_loading(self.driver)
        file = os.path.isfile(self.filename)
        self.p.page_loading(self.driver)
        os.remove(self.filename)
        self.p.page_loading(self.driver)
        return count, file

    def test_click_on_school_btn(self):
        self.p = GetData()
        cal = pwd()
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        management_name = self.p.get_management_selected_option()
        self.driver.find_element_by_id(Data.scm_school).click()
        self.p.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        count = len(dots) - 1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(30)
        self.filename = cal.get_download_dir() + '/' + self.fname.scmap_school() + management_name + '_allSchools_' + self.p.get_current_date() + ".csv"
        print(self.filename)
        self.p.page_loading(self.driver)
        file = os.path.isfile(self.filename)
        self.p.page_loading(self.driver)
        os.remove(self.filename)
        return count, file

    def test_check_total_schoolvalue(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        try:
            school = self.driver.find_element_by_id(Data.sc_no_of_schools).text
            res = re.sub('\D', "", school)
            self.p.page_loading(self.driver)

            self.driver.find_element_by_id(Data.scm_block).click()
            self.p.page_loading(self.driver)
            bschool = self.driver.find_element_by_id(Data.sc_no_of_schools).text
            bres = re.sub('\D', "", bschool)
            self.p.page_loading(self.driver)

            self.driver.find_element_by_id(Data.scm_cluster).click()
            self.p.page_loading(self.driver)
            time.sleep(10)
            cschool = self.driver.find_element_by_id(Data.sc_no_of_schools).text
            cres = re.sub('\D', "", cschool)
            self.p.page_loading(self.driver)

            self.driver.find_element_by_id(Data.scm_school).click()
            time.sleep(15)
            sschool = self.driver.find_element_by_id(Data.sc_no_of_schools).text
            sres = re.sub('\D', "", sschool)
            self.p.page_loading(self.driver)

            return res, bres, cres, sres
        except exceptions.ElementClickInterceptedException:
            print("no of schools are same ")
            self.p.page_loading(self.driver)

    def test_click_blocks(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id('blockbtn').click()
        self.p.page_loading(self.driver)
        time.sleep(10)
        scores = Select(self.driver.find_element_by_id("choose_infra"))
        for i in range(len(scores.options)):
            time.sleep(1)
            scores.select_by_index(i)
        self.p.page_loading(self.driver)

    def test_click_clusters(self):
        self.driver.implicitly_wait(30)
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id('clusterbtn').click()
        self.p.page_loading(self.driver)
        time.sleep(15)
        scores = Select(self.driver.find_element_by_id("choose_infra"))
        for i in range(len(scores.options)):
            time.sleep(1)
            scores.select_by_index(i)
        self.p.page_loading(self.driver)

    def test_click_schools(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id('schoolbtn').click()
        self.p.page_loading(self.driver)
        time.sleep(20)
        scores = Select(self.driver.find_element_by_id("choose_infra"))
        for i in range(len(scores.options)):
            time.sleep(1)
            scores.select_by_index(i)
        self.p.page_loading(self.driver)

    def test_districtlist(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        Districts = self.driver.find_elements_by_xpath(Data.sc_choosedist)
        self.p.page_loading(self.driver)
        count = len(Districts) - 1
        return count

    def test_map(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        self.p.page_loading(self.driver)
        count = len(dots) - 1
        return count

    def test_home(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)

        self.driver.find_element_by_id(Data.scm_block).click()
        self.p.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        self.p.page_loading(self.driver)
        count1 = len(dots) - 1

        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.scm_cluster).click()
        self.p.page_loading(self.driver)
        time.sleep(20)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        self.p.page_loading(self.driver)
        count2 = len(dots) - 1
        self.p.page_loading(self.driver)

        self.driver.find_element_by_id(Data.scm_school).click()
        self.p.page_loading(self.driver)
        time.sleep(30)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        self.p.page_loading(self.driver)
        count3 = len(dots) - 1
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        return count1, count2, count3

    def test_options(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        Districts = self.driver.find_elements_by_xpath(Data.sc_choosedist)
        count = len(Districts) - 1
        for i in range(len(Districts)):
            Districts[i].click()
            self.p.page_loading(self.driver)
            print(Districts[i].text)

        return count

    def test_districtwise(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        self.p.page_loading(self.driver)

    def test_mousehover(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        markers = self.driver.find_elements_by_class_name(Data.dots)
        count = len(markers) - 1
        print("Mousehover on each markers..")
        self.p.test_mouse_over()
        self.p.page_loading(self.driver)
        return count

    def test_dist_blocks(self):
        self.driver.implicitly_wait(20)
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        Districts = self.driver.find_elements_by_xpath(Data.sc_choosedist)
        blocks = self.driver.find_elements_by_xpath(Data.sc_chooseblock)
        for i in range(1, len(Districts)):
            Districts[i].click()
            print(Districts[i].text)
            self.p.page_loading(self.driver)

    def test_blocks(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.scm_dist).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.scm_blk).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.homeicon).click()
        self.p.page_loading(self.driver)

    def test_count(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.scm_block).click()
        self.p.page_loading(self.driver)
        schools = self.driver.find_element_by_id(Data.sc_no_of_schools).text
        res = re.sub("\D", "", schools)
        self.p.page_loading(self.driver)
        return res

    def test_blockwise_data(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.scm_dist).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.scm_blk).click()
        self.p.page_loading(self.driver)
        lists = self.driver.find_elements_by_class_name(Data.dots)
        self.p.page_loading(self.driver)
        count = len(lists) - 1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        return count

    def test_clusterbtn(self):
        self.p = GetData()
        cal = pwd()
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        management_name = self.p.get_management_selected_option()
        self.driver.find_element_by_id(Data.scm_cluster).click()
        self.p.page_loading(self.driver)
        time.sleep(20)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        count = len(dots) - 1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(4)
        self.filename = cal.get_download_dir() + '/' + self.fname.scmap_cluster() + management_name + '_allClusters_' + self.p.get_current_date() + '.csv'
        print(self.filename)
        self.p.page_loading(self.driver)
        file = os.path.isfile(self.filename)
        self.p.page_loading(self.driver)
        os.remove(self.filename)
        self.p.page_loading(self.driver)
        return count, file

    def test_donwload(self):
        self.p = GetData()
        cal = pwd()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        managment_name = self.driver.find_element_by_id('name').text
        name = managment_name[16:].strip().lower()
        time.sleep(2)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        self.filename = cal.get_download_dir() + '/' + self.fname.scmap_district() + name + '_allDistricts_' + self.p.get_current_date() + '.csv'
        self.p.page_loading(self.driver)
        if not os.path.isfile(self.filename):
            print("Districtwise csv is not downloaded")
            count = count + 1
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                schools = 0
                for row in csv.reader(fin):
                    schools += int(row[0])
                school = self.driver.find_element_by_id("schools").text
                sc = re.sub('\D', "", school)
                if int(sc) != int(schools):
                    print("school count mismatched")
                    count = count + 1
            os.remove(self.filename)
        return count
