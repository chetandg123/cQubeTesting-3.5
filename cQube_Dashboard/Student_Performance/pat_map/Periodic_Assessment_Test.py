import csv
import os
import re
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Locators.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData

'''Script perform the test the blocks , cluster and school level buttons and dropdowns , map records , 
footer information's '''


class Periodic_Assessment_Test():

    def __init__(self, driver):
        self.driver = driver

    def click_download_icon(self):
        cal = GetData()
        count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.pat_district() + management + '_all_allGrades__allDistricts_' + cal.get_current_date() + '.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        else:
            markers = self.driver.find_elements_by_class_name(Data.dots)
            dots = len(markers) - 1
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                data = list(csv_reader)
                row_count = len(data)
                # total = 0
                # schools = 0
                # for row in csv.reader(fin):
                #     total += int(row[2])
                #     schools += int(row[3])
                # students = self.driver.find_element_by_id("students").text
                # res = re.sub('\D', "", students)
                #
                # school = self.driver.find_element_by_id("schools").text
                # sc = re.sub('\D', "", school)
                # if int(res) != total:
                #     print("student count mismatched")
                #     count = count + 1
                # if int(sc) != schools:
                #     print("school count mismatched")
                #     count = count + 1
                if int(dots) != row_count:
                    print("Markers and csv file records count mismatched", dots, row_count)
                    count = count + 1
            os.remove(self.filename)
        return count

    def check_with_footervalues(self):
        cal = GetData()
        files = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_id(Data.block_btn).click()
        cal.page_loading(self.driver)
        marker = self.driver.find_elements_by_class_name(Data.dots)
        counts = len(marker) - 1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        p = pwd()
        count = 0
        self.filename = p.get_download_dir() + "/" + files.pat_block() + management + '_all_allGrades__allBlocks_' + cal.get_current_date() + '.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        else:
            markers = self.driver.find_elements_by_class_name(Data.dots)
            dots = len(markers) - 1
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                data = list(csv_reader)
                row_count = len(data)
                if int(dots) != row_count:
                    print("Markers and csv file records count mismatched", dots, row_count)
                    count = count + 1
            os.remove(self.filename)
        return counts, count

    def check_with_footervalues(self):
        cal = GetData()
        files = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_id(Data.cluster_btn).click()
        cal.page_loading(self.driver)
        markers = self.driver.find_elements_by_class_name(Data.dots)
        dots = len(markers) - 1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(10)
        p = pwd()
        count = 0
        self.filename = p.get_download_dir() + "/" + files.pat_cluster() + management + '_all_allGrades__allClusters_' + cal.get_current_date() + '.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                data = list(csv_reader)
                row_count = len(data)
                if int(dots) != row_count:
                    print("Markers and csv file records count mismatched", dots, row_count)
                    count = count + 1
            os.remove(self.filename)
        return dots, count

    def check_with_footers(self):
        cal = GetData()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_id(Data.schoolbtn).click()
        time.sleep(20)
        markers = self.driver.find_elements_by_class_name(Data.dots)
        dots = len(markers) - 1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(15)
        p = pwd()
        count = 0
        files = file_extention()
        self.filename = p.get_download_dir() + "/" + files.pat_school() + management + '_all_allGrades__allSchools_' + cal.get_current_date() + '.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        else:
            markers = self.driver.find_elements_by_class_name(Data.dots)
            dots = len(markers) - 1
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                data = list(csv_reader)
                row_count = len(data)
                if int(dots) != row_count:
                    print("Markers and csv file records count mismatched", dots, row_count)
                    count = count + 1
            os.remove(self.filename)
        return dots, count

    global student_count

    def block_cluster_schools_footer_info(self):
        cal = GetData()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)

        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(4)
        time.sleep(4)
        schools = self.driver.find_element_by_id('schools').text
        scs = re.sub('\D', "", schools)

        student = self.driver.find_element_by_id('students').text
        stds = re.sub('\D', "", student)

        attended = self.driver.find_element_by_id('studentsAttended').text
        attds = re.sub('\D', "", attended)

        print('Expected Footer values : ', scs, stds, attds)
        "********************Block level Records *******************"
        self.driver.find_element_by_id(Data.block_btn).click()
        cal.page_loading(self.driver)

        schools = self.driver.find_element_by_id('schools').text
        bscs = re.sub('\D', "", schools)

        student = self.driver.find_element_by_id('students').text
        bstds = re.sub('\D', "", student)

        attended = self.driver.find_element_by_id('studentsAttended').text
        battds = re.sub('\D', "", attended)
        count = 0
        if scs != bscs:
            print('Block level schools count mismatch found', 'fi:' + scs, bscs)
            count = count + 1
        if stds != bstds:
            print('Block level students count mismatch found', stds, bstds)
            count = count + 1
        if attds != battds:
            print('Block level schools count mismatch found', attds, battds)
            count = count + 1
        "********************Cluster level Records *******************"
        self.driver.find_element_by_id(Data.cluster_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(10)
        schools = self.driver.find_element_by_id('schools').text
        cscs = re.sub('\D', "", schools)

        student = self.driver.find_element_by_id('students').text
        cstds = re.sub('\D', "", student)

        attended = self.driver.find_element_by_id('studentsAttended').text
        cattds = re.sub('\D', "", attended)
        if scs != cscs:
            print('Cluster level schools count mismatch found', scs, cscs)
            count = count + 1
        if stds != cstds:
            print('Cluster level students count mismatch found', stds, cstds)
            count = count + 1
        if attds != cattds:
            print('Cluster level schools count mismatch found', attds, cattds)
            count = count + 1
        "********************School level Records *******************"
        self.driver.find_element_by_id(Data.schoolbtn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(10)
        schools = self.driver.find_element_by_id('schools').text
        sscs = re.sub('\D', "", schools)

        student = self.driver.find_element_by_id('students').text
        sstds = re.sub('\D', "", student)

        attended = self.driver.find_element_by_id('studentsAttended').text
        sattds = re.sub('\D', "", attended)

        if scs != sscs:
            print('School level schools count mismatch found', scs, sscs)
            count = count + 1
        if stds != sstds:
            print('School level students count mismatch found', stds, sstds)
            count = count + 1
        if attds != sattds:
            print('School level schools count mismatch found', attds, sattds)
            count = count + 1

        return count

    def click_on_blocks_click_on_home_icon(self):
        cal = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.block_btn).click()
        cal.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)

    def click_HomeButton(self):
        count = 0
        cal = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        cal.page_loading(self.driver)
        if 'dashboard' in self.driver.current_url:
            print('Landing page is displayed')
        else:
            print('Home btn is not working ')
            count = count + 1
        cal.page_loading(self.driver)
        return count

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

    def click_on_logout(self):
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.logout).click()
        return self.driver.title

    def check_district(self):
        cal = GetData()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(4)
        time.sleep(3)
        self.year, self.month = cal.pat_year_month_firstselected()
        cal.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        count = 0
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            value = self.driver.find_element_by_id('choose_dist').get_attribute('value')
            value = value.split(":")
            markers = self.driver.find_elements_by_class_name(Data.dots)
            time.sleep(3)
            if (len(markers) - 1) == 0:
                print("District" + select_district.first_selected_option.text + "no data")
                count = count + 1
            else:
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(4)
                p = pwd()
                file = file_extention()
                self.filename = p.get_download_dir() + "/" + file.pat_districtwise() + management + "_" + self.year + '_' + self.month + '_allGrades__blocks_of_district_' + \
                                value[1].strip() + '_' + cal.get_current_date() + '.csv'
                print(self.filename)
                if not os.path.isfile(self.filename):
                    print("District" + select_district.first_selected_option.text + "csv is not downloaded")
                    count = count + 1
                else:
                    values = pd.read_csv(self.filename)

                    school = values['Total Schools'].sum()
                    students = values['Total Students'].sum()
                    attend = values['Students Attended'].sum()

                    schools = self.driver.find_element_by_id('schools').text
                    scs = re.sub('\D', '', schools)

                    student = self.driver.find_element_by_id('students').text
                    stds = re.sub('\D', '', student)

                    attended = self.driver.find_element_by_id('studentsAttended').text
                    attds = re.sub('\D', '', attended)
                    print(school, scs, students, stds, attend, attds)

                    if int(scs) != school:
                        print("schools count in footer and csv file records count mismatched", int(scs),
                              int(schools))
                        count = count + 1

                    if int(stds) != students:
                        print("student count in footer and csv file records count mismatched", int(scs),
                              int(schools))
                        count = count + 1

                    if int(attds) != attend:
                        print("Attended count in footer and csv file records count mismatched", int(scs),
                              int(schools))
                        count = count + 1

                os.remove(self.filename)
            return count

    def remove_csv(self):
        os.remove(self.filename)

    def check_district_block_cluster(self):
        self.cal = GetData()
        self.driver.implicitly_wait(50)
        self.cal.click_on_state(self.driver)
        self.cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(4)
        self.cal.page_loading(self.driver)
        self.year, self.month = self.cal.pat_year_month_firstselected()
        self.fname = file_extention()
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        select_block = Select(self.driver.find_element_by_id('choose_block'))
        select_cluster = Select(self.driver.find_element_by_id('choose_cluster'))
        count = 0
        for x in range(len(select_district.options) - 1, len(select_district.options)):
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
                    time.sleep(3)
                    nodata = self.driver.find_element_by_id("errMsg").text
                    markers = self.driver.find_elements_by_class_name(Data.dots)
                    if len(markers) - 1 == 0:
                        print(
                            "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "No data")
                        count = count + 1
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(3)
                    p = pwd()
                    self.filename = p.get_download_dir() + "/" + self.fname.pat_clusterwise() + management + "_" + self.year + '_' + self.month + '_allGrades__schools_of_cluster_' + \
                                    value[1].strip() + '_' + self.cal.get_current_date() + '.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print(
                            "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "csv is not downloaded")
                        count = count + 1
                    else:
                        values = pd.read_csv(self.filename)

                        school = values['Total Schools'].sum()
                        students = values['Total Students'].sum()
                        attend = values['Students Attended'].sum()

                        schools = self.driver.find_element_by_id('schools').text
                        scs = re.sub('\D', '', schools)

                        student = self.driver.find_element_by_id('students').text
                        stds = re.sub('\D', '', student)

                        attended = self.driver.find_element_by_id('studentsAttended').text
                        attds = re.sub('\D', '', attended)

                        print(school, scs, students, stds, attend, attds)

                        if int(scs) != school:
                            print("schools count in footer and csv file records count mismatched", int(scs),
                                  int(schools))
                            count = count + 1

                        if int(stds) != students:
                            print("student count in footer and csv file records count mismatched", int(scs),
                                  int(schools))
                            count = count + 1

                        if int(attds) != attend:
                            print("Attended count in footer and csv file records count mismatched", int(scs),
                                  int(schools))
                            count = count + 1

                    os.remove(self.filename)
            return count

    def check_grade_dropdown_options(self):
        self.data = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        grade = Select(self.driver.find_element_by_id(Data.Grade))
        counter = len(grade.options)
        for i in range(1, len(grade.options)):
            grade.select_by_index(i)
            print(grade.options[i].text)
            self.data.page_loading(self.driver)
        return counter

    def click_each_grades(self):
        self.data = GetData()
        self.driver.implicitly_wait(50)
        count = 0
        p = pwd()
        files = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        management = self.driver.find_element(By.ID, 'name').text
        manage = management[16:].lower()
        grade = Select(self.driver.find_element_by_id(Data.Grade))
        for i in range(1, len(grade.options) - 2):
            grade.select_by_index(i)
            gradename = (grade.options[i].text).strip()
            gradenum = re.sub('\D', '', gradename)
            dots = self.driver.find_elements_by_class_name(Data.dots)
            markers = len(dots) - 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            self.filename = p.get_download_dir() + '/' + files.pat_gradewise() + manage.strip() + '_all_Grade ' + gradenum.strip() + '__allDistricts_' + self.data.get_current_date() + '.csv'
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print('District wise csv file is not downloaded')
                count = count + 1
            else:
                file = open(self.filename)
                read = file.read()
                if grade.options[i].text in read:
                    print(grade.options[i].text, "is present")
                self.data.page_loading(self.driver)
            os.remove(self.filename)
        self.data.page_loading(self.driver)
        return count

    def select_subjects_dropdown(self):
        self.data = GetData()
        p = pwd()
        count = 0
        self.driver.implicitly_wait(100)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        grade = Select(self.driver.find_element_by_id(Data.Grade))
        subjects = Select(self.driver.find_element_by_id(Data.Subject))
        subcount = len(subjects.options) - 1
        files = file_extention()
        for i in range(1, len(grade.options)):
            grade.select_by_index(i)
            self.data.page_loading(self.driver)
            gradename = grade.options[i].text.strip()
            gradenum = re.sub('\D', '', gradename)
            for j in range(len(subjects.options) - 1, len(subjects.options)):
                subjects.select_by_index(j)
                self.data.page_loading(self.driver)
                sub = (subjects.options[j].text).strip()
                if "No data found" in self.driver.page_source:
                    print("No data found ")
                else:
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(3)
                    self.filename = p.get_download_dir() + '/' + files.pat_gradewise() + management + '_all_Grade ' + gradenum.strip() + '_' + sub + '_allDistricts_' + self.data.get_current_date() + '.csv'
                    print(self.filename)
                    if os.path.isfile(self.filename) != True:
                        print('grade wise wise csv file is not downloaded')
                        count = count + 1
                    else:
                        file = open(self.filename)
                        read = file.read()
                        if grade.options[j].text in read:
                            print(grade.options[j].text, "is present")
                        self.data.page_loading(self.driver)
                    os.remove(self.filename)
            return count

    def test_options_times(self):
        data = GetData()
        data.page_loading(self.driver)
        times = Select(self.driver.find_element_by_id('period'))
        count = len(times.options)
        return count

    def time_over_all(self):
        self.data = GetData()
        p = pwd()
        count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        dist = Select(self.driver.find_element_by_id('choose_dist'))
        times = Select(self.driver.find_element_by_id('period'))
        for i in range(1, len(times.options)):
            times.select_by_index(i)
            time.sleep(3)
            if 'No data found' in self.driver.page_source:
                print(times.options[i].text, 'has no data found')
            else:
                for j in range(1, len(dist.options) - 1):
                    dist.select_by_index(j)
                    value = self.driver.find_element_by_id('choose_dist').get_attribute('value')
                    value = value.split(":")

                    time.sleep(2)
                    markers = self.driver.find_elements_by_class_name(Data.dots)
                    dots = len(markers) - 1
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(4)
                    self.filename = p.get_download_dir() + '/' + self.fname.pat_districtwise() + management + '_all_allGrades__blocks_of_district_' + \
                                    value[1].strip() + '_' + self.data.get_current_date() + '.csv'
                    print(self.filename)
                    time.sleep(2)
                    if os.path.isfile(self.filename) != True:
                        print(dist.options[i], "district csv file not downloaded ")
                        count = count + 1
                    else:
                        markers = self.driver.find_elements_by_class_name(Data.dots)
                        dots = len(markers) - 1
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            data = list(csv_reader)
                            row_count = len(data)
                            if int(dots) != row_count:
                                print("Markers and csv file records count mismatched", dots, row_count)
                                count = count + 1
                        os.remove(self.filename)
            return count

    # def time_over_all(self):
    #         self.data = GetData()
    #         p = pwd()
    #         count = 0
    #         management = self.driver.find_element_by_id('name').text
    #         management = management[16:].lower().strip()
    #         self.fname = file_extention()
    #         self.driver.find_element_by_xpath(Locators.hyper_link).click()
    #         self.data.page_loading(self.driver)
    #         dist = Select(self.driver.find_element_by_id('choose_dist'))
    #         times = Select(self.driver.find_element_by_id('period'))
    #         for i in range(1, len(times.options)):
    #             times.select_by_index(i)
    #             time.sleep(3)
    #             if 'No data found' in self.driver.page_source:
    #                 print(times.options[i].text, 'has no data found')
    #             else:
    #                 for j in range(1, len(dist.options) - 1):
    #                     dist.select_by_index(j)
    #                     value = self.driver.find_element_by_id('choose_dist').get_attribute('value')
    #                     value = (value[4:] + '_').strip()
    #                     time.sleep(2)
    #                     markers = self.driver.find_elements_by_class_name(Locators.dots)
    #                     dots = len(markers) - 1
    #                     self.driver.find_element_by_id(Locators.Download).click()
    #                     time.sleep(4)
    #                     self.filename = p.get_download_dir() + '/' + self.fname.pat_districtwise() + management + '_all_allGrades__blocks_of_district_' + value.strip() + self.data.get_current_date() + '.csv'
    #                     print(self.filename)
    #                     time.sleep(2)
    #                     if os.path.isfile(self.filename) != True:
    #                         print(dist.options[i], "district csv file not downloaded ")
    #                         count = count + 1
    #                     else:
    #                         markers = self.driver.find_elements_by_class_name(Locators.dots)
    #                         dots = len(markers) - 1
    #                         with open(self.filename) as fin:
    #                             csv_reader = csv.reader(fin, delimiter=',')
    #                             header = next(csv_reader)
    #                             data = list(csv_reader)
    #                             row_count = len(data)
    #                             if int(dots) != row_count:
    #                                 print("Markers and csv file records count mismatched", dots, row_count)
    #                                 count = count + 1
    #                         os.remove(self.filename)
    #             return count

    def check_last_30_days(self):
        cal = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        times = Select(self.driver.find_element_by_id('period'))
        times.select_by_index(2)
        print(times.first_selected_option.text)
        time.sleep(3)
        schools = self.driver.find_element_by_id('schools').text
        students = self.driver.find_element_by_id('students').text
        attended = self.driver.find_element_by_id('studentsAttended').text

        schol = re.sub('\D', "", schools)
        std = re.sub('\D', "", students)
        attd = re.sub('\D', "", attended)

        print('Expected footer values : ', schol, std, attd)

        print('***************Block level footer values******************')

        self.driver.find_element_by_id(Data.block_btn).click()
        cal = GetData()
        if 'No data found' in self.driver.page_source:
            print("NO DATA FOUND")
        else:
            cal.page_loading(self.driver)
            time.sleep(5)
            dots = self.driver.find_elements_by_class_name(Data.dots)
            markers = len(dots) - 1
            if markers == 0:
                print("Block level markers are not present ")
                count = count + 1
            else:
                bschools = self.driver.find_element_by_id('schools').text
                bsch = re.sub('\D', "", bschools)

                bstudents = self.driver.find_element_by_id('students').text
                bstd = re.sub('\D', "", bstudents)

                battended = self.driver.find_element_by_id('studentsAttended').text
                battd = re.sub('\D', "", battended)

                print('after Clicking of block footer values ', bsch, bstd, battd)

                count = 0
                if int(bsch) != int(schol):
                    print('Block level footer mismatch found', int(bsch), int(schol))
                    count = count + 1
                if int(bstd) != int(std):
                    print('Block level footer mismatch found', int(bstd), int(std))
                    count = count + 1
                if int(battd) != int(attd):
                    print('Block level footer mismatch found', int(battd), int(attd))
                    count = count + 1

            print('***************Cluster level footer values******************')

            self.driver.find_element_by_id(Data.cluster_btn).click()
            cal = GetData()
            cal.page_loading(self.driver)
            time.sleep(10)
            if 'No data found' in self.driver.page_source:
                print("NO DATA FOUND")
            else:
                dots = self.driver.find_elements_by_class_name(Data.dots)
                dots = len(dots) - 1
                if dots == 0:
                    print("Cluster level markers are not present ")
                    count = count + 1

                cschools = self.driver.find_element_by_id('schools').text
                csch = re.sub('\D', '', cschools)

                cstudents = self.driver.find_element_by_id('students').text
                cstd = re.sub('\D', '', cstudents)

                cattended = self.driver.find_element_by_id('studentsAttended').text
                cattd = re.sub('\D', '', cattended)

                print('after Clicking of cluster footer values ', csch, cstd, cattd)

                if int(csch) != int(schol):
                    print('Cluster level footer mismatch found', int(csch), int(schol))
                    count = count + 1
                if int(cstd) != int(std):
                    print('Cluster level footer mismatch found', int(cstd), int(std))
                    count = count + 1
                if int(cattd) != int(attd):
                    print('Cluster level footer mismatch found', int(cattd), int(attd))
                    count = count + 1

            print('***************School level footer values******************')

            self.driver.find_element_by_id(Data.schoolbtn).click()
            cal = GetData()
            cal.page_loading(self.driver)
            time.sleep(10)
            if 'No data found' in self.driver.page_source:
                print("NO DATA FOUND")
            else:
                result = self.driver.find_elements_by_class_name(Data.dots)
                dots = len(result) - 1
                if dots == 0:
                    print("School level markers are not present ")
                    count = count + 1

                sschools = self.driver.find_element_by_id('schools').text
                ssch = re.sub('\D', '', cschools)

                sstudents = self.driver.find_element_by_id('students').text
                sstd = re.sub('\D', '', cstudents)

                sattended = self.driver.find_element_by_id('studentsAttended').text
                sattd = re.sub('\D', '', cattended)

                print('after Clicking of School footer values ', ssch, sstd, sattd)

                if int(ssch) != int(schol):
                    print('School level footer mismatch found', int(ssch), int(schol))
                    count = count + 1
                if int(sstd) != int(std):
                    print('School level footer mismatch found', int(sstd), int(std))
                    count = count + 1
                if int(sattd) != int(attd):
                    print('School level footer mismatch found', int(sattd), int(attd))
                    count = count + 1
        return count

    def check_last_7_days(self):
        cal = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        times = Select(self.driver.find_element_by_id('period'))
        times.select_by_index(3)
        print(times.first_selected_option.text)
        time.sleep(3)
        schools = self.driver.find_element_by_id('schools').text
        students = self.driver.find_element_by_id('students').text
        attended = self.driver.find_element_by_id('studentsAttended').text

        schol = re.sub('\D', "", schools)
        std = re.sub('\D', "", students)
        attd = re.sub('\D', "", attended)

        print('Expected footer values : ', schol, std, attd)

        print('***************Block level footer values******************')

        self.driver.find_element_by_id(Data.block_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(5)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        markers = len(dots) - 1
        if markers == 0:
            print("Block level markers are not present ")
            count = count + 1
        else:
            bschools = self.driver.find_element_by_id('schools').text
            bsch = re.sub('\D', "", bschools)

            bstudents = self.driver.find_element_by_id('students').text
            bstd = re.sub('\D', "", bstudents)

            battended = self.driver.find_element_by_id('studentsAttended').text
            battd = re.sub('\D', "", battended)

            print('after Clicking of block footer values ', bsch, bstd, battd)

            count = 0
            if int(bsch) != int(schol):
                print('Block level footer mismatch found', int(bsch), int(schol))
                count = count + 1
            if int(bstd) != int(std):
                print('Block level footer mismatch found', int(bstd), int(std))
                count = count + 1
            if int(battd) != int(attd):
                print('Block level footer mismatch found', int(battd), int(attd))
                count = count + 1

            print('***************Cluster level footer values******************')

            self.driver.find_element_by_id(Data.cluster_btn).click()
            cal = GetData()
            cal.page_loading(self.driver)
            dots = self.driver.find_elements_by_class_name(Data.dots)
            dots = len(dots) - 1
            if dots == 0:
                print("Cluster level markers are not present ")
                count = count + 1

            cschools = self.driver.find_element_by_id('schools').text
            csch = re.sub('\D', '', cschools)

            cstudents = self.driver.find_element_by_id('students').text
            cstd = re.sub('\D', '', cstudents)

            cattended = self.driver.find_element_by_id('studentsAttended').text
            cattd = re.sub('\D', '', cattended)

            print('after Clicking of cluster footer values ', csch, cstd, cattd)

            if int(csch) != int(schol):
                print('Cluster level footer mismatch found', int(csch), int(schol))
                count = count + 1
            if int(cstd) != int(std):
                print('Cluster level footer mismatch found', int(cstd), int(std))
                count = count + 1
            if int(cattd) != int(attd):
                print('Cluster level footer mismatch found', int(cattd), int(attd))
                count = count + 1

            print('***************School level footer values******************')

            self.driver.find_element_by_id(Data.schoolbtn).click()
            cal = GetData()
            cal.page_loading(self.driver)
            result = self.driver.find_elements_by_class_name(Data.dots)
            dots = len(result) - 1
            if dots == 0:
                print("Cluster level markers are not present ")
                count = count + 1

            sschools = self.driver.find_element_by_id('schools').text
            ssch = re.sub('\D', '', cschools)

            sstudents = self.driver.find_element_by_id('students').text
            sstd = re.sub('\D', '', cstudents)

            sattended = self.driver.find_element_by_id('studentsAttended').text
            sattd = re.sub('\D', '', cattended)

            print('after Clicking of School footer values ', ssch, sstd, sattd)

            if int(ssch) != int(schol):
                print('School level footer mismatch found', int(ssch), int(schol))
                count = count + 1
            if int(sstd) != int(std):
                print('School level footer mismatch found', int(sstd), int(std))
                count = count + 1
            if int(sattd) != int(attd):
                print('Cluster level footer mismatch found', int(sattd), int(attd))
                count = count + 1
        return count

    def check_last_30_days_districts(self):
        cal = GetData()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        times = Select(self.driver.find_element_by_id('period'))
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        times.select_by_index(2)
        time.sleep(2)
        timeseries = times.first_selected_option.text
        timeseries = timeseries.lower().replace(" ", '_')
        time.sleep(3)
        if 'No data found' in self.driver.page_source:
            print("No Data Found for last 30 days ")
        else:
            select_district = Select(self.driver.find_element_by_id('choose_dist'))
            count = 0
            for x in range(1, len(select_district.options)):
                select_district.select_by_index(x)
                cal.page_loading(self.driver)
                value = self.driver.find_element_by_id('choose_dist').get_attribute('value')
                value = value[4:] + '_'
                markers = self.driver.find_elements_by_class_name(Data.dots)
                if (len(markers) - 1) == 0:
                    print("District " + select_district.first_selected_option.text + " no data")
                    count = count + 1
                else:
                    self.driver.find_element_by_id(Data.Download).click()
                    p = pwd()
                    time.sleep(5)
                    self.filename = p.get_download_dir() + "/" + self.fname.pat_districtwise() + management + '_' + timeseries.lower() + '_allGrades__blocks_of_district_' + value.strip() + cal.get_current_date() + '.csv'
                    if not os.path.isfile(self.filename):
                        print("District " + select_district.first_selected_option.text + " csv is not downloaded")
                        count = count + 1
                    else:
                        data = pd.read_csv(self.filename)
                        student = data['Total Students'].sum()
                        schools = data['Total Schools'].sum()
                        attended = data['Students Attended'].sum()
                        students = self.driver.find_element_by_id("students").text
                        studs = re.sub('\D', "", students)

                        school = self.driver.find_element_by_id("schools").text
                        sc = re.sub('\D', "", school)

                        attend = self.driver.find_element_by_id("studentsAttended").text
                        atd = re.sub('\D', "", attend)

                        print('value on footer', student, schools, attended)
                        print('value on csv file', studs, sc, atd)

                        if int(studs) != int(student):
                            print(
                                "District " + select_district.first_selected_option.text + " student count mismatched",
                                int(studs), int(student))
                            count = count + 1

                        if int(sc) != int(schools):
                            print(
                                "District " + select_district.first_selected_option.text + " school count mismatched",
                                int(sc), int(schools))
                            count = count + 1

                        if int(atd) != int(attended):
                            print(
                                "District " + select_district.first_selected_option.text + " student attended mismatched",
                                int(atd), int(attended))
                            count = count + 1

                os.remove(self.filename)
        return count

    def check_last_7_days_districts(self):
        cal = GetData()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        times = Select(self.driver.find_element_by_id('period'))
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        timeseries = times.first_selected_option.text
        timeseries = timeseries.lower().replace(" ", '_')
        time.sleep(3)
        if 'No data found' in self.driver.page_source:
            print("No Data Found for last 7 days ")
        else:
            select_district = Select(self.driver.find_element_by_id('choose_dist'))
            for x in range(1, len(select_district.options)):
                select_district.select_by_index(x)
                cal.page_loading(self.driver)
                value = self.driver.find_element_by_id('choose_dist').get_attribute('value')
                value = value.split(":")
                values = value[1].strip()
                markers = self.driver.find_elements_by_class_name(Data.dots)
                if (len(markers) - 1) == 0:
                    print("District " + select_district.first_selected_option.text + " no data")
                    count = count + 1
                else:
                    self.driver.find_element_by_id(Data.Download).click()
                    p = pwd()
                    time.sleep(5)
                    self.filename = p.get_download_dir() + "/" + self.fname.pat_districtwise() + management + '_' + timeseries.lower() + '_allGrades__blocks_of_district_' + values + '_' + cal.get_current_date() + '.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print("District " + select_district.first_selected_option.text + " csv is not downloaded")
                        count = count + 1
                    else:
                        # with open(self.filename) as fin:
                        #     csv_reader = csv.reader(fin, delimiter=',')
                        #     header = next(csv_reader)
                        #     student = 0
                        #     schools = 0
                        #     attended = 0
                        #     for row in csv.reader(fin):
                        #         student += int(row[5])
                        #         schools += int(row[7])
                        #         attended += int(row[6])
                        #     print(self.filename, ':', student, schools, attended)
                        data = pd.read_csv(self.filename)
                        student = data['Total Students'].sum()
                        schools = data['Total Schools'].sum()
                        attended = data['Students Attended'].sum()
                        students = self.driver.find_element_by_id("students").text
                        studs = re.sub('\D', "", students)

                        school = self.driver.find_element_by_id("schools").text
                        sc = re.sub('\D', "", school)

                        attend = self.driver.find_element_by_id("studentsAttended").text
                        atd = re.sub('\D', "", attend)

                        print('value on footer', student, schools, attended)
                        print('value on csv file', studs, sc, atd)

                        if int(studs) != int(student):
                            print(
                                "District " + select_district.first_selected_option.text + " student count mismatched",
                                int(studs), int(student))
                            count = count + 1

                        if int(sc) != int(schools):
                            print(
                                "District " + select_district.first_selected_option.text + " school count mismatched",
                                int(sc), int(schools))
                            count = count + 1

                        if int(atd) != int(attended):
                            print(
                                "District " + select_district.first_selected_option.text + " student attended mismatched",
                                int(atd), int(attended))
                            count = count + 1
                os.remove(self.filename)
        return count

    def check_districts_block(self):
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
            for y in range(len(select_block.options) - 2, len(select_block.options)):
                select_block.select_by_index(y)
                cal.page_loading(self.driver)
                value = self.driver.find_element_by_id('choose_block').get_attribute('value')
                value = value[4:] + '_'
                markers = self.driver.find_elements_by_class_name(Data.dots)
                if len(markers) - 1 == 0:
                    print(
                        "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "No Locators")
                    count = count + 1
                else:
                    time.sleep(2)
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(2)
                    p = pwd()
                    self.filename = p.get_download_dir() + "/" + self.fname.pat_blockwise() + management + '_all_allGrades__clusters_of_block_' + value.strip() + cal.get_current_date() + '.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print(
                            "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "csv is not downloaded")
                        count = count + 1
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            data = list(csv_reader)
                            row_count = len(data)
                            dots = len(markers) - 1
                            if dots != row_count:
                                print('Markers records and csv file records are not matching ', dots, row_count)
                                count = count + 1
                        os.remove(self.filename)
                return count

    def check_last30days_districts_block(self):
        cal = GetData()
        count = 0
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(2)
        timeseries = period.first_selected_option.text
        timeseries = timeseries.lower().replace(" ", '_')
        time.sleep(3)
        if 'No data found' in self.driver.page_source:
            print("No Data Found for last 30 days ")
        else:
            select_district = Select(self.driver.find_element_by_id('choose_dist'))
            select_block = Select(self.driver.find_element_by_id('choose_block'))
            for x in range(len(select_district.options) - 1, len(select_district.options)):
                select_district.select_by_index(x)
                cal.page_loading(self.driver)
                for y in range(1, len(select_block.options)):
                    select_block.select_by_index(y)
                    cal.page_loading(self.driver)
                    value = self.driver.find_element_by_id('choose_block').get_attribute('value')
                    value = value.split(":")
                    values = value[1].strip()
                    markers = self.driver.find_elements_by_class_name(Data.dots)
                    if len(markers) - 1 == 0:
                        print(
                            "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "No Locators")
                        count = count + 1
                    else:
                        self.driver.find_element_by_id(Data.Download).click()
                        time.sleep(3)
                        p = pwd()
                        self.filename = p.get_download_dir() + "/" + self.fname.pat_blockwise() + management + '_' + timeseries + '_allGrades__clusters_of_block_' + values + '_' + cal.get_current_date() + '.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(
                                "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "csv is not downloaded")
                            count = count + 1
                        else:
                            data = pd.read_csv(self.filename)
                            student = data['Total Students'].sum()
                            schools = data['Total Schools'].sum()
                            attended = data['Students Attended'].sum()
                            students = self.driver.find_element_by_id("students").text
                            studs = re.sub('\D', "", students)

                            students = self.driver.find_element_by_id("students").text
                            studs = re.sub('\D', "", students)

                            school = self.driver.find_element_by_id("schools").text
                            sc = re.sub('\D', "", school)

                            attend = self.driver.find_element_by_id("studentsAttended").text
                            atd = re.sub('\D', "", attend)

                            print('value on footer', student, schools, attended)
                            print('value on csv file', studs, sc, atd)

                            if int(studs) != int(student):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + " student count mismatched",
                                    int(studs), int(student))
                                count = count + 1

                            if int(sc) != int(schools):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + " school count mismatched",
                                    int(sc), int(schools))
                                count = count + 1

                            if int(atd) != int(attended):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + " student attended mismatched",
                                    int(atd), int(attended))
                                count = count + 1
                    os.remove(self.filename)
        return count

    def check_last7days_districts_block(self):
        cal = GetData()
        count = 0
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(3)
        timeseries = period.first_selected_option.text
        timeseries = timeseries.lower().replace(" ", '_')
        time.sleep(3)
        if 'No data found' in self.driver.page_source:
            print("No Data Found for last 7 days ")
        else:
            select_district = Select(self.driver.find_element_by_id('choose_dist'))
            select_block = Select(self.driver.find_element_by_id('choose_block'))
            for x in range(len(select_district.options) - 1, len(select_district.options)):
                select_district.select_by_index(x)
                cal.page_loading(self.driver)
                for y in range(len(select_block.options) - 3, len(select_block.options)):
                    select_block.select_by_index(y)
                    cal.page_loading(self.driver)
                    value = self.driver.find_element_by_id('choose_block').get_attribute('value')
                    value = value.split(":")
                    values = value[1].strip()
                    markers = self.driver.find_elements_by_class_name(Data.dots)
                    if len(markers) - 1 == 0:
                        print(
                            "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "No Locators")
                        count = count + 1
                    else:
                        time.sleep(2)
                        self.driver.find_element_by_id(Data.Download).click()
                        time.sleep(2)
                        p = pwd()
                        self.filename = p.get_download_dir() + "/" + self.fname.pat_blockwise() + management + "_" + timeseries + '_allGrades__clusters_of_block_' + values + "_" + cal.get_current_date() + '.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(
                                "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "csv is not downloaded")
                            count = count + 1
                        else:
                            data = pd.read_csv(self.filename)
                            student = data['Total Students'].sum()
                            schools = data['Total Schools'].sum()
                            attended = data['Students Attended'].sum()
                            students = self.driver.find_element_by_id("students").text
                            studs = re.sub('\D', "", students)

                            students = self.driver.find_element_by_id("students").text
                            studs = re.sub('\D', "", students)

                            school = self.driver.find_element_by_id("schools").text
                            sc = re.sub('\D', "", school)

                            attend = self.driver.find_element_by_id("studentsAttended").text
                            atd = re.sub('\D', "", attend)

                            print('value on footer', student, schools, attended)
                            print('value on csv file', studs, sc, atd)

                            if int(studs) != int(student):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + " student count mismatched",
                                    int(studs), int(student))
                                count = count + 1

                            if int(sc) != int(schools):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + " school count mismatched",
                                    int(sc), int(schools))
                                count = count + 1

                            if int(atd) != int(attended):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + " student attended mismatched",
                                    int(atd), int(attended))
                                count = count + 1
                    os.remove(self.filename)
        return count

    def check_last30_district_block_cluster(self):
        cal = GetData()
        count = 0
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(2)
        time.sleep(3)
        if 'No data found' in self.driver.page_source:
            print(period.first_selected_option.text, ' is not having data')
        else:
            timeseries = period.first_selected_option.text
            timeseries = timeseries.lower().replace(" ", '_')
            select_district = Select(self.driver.find_element_by_id('choose_dist'))
            select_block = Select(self.driver.find_element_by_id('choose_block'))
            select_cluster = Select(self.driver.find_element_by_id('choose_cluster'))
            for x in range(len(select_district.options) - 1, len(select_district.options)):
                select_district.select_by_index(x)
                cal.page_loading(self.driver)
                for y in range(len(select_block.options) - 1, len(select_block.options)):
                    select_block.select_by_index(y)
                    cal.page_loading(self.driver)
                    for z in range(len(select_cluster.options) - 2, len(select_cluster.options)):
                        select_cluster.select_by_index(z)
                        time.sleep(2)
                        cal.page_loading(self.driver)
                        value = self.driver.find_element_by_id('choose_cluster').get_attribute('value')
                        value = value.split(":")
                        values = value[1].strip() + '_'
                        markers = self.driver.find_elements_by_class_name(Data.dots)
                        if len(markers) - 1 == 0:
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "No data")
                            count = count + 1
                        time.sleep(2)
                        self.driver.find_element_by_id(Data.Download).click()
                        time.sleep(3)
                        p = pwd()
                        self.filename = p.get_download_dir() + "/" + self.fname.pat_clusterwise() + management + '_' + timeseries + '_allGrades__schools_of_cluster_' + values + cal.get_current_date() + '.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "csv is not downloaded")
                            count = count + 1
                        else:
                            data = pd.read_csv(self.filename)
                            student = data['Total Students'].sum()
                            schools = data['Total Schools'].sum()
                            attended = data['Students Attended'].sum()
                            students = self.driver.find_element_by_id("students").text
                            studs = re.sub('\D', "", students)

                            students = self.driver.find_element_by_id("students").text
                            studs = re.sub('\D', "", students)

                            school = self.driver.find_element_by_id("schools").text
                            sc = re.sub('\D', "", school)

                            attend = self.driver.find_element_by_id("studentsAttended").text
                            atd = re.sub('\D', "", attend)

                            print('value on footer', student, schools, attended)
                            print('value on csv file', studs, sc, atd)

                            if int(studs) != int(student):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + " student count mismatched",
                                    int(studs), int(student))
                                count = count + 1

                            if int(sc) != int(schools):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + " school count mismatched",
                                    int(sc), int(schools))
                                count = count + 1

                            if int(atd) != int(attended):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + " student attended mismatched",
                                    int(atd), int(attended))
                                count = count + 1

                            os.remove(self.filename)
        return count

    def check_last7_district_block_cluster(self):
        cal = GetData()
        count = 0
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(3)
        time.sleep(3)
        if 'No data found' in self.driver.page_source:
            print(period.first_selected_option.text, ' is not having data')
        else:
            timeseries = period.first_selected_option.text
            timeseries = timeseries.lower().replace(" ", '_')
            select_district = Select(self.driver.find_element_by_id('choose_dist'))
            select_block = Select(self.driver.find_element_by_id('choose_block'))
            select_cluster = Select(self.driver.find_element_by_id('choose_cluster'))
            for x in range(len(select_district.options) - 1, len(select_district.options)):
                select_district.select_by_index(x)
                cal.page_loading(self.driver)
                for y in range(len(select_block.options) - 1, len(select_block.options)):
                    select_block.select_by_index(y)
                    cal.page_loading(self.driver)
                    for z in range(len(select_cluster.options) - 2, len(select_cluster.options)):
                        select_cluster.select_by_index(z)
                        time.sleep(2)
                        cal.page_loading(self.driver)
                        value = self.driver.find_element_by_id('choose_cluster').get_attribute('value')
                        value = value.split(":")
                        values = value[1].strip() + '_'
                        markers = self.driver.find_elements_by_class_name(Data.dots)
                        if len(markers) - 1 == 0:
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "No data")
                            count = count + 1
                        time.sleep(2)
                        self.driver.find_element_by_id(Data.Download).click()
                        time.sleep(3)
                        p = pwd()
                        self.filename = p.get_download_dir() + "/" + self.fname.pat_clusterwise() + management + '_' + timeseries + '_allGrades__schools_of_cluster_' + values + cal.get_current_date() + '.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "csv is not downloaded")
                            count = count + 1
                        else:
                            data = pd.read_csv(self.filename)
                            student = data['Total Students'].sum()
                            schools = data['Total Schools'].sum()
                            attended = data['Students Attended'].sum()
                            students = self.driver.find_element_by_id("students").text
                            studs = re.sub('\D', "", students)

                            students = self.driver.find_element_by_id("students").text
                            studs = re.sub('\D', "", students)

                            school = self.driver.find_element_by_id("schools").text
                            sc = re.sub('\D', "", school)

                            attend = self.driver.find_element_by_id("studentsAttended").text
                            atd = re.sub('\D', "", attend)

                            print('value on footer', student, schools, attended)
                            print('value on csv file', studs, sc, atd)

                            if int(studs) != int(student):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + " student count mismatched",
                                    int(studs), int(student))
                                count = count + 1

                            if int(sc) != int(schools):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + " school count mismatched",
                                    int(sc), int(schools))
                                count = count + 1

                            if int(atd) != int(attended):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + " student attended mismatched",
                                    int(atd), int(attended))
                                count = count + 1

                            os.remove(self.filename)
        return count

    def check_landing_page(self):
        self.data = GetData()
        count = 0
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(2)
        self.data.navigate_to_periodic_report()
        self.data.page_loading(self.driver)
        if 'pat-report' in self.driver.current_url:
            print('Navigated to Periodic Assessment report')
        else:
            print('Pat report icon is not working')
            count = count + 1
        return count

    def click_download_icon_of_blocks(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.block_btn).click()
        cal.page_loading(self.driver)
        marker = self.driver.find_elements_by_class_name(Data.dots)
        counts = len(marker) - 1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        p = pwd()
        count = 0
        self.filename = p.get_download_dir() + "/" + self.fname.pat_block()
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        if os.path.isfile(self.filename) == True:
            print('Block wise csv file is downloaded')
        os.remove(self.filename)
        return counts

    def click_download_icon_of_clusters(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cluster_btn).click()
        cal.page_loading(self.driver)
        markers = self.driver.find_elements_by_class_name(Data.dots)
        dots = len(markers) - 1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(10)
        p = pwd()
        count = 0
        self.filename = p.get_download_dir() + "/" + self.fname.pat_cluster()
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        if os.path.isfile(self.filename) == True:
            print('Cluster wise csv file downloaded')
        os.remove(self.filename)
        return dots

    def click_download_icon_of_schools(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.schoolbtn).click()
        time.sleep(10)
        markers = self.driver.find_elements_by_class_name(Data.dots)
        dots = len(markers) - 1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(15)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.pat_school()
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        if os.path.isfile(self.filename) == True:
            print("School wise csv file is downloaded")
        os.remove(self.filename)
        return dots

    def check_dots_on_each_districts(self):
        cal = GetData()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        count = 0
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            time.sleep(5)
            dots = self.driver.find_elements_by_class_name(Data.dots)
            if int(len(dots) - 1) == 0:
                print("District" + select_district.first_selected_option.text + "Markers are not found")
                count = count + 1

        return count
