import csv
import os
import time

import pandas as pd
from selenium.common import exceptions
from selenium.webdriver.support.select import Select

from Locators.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class Composite_Report():

    def __init__(self,driver):
        self.driver = driver

    def test_report(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        try:
            self.driver.find_element_by_id(Data.menu_icon).click()
            self.p.page_loading(self.driver)
            text = self.driver.find_element_by_id(Data.sch_infra).text
            print(text)
            self.driver.find_element_by_xpath(Data.composite).click()
            self.p.page_loading(self.driver)
            self.p.page_loading(self.driver)
            if "school-infrastructure" in self.driver.current_url:
                print("Shool infrastructure report page")
            else:
                print("School infrastructure report page is not exist")
            return text
        except exceptions.NoSuchElementException:
            print("school infra report page is present on screen")
            self.p.page_loading(self.driver)

    def test_schools(self):
        p = pwd()
        self.cal = GetData()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        District_wise = Select(self.driver.find_element_by_id("downloader"))
        # District_wise.select_by_visible_text(" Dist Wise Infra_Table_Report ")
        District_wise.select_by_index(1)
        self.cal.page_loading(self.driver)
        self.file= file_extention()
        self.driver.find_element_by_id(Data.Download_scator).click()
        time.sleep(5)
        count = 0
        self.filename = p.get_download_dir() +'/'+ self.file.sc_district()+management+'_allDistricts_'+self.cal.get_current_date()+'.csv'
        self.cal.page_loading(self.driver)
        if os.path.isfile(self.filename) != True:
            print("District wise csv file is not downloaded")
            count = count + 1
        os.remove(self.filename)
        return  count

    def test_menulist(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.sch_infra).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.composite).click()
        self.p.page_loading(self.driver)

    def test_block(self):
        self.p = GetData()
        self.driver.implicitly_wait(20)
        self.fname=file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        p =pwd()
        District_wise=Select(self.driver.find_element_by_name("downloadType"))
        District_wise.select_by_index(2)
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download_scator).click()
        time.sleep(15)
        count=0
        self.filename = p.get_download_dir() + "/"+ self.fname.sc_block()+management+'_allBlocks_'+self.p.get_current_date()+'.csv'
        print(self.filename)
        self.p.page_loading(self.driver)
        if os.path.isfile(self.filename) != True:
            print('File is not downloaded ')
            count = count +1
        else:
            print('Block level file is downloaded')
            os.remove(self.filename)
        return count

    def test_districtwise(self):
        self.cal = GetData()
        self.fname = file_extention()
        self.driver.implicitly_wait(20)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.cal.page_loading(self.driver)
        p =pwd()
        count = 0
        District_wise=Select(self.driver.find_element_by_name("downloadType"))
        District_wise.select_by_index(1)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download_scator).click()
        self.cal.page_loading(self.driver)
        time.sleep(10)
        self.filename = p.get_download_dir() + "/" + self.fname.sc_district()+management+'_allDistricts_'+self.cal.get_current_date()+'.csv'
        if os.path.isfile(self.filename) != True:
            print('File is not downloaded ')
            count = count + 1
        else:
            print('Block level file is downloaded')
            os.remove(self.filename)
        return count

    def test_clusterwise(self):
        self.p = GetData()
        self.fname = file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        p =pwd()
        District_wise=Select(self.driver.find_element_by_name("downloadType"))
        District_wise.select_by_index(3)
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download_scator).click()
        time.sleep(15)
        count = 0
        self.filename = p.get_download_dir() + "/" + self.fname.sc_cluster()+management+'_allClusters_'+self.p.get_current_date()+'.csv'
        if os.path.isfile(self.filename) != True:
            print('File is not downloaded ')
            count = count + 1
        else:
            print('Block level file is downloaded')
            os.remove(self.filename)
        return count

    def test_schoolwise(self):
        self.data = GetData()
        self.fname =file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.data.page_loading(self.driver)
        try:
            p = pwd()
            District_wise=Select(self.driver.find_element_by_name("downloadType"))
            District_wise.select_by_index(4)
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.Download_scator).click()
            time.sleep(30)
            self.filename = p.get_download_dir() + "/" + self.fname.sc_school()+management+'_allSchools_'+self.data.get_current_date()+'.csv'
            time.sleep(10)
            count = 0
            if os.path.isfile(self.filename) != True:
                print('File is not downloaded ')
                count = count + 1
            else:
                print('Block level file is downloaded')
                os.remove(self.filename)
            return count

        except exceptions.NoSuchElementException:
            print("school wise csv downloaded")

    def click_on_hyperlinks(self):
        self.p = GetData()
        self.driver.implicitly_wait(20)  # seconds
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(3)
        self.p.page_loading(self.driver)
        dist = Select(self.driver.find_element_by_name("myDistrict"))
        dist.select_by_index(1)
        self.p.page_loading(self.driver)
        block = Select(self.driver.find_element_by_name("myBlock"))
        block.select_by_index(1)
        self.p.page_loading(self.driver)
        cluster = Select(self.driver.find_element_by_name("myCluster"))
        cluster.select_by_index(1)
        self.p.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.cluster_hyper).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.block_hyper).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.dist_hyper).click()
        self.p.page_loading(self.driver)

    def test_homeicon(self):
        self.p = GetData()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        dist = Select(self.driver.find_element_by_name("myDistrict"))
        dist.select_by_index(1)
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(4)
        self.driver.find_element_by_id(Data.homeicon).click()

    def test_homebtn(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.data.page_loading(self.driver)
        if 'dashboard' in self.driver.current_url:
            print("Dashboard Page is displayed ")
        else:
            print('cQube logo is not working ')
            count = count + 1
        self.data.navigate_to_composite_infrastructure()
        self.data.page_loading(self.driver)
        return count

    def test_tablevalue(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.d_names).click()
        self.p.page_loading(self.driver)
        values = self.driver.find_elements_by_xpath("//th[1]")
        for i in values:
            print(i.get_attribute("aria-sort"))

        self.p.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.d_names).click()
        self.p.page_loading(self.driver)
        value = self.driver.find_elements_by_xpath("//th[1]")
        for i in value:
            print(i.get_attribute("aria-sort"))

    def remove_csv1(self):
        os.remove(self.filename)

    def check_csv_download1(self):
        p = pwd()
        self.cal = GetData()
        self.fname =file_extention()
        self.driver.implicitly_wait(50)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.cal.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        select_block = Select(self.driver.find_element_by_name('myBlock'))
        select_cluster = Select(self.driver.find_element_by_name('myCluster'))
        count = 0
        for x in range(int(len(select_district.options))-1, int(len(select_district.options))):
            select_district.select_by_index(x)
            self.cal.page_loading(self.driver)
            print(select_district.options[x].text)
            for y in range(len(select_block.options)-3, len(select_block.options)):
                select_block.select_by_index(y)
                self.cal.page_loading(self.driver)
                for z in range(1, len(select_cluster.options)):
                    select_cluster.select_by_index(z)
                    self.cal.page_loading(self.driver)
                    value = self.driver.find_element_by_name('myCluster').get_attribute('value')
                    cvalue = value.split(":")
                    value = cvalue[1].strip()
                    nodata = self.driver.find_element_by_id("errMsg").text
                    if nodata == "No data found":
                        print(select_district.options[x].text,select_block.options[y],select_cluster.options[z].text, "no data found!")
                        count = count + 1
                    else:
                        self.driver.find_element_by_id(Data.Download).click()
                        time.sleep(3)
                        self.filename = p.get_download_dir() + "/" + self.fname.sc_clusterwise()+management+'_schools_of_cluster_'+ value+'_'+self.cal.get_current_date()+".csv"
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(select_cluster.options[z].text,"csv is not downloaded..")
                        else:
                            with open(self.filename) as fin:
                                csv_dict = [row for row in csv.DictReader(self.filename)]
                                if len(csv_dict) == 0:
                                    print(select_district.options[z].text,"does not contain Table records")
                            os.remove(self.filename)
                            self.cal.page_loading(self.driver)
            return  count

    def test_table_data(self):
            self.p = GetData()
            self.driver.find_element_by_xpath(Data.hyper).click()
            self.p.page_loading(self.driver)
            try:
                select_district = Select(self.driver.find_element_by_name('myDistrict'))
                count = 0
                for k in range(len(select_district.options)-5, len(select_district.options)):
                    select_district.select_by_index(k)
                    self.p.page_loading(self.driver)
                    table_data = []

                    li2 = self.driver.find_elements_by_xpath('//*[@id="table"]/tbody/tr')
                    for x in li2:
                        table_data_rows = x.text
                        table_data_rows = table_data_rows.split()
                        table_data.append(table_data_rows)

                    for i in range(len(table_data)):
                        for j in range(len(table_data[i])):
                            if table_data[i][j].isalpha() and table_data[i][j + 1].isalpha():
                                table_data[i][j] = table_data[i][j] + table_data[i][j + 1]

                    for x in range(len(table_data)):
                        for y in range(len(table_data[x])):
                            if table_data[x][y].isalpha() and table_data[x][y + 1].isalpha():
                                del (table_data[x][y + 1])
                            break
                    df = pd.DataFrame(table_data)
                    index = df.index
                    number_of_rows = len(index)
                    table_data.clear()
                    if number_of_rows ==0:
                        count = count + 1
                        print("District" + select_district.first_selected_option.text + "table data not found")
                    else:
                         print("Tables having Records...")
            finally:
                print("Records are present...")
            time.sleep(3)
            return count

    def test_logout(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(2)
        self.driver.find_element_by_id(Data.logout).click()

    def test_xplots(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        try:
            x_axis = Select(self.driver.find_element_by_id(Data.x))
            y_axis = Select(self.driver.find_element_by_id(Data.y))
            self.p.page_loading(self.driver)
            for x in range(1, len(x_axis.options)):
                x_axis.select_by_index(x)
                self.p.page_loading(self.driver)
            for y in range(1, len(y_axis.options)):
                    y_axis.select_by_index(y)
                    self.p.page_loading(self.driver)
        except exceptions.NoSuchElementException:
            print("Both x and y axis are selectable ")

    def test_yaxis(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        try:
            y_axis = Select(self.driver.find_element_by_id(Data.y))
            self.p.page_loading(self.driver)
            for y in range(1, len(y_axis.options)):
                y_axis.select_by_index(y)
                self.p.page_loading(self.driver)
        except exceptions.NoSuchElementException:
            print("Both x and y axis are selectable ")

    def test_districtwise(self):
        p = pwd()
        self.cal = GetData()
        self.fname =file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        count = 0
        for x in range(len(select_district.options)-4, len(select_district.options)):
            select_district.select_by_index(x)
            self.cal.page_loading(self.driver)
            value = self.driver.find_element_by_name('myDistrict').get_attribute("value")
            blkval =value.split(":")
            val = blkval[1].strip()
            nodata = self.driver.find_element_by_id("errMsg").text
            if nodata == "No data found":
                print(select_district.options[x].text, "no data found!")
            else:
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(3)
                self.filename = p.get_download_dir() + "/" + self.fname.sc_districtwise()+management+'_blocks_of_district_'+(val+'_').strip()+self.cal.get_current_date()+'.csv'
                print(self.filename)
                if not os.path.isfile(self.filename):
                    print(select_district.options[x].text , " csv file is not downloaded")
                    count = count + 1
                else:
                    with open(self.filename) as fin:
                        csv_dict = [row for row in csv.DictReader(self.filename)]
                        if len(csv_dict) == 0:
                            print(select_district.options[x].text,'csv file is empty')
                    os.remove(self.filename)
        return count

    def test_blockwise(self):
        p = pwd()
        self.cal = GetData()
        self.fname =file_extention()
        self.driver.implicitly_wait(60)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.cal.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        select_block = Select(self.driver.find_element_by_name('myBlock'))
        count = 0
        for x in range(len(select_district.options)-1, len(select_district.options)):
            select_district.select_by_index(x)
            self.cal.page_loading(self.driver)
            for y in range(1, len(select_block.options)):
                select_block.select_by_index(y)
                self.cal.page_loading(self.driver)
                value = self.driver.find_element_by_name('myBlock').get_attribute('value')
                cval = value.split(":")
                sval = cval[1].strip()
                nodata = self.driver.find_element_by_id("errMsg").text
                if nodata == "No data found":
                    print(select_block.options[y].text, "no data found!")
                    count = count + 1
                else:
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(3)
                    self.filename = p.get_download_dir() + "/" + self.fname.sc_blockwise()+management+'_clusters_of_block_'+(sval+'_').strip()+self.cal.get_current_date()+'.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print(select_block.options[y].text,"csv file is not downloaded")
                        count = count + 1
                    else:
                        with open(self.filename) as fin:
                            csv_dict = [row for row in csv.DictReader(self.filename)]
                            if len(csv_dict) == 0:
                                print(select_district.options[y].text,"Does not Table records")
                        os.remove(self.filename)
        return count

