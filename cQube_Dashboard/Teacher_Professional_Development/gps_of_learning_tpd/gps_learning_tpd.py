import os
import re
import time

import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Locators.parameters import Data
from filenames import file_extention
from files import Files
from get_dir import pwd
from reuse_func import GetData


class tpd_content_plays_map_report():
    def __init__(self,driver):
        self.driver = driver
        self.count = 0
        self.data = GetData()

    def check_navigation_from_dashboard(self):
        data = GetData()
        self.driver.find_element(By.XPATH,Data.hyper_link).click()
        data.page_loading(self.driver)
        self.driver.find_element(By.ID,Data.cQube_logo).click()
        data.navigate_to_gps_of_learning_tpd()
        if 'tpd-total-content-plays' in self.driver.current_url:
            print("GPS of Learning- TPD Report is displayed")
        else:
            print('GPS of Learning- TPD Report is not displayed')
            self.count = self.count + 1
        return self.count

    def check_report_home_page(self):
        count = 0
        self.data.click_on_state(self.driver)
        self.driver.find_element(By.ID,Data.cQube_logo).click()
        time.sleep(1)
        self.data.navigate_to_gps_of_learning_tpd()
        if 'No data found' in self.driver.page_source:
            print("GPS of Learning- TPD Report is showing no data found!!!")
            count = count + 1
        markers = self.driver.find_elements(By.CLASS_NAME,Data.dots)
        values = len(markers)-1
        return count , values

    def check_choose_type_dropdown(self):
        self.data.click_on_state(self.driver)
        timespent = Select(self.driver.find_element(By.ID,Data.time_spent_Dropdown))
        options = len(timespent.options)-1
        return options

    def check_selection_of_options(self):
        self.data.click_on_state(self.driver)
        timespent = Select(self.driver.find_element(By.ID, Data.time_spent_Dropdown))
        spents = len(timespent.options) - 1
        for i in range(1,spents):
            timespent.select_by_index(i)
            time.sleep(2)
            print(timespent.options[i].text,'is selected and displayed on markers...')

    def check_hyperlink_functionality(self):
        count = 0
        self.data.click_on_state(self.driver)
        timespent = Select(self.driver.find_element(By.ID, Data.time_spent_Dropdown))
        timespent.select_by_index(3)
        time.sleep(2)
        self.driver.find_element(By.XPATH,Data.hyper_link).click()
        time.sleep(3)
        if timespent.options[2].text in self.driver.page_source:
            print("Hyper link is not working...")
            count = count + 1
        else:
             print("Hyper link text is refreshed to home page..")
        return count

    def check_legend_card_functionality(self):
        count = 0
        self.data.click_on_state(self.driver)
        markers = self.driver.find_elements(By.CLASS_NAME,Data.dots)
        legends = self.driver.find_elements(By.CLASS_NAME,Data.legends)
        for i in range(len(legends)-1):
            cards = self.driver.find_element(By.ID,i)
            cards.click()
            time.sleep(2)
            if len(markers)-1 == 0 or 'No data found' in self.driver.page_source:
                print(legends.text,"selected legend card does not having markers and showing no data found")
                count = count + 1
            else:
                print("Legend cards are working as expected ")
        return count

    def check_total_content_plays_legendcard(self):
        count = 0
        sum = 0
        self.data.click_on_state(self.driver)
        timespent = Select(self.driver.find_element(By.ID, Data.time_spent_Dropdown))
        timespent.select_by_index(1)
        time.sleep(2)
        markers = self.driver.find_elements(By.CLASS_NAME, Data.dots)
        total_markers = len(markers) - 1
        legends = self.driver.find_elements(By.CLASS_NAME, Data.legends)
        for i in range(5):
            cards = self.driver.find_element(By.ID, Data.legend_button + i)
            cards.click()
            time.sleep(2)
            if 'No data found' in self.driver.page_source:
                print(legends.text, "selected legend card does not having markers and showing no data found")
                continue
            else:
                print("Legend cards are working as expected ")
                sum = sum + total_markers
                self.driver.find_element(By.ID, Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + self.fname.tpd_content_plays_file
                if os.path.isfile(self.filename) != False:
                    print(self.fname.tpd_content_plays_file, 'is not downloaded ')
                    count = count + 1
                else:
                    df = pd.read_csv(self.filename)
                    size = len(df)
                    if size != total_markers:
                        print(
                            'Total markers present in screen is not equivalent to no of records in the downloaded csv file')
                        count = count + 1
                    else:
                        print(
                            'Total markers present in screen is equivalent to no of records in the downloaded csv file')

        if total_markers != sum:
            print("No of Markers is Not Equal to sum of each legend score markers")
            count = count + 1
        return count

    def check_total_time_spent_legendcard(self):
        count = 0
        sum = 0
        self.data.click_on_state(self.driver)
        timespent = Select(self.driver.find_element(By.ID, Data.time_spent_Dropdown))
        timespent.select_by_index(2)
        time.sleep(2)
        markers = self.driver.find_elements(By.CLASS_NAME, Data.dots)
        total_markers = len(markers)-1
        legends = self.driver.find_elements(By.CLASS_NAME, Data.legends)
        for i in range(5):
            cards = self.driver.find_element(By.ID, Data.legend_button+i)
            cards.click()
            time.sleep(2)
            if 'No data found' in self.driver.page_source:
                print(legends.text, "selected legend card does not having markers and showing no data found")
                continue
            else:
                print("Legend cards are working as expected ")
                sum = sum + total_markers
                self.driver.find_element(By.ID, Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + self.fname.tpd_time_spent_file
                if os.path.isfile(self.filename) != False:
                    print(self.fname.tpd_time_spent_file, 'is not downloaded ')
                    count = count + 1
                else:
                    df = pd.read_csv(self.filename)
                    size = len(df)
                    if size != total_markers:
                        print('Total markers present in screen is not equivalent to no of records in the downloaded csv file')
                        count = count + 1
                    else:
                        print('Total markers present in screen is equivalent to no of records in the downloaded csv file')

        if total_markers != sum:
            print("No of Markers is Not Equal to sum of each legend score markers")
            count = count + 1
        return count

    def check_averaage_timespent_legendcard(self):
        count = 0
        sum = 0
        self.data.click_on_state(self.driver)
        timespent = Select(self.driver.find_element(By.ID, Data.time_spent_Dropdown))
        timespent.select_by_index(2)
        time.sleep(3)
        markers = self.driver.find_elements(By.CLASS_NAME, Data.dots)
        total_markers = len(markers)-1
        legends = self.driver.find_elements(By.CLASS_NAME, Data.legends)
        for i in range(5):
            cards = self.driver.find_element(By.ID, Data.legend_button+i)
            cards.click()
            time.sleep(2)
            if 'No data found' in self.driver.page_source:
                print(legends.text, "selected legend card does not having markers and showing no data found")
                continue
            else:
                print("Legend cards are working as expected ")
                sum = sum + total_markers
                self.driver.find_element(By.ID, Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + self.fname.tpd_average_time_spent_file
                if os.path.isfile(self.filename) != False:
                    print(self.fname.tpd_average_time_spent_file, 'is not downloaded ')
                    count = count + 1
                else:
                    df = pd.read_csv(self.filename)
                    size = len(df)
                    if size != total_markers:
                        print('Total markers present in screen is not equivalent to no of records in the downloaded csv file')
                        count = count + 1
                    else:
                        print('Total markers present in screen is equivalent to no of records in the downloaded csv file')

        if total_markers != sum:
            print("No of Markers is Not Equal to sum of each legend score markers")
            count = count + 1
        return count


    def check_logout_from_the_report(self):
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
             self.data.navigate_to_gps_of_learning_tpd()
             if 'tpd-total-content-plays' in self.driver.current_url:
                 print("Content Plays Map report home page is displayed ")
             else:
                 print("Navigation to Content Plays Map Report is failed !")
                 count = count + 1
        return count

    def check_total_content_plays_records(self):
        count = 0
        self.p = pwd()
        self.msg = file_extention()
        self.fname = Files()
        self.data.click_on_state(self.driver)
        timespent = Select(self.driver.find_element(By.ID, Data.time_spent_Dropdown))
        timespent.select_by_index(1)
        time.sleep(2)
        markers = self.driver.find_elements(By.CLASS_NAME, Data.dots)
        if len(markers) - 1 == 0 or 'No data found' in self.driver.page_source:
                print("markers are not displayed and showing no data found")
                count = count + 1
        else:
            self.driver.find_element(By.ID,Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + self.fname.tpd_content_plays_file
            if os.path.isfile(self.filename) != False:
                print(self.fname.tpd_content_plays_file,'is not downloaded ')
                count = count + 1
            else:
                df = pd.read_csv(self.filename)
                size = len(df)
                content_plays = df['Total Content Plays'].sum()
                time_spent = df['Total Time Spent'].sum()
                avg_time = df['Avg Time Spent'].sum() / size
                total_cp = self.driver.find_element(By.ID,Data.content_plays).text
                total_ts= self.driver.find_element(By.ID,Data.time_spent).text
                avg_spent=self.driver.find_element(By.ID,avg_time).text

                total_cp = re.sub('\D',"",total_cp)
                total_ts = re.sub('\D',"",total_ts)
                avg_spent = re.sub('\D',"",avg_spent)

                if total_cp != content_plays:
                    print("Total content plays is not matching with footer information",total_cp,content_plays)
                    count = count + 1
                else:
                    print(total_cp,content_plays,'are matching with footer information')

                if time_spent != total_ts:
                    print("Total content plays is not matching with footer information",time_spent,total_ts)
                    count = count + 1
                else:
                    print(time_spent,total_ts,'are matching with footer information')

                if avg_spent != avg_time:
                    print("Total content plays is not matching with footer information",avg_spent,avg_time)
                    count = count + 1
                else:
                    print(avg_spent,avg_time,'are matching with footer information')
        return count

    def check_total_timespent_plays_records(self):
        count = 0
        self.p = pwd()
        self.msg = file_extention()
        self.fname = Files()
        self.data.click_on_state(self.driver)
        timespent = Select(self.driver.find_element(By.ID, Data.time_spent_Dropdown))
        timespent.select_by_index(2)
        time.sleep(2)
        markers = self.driver.find_elements(By.CLASS_NAME, Data.dots)
        if len(markers) - 1 == 0 or 'No data found' in self.driver.page_source:
                print("markers are not displayed and showing no data found")
                count = count + 1
        else:
            self.driver.find_element(By.ID,Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + self.fname.tpd_time_spent_file
            if os.path.isfile(self.filename) != False:
                print(self.fname.tpd_content_plays_file,'is not downloaded ')
                count = count + 1
            else:
                df = pd.read_csv(self.filename)
                size = len(df)
                content_plays = df['Total Content Plays'].sum()
                time_spent = df['Total Time Spent'].sum()
                avg_time = df['Avg Time Spent'].sum() / size

                total_cp = self.driver.find_element(By.ID,Data.content_plays).text
                total_ts= self.driver.find_element(By.ID,Data.time_spent).text
                avg_spent=self.driver.find_element(By.ID,avg_time).text

                total_cp = re.sub('\D',"",total_cp)
                total_ts = re.sub('\D',"",total_ts)
                avg_spent = re.sub('\D',"",avg_spent)

                if total_cp != content_plays:
                    print("Total content plays is not matching with footer information",total_cp,content_plays)
                    count = count + 1
                else:
                    print(total_cp,content_plays,'are matching with footer information')

                if time_spent != total_ts:
                    print("Total content plays is not matching with footer information",time_spent,total_ts)
                    count = count + 1
                else:
                    print(time_spent,total_ts,'are matching with footer information')

                if avg_spent != avg_time:
                    print("Total content plays is not matching with footer information",avg_spent,avg_time)
                    count = count + 1
                else:
                    print(avg_spent,avg_time,'are matching with footer information')
        return count

    def check_average_time_records(self):
        count = 0
        self.p = pwd()
        self.msg = file_extention()
        self.fname = Files()
        self.data.click_on_state(self.driver)
        timespent = Select(self.driver.find_element(By.ID, Data.time_spent_Dropdown))
        timespent.select_by_index(3)
        time.sleep(2)
        markers = self.driver.find_elements(By.CLASS_NAME, Data.dots)
        if len(markers) - 1 == 0 or 'No data found' in self.driver.page_source:
                print("markers are not displayed and showing no data found")
                count = count + 1
        else:
            self.driver.find_element(By.ID,Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + self.fname.tpd_average_time_spent_file
            if os.path.isfile(self.filename) != False:
                print(self.fname.tpd_content_plays_file,'is not downloaded ')
                count = count + 1
            else:
                df = pd.read_csv(self.filename)
                size = len(df)
                content_plays = df['Total Content Plays'].sum()
                time_spent = df['Total Time Spent'].sum()
                avg_time = df['Avg Time Spent'].sum() / size
                total_cp = self.driver.find_element(By.ID,Data.content_plays).text
                total_ts= self.driver.find_element(By.ID,Data.time_spent).text
                avg_spent=self.driver.find_element(By.ID,avg_time).text

                total_cp = re.sub('\D',"",total_cp)
                total_ts = re.sub('\D',"",total_ts)
                avg_spent = re.sub('\D',"",avg_spent)

                if total_cp != content_plays:
                    print("Total content plays is not matching with footer information",total_cp,content_plays)
                    count = count + 1
                else:
                    print(total_cp,content_plays,'are matching with footer information')

                if time_spent != total_ts:
                    print("Total content plays is not matching with footer information",time_spent,total_ts)
                    count = count + 1
                else:
                    print(time_spent,total_ts,'are matching with footer information')

                if avg_spent != avg_time:
                    print("Total content plays is not matching with footer information",avg_spent,avg_time)
                    count = count + 1
                else:
                    print(avg_spent,avg_time,'are matching with footer information')
        return count

