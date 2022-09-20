import csv
import os
import re
import time
from selenium.webdriver.support.select import Select
from Locators.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData

'''Script perform the test the blocks , cluster and school level buttons and dropdowns , map records , 
footer information's '''


class Sat_Map_Report():
    def __init__(self, driver):
        self.fname = None
        self.data = None
        self.semester = None
        self.driver = driver

    def check_semester_landing_page(self):
        return self.driver.current_url

    def click_download_icon_of_schools(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_id(Data.schoolbtn).click()
        cal.page_loading(self.driver)
        time.sleep(10)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(15)
        p = pwd()
        count = 0
        self.filename = p.get_download_dir() + "/" + self.fname.sr_school() + management + '_all_allGrades__allSchools_' + cal.get_current_date() + '.csv'
        if os.path.isfile(self.filename) != True:
            print('School level csv file is not download')
            count = count + 1
        return count

    def check_markers_on_block_map(self):
        self.driver.find_element_by_id(Data.block_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        return dots

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
        cal.page_loading(self.driver)
        time.sleep(5)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        markers = len(dots) - 1
        if markers == 0:
            print("Block level markers are not present ")
            count = count + 1
        else:
            print('*********Block level markers are displayed***********')
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
            # if int(bstd) != int(std):
            #     print('Block level footer mismatch found', int(bstd), int(std))
            #     count = count + 1
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
            # if int(cstd) != int(std):
            #     print('Cluster level footer mismatch found', int(cstd), int(std))
            #     count = count + 1
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
            # if int(sstd) != int(std):
            #     print('School level footer mismatch found', int(sstd), int(std))
            #     count = count + 1
            if int(sattd) != int(attd):
                print('Cluster level footer mismatch found', int(sattd), int(attd))
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
        if 'No data found' in self.driver.page_source:
            print(times.first_selected_option.text, "is not having Data..")
        else:
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
        for i in range(2, len(times.options)):
            times.select_by_index(i)
            timeseries = times.options[i].text
            timeseries = timeseries.replace(' ', '_')
            time.sleep(3)
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
                    self.filename = p.get_download_dir() + "/" + self.fname.sr_districtwise() + management + '_' + timeseries.lower() + '_allGrades__blocks_of_district_' + value.strip() + cal.get_current_date() + '.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print("District " + select_district.first_selected_option.text + " csv is not downloaded")
                        count = count + 1
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            student = 0
                            schools = 0
                            attended = 0
                            for row in csv.reader(fin):
                                # student += int(row[5])
                                schools += int(row[6])
                                attended += int(row[5])
                            print(self.filename, ':', student, schools, attended)

                            # students = self.driver.find_element_by_id("students").text
                            # studs = re.sub('\D', "", students)

                            school = self.driver.find_element_by_id("schools").text
                            sc = re.sub('\D', "", school)

                            attend = self.driver.find_element_by_id("studentsAttended").text
                            atd = re.sub('\D', "", attend)

                            # print('value on footer', student, schools, attended)
                            # print('value on csv file', studs,sc,atd)
                            #
                            # if int(studs) != int(student):
                            #     print(
                            #         "District " + select_district.first_selected_option.text + " student count mismatched",int(studs) , int(student))
                            #     count = count + 1

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
        for i in range(3, len(times.options)):
            times.select_by_index(i)
            timeseries = times.options[i].text
            if 'No data found' in self.driver.page_source:
                print(timeseries, 'is not having Data...')
                return count
            else:
                timeseries = timeseries.replace(' ', '_')
                time.sleep(3)
                select_district = Select(self.driver.find_element_by_id('choose_dist'))
                count = 0
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
                        self.filename = p.get_download_dir() + "/" + self.fname.sr_districtwise() + management + '_' + timeseries.lower() + '_allGrades__blocks_of_district_' + values + '_' + cal.get_current_date() + '.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print("District " + select_district.first_selected_option.text + " csv is not downloaded")
                            count = count + 1
                        else:
                            with open(self.filename) as fin:
                                csv_reader = csv.reader(fin, delimiter=',')
                                header = next(csv_reader)
                                student = 0
                                schools = 0
                                attended = 0
                                for row in csv.reader(fin):
                                    student += int(row[5])
                                    schools += int(row[7])
                                    attended += int(row[6])
                                print(self.filename, ':', student, schools, attended)

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

    def check_markers_on_clusters_map(self):
        self.driver.find_element_by_id(Data.cluster_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        return dots

    def check_markers_on_school_map(self):
        self.driver.find_element_by_id(Data.schoolbtn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(15)
        result = self.driver.find_elements_by_class_name(Data.dots)
        return result

    def click_on_logout(self):
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.logout).click()
        return self.driver.title

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

    def click_download_icon_of_district(self):
        cal = GetData()
        count = 0
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        markers = self.driver.find_elements_by_class_name(Data.dots)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.sr_district() + management + '_all_allGrades__allDistricts_' + cal.get_current_date() + '.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
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

    def click_download_icon_of_blocks(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        year = Select(self.driver.find_element_by_id('year'))
        self.year = year.first_selected_option.text
        semester = self.driver.find_element_by_id('choose_semester').get_attribute('value')
        value = semester.split(":")
        self.semester = value[1].strip()
        self.driver.find_element_by_id(Data.block_btn).click()
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.sr_block() + management + '_' + self.year.strip() + '_' + self.semester + '_allGrades__allBlocks_' + cal.get_current_date() + '.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        if os.path.isfile(self.filename) == True:
            os.remove(self.filename)

    def click_download_icon_of_clusters(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        year = Select(self.driver.find_element_by_id('year'))
        self.year = year.first_selected_option.text
        semester = self.driver.find_element_by_id('choose_semester').get_attribute('value')
        value = semester.split(":")
        self.semester = value[1].strip()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_id(Data.cluster_btn).click()
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(10)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.sr_cluster() + management + '_' + self.year.strip() + '_' + self.semester + '_allGrades__allClusters_' + cal.get_current_date() + '.csv'
        print(self.filename)
        if not os.path.isfile(self.filename):
            return "File Not Downloaded"
        if os.path.isfile(self.filename):
            os.remove(self.filename)

    def click_on_blocks_click_on_home_icon(self):
        self.driver.find_element_by_id(Data.block_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)

    def click_HomeButton(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal = GetData()
        cal.page_loading(self.driver)
        return self.driver.current_url

    def check_grade_dropdown_options(self):
        self.data = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        year = Select(self.driver.find_element_by_id('year'))
        self.year = year.first_selected_option.text
        semester = self.driver.find_element_by_id('choose_semester').get_attribute('value')
        value = semester.split(":")
        self.semester = value[1].strip()
        grade = Select(self.driver.find_element_by_id(Data.Grade))
        counter = len(grade.options)
        for i in range(1, len(grade.options)):
            grade.select_by_index(i)
            print(grade.options[i].text)
            time.sleep(2)
            self.data.page_loading(self.driver)
        return counter

    def click_each_grades(self):
        self.data = GetData()
        count = 0
        p = pwd()
        files = file_extention()
        self.driver.implicitly_wait(100)
        year = Select(self.driver.find_element_by_id('year'))
        self.year = year.first_selected_option.text
        semester = self.driver.find_element_by_id('choose_semester').get_attribute('value')
        value = semester.split(":")
        self.semester = value[1].strip()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        grade = Select(self.driver.find_element_by_id(Data.Grade))
        for i in range(1, len(grade.options)):
            grade.select_by_index(i)
            time.sleep(3)
            gradename = (grade.options[i].text).strip()
            gradenum = re.sub('\D', '', gradename)
            self.data.page_loading(self.driver)
            dots = self.driver.find_elements_by_class_name(Data.dots)
            markers = len(dots) - 1
            self.data.page_loading(self.driver)
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(4)
            self.filename = p.get_download_dir() + '/' + files.sr_gradewise() + management + "_" + self.year.strip() + "_" + self.semester + "_Grade " + gradenum.strip() + '__allDistricts_' + self.data.get_current_date() + '.csv'
            print(self.filename)
            time.sleep(1)
            if os.path.isfile(self.filename) != True:
                print('Grade ' + gradenum.strip() + 'wise csv file is not downloaded')
                count = count + 1
            else:
                file = open(self.filename)
                read = file.read()
                if grade.options[i].text in read:
                    print(grade.options[i].text, "is present")
                self.data.page_loading(self.driver)
                os.remove(self.filename)
        return count

    def select_subjects_dropdown(self):
        self.data = GetData()
        p = pwd()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        year = Select(self.driver.find_element_by_id('year'))
        self.year = year.first_selected_option.text
        semester = self.driver.find_element_by_id('choose_semester').get_attribute('value')
        value = semester.split(":")
        self.semester = value[1].strip()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        grade = Select(self.driver.find_element_by_id(Data.Grade))
        subjects = Select(self.driver.find_element_by_id(Data.Subject))
        subcount = len(subjects.options) - 1
        files = file_extention()
        for i in range(1, len(grade.options) - 1):
            grade.select_by_index(i)
            time.sleep(2)
            print(grade.options[i].text)
            self.data.page_loading(self.driver)
            gradename = (grade.options[i].text).strip()
            gradenum = re.sub('\D', '', gradename)
            for j in range(1, len(subjects.options) - 1):
                time.sleep(1)
                subjects.select_by_index(j)
                time.sleep(2)
                print(subjects.options[j].text)
                if 'No data found' in self.driver.page_source:
                    print(grade.options[i].text + ', ' + subjects.options[j].text + " is not having data")
                    return count
                else:
                    self.data.page_loading(self.driver)
                    sub = (subjects.options[j].text).strip()
                    time.sleep(3)
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(3)
                    self.filename = p.get_download_dir() + '/' + files.sr_gradewise() + management + "_" + self.year.strip() + "_" + self.semester + "_Grade " + gradenum.strip() + '_' + sub + '_allDistricts_' + self.data.get_current_date() + '.csv'
                    print(self.filename)
                    if os.path.isfile(self.filename) != True:
                        print(files.sr_gradewise() + gradenum.strip(), ' wise csv file is not downloaded')
                        count = count + 1

                    os.remove(self.filename)
                    self.data.page_loading(self.driver)
                return count

    def remove_csv(self):
        os.remove(self.filename)

    def check_district(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        year = Select(self.driver.find_element_by_id('year'))
        self.year = year.first_selected_option.text
        semester = self.driver.find_element_by_id('choose_semester').get_attribute('value')
        value = semester.split(":")
        self.semester = value[1].strip()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        count = 0
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            value = self.driver.find_element_by_id('choose_dist').get_attribute('value')
            value = value.split(":")
            val = value[1].strip()
            markers = self.driver.find_elements_by_class_name(Data.dots)
            time.sleep(3)
            if (len(markers) - 1) == 0:
                print("District" + select_district.first_selected_option.text + "no data")
                count = count + 1
            else:
                time.sleep(2)
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(3)
                p = pwd()
                self.filename = p.get_download_dir() + "/" + self.fname.sr_districtwise() + management + '_' + self.year.strip() + '_' + self.semester + '_allGrades__blocks_of_district_' + val + '_' + cal.get_current_date() + '.csv'
                print(self.filename)
                if not os.path.isfile(self.filename):
                    print("District " + select_district.first_selected_option.text + " csv is not downloaded")
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
                    self.remove_csv()

        return count

    def check_districts_block(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        year = Select(self.driver.find_element_by_id('year'))
        self.year = year.first_selected_option.text
        semester = self.driver.find_element_by_id('choose_semester').get_attribute('value')
        value = semester.split(":")
        self.semester = value[1].strip()
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
                value = value.split(":")
                markers = self.driver.find_elements_by_class_name(Data.dots)
                if len(markers) - 1 == 0:
                    print(
                        "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "No Data")
                    count = count + 1
                else:
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(2)
                    p = pwd()
                    self.filename = p.get_download_dir() + "/" + self.fname.sr_blockwise() + management + '_' + self.year.strip() + '_' + self.semester + '_allGrades__clusters_of_block_' + \
                                    value[1].strip() + '_' + cal.get_current_date() + '.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print(
                            "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "csv is not downloaded")
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
                        self.remove_csv()

                return count

    def check_last30days_districts_block(self):
        cal = GetData()
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
                value = value.split(":")
                values = value[1].strip()
                markers = self.driver.find_elements_by_class_name(Data.dots)
                if len(markers) - 1 == 0:
                    print(
                        "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "No Data")
                    count = count + 1
                else:
                    time.sleep(2)
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(2)
                    p = pwd()
                    self.filename = p.get_download_dir() + "/" + self.fname.sr_blockwise() + management + '_' + timeseries + '_allGrades__clusters_of_block_' + values + '_' + cal.get_current_date() + '.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print(
                            "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "csv is not downloaded")
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
                        self.remove_csv()

                return count

    def check_last7days_districts_block(self):
        cal = GetData()
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
        count = 0
        if 'No data found' in self.driver.page_source:
            print(timeseries, 'is not having Data..')
            return count
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
                            "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "No Data")
                        count = count + 1
                    else:
                        time.sleep(2)
                        self.driver.find_element_by_id(Data.Download).click()
                        time.sleep(4)
                        p = pwd()
                        self.filename = p.get_download_dir() + "/" + self.fname.sr_blockwise() + management + "_" + timeseries + '_allGrades__clusters_of_block_' + values + "_" + cal.get_current_date() + '.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(
                                "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "csv is not downloaded")
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
                            self.remove_csv()
                    return count

    def check_district_block_cluster(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        year = Select(self.driver.find_element_by_id('year'))
        self.year = year.first_selected_option.text
        semester = self.driver.find_element_by_id('choose_semester').get_attribute('value')
        value = semester.split(":")
        self.semester = value[1].strip()
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        select_block = Select(self.driver.find_element_by_id('choose_block'))
        select_cluster = Select(self.driver.find_element_by_id('choose_cluster'))
        count = 0
        for x in range(len(select_district.options) - 1, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            for y in range(len(select_block.options) - 1, len(select_block.options)):
                select_block.select_by_index(y)
                cal.page_loading(self.driver)
                for z in range(1, len(select_cluster.options)):
                    select_cluster.select_by_index(z)
                    time.sleep(3)
                    cal.page_loading(self.driver)
                    value = self.driver.find_element_by_id('choose_cluster').get_attribute('value')
                    value = value[3:]
                    markers = self.driver.find_elements_by_class_name(Data.dots)
                    if len(markers) - 1 == 0:
                        print(
                            "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "No data")
                        count = count + 1
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(4)
                    p = pwd()
                    self.filename = p.get_download_dir() + "/" + self.fname.sr_clusterwise() + management + '_' + self.year.strip() + '_' + self.semester + '_allGrades__schools_of_cluster_' + value.strip() + '_' + cal.get_current_date() + '.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print(
                            "District " + select_district.first_selected_option.text + " Block: " + select_block.first_selected_option.text + " Cluster: " + select_cluster.first_selected_option.text + "csv is not downloaded")
                        count = count + 1
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            next(csv_reader)
                            data = list(csv_reader)
                            row_count = len(data)
                            dots = len(markers) - 1
                            if dots != row_count:
                                print('Markers records and csv file records are not matching ', dots, row_count)
                                count = count + 1
                        self.remove_csv()
                return count

    def check_last30_district_block_cluster(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(2)
        time.sleep(3)
        if 'No Data found' in self.driver.page_source:
            print(period.first_selected_option.text, ' is not having data')
        else:
            timeseries = period.first_selected_option.text
            timeseries = timeseries.lower().replace(" ", '_')
            select_district = Select(self.driver.find_element_by_id('choose_dist'))
            select_block = Select(self.driver.find_element_by_id('choose_block'))
            select_cluster = Select(self.driver.find_element_by_id('choose_cluster'))
            count = 0
            for x in range(len(select_district.options) - 1, len(select_district.options)):
                select_district.select_by_index(x)
                cal.page_loading(self.driver)
                for y in range(len(select_block.options) - 1, len(select_block.options)):
                    select_block.select_by_index(y)
                    cal.page_loading(self.driver)
                    for z in range(1, len(select_cluster.options)):
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
                        self.filename = p.get_download_dir() + "/" + self.fname.sr_clusterwise() + management + '_' + timeseries + '_allGrades__schools_of_cluster_' + values + cal.get_current_date() + '.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "csv is not downloaded")
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
                            self.remove_csv()

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
        if 'No Data found' in self.driver.page_source:
            print(period.first_selected_option.text, ' is not having data')
            return count
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
                    for z in range(2, len(select_cluster.options)):
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
                        self.filename = p.get_download_dir() + "/" + self.fname.sr_clusterwise() + management + '_' + timeseries + '_allGrades__schools_of_cluster_' + values + cal.get_current_date() + '.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "csv is not downloaded")
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
                            self.remove_csv()

                    return count
