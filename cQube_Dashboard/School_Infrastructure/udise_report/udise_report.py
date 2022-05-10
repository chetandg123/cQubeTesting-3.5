
import csv
import os
import re
import time
import pandas as pd
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Locators.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData

'''Script perform the test the blocks , cluster and school level buttons and dropdowns , map records , 
footer information's '''

class UdiseReport():
    def __init__(self,driver):
        self.driver = driver

    def test_link(self):
        self.p = GetData()
        count = 0
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.scm_block).click()
        time.sleep(5)
        markers = self.driver.find_elements(By.CLASS_NAME,Data.dots)
        count1 = len(markers)-1
        self.driver.find_element(By.XPATH,"//p/span").click()
        time.sleep(3)
        marker = self.driver.find_elements(By.CLASS_NAME, Data.dots)
        count2 = len(marker)-1
        if count1!=count2:
            print("Hyperlink is working as expected...",count1,count2)
        else:
            print("Hyperlink is not working ",count1,count2)
            count = count + 1
            self.p.page_loading(self.driver)
        return count


    def test_districtwise(self):
        self.p = GetData()
        cal = pwd()
        self.fname =file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        time.sleep(3)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        self.filename = cal.get_download_dir() + '/' +'UDISE_report_'+management+'_Infrastructure_Score_allDistricts_'+self.p.get_current_date()+'.csv'
        self.p.page_loading(self.driver)
        print(self.filename)
        file = os.path.isfile(self.filename)
        if True == file:
            print('Udise districtwise csv file is downloaded')
        else:
            print('Districtwise csv file is not downloaded ')
            count = count + 1
        self.p.page_loading(self.driver)
        os.remove(self.filename)
        return count

    def check_download_csv1(self):
        p = pwd()
        self.cal = GetData()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.cal.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        select_block = Select(self.driver.find_element_by_id('choose_block'))
        select_cluster = Select(self.driver.find_element_by_id('choose_cluster'))
        count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.fname = file_extention()
        for x in range( int(len(select_district.options))-1, int(len(select_district.options))):
            select_district.select_by_index(x)
            self.cal.page_loading(self.driver)
            for y in range(len(select_block.options)-1,len(select_block.options)):
                select_block.select_by_index(y)
                self.cal.page_loading(self.driver)
                time.sleep(2)
                for z in range(1,len(select_cluster.options)):
                    select_cluster.select_by_index(z)
                    self.cal.page_loading(self.driver)
                    time.sleep(2)
                    value = self.driver.find_element_by_id('choose_cluster').get_attribute('value')
                    # values = value[3:]+'_'
                    value = value.split(":")
                    nodata = self.driver.find_element_by_id("errMsg").text
                    markers = self.driver.find_elements_by_class_name(Data.dots)
                    if len(markers)-1 == 0:
                            print(select_cluster.options[z].text,"does not contains markers on map")
                    else:
                        self.driver.find_element_by_id(Data.Download).click()
                        time.sleep(3)
                        self.filename = p.get_download_dir() + "/" +"UDISE_report_"+management+"_Infrastructure_Score_schools_of_cluster_"+value[1].strip()+'_'+self.cal.get_current_date()+'.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(select_district.options[x].text,select_block.options[y].text,select_cluster.options[z].text ,"csv file is not downloaded!")
                            count = count + 1
                        schools = self.driver.find_element_by_id('footer').text
                        sc = re.sub('\D','',schools)
                        if len(markers)-1 != int(sc):
                            print('Total no of school mis match found with no of markers ',len(markers),sc)
                            count = count + 1
                        os.remove(self.filename)
        return count

    def test_check_total_schoolvalue(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        try:
            school = self.driver.find_element_by_id(Data.sc_no_of_schools).text
            res = re.sub('\D', "", school)
            self.p.page_loading(self.driver)

            self.driver.find_element_by_id(Data.scm_block).click()
            self.p.page_loading(self.driver)
            bschool = self.driver.find_element_by_id(Data.sc_no_of_schools).text
            bres = re.sub('\D',"",bschool)
            self.p.page_loading(self.driver)

            self.driver.find_element_by_id(Data.scm_cluster).click()
            self.p.page_loading(self.driver)
            time.sleep(10)
            cschool = self.driver.find_element_by_id(Data.sc_no_of_schools).text
            cres = re.sub('\D', "", cschool)
            self.p.page_loading(self.driver)

            self.driver.find_element_by_id(Data.scm_school).click()
            time.sleep(15)
            sschool = self.driver.find_element_by_id(Data.sc_no_of_schools).text
            sres = re.sub('\D', "", sschool)
            self.p.page_loading(self.driver)

            return res ,bres ,cres,sres
        except exceptions.ElementClickInterceptedException :
            print("no of schools are same ")
            self.p.page_loading(self.driver)

    def test_download_blockwise(self):
        self.p = GetData()
        cal = pwd()
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_id(Data.scm_block).click()
        self.p.page_loading(self.driver)
        time.sleep(10)
        markers = self.driver.find_elements_by_class_name(Data.dots)
        self.p.page_loading(self.driver)
        dots = len(markers)-1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(4)
        self.filename = cal.get_download_dir() + '/' +'UDISE_report_'+management+'_Infrastructure_Score_allBlocks_'+self.p.get_current_date()+'.csv'
        self.p.page_loading(self.driver)
        file = os.path.isfile(self.filename)
        os.remove(self.filename)
        return file ,dots

    def test_clusterbtn(self):
        self.p = GetData()
        cal = pwd()
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_id(Data.scm_cluster).click()
        self.p.page_loading(self.driver)
        time.sleep(10)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        count = len(dots)-1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        self.filename = cal.get_download_dir() + '/' +'UDISE_report_'+management+'_Infrastructure_Score_allClusters_'+self.p.get_current_date()+'.csv'
        self.p.page_loading(self.driver)
        file = os.path.isfile(self.filename)
        self.p.page_loading(self.driver)
        os.remove(self.filename)
        return count, file

    def test_click_on_school_btn(self):
        self.p = GetData()
        cal = pwd()
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_id(Data.scm_school).click()
        self.p.page_loading(self.driver)
        time.sleep(10)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        count = len(dots)-1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(20)
        self.filename = cal.get_download_dir() + '/' +'UDISE_report_'+management+'_Infrastructure_Score_allSchools_'+self.p.get_current_date() +'.csv'
        self.p.page_loading(self.driver)
        file = os.path.isfile(self.filename)
        self.p.page_loading(self.driver)
        os.remove(self.filename)
        return count, file

    def test_click_blocks(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.scm_block).click()
        count = 0
        self.p.page_loading(self.driver)
        time.sleep(10)
        scores = Select(self.driver.find_element_by_id("choose_infra"))
        for i in range(1,len(scores.options)-12):
            time.sleep(2)
            scores.select_by_index(i)
            time.sleep(5)
            self.p.page_loading(self.driver)
            markers = self.driver.find_elements_by_class_name(Data.dots)
            dots = len(markers)-1
            if dots == 0:
                # print(scores.options[i].text , 'does not contains markers on map ')
                count = count + 1
        self.p.page_loading(self.driver)
        scores.select_by_index(1)
        time.sleep(2)
        return count

    def test_click_clusters(self):
        self.driver.implicitly_wait(30)
        self.p = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.scm_cluster).click()
        self.p.page_loading(self.driver)
        time.sleep(5)
        scores = Select(self.driver.find_element_by_id("choose_infra"))
        for i in range(len(scores.options)-12):
            time.sleep(2)
            scores.select_by_index(i)
            # infra_option = scores.options[i].text
            time.sleep(4)
            self.p.page_loading(self.driver)
            markers = self.driver.find_elements_by_class_name(Data.dots)
            dots = len(markers) - 1
            if dots == 0:
                print('does not contains markers on map ')
                count = count + 1
        self.p.page_loading(self.driver)
        return count

    #indices downloading functionality
    def infrastructure_score(self):
        self.cal = GetData()
        self.fname = file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_css_selector('p >span').click()
        self.cal.page_loading(self.driver)
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(1)
        self.cal.page_loading(self.driver)
        row_count = 0
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[1].text,'is not having data')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Infrastructure_Score_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            print(self.filename)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("infrastructure_score  is selected and csv file is downloaded")
            return row_count-1


    def administation(self):
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(2)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[2].text,'is not having data')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Administration_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            row_count = 0
            if True != file:
                print('csv file not downloaded')
            else:

                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("Administration is selected and csv file is downloaded")
            return row_count - 1

    def artslab(self):
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(3)
        row_count = 0
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[3].text,'is not having data')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Arts_Lab_Index_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("artslab  is selected and csv file is downloaded")
            return row_count - 1

    def community(self):
        row_count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(3)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(4)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[4].text,'is not having data')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Community_Participation_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:

                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("Community  is selected and csv file is downloaded")
            return row_count - 1

    def Enrollment(self):
        row_count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(5)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[5].text,'is not having data')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Enrollment_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("Enrollment  is selected and csv file is downloaded")
            return row_count - 1

    def grant_expenditure(self):
        row_count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(6)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[6].text,'is not having data')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Grant_Expenditure_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("Grant expenditure is selected and csv file is downloaded")
            return row_count - 1

    def ictlab(self):
        row_count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(7)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[7].text,'is not having data')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_ICT_Lab_Index_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("ICTlab  is selected and csv file is downloaded")
            return row_count - 1

    def Medical(self):
        row_count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(8)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[8].text,'is not having data')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Medical_Index_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("Medical is selected and csv file is downloaded")
            return row_count - 1

    def nsqf(self):
        row_count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(9)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[9].text,'is not having data')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_NSQF_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("nsqf is selected and csv file is downloaded")
            return row_count - 1

    def policy(self):
        row_count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(10)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[10].text,'is not having data')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Policy_Implementation_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("Policy is selected and csv file is downloaded")
            return row_count - 1

    def Safety(self):
        row_count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(11)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[11].text,'is not having data')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Safety_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("Safety  is selected and csv file is downloaded")
            return row_count - 1

    def School_infrastructure(self):
        row_count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(12)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[12].text,'is not having data')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_School_Infrastructure_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("School infrastructure is selected and csv file is downloaded")
            return row_count - 1

    def School_inspection(self):
        row_count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(13)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[13].text,'is not having data')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_School_Inspection_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("school inspection  is selected and csv file is downloaded")
            return row_count - 1

    def School_perfomance(self):
        row_count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(14)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[14].text,'is not having data')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_School_Performance_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:

                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("School performance is selected and csv file is downloaded")
            return row_count - 1

    def Science_lab(self):
        row_count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(15)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[15].text,'is not having data')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Science_Lab_Index_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("Science lab is selected and csv file is downloaded")
            return row_count - 1

    def Teacher_profile(self):
        row_count = 0
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(16)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            print(chooseinfra.options[16].text,'is not having data')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Teacher_Profile_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                print("Teachers profile is selected and csv file is downloaded")
            chooseinfra.select_by_index(1)
            time.sleep(2)
        return row_count - 1

    def remove_csv(self):
        os.remove(self.filename)

    def test_download(self):
        self.p = GetData()
        cal = pwd()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        managmemnt =self.driver.find_element_by_id('name').text
        manage = managmemnt[16:]+''
        self.driver.find_element_by_id(Data.scm_cluster).click()
        self.p.page_loading(self.driver)
        time.sleep(5)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        count =len(dots)-1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        self.file = file_extention()
        self.filename = cal.get_download_dir() + '/' + self.file.udise_cluster()+(manage.lower()).strip()+'_Infrastructure_Score_allClusters_'+self.p.get_current_date()+'.csv'
        self.p.page_loading(self.driver)
        file = os.path.isfile(self.filename)
        os.remove(self.filename)
        return file,count

    def check_logout(self):
        self.driver.find_element_by_id(Data.menu_icon).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.logout).click()
        time.sleep(3)
        return self.driver.title

    def test_districtwise_schools_count(self):
        p = pwd()
        count = 0
        self.cal = GetData()
        self.driver.implicitly_wait(30)
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            self.cal.page_loading(self.driver)
            markers = self.driver.find_elements_by_class_name(Data.dots)
            if len(markers)-1 == 0:
                print(select_district.options[x].text,"has no data on map")
            else:
                count = 0
                schools = self.driver.find_element_by_id(Data.schoolcount).text
                sc = re.sub('\D', "", schools)
                if int(sc) == 0:
                    print(select_district.options[x],'has no no of school count')
                    count = count + 1
                time.sleep(2)

        return count
    def test_mousehover(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        markers = self.driver.find_elements_by_class_name(Data.dots)
        count = len(markers)-1
        print("Mousehover on each markers..")
        self.p.test_mouse_over()
        self.p.page_loading(self.driver)
        return count
    def test_click_schools(self):
        self.p = GetData()
        count =0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id('school').click()
        time.sleep(15)
        scores = Select(self.driver.find_element_by_id("choose_infra"))
        for i in range(1,len(scores.options)):
            # scores.select_by_index(i)
            print(scores.options[i].text,"is selected as indices")
            markers = self.driver.find_elements_by_class_name(Data.dots)
            dots = len(markers) - 1
            if dots == 0:
                print(scores.options[i].text, 'does not contains markers on map ')
                count = count + 1
        self.p.page_loading(self.driver)
        return count
    def test_district(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id('block').click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.homeicon).click()
        print("home icon is working ")
        self.p.page_loading(self.driver)
    def test_schools(self):
        p = pwd()
        self.cal = GetData()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.cal.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        select_block = Select(self.driver.find_element_by_id('choose_block'))
        count = 0
        for x in range(2, len(select_district.options)):
            select_district.select_by_index(x)
            # print(select_district.options[x].text)
            self.cal.page_loading(self.driver)
            for y in range(1,len(select_block.options)):
                select_block.select_by_index(y)
                self.cal.page_loading(self.driver)
                nodata = self.driver.find_element_by_id("errMsg").text
                if nodata == "No data found":
                    print(select_district.options[x].text, "no data found!")
                    count = count + 1
                else:
                    markers = self.driver.find_elements_by_class_name(Data.dots)
                    if len(markers)-1 != 0:
                        self.driver.find_element_by_id(Data.Download).click()
                        time.sleep(4)
                        self.filename = p.get_download_dir() + "/Cluster_per_block_report.csv"
                        if not os.path.isfile(self.filename):
                            print(select_block.options[y].text,"csv is not dowloaded")
                            count = count + 1
                        # else:
                        #     with open(self.filename) as fin:
                        #         csv_reader = csv.reader(fin, delimiter=',')
                        #         header = list(csv_reader)
                        #         data = len(header)
                        #         # total = 0
                        #         # schools = 0
                        #         # for row in csv.reader(fin):
                        #         #     schools += int(row[2])
                        #         school = self.driver.find_element_by_id("schools").text
                        #         sc= re.sub('\D', "", school)
                        #         if int(sc) != header:
                        #             print(select_block.options[y].text,"schools:",header ,int(sc) ,"mismatch found" )
                        #         time.sleep(2)
                            os.remove(self.filename)
            return count

    def test_each_districtwise(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        managment_name = self.driver.find_element_by_id('name').text
        name = managment_name[16:].strip().lower()
        time.sleep(2)
        Districts = Select(self.driver.find_element_by_id('choose_dist'))
        self.p.page_loading(self.driver)
        count = 0
        for i in range(1,len(Districts.options)-10):
            Districts.select_by_index(i)
            self.p.page_loading(self.driver)
            value = self.driver.find_element_by_id('choose_dist').get_attribute('value')
            value = value.split(":")
            dist_name = Districts.options[i].text
            markers = self.driver.find_elements_by_class_name(Data.dots)
            marker_value = len(markers)-1
            self.p.page_loading(self.driver)
            if marker_value == 0 or 'no data found' in self.driver.page_source:
                print(Districts.options[i].text , " does not have markers on map")
                count = count + 1
            else:
                cal = pwd()
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(2)
                self.filename = cal.get_download_dir() + '/' +"UDISE_report_"+name +"_Infrastructure_Score_blocks_of_district_"+value[1].strip()+'_'+self.p.get_current_date()+'.csv'
                print(self.filename)
                self.p.page_loading(self.driver)
                if not os.path.isfile(self.filename):
                    print(dist_name," csv is not downloaded")
                    count = count + 1
                # else:
                #     df = pd.read_csv(self.filename)
                #     schools = df['']
                #     school = self.driver.find_element_by_id("schools").text
                #     sc = re.sub('\D', "", school)
                #     if int(sc) != int(schools):
                #         print("school count mismatched")
                #         count = count + 1
                os.remove(self.filename)

        return count

    def test_map(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        self.p.page_loading(self.driver)
        count = len(dots)-1
        return count
    def test_dashboard(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        time.sleep(2)
        self.driver.find_element_by_id(Data.sch_infra).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.udise_report).click()
        self.p.page_loading(self.driver)
        count = 0
        if 'udise-report' in self.driver.current_url:
            print('UDISE map report is displayed')
        else:
            print('UDISE map report is not displayed')
            count = count + 1
        return count

