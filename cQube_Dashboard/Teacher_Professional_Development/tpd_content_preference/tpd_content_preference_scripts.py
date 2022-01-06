import csv
import os
import re
import time

import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Locators.parameters import Data
from files import Files
from get_dir import pwd
from reuse_func import GetData


class tpd_content_usage_piechart():

    def __init__(self,driver):
        self.driver = driver
        self.data = GetData()
        self.p = pwd()
        self.fname = Files()
    def check_navigation_to_content_usage_report(self):
        count = 0
        self.data.click_on_state(self.driver)
        self.driver.find_element(By.ID,Data.cQube_logo).click()
        time.sleep(1)
        self.data.navigate_to_tpd_content_usage_piechart_report()
        if 'content-usage-pie-chart' not in self.driver.current_url:
            print('Content Usage Pie Chart Report is not displayed')
            count = count + 1
        else:
             print("Content Usage Pie Chart Report is displayed")
        return count

    def check_hyperlink_functionality(self):
        count = 0
        self.driver.find_element(By.XPATH,Data.hyper_link).click()
        time.sleep(3)
        districts = Select(self.driver.find_element(By.ID,Data.dist_dropdown))
        districts.select_by_index(2)
        print(districts.options[2].text,'is selected')
        time.sleep(1)
        self.driver.find_element(By.XPATH,Data.hyper_link).click()
        if districts.first_selected_option.text == districts.options[2].text:
            print("Hyperlink is not working ")
            count = count + 1
        else:
             print("Hyper link is working as expected ")
        return count

    def check_dropdown_options(self):
        self.data.click_on_state(self.driver)
        districts = Select(self.driver.find_element(By.ID, Data.dist_dropdown))
        options = len(districts.options) - 1
        return options

    def check_selection_of_options(self):
        self.driver.find_element(By.XPATH,Data.hyper_link).click()
        time.sleep(3)
        district = Select(self.driver.find_element(By.ID, Data.dist_dropdown))
        spents = len(district.options) - 1
        for i in range(1,spents):
            district.select_by_index(i)
            time.sleep(2)
            print(district.options[i].text,'is selected and chart also displayed...')
        return spents

    def check_piechart_in_screen(self):
        self.data.click_on_state(self.driver)
        self.driver.execute_script("document.getElementsByClassName('comment-user')[0].click()")

    def check_logout_to_report(self):
        count = 0
        self.data.click_on_state(self.driver)
        self.driver.find_element(By.ID,Data.cQube_logo).click()
        time.sleep(1)
        self.driver.find_element(By.ID,Data.logout).click()
        time.sleep(3)
        if 'cQube' not in self.driver.page_source:
            print("Logout button is not working ")
            count = count + 1
        else:
             print("Logout button is working as expected ")
             self.data.login_cqube(self.driver)
             self.data.navigate_to_tpd_content_usage_piechart_report()
             if 'content-usage-pie-chart' in self.driver.current_url:
                 print(" content-usage-pie-chart  report home page is displayed ")
             else:
                 print("Navigation to content-usage-pie-chart Report is failed !")
                 count = count + 1
        return count



    def check_download_statewise_with_contentplays(self):
        count = 0
        self.driver.find_element(By.XPATH, Data.hyper_link).click()
        time.sleep(3)
        self.driver.refresh()
        self.data.page_loading(self.driver)
        print('hyperlink click is happened')
        if 'No data found' in self.driver.page_source:
            print("Content Preference Report showing no data found ")
        else:

            self.driver.find_element(By.ID, Data.Download).click()
            time.sleep(3)
            print('Downlaod click is happened')
            self.filename = self.p.get_download_dir() + '/'+self.fname.content_preference_state
            print(os.path.isfile(self.filename), 'file is present or not ')
            if os.path.isfile(self.filename) != True:
                print(self.fname.content_preference_state, 'is not downloaded: ',self.filename)
                count = count + 1
            else:
                print(os.path.isfile(self.filename),'file is present or not ')
                df = pd.read_csv(self.filename)
                size = len(df)
                content_plays = df['Total Content Plays Gujarat'].sum()

                total_cp = self.driver.find_element(By.TAG_NAME, Data.state_cp_header).text
                total_cp = re.sub('\D', "", total_cp)


                if int(total_cp) != int(content_plays):
                    print("Total content plays is not matching with header information", total_cp, content_plays)
                    count = count + 1
                else:
                    print(total_cp, content_plays, 'are matching with header information')
                os.remove(self.filename)
        return count

    def check_download_state_with_districts_content_plays(self):
        count = 0
        self.p = pwd()
        self.fname = Files()
        self.driver.find_element(By.XPATH,Data.hyper_link).click()
        time.sleep(3)
        if 'No data found' in self.driver.page_source:
            print("Content Preference Report showing no data found ")
        else:
            dropdown = Select(self.driver.find_element(By.ID,Data.state_district))
            dropdown.select_by_index(2)
            print(dropdown.options[2].text,'is selected')
            time.sleep(5)
            self.driver.find_element(By.ID, Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + '/' + self.fname.content_preference_state
            if os.path.isfile(self.filename) != True:
                print(self.fname.content_preference_state, 'is not downloaded ')
                count = count + 1
            else:
                df = pd.read_csv(self.filename)
                size = len(df)
                content_plays = df['Total Content Plays Gujarat'].sum()

                total_cp = self.driver.find_element(By.TAG_NAME, Data.state_cp_header).text

                total_cp = re.sub('\D', "", total_cp)
                os.remove(self.filename)
                if int(total_cp) != int(content_plays):
                    print("Total content plays is not matching with header information", total_cp, content_plays)
                    count = count + 1
                else:
                    print(total_cp, content_plays, 'are matching with header information')
        return count

    def check_download_state_with_random_district_content_plays(self):
        count = 0
        self.p = pwd()
        self.fname = Files()
        # self.data.click_on_state(self.driver)
        self.driver.find_element(By.XPATH,Data.hyper_link).click()
        time.sleep(3)
        if 'No data found' in self.driver.page_source:
            print("Content Preference Report showing no data found ")
        else:
            dropdown = Select(self.driver.find_element(By.ID,Data.state_district))
            dropdown.select_by_index(2)
            time.sleep(5)
            selection = Select(self.driver.find_element(By.ID,Data.multi_selection))
            print(selection.is_multiple)
            time.sleep(2)
            selection.select_by_index(4)
            time.sleep(2)
            self.driver.find_element(By.ID,Data.multi_submit).click()
            time.sleep(5)
            validation_selection = self.driver.find_element(By.XPATH,"//*[@id='multiSelector']/span").text
            selected =re.sub('\D', "", validation_selection)
            if int(selected) != 2:
                print('Multi selection is not working')
                count = count + 1
            else:
                self.driver.find_element(By.ID, Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + self.fname.content_preference_state
                if os.path.isfile(self.filename) != False:
                    print(self.fname.tpd_content_plays_file, 'is not downloaded ')
                    count = count + 1
                else:
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        select1 = 0
                        select2 = 0
                        for row in csv.reader(fin):
                            select1 += int(row[3])
                            select2 += int(row[4])
                    os.remove(self.filename)
                    if select1 not in self.driver.page_source:
                        print("Total content plays is not matching with header information", select1)
                        count = count + 1
                    else:
                        print( select1, 'are matching with header information')

                    if  select2 not in self.driver.page_source:
                        print("Total content plays is not matching with header information", select2)
                        count = count + 1
                    else:
                        print(select2, 'are matching with header information')

        return count

