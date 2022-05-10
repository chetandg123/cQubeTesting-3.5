import csv
import os
import re
import time

from selenium.webdriver.support.select import Select

from Locators.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class Periodic_Assessment_Test_LoTable():
    def __init__(self, driver):
        self.fname = None
        self.year = None
        self.month = None
        self.driver = driver

    def viewbys_options(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        self.fname = file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        self.load.page_loading(self.driver)
        year = Select(self.driver.find_element_by_id('year'))
        month = Select(self.driver.find_element_by_id('month'))
        self.year = (year.first_selected_option.text).strip()
        self.month = (month.first_selected_option.text).strip()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        grades = Select(self.driver.find_element_by_id(Data.grade))
        grades.select_by_index(2)
        gradename = grades.options[2].text
        gradenum = re.sub('\D', '', gradename).strip()
        self.load.page_loading(self.driver)

        view_by = Select(self.driver.find_element_by_id(Data.view_by))
        # view_by.select_by_visible_text(' Question Id ')
        view_by.select_by_index(1)
        self.load.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        self.filename = self.p.get_download_dir() + "/" + self.fname.patlo_views() + management + '_' + gradenum + '_' + Data.question_id + self.month + '_' \
                        + self.year + '_' + self.load.get_current_date() + '.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            print(Data.question_id, 'csv file is not downloaded')
            count = count + 1
        # view_by.select_by_visible_text(' Indicator ')
        view_by.select_by_index(2)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        self.file = self.p.get_download_dir() + "/" + self.fname.patlo_views() + management + '_' + gradenum + '_' + Data.indicator_id + self.month + '_' \
                    + self.year + '_' + self.load.get_current_date() + '.csv'
        print(self.file)
        if os.path.isfile(self.file) != True:
            print(Data.indicator_id, 'csv file is not downloaded')
            count = count + 1
        os.remove(self.filename)
        os.remove(self.file)
        return count

    def test_questions_records(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        view_by = Select(self.driver.find_element_by_id(Data.view_by))
        view_by.select_by_index(1)
        self.load.page_loading(self.driver)
        if view_by.options[1].text in self.driver.page_source:
            print(view_by.options[1].text, 'is displayed records in heat chart')
        else:
            print(view_by.options[1].text, 'Records are not displayed')
            count = count + 1
        self.load.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        self.filename = self.p.get_download_dir() + "/" + self.fname.pchart_views()
        if os.path.isfile(self.filename) != True:
            print(view_by.options[1].text, 'csv file is not downloaded')
            count = count + 1
        else:
            print(view_by.options[1].text, 'csv file is downloaded')
        os.remove(self.filename)
        return count

    def test_indicator_records(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        view_by = Select(self.driver.find_element_by_id(Data.view_by))
        view_by.select_by_index(2)
        self.load.page_loading(self.driver)
        if view_by.options[2].text in self.driver.page_source:
            print(view_by.options[2].text, 'is displayed records in heat chart')
        else:
            print(view_by.options[2].text, 'Records are not displayed')
            count = count + 1
        self.load.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        self.filename = self.p.get_download_dir() + "/" + self.fname.pchart_subjects()
        if os.path.isfile(self.filename) != True:
            print(view_by.options[2].text, 'csv file is not downloaded')
            count = count + 1
        else:
            print(view_by.options[2].text, 'csv file is downloaded')
        os.remove(self.filename)
        return count

    def download_all_district_records(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.fname = file_extention()
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.load.page_loading(self.driver)
        self.load.navigate_to_lo_table_report()
        self.load.page_loading(self.driver)
        self.year, self.month = self.load.get_pat_month_and_year_values()
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        self.filename = self.p.get_download_dir() + '/' + self.fname.patlo_all_districts() + management + '_overall_allDistricts_' + self.month + '_' + self.year + '_' + self.load.get_current_date() + '.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            print('Districtwise csv file is not downloaded ')
            count = count + 1
        else:
            print('District wise csv file is downloaded ')
        self.load.page_loading(self.driver)
        os.remove(self.filename)
        return count

    def exams_dates(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        examdates = Select(self.driver.find_element_by_id(Data.exam_dates))
        for i in range(1, len(examdates.options)):
            examdates.select_by_index(i)
            self.load.page_loading(self.driver)
            if examdates.options[i].text in self.driver.page_source:
                print(examdates.options[i].text, 'is displaying chart table ')
                self.load.page_loading(self.driver)
            else:
                print(examdates.options[i].text, 'is not displayed ')
                count = count + 1
        self.load.page_loading(self.driver)
        return count

    def subjects_types(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.load.page_loading(self.driver)
        self.load.navigate_to_lo_table_report()
        self.load.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.year, self.month = self.load.get_pat_month_and_year_values()
        grade = Select(self.driver.find_element_by_id(Data.grade))
        grade.select_by_index(4)
        gradename = (grade.options[4].text).strip()
        gradenum = re.sub('\D', '', gradename)
        self.load.page_loading(self.driver)
        subject = Select(self.driver.find_element_by_id(Data.subjects))
        for i in range(2, len(subject.options)):
            subject.select_by_index(i)
            self.load.page_loading(self.driver)
            if subject.options[i].text in self.driver.page_source:
                print(subject.options[i].text, 'is displayed chart table ')
                self.load.page_loading(self.driver)
            else:
                print(subject.options[i].text, 'is not displayed ')
                count = count + 1
            if 'No data found' in self.driver.page_source:
                print("No Data found on screen")
            else:
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + '/' + self.fname.patlo_subjects() + management + '_' + gradenum + '_' + (
                    subject.options[i].text).strip() + \
                                '_allDistricts_' + self.month + '_' + self.year + '_' + self.load.get_current_date() + '.csv'
                print(self.filename)
                if os.path.isfile(self.filename) != True:
                    print(subject.options[i].text, 'csv file is not downloaded')
                    count = count + 1
                self.load.page_loading(self.driver)
                os.remove(self.filename)
        return count

    def test_homeicons(self):
        self.load = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_id(Data.exam_dates))
        timeseries.select_by_index(2)
        self.load.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)

    def test_homebutton(self):
        self.load = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.load.page_loading(self.driver)
        self.load.navigate_to_lo_table_report()
        self.load.page_loading(self.driver)
        if 'PAT-LO-table' in self.driver.current_url:
            print('Pat LO Table is present ')
        else:
            print('Home button is not working ')
            count = count + 1
        self.load.page_loading(self.driver)
        return count

    def test_logoutbtn(self):
        self.data = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.logout).click()
        if 'Log in to cQube' in self.driver.title:
            print("Logout button is working ")
        else:
            print("Logout button is not working ")
            count = count + 1
        self.data.page_loading(self.driver)
        return count

    def test_year_dropdown(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        year_select = Select(self.driver.find_element_by_id(Data.year_select))
        for i in range(1, len(year_select.options)):
            year_select.select_by_index(i)
            self.load.page_loading(self.driver)
            if year_select.options[i].text in self.driver.page_source:
                print(year_select.options[i].text, 'is displaying chart table ')
                self.load.page_loading(self.driver)
            else:
                print(year_select.options[i].text, 'is not displayed ')
                count = count + 1
        self.load.page_loading(self.driver)
        return count

    def District_select_box(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        self.fname = file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        year = Select(self.driver.find_element_by_id('year'))
        month = Select(self.driver.find_element_by_id('month'))
        self.year = (year.first_selected_option.text).strip()
        self.month = (month.first_selected_option.text).strip()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        grades = Select(self.driver.find_element_by_id(Data.grade))
        grades.select_by_index(1)
        gradename = (grades.options[1].text).strip()
        gradenum = re.sub('\D', '', gradename).strip()
        dists = Select(self.driver.find_element_by_id(Data.district_dropdown))
        view_by = Select(self.driver.find_element_by_id(Data.view_by))
        for j in range(len(view_by.options)):
            view_by.select_by_index(j)
            self.load.page_loading(self.driver)
            for i in range(len(dists.options) - 4, len(dists.options)):
                dists.select_by_index(i)
                print(dists.options[i].text)
                value = self.driver.find_element_by_id(Data.district_dropdown).get_attribute('value')
                value = value[5:] + '_'
                self.load.page_loading(self.driver)
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(4)
                self.filename = self.p.get_download_dir() + '/' + self.fname.patlo_blocks() + management + '_' + gradenum + \
                                "_blocks_of_district_" + value.strip() + self.month + '_' + self.year + '_' + self.load.get_current_date() + '.csv'
                print(self.filename)
                if self.filename != True:
                    print(dists.options[i].text, 'csv file is not downloaded')
                    count = count + 0
                else:
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        data = list(csv_reader)
                        row_count = len(data)
                    os.remove(self.filename)
                    tablecount = self.driver.find_elements_by_tag_name('tr')
                    records = int(len(tablecount)) - 2
                    time.sleep(2)
                    if row_count != records:
                        print(dists.options[i].text, "records count mismatch in downloaded file and table records")
                        count = count + 1

                return count

    def Clusters_select_box(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        self.year, self.month = self.load.get_pat_month_and_year_values()
        dists = Select(self.driver.find_element_by_id(Data.district_dropdown))
        Blocks = Select(self.driver.find_element_by_id(Data.blocks_dropdown))
        grade = Select(self.driver.find_element_by_id(Data.grade))
        self.load.page_loading(self.driver)
        for m in range(2, len(grade.options)):
            grade.select_by_index(m)
            gradename = grade.options[m].text
            gradenum = re.sub('\D', '', gradename).strip()
            self.load.page_loading(self.driver)
            for i in range(len(dists.options) - 1, len(dists.options)):
                dists.select_by_index(i)
                self.load.page_loading(self.driver)
                for j in range(len(Blocks.options) - 1, len(Blocks.options)):
                    Blocks.select_by_index(j)
                    self.load.page_loading(self.driver)
                    value = self.driver.find_element_by_id(Data.blocks_dropdown).get_attribute('value')
                    vals = value.split(":")
                    val = vals[1].strip()
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(3)
                    self.filename = self.p.get_download_dir() + '/' + self.fname.patlo_clusters() + management + '_' + gradenum + "_schools_of_cluster_" + vals + self.month + '_' + self.year + '_' + \
                                    self.load.get_current_date() + '.csv'
                    print(self.filename)
                    file = os.path.isfile(self.filename)
                    if file != True:
                        print(Blocks.options[j].text, 'Cluster wise records csv file is not downloaded')
                        count = count + 1
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            data = list(csv_reader)
                            row_count = len(data)
                        os.remove(self.filename)
                        tablecount = self.driver.find_elements_by_tag_name('tr')
                        records = int(len(tablecount)) - 2
                        time.sleep(2)
                        if row_count != records:
                            print(dists.options[i].text, Blocks.options[j].text,
                                  "records count mismatch in downloaded file and table records")
                            count = count + 1

                    return count

    def Clusters_select_box(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        self.year, self.month = self.load.get_pat_month_and_year_values()
        clust = Select(self.driver.find_element_by_id(Data.cluster_dropdown))
        dists = Select(self.driver.find_element_by_id(Data.district_dropdown))
        Blocks = Select(self.driver.find_element_by_id(Data.blocks_dropdown))
        grade = Select(self.driver.find_element_by_id(Data.grade))
        self.load.page_loading(self.driver)
        for m in range(2, len(grade.options)):
            grade.select_by_index(m)
            gradename = grade.options[m].text
            gradenum = re.sub('\D', '', gradename).strip()
            self.load.page_loading(self.driver)
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
                        values = value[3:] + '_'
                        self.driver.find_element_by_id(Data.Download).click()
                        time.sleep(3)
                        self.filename = self.p.get_download_dir() + '/' + self.fname.patlo_schools() + management + '_' + gradenum + "_schools_of_cluster_" + values.strip() + self.month + '_' + self.year + '_' + \
                                        self.load.get_current_date() + '.csv'
                        print(self.filename)
                        file = os.path.isfile(self.filename)
                        if file != True:
                            print(clust.options[k].text, 'Cluster wise records csv file is not downloaded')
                            count = count + 1
                        else:
                            with open(self.filename) as fin:
                                csv_reader = csv.reader(fin, delimiter=',')
                                header = next(csv_reader)
                                data = list(csv_reader)
                                row_count = len(data)
                            os.remove(self.filename)
                            tablecount = self.driver.find_elements_by_tag_name('tr')
                            records = int(len(tablecount)) - 2
                            time.sleep(2)
                            if row_count != records:
                                print(dists.options[i].text, Blocks.options[j].text, clust.options[k].text,
                                      "records count mismatch in downloaded file and table records")
                                count = count + 1

                        return count

    def grades_files(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.fname = file_extention()
        year = Select(self.driver.find_element_by_id('year'))
        month = Select(self.driver.find_element_by_id('month'))
        self.year = (year.first_selected_option.text).strip()
        self.month = (month.first_selected_option.text).strip()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        grades = Select(self.driver.find_element_by_id(Data.grade))
        self.load.page_loading(self.driver)
        for i in range(2, len(grades.options)):
            time.sleep(2)
            grades.select_by_index(i)
            gradename = grades.options[i].text
            gradenum = re.sub('\D', '', gradename).strip()
            self.load.page_loading(self.driver)
            if grades.options[i].text in self.driver.page_source:
                print(grades.options[i].text, 'is displayed in chart ')
                self.load.page_loading(self.driver)
            else:
                print(grades.options[i].text, 'is not displayed ')
                count = count + 1
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + "/" + self.fname.patlo_grades() + management + '_' + gradenum + '_' + 'allDistricts_' + self.month + '_' + self.year + '_' + self.load.get_current_date() + '.csv'
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print(grades.options[i].text, 'csv file is not downloaded ')
                count = count + 1
            else:
                print(grades.options[i].text, "csv file is downloaded")
            os.remove(self.filename)
        self.load.page_loading(self.driver)
        return count

    def test_randoms(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.load.page_loading(self.driver)
        grades = Select(self.driver.find_element_by_id(Data.grade))
        grades.select_by_index(4)
        if grades.options[4].text in self.driver.page_source:
            print(grades.options[4].text, 'is displayed in chart ')
            self.load.page_loading(self.driver)
        else:
            print(grades.options[4].text, 'is not displayed ')
            count = count + 1
        subject = Select(self.driver.find_element_by_id(Data.subjects))
        subject.select_by_index(3)
        if subject.options[3].text in self.driver.page_source:
            print(subject.options[3].text, 'is displayed in chart ')
            self.load.page_loading(self.driver)
        else:
            print(subject.options[3].text, 'is not displayed ')
            count = count + 1
        self.load.page_loading(self.driver)

        grades = Select(self.driver.find_element_by_id(Data.grade))
        grades.select_by_index(3)
        if grades.options[3].text in self.driver.page_source:
            print(grades.options[3].text, 'is displayed in chart ')
            self.load.page_loading(self.driver)
        else:
            print(grades.options[3].text, 'is not displayed ')
            count = count + 1
        subject = Select(self.driver.find_element_by_id(Data.subjects))
        subject.select_by_index(2)
        if subject.options[2].text in self.driver.page_source:
            print(subject.options[2].text, 'is displayed in chart ')
            self.load.page_loading(self.driver)
        else:
            print(subject.options[2].text, 'is not displayed ')
            count = count + 1
        self.load.page_loading(self.driver)
        return count
