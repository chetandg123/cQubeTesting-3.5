import os
import re
import time
from unittest import skip

import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Locators.parameters import Data
from filenames import file_extention
from files import Files
from get_dir import pwd
from reuse_func import GetData

'''Script developed to test the each functionalities of web element like buttons , charts , dropdowns , map and markers 
etc '''


class Tpd_Content_Plays_Map_Report():
    def __init__(self, driver):
        self.driver = driver
        self.count = 0
        self.data = GetData()
        self.p = pwd()

    def check_navigation_from_dashboard(self):
        data = GetData()
        self.driver.find_element(By.XPATH, Data.hyper_link).click()
        data.page_loading(self.driver)
        self.driver.find_element(By.ID, Data.cQube_logo).click()
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
        self.driver.find_element(By.ID, Data.cQube_logo).click()
        time.sleep(1)
        self.data.navigate_to_gps_of_learning_tpd()
        if 'No data found' in self.driver.page_source:
            print("GPS of Learning- TPD Report is showing no data found!!!")
            count = count + 1
        else:
            markers = self.driver.find_elements(By.CLASS_NAME, Data.dots)
            values = len(markers) - 1

        return count

    def check_choose_type_dropdown(self):
        self.data.click_on_state(self.driver)
        timespent = Select(self.driver.find_element(By.ID, Data.time_spent_Dropdown))
        options = len(timespent.options) - 1
        return options

    def check_selection_of_options(self):
        self.data.click_on_state(self.driver)
        timespent = Select(self.driver.find_element(By.ID, Data.time_spent_Dropdown))
        spents = len(timespent.options) - 1
        for i in range(1, spents):
            timespent.select_by_index(i)
            time.sleep(2)
            print(timespent.options[i].text, 'is selected and displayed on markers...')

    def check_hyperlink_functionality(self):
        count = 0
        self.data.click_on_state(self.driver)
        timespent = Select(self.driver.find_element(By.ID, Data.time_spent_Dropdown))
        timespent.select_by_index(1)
        time.sleep(2)
        option_name = timespent.options[1].text
        print(option_name)
        self.driver.find_element(By.XPATH, Data.hyper_link).click()
        time.sleep(2)
        if " Total Time Spent  " in self.driver.page_source:
            print("Hyper link text is refreshed to home page..")
        else:
            print("Hyper link is not working...")
            count = count + 1
        return count

    def check_legend_card_functionality(self):
        count = 0
        self.data.click_on_state(self.driver)
        markers = self.driver.find_elements(By.CLASS_NAME, Data.dots)
        legends = self.driver.find_elements(By.CLASS_NAME, Data.legends)
        for i in range(1, len(legends) - 3):
            cards = self.driver.find_element(By.ID, i)
            cards.click()
            time.sleep(2)
            if len(markers) - 1 == 0 or 'No data found' in self.driver.page_source:
                print(i, "selected legend card does not having markers and showing no data found")
                # count = count + 1
            else:
                print(i, "Legend cards are working as expected ")
        return count

    def check_total_content_plays_legendcard(self):
        count = 0
        sum = 0
        self.fname = Files()
        self.data.click_on_state(self.driver)
        timespent = Select(self.driver.find_element(By.ID, Data.time_spent_Dropdown))
        timespent.select_by_index(1)
        print(timespent.options[1].text, 'is selected')
        time.sleep(2)
        markers = self.driver.find_elements(By.CLASS_NAME, Data.dots)
        tot_markers = len(markers) - 1
        legends = self.driver.find_elements(By.CLASS_NAME, Data.legends)
        for i in range(len(legends) - 3):
            cards = self.driver.find_element(By.ID, str(i))
            cards.click()
            time.sleep(2)
            if 'No data found' in self.driver.page_source:
                print(i, "selected legend card does not having markers and showing no data found")
            else:
                print(i, "Legend cards are working as expected ")
                markers = self.driver.find_elements(By.CLASS_NAME, Data.dots)
                total_markers = len(markers) - 1
                sum = sum + total_markers
                self.driver.find_element(By.ID, Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + '/' + self.fname.tpd_content_plays_file
                if os.path.isfile(self.filename) != True:
                    print(self.fname.tpd_content_plays_file, 'is not downloaded ')
                    count = count + 1
                else:
                    df = pd.read_csv(self.filename)
                    size = len(df)
                    if size != total_markers:
                        print(
                            size, total_markers,
                            'Total markers present in screen is not equivalent to no of records in the downloaded csv file')
                        count = count + 1
                    else:
                        print(
                            size, total_markers,
                            'Total markers present in screen is equivalent to no of records in the downloaded csv file')

        if tot_markers != sum:
            print(tot_markers, sum, "No of Markers is Not Equal to sum of each legend score markers")
            count = count + 1
        else:
            print("Total no of markers is equal to sum of each legend card ")
        os.remove(self.filename)
        return count

    def check_total_time_spent_legendcard(self):
        count = 0
        0
        self.fname = Files()
        self.data.click_on_state(self.driver)
        timespent = Select(self.driver.find_element(By.ID, Data.time_spent_Dropdown))
        timespent.select_by_index(2)
        time.sleep(2)
        markers = self.driver.find_elements(By.CLASS_NAME, Data.dots)
        tot_markers = len(markers) - 1
        legends = self.driver.find_elements(By.CLASS_NAME, Data.legends)
        for i in range(len(legends) - 3):
            cards = self.driver.find_element(By.ID, str(i))
            cards.click()
            time.sleep(3)
            if 'No data found' in self.driver.page_source:
                print(i, "selected legend card does not having markers and showing no data found")
                skip("no data found")
            else:
                print(i, "is legend card button is clicked")
        #         markers = self.driver.find_elements(By.CLASS_NAME, Data.dots)
        #         total_markers = len(markers) - 1
        #         sum = sum + total_markers
        #         self.driver.find_element(By.ID, Data.Download).click()
        #         time.sleep(3)
        #         self.filename = self.p.get_download_dir() + '/' + self.fname.tpd_time_spent_file
        #         if os.path.isfile(self.filename) != True:
        #             print(self.fname.tpd_time_spent_file, 'is not downloaded ')
        #             count = count + 1
        #         else:
        #             df = pd.read_csv(self.filename)
        #             size = len(df)
        #             if size != total_markers:
        #                 print(size,total_markers,'Total markers present in screen is not equivalent to no of records in the downloaded csv file')
        #                 count = count + 1
        #             else:
        #                 print(size,total_markers,'Total markers present in screen is equivalent to no of records in the downloaded csv file')
        #
        # if tot_markers != sum:
        #     print(tot_markers,sum,"No of Markers is Not Equal to sum of each legend score markers")
        #     count = count + 1
        # else:
        #      print("Total no of markers is equal to sum of each legend card ")
        # os.remove(self.filename)
        return count

    def check_averaage_timespent_legendcard(self):
        count = 0
        sum = 0
        self.fname = Files()
        self.data.click_on_state(self.driver)
        timespent = Select(self.driver.find_element(By.ID, Data.time_spent_Dropdown))
        timespent.select_by_index(3)
        time.sleep(3)
        markers = self.driver.find_elements(By.CLASS_NAME, Data.dots)
        tot_markers = len(markers) - 1
        legends = self.driver.find_elements(By.CLASS_NAME, Data.legends)
        for i in range(len(legends) - 3):
            self.p = pwd()
            cards = self.driver.find_element(By.ID, str(i))
            cards.click()
            time.sleep(3)
            if 'No data found' in self.driver.page_source:
                print(i, "selected legend card does not having markers and showing no data found")
            else:
                markers = self.driver.find_elements(By.CLASS_NAME, Data.dots)
                total_markers = len(markers) - 1
                sum = sum + total_markers
                self.driver.find_element(By.ID, Data.Download).click()
                time.sleep(3)
                self.filename = self.p.get_download_dir() + '/' + self.fname.tpd_average_time_spent_file
                if os.path.isfile(self.filename) != True:
                    print(self.fname.tpd_time_spent_file, 'is not downloaded ')
                    count = count + 1
                else:
                    df = pd.read_csv(self.filename)
                    size = len(df)
                    if size != total_markers:
                        print(size, total_markers,
                              'Total markers present in screen is not equivalent to no of records in the downloaded csv file')
                        count = count + 1
        if tot_markers != sum:
            print(tot_markers, sum, "No of Markers is Not Equal to sum of each legend score markers")
            count = count + 1
        else:
            print("Total no of markers is equal to sum of each legend card ")
        os.remove(self.filename)
        return count

    def check_logout_from_the_report(self):
        count = 0
        self.data.click_on_state(self.driver)
        self.driver.find_element(By.ID, Data.cQube_logo).click()
        time.sleep(1)
        self.driver.find_element(By.ID, Data.logout).click()
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
            self.driver.find_element(By.ID, Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + '/' + self.fname.tpd_content_plays_file
            if os.path.isfile(self.filename) != True:
                print(self.fname.tpd_content_plays_file, 'is not downloaded ')
                count = count + 1
            else:
                df = pd.read_csv(self.filename)
                size = len(df)
                content_plays = df['Total Content Plays'].sum()
                time_spent = df['Total Time Spent'].sum()
                avg_time = round(df['Avg Time Spent'].sum() / size)

                total_cp = self.driver.find_element(By.ID, Data.content_plays).text
                total_ts = self.driver.find_element(By.ID, Data.time_spent).text
                avg_spent = self.driver.find_element(By.ID, avg_time).text

                total_cp = re.sub('\D', "", total_cp)
                total_ts = re.sub('\D', "", total_ts)
                avg_spent = re.sub('\D', "", avg_spent)

                # outside
                t_contet_plays = self.driver.find_element(By.XPATH, Data.t_c_play).text
                t_t_spent = self.driver.find_element(By.XPATH, Data.t_t_spent).text
                t_a_spent = self.driver.find_element(By.XPATH, Data.t_a_spent).text

                tcp = re.sub('\D', "", t_contet_plays)
                tts = re.sub('\D', "", t_t_spent)
                tas = re.sub('\D', "", t_a_spent)

                tc = round(int(tcp) / 1000)

                if int(total_cp) != 0 and int(time_spent) != 0 and int(avg_spent) != 0:
                    print("Footer information is showing as expected")
                else:
                    print('Footer information is not provided in downloaded csv file')
                    count = count + 1
                # if int(total_cp) != int(content_plays+tcp):
                #     print("Total content plays is content plays not matching with footer information",total_cp,content_plays)
                #     count = count + 1
                # else:
                #     print(total_cp,content_plays,' content plays are matching with footer information')
                #
                # if  int(time_spent) != int(total_ts+tts):
                #     print("Total content plays is time spent not matching with footer information",time_spent,total_ts)
                #     count = count + 1
                # else:
                #     print(time_spent,total_ts, ' Time spent are matching with footer information')
                #
                # if int(avg_spent) != round(avg_time)+int(tas): print("Total content plays - Average time is not
                # matching with footer information",avg_spent,avg_time) count = count + 1 else: print(avg_spent,
                # avg_time,'Averages  are matching with footer information')
            os.remove(self.filename)
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
            self.driver.find_element(By.ID, Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + '/' + self.fname.tpd_time_spent_file
            if os.path.isfile(self.filename) != True:
                print(self.fname.tpd_content_plays_file, 'is not downloaded ')
                count = count + 1
            else:
                df = pd.read_csv(self.filename)
                size = len(df)
                content_plays = df['Total Content Plays'].sum()
                time_spent = df['Total Time Spent'].sum()
                avg_time = round(df['Avg Time Spent'].sum() / size)

                total_cp = self.driver.find_element(By.ID, Data.content_plays).text
                total_ts = self.driver.find_element(By.ID, Data.time_spent).text
                avg_spent = self.driver.find_element(By.ID, avg_time).text

                total_cp = re.sub('\D', "", total_cp)
                total_ts = re.sub('\D', "", total_ts)
                avg_spent = re.sub('\D', "", avg_spent)

                # outside
                t_contet_plays = self.driver.find_element(By.XPATH, Data.t_c_play).text
                t_t_spent = self.driver.find_element(By.XPATH, Data.t_t_spent).text
                t_a_spent = self.driver.find_element(By.XPATH, Data.t_a_spent).text

                tcp = re.sub('\D', "", t_contet_plays)
                tts = re.sub('\D', "", t_t_spent)
                tas = re.sub('\D', "", t_a_spent)

                round(int(tcp) / 1000)

                if int(total_cp) != 0 and int(time_spent) != 0 and int(avg_spent) != 0:
                    print("Footer information is showing as expected")
                else:
                    print('Footer information is not provided in downloaded csv file')
                    count = count + 1
                # if total_cp != content_plays:
                #     print("Total content plays is not matching with footer information",total_cp,content_plays)
                #     count = count + 1
                # else:
                #     print(total_cp,content_plays,'are matching with footer information')
                #
                # if time_spent != total_ts:
                #     print("Total content plays is not matching with footer information",time_spent,total_ts)
                #     count = count + 1
                # else:
                #     print(time_spent,total_ts,'are matching with footer information')
                #
                # if avg_spent != round(avg_time):
                #     print("Total content plays is not matching with footer information",avg_spent,avg_time)
                #     count = count + 1
                # else:
                #     print(avg_spent,round(avg_time),'are matching with footer information')
            os.remove(self.filename)
        return count

    def check_average_time_records(self):
        count = 0
        self.p = pwd()
        self.msg = file_extention()
        self.fname = Files()
        self.data.click_on_state(self.driver)
        timespent = Select(self.driver.find_element(By.ID, Data.time_spent_Dropdown))
        timespent.select_by_index(3)
        print(timespent.options[3].text)
        time.sleep(3)
        markers = self.driver.find_elements(By.CLASS_NAME, Data.dots)
        if len(markers) - 1 == 0 or 'No data found' in self.driver.page_source:
            print("markers are not displayed and showing no data found")
        else:
            self.driver.find_element(By.ID, Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + '/' + self.fname.tpd_average_time_spent_file
            if os.path.isfile(self.filename) != True:
                print(self.fname.tpd_content_plays_file, 'is not downloaded ')
                count = count + 1
            else:
                df = pd.read_csv(self.filename)
                size = len(df)
                content_plays = df['Total Content Plays'].sum()
                time_spent = df['Total Time Spent'].sum()
                avg_time = round(df['Avg Time Spent'].sum() / size)
                print(avg_time)
                total_cp = self.driver.find_element(By.ID, Data.content_plays).text
                total_ts = self.driver.find_element(By.ID, Data.time_spent).text
                avg_spent = self.driver.find_element(By.ID, avg_time).text

                total_cp = re.sub('\D', "", total_cp)
                total_ts = re.sub('\D', "", total_ts)
                avg_spent = re.sub('\D', "", avg_spent)

                # outside
                t_contet_plays = self.driver.find_element(By.XPATH, Data.t_c_play).text
                t_t_spent = self.driver.find_element(By.XPATH, Data.t_t_spent).text
                t_a_spent = self.driver.find_element(By.XPATH, Data.t_a_spent).text

                tcp = re.sub('\D', "", t_contet_plays)
                tts = re.sub('\D', "", t_t_spent)
                tas = re.sub('\D', "", t_a_spent)

                tc = round(int(tcp) / 1000)

                if int(total_cp) != 0 and int(time_spent) != 0 and int(avg_spent) != 0:
                    print("Footer information is showing as expected")
                else:
                    print('Footer information is not provided in downloaded csv file')
                    count = count + 1

                print(total_cp, total_ts, avg_spent)
                # if total_cp != content_plays:
                #     print("Total content plays is not matching with footer information",total_cp,content_plays)
                #     count = count + 1
                # else:
                #     print(total_cp,content_plays,'are matching with footer information')
                #
                # if time_spent != total_ts:
                #     print("Total content plays is not matching with footer information",time_spent,total_ts)
                #     count = count + 1
                # else:
                #     print(time_spent,total_ts,'are matching with footer information')
                #
                # if avg_spent != round(avg_time):
                #     print("Total content plays is not matching with footer information",avg_spent,avg_time)
                #     count = count + 1
                # else:
                #     print(avg_spent,round(avg_time),'are matching with footer information')
            os.remove(self.filename)
        return count
