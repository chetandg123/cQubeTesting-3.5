import os
import time

from selenium.webdriver.support.select import Select

from Locators.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData

'''Script validating the Graphs , Block level , Cluster level buttons , District , Block and Cluster level metrics 
along with graph '''


class Composite_Report_Across_Metric():
    def __init__(self, driver):
        self.driver = driver

    def test_district_wise(self):
        p = pwd()
        self.cal = GetData()
        self.driver.implicitly_wait(20)
        self.fname = file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(3)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(10)
        self.filename = p.get_download_dir() + "/" + self.fname.composite_district() + management + "_allDistricts_" + self.cal.get_current_date() + '.csv'
        print(self.filename)
        self.cal.page_loading(self.driver)
        return os.path.isfile(self.filename)

    def remove_csv(self):
        os.remove(self.filename)

    def test_blockwise(self):
        p = pwd()
        self.cal = GetData()
        self.fname = file_extention()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.cal.page_loading(self.driver)
        time.sleep(3)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_id('allBlock').click()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        self.filename = p.get_download_dir() + "/" + self.fname.composite_block() + management + '_allBlocks_' + self.cal.get_current_date() + '.csv'
        time.sleep(3)
        print(self.filename)
        return os.path.isfile(self.filename)

    def remove_file(self):
        os.remove(self.filename)

    def test_clusterwise(self):
        p = pwd()
        self.cal = GetData()
        self.fname = file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.cal.page_loading(self.driver)
        time.sleep(3)
        self.driver.find_element_by_id('allCluster').click()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(15)
        self.filename = p.get_download_dir() + "/" + self.fname.composite_cluster() + management + '_allClusters_' + self.cal.get_current_date() + '.csv'
        self.cal.page_loading(self.driver)
        print(self.filename)
        return os.path.isfile(self.filename)

    def test_hyperlink(self):
        self.p = GetData()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        time.sleep(3)
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
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(3)

    def test_xaxis(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        xaxis_lists = Select(self.driver.find_element_by_id('x_axis'))
        self.p.page_loading(self.driver)
        count = len(xaxis_lists.options) - 1
        return count

    def test_yaxis(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        xaxis_lists = Select(self.driver.find_element_by_id('y_axis'))
        self.p.page_loading(self.driver)
        count = len(xaxis_lists.options) - 1
        return count

    def test_xplots(self):
        self.driver.implicitly_wait(30)
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        time.sleep(3)
        dist = Select(self.driver.find_element_by_id("choose_district1"))
        dist.select_by_index(5)
        self.p.page_loading(self.driver)
        xaxis_lists = Select(self.driver.find_element_by_id('x_axis'))
        for i in range(len(xaxis_lists.options)):
            time.sleep(2)
            xaxis_lists.select_by_index(i)
            self.p.page_loading(self.driver)
        self.p.page_loading(self.driver)

    def test_yplots(self):
        self.driver.implicitly_wait(30)
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(3)
        dist = Select(self.driver.find_element_by_id("choose_district1"))
        dist.select_by_index(3)
        self.p.page_loading(self.driver)
        yaxis_lists = Select(self.driver.find_element_by_id('y_axis'))
        for i in range(len(yaxis_lists.options)):
            time.sleep(2)
            yaxis_lists.select_by_index(i)
            self.p.page_loading(self.driver)
        self.p.page_loading(self.driver)

    def test_homeicon(self):
        self.p = GetData()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        dist = Select(self.driver.find_element_by_name("myDistrict"))
        dist.select_by_index(1)
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.homeicon).click()
        self.p.page_loading(self.driver)

    def test_homebutton(self):
        self.p = GetData()
        count = 0
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(3)
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.p.page_loading(self.driver)
        if 'dashboard' in self.driver.current_url:
            print("home button is working fine , landing page is displayed ")
        else:
            print("Landing page is not displayed due to home button click not happened")
            count = count + 1
        self.p.navigate_to_composite_report()
        self.p.page_loading(self.driver)
        return count

    def click_on_blocks_button(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(3)
        self.driver.find_element_by_id('allBlock').click()
        self.data.page_loading(self.driver)
        time.sleep(2)
        graph = self.driver.find_element_by_id('myChart')
        result = graph.is_displayed()
        if True != result:
            print("Block level graph is not displayed ")
            count = count + 1
        xaxis_lists = Select(self.driver.find_element_by_id('x_axis'))
        for i in range(1, len(xaxis_lists.options) - 10):
            time.sleep(2)
            xaxis_lists.select_by_index(i)
            self.data.page_loading(self.driver)
        yaxis_lists = Select(self.driver.find_element_by_id('y_axis'))
        for i in range(1, len(yaxis_lists.options) - 10):
            time.sleep(2)
            yaxis_lists.select_by_index(i)
            self.data.page_loading(self.driver)
        return count

    def click_on_clusters_button(self):
        count = 0
        self.data = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('allCluster').click()
        self.data.page_loading(self.driver)
        graph = self.driver.find_element_by_id('myChart')
        result = graph.is_displayed()
        if True != result:
            print("Cluster level graph is not displayed ")
            count = count + 1
        xaxis_lists = Select(self.driver.find_element_by_id('x_axis'))
        for i in range(1, len(xaxis_lists.options) - 10):
            time.sleep(2)
            xaxis_lists.select_by_index(i)
            self.data.page_loading(self.driver)
        yaxis_lists = Select(self.driver.find_element_by_id('y_axis'))
        for i in range(1, len(yaxis_lists.options) - 10):
            time.sleep(2)
            yaxis_lists.select_by_index(i)
            self.data.page_loading(self.driver)
        return count

    def check_districtwise_csv_download(self):
        p = pwd()
        self.cal = GetData()
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(3)
        self.cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        count = 0

        self.fname = file_extention()
        for x in range(int(len(select_district.options)) - 5, int(len(select_district.options))):
            select_district.select_by_index(x)
            self.cal.page_loading(self.driver)
            value = self.driver.find_element_by_name('myDistrict').get_attribute('value')
            value = value[4:] + '_'
            nodata = self.driver.find_element_by_id("errMsg").text
            if nodata == "No data found":
                print(select_district.options[x].text, "no data found!")
                count = count + 1
            else:
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(3)
                self.filename = p.get_download_dir() + "/" + self.fname.composite_districtwise() + management + '_blocks_of_district_' + value.strip() + self.cal.get_current_date() + '.csv'
                print(self.filename)
                self.cal.page_loading(self.driver)
                self.file = os.path.isfile(self.filename)
                os.remove(self.filename)
            return self.file

    def check_csv_download(self):
        p = pwd()
        self.cal = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        select_block = Select(self.driver.find_element_by_name('myBlock'))
        select_cluster = Select(self.driver.find_element_by_name('myCluster'))
        count = 0
        self.fname = file_extention()
        for x in range(1, int(len(select_district.options)) - 30):
            select_district.select_by_index(x)
            self.cal.page_loading(self.driver)
            for y in range(1, len(select_block.options)):
                select_block.select_by_index(y)
                self.cal.page_loading(self.driver)
                for z in range(1, len(select_cluster.options)):
                    select_cluster.select_by_index(z)
                    self.cal.page_loading(self.driver)
                    value = self.driver.find_element_by_name('myCluster').get_attribute('value')
                    dvalue = value.split(":")
                    val = dvalue[1].strip()
                    nodata = self.driver.find_element_by_id("errMsg").text
                    if nodata == "No data found":
                        print(select_district.options[x].text, select_block.options[y].text,
                              select_cluster.options[z].text, "no data found!")
                        count = count + 1
                    else:
                        self.driver.find_element_by_id(Data.Download).click()
                        time.sleep(3)
                        self.filename = p.get_download_dir() + "/" + self.fname.composite_clusterwise() + management + '_schools_of_cluster_' + val + '_' + self.cal.get_current_date() + '.csv'
                        print(self.filename)
                        self.cal.page_loading(self.driver)
                        self.file = os.path.isfile(self.filename)
                        os.remove(self.filename)
                    return self.file

    def check_csv_download_district_block(self):
        p = pwd()
        self.cal = GetData()
        self.driver.implicitly_wait(60)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.cal.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        select_block = Select(self.driver.find_element_by_name('myBlock'))
        count = 0
        self.fname = file_extention()
        for x in range(1, int(len(select_district.options)) - 26):
            select_district.select_by_index(x)
            self.cal.page_loading(self.driver)
            for y in range(1, len(select_block.options)):
                select_block.select_by_index(y)
                self.cal.page_loading(self.driver)
                value = self.driver.find_element_by_name('myBlock').get_attribute('value')
                dvalue = value.split(":")
                val = dvalue[1].strip()
                nodata = self.driver.find_element_by_id("errMsg").text
                if nodata == "No data found":
                    print(select_district.options[x].text, select_block.options[y].text,
                          "no data found!")
                    count = count + 1
                else:
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(3)
                    self.filename = p.get_download_dir() + "/" + self.fname.composite_blockwise() + management + '_clusters_of_block_' + val + '_' + self.cal.get_current_date() + '.csv'
                    print(self.filename)
                    self.cal.page_loading(self.driver)
                    self.file = os.path.isfile(self.filename)
                    os.remove(self.filename)
                return self.file

    def test_schoolwise(self):
        self.cal = GetData()
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.cal.page_loading(self.driver)
        p = pwd()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        dist = Select(self.driver.find_element_by_name('myDistrict'))
        dist.select_by_index(1)
        self.cal.page_loading(self.driver)
        blk = Select(self.driver.find_element_by_name('myBlock'))
        blk.select_by_index(1)
        self.cal.page_loading(self.driver)
        clu = Select(self.driver.find_element_by_name('myCluster'))
        clu.select_by_index(1)
        value = self.driver.find_element_by_name('myCluster').get_attribute('value')
        value = value[3:] + '_'
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        self.cal.page_loading(self.driver)
        self.filename = p.get_download_dir() + "/" + self.fname.composite_clusterwise() + management + "_" + 'schools_of_cluster_' + value.strip() + self.cal.get_current_date() + '.csv'
        print(self.filename)
        self.cal.page_loading(self.driver)
        return os.path.isfile(self.filename)
