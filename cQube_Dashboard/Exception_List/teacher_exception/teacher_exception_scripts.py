import csv
import os
import re
import time
from selenium.webdriver.support.select import Select
from Locators.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData

'''Script perform the functionality test of blocks , cluster and school level buttons and dropdowns , map records , 
footer information's '''


class Teacher_Exception_Report():

    def __init__(self, driver, year, month):
        self.p = None
        self.file = None
        self.driver = driver
        self.filename = ''
        self.year = year.strip()
        self.month = month.strip()

    def test_icon(self):
        self.data = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.data.page_loading(self.driver)
        self.data.navigate_to_teacher_exception()
        self.data.page_loading(self.driver)
        if "teacher-attendance-exception" in self.driver.current_url:
            print("Teacher exception report page is dispayed")
        else:
            print("Teacher exception icon is not working")
            count = count + 1
        return count

    def click_on_logout(self):
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.logout).click()
        return self.driver.title

    def test_click_on_dashboard(self):
        count = 0
        cal = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        cal.page_loading(self.driver)
        cal.navigate_to_teacher_exception()
        cal.page_loading(self.driver)
        if 'teacher-attendance-exception' in self.driver.current_url:
            print("Teacher exception report is present ")
        else:
            print("Teacher exception is not exist")
            count = count + 1
        return count

    def test_total_not_recieved_data(self):
        cal = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)

        school_not_recived = self.driver.find_element_by_id('students').text
        notcount = re.sub("\D", "", school_not_recived)

        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.driver.find_element_by_id('blockbtn').click()
        cal.page_loading(self.driver)
        blockcount = self.driver.find_element_by_id('students').text
        bcount = re.sub("\D", "", blockcount)
        cal.page_loading(self.driver)

        self.driver.find_element_by_id('clusterbtn').click()
        cal.page_loading(self.driver)
        clustcount = self.driver.find_element_by_id('students').text
        clustercount = re.sub("\D", "", clustcount)
        cal.page_loading(self.driver)

        self.driver.find_element_by_id('schoolbtn').click()
        cal.page_loading(self.driver)
        sccount = self.driver.find_element_by_id('students').text
        schoolcount = re.sub("\D", "", sccount)
        cal.page_loading(self.driver)

        return notcount, bcount, clustercount, schoolcount

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
        self.markers = 1
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.year, self.month = cal.get_student_month_and_year_values()
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        count = 0
        marker = 0
        for x in range(1, len(select_district.options) - 1):
            time.sleep(1)
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            value = self.driver.find_element_by_id('choose_dist').get_attribute('value')
            value = value.split(":")
            markers = self.driver.find_elements_by_class_name(Data.dots)
            time.sleep(3)
            marker = len(markers) - 1
            if (len(markers) - 1) == 0:
                print("District " + select_district.first_selected_option.text + " no data")
                count = count + 1
                return count
            else:
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(3)
                p = pwd()
                self.filename = p.get_download_dir() + "/" + "teacher_attendance_exception_" + management + "_blockPerDistricts_of_district_" + \
                                value[
                                    1].strip() + "_" + self.month + '_' + self.year + '_' + cal.get_current_date() + ".csv"
                print(self.filename)
                if os.path.isfile(self.filename) != True:
                    return "File Not Downloaded"
                else:
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        schools = 0
                        teacher = 0
                        for row in csv.reader(fin):
                            # schools += int(row[6])
                            teacher += int(row[4])
                        teach = self.driver.find_element_by_id("students").text
                        ta = re.sub('\D', "", teach)

                        if int(teacher) != int(ta):
                            print("school count mismatched", int(teacher), int(ta))
                            count = count + 1
                os.remove(self.filename)
        return count

    def ClusterPerBlockCsvDownload(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.year, self.month = cal.get_student_month_and_year_values()
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
                values = value[3:] + '_'
                time.sleep(2)
                dots = self.driver.find_elements_by_class_name(Data.dots)
                markers = len(dots) - 1
                if markers == 0:
                    print(select_block.options[y].text, "does not have markers")
                    count = count + 1
                else:
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(4)
                    p = pwd()
                    self.filename = p.get_download_dir() + "/" + "teacher_attendance_exception_" + management + "_clusterPerBlocks_of_block_" + values.strip() + self.month + '_' + self.year + '_' + cal.get_current_date() + ".csv"
                    print(self.filename)
                    if os.path.isfile(self.filename) != True:
                        return "File Not Downloaded"
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            teacher = 0
                            for row in csv.reader(fin):
                                teacher += int(row[6])

                            teach = self.driver.find_element_by_id("students").text
                            ta = re.sub('\D', "", teach)

                            if int(teacher) != int(ta):
                                print("Teacher count mismatched", int(teacher), int(ta))
                                count = count + 1
                        os.remove(self.filename)
                    print(markers, count)
            return count

    def SchoolPerClusterCsvDownload(self):
        cal = GetData()
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(3)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.year, self.month = cal.get_student_month_and_year_values()
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        select_block = Select(self.driver.find_element_by_id('choose_block'))
        select_cluster = Select(self.driver.find_element_by_id('choose_cluster'))
        count = 0
        markers = 0
        if 'No data found' in self.driver.page_source:
            print("No data found showing on report")
            count = count + 1
            return count
        else:
            for x in range(len(select_district.options) - 1, len(select_district.options)):
                time.sleep(1)
                select_district.select_by_index(x)
                cal.page_loading(self.driver)
                for y in range(1, len(select_block.options)):
                    time.sleep(2)
                    select_block.select_by_index(y)
                    cal.page_loading(self.driver)
                    for z in range(1, len(select_cluster.options)):
                        select_cluster.select_by_index(z)
                        cal.page_loading(self.driver)
                        time.sleep(2)
                        value = self.driver.find_element_by_id('choose_cluster').get_attribute('value')
                        values = value[3:] + '_'
                        dots = self.driver.find_elements_by_class_name(Data.dots)
                        markers = len(dots) - 1
                        self.driver.find_element_by_id(Data.Download).click()
                        time.sleep(4)
                        p = pwd()
                        self.filename = p.get_download_dir() + "/" + "teacher_attendance_exception_" + management + "_schoolPerClusters_of_cluster_" + values.strip() + self.month + "_" + self.year + '_' + cal.get_current_date() + ".csv"
                        print(self.filename)
                        if os.path.isfile(self.filename) != True:
                            return "File Not Downloaded"
                        else:
                            with open(self.filename) as fin:
                                csv_reader = csv.reader(fin, delimiter=',')
                                header = next(csv_reader)
                                teacher = 0
                                for row in csv.reader(fin):
                                    teacher += int(row[8])

                                teach = self.driver.find_element_by_id("students").text
                                ta = re.sub('\D', "", teach)

                                if int(teacher) != int(ta):
                                    print("Teacher count mismatched", int(teacher), int(ta))
                                    count = count + 1
                        os.remove(self.filename)
            return count

    def check_markers_on_block_map(self):
        cal = GetData()
        count = 0
        self.fname = file_extention()
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
        self.filename = p.get_download_dir() + "/" + "teacher_attendance_exception_" + management + "_allBlocks_overall_" + cal.get_current_date() + ".csv"
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                schools = 0
                teacher = 0
                for row in csv.reader(fin):
                    teacher += int(row[4])
                teach = self.driver.find_element_by_id("students").text
                ta = re.sub('\D', "", teach)
                print("no of missing data", teacher, ta)
                if int(teacher) != int(ta):
                    print("missed teacher count mismatched", int(teacher), int(ta))
                    count = count + 1
            os.remove(self.filename)
        return markers, count

    def check_markers_on_clusters_map(self):
        self.driver.find_element_by_id('clusterbtn').click()
        cal = GetData()
        count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.fname = file_extention()
        cal.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        markers = len(dots) - 1
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + "teacher_attendance_exception_" + management + "_allClusters_overall_" + cal.get_current_date() + ".csv"
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                schools = 0
                teacher = 0
                for row in csv.reader(fin):
                    teacher += int(row[6])
                teach = self.driver.find_element_by_id("students").text
                ta = re.sub('\D', "", teach)
                print("no of missing data", teacher, ta)
                if int(teacher) != int(ta):
                    print("Teacher count mismatched", int(teacher), int(ta))
                    count = count + 1
            os.remove(self.filename)
        return markers, count

    def check_markers_on_school_map(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(3)
        self.driver.find_element_by_id('schoolbtn').click()
        cal = GetData()
        count = 0
        time.sleep(10)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.fname = file_extention()
        cal.page_loading(self.driver)
        result = self.driver.find_elements_by_class_name(Data.dots)
        cal.page_loading(self.driver)
        markers = len(result) - 1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + "teacher_attendance_exception_" + management + "_allSchools_overall_" + cal.get_current_date() + ".csv"
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                teacher = 0
                for row in csv.reader(fin):
                    teacher += int(row[8])
                teach = self.driver.find_element_by_id("students").text
                ta = re.sub('\D', "", teach)
                print("no of missing data", teacher, ta)
                if int(teacher) != int(ta):
                    print("Teacher count mismatched", int(teacher), int(ta))
                    count = count + 1
            os.remove(self.filename)
        return markers, count

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
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(4)
        # self.driver.find_element_by_xpath(Locators.sr_school_hyper).click()
        # cal.page_loading(self.driver)
        # self.driver.find_element_by_xpath(Locators.sr_cluster_hyper).click()
        # cal.page_loading(self.driver)
        # self.driver.find_element_by_xpath(Locators.sr_dist_hyper).click()
        # cal.page_loading(self.driver)
        # result1 = self.driver.find_element_by_id('choose_block').is_displayed()
        # time.sleep(2)
        # result2 = self.driver.find_element_by_id('choose_cluster').is_displayed()
        # time.sleep(2)
        # dist = Select(self.driver.find_element_by_id('choose_dist'))
        # choose_dist = dist.first_selected_option.text
        # return result1, result2, choose_dist

    def check_time_series_overall(self):
        cal = GetData()
        self.p = pwd()
        count = 0
        self.file = file_extention()
        cal.click_on_state(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        timeperiods = Select(self.driver.find_element_by_id('period'))
        # timeperiods.select_by_visible_text(' Overall ')
        timeperiods.select_by_index(1)
        cal.page_loading(self.driver)
        markers = self.driver.find_elements_by_class_name(Data.dots)
        dots = len(markers) - 1
        if markers == 0:
            print('Markers are not present on screen ')
            count = count + 1
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + '/' + "teacher_attendance_exception_" + management + "_allDistricts_overall_" + cal.get_current_date() + '.csv'
            if os.path.isfile(self.filename) != True:
                print("Over all time series csv file is not downloaded")
            else:
                with open(self.filename) as fin:
                    csv_reader = csv.reader(fin, delimiter=',')
                    header = next(csv_reader)
                    schools = 0
                    for row in csv.reader(fin):
                        schools += int(row[3])
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
        self.file = file_extention()
        cal.click_on_state(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        timeperiods = Select(self.driver.find_element_by_id('period'))
        # timeperiods.select_by_visible_text(' Last 7 Days ')
        timeperiods.select_by_index(3)
        cal.page_loading(self.driver)
        markers = self.driver.find_elements_by_class_name(Data.dots)
        dots = len(markers) - 1
        if markers == 0:
            print('Markers are not present on screen ')
            count = count + 1
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + '/' + "teacher_attendance_exception_" + management + "_allDistricts_last_7_days_" + cal.get_current_date() + '.csv'
            if os.path.isfile(self.filename) != True:
                print(" Last 7 Days time series csv file is not downloaded")
            else:
                with open(self.filename) as fin:
                    csv_reader = csv.reader(fin, delimiter=',')
                    header = next(csv_reader)
                    schools = 0
                    for row in csv.reader(fin):
                        schools += int(row[3])
                    school = self.driver.find_element_by_id("schools").text
                    sc = re.sub('\D', "", school)
                    if int(sc) != int(schools):
                        print("school count mismatched", int(sc), int(schools))
                        count = count + 1
                os.remove(self.filename)
        return count

    def check_time_series_last_30_days(self):
        cal = GetData()
        self.p = pwd()
        count = 0
        self.file = file_extention()
        cal.click_on_state(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        timeperiods = Select(self.driver.find_element_by_id('period'))
        # timeperiods.select_by_visible_text(' Last 30 Days ')
        timeperiods.select_by_index(2)
        cal.page_loading(self.driver)
        markers = self.driver.find_elements_by_class_name(Data.dots)
        dots = len(markers) - 1
        if markers == 0:
            print('Markers are not present on screen ')
            count = count + 1
        else:
            cal.page_loading(self.driver)
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(5)
            self.filename = self.p.get_download_dir() + '/' + "teacher_attendance_exception_" + management + "_allDistricts_last_30_days_" + cal.get_current_date() + '.csv'
            if os.path.isfile(self.filename) != True:
                print(" Last 30 Days time series csv file is not downloaded")
            else:
                with open(self.filename) as fin:
                    csv_reader = csv.reader(fin, delimiter=',')
                    header = next(csv_reader)
                    schools = 0
                    for row in csv.reader(fin):
                        schools += int(row[3])
                    school = self.driver.find_element_by_id("schools").text
                    sc = re.sub('\D', "", school)
                    if int(sc) != int(schools):
                        print("school count mismatched", int(sc), int(schools))
                        count = count + 1
                os.remove(self.filename)
        return count

    def check_time_series_dropdown(self):
        self.data = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        timeperiod = Select(self.driver.find_element_by_id('period'))
        for i in range(1, len(timeperiod.options)):
            timeperiod.select_by_index(i)
            self.data.page_loading(self.driver)
            print(timeperiod.options[i].text, 'is selected and displayed on screen')
            if 'No data found' in self.driver.page_source:
                print(timeperiod.options[i].text, "is not having Locators")
            else:
                markers = self.driver.find_elements_by_xpath(Data.dots)
                dots = len(markers) - 1
                if dots == 0:
                    count = count + 1
                    print('Markers are not present on screen')
        return count

    def check_time_series_dropdown_options(self):
        self.data = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        timeperiod = Select(self.driver.find_element_by_id('period'))
        count = len(timeperiod.options) - 1
        return count

    def check_time_overall_series_dropdown(self):
        self.data = GetData()
        count = 0
        self.p = pwd()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        timeperiods = Select(self.driver.find_element_by_id('period'))
        # timeperiods.select_by_visible_text(' Overall ')
        timeperiods.select_by_index(1)
        self.data.page_loading(self.driver)
        if 'No data found' in self.driver.page_source:
            print("Overall is not having Locators")
        else:
            markers = self.driver.find_elements_by_class_name(Data.dots)
            dots = len(markers) - 1
            if markers == 0:
                print('Markers are not present on screen ')
                count = count + 1
            else:
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + '/' + "teacher_attendance_exception_allDistricts_overall_" + self.data.get_current_date() + '.csv'
                print(self.filename)
                if os.path.isfile(self.filename) != True:
                    print("Over all time series csv file is not downloaded")
                else:
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        student = 0
                        for row in csv.reader(fin):
                            student += int(row[2])
                        stds = self.driver.find_element_by_id("students").text
                        std = re.sub('\D', "", stds)
                        if int(std) != int(student):
                            print("school count mismatched", int(std), int(student))
                            count = count + 1

                    os.remove(self.filename)
        return count

    def check_time_series_last_7_days(self):
        cal = GetData()
        self.p = pwd()
        count = 0
        self.file = file_extention()
        cal.click_on_state(self.driver)
        timeperiods = Select(self.driver.find_element_by_id('period'))
        # timeperiods.select_by_visible_text(' Last 7 Days ')
        timeperiods.select_by_index(3)
        cal.page_loading(self.driver)
        if 'No data found' in self.driver.page_source:
            print("Last 7 days is not having Locators")
        else:
            markers = self.driver.find_elements_by_class_name(Data.dots)
            dots = len(markers) - 1
            if markers == 0:
                print('Markers are not present on screen ')
                count = count + 1
            else:
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + '/' + "teacher_attendance_exception_allDistricts_last_7_days_" + cal.get_current_date() + '.csv'
                print(self.filename)
                if os.path.isfile(self.filename) != True:
                    print(" Last 7 Days time series csv file is not downloaded")
                else:
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        student = 0
                        for row in csv.reader(fin):
                            student += int(row[2])

                        stds = self.driver.find_element_by_id("students").text
                        std = re.sub('\D', "", stds)
                        if int(student) != int(std):
                            print("missing data count mismatched", int(std), int(student))
                            count = count + 1
                    os.remove(self.filename)
        return count

    def check_time_series_last_30_days(self):
        cal = GetData()
        self.p = pwd()
        count = 0
        self.file = file_extention()
        cal.click_on_state(self.driver)
        self.year, self.month = cal.get_student_month_and_year_values()
        timeperiods = Select(self.driver.find_element_by_id('period'))
        # timeperiods.select_by_visible_text(' Last 30 Days ')
        timeperiods.select_by_index(2)
        cal.page_loading(self.driver)
        if 'No data found' in self.driver.page_source:
            print("Last 30 days is not having Locators")
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
                self.filename = self.p.get_download_dir() + '/' + "teacher_attendance_exception_allDistricts_last_30_days_" + cal.get_current_date() + '.csv'
                print(self.filename)
                if os.path.isfile(self.filename) != True:
                    print(" Last 30 Days time series csv file is not downloaded")
                else:
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        student = 0
                        for row in csv.reader(fin):
                            student += int(row[2])
                        stds = self.driver.find_element_by_id("students").text
                        std = re.sub('\D', "", stds)

                        if int(student) != int(std):
                            print("student count mismatched", int(std), int(student))
                            count = count + 1
                    os.remove(self.filename)
        return count

    def check_time_series_day(self):
        cal = GetData()
        self.p = pwd()
        count = 0
        self.file = file_extention()
        cal.click_on_state(self.driver)
        self.year, self.month = cal.get_student_month_and_year_values()
        timeperiods = Select(self.driver.find_element_by_id('period'))
        # timeperiods.select_by_visible_text(' Last Day ')
        timeperiods.select_by_index(4)
        cal.page_loading(self.driver)
        if 'No data found' in self.driver.page_source:
            print("Last Day is not having Locators")
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
                self.filename = self.p.get_download_dir() + '/' + "teacher_attendance_exception_allDistricts_last_day_" + cal.get_current_date() + '.csv'
                print(self.filename)
                if os.path.isfile(self.filename) != True:
                    print(" Last Day time series csv file is not downloaded")
                else:
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        student = 0
                        for row in csv.reader(fin):
                            student += int(row[2])

                        stds = self.driver.find_element_by_id("students").text
                        std = re.sub('\D', "", stds)

                        if int(student) != int(std):
                            print("student count mismatched", int(std), int(student))
                            count = count + 1
                    os.remove(self.filename)
        return count

    def check_time_series_month_and_year(self):
        cal = GetData()
        self.p = pwd()
        count = 0
        self.file = file_extention()
        cal.click_on_state(self.driver)
        self.year, self.month = cal.get_student_month_and_year_values()
        timeperiods = Select(self.driver.find_element_by_id('period'))
        # timeperiods.select_by_visible_text(' Year and Month ')
        timeperiods.select_by_index(5)
        cal.page_loading(self.driver)
        if 'No data found' in self.driver.page_source:
            print("Year and month is not having Locators")
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
                self.filename = self.p.get_download_dir() + '/' + "teacher_attendance_exception_allDistricts_" + self.month + "_" + self.year + "_" + cal.get_current_date() + ".csv"
                print(self.filename)
                if os.path.isfile(self.filename) != True:
                    print(" year and month time series csv file is not downloaded")
                else:
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        student = 0
                        for row in csv.reader(fin):
                            student += int(row[2].replace(',', ''))

                        stds = self.driver.find_element_by_id("students").text
                        std = re.sub('\D', "", stds)

                        if int(student) != int(std):
                            print("school missing data count mismatched", int(std), int(student))
                            count = count + 1
                    os.remove(self.filename)
        return count

    def check_year_and_month_dropdowns_csv_download(self):
        cal = GetData()
        self.p = pwd()
        count = 0
        self.file = file_extention()
        cal.click_on_state(self.driver)
        timeperiods = Select(self.driver.find_element_by_id('period'))
        # timeperiods.select_by_visible_text(' Year and Month ')
        timeperiods.select_by_index(5)
        cal.page_loading(self.driver)
        if 'No data found' in self.driver.page_source:
            print("Year and month is not having Locators")
        else:
            markers = self.driver.find_elements_by_class_name(Data.dots)
            dots = len(markers) - 1
            if markers == 0:
                print('Markers are not present on screen ')
                count = count + 1
            else:
                cal.page_loading(self.driver)
                year = Select(self.driver.find_element_by_id('year'))
                month = Select(self.driver.find_element_by_id('month'))
                for i in range(1, len(year.options)):
                    year.select_by_index(i)
                    cal.page_loading(self.driver)
                    for j in range(1, len(month.options)):
                        month.select_by_index(j)
                        cal.page_loading(self.driver)
                        self.driver.find_element_by_id(Data.Download).click()
                        time.sleep(5)
                        self.filename = self.p.get_download_dir() + '/' + "teacher_attendance_exception_allDistricts_" + (
                            month.options[j].text).replace(' ', '') + "_" + (year.options[i].text).replace(' ',
                                                                                                           '') + cal.get_current_date() + ".csv"
                        print(self.filename)
                        if os.path.isfile(self.filename) != True:
                            print(year.options[i].text, month.options[j].text, "time series csv file is not downloaded")
                        else:
                            with open(self.filename) as fin:
                                csv_reader = csv.reader(fin, delimiter=',')
                                header = next(csv_reader)
                                student = 0
                                for row in csv.reader(fin):
                                    student += int(row[2].replace(',', ''))

                                stds = self.driver.find_element_by_id("students").text
                                std = re.sub('\D', "", stds)

                                if int(student) != int(std):
                                    print("student count mismatched", int(std), int(student))
                                    count = count + 1
                            os.remove(self.filename)
        return count

    def check_select_time_series_and_click_on_block_cluster_school_btns(self):
        self.data = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        timeperiod = Select(self.driver.find_element_by_id('period'))
        for i in range(1, len(timeperiod.options)):
            timeperiod.select_by_index(i)
            self.data.page_loading(self.driver)
            print(timeperiod.options[i].text, 'is selected and displayed on screen')
            if 'No data found' in self.driver.page_source:
                print(timeperiod.options[i].text, "is not having Locators")
            else:
                cur_students = self.driver.find_element_by_id(Data.students).text
                cstudents = re.sub('\D', '', cur_students)

                blk = self.driver.find_element_by_id(Data.sr_block_btn).click()
                self.data.page_loading(self.driver)

                blk_students = self.driver.find_element_by_id(Data.students).text
                bstudents = re.sub('\D', '', blk_students)

                cls = self.driver.find_element_by_id(Data.sr_cluster_btn).click()
                self.data.page_loading(self.driver)
                time.sleep(5)
                cls_students = self.driver.find_element_by_id(Data.students).text

                cl_students = re.sub('\D', '', cls_students)

                sc = self.driver.find_element_by_id(Data.sr_schools_btn).click()
                self.data.page_loading(self.driver)
                time.sleep(10)
                sc_students = self.driver.find_element_by_id(Data.students).text

                s_students = re.sub('\D', '', sc_students)
                count = 0

                if int(cstudents) != int(bstudents):
                    print('Block level mismatch found at footers', cur_students, blk_students)
                    count = count + 1

                if int(cstudents) != int(cl_students):
                    print('Cluster level mismatch found at footers', cur_students, cl_students)
                    count = count + 1

                if int(cstudents) != int(s_students):
                    print('School level mismatch found at footers', cur_students, s_students)
                    count = count + 1
        return count
