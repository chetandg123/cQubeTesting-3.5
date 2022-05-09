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


class tpd_course_progress_report():
    def __init__(self, driver):
        self.fname = None
        self.data = None
        self.driver = driver

    def check_last_day_districtwise_download(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        periods = Select(self.driver.find_element_by_id(Data.timeperiods))
        # periods.select_by_visible_text(' Last Day ')
        periods.select_by_index(4)
        self.data.page_loading(self.driver)
        if self.fname.no_data_found() in self.driver.page_source:
            print('Last Day does not having records')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + "/" + self.fname.tpd_lastday() + self.data.get_current_date() + '.csv'
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print('Last Day Districtwise csv file is not downloaded ')
                count = count + 1
            else:
                print('Last day districtwise csv file is downloaded')
                with open(self.filename) as fin:
                    csv_reader = csv.reader(fin, delimiter=',')
                    header = next(csv_reader)
                    data = list(csv_reader)
                    row_count = len(data)
                os.remove(self.filename)
                time.sleep(2)
                if row_count == 0:
                    print("records are not found in csv file ")
                    count = count + 1
        return count

    def check_last_30_day_districtwise_download(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        periods = Select(self.driver.find_element_by_id(Data.timeperiods))
        # periods.select_by_visible_text(' Last 30 Days ')
        periods.select_by_index(2)
        self.data.page_loading(self.driver)
        if self.fname.no_data_found() in self.driver.page_source:
            print('Last Day does not having records')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + "/" + self.fname.tpd_lastmonth() + self.data.get_current_date() + '.csv'
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print('Last Day Districtwise csv file is not downloaded ')
                count = count + 1
            else:
                print('Last day districtwise csv file is downloaded')
                with open(self.filename) as fin:
                    csv_reader = csv.reader(fin, delimiter=',')
                    header = next(csv_reader)
                    data = list(csv_reader)
                    row_count = len(data)
                os.remove(self.filename)
                time.sleep(2)
                if row_count == 0:
                    print("records are not found in csv file ")
                    count = count + 1
        return count

    def check_last_7_days_districtwise_download(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        periods = Select(self.driver.find_element_by_id(Data.timeperiods))
        # periods.select_by_visible_text(' Last 7 Days ')
        periods.select_by_index(3)
        self.data.page_loading(self.driver)
        if self.fname.no_data_found() in self.driver.page_source:
            print('Last 7 Day does not having records')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + "/" + self.fname.tpd_lastweek() + self.data.get_current_date() + '.csv'
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print('Last Day Districtwise csv file is not downloaded ')
                count = count + 1
            else:
                print('Last day districtwise csv file is downloaded')
                with open(self.filename) as fin:
                    csv_reader = csv.reader(fin, delimiter=',')
                    header = next(csv_reader)
                    data = list(csv_reader)
                    row_count = len(data)
                os.remove(self.filename)
                time.sleep(2)
                if row_count == 0:
                    print("records are not found in csv file ")
                    count = count + 1
        return count

    def check_all_districtwise_download(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        self.filename = self.p.get_download_dir() + "/" + self.fname.tpd_districts() + self.data.get_current_date() + '.csv'
        if os.path.isfile(self.filename) != True:
            print('All Districtwise csv file is not downloaded ')
            count = count + 1
        else:
            print('All districtwise csv file is downloaded')
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                data = list(csv_reader)
                row_count = len(data)
            os.remove(self.filename)
            time.sleep(2)
            if row_count == 0:
                print("records are not found in csv file ")
                count = count + 1
        return count

    def test_homeicons(self):
        self.load = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_id(Data.timeperiods))
        timeseries.select_by_index(2)
        self.load.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.load.page_loading(self.driver)
        self.load.navigate_to_tpd_content_progress()
        self.load.page_loading(self.driver)

    def test_homebutton(self):
        self.load = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.load.page_loading(self.driver)
        self.load.navigate_to_tpd_content_progress()
        self.load.page_loading(self.driver)
        if 'tpd-course-progress' in self.driver.current_url:
            print('TPD course progress chart is present ')
        else:
            print('TPD course progress chart is not present in report')
            count = count + 1
        self.load.page_loading(self.driver)
        return count

    def test_all_districtwise(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        self.fname = file_extention()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        dists = Select(self.driver.find_element_by_id(Data.district_dropdown))
        period = Select(self.driver.find_element_by_id(Data.timeperiods))
        # period.select_by_visible_text(' Overall ')
        period.select_by_index(1)
        print(period.first_selected_option)
        self.load.page_loading(self.driver)
        for i in range(1, len(dists.options)):
            dists.select_by_index(i)
            time.sleep(2)
            value = self.driver.find_element_by_id(Data.district_dropdown).get_attribute('value')
            value = value.split(":")
            self.load.page_loading(self.driver)
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + "/" + self.fname.tpd_all_districtwise() + value[
                1].strip() + '_' + self.load.get_current_date() + '.csv'
            file = os.path.isfile(self.filename)
            if file != True:
                print(dists.options[i].text, 'District wise records csv file is not downloaded')
                count = count + 1
            else:
                with open(self.filename) as fin:
                    csv_reader = csv.reader(fin, delimiter=',')
                    header = next(csv_reader)
                    data = list(csv_reader)
                    row_count = len(data)
                os.remove(self.filename)
                time.sleep(2)
                if row_count == 0:
                    print("records are not found in csv file ")
                    count = count + 1
            return count

        return count

    def test_last_day_districtwise(self):
        self.driver.implicitly_wait(100)
        self.p = pwd()
        self.load = GetData()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        dists = Select(self.driver.find_element_by_id(Data.district_dropdown))
        period = Select(self.driver.find_element_by_id(Data.timeperiods))
        # period.select_by_visible_text(' Last Day ')
        period.select_by_index(4)
        self.load.page_loading(self.driver)
        if self.fname.no_data_found() in self.driver.page_source:
            print("Last 7 days does not have records ")
        else:
            for i in range(1, len(dists.options)):
                dists.select_by_index(i)
                time.sleep(2)
                value = self.driver.find_element_by_id(Data.district_dropdown).get_attribute('value')
                value = value.split(":")
                self.load.page_loading(self.driver)
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + "/" + self.fname.tpd_lastday_districtwise() + value[
                    1].strip() + '_' + self.load.get_current_date() + '.csv'
                print(self.filename)
                file = os.path.isfile(self.filename)
                if file != True:
                    print(dists.options[i].text, 'District wise records csv file is not downloaded')
                    count = count + 1
                else:
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        data = list(csv_reader)
                        row_count = len(data)
                    os.remove(self.filename)
                    time.sleep(2)
                    if row_count == 0:
                        print("records are not found in csv file ")
                        count = count + 1
        return count

    def test_last_7_days_districtwise(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        dists = Select(self.driver.find_element_by_id(Data.district_dropdown))
        period = Select(self.driver.find_element_by_id(Data.timeperiods))
        # period.select_by_visible_text(' Last 7 Days ')
        period.select_by_index(3)
        self.load.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print("Last 7 days does not have records ")
        else:
            for i in range(1, len(dists.options)):
                dists.select_by_index(i)
                time.sleep(2)
                value = self.driver.find_element_by_id(Data.district_dropdown).get_attribute('value')
                value = value.split(":")
                self.load.page_loading(self.driver)
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + "/" + self.fname.tpd_lastweek_districtwise() + value[
                    1].strip() + '_' + self.load.get_current_date() + '.csv'
                print(self.filename)
                file = os.path.isfile(self.filename)
                if file != True:
                    print(dists.options[i].text, 'District wise records csv file is not downloaded')
                    count = count + 1
                else:
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        data = list(csv_reader)
                        row_count = len(data)
                    os.remove(self.filename)
                    time.sleep(2)
                    if row_count == 0:
                        print("records are not found in csv file ")
                        count = count + 1
        return count

    def test_last_30_days_districtwise(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        self.driver.implicitly_wait(50)
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        dists = Select(self.driver.find_element_by_id(Data.district_dropdown))
        period = Select(self.driver.find_element_by_id(Data.timeperiods))
        # period.select_by_visible_text(' Last 30 Days ')
        period.select_by_index(2)
        self.load.page_loading(self.driver)
        if self.fname.no_data_found() in self.driver.page_source:
            print("Last 7 days does not have records ")
        else:
            for i in range(1, len(dists.options)):
                dists.select_by_index(i)
                time.sleep(2)
                value = self.driver.find_element_by_id(Data.district_dropdown).get_attribute('value')
                value = value[4:] + '_'
                self.load.page_loading(self.driver)
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + "/" + self.fname.tpd_lastmonth_districtwise() + value.strip() + self.load.get_current_date() + '.csv'
                print(self.filename)
                file = os.path.isfile(self.filename)
                if file != True:
                    print(dists.options[i].text, 'District wise records csv file is not downloaded')
                    count = count + 1
                else:
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        data = list(csv_reader)
                        row_count = len(data)
                    os.remove(self.filename)
                    time.sleep(2)
                    if row_count == 0:
                        print("records are not found in csv file ")
                        count = count + 1
                    self.load.page_loading(self.driver)
        return count

    def Blocks_select_box(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        dists = Select(self.driver.find_element_by_id(Data.district_dropdown))
        Blocks = Select(self.driver.find_element_by_id(Data.blocks_dropdown))
        for i in range(len(dists.options) - 1, len(dists.options)):
            dists.select_by_index(i)
            self.load.page_loading(self.driver)
            for j in range(len(Blocks.options), len(Blocks.options)):
                Blocks.select_by_index(j)
                self.load.page_loading(self.driver)
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + '/' + self.fname.tpd_cluster() + self.load.get_current_date() + '.csv'
                print(self.filename)
                file = os.path.isfile(self.filename)
                if file != True:
                    print(dists.options[i].text, Blocks.options[j].text,
                          'Cluster wise records csv file is not downloaded ')
                    count = count + 1
                else:
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        data = list(csv_reader)
                        row_count = len(data)
                    os.remove(self.filename)
                    time.sleep(2)
                    if row_count == 0:
                        print("records are not found in csv file ")
                        count = count + 1
                    self.load.page_loading(self.driver)
        return count

    def Clusters_select_box(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        clust = Select(self.driver.find_element_by_id(Data.cluster_dropdown))
        dists = Select(self.driver.find_element_by_id(Data.district_dropdown))
        Blocks = Select(self.driver.find_element_by_id(Data.blocks_dropdown))
        for i in range(len(dists.options) - 1, len(dists.options)):
            dists.select_by_index(i)
            self.load.page_loading(self.driver)
            for j in range(len(Blocks.options) - 1, len(Blocks.options)):
                Blocks.select_by_index(j)
                self.load.page_loading(self.driver)
                for k in range(1, len(clust.options)):
                    clust.select_by_index(k)
                    self.load.page_loading(self.driver)
                    value = self.driver.find_element_by_id(Data.cluster_dropdown).get_attribute('value')
                    value = value[3:] + '_'
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(3)
                    self.filename = self.p.get_download_dir() + '/' + self.fname.tpd_school() + value.strip() + self.load.get_current_date() + '.csv'
                    print(self.filename)
                    file = os.path.isfile(self.filename)
                    if file != True:
                        print(dists.options[i].text, Blocks.options[j].text, clust.options[k].text,
                              'School wise records csv file is not downloaded')
                        count = count + 1
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            data = list(csv_reader)
                            row_count = len(data)
                        os.remove(self.filename)
                        time.sleep(2)
                        if row_count == 0:
                            print("records are not found in csv file ")
                            count = count + 1
                        self.load.page_loading(self.driver)
        return count

    def test_logoutbtn(self):
        self.data = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(2)
        self.driver.find_element_by_id(Data.logout).click()
        if 'Log in to cQube' in self.driver.title:
            print("Logout button is working ")
        else:
            print("Logout button is not working ")
            count = count + 1
        self.data.page_loading(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_tpd_content_progress()
        self.data.page_loading(self.driver)
        return count

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
