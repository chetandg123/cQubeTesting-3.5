
import os
import re
import time
import pandas as pd
from Locators.parameters import Data
from files import Files
from get_dir import pwd
from reuse_func import GetData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class usage_per_capita_map():

    def __init__(self,driver):
        self.driver = driver
        self.data = GetData()
        self.p = pwd()
        self.fname = Files()

    def check_navigation_from_dashboard(self):
        data = GetData()
        self.driver.find_element(By.XPATH,Data.hyper_link).click()
        data.page_loading(self.driver)
        self.driver.find_element(By.ID,Data.cQube_logo).click()
        data.navigate_to_etb_usage_per_capita_report()
        if 'etb-per-capita' in self.driver.current_url:
            print("Usage Per Capita Report is displayed")
        else:
            print('Usage Per Capita  Report is not displayed')
            self.count = self.count + 1
        return self.count

    def check_report_home_page(self):
        count = 0
        self.data.click_on_state(self.driver)
        self.driver.find_element(By.ID,Data.cQube_logo).click()
        time.sleep(1)
        self.data.navigate_to_etb_content_plays_report()
        if 'No data found' in self.driver.page_source:
            print("Usage Per Capita is showing no data found!!!")
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
        for i in range(1,len(legends)-1):
            cards = self.driver.find_element(By.ID,i)
            cards.click()
            time.sleep(2)
            if len(markers)-1 == 0 or 'No data found' in self.driver.page_source:
                print(legends.text,"selected legend card does not having markers and showing no data found")
                count = count + 1
            else:
                print("Legend cards are working as expected ")
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
             self.data.navigate_to_etb_usage_per_capita_report()
             if 'etb-per-capita' in self.driver.current_url:
                 print("Usage Per Capita Report is displayed")
             else:
                 print('Usage Per Capita  Report is not displayed')
                 self.count = self.count + 1
        return count

    def check_with_upper_quartile_functionality(self):
        count = 0
        self.data.click_on_state(self.driver)
        markers = self.driver.find_elements(By.CLASS_NAME,Data.dots)
        total_markers = len(markers)-1
        upper_quartile = self.driver.find_element(By.ID,'0')
        upper_quartile.click()
        if 'No data found' in self.driver.page_source:
            print('Upper Quartile is showing no data found on screen')
            count = count + 1
        else:
            upper_marker = len(markers)-1
            rgb_legend =self.driver.find_element(By.ID,"0").value_of_css_property('background-color')
            rgb_markers = markers.value_of_css_property('background-color')
            if total_markers > upper_marker:
                print('Upper Quartile Markers are showing correct ')
            if rgb_legend != rgb_markers:
                print('Upper Quartile button background color and markers background color are not matching')
                count = count + 1
            return count

    def check_with_inter_quartile_functionality(self):
        count = 0
        self.data.click_on_state(self.driver)
        markers = self.driver.find_elements(By.CLASS_NAME,Data.dots)
        total_markers = len(markers)-1
        inter_quartile = self.driver.find_element(By.ID,'1')
        inter_quartile.click()
        if 'No data found' in self.driver.page_source:
            print('Inter Quartile is showing no data found on screen')
            count = count + 1
        else:
            inter_markers = len(markers)-1
            rgb_legend =self.driver.find_element(By.ID,'1').value_of_css_property('background-color')
            rgb_markers = markers.value_of_css_property('background-color')
            if total_markers > inter_markers:
                print('Inter Quartile Markers are showing correct ')
            if rgb_legend != rgb_markers:
                print('Inter Quartile button background color and markers background color are not matching')
                count = count + 1
        return count

    def check_with_bottom_quartile_functionality(self):
        count = 0
        self.data.click_on_state(self.driver)
        markers = self.driver.find_elements(By.CLASS_NAME,Data.dots)
        total_markers = len(markers)-1
        bottom_quartile = self.driver.find_element(By.ID,'2')
        bottom_quartile.click()
        if 'No data found' in self.driver.page_source:
            print('Bottom Quartile is showing no data found on screen')
            count = count + 1
        else:
            bottom_markers = len(markers)-1
            rgb_legend =self.driver.find_element(By.ID,'1').value_of_css_property('background-color')
            rgb_markers = markers.value_of_css_property('background-color')
            if total_markers > bottom_markers:
                print('Bottom Quartile Markers are showing correct ')
            if rgb_legend != rgb_markers:
                print('Bottom Quartile button background color and markers background color are not matching')
                count = count + 1
        return count

    def check_download_functionality_with_upper_quartile(self):
        count = 0
        self.data.click_on_state(self.driver)
        markers = self.driver.find_elements(By.CLASS_NAME,Data.dots)
        total_markers = len(markers)-1
        upper_quartile = self.driver.find_element(By.ID,'0')
        upper_quartile.click()
        if 'No data found' in self.driver.page_source:
            print('Upper Quartile is showing no data found on screen')
            count = count + 1
        else:
            self.driver.find_element(By.ID,Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + '/' + self.fname.etb_per_capita_statewise
            if os.path.isfile(self.filename) != True:
                print('upper quartile file is not downloaded')
                count = count + 1
            else:
                print(self.filename, 'upper quartile file is downlaoded')
                df = pd.read_csv(self.filename)
                size = len(df)
                if int(len(markers)-1) != int(size):
                    print('Total no of markers information is not present in downloaded csv file',len(markers)-1,size)
                    count = count + 1
        return count

    def check_download_functionality_with_inter_quartile(self):
        count = 0
        self.data.click_on_state(self.driver)
        markers = self.driver.find_elements(By.CLASS_NAME,Data.dots)
        total_markers = len(markers)-1
        inter_quartile = self.driver.find_element(By.ID,'1')
        inter_quartile.click()
        if 'No data found' in self.driver.page_source:
            print('Inter Quartile is showing no data found on screen')
            count = count + 1
        else:
            self.driver.find_element(By.ID,Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + '/' + self.fname.etb_per_capita_statewise
            if os.path.isfile(self.filename) != True:
                print('Inter quartile file is not downloaded')
                count = count + 1
            else:
                print(self.filename, 'Inter quartile file is downlaoded')
                df = pd.read_csv(self.filename)
                size = len(df)
                if int(len(markers)-1) != int(size):
                    print('Total no of markers information is not present in downloaded csv file',len(markers)-1,size)
                    count = count + 1
        return count

    def check_download_functionality_with_bottom_quartile(self):
        count = 0
        self.data.click_on_state(self.driver)
        markers = self.driver.find_elements(By.CLASS_NAME,Data.dots)
        total_markers = len(markers)-1
        bottom_quartile = self.driver.find_element(By.ID,'2')
        bottom_quartile.click()
        if 'No data found' in self.driver.page_source:
            print('Bottom Quartile is showing no data found on screen')
            count = count + 1
        else:
            self.driver.find_element(By.ID,Data.Download).click()
            time.sleep(3)
            self.filename = self.p.get_download_dir() + '/' + self.fname.etb_per_capita_statewise
            if os.path.isfile(self.filename) != True:
                print('Bottom quartile file is not downloaded')
                count = count + 1
            else:
                print(self.filename, 'Bottom quartile file is downlaoded')
                df = pd.read_csv(self.filename)
                size = len(df)
                if int(len(markers)-1) != int(size):
                    print('Total no of markers information is not present in downloaded csv file',len(markers)-1,size)
                    count = count + 1
        return count

    def check_download_functionality_per_capita_over_quartile(self):
        count = 0
        self.data.click_on_state(self.driver)
        self.data.page_loading(self.driver)
        self.driver.find_element(By.ID,Data.Download).click()
        time.sleep(3)
        self.filename = self.p.get_download_dir() + '/' + self.fname.etb_per_capita_statewise
        if os.path.isfile(self.filename) != True:
            print('Statelevel overall Per Capita Report csv file is not downloaded ')
            count = count + 1
        else:
            df = pd.read_csv(self.filename)
            size = len(df)
            etb_exp_user = df['Expected Etb Users'].sum()
            etb_act_user = df['Actual Etb Users'].sum()
            content_plays = df['Total Content Plays'].sum()
            play_per_capita = df['Plays Per Capita'].sum() / size
            play_per_capita = round(play_per_capita)

            exp_user = self.driver.find_element(By.ID,Data.etb_exp_usr).text
            act_user = self.driver.find_element(By.ID,Data.etb_act_usr).text
            plays = self.driver.find_element(By.ID,Data.etb_play_capita).text

            exp_user = re.sub('\D','',exp_user)
            act_user = re.sub('\D','',act_user)
            plays = re.sub('\D','',plays)

            if etb_exp_user !=exp_user:
                print('Expected ETB Users value in file and footer value are not matching',etb_exp_user,exp_user)
                count = count + 1
            if etb_act_user != act_user:
                print('Actual ETB Users value in file and footer value are not matching', etb_act_user, act_user)
                count = count + 1
            if plays != play_per_capita:
                print('Plays per capita value file and footer value are not matching',plays,play_per_capita)
                count = count + 1
        return count




