import csv
import os
import re
import time

import pandas as pd
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.support.select import Select

from Locators.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class student_attendance_report():
    def __init__(self,driver, year, month):
        self.driver = driver
        self.year = year.strip()
        self.month = month.strip()
        self.student_count = ''
        self.school_count = ''

    global student_count

    def click_on_sar(self):
        try:
            cal = GetData()
            cal.click_on_state(self.driver)
            cal.page_loading(self.driver)
            cal.navigate_to_student_report()
            cal.page_loading(self.driver)
            return self.driver.current_url

        except ElementClickInterceptedException:
            print("Element not found and test failed")

    def check_markers_on_block_map(self):
        self.driver.find_element_by_id(Data.SAR_Blocks_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        return dots
    def check_markers_on_clusters_map(self):
        self.driver.find_element_by_id(Data.SAR_Clusters_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(5)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        return dots
    def check_markers_on_schools_map(self):
        self.driver.find_element_by_id(Data.SAR_Schools_btn).click()
        cal = GetData()
        time.sleep(10)
        cal.page_loading(self.driver)
        result = self.driver.find_elements_by_class_name(Data.dots)
        return   result

    def test_academicYear_dropdown(self):
        cal = GetData()
        count = 0
        p = pwd()
        cal.page_loading(self.driver)
        cal.click_on_state(self.driver)
        time.sleep(2)
        academic = Select(self.driver.find_element_by_id('academicYear'))
        opt = len(academic.options)-1
        for i in range(1,len(academic.options)):
             academic.select_by_index(i)
             time.sleep(3)
             year = academic.first_selected_option.text+""
             self.driver.find_element_by_id('downloadRaw').click()
             time.sleep(5)
             self.filename = p.get_download_dir()+"/student_attendance_all_districts_"+year+".csv"
             if self.filename != True:
                 print(year,'raw file is not downloaded')
                 count = count + 1
             else:
                 print(year,"raw file is downloaded")
                 os.remove(self.filename)
        return count,opt


    def test_click_on_trends_link(self):
        cal = GetData()
        count = 0
        p = pwd()
        cal.page_loading(self.driver)
        cal.click_on_state(self.driver)
        self.driver.find_element_by_id('trends').click()
        time.sleep(2)
        if "student-attendance-chart" in self.driver.current_url:
            print("Trend chart screen is displayed ")
        else:
            print("Trend chart is not displayed")
            count = count + 1
        return count

    def click_download_icon_of_district(self):
        cal = GetData()
        count = 0
        files = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        self.year ,self.month = cal.get_student_month_and_year_values()
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        p = pwd()
        self.filename = p.get_download_dir()+files.student_download()+name+'_allDistricts_'+self.month+'_'+self.year+'_'+cal.get_current_date()+".csv"
        print(self.filename)
        if not os.path.isfile(self.filename):
            print("Districtwise csv is not downloaded")
            count = count + 1
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                total = 0
                schools = 0
                for row in csv.reader(fin):
                    total += int(row[3])
                    schools += int(row[4])
                students = self.driver.find_element_by_id("students").text
                res = re.sub('\D', "", students)

                school = self.driver.find_element_by_id("schools").text
                sc = re.sub('\D', "", school)
                if int(res) != total:
                    print("student count mismatched")
                    count = count + 1
                if int(sc) != schools:
                    print("school count mismatched")
                    count = count + 1
            os.remove(self.filename)
        return  count




    def click_download_icon_of_blocks(self):
        cal = GetData()
        file = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        self.year, self.month = cal.get_student_month_and_year_values()
        self.driver.find_element_by_id(Data.SAR_Blocks_btn).click()
        cal.page_loading(self.driver)
        time.sleep(5)
        if 'No data found' in self.driver.page_source:
            print("Year and month does not having data showing no data found")
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(5)
            p = pwd()
            count = 0
            self.filename = p.get_download_dir() + file.student_block_download() + name + '_allBlocks_' + self.month + '_' + self.year + '_' + cal.get_current_date() + ".csv"
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print('Block level csv file is not downloaded')
                count = count + 1
            else:
                df = pd.read_csv(self.filename)
                student = df['Number Of Students'].sum()
                sch = df['Number Of Schools'].sum()

                students = self.driver.find_element_by_id("students").text
                stds = re.sub('\D', "", students)

                school = self.driver.find_element_by_id('schools').text
                scs = re.sub('\D', "", school)

                if int(stds) != int(student):
                    print('Number of students with missing data mismatch found', stds, student)
                    count = count + 1
                if int(scs) != int(sch):
                    print('Number of schools with missing data mismatch found', scs, sch)
                    count = count + 1
                os.remove(self.filename)
            return count

    def click_download_icon_of_clusters(self):
        cal = GetData()
        file = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        self.year,self.month = cal.get_student_month_and_year_values()
        self.driver.find_element_by_id(Data.SAR_Clusters_btn).click()
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        p = pwd()
        self.filename = p.get_download_dir() +file.student_cluster_download()+name+'_allClusters_'+self.month+'_'+self.year+'_'+cal.get_current_date()+".csv"
        print(self.filename)
        return os.path.isfile(self.filename)

    def remove_csv(self):
        os.remove(self.filename)

    def click_download_icon_of_schools(self):
        cal = GetData()
        file = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        self.year,self.month = cal.get_student_month_and_year_values()
        self.driver.find_element_by_id(Data.SAR_Schools_btn).click()
        cal.page_loading(self.driver)
        time.sleep(5)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        p = pwd()
        self.filename = p.get_download_dir() +file.student_school_download()+name+'_allSchools_'+self.month+'_'+self.year+'_'+cal.get_current_date()+".csv"
        print(self.filename)
        return os.path.isfile(self.filename)


    def check_districts_csv_download(self):
        cal = GetData()
        files = file_extention()
        cal.click_on_state(self.driver)
        self.year, self.month = cal.get_student_month_and_year_values()
        cal.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_id('period'))
        timeseries.select_by_index(5)
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        count = 0
        for x in range(1, len(select_district.options) - 27):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            val = self.driver.find_element_by_name('myDistrict').get_attribute('value')
            distval = val[4:] + '_'
            markers = self.driver.find_elements_by_class_name(Data.dots)
            if len(markers) - 1 == 0:
                print("District" + select_district.first_selected_option.text + "no data")
                count = count + 1
            time.sleep(2)
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + files.student_districtwise_download() + name + '_blockPerDistricts_of_district_' + distval.strip() + self.month + "_" + self.year + '_' + cal.get_current_date() + ".csv"
            print(self.filename)
            if not os.path.isfile(self.filename):
                print("District" + select_district.first_selected_option.text + "csv is not downloaded")
                count = count + 1
            else:
                with open(self.filename) as fin:
                    csv_reader = csv.reader(fin, delimiter=',')
                    header = next(csv_reader)
                    total = 0
                    schools = 0
                    for row in csv.reader(fin):
                        total += int(row[5])
                        schools += int(row[6])
                    students = self.driver.find_element_by_id("students").text
                    res = re.sub('\D', "", students)

                    school = self.driver.find_element_by_id("schools").text
                    sc = re.sub('\D', "", school)

                    if int(res) != total:
                        print("District" + select_district.first_selected_option.text + "student count mismatched")
                        count = count + 1
                    if int(sc) != schools:
                        print("District" + select_district.first_selected_option.text + "school count mismatched")
                        count = count + 1
                os.remove(self.filename)
        return count

    def check_csv_download(self):
        cal = GetData()
        files = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        self.year ,self.month = cal.get_student_month_and_year_values()
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        select_block = Select(self.driver.find_element_by_name('myBlock'))
        count = 0
        for x in range(1, len(select_district.options)-31):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            for y in range(1, len(select_block.options)):
                select_block.select_by_index(y)
                cal.page_loading(self.driver)
                value = self.driver.find_element_by_name('myBlock').get_attribute('value')
                blkvalue = value[4:]+'_'
                time.sleep(2)
                markers = self.driver.find_elements_by_class_name(Data.dots)
                if len(markers) - 1 == 0:
                    print(
                        "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "No Locators")
                    count = count + 1
                time.sleep(2)
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(5)
                p = pwd()
                self.filename = p.get_download_dir() +files.student_blockwise_download()+name+"_clusterPerBlocks_of_block_"+blkvalue.strip()+self.month + "_" + self.year+'_'+cal.get_current_date()+".csv"
                print(self.filename)
                if not os.path.isfile(self.filename):
                    print(
                        "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "csv is not downloaded")
                    count = count + 1
                else:
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        total = 0
                        schools = 0
                        for row in csv.reader(fin):
                            total += int(row[7].replace(',',''))
                            schools += int(row[8].replace(',',''))
                        students = self.driver.find_element_by_id("students").text
                        res = re.sub('\D', "", students)

                        school = self.driver.find_element_by_id("schools").text
                        sc = re.sub('\D', "", school)
                        if int(res) != total:
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "student count mismatched")
                            count = count + 1
                        if int(sc) != schools:
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "school count mismatched")
                            count = count + 1
                    os.remove(self.filename)

        return count

    def check_district_block_cluster(self):
        cal = GetData()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        name = management[16:].strip().lower()
        self.year ,self.month = cal.get_student_month_and_year_values()
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        select_block = Select(self.driver.find_element_by_name('myBlock'))
        select_cluster = Select(self.driver.find_element_by_name('myCluster'))
        count = 0
        for x in range(len(select_district.options)-1, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            for y in range(len(select_block.options)-1, len(select_block.options)):
                select_block.select_by_index(y)
                cal.page_loading(self.driver)
                for z in range(1, len(select_cluster.options)):
                    select_cluster.select_by_index(z)
                    cal.page_loading(self.driver)
                    value = self.driver.find_element_by_name('myCluster').get_attribute('value')
                    cluvalue = (value[3:]+'_').replace(':','').strip()
                    markers = self.driver.find_elements_by_class_name(Data.dots)
                    files = file_extention()
                    if len(markers) - 1 == 0:
                        print(
                            "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "No data")
                        count = count + 1
                    time.sleep(2)
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(3)
                    p = pwd()
                    self.filename =  p.get_download_dir() +files.student_clusterwise_download()+name+'_schoolPerClusters_of_cluster_'+cluvalue.strip()+ self.month + "_" + self.year+'_'+cal.get_current_date() + ".csv"
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print(
                            "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "csv is not downloaded")
                        count = count + 1
                    else:
                        df = pd.read_csv(self.filename)
                        student = df['Number Of Students'].sum()
                        students = self.driver.find_element_by_id("students").text
                        std = re.sub('\D', "", students)

                        school = self.driver.find_element_by_id("schools").text
                        sc = re.sub('\D', "", school)

                        if int(std) != student:
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "student count mismatched")
                            count = count + 1
                        if int(sc) != len(markers)-1:
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "school count mismatched")
                            count = count + 1
                    os.remove(self.filename)

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
        result2 = self.driver.find_element_by_id('choose_cluster').is_displayed()
        dist = Select(self.driver.find_element_by_id('choose_dist'))
        choose_dist = dist.first_selected_option.text
        return result1, result2, choose_dist

    def click_HomeButton(self):
            self.driver.find_element_by_id(Data.cQube_logo).click()
            cal = GetData()
            cal.page_loading(self.driver)
            cal.navigate_to_student_report()
            return self.driver.current_url

    def click_on_blocks_click_on_home_icon(self):
        self.driver.find_element_by_id(Data.SAR_Blocks_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)

    #Student_Acedemic dropdown

    def check_academic_dropdown_is_present(self):
        cal = GetData()
        cal.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        academic = Select(self.driver.find_element_by_id('academicYear'))
        options = len(academic.options)-1
        return options

    def check_academic_dropdown_options(self):
        cal = GetData()
        count = 0
        cal.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        academic = Select(self.driver.find_element_by_id('academicYear'))
        options = len(academic.options) - 1
        for i in range(1,len(academic.options)):
            academic.select_by_index(i)
            print(academic.options[i].text,'is selected')
            count = count + 1
            time.sleep(2)
        cal.page_loading(self.driver)
        return count

    def download_yearwise_files_by_academic_year(self):
        cal = GetData()
        count = 0
        p = pwd()
        cal.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        file = file_extention()
        academic = Select(self.driver.find_element_by_id('academicYear'))
        options = len(academic.options) - 1
        for i in range(1, len(academic.options)):
            academic.select_by_index(i)
            print(academic.options[i].text, 'is selected')
            self.driver.find_element_by_id('downloadRaw').click()
            time.sleep(5)
            self.filename = p.get_download_dir() +"/" + file.student_academic_files()+(academic.options[i].text).strip()+'.csv'
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print(academic.options[i].text,"academic csv file is not download")
                count = count + 1
            cal.page_loading(self.driver)
        return count

    def block_total_no_of_students(self):
        cal = GetData()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        # self.driver.find_element_by_id()
        # total_students = self.driver.find_element_by_id(Data.students).text
        # print(total_students)
        # time.sleep(1)
        # students = re.sub("\D", "", total_students)
        # self.student_count = students
        #
        # no_schools = self.driver.find_element_by_id(Data.schoolcount).text
        # print(no_schools)
        # schools = re.sub("\D", "", no_schools)
        # self.school_count = schools
        #
        # print(students ,schools,"  -student and school -")
        #
        # self.driver.find_element_by_id(Data.SAR_Blocks_btn).click()
        # cal.page_loading(self.driver)
        # time.sleep(5)
        # Bstudents = self.driver.find_element_by_id(Data.students).text
        # Bstudent = re.sub("\D", "", Bstudents)
        #
        # Bschools = self.driver.find_element_by_id(Data.schoolcount).text
        # Bschools = re.sub("\D", "", Bschools)
        #
        # print('final values',self.student_count, Bstudent, self.school_count, Bschools)
        # return self.student_count, Bstudent, self.school_count, Bschools
        total_students = self.driver.find_element_by_id(Data.students).text
        students = re.sub("\D", "", total_students)
        student_count = students

        no_schools = self.driver.find_element_by_id(Data.schoolcount).text
        print(no_schools)
        schools = re.sub("\D", "", no_schools)
        school_count = schools

        self.driver.find_element_by_id(Data.SAR_Blocks_btn).click()
        cal.page_loading(self.driver)
        time.sleep(5)

        block_stds = students
        block_schs = schools
        print( student_count, block_stds, school_count, block_schs)
        return student_count, block_stds, school_count, block_schs

    def cluster_total_no_of_students(self):
        self.driver.find_element_by_id(Data.SAR_Clusters_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(10)
        Cstudents = self.driver.find_element_by_id(Data.students).text
        Cstudent = re.sub("\D", "", Cstudents)
        Cschools = self.driver.find_element_by_id(Data.schoolcount).text
        Cschool = re.sub("\D", "", Cschools)
        print(self.student_count, Cstudent,self.school_count,Cschool)
        return self.student_count, Cstudent,self.school_count,Cschool


    def schools_total_no_of_students(self):
        self.driver.find_element_by_id(Data.SAR_Schools_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(10)
        Sstudents = self.driver.find_element_by_id(Data.students).text
        Sstudent = re.sub("\D", "", Sstudents)

        Sschools = self.driver.find_element_by_id(Data.schoolcount).text
        Sschool = re.sub("\D", "", Sschools)
        print(self.student_count, Sstudent, self.school_count, Sschool)
        return self.student_count, Sstudent, self.school_count, Sschool

    def click_on_logout(self):
        self.driver.find_element_by_id(Data.menu_icon).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.logout).click()
        return self.driver.title

    def block_no_of_schools(self):
        cal = GetData()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        no_schools = self.driver.find_element_by_id(Data.students).text
        schools = re.sub("\D", "", no_schools)
        self.school_count = schools
        self.driver.find_element_by_id(Data.SAR_Blocks_btn).click()
        cal.page_loading(self.driver)
        Bschools = self.driver.find_element_by_id(Data.students).text
        Bschools = re.sub("\D", "", Bschools)
        return self.school_count, Bschools

    def cluster_no_of_schools(self):
        self.driver.find_element_by_id(Data.SAR_Clusters_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(15)
        Cschools = self.driver.find_element_by_id(Data.students).text
        Cschools = re.sub("\D", "", Cschools)
        return self.school_count, Cschools

    def schools_no_of_schools(self):
        try:
            self.driver.find_element_by_id(Data.SAR_Schools_btn).click()
            cal = GetData()
            cal.page_loading(self.driver)
            time.sleep(15)
            Sschools = self.driver.find_element_by_id(Data.students).text
            Sschools = re.sub("\D", "", Sschools)
            return self.school_count, Sschools
        except NoSuchElementException:
            print("Element Not Found")

    global student_count

    def block_total_no_of_students(self):
        cal = GetData()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        total_students = self.driver.find_element_by_id(Data.students).text
        students = re.sub("\D", "", total_students)
        self.student_count = students
        self.driver.find_element_by_id(Data.SAR_Blocks_btn).click()
        cal.page_loading(self.driver)
        Bstudents = self.driver.find_element_by_id(Data.students).text
        Bstudent = re.sub("\D", "", Bstudents)
        return self.student_count, Bstudent

    def cluster_total_no_of_students(self):
        self.driver.find_element_by_id(Data.SAR_Clusters_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(20)
        Cstudents = self.driver.find_element_by_id(Data.students).text
        Cstudent = re.sub("\D", "", Cstudents)
        return self.student_count, Cstudent

    def schools_total_no_of_students(self):
        self.driver.find_element_by_id(Data.SAR_Schools_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(20)
        Sstudents = self.driver.find_element_by_id(Data.students).text
        Sstudent = re.sub("\D", "", Sstudents)
        return self.student_count, Sstudent
