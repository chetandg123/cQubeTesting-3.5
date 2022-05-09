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


class tpd_completion_percentage_report():
    def __init__(self, driver):
        self.driver = driver

    def test_completion_percentage_icon(self):
        self.data = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(1)
        if 'dashboard' in self.driver.current_url:
            print('cQube landing page is displayed')
        else:
            print('Homebtn is not working ')
            count = count + 1
        self.data.page_loading(self.driver)
        self.data.navigate_to_tpd_completion_percentage()
        if 'tpd-completion' in self.driver.current_url:
            print('TPD Completion percentage report is displayed ')
        else:
            print('TPD Completion percentage icon is not working ')
            count = count + 1
        self.data.page_loading(self.driver)
        return count

    def test_dashboard_completion_report(self):
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
        self.data.navigate_to_tpd_completion_percentage()
        self.data.page_loading(self.driver)
        if 'tpd-completion' in self.driver.current_url:
            print("Completion percentage report is displayed")
        else:
            print('Completion percentage report is not present ')
            count = count + 1
        self.data.page_loading(self.driver)
        return count

    def test_homeicon_functionality(self):
        self.data = GetData()
        self.p = pwd()
        0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_id(Data.sar_district))
        timeseries.select_by_index(5)
        self.data.page_loading(self.driver)
        # present = self.driver.find_element_by_id(Locators.homeicon).is_Displayed()
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
        self.data.navigate_to_tpd_completion_percentage()
        self.data.page_loading(self.driver)
        return count

    def test_hyperlink_function(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        # timeseries = Select(self.driver.find_element_by_name(Locators.timeperiods))
        # timeseries.select_by_visible_text(' Last 7 Days ')
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        print("Checked with hyper link function")
        self.data.page_loading(self.driver)

    def test_check_download_icon(self):
        self.data = GetData()
        count = 0
        self.p = pwd()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        self.filename = self.p.get_download_dir() + '/' + "completion_percentage_all_district_overall_" + self.data.get_current_date() + '.csv'
        if os.path.isfile(self.filename) != True:
            print('Districtwise csv file is not downloaded')
            count = count + 1
        self.data.page_loading(self.driver)
        os.remove(self.filename)
        return count

    def test_district_selectbox(self):
        self.driver.implicitly_wait(200)
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        districts = Select(self.driver.find_element_by_id(Data.sar_district))
        collections = Select(self.driver.find_element_by_id(Data.coll_names))
        coll_count = len(collections.options) - 1
        for i in range(1, len(districts.options) - 28):
            districts.select_by_index(i)
            name = self.driver.find_element_by_id(Data.sar_district).get_attribute('value')
            value = name[4:] + '_'

            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + "/" + "completion_percentage_overall_" + value.strip() + self.data.get_current_date() + ".csv"
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print(districts.options[i].text, 'csv file is not downloaded')
                count = count + 1
            self.data.page_loading(self.driver)
            os.remove(self.filename)
            for j in range(len(collections.options) - 2, len(collections.options)):
                time.sleep(1)
                collections.select_by_index(j)
                self.data.page_loading(self.driver)

        return count, coll_count

    def test_blocks_selectbox(self):
        self.driver.implicitly_wait(100)
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        districts = Select(self.driver.find_element_by_id(Data.sar_district))
        blocks = Select(self.driver.find_element_by_id(Data.sar_block))
        collections = Select(self.driver.find_element_by_id(Data.coll_names))
        coll_count = len(collections.options) - 1
        for i in range(len(districts.options) - 1, len(districts.options)):
            districts.select_by_index(i)
            self.data.page_loading(self.driver)
            for j in range(1, len(blocks.options)):
                blocks.select_by_index(j)
                name = self.driver.find_element_by_id(Data.sar_block).get_attribute('value')
                value = name[3:] + '_'
                self.data.page_loading(self.driver)
                time.sleep(2)
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + "/completion_percentage_overall_" + value.strip() + self.data.get_current_date() + ".csv"
                print(self.filename)
                if os.path.isfile(self.filename) != True:
                    print(districts.options[i].text, 'csv file is not downloaded')
                    count = count + 1
                self.data.page_loading(self.driver)
                os.remove(self.filename)
                for k in range(len(collections.options) - 2, len(collections.options)):
                    collections.select_by_index(k)
                    self.data.page_loading(self.driver)
        return count, coll_count

    def test_clusters_selectbox(self):
        self.driver.implicitly_wait(100)
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        districts = Select(self.driver.find_element_by_id(Data.sar_district))
        blocks = Select(self.driver.find_element_by_id(Data.sar_block))
        clusters = Select(self.driver.find_element_by_id(Data.sar_cluster))
        collections = Select(self.driver.find_element_by_id(Data.coll_names))
        coll_count = len(collections.options) - 1
        for i in range(len(districts.options) - 1, len(districts.options)):
            districts.select_by_index(i)
            print(districts.options[i].text)
            self.data.page_loading(self.driver)
            for j in range(1, len(blocks.options)):
                blocks.select_by_index(j)
                print(blocks.options[j].text)
                self.data.page_loading(self.driver)
                for k in range(len(clusters.options) - 1, len(clusters.options)):
                    clusters.select_by_index(k)
                    name = self.driver.find_element_by_id(Data.sar_cluster).get_attribute('value')
                    value = name.split(":")
                    val = value[1].strip()
                    self.data.page_loading(self.driver)
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(3)
                    self.filename = self.p.get_download_dir() + "/" + 'completion_percentage_overall_' + val + '_' + self.data.get_current_date() + ".csv"
                    print(self.filename)
                    if os.path.isfile(self.filename) != True:
                        print(districts.options[i].text, blocks.options[j].text, clusters.options[k].text,
                              'csv file is not downloaded')
                        count = count + 1
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            # enrolls = 0
                            # for row in csv.reader(fin):
                            #     enrolls += int(row[12])
                            # totalenrollment = self.driver.find_element_by_id("totalCount").text
                            # enrol = re.sub('\D', "", totalenrollment)
                            # if int(enrol) != int(enrolls):
                            #     print(int(enrol) != int(enrolls), 'mis match found at enrollment count')
                            #     count = count + 1
                    os.remove(self.filename)
                    self.data.page_loading(self.driver)
        return count

    def click_on_logout_btn(self):
        self.data = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.logout).click()
        self.data.page_loading(self.driver)
        if 'Log in to cQube' in self.driver.title:
            print('Logout button is working ')
        else:
            print('Logout is not working')
            count = count + 1
        self.data.login_cqube(self.driver)
        self.data.navigate_to_tpd_completion_percentage()
        self.data.page_loading(self.driver)
        return count

    def test_download_collection_options(self):
        self.data = GetData()
        count = 0
        self.p = pwd()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        colls = Select(self.driver.find_element_by_id(Data.coll_names))
        colcount = len(colls.options) - 1
        for i in range(1, len(colls.options) - 1):
            time.sleep(1)
            colls.select_by_index(i)
            time.sleep(5)
            self.data.page_loading(self.driver)
            name = colls.options[i].text
            # self.driver.find_element_by_id(Locators.Download).click()
            # time.sleep(3)
            # self.filename = self.p.get_download_dir() +"/completion_percentage_overall_undefined_"+self.data.get_current_date()+".csv"
            # print(self.filename)
            # if os.path.isfile(self.filename) != True:
            #     print(colls.options[i].text,"csv file is not downloaded ")
            #     count = count + 1
            #     self.data.page_loading(self.driver)
            # os.remove(self.filename)
        return colcount, count

    def test_districtwise_collections(self):
        self.data = GetData()
        count = 0
        self.p = pwd()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        district = Select(self.driver.find_element_by_id(Data.sar_district))
        colls = Select(self.driver.find_element_by_id(Data.coll_names))
        colcount = len(colls.options) - 1
        self.data.page_loading(self.driver)
        for j in range(1, len(district.options) - 28):
            district.select_by_index(j)
            self.data.page_loading(self.driver)
            value = self.driver.find_element_by_id(Data.sar_district).get_attribute('value')
            value = value[4:]
            for i in range(1, len(colls.options)):
                colls.select_by_index(i)
                self.data.page_loading(self.driver)
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + "/" + "completion_percentage_overall_" + value.strip() + '_' + self.data.get_current_date() + ".csv"
                print(self.filename)
                if os.path.isfile(self.filename) != True:
                    print(colls.options[i].text, "csv file is not downloaded ")
                    count = count + 1
                    self.data.page_loading(self.driver)
                os.remove(self.filename)
        return colcount, count

    def test_blockwise_collections(self):
        self.data = GetData()
        count = 0
        self.p = pwd()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        district = Select(self.driver.find_element_by_id(Data.sar_district))
        block = Select(self.driver.find_element_by_id(Data.sar_block))
        colls = Select(self.driver.find_element_by_id(Data.coll_names))
        colcount = len(colls.options) - 1
        self.data.page_loading(self.driver)
        for j in range(1, len(district.options) - 32):
            district.select_by_index(j)
            for k in range(1, len(block.options) - 2):
                block.select_by_index(k)
                self.data.page_loading(self.driver)
                value = self.driver.find_element_by_id(Data.sar_block).get_attribute('value')
                value = value[5:] + '_'
                for i in range(1, len(colls.options)):
                    colls.select_by_index(i)
                    self.data.page_loading(self.driver)
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(3)
                    self.filename = self.p.get_download_dir() + "/" + "completion_percentage_overall_" + value.strip() + '_' + self.data.get_current_date() + ".csv"
                    print(self.filename)
                    if os.path.isfile(self.filename) != True:
                        print(colls.options[i].text, "csv file is not downloaded ")
                        count = count + 1
                        self.data.page_loading(self.driver)
                    os.remove(self.filename)
        return colcount, count

    def test_clusterwise_collections(self):
        self.data = GetData()
        count = 0
        self.p = pwd()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        district = Select(self.driver.find_element_by_id(Data.sar_district))
        block = Select(self.driver.find_element_by_id(Data.sar_block))
        cluster = Select(self.driver.find_element_by_id(Data.sar_cluster))
        colls = Select(self.driver.find_element_by_id(Data.coll_names))
        colcount = len(colls.options) - 1
        self.data.page_loading(self.driver)
        for j in range(1, len(district.options) - 32):
            district.select_by_index(j)
            for k in range(1, len(block.options) - 3):
                block.select_by_index(k)
                for m in range(1, len(cluster.options)):
                    cluster.select_by_index(m)
                    self.data.page_loading(self.driver)
                    value = self.driver.find_element_by_id(Data.sar_cluster).get_attribute('value')
                    value = value[5:] + '_'
                    for i in range(1, len(colls.options)):
                        colls.select_by_index(i)
                        self.data.page_loading(self.driver)
                        self.driver.find_element_by_id(Data.Download).click()
                        time.sleep(3)
                        self.filename = self.p.get_download_dir() + "/" + "completion_percentage_overall_" + value.strip() + '_' + self.data.get_current_date() + ".csv"
                        print(self.filename)
                        if os.path.isfile(self.filename) != True:
                            print(colls.options[i].text, "csv file is not downloaded ")
                            count = count + 1
                            self.data.page_loading(self.driver)
                        os.remove(self.filename)
        return colcount, count

    def test_overall_rawfile_download(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        if " No Locators Available " in self.driver.page_source:
            print("Report is not having data..")
            return count
        else:
            self.driver.find_element_by_id('rawDownload').click()
            time.sleep(35)
            self.filename = self.p.get_download_dir() + "/overall.csv"
            if os.path.isfile(self.filename) != True:
                print('Downlaod raw file is not downloaded')
                count = count + 1
            else:
                print('Download raw file is downloaded..')
                os.remove(self.filename)
            return count
