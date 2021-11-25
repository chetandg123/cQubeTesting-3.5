import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Locators.parameters import Data
from reuse_func import GetData


class etb_content_plays_map_report():
    def __init__(self,driver):
        self.driver = driver
        self.count = 0
        self.data = GetData()
    def check_navigation_from_dashboard(self):
        data = GetData()
        self.driver.find_element(By.XPATH,Data.hyper_link).click()
        data.page_loading(self.driver)
        self.driver.find_element(By.ID,Data.cQube_logo).click()
        data.navigate_to_etb_content_plays_report()
        if 'etb-total-content-plays' in self.driver.current_url:
            print("etb Content Plays report is displayed")
        else:
            print('etb Content Plays report is not displayed')
            self.count = self.count + 1
        return self.count

    def check_report_home_page(self):
        count = 0
        self.data.click_on_state(self.driver)
        self.driver.find_element(By.ID.Data.cQube_logo).click()
        time.sleep(1)
        self.data.navigate_to_etb_content_plays_report()
        if 'No data found' in self.driver.page_source:
            print("etb Content Plays Report is showing no data found!!!")
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
        timespent.select_by_index(2)
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

    def check_totalcontent_plays_legendcard(self):
        count = 0
        self.data.click_on_state(self.driver)
        timespent = Select(self.driver.find_element(By.ID, Data.time_spent_Dropdown))
        timespent.select_by_index(1)
        time.sleep(2)
        markers = self.driver.find_elements(By.CLASS_NAME, Data.dots)
        legends = self.driver.find_elements(By.CLASS_NAME, Data.legends)
        for i in range(len(legends) - 1):
            cards = self.driver.find_element(By.ID, i)
            cards.click()
            time.sleep(2)
            if len(markers) - 1 == 0 or 'No data found' in self.driver.page_source:
                print(legends.text, "selected legend card does not having markers and showing no data found")
                count = count + 1
            else:
                print("Legend cards are working as expected ")
        return count

    def check_totaltime_spent_legendcard(self):
        count = 0
        self.data.click_on_state(self.driver)
        timespent = Select(self.driver.find_element(By.ID, Data.time_spent_Dropdown))
        timespent.select_by_index(2)
        time.sleep(2)
        markers = self.driver.find_elements(By.CLASS_NAME, Data.dots)
        legends = self.driver.find_elements(By.CLASS_NAME, Data.legends)
        for i in range(len(legends) - 1):
            cards = self.driver.find_element(By.ID, i)
            cards.click()
            time.sleep(2)
            if len(markers) - 1 == 0 or 'No data found' in self.driver.page_source:
                print(legends.text, "selected legend card does not having markers and showing no data found")
                count = count + 1
            else:
                print("Legend cards are working as expected ")
        return count

    def check_average_time_legendcard(self):
        count = 0
        self.data.click_on_state(self.driver)
        timespent = Select(self.driver.find_element(By.ID, Data.time_spent_Dropdown))
        timespent.select_by_index(3)
        time.sleep(2)
        markers = self.driver.find_elements(By.CLASS_NAME, Data.dots)
        legends = self.driver.find_elements(By.CLASS_NAME, Data.legends)
        for i in range(len(legends) - 1):
            cards = self.driver.find_element(By.ID, i)
            cards.click()
            time.sleep(2)
            if len(markers) - 1 == 0 or 'No data found' in self.driver.page_source:
                print(legends.text, "selected legend card does not having markers and showing no data found")
                count = count + 1
            else:
                print("Legend cards are working as expected ")
        return count

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
             self.data.navigate_to_etb_content_plays_report()
             if 'etb-total-content-plays' in self.driver.current_url:
                 print("Content Plays Map report home page is displayed ")
             else:
                 print("Navigation to Content Plays Map Report is failed !")
                 count = count + 1
        return count
