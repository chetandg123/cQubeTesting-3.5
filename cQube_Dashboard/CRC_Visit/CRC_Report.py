import csv
import os
import re
import time

import pandas as pd
from selenium.webdriver.support.select import Select

from Locators.parameters import Data
from reuse_func import GetData


class crc_visits():
    def __init__(self,driver):
        self.driver = driver
        self.filename=''

    def remove_file(self):
        os.remove(self.filename)
    def test_blocklevel(self):
        self.cal = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.cal.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        count = 0
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            self.cal.page_loading(self.driver)
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            p = pwd()
            self.filename = p.get_download_dir() + "/Block_level_CRC_Report.csv"
            self.cal.page_loading(self.driver)
            if os.path.isfile(self.filename) != True:
                print("District" + select_district.first_selected_option.text + "csv is not downloaded")
                count = count + 1
            if os.path.isfile(self.filename) == True:
                os.remove(self.filename)
        self.cal.page_loading(self.driver)
        return count

    def test_crc(self):
        self.p = GetData()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        self.p.navigate_to_crc_report()
        self.p.page_loading(self.driver)

    def test_districtwise(self):
        p =pwd()
        count = 0
        self.cal = GetData()
        self.driver.implicitly_wait(20)
        self.fname =file_extention()
        self.driver.find_element_by_xpath(Data.hyper).click()
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        self.cal.page_loading(self.driver)
        District_wise=Select(self.driver.find_element_by_id("downloader"))
        # District_wise.select_by_visible_text(" District Wise Report ")
        District_wise.select_by_index(1)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        self.filename = p.get_download_dir() + '/' + self.fname.crc_district()+name+'_overall_allDistricts_'+self.cal.get_current_date()+'.csv'
        if not os.path.isfile(self.filename):
            print("District wise csv file not downloaded")
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                tschools = 0
                vsts = 0
                vstd = 0
                for row in csv.reader(fin):
                    tschools += int(row[0])
                    vsts += int(row[2])
                    vstd += int(row[1])
                totalschools = self.driver.find_element_by_id("schools").text
                visited = self.driver.find_element_by_id("visited").text
                visits = self.driver.find_element_by_id("visits").text
                tsc = re.sub('\D', "", totalschools)
                vs = re.sub('\D', "", visits)
                vd = re.sub('\D', "", visited)
                if int(tsc) != tschools:
                    print("total no of schools  :", tschools,
                          int(tsc), "records are mismatch found")
                    count = count + 1
                if int(vs) != vsts:
                    print("total no of visits  :", int(vs), vsts,
                          "records are mismatch found")
                    count = count + 1
                if int(vd) != vstd:
                    print("Total no of visits  :", int(vd), vstd,
                          "records are mismatch found")
                    count = count + 1

            os.remove(self.filename)
        return count

    def test_blockwise(self):
        p =pwd()
        count = 0
        self.cal  = GetData()
        self.fname = file_extention()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.cal.page_loading(self.driver)
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        District_wise=Select(self.driver.find_element_by_id("downloader"))
        # District_wise.select_by_visible_text(" Block Wise Report ")
        District_wise.select_by_index(2)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(4)
        self.filename = p.get_download_dir() + '/' + self.fname.crc_block()+name+'_overall_allBlocks_'+self.cal.get_current_date()+'.csv'
        print(self.filename)
        if not os.path.isfile(self.filename):
            print("District wise csv file not downloaded")
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                tschools = 0
                vsts = 0
                vstd = 0
                for row in csv.reader(fin):
                    tschools += int(row[0])
                    vsts += int(row[2])
                    vstd += int(row[1])
                totalschools = self.driver.find_element_by_id("schools").text
                visited = self.driver.find_element_by_id("visited").text
                visits = self.driver.find_element_by_id("visits").text
                tsc = re.sub('\D', "", totalschools)
                vs = re.sub('\D', "", visits)
                vd = re.sub('\D', "", visited)
                if int(tsc) != tschools:
                    print("total no of schools  :", tschools,
                          int(tsc), "records are mismatch found")
                    count = count + 1
                if int(vs) != vsts:
                    print("total no of visits  :", int(vs), vsts,
                          "records are mismatch found")
                    count = count + 1
                if int(vd) != vstd:
                    print("Total no of visits  :", int(vd), vstd,
                          "records are mismatch found")
                    count = count + 1

            os.remove(self.filename)
        return count

    def test_clusterwise(self):
        p = pwd()
        count = 0
        self.cal = GetData()
        self.fname=file_extention()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.cal.page_loading(self.driver)
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        District_wise = Select(self.driver.find_element_by_id("downloader"))
        # District_wise.select_by_visible_text(" Cluster Wise Report ")
        District_wise.select_by_index(3)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        self.filename = p.get_download_dir() + '/' + self.fname.crc_cluster()+name+'_overall_allClusters_'+self.cal.get_current_date()+'.csv'
        print(self.filename)
        if not os.path.isfile(self.filename):
            print("District wise csv file not downloaded")
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                tschools = 0
                vsts = 0
                vstd = 0
                for row in csv.reader(fin):
                    tschools += int(row[0])
                    vsts += int(row[2])
                    vstd += int(row[1])
                totalschools = self.driver.find_element_by_id("schools").text
                visited = self.driver.find_element_by_id("visited").text
                visits = self.driver.find_element_by_id("visits").text
                tsc = re.sub('\D', "", totalschools)
                vs = re.sub('\D', "", visits)
                vd = re.sub('\D', "", visited)
                if int(tsc) != tschools:
                    print("total no of schools  :", tschools,
                          int(tsc), "records are mismatch found")
                    count = count + 1
                if int(vs) != vsts:
                    print("total no of visits  :", int(vs), vsts,
                          "records are mismatch found")
                    count = count + 1
                if int(vd) != vstd:
                    print("Total no of visits  :", int(vd), vstd,
                          "records are mismatch found")
                    count = count + 1

            os.remove(self.filename)
        return count

    def test_schoolwise(self):
        count = 0
        self.cal = GetData()
        self.fname=file_extention()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.cal.page_loading(self.driver)
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        p =pwd()
        District_wise=Select(self.driver.find_element_by_id("downloader"))
        # District_wise.select_by_visible_text(" School Wise Report ")
        District_wise.select_by_index(4)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        self.cal.page_loading(self.driver)
        self.filename = p.get_download_dir() + '/' + self.fname.crc_school()+name+'_overall_allSchools_'+self.cal.get_current_date()+'.csv'
        self.cal.page_loading(self.driver)
        if not os.path.isfile(self.filename):
            print("District wise csv file not downloaded")
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                tschools = 0
                vsts = 0
                vstd = 0
                for row in csv.reader(fin):
                    tschools += int(row[0])
                    vsts += int(row[2])
                    vstd += int(row[1])
                totalschools = self.driver.find_element_by_id("schools").text
                visited = self.driver.find_element_by_id("visited").text
                visits = self.driver.find_element_by_id("visits").text
                tsc = re.sub('\D', "", totalschools)
                vs = re.sub('\D', "", visits)
                vd = re.sub('\D', "", visited)
                if int(tsc) != tschools:
                    print("total no of schools  :", tschools,
                          int(tsc), "records are mismatch found")
                    count = count + 1
                if int(vs) != vsts:
                    print("total no of visits  :", int(vs), vsts,
                          "records are mismatch found")
                    count = count + 1
                if int(vd) != vstd:
                    print("Total no of visits  :", int(vd), vstd,
                          "records are mismatch found")
                    count = count + 1

            os.remove(self.filename)
        return count

    def test_districtwise(self):
        p = pwd()
        self.cal = GetData()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.cal.page_loading(self.driver)
        self.year , self.month = self.cal.get_crc_month_and_year_values()
        print(self.year,self.month , type(self.year),type(self.month))
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        count = 0
        self.fname=file_extention()
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            self.cal.page_loading(self.driver)
            value = self.driver.find_element_by_name('myDistrict').get_attribute('value')
            value=value.split(":")
            distval= value[1].strip()
            nodata = self.driver.find_element_by_id("errMsg").text
            if nodata == "No data found":
                print(select_district.options[x].text, "no data found!")
                count = count + 1
            else:
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(4)
                self.filename = p.get_download_dir() + "/" + self.fname.crc_districtwise()+name+"_"+self.year+"_"+str(self.month)+'_blocks_of_district_'+distval+'_'+self.cal.get_current_date()+'.csv'

                print(self.filename)
                if os.path.isfile(self.filename) != True:
                    print(select_district.options[x].text,'csv file is not downloaded')
                    count = count + 1
                else:
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        tschools = 0
                        vsts = 0
                        vstd = 0
                        for row in csv.reader(fin):
                            tschools += int(row[0])
                            vsts +=int(row[2])
                            vstd +=int(row[1])
                        totalschools = self.driver.find_element_by_id("schools").text
                        visited = self.driver.find_element_by_id("visited").text
                        visits = self.driver.find_element_by_id("visits").text
                        tsc = re.sub('\D',"",totalschools)
                        vs = re.sub('\D',"",visits)
                        vd= re.sub('\D', "",visited)
                        if int(tsc) != tschools:
                            print(select_district.options[x].text, ":", "total no of schools  :",tschools, int(tsc),"records are mismatch found")
                        if int(vs) != vsts:
                            print(select_district.options[x].text, ":", "total no of visits  :",int(vs) , vsts,"records are mismatch found")
                        if int(vd) != vstd:
                            print(select_district.options[x].text, ":", "total no of visits  :", int(vd), vstd,
                                  "records are mismatch found")
                    os.remove(self.filename)
        return count

    def test_homeicon(self):
        self.p = GetData()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        dist = Select(self.driver.find_element_by_name("myDistrict"))
        dist.select_by_index(1)
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.homeicon).click()
        self.p.page_loading(self.driver)
        down = self.driver.find_element_by_id(Data.Download)
        time.sleep(3)
        return down.is_displayed()

    def test_homebutton(self):
        self.p = GetData()
        count = 0
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.p.page_loading(self.driver)
        if 'dashboard' in self.driver.current_url:
            print("home button is working fine , landing page is displayed ")
        else:
            print("Landing page is not displayed due to homebutton click not happened")
            count = count + 1
        self.p.navigate_to_crc_report()
        self.p.page_loading(self.driver)
        return count

    def check_csv_download(self):
        p = pwd()
        self.cal = GetData()
        self.fname =file_extention()
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.cal.page_loading(self.driver)
        self.year,self.month = self.cal.get_crc_month_and_year_values()
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        select_block = Select(self.driver.find_element_by_name('myBlock'))
        count = 0
        for x in range(int(len(select_district.options))-1, int(len(select_district.options))):
            select_district.select_by_index(x)
            self.cal.page_loading(self.driver)
            for y in range(1, len(select_block.options)):
                select_block.select_by_index(y)
                self.cal.page_loading(self.driver)
                cluval = self.driver.find_element_by_name('myBlock').get_attribute('value')
                cluval = cluval.split(":")
                value = cluval[1].strip()
                nodata = self.driver.find_element_by_id("errMsg").text
                if nodata == "No data found":
                    print(select_district.options[x].text, select_block.options[y].text,"no data found!")
                    count = count + 1
                else:
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(3)
                    self.filename = p.get_download_dir() + '/' + self.fname.crc_blockwise()+name+"_"+self.year+"_"+str(self.month)+'_clusters_of_block_' + value.strip() +"_"+ self.cal.get_current_date() + '.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print(select_block.options[y].text, " csv file not downloaded")
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            tschools = 0
                            vsts = 0
                            vstd = 0
                            for row in csv.reader(fin):
                                tschools += int(row[0])
                                vsts += int(row[2])
                                vstd += int(row[1])
                            totalschools = self.driver.find_element_by_id("schools").text
                            visited = self.driver.find_element_by_id("visited").text
                            visits = self.driver.find_element_by_id("visits").text
                            tsc = re.sub('\D', "", totalschools)
                            vs = re.sub('\D', "", visits)
                            vd = re.sub('\D', "", visited)
                            if int(tsc) != tschools:
                                print(select_district.options[x].text, ":", "total no of schools  :", tschools,
                                      int(tsc), "records are mismatch found")
                                count = count + 1
                            if int(vs) != vsts:
                                print(select_district.options[x].text, ":", "total no of visits  :", int(vs), vsts,
                                      "records are mismatch found")
                                count = count + 1
                            if int(vd) != vstd:
                                print(select_district.options[x].text, ":", "total no of visits  :", int(vd), vstd,
                                      "records are mismatch found")
                                count = count + 1
                        os.remove(self.filename)
            return count
    def test_table_data(self):
        self.p = GetData()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        count = 0
        for k in range(1, len(select_district.options)):
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
            if number_of_rows == 0:
                count = count + 1
                print("District" + select_district.first_selected_option.text + "table data not found")
        return count

    def test_logout(self):
        self.p = GetData()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.logout).click()
        self.p.page_loading(self.driver)
        if "Log in to cQube" in self.driver.title:
            print("login page is displayed")
        else:
            print("logout is not working")
        data = GetData()
        data.login_cqube(self.driver)
        self.p.page_loading(self.driver)
        data.navigate_to_crc_report()

    def test_plots(self):
        self.driver.implicitly_wait(30)
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        dist = Select(self.driver.find_element_by_id("choose_dist"))
        dist.select_by_index(5)
        self.p.page_loading(self.driver)
        xaxis_lists = Select(self.driver.find_element_by_id('x-axis'))
        yaxis_lists = Select(self.driver.find_element_by_id('y-axis'))
        count1 = len(xaxis_lists.options)-1
        count2 = len(yaxis_lists.options)-1
        for i in range(len(xaxis_lists.options)):
            time.sleep(2)
            xaxis_lists.select_by_index(i)
            self.p.page_loading(self.driver)

        for i in range(len(yaxis_lists.options)):
            time.sleep(2)
            yaxis_lists.select_by_index(i)
            self.p.page_loading(self.driver)
        return count1,count2

    def test_order(self):
        self.p =GetData()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        title = self.driver.find_element_by_id(Data.cQube_logo).text
        self.p.navigate_to_crc_report()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.t_head).click()
        self.p.page_loading(self.driver)
        values = self.driver.find_elements_by_xpath("//th[1]")
        for i in values:
            print(i.get_attribute("aria-sort"))

        self.p.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.t_head).click()
        self.p.page_loading(self.driver)
        value = self.driver.find_elements_by_xpath("//th[1]")
        for i in value:
            print(i.get_attribute("aria-sort"))

        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        return title

    def test_hyperlink(self):
        self.p = GetData()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        dist = Select(self.driver.find_element_by_name("myDistrict"))
        dist.select_by_index(1)
        self.p.page_loading(self.driver)
        block = Select(self.driver.find_element_by_name("myBlock"))
        block.select_by_index(1)
        self.p.page_loading(self.driver)
        # cluster = Select(self.driver.find_element_by_name("myCluster"))
        # cluster.select_by_index(1)
        self.p.page_loading(self.driver)
        # self.driver.find_element_by_xpath(Locators.school_hyper).click()
        # self.p.page_loading(self.driver)
        # self.driver.find_element_by_xpath(Locators.cluster_hyper).click()
        # self.p.page_loading(self.driver)
        # self.driver.find_element_by_xpath(Locators.dist_hyper).click()
        self.driver.find_element_by_id(Data.homeicon).click()
        self.p.page_loading(self.driver)

