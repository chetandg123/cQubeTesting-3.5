import csv
import os
import re
import time

from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Locators.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class Teacher_Attendance_report():
    def __init__(self, driver, year, month):
        self.driver = driver
        self.year = year.strip()
        self.month = month.strip()
        self.student_count = ''
        self.driver = driver
        self.student_count = ''

    global student_count

    global student_count

    def click_on_tar(self):
        try:
            cal = GetData()
            self.driver.find_element_by_xpath(Data.hyper_link).click()
            time.sleep(3)
            cal.page_loading(self.driver)
            self.driver.find_element_by_id('cubeLogo').click()
            time.sleep(2)
            cal.navigate_to_teacher_attendance_report()
            cal.page_loading(self.driver)
            return self.driver.current_url

        except ElementClickInterceptedException:
            print("Element not found and test failed")

    def check_markers_on_block_map(self):
        self.driver.find_element_by_id(Data.SAR_Blocks_btn).click()
        cal = GetData()
        time.sleep(15)
        cal.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        return dots

    def check_markers_on_clusters_map(self):
        self.driver.find_element_by_id(Data.SAR_Clusters_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(20)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        return dots

    def check_markers_on_school_map(self):
        self.driver.find_element_by_id(Data.SAR_Schools_btn).click()
        cal = GetData()
        time.sleep(15)
        cal.page_loading(self.driver)
        result = self.driver.find_elements_by_class_name(Data.dots)
        return result

    def click_download_icon_of_district(self):
        cal = GetData()
        count = 0
        files = file_extention()
        management_name = self.driver.find_element_by_id('name').text
        period = Select(self.driver.find_element_by_id('period'))
        name = management_name[16:].strip().lower()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        p = pwd()
        self.filename = p.get_download_dir()+'/'+files.teacher_download()+name+'_allDistricts_overall_'+cal.get_current_date()+".csv"
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
                    total += int(row[3].replace(',',''))
                    schools += int(row[4].replace(',',''))
                students = self.driver.find_element_by_id("students").text
                res = re.sub('\D', "", students)

                school = self.driver.find_element_by_id("schools").text
                sc = re.sub('\D', "", school)
                if int(res) != total:
                    print(int(res) , total,"Teacher count mismatched")
                    count = count + 1
                if int(sc) != schools:
                    print(int(sc) ,schools,"school count mismatched")
                    count = count + 1
            os.remove(self.filename)
        return  count

    def click_download_icon_of_blocks(self):
        cal = GetData()
        files = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        period = Select(self.driver.find_element_by_id('period'))
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        self.driver.find_element_by_id(Data.SAR_Blocks_btn).click()
        cal.page_loading(self.driver)
        time.sleep(5)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        p = pwd()
        self.filename = p.get_download_dir() +'/'+files.teacher_block_download()+name+"_allBlocks_overall_"+cal.get_current_date()+".csv"
        print(self.filename)
        return os.path.isfile(self.filename)

    def remove_csv(self):
        os.remove(self.filename)

    def click_download_icon_of_clusters(self):
        cal = GetData()
        files = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        self.year,self.month = cal.get_student_month_and_year_values()
        self.driver.find_element_by_id(Data.SAR_Clusters_btn).click()
        cal.page_loading(self.driver)
        time.sleep(5)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        p = pwd()
        count = 0
        self.filename = p.get_download_dir() +'/'+files.teacher_cluster_download()+name+'_allClusters_'+self.month+"_"+self.year+'_'+cal.get_current_date()+".csv"
        print(self.filename)
        if os.path.isfile(self.filename) !=True:
            count = count + 1
        else:
            os.remove(self.filename)
        return count
    def click_download_icon_of_schools(self):
        cal = GetData()
        files = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        self.year,self.month =cal.get_student_month_and_year_values()
        self.driver.find_element_by_id(Data.SAR_Schools_btn).click()
        cal.page_loading(self.driver)
        time.sleep(5)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        p = pwd()
        self.filename = p.get_download_dir()+'/'+files.teacher_school_download()+name+'_allSchools_'+self.month +'_'+self.year+'_'+cal.get_current_date()+'.csv'
        print(self.filename)
        return os.path.isfile(self.filename)

    def check_districts_csv_download(self):
        cal = GetData()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        self.year,self.month = cal.get_student_month_and_year_values()
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        count = 0
        files = file_extention()
        for x in range(1, len(select_district.options)-26):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            value = self.driver.find_element_by_name('myDistrict').get_attribute('value')
            value = value.split(":")
            markers = self.driver.find_elements_by_class_name(Data.dots)
            if len(markers) - 1 == 0:
                print("District" + select_district.first_selected_option.text + "no data")
                count = count + 1
            time.sleep(2)
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            p = pwd()
            self.filename = p.get_download_dir() +'/'+files.teacher_districtwise_download()+name+"_blockPerDistricts_of_district_"+value[1].strip()+'_'+ self.month + "_" + self.year+'_'+cal.get_current_date() + ".csv"
            print(self.filename)
            if not os.path.isfile(self.filename):
                print("District - " + select_district.first_selected_option.text + " csv is not downloaded")
                count = count + 1
            else:
                with open(self.filename) as fin:
                    csv_reader = csv.reader(fin, delimiter=',')
                    header = next(csv_reader)
                    total = 0
                    schools = 0
                    for row in csv.reader(fin):
                        total += int(row[5].replace(',',''))
                        schools += int(row[6].replace(',',''))
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
                self.remove_csv()

        return count
    def check_dots_on_each_districts(self):
        cal = GetData()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        count = 0
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            time.sleep(3)
            dots = self.driver.find_elements_by_class_name(Data.dots)
            if int(len(dots) - 1) == 0:
                print("District" + select_district.first_selected_option.text + "Markers are not found")
                count = count + 1
        return count

    def check_csv_download(self):
        cal = GetData()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        self.year,self.month = cal.get_student_month_and_year_values()
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        select_block = Select(self.driver.find_element_by_name('myBlock'))
        count = 0
        files = file_extention()
        for x in range(len(select_district.options)-2, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            for y in range(len(select_block.options)-2, len(select_block.options)):
                select_block.select_by_index(y)
                cal.page_loading(self.driver)
                value = self.driver.find_element_by_name('myBlock').get_attribute('value')
                value = value.split(":")
                time.sleep(2)
                markers = self.driver.find_elements_by_class_name(Data.dots)
                if len(markers) - 1 == 0:
                    print(
                        "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "No Locators")
                    count = count + 1
                time.sleep(2)
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(4)
                p = pwd()
                self.filename = p.get_download_dir()+'/'+files.teacher_blockwise_download()+name+'_clusterPerBlocks_of_block_' +value[1].strip()+'_'+self.month + "_" + self.year+'_'+cal.get_current_date()+ ".csv"
                print(self.filename)
                if not os.path.isfile(self.filename):
                    print(
                        "District " + select_district.first_selected_option.text + " Block" + select_block.first_selected_option.text + " csv is not downloaded")
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
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text , int(res) , total, "student count mismatched")
                            count = count + 1
                        if int(sc) != schools:
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "school count mismatched")
                            count = count + 1
                    self.remove_csv()

        return count

    def check_school_level_csv_download(self):
        cal = GetData()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        select_block = Select(self.driver.find_element_by_name('myBlock'))
        select_cluster=Select(self.driver.find_element_by_name('myCluster'))
        count = 0
        for x in range(len(select_district.options)-1, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            for y in range(len(select_block.options)-1, len(select_block.options)):
                select_block.select_by_index(y)
                cal.page_loading(self.driver)
                time.sleep(2)
                for z in range(1,len(select_cluster.options)):
                    select_cluster.select_by_index(z)
                    cal.page_loading(self.driver)
                    time.sleep(2)
                    markers = self.driver.find_elements_by_class_name(Data.dots)
                    if len(markers) - 1 == 0:
                        print(
                            "District -" + select_district.first_selected_option.text + " Block " + select_block.first_selected_option.text +
                            " cluster - "+select_cluster.first_selected_option.text +" No Locators")
                        count = count + 1
                    time.sleep(2)
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(5)
                    p = pwd()
                    self.filename = p.get_download_dir() + "/Schools_per_cluster_report_" + self.month + "_" + self.year + ".csv"
                    if not os.path.isfile(self.filename):
                        print(
                            "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "cluster"+select_cluster.first_selected_option.text + "csv is not downloaded")
                        count = count + 1
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            total = 0
                            schools = 0
                            for row in csv.reader(fin):
                                total += int(row[9].replace(',',''))
                            students = self.driver.find_element_by_id("students").text
                            res = re.sub('\D', "", students)

                            school = self.driver.find_element_by_id("schools").text
                            sc = re.sub('\D', "", school)
                            if int(res) != total:
                                print(
                                    "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text , int(res) , total, "student count mismatched")
                                count = count + 1
                            if int(sc) != len(markers)-1:
                                print(
                                    "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "school count mismatched")
                                count = count + 1
                        self.remove_csv()
        return count

    def check_district_block_cluster(self):
        cal = GetData()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        self.year,self.month = cal.get_student_month_and_year_values()
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        select_block = Select(self.driver.find_element_by_name('myBlock'))
        select_cluster = Select(self.driver.find_element_by_name('myCluster'))
        count = 0
        file = file_extention()
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
                    # value = value[4:]+'_'
                    value = value.split(":")
                    markers = self.driver.find_elements_by_class_name(Data.dots)
                    if len(markers) - 1 == 0:
                        print(
                            "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "No data")
                        count = count + 1
                    time.sleep(2)
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(4)
                    p = pwd()
                    self.filename =  p.get_download_dir() + '/'+file.teacher_clusterwise_download()+name+'_schoolPerClusters_of_cluster_'+value[1].strip()+'_'+ self.month + "_" + self.year +"_"+ cal.get_current_date()+".csv"
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print(
                            "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "csv is not downloaded")
                        count = count + 1
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            total = 0
                            for row in csv.reader(fin):
                                row = row[9].strip('\"')
                                row1 = row.replace(',', "")
                                total += int(row1)
                            students = self.driver.find_element_by_id("students").text
                            res = re.sub('\D', "", students)

                            school = self.driver.find_element_by_id("schools").text
                            sc = re.sub('\D', "", school)

                            if int(res) != total:
                                print(
                                    "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "student count mismatched")
                                count = count + 1
                            if int(sc) != len(markers) - 1:
                                print(
                                    "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "school count mismatched")
                                count = count + 1
                        self.remove_csv()

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
            cal.navigate_to_teacher_attendance_report()
            return self.driver.current_url

    def click_on_blocks_click_on_home_icon(self):
        self.driver.find_element_by_id(Data.SAR_Blocks_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)


    #Teacher_Acedemic dropdown

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
            self.filename = p.get_download_dir() +"/" + file.teacher_academic_file()+(academic.options[i].text).strip()+'.csv'
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
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        total_students = self.driver.find_element_by_id(Data.students).text
        students = re.sub("\D", "", total_students)
        self.student_count = students
        no_schools = self.driver.find_element_by_id(Data.schoolcount).text
        schools = re.sub("\D", "", no_schools)
        self.school_count = schools

        self.driver.find_element_by_id(Data.SAR_Blocks_btn).click()
        cal.page_loading(self.driver)
        Bstudents = self.driver.find_element_by_id(Data.students).text
        Bstudent = re.sub("\D", "", Bstudents)

        Bschools = self.driver.find_element_by_id(Data.schoolcount).text
        Bschools = re.sub("\D", "", Bschools)
        print('Blocklevel', self.student_count, Bstudent, self.school_count, Bschools)

        return self.student_count, Bstudent, self.school_count, Bschools


    def cluster_total_no_of_students(self):
        cal = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.SAR_Clusters_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(4)
        Cstudents = self.driver.find_element_by_id(Data.students).text
        Cstudent = re.sub("\D", "", Cstudents)
        Cschools = self.driver.find_element_by_id(Data.schoolcount).text
        Cschool = re.sub("\D", "", Cschools)
        print("Cluster level",self.student_count, Cstudent,self.school_count,Cschool)
        return self.student_count, Cstudent,self.school_count,Cschool


    def schools_total_no_of_students(self):
        global Sstudent, Sschool
        cal = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.SAR_Schools_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(10)
        if 'No data found' in self.driver.page_source:
            print('School level has no data')
        else:
            Sstudents = self.driver.find_element_by_id(Data.students).text
            Sstudent = re.sub("\D", "", Sstudents)

            Sschools = self.driver.find_element_by_id(Data.schoolcount).text
            Sschool = re.sub("\D", "", Sschools)
            print('School level',self.student_count, Sstudent, self.school_count, Sschool)
        return self.student_count, Sstudent, self.school_count, Sschool

    def click_on_logout(self):
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(2)
        self.driver.find_element_by_id(Data.logout).click()
        return self.driver.title

    def block_no_of_schools(self):
        cal = GetData()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        no_schools = self.driver.find_element_by_id(Data.schoolcount).text
        schools = re.sub("\D", "", no_schools)
        self.school_count = schools
        self.driver.find_element_by_id(Data.SAR_Blocks_btn).click()
        cal.page_loading(self.driver)
        Bschools = self.driver.find_element_by_id(Data.schoolcount).text
        Bschools = re.sub("\D", "", Bschools)
        return self.school_count, Bschools

    def cluster_no_of_schools(self):
        self.driver.find_element_by_id(Data.SAR_Clusters_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(15)
        Cschools = self.driver.find_element_by_id(Data.schoolcount).text
        Cschools = re.sub("\D", "", Cschools)
        return self.school_count, Cschools

    def schools_no_of_schools(self):
        try:
            self.driver.find_element_by_id(Data.SAR_Schools_btn).click()
            cal = GetData()
            cal.page_loading(self.driver)
            time.sleep(15)
            Sschools = self.driver.find_element_by_id(Data.schoolcount).text
            Sschools = re.sub("\D", "", Sschools)
            return self.school_count, Sschools
        except NoSuchElementException:
            print("Element Not Found")

    def block_total_no_of_teachers(self):
        cal = GetData()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        total_teachers = self.driver.find_element_by_id(Data.students).text
        teachers = re.sub("\D", "", total_teachers)
        self.teacher_count = teachers
        self.driver.find_element_by_id(Data.SAR_Blocks_btn).click()
        cal.page_loading(self.driver)
        Bteacher = self.driver.find_element_by_id(Data.students).text
        Bteachers = re.sub("\D", "", Bteacher)
        return self.teacher_count, Bteachers

    def cluster_total_no_of_teachers(self):
        self.driver.find_element(By.XPATH,Data.hyper_link).click()
        time.sleep(3)
        total_teachers = self.driver.find_element_by_id(Data.students).text
        teachers = re.sub("\D", "", total_teachers)
        self.teacher_count = teachers

        self.driver.find_element_by_id(Data.SAR_Clusters_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(20)
        Cstudents = self.driver.find_element_by_id(Data.students).text
        Cstudent = re.sub("\D", "", Cstudents)
        return self.teacher_count, Cstudent

    def schools_total_no_of_teacher(self):
        self.driver.find_element(By.XPATH, Data.hyper_link).click()
        time.sleep(3)
        total_teachers = self.driver.find_element_by_id(Data.students).text
        teachers = re.sub("\D", "", total_teachers)
        self.teacher_count = teachers
        self.driver.find_element_by_id(Data.SAR_Schools_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(20)
        Sstudents = self.driver.find_element_by_id(Data.students).text
        Sstudent = re.sub("\D", "", Sstudents)
        return self.teacher_count, Sstudent
